#!/usr/bin/env python3
"""Digest の各記事の見出し直下に、元記事の OGP 画像を `![](url)` として差し込む。

- 冪等：既に画像行がある記事はスキップする。
- 取得に失敗した URL は _system/news/og-cache.json に記録し、次回以降は再取得しない。
- 使い方：python3 scripts/add_images.py [Digest/YYYY-MM-DD.md ...]（省略時は Digest/*.md 全部）
"""
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE_PATH = ROOT / "_system/news/og-cache.json"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"

ITEM_HEADING = re.compile(r"^## \d+\. ")
LINK = re.compile(r"\[[^\]]*\]\((https?://[^)\s]+)\)")
META_TAG = re.compile(r"<meta\s[^>]*>", re.I)
ATTR = re.compile(r'([a-zA-Z:_-]+)\s*=\s*("([^"]*)"|\'([^\']*)\')')


def load_cache():
    try:
        return json.loads(CACHE_PATH.read_text())
    except (OSError, ValueError):
        return {}


def fetch_og_image(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ja,en;q=0.8"})
    with urllib.request.urlopen(req, timeout=15) as res:
        final_url = res.geturl()
        body = res.read(600_000).decode(res.headers.get_content_charset() or "utf-8", "replace")
    found = {}
    for tag in META_TAG.findall(body):
        attrs = {m.group(1).lower(): m.group(3) if m.group(3) is not None else m.group(4) for m in ATTR.finditer(tag)}
        key = (attrs.get("property") or attrs.get("name") or "").lower()
        if key in ("og:image", "og:image:url", "og:image:secure_url", "twitter:image", "twitter:image:src") and attrs.get("content"):
            found.setdefault(key, attrs["content"])
    for key in ("og:image", "og:image:secure_url", "og:image:url", "twitter:image", "twitter:image:src"):
        if key in found:
            return urllib.parse.urljoin(final_url, html.unescape(found[key].strip()))
    return None


def image_for(url, cache):
    if url in cache:
        return cache[url]
    try:
        img = fetch_og_image(url)
    except Exception as e:  # noqa: BLE001 - ネットワーク系の失敗はすべて「画像なし」として扱う
        print(f"  fetch failed: {url} ({e.__class__.__name__})", file=sys.stderr)
        img = None
    cache[url] = img
    return img


def process(path, cache):
    lines = path.read_text().split("\n")
    out, changed = [], False
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        if ITEM_HEADING.match(line):
            nxt = next((l for l in lines[i + 1:] if l.strip()), "")
            if not nxt.startswith("!["):
                section = []
                for l in lines[i + 1:]:
                    if l.startswith("## "):
                        break
                    section.append(l)
                link_line = next((l for l in section if l.startswith("🔗")), "")
                img = next(filter(None, (image_for(u, cache) for u in LINK.findall(link_line))), None)
                if img:
                    out.append(f"![]({img})")
                    changed = True
                    print(f"  + {line[3:40]}")
        i += 1
    if changed:
        path.write_text("\n".join(out))
    return changed


def main():
    targets = [Path(p) for p in sys.argv[1:]] or sorted((ROOT / "Digest").glob("*.md"))
    cache = load_cache()
    for path in targets:
        print(path.name)
        process(path, cache)
    CACHE_PATH.write_text(json.dumps(cache, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    main()
