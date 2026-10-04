#!/usr/bin/env python3
"""Matcha の設定ファイルが壊れていないかを確かめる（週次レビューが検索キーワードを書き換えるため）。
問題があれば理由を表示して終了コード 1 を返す。"""
import re
import sys
from pathlib import Path

PATH = Path(__file__).resolve().parent.parent / "_system/matcha/config.yaml"
FEED = re.compile(r"^  - (https://\S+)( \d+)?(\s+#.*)?$")
KEYWORD = re.compile(r"^https://news\.google\.com/rss/search\?q=[A-Za-z0-9%.\-_]+&(hl=en-US&gl=US&ceid=US:en|hl=ja&gl=JP&ceid=JP:ja)$")

errors, feeds, keywords, in_feeds = [], 0, 0, False
text = PATH.read_text()
for no, line in enumerate(text.split("\n"), 1):
    if line.startswith("feeds:"):
        in_feeds = True
        continue
    if in_feeds and line and not line.startswith(" "):
        in_feeds = False
    if not in_feeds or not line.strip() or line.strip().startswith("#"):
        continue
    m = FEED.match(line)
    if not m:
        errors.append(f"{no} 行目：フィードの形式が不正：{line.strip()[:80]}")
        continue
    feeds += 1
    url = m.group(1)
    if "news.google.com/rss/search?q=" in url and "site%3Ax.com" not in url:
        keywords += 1
        if not KEYWORD.match(url):
            errors.append(f"{no} 行目：キーワード検索の URL が既定の形式と違う：{url[:90]}")
for key in ("markdown_dir_path:", "database_file_path:"):
    if key not in text:
        errors.append(f"{key} がない")
if feeds < 8:
    errors.append(f"フィードが {feeds} 本しかない（消しすぎ）")
if keywords > 12:
    errors.append(f"キーワード検索が {keywords} 本ある（上限 12 本）")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: feeds={feeds}, keyword searches={keywords}")
