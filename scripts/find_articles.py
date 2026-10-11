#!/usr/bin/env python3
"""問いやキーワードに関係する記事を、候補ログ・Digest・wiki から横断して引く。

Claude と会話するときの検索の補助。候補ログは原題（英語が多い）、terms は日本語、Digest は日本語の要約と
言語がばらけているので、まとめて検索する。出力は Markdown（そのまま会話に貼れる）。

使い方：
  python3 scripts/find_articles.py FDE 資格 certification        # どれかに当たれば出す（OR）
  python3 scripts/find_articles.py --and AI レビュー               # 全部に当たるものだけ（AND）
  python3 scripts/find_articles.py --topic career --days 28        # 話題コードで絞る（候補ログの topic / topic2）
  python3 scripts/find_articles.py 銀行 --shown                    # Digest に載ったものだけ
  python3 scripts/find_articles.py 銀行 --days 0                   # 全期間（既定は直近 28 日）
  python3 scripts/find_articles.py --terms                         # terms の一覧と件数（検索語を決めるときに）

検索対象：原題、terms、topic、keyword、publisher、entities、Digest の見出し・一言で・So what。
依存：標準ライブラリのみ。
"""
import argparse
import datetime as dt
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAND = ROOT / "_system/news/candidates"
DIGEST = ROOT / "Digest"
ARTICLES = ROOT / "wiki/articles"
SITE = "https://benjamin-taro.github.io/news-catchup"

ITEM = re.compile(r"^## (\d+)\. (.*)")
VOTE = re.compile(r"^[-*]\s*\[( |x|X)\]\s*(👍|👎)")
LABEL = re.compile(r"^\*\*(一言で|So what)\*\*\s*[：:]\s*(.*)$", re.I)
STATUS = {"main": "本編", "explore": "Explore", "stack": "Stack", "dropped": "不採用"}


def read_digest(date):
    """{rank: {title, summary, sowhat, vote}} を返す。"""
    path = DIGEST / f"{date}.md"
    items, rank = {}, None
    if not path.exists():
        return items
    for line in path.read_text(encoding="utf-8").split("\n"):
        h = ITEM.match(line)
        if h:
            rank = int(h.group(1))
            items[rank] = {"title": h.group(2).strip(), "summary": "", "sowhat": "", "vote": ""}
            continue
        if line.startswith("## "):
            rank = None
            continue
        if rank is None:
            continue
        m = LABEL.match(line.strip())
        if m:
            items[rank]["summary" if m.group(1) == "一言で" else "sowhat"] = m.group(2)
            continue
        v = VOTE.match(line.strip())
        if v and v.group(1) != " ":
            items[rank]["vote"] = v.group(2)
    return items


def wiki_notes():
    """{(date, rank): ノート名}"""
    notes = {}
    if ARTICLES.exists():
        for p in ARTICLES.glob("*.md"):
            m = re.match(r"(\d{4}-\d{2}-\d{2})-(\d{2}) ", p.name)
            if m:
                notes[(m.group(1), int(m.group(2)))] = p.stem
    return notes


def load(days):
    rows, digests = [], {}
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat() if days else ""
    for path in sorted(CAND.glob("*.jsonl")):
        date = path.stem
        if date < since:
            continue
        digests[date] = read_digest(date)
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            r["date"] = date
            d = digests[date].get(r.get("rank")) if r.get("rank") else None
            r["digest"] = d or {}
            rows.append(r)
    return rows


def haystack(r):
    parts = [r.get("title", ""), " ".join(r.get("terms") or []), r.get("topic", ""), r.get("topic2", ""),
             r.get("keyword", ""), r.get("publisher", ""),
             " ".join(e.get("name", "") for e in (r.get("entities") or []) if isinstance(e, dict))]
    d = r.get("digest") or {}
    parts += [d.get("title", ""), d.get("summary", ""), d.get("sowhat", "")]
    return " ".join(parts).lower()


def matches(r, queries, use_and):
    h = haystack(r)
    hits = [q for q in queries if q.lower() in h]
    return (len(hits) == len(queries)) if use_and else bool(hits)


def fmt(r, notes):
    d = r.get("digest") or {}
    status = STATUS.get(r.get("status"), r.get("status") or "")
    shown = r.get("status") in ("main", "explore")
    head = d.get("title") or r.get("title", "")
    line = f"- **{r['date']}**"
    if shown:
        line += f" #{r['rank']}"
    line += f"（{status}"
    if r.get("score") is not None:
        line += f"・{r['score']}点"
    if d.get("vote"):
        line += f"・{d['vote']}"
    line += f"）{head}"
    out = [line]
    if shown and d.get("title") and d["title"] != r.get("title"):
        out.append(f"  - 原題：{r.get('title', '')}")
    if d.get("summary"):
        out.append(f"  - 一言で：{d['summary']}")
    if d.get("sowhat"):
        out.append(f"  - So what：{d['sowhat']}")
    meta = []
    if r.get("terms"):
        meta.append("terms: " + "、".join(r["terms"]))
    if r.get("topic"):
        meta.append("topic: " + "/".join(t for t in (r.get("topic"), r.get("topic2")) if t))
    if r.get("feed"):
        meta.append("feed: " + r["feed"] + (f"（{r['publisher']}）" if r.get("publisher") else ""))
    if meta:
        out.append("  - " + " ｜ ".join(meta))
    links = [f"[元記事]({r.get('url', '')})"]
    if shown:
        links.append(f"[Digest]({SITE}/{r['date']}.html#item-{r['rank']})")
        note = notes.get((r["date"], r["rank"]))
        if note:
            links.append(f"[[{note}]]")
    out.append("  - " + " ｜ ".join(links))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query", nargs="*", help="検索語（大文字小文字は区別しない）")
    ap.add_argument("--and", dest="use_and", action="store_true", help="すべての検索語に当たるものだけ")
    ap.add_argument("--topic", action="append", default=[], help="話題コードで絞る（複数可）")
    ap.add_argument("--days", type=int, default=28, help="直近 N 日（0 で全期間。既定 28）")
    ap.add_argument("--shown", action="store_true", help="Digest に載った記事（本編・Explore）だけ")
    ap.add_argument("--limit", type=int, default=40, help="最大件数（既定 40）")
    ap.add_argument("--terms", action="store_true", help="terms の一覧と件数を出して終わる")
    args = ap.parse_args()

    rows = load(args.days)
    if args.terms:
        c = Counter(t for r in rows for t in (r.get("terms") or []))
        print(f"直近 {args.days or '全'} 日の terms（{len(c)} 語）")
        for t, n in c.most_common():
            print(f"- {t}：{n}")
        return
    if not args.query and not args.topic:
        ap.error("検索語か --topic を指定してください")

    hit = []
    for r in rows:
        if args.shown and r.get("status") not in ("main", "explore"):
            continue
        if args.topic and not ({r.get("topic"), r.get("topic2")} & set(args.topic)):
            continue
        if args.query and not matches(r, args.query, args.use_and):
            continue
        hit.append(r)

    # 同じ URL は 1 回だけ（まとめ記事で重複することがある）
    seen, uniq = set(), []
    for r in sorted(hit, key=lambda r: (r["date"], r.get("rank") or 99), reverse=True):
        key = r.get("url") or r.get("title")
        if key in seen:
            continue
        seen.add(key)
        uniq.append(r)

    shown = sum(r.get("status") in ("main", "explore") for r in uniq)
    votes = Counter(r["digest"].get("vote") for r in uniq if r.get("digest"))
    cond = " ".join(args.query) + (" " + " ".join(f"topic={t}" for t in args.topic) if args.topic else "")
    print(f"## 検索：{cond.strip()}（直近 {args.days or '全'} 日）")
    print(f"該当 {len(uniq)} 件（Digest に載った {shown} 件、👍 {votes.get('👍', 0)} / 👎 {votes.get('👎', 0)}）")
    if len(uniq) > args.limit:
        print(f"※ 多いので新しい順に {args.limit} 件まで。--limit で変えられる")
    print()
    notes = wiki_notes()
    for r in uniq[: args.limit]:
        print(fmt(r, notes))


if __name__ == "__main__":
    main()
