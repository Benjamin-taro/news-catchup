#!/usr/bin/env python3
"""候補ログ（_system/news/candidates/*.jsonl）と Digest の 👍/👎 を突き合わせ、
フィード・キーワード・話題・種類ごとの成績を集計する。

使い方：python3 scripts/source_stats.py [--days 28] [--by feed|keyword|topic|type|publisher]
出力は Markdown の表（集めた件数 → Digest に載った件数 → 👍 → 👎）。
"""
import argparse
import datetime as dt
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAND_DIR = ROOT / "_system/news/candidates"
DIGEST_DIR = ROOT / "Digest"

ITEM_HEADING = re.compile(r"^## (\d+)\. ")
VOTE_LINE = re.compile(r"^[-*]\s*\[( |x|X)\]\s*(👍|👎)")


def read_votes(date):
    """Digest/<date>.md から {rank: 'up' | 'down' | None} を返す。"""
    path = DIGEST_DIR / f"{date}.md"
    votes, rank = {}, None
    if not path.exists():
        return votes
    for line in path.read_text().split("\n"):
        h = ITEM_HEADING.match(line)
        if h:
            rank = int(h.group(1))
            votes[rank] = None
        elif line.startswith("## "):
            rank = None
        elif rank is not None:
            v = VOTE_LINE.match(line)
            if v and v.group(1) != " ":
                votes[rank] = "up" if v.group(2) == "👍" else "down"
    return votes


def load(days):
    since = dt.date.today() - dt.timedelta(days=days)
    rows = []
    for path in sorted(CAND_DIR.glob("*.jsonl")):
        try:
            date = dt.date.fromisoformat(path.stem)
        except ValueError:
            continue
        if date < since:
            continue
        votes = read_votes(path.stem)
        # 1 件でも評価を付けた日だけを「読んだ日」とみなす（無反応と未読を区別するため）
        read_day = any(votes.values())
        for line in path.read_text().split("\n"):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except ValueError:
                continue
            row["date"] = path.stem
            row["vote"] = votes.get(row.get("rank")) if row.get("rank") is not None else None
            row["read_day"] = read_day
            rows.append(row)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--by", default="feed", choices=["feed", "keyword", "topic", "type", "publisher"])
    args = ap.parse_args()

    rows = load(args.days)
    stats = defaultdict(lambda: defaultdict(int))
    for r in rows:
        key = r.get(args.by) or "（なし）"
        if args.by == "keyword" and r.get("feed") not in ("Google News", "Google Alerts"):
            continue
        s = stats[key]
        s["collected"] += 1
        if r.get("status") in ("main", "explore"):
            s["selected"] += 1
            if r["read_day"]:
                s["shown_read"] += 1
        if r["vote"] == "up":
            s["up"] += 1
        elif r["vote"] == "down":
            s["down"] += 1

    days = len({r["date"] for r in rows})
    print(f"対象：直近 {args.days} 日のうち候補ログがある {days} 日分、{len(rows)} 件\n")
    print(f"| {args.by} | 集めた | Digest に載った | 採用率 | 👍 | 👎 | 👍 率（読んだ日） |")
    print("|---|---:|---:|---:|---:|---:|---:|")
    for key, s in sorted(stats.items(), key=lambda kv: (-kv[1]["up"], -kv[1]["selected"], kv[0])):
        rate = f"{s['selected'] / s['collected']:.0%}" if s["collected"] else "–"
        up_rate = f"{s['up'] / s['shown_read']:.0%}" if s["shown_read"] else "–"
        print(f"| {key} | {s['collected']} | {s['selected']} | {rate} | {s['up']} | {s['down']} | {up_rate} |")


if __name__ == "__main__":
    main()
