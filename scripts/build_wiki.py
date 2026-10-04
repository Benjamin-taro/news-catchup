#!/usr/bin/env python3
"""Digest で 👍 を付けた記事から、Obsidian 用の知識ノートを作る。

- wiki/articles/  記事ノート（1 記事 = 1 ノート）。プロパティとリンクを持つ
- wiki/topics/    トピックノート（なければ雛形を作る。本文は週次レビューが育てる）
- wiki/entities/  企業・人物・製品のノート（なければ雛形を作る）
- wiki/views/     Bases の一覧、wiki/Home.md 入口

冪等：既にあるノートは一切書き換えない（自分のメモを守るため）。新しい 👍 の分だけ作る。
トピックと登場する企業・人物は、候補ログ（_system/news/candidates/*.jsonl）から取る。
候補ログがない過去分は _system/news/wiki-backfill.json を使う。

使い方：python3 scripts/build_wiki.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIGEST = ROOT / "Digest"
WIKI = ROOT / "wiki"
CAND = ROOT / "_system/news/candidates"
BACKFILL = ROOT / "_system/news/wiki-backfill.json"

# 候補ログの topic コード → トピックノート名（ノート名を変えるときはここと既存ノートの両方を直す）
TOPICS = {
    "ai-work": "AI と開発者の働き方",
    "ai-enterprise": "AI の企業導入",
    "career": "FDE とエンジニアのキャリア",
    "bigtech": "大手テック企業の動き",
    "incident": "セキュリティ事故",
    "agent-infra": "AI エージェントの基盤と安全性",
    "llm": "LLM とモデル競争",
    "autonomous": "自動運転",
    "stack": "開発スタック",
    "other": "その他の話題",
}
KIND_LABEL = {
    "opinion": "議論・意見", "release": "製品・発表", "incident": "事故・障害", "data": "調査・データ",
    "howto": "解説", "news": "報道", "social": "SNS", "promo": "宣伝",
}
ENTITY_KIND_LABEL = {"company": "企業・組織", "person": "人物", "product": "製品・技術"}

ITEM = re.compile(r"^## (\d+)\. (.+)$")
VOTE = re.compile(r"^[-*]\s*\[( |x|X)\]\s*(👍|👎)")
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
IMG = re.compile(r"^!\[[^\]]*\]\(<?([^)>\s]+)>?\)")
BAD_CHARS = re.compile(r'[\\/:*?"<>|#^\[\]]')


def safe_name(s, limit=70):
    s = BAD_CHARS.sub(" ", s)
    s = re.sub(r"\s+", " ", s).strip(" .")
    return s[:limit].rstrip(" .")


def yaml_str(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse_digest(path):
    items, cur, explore = [], None, False
    for line in path.read_text().split("\n"):
        m = ITEM.match(line)
        if m:
            cur = {"rank": int(m.group(1)), "title": m.group(2).strip(), "explore": explore, "image": "",
                   "summary": "", "points": [], "sowhat": "", "links": [], "score": None, "reason": "", "vote": None}
            items.append(cur)
            continue
        if line.startswith("## "):
            if "Explore" in line:
                explore = True
            cur = None
            continue
        if cur is None:
            continue
        s = line.strip()
        if not s or s == "---":
            continue
        v = VOTE.match(s)
        if v:
            if v.group(1) != " ":
                cur["vote"] = "up" if v.group(2) == "👍" else "down"
        elif IMG.match(s):
            cur["image"] = cur["image"] or IMG.match(s).group(1)
        elif s.startswith("**一言で**"):
            cur["summary"] = re.sub(r"^\*\*一言で\*\*[：:]\s*", "", s)
        elif s.startswith("**So what**"):
            cur["sowhat"] = re.sub(r"^\*\*So what\*\*[：:]\s*", "", s)
        elif "🔗" in s:
            cur["links"] = LINK.findall(s)
            parts = [p.strip() for p in s.split("｜")]
            for p in parts[1:]:
                sm = re.match(r"^(\d+)\s*点$", p)
                if sm:
                    cur["score"] = int(sm.group(1))
                else:
                    cur["reason"] = p
        elif s.startswith("- "):
            cur["points"].append(s[2:])
    return items


def load_meta(date):
    """{rank: {topic, topic2, kind, entities:[{name, kind}]}} を返す。"""
    meta = {}
    path = CAND / f"{date}.jsonl"
    if path.exists():
        for line in path.read_text().split("\n"):
            try:
                row = json.loads(line)
            except ValueError:
                continue
            rank = row.get("rank")
            if rank is None:
                continue
            m = meta.setdefault(int(rank), {"topic": row.get("topic"), "topic2": row.get("topic2") or "",
                                            "kind": row.get("type") or "", "entities": []})
            for e in row.get("entities") or []:
                if isinstance(e, dict) and e.get("name") and e["name"] not in [x["name"] for x in m["entities"]]:
                    m["entities"].append({"name": e["name"], "kind": e.get("kind") or ""})
    if BACKFILL.exists():
        for key, val in json.loads(BACKFILL.read_text()).items():
            d, _, r = key.partition("#")
            if d == date and int(r) not in meta:
                meta[int(r)] = val
    return meta


def write_if_missing(path, text):
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    print(f"  + {path.relative_to(ROOT)}")
    return True


def topic_note(code, name):
    return f"""---
type: topic
code: {code}
updated:
---
# {name}

## 現状のまとめ
（週次レビューが、その週の記事をもとに書き直します）

## 論点と立場

## 問い

## 自分の考え
<!-- ここはあなたが書く欄です。Claude は書き換えません -->

## 関連記事
![[wiki/views/articles.base#このノートに関連する記事]]
"""


def entity_note(name, kind):
    return f"""---
type: entity
kind: {ENTITY_KIND_LABEL.get(kind, "未分類")}
aliases: []
---
# {name}

## 概要

## 自分のメモ
<!-- ここはあなたが書く欄です。Claude は書き換えません -->

## 関連記事
![[wiki/views/articles.base#このノートに関連する記事]]
"""


def article_note(date, it, meta):
    topics = [TOPICS[c] for c in (meta.get("topic"), meta.get("topic2")) if c in TOPICS]
    topics = list(dict.fromkeys(topics)) or [TOPICS["other"]]
    entities = [safe_name(e["name"]) for e in meta.get("entities", []) if safe_name(e["name"])]
    fm = ["---", "type: article", f"day: {date}", "vote: up",
          f"score: {it['score']}" if it["score"] is not None else "score:",
          f"kind: {KIND_LABEL.get(meta.get('kind'), meta.get('kind') or '')}",
          f"source: {yaml_str(it['links'][0][0]) if it['links'] else ''}",
          f"url: {yaml_str(it['links'][0][1]) if it['links'] else ''}",
          f"main_topic: {yaml_str('[[' + topics[0] + ']]')}",
          "topics:"] + [f"  - {yaml_str('[[' + t + ']]')}" for t in topics]
    fm += ["entities:"] + [f"  - {yaml_str('[[' + e + ']]')}" for e in entities] if entities else ["entities: []"]
    fm += [f"digest: {yaml_str('[[Digest/' + date + ']]')}", f"digest_rank: {it['rank']}", "---"]
    body = [f"# {it['title']}", ""]
    if it["image"]:
        body += [f"![]({it['image']})", ""]
    if it["summary"]:
        body += ["> [!summary] 一言で", f"> {it['summary']}", ""]
    body += [f"- {p}" for p in it["points"]] + ([""] if it["points"] else [])
    if it["sowhat"]:
        body += ["> [!tip] So what", f"> {it['sowhat']}", ""]
    body += ["**トピック**：" + "、".join(f"[[{t}]]" for t in topics)]
    if entities:
        body += ["**登場**：" + "、".join(f"[[{e}]]" for e in entities)]
    body += ["**出典**：" + "・".join(f"[{t}]({u})" for t, u in it["links"]) + f"（[[Digest/{date}|{date} の Digest]] {it['rank']} 番）", "",
             "## 自分のメモ", "<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->", ""]
    return "\n".join(fm + [""] + body)


ARTICLES_BASE = """filters:
  and:
    - file.inFolder("wiki/articles")
properties:
  file.name:
    displayName: 記事
  note.day:
    displayName: 日付
  note.main_topic:
    displayName: トピック
  note.kind:
    displayName: 種類
  note.source:
    displayName: 出典
  note.score:
    displayName: 点数
  note.entities:
    displayName: 登場
views:
  - type: table
    name: "このノートに関連する記事"
    filters:
      and:
        - file.hasLink(this.file)
    order:
      - file.name
      - note.day
      - note.kind
      - note.source
    sort:
      - property: note.day
        direction: DESC
  - type: table
    name: "直近 7 日"
    filters:
      and:
        - 'day > today() - "7d"'
    order:
      - file.name
      - note.day
      - note.main_topic
      - note.kind
      - note.entities
    sort:
      - property: note.day
        direction: DESC
  - type: table
    name: "トピック別"
    groupBy:
      property: note.main_topic
      direction: ASC
    order:
      - file.name
      - note.day
      - note.kind
      - note.source
    sort:
      - property: note.day
        direction: DESC
  - type: table
    name: "種類別"
    groupBy:
      property: note.kind
      direction: ASC
    order:
      - file.name
      - note.day
      - note.main_topic
    sort:
      - property: note.day
        direction: DESC
  - type: table
    name: "すべて"
    order:
      - file.name
      - note.day
      - note.main_topic
      - note.kind
      - note.source
      - note.score
    sort:
      - property: note.day
        direction: DESC
"""

NOTES_BASE = """filters:
  or:
    - file.inFolder("wiki/topics")
    - file.inFolder("wiki/entities")
properties:
  file.name:
    displayName: ノート
  note.kind:
    displayName: 種類
  note.updated:
    displayName: 更新日
  file.backlinks:
    displayName: 関連記事
views:
  - type: table
    name: "トピック"
    filters:
      and:
        - file.inFolder("wiki/topics")
    order:
      - file.name
      - note.updated
  - type: table
    name: "企業・人物・製品"
    filters:
      and:
        - file.inFolder("wiki/entities")
    groupBy:
      property: note.kind
      direction: ASC
    order:
      - file.name
      - note.kind
"""


def home_note():
    lines = ["---", "type: home", "---", "# ニュースの知識ノート", "",
             "👍 を付けた記事が、トピック・企業・人物とリンクでつながって積み上がる場所です。",
             "グラフビューを開くと、つながりを図で見られます。", "",
             "## まだ答えていない問い", "週次レビューが出した問いのうち、チェックが付いていないものです。答えたら、各トピックの「自分の考え」に書いてチェックを付けます。", "",
             "```query", "path:wiki/topics /^- \\[ \\] /", "```", "",
             "## 直近 7 日の記事", "![[wiki/views/articles.base#直近 7 日]]", "",
             "## トピックごとの現状", ""]
    for name in TOPICS.values():
        lines += [f"### [[{name}]]", f"![[{name}#現状のまとめ]]", ""]
    lines += ["## 一覧", "![[wiki/views/notes.base#トピック]]", "", "![[wiki/views/notes.base#企業・人物・製品]]", "",
              "![[wiki/views/articles.base#トピック別]]", ""]
    return "\n".join(lines)


def main():
    write_if_missing(WIKI / "views/articles.base", ARTICLES_BASE)
    write_if_missing(WIKI / "views/notes.base", NOTES_BASE)
    for code, name in TOPICS.items():
        write_if_missing(WIKI / "topics" / f"{name}.md", topic_note(code, name))
    write_if_missing(WIKI / "Home.md", home_note())

    created = 0
    for path in sorted(DIGEST.glob("*.md")):
        date = path.stem
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            continue
        meta = None
        for it in parse_digest(path):
            if it["vote"] != "up":
                continue
            prefix = f"{date}-{it['rank']:02d}"
            if list((WIKI / "articles").glob(f"{prefix} *.md")):
                continue
            if meta is None:
                meta = load_meta(date)
            m = meta.get(it["rank"], {})
            for e in m.get("entities", []):
                name = safe_name(e["name"])
                if name:
                    write_if_missing(WIKI / "entities" / f"{name}.md", entity_note(name, e.get("kind")))
            write_if_missing(WIKI / "articles" / f"{prefix} {safe_name(it['title'])}.md", article_note(date, it, m))
            created += 1
    print(f"new article notes: {created}")


if __name__ == "__main__":
    main()
