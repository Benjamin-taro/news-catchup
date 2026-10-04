#!/usr/bin/env python3
"""週次の数字をまとめる：話題・キーワード・フィード別の成績と、👍/👎 の回帰分析。

入力：候補ログ（_system/news/candidates/*.jsonl）と Digest の 👍/👎
出力：
  - _system/news/stats/<週>.md   Weekly に載せる表（標準出力にも同じものを出す）
  - _system/news/model.json      回帰の係数。日次の採点が補正に使う

使い方：python3 scripts/weekly_stats.py [--date YYYY-MM-DD]（その日までの 7 日間を「今週」とする。省略時は今日）
依存：標準ライブラリのみ。
"""
import argparse
import datetime as dt
import json
import math
import re
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAND = ROOT / "_system/news/candidates"
DIGEST = ROOT / "Digest"
STATS = ROOT / "_system/news/stats"
MODEL = ROOT / "_system/news/model.json"
CONFIG = ROOT / "_system/matcha/config.yaml"

TOPIC_NAME = {
    "ai-work": "AI と開発者の働き方", "ai-enterprise": "AI の企業導入", "career": "FDE とエンジニアのキャリア",
    "bigtech": "大手テック企業の動き", "incident": "セキュリティ事故", "agent-infra": "AI エージェントの基盤と安全性",
    "llm": "LLM とモデル競争", "banking": "銀行業界と金融の構造", "legal-tech": "法務・コンプライアンスのテクノロジー",
    "autonomous": "自動運転", "stack": "開発スタック", "other": "その他の話題",
}
TYPE_NAME = {"opinion": "議論・意見", "release": "製品・発表", "incident": "事故・障害", "data": "調査・データ",
             "howto": "解説", "news": "報道", "social": "SNS", "promo": "宣伝"}
ITEM = re.compile(r"^## (\d+)\. ")
VOTE = re.compile(r"^[-*]\s*\[( |x|X)\]\s*(👍|👎)")


def read_votes(date):
    path, votes, rank = DIGEST / f"{date}.md", {}, None
    if not path.exists():
        return votes
    for line in path.read_text().split("\n"):
        h = ITEM.match(line)
        if h:
            rank = int(h.group(1))
            votes[rank] = None
        elif line.startswith("## "):
            rank = None
        elif rank is not None:
            v = VOTE.match(line)
            if v and v.group(1) != " ":
                votes[rank] = "up" if v.group(2) == "👍" else "down"
    return votes


def load_all():
    rows = []
    for path in sorted(CAND.glob("*.jsonl")):
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", path.stem):
            continue
        votes = read_votes(path.stem)
        for line in path.read_text().split("\n"):
            if not line.strip():
                continue
            try:
                r = json.loads(line)
            except ValueError:
                continue
            r["date"] = path.stem
            r["shown"] = r.get("status") in ("main", "explore")
            r["vote"] = votes.get(r.get("rank")) if r.get("rank") is not None else None
            rows.append(r)
    return rows


def unique_shown(rows):
    """1 つの Digest 項目に複数の記事をまとめた場合、項目単位で 1 件として数える。"""
    seen, out = set(), []
    for r in rows:
        if not r["shown"]:
            continue
        key = (r["date"], r.get("rank"))
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def table(headers, lines):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] + ["---:"] * (len(headers) - 1)) + "|"]
    out += ["| " + " | ".join(str(c) for c in line) + " |" for line in lines]
    return "\n".join(out)


def tally(rows, key_fn):
    """key ごとに 集めた件数・載った件数・👍・👎 を数える。"""
    stats = defaultdict(lambda: Counter())
    for r in rows:
        for k in key_fn(r):
            stats[k]["collected"] += 1
    for r in unique_shown(rows):
        for k in key_fn(r):
            s = stats[k]
            s["shown"] += 1
            if r["vote"] == "up":
                s["up"] += 1
            elif r["vote"] == "down":
                s["down"] += 1
    return stats


def verdict(s):
    up, down = s["up"], s["down"]
    if up + down < 2:
        return "–"
    if up >= 2 * max(down, 1) and up - down >= 2:
        return "好み"
    if down >= 2 * max(up, 1) and down - up >= 2:
        return "不評"
    return "割れている"


# ---- 回帰（L2 正則化つきロジスティック回帰。データが少ないので正則化を強めにする） ----
def features(r):
    f = [f"話題：{TOPIC_NAME.get(r.get('topic'), r.get('topic') or '不明')}",
         f"種類：{TYPE_NAME.get(r.get('type'), r.get('type') or '不明')}"]
    if r.get("feed") and r["feed"] != "不明":
        f.append(f"フィード：{r['feed']}")
    if r.get("lang"):
        f.append("言語：日本語" if r["lang"] == "ja" else "言語：英語")
    return f


def fit(X, y, names, l2=1.0, iters=3000, lr=0.3):
    w = {n: 0.0 for n in names}
    b = 0.0
    n = len(y)
    for _ in range(iters):
        gb, gw = 0.0, defaultdict(float)
        for xi, yi in zip(X, y):
            z = b + sum(w[f] for f in xi)
            p = 1 / (1 + math.exp(-max(-30, min(30, z))))
            d = p - yi
            gb += d
            for f in xi:
                gw[f] += d
        b -= lr * gb / n
        for f in names:
            w[f] -= lr * (gw[f] / n + l2 * w[f] / n)
    return b, w


def predict(b, w, xi):
    z = b + sum(w.get(f, 0.0) for f in xi)
    return 1 / (1 + math.exp(-max(-30, min(30, z))))


def regression(rows):
    labeled = [r for r in unique_shown(rows) if r["vote"] in ("up", "down")]
    if len(labeled) < 20:
        return None
    X = [features(r) for r in labeled]
    y = [1 if r["vote"] == "up" else 0 for r in labeled]
    count = Counter(f for xi in X for f in xi)
    names = sorted(f for f, c in count.items() if c >= 3)  # 3 件未満の特徴は使わない
    X = [[f for f in xi if f in names] for xi in X]
    b, w = fit(X, y, names)
    # 1 件抜き交差検証で、当てはまりではなく予測の精度を見る
    hit = 0
    for i in range(len(y)):
        bi, wi = fit(X[:i] + X[i + 1:], y[:i] + y[i + 1:], names, iters=800)
        hit += (predict(bi, wi, X[i]) >= 0.5) == (y[i] == 1)
    ups = sum(y)
    per = {f: Counter() for f in names}
    for xi, yi in zip(X, y):
        for f in xi:
            per[f]["up" if yi else "down"] += 1
    return {"n": len(y), "up": ups, "down": len(y) - ups, "intercept": b, "weights": w, "per": per,
            "loo_accuracy": hit / len(y), "baseline": max(ups, len(y) - ups) / len(y)}


def search_keywords():
    """config.yaml の Google News 検索キーワードを取り出す（引用符と when: を除いた検索語）。"""
    if not CONFIG.exists():
        return []
    out = []
    for line in CONFIG.read_text().split("\n"):
        m = re.match(r"^  - https://news\.google\.com/rss/search\?q=([^&\s]+)&", line)
        if not m or "site%3Ax.com" in m.group(1):
            continue
        q = urllib.parse.unquote(m.group(1))
        out.append(re.sub(r"\s*when:\d+d\s*", "", q).strip().strip('"'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    args = ap.parse_args()
    end = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    start = end - dt.timedelta(days=6)
    week = f"{end.isocalendar()[0]}-W{end.isocalendar()[1]:02d}"

    rows = load_all()
    this = [r for r in rows if start.isoformat() <= r["date"] <= end.isoformat()]
    prev = [r for r in rows if r["date"] < start.isoformat()]
    shown = unique_shown(this)
    has_dropped = any(not r["shown"] for r in this)
    out = [f"<!-- scripts/weekly_stats.py が生成（{start} 〜 {end}）。手で直さない -->", ""]

    # 1. 話題別
    t = tally(this, lambda r: [c for c in (r.get("topic"), r.get("topic2")) if c])
    lines = []
    for code, name in TOPIC_NAME.items():
        s = t.get(code, Counter())
        lines.append([name, s["collected"] if has_dropped else "–", s["shown"], s["up"], s["down"], verdict(s)])
    lines.sort(key=lambda x: -x[2])
    out += ["### 話題ごとの登場数と反応", "",
            table(["話題", "集まった記事", "Digest に載った", "👍", "👎", "反応"], lines), ""]
    if not has_dropped:
        out += ["※「集まった記事」は、落とした記事も記録するようになった週から出ます。", ""]

    # 2. キーワード
    k = tally(this, lambda r: r.get("terms") or [])
    hot = sorted(k.items(), key=lambda kv: (-kv[1]["shown"], -kv[1]["up"]))[:12]
    out += ["### 今週よく出たキーワード", "",
            table(["キーワード", "Digest に載った", "👍", "👎", "反応"],
                  [[name, s["shown"], s["up"], s["down"], verdict(s)] for name, s in hot]), ""]

    # 3. あまり出なかったもの
    cold = [name for code, name in TOPIC_NAME.items() if t.get(code, Counter())["shown"] <= 1 and code != "other"]
    prev_terms = Counter(x for r in unique_shown(prev) for x in (r.get("terms") or []))
    gone = [x for x, c in prev_terms.most_common() if c >= 2 and x not in k][:8]
    kw = tally(this, lambda r: [r["keyword"]] if r.get("feed") == "Google News" and r.get("keyword") else [])
    dead_kw = [x for x in search_keywords() if kw.get(x, Counter())["shown"] == 0] if has_dropped else []
    out += ["### あまり出てこなかったもの", ""]
    out += [f"- **載った記事が 1 件以下の話題**：{'、'.join(cold) if cold else 'なし'}"]
    out += [f"- **先週までは出ていたのに、今週は出なかったキーワード**：{'、'.join(gone) if gone else 'なし（比べる過去の週がまだない）' if not prev else 'なし'}"]
    if has_dropped:
        out += [f"- **1 件も Digest に載らなかった検索キーワード**：{'、'.join(dead_kw) if dead_kw else 'なし'}"]
    out += [""]

    # 4. フィード別
    f = tally(this, lambda r: [r.get("feed") or "不明"])
    lines = [[name, s["collected"] if has_dropped else "–", s["shown"], s["up"], s["down"], verdict(s)]
             for name, s in sorted(f.items(), key=lambda kv: -kv[1]["shown"])]
    out += ["### フィードごとの成績", "", table(["フィード", "集めた", "Digest に載った", "👍", "👎", "反応"], lines), ""]
    if has_dropped:
        lines = [[name, s["collected"], s["shown"], s["up"], s["down"]] for name, s in sorted(kw.items(), key=lambda kv: -kv[1]["shown"])]
        if lines:
            out += ["### 検索キーワードごとの成績（Google News）", "", table(["キーワード", "集めた", "Digest に載った", "👍", "👎"], lines), ""]

    # 5. 回帰
    reg = regression(rows)
    out += ["### 👍/👎 の回帰分析（これまでの全期間）", ""]
    if reg is None:
        out += ["評価がまだ 20 件に届かないので、回帰は行っていません。", ""]
    else:
        ws = sorted(reg["weights"].items(), key=lambda kv: -kv[1])
        lines = [[name, f"{w:+.2f}", reg["per"][name]["up"], reg["per"][name]["down"],
                  "👍 寄り" if w > 0.25 else "👎 寄り" if w < -0.25 else "中立"] for name, w in ws]
        out += [f"評価 {reg['n']} 件（👍 {reg['up']} / 👎 {reg['down']}）を、話題・種類・フィード・言語で説明するロジスティック回帰。"
                "係数がプラスなら 👍 が付きやすく、マイナスなら 👎 が付きやすい特徴です。", "",
                table(["特徴", "係数", "👍", "👎", "傾向"], lines), "",
                f"- **予測の当たり具合**：1 件ずつ抜いて予測する検証で {reg['loo_accuracy']:.0%}"
                f"（何も考えず多いほうを答えた場合は {reg['baseline']:.0%}）。",
                "- 件数が少ない特徴の係数は、数件の評価で大きく動きます。件数（👍・👎 の列）と一緒に読んでください。", ""]
        MODEL.write_text(json.dumps({
            "updated": end.isoformat(), "n": reg["n"], "loo_accuracy": round(reg["loo_accuracy"], 3),
            "baseline": round(reg["baseline"], 3), "intercept": round(reg["intercept"], 3),
            "weights": {name: {"coef": round(w, 3), "up": reg["per"][name]["up"], "down": reg["per"][name]["down"]} for name, w in ws},
        }, ensure_ascii=False, indent=1) + "\n")

    text = "\n".join(out)
    STATS.mkdir(parents=True, exist_ok=True)
    (STATS / f"{week}.md").write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
