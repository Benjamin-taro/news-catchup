#!/usr/bin/env python3
"""Digest/*.md（と Weekly/*.md）から GitHub Pages 用の静的サイトを _site/ に生成する。

使い方:
    python3 scripts/build_site.py                 # リポジトリ直下の Digest/ Weekly/ -> _site/
    python3 scripts/build_site.py --root DIR --out OUT

標準ライブラリのみ。リンクはすべて相対パス（project page の /news-catchup/ 配下でも動く）。
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

SITE_TITLE = "Tech Digest"
WEEKDAYS = "月火水木金土日"

# ---------------------------------------------------------------------------
# inline markdown
# ---------------------------------------------------------------------------

INLINE_RE = re.compile(
    r"!\[(?P<ialt>[^\]]*)\]\((?P<isrc>[^)\s]+)\)"
    r"|\[(?P<text>[^\]]+)\]\((?P<href>[^)\s]+)\)"
    r"|\*\*(?P<bold>.+?)\*\*"
    r"|`(?P<code>[^`]+)`"
    r"|(?P<url>https?://[^\s<>()（）]+)"
)


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def safe_url(url: str) -> str:
    """http(s)・相対 URL のみ通す。javascript: などは # に置き換える。"""
    u = url.strip()
    scheme = urlparse(u).scheme.lower()
    if scheme and scheme not in ("http", "https", "mailto"):
        return "#"
    return u


def ext_link(href: str, inner_html: str, cls: str = "") -> str:
    href = safe_url(href)
    attrs = f' class="{cls}"' if cls else ""
    if href.startswith(("http://", "https://")):
        attrs += ' target="_blank" rel="noopener noreferrer"'
    return f'<a href="{esc(href)}"{attrs}>{inner_html}</a>'


def inline(text: str) -> str:
    out: list[str] = []
    pos = 0
    for m in INLINE_RE.finditer(text):
        out.append(esc(text[pos:m.start()]))
        if m.group("isrc") is not None:
            out.append(
                f'<img src="{esc(safe_url(m.group("isrc")))}" alt="{esc(m.group("ialt"))}" '
                'loading="lazy" referrerpolicy="no-referrer" class="inline-img">'
            )
        elif m.group("href") is not None:
            out.append(ext_link(m.group("href"), inline(m.group("text"))))
        elif m.group("bold") is not None:
            out.append(f"<strong>{inline(m.group('bold'))}</strong>")
        elif m.group("code") is not None:
            out.append(f"<code>{esc(m.group('code'))}</code>")
        else:
            url = m.group("url")
            out.append(ext_link(url, esc(url)))
        pos = m.end()
    out.append(esc(text[pos:]))
    return "".join(out)


def strip_inline(text: str) -> str:
    """見出しなどをプレーンテキスト化（markdown 記号を落とす）。"""
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text.strip()


# ---------------------------------------------------------------------------
# block markdown（フォールバック用の簡易レンダラ）
# ---------------------------------------------------------------------------

LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
CHECK_RE = re.compile(r"^\[( |x|X)\]\s+(.*)$")


def render_markdown(lines: list[str]) -> str:
    out: list[str] = []
    para: list[str] = []
    list_tag: str | None = None
    in_code = False
    code: list[str] = []
    table: list[str] = []

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + "<br>".join(inline(p) for p in para) + "</p>")
            para = []

    def close_list():
        nonlocal list_tag
        if list_tag:
            out.append(f"</{list_tag}>")
            list_tag = None

    def flush_table():
        nonlocal table
        if not table:
            return
        rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in table]
        rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c or "-") for c in r)]
        if rows:
            out.append('<div class="table-wrap"><table>')
            head, *body = rows
            out.append("<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>")
            out.append("<tbody>")
            for r in body:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            out.append("</tbody></table></div>")
        table = []

    for raw in lines:
        line = raw.rstrip("\n")
        if in_code:
            if line.strip().startswith("```"):
                out.append("<pre><code>" + esc("\n".join(code)) + "</code></pre>")
                code, in_code = [], False
            else:
                code.append(line)
            continue
        s = line.strip()
        if s.startswith("```"):
            flush_para(); close_list(); flush_table()
            in_code = True
            continue
        if s.startswith("|"):
            flush_para(); close_list()
            table.append(s)
            continue
        flush_table()
        if not s:
            flush_para(); close_list()
            continue
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", s):
            flush_para(); close_list()
            out.append("<hr>")
            continue
        hm = re.match(r"^(#{1,6})\s+(.*)$", s)
        if hm:
            flush_para(); close_list()
            lvl = min(len(hm.group(1)) + 1, 6)  # h1 はページタイトルに使うので 1 段下げる
            out.append(f"<h{lvl}>{inline(hm.group(2))}</h{lvl}>")
            continue
        if s.startswith(">"):
            flush_para(); close_list()
            out.append(f"<blockquote>{inline(s.lstrip('>').strip())}</blockquote>")
            continue
        lm = LIST_RE.match(line)
        if lm:
            flush_para()
            tag = "ol" if lm.group(2)[0].isdigit() else "ul"
            if list_tag != tag:
                close_list()
                out.append(f"<{tag}>")
                list_tag = tag
            body = lm.group(3)
            cm = CHECK_RE.match(body)
            if cm:
                mark = "☑" if cm.group(1).lower() == "x" else "☐"
                out.append(f'<li class="task">{mark} {inline(cm.group(2))}</li>')
            else:
                out.append(f"<li>{inline(body)}</li>")
            continue
        if list_tag:
            close_list()
        para.append(s)
    if in_code:
        out.append("<pre><code>" + esc("\n".join(code)) + "</code></pre>")
    flush_para(); close_list(); flush_table()
    return "\n".join(out)


# ---------------------------------------------------------------------------
# digest parser
# ---------------------------------------------------------------------------

@dataclass
class Item:
    rank: int
    title: str
    image: str | None = None
    summary: str = ""
    points: list[str] = field(default_factory=list)
    sowhat: str = ""
    links: list[tuple[str, str]] = field(default_factory=list)
    score: int | None = None
    reason: str = ""
    up: bool = False
    down: bool = False
    explore: bool = False
    extra: list[str] = field(default_factory=list)

    @property
    def domain(self) -> str:
        for _, url in self.links:
            host = urlparse(url).hostname or ""
            if host:
                return host.removeprefix("www.")
        return ""


@dataclass
class Digest:
    date: dt.date
    path: Path
    meta: dict[str, str] = field(default_factory=dict)
    title: str = ""
    preamble: list[str] = field(default_factory=list)
    items: list[Item] = field(default_factory=list)
    stack: list[tuple[str, str, str]] = field(default_factory=list)  # (title, url, text)
    stack_extra: list[str] = field(default_factory=list)
    sections: list[tuple[str, list[str]]] = field(default_factory=list)  # 未知の ## セクション


FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
ITEM_H_RE = re.compile(r"^(\d+)[.)]\s*(.*)$")
IMG_LINE_RE = re.compile(r"^!\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)$")
LABEL_RE = re.compile(r"^\*\*(一言で|So what|Sowhat|so what)\*\*\s*[：:]\s*(.*)$", re.I)
VOTE_RE = re.compile(r"^[-*]\s*\[( |x|X)\]\s*(👍|👎)")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
STACK_RE = re.compile(r"^[-*]\s+\[([^\]]+)\]\(([^)\s]+)\)\s*(?:[—–:-]+\s*)?(.*)$")
SCORE_RE = re.compile(r"^(\d+)\s*点$")


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("\"'")
    return meta, text[m.end():]


def parse_links_line(item: Item, line: str) -> None:
    body = line.lstrip("🔗").strip()
    parts = [p.strip() for p in re.split(r"[｜|]", body)]
    item.links.extend(LINK_RE.findall(parts[0]))
    rest = []
    for p in parts[1:]:
        if not p:
            continue
        sm = SCORE_RE.match(p)
        if sm and item.score is None:
            item.score = int(sm.group(1))
        else:
            rest.append(p)
    item.reason = " ｜ ".join(rest)


def parse_item(rank: int, title: str, lines: list[str], explore: bool) -> Item:
    item = Item(rank=rank, title=title.strip(), explore=explore)
    current = None  # 続き行の吸収先 ("summary" / "sowhat" / "point")
    for raw in lines:
        s = raw.strip()
        if not s or re.fullmatch(r"-{3,}", s):
            current = None
            continue
        im = IMG_LINE_RE.match(s)
        if im and item.image is None:
            item.image = im.group(1)
            current = None
            continue
        lm = LABEL_RE.match(s)
        if lm:
            if lm.group(1) == "一言で":
                item.summary, current = lm.group(2), "summary"
            else:
                item.sowhat, current = lm.group(2), "sowhat"
            continue
        vm = VOTE_RE.match(s)
        if vm:
            checked = vm.group(1).lower() == "x"
            if vm.group(2) == "👍":
                item.up = checked
            else:
                item.down = checked
            current = None
            continue
        if s.startswith("🔗"):
            parse_links_line(item, s)
            current = None
            continue
        if re.match(r"^[-*+]\s+", s):
            item.points.append(re.sub(r"^[-*+]\s+", "", s))
            current = "point"
            continue
        # 続き行（行折り返し）
        if current == "summary":
            item.summary += s
        elif current == "sowhat":
            item.sowhat += s
        elif current == "point" and raw.startswith((" ", "\t")):
            item.points[-1] += s
        else:
            item.extra.append(raw)
            current = None
    return item


def parse_digest(path: Path, date: dt.date) -> Digest:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    meta, body = parse_frontmatter(text)
    d = Digest(date=date, path=path, meta=meta)

    # ## 単位でセクションに分割
    blocks: list[tuple[str | None, list[str]]] = [(None, [])]
    for line in body.split("\n"):
        hm = re.match(r"^##\s+(.*)$", line)
        if hm and not line.startswith("###"):
            blocks.append((hm.group(1).strip(), []))
        else:
            blocks[-1][1].append(line)

    explore = False
    for heading, lines in blocks:
        if heading is None:
            for ln in lines:
                t = re.match(r"^#\s+(.*)$", ln)
                if t and not d.title:
                    d.title = t.group(1).strip()
                elif ln.strip() and not re.fullmatch(r"-{3,}", ln.strip()):
                    d.preamble.append(ln)
            continue
        im = ITEM_H_RE.match(heading)
        plain = strip_inline(heading)
        if im:
            d.items.append(parse_item(int(im.group(1)), im.group(2), lines, explore))
        elif "explore" in plain.lower() and len(plain) < 30:
            explore = True
            rest = [ln for ln in lines if ln.strip() and not re.fullmatch(r"-{3,}", ln.strip())]
            if rest:
                d.sections.append((heading, rest))
        elif "stack" in plain.lower():
            for ln in lines:
                sm = STACK_RE.match(ln.strip())
                if sm:
                    d.stack.append((sm.group(1), sm.group(2), sm.group(3).strip()))
                elif ln.strip() and not re.fullmatch(r"-{3,}", ln.strip()):
                    d.stack_extra.append(ln)
        else:
            d.sections.append((heading, lines))
    return d


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

def fmt_date(d: dt.date) -> str:
    return f"{d.year}年{d.month}月{d.day}日（{WEEKDAYS[d.weekday()]}）"


def hue_of(s: str) -> int:
    return int(hashlib.md5((s or "x").encode()).hexdigest()[:4], 16) % 360


def placeholder(domain: str) -> str:
    label = domain or "no image"
    return (
        f'<div class="ph" style="--h:{hue_of(domain)}" aria-hidden="true">'
        f'<span class="ph-domain">{esc(label)}</span></div>'
    )


def media(image: str | None, domain: str, cls: str = "media") -> str:
    ph = placeholder(domain)
    if not image:
        return f'<div class="{cls}">{ph}</div>'
    return (
        f'<div class="{cls}">{ph}'
        f'<img src="{esc(safe_url(image))}" alt="" loading="lazy" decoding="async" '
        'referrerpolicy="no-referrer" onerror="this.remove()"></div>'
    )


def render_item(it: Item) -> str:
    p = [f'<article class="card{" card-explore" if it.explore else ""}" id="item-{it.rank}">']
    p.append(media(it.image, it.domain))
    p.append('<div class="card-body">')
    p.append(f'<div class="card-head"><span class="rank">{it.rank:02d}</span>'
             f'<h2 class="card-title">{inline(it.title)}</h2></div>')
    votes = []
    if it.up:
        votes.append('<span class="vote vote-up" title="👍 済み">👍</span>')
    if it.down:
        votes.append('<span class="vote vote-down" title="👎 済み">👎</span>')
    if it.summary:
        p.append(f'<p class="summary">{inline(it.summary)}</p>')
    if it.points:
        p.append('<ul class="points">' + "".join(f"<li>{inline(x)}</li>" for x in it.points) + "</ul>")
    if it.extra:
        p.append(f'<div class="extra">{render_markdown(it.extra)}</div>')
    if it.sowhat:
        p.append(f'<div class="sowhat"><span class="sowhat-label">So what</span>'
                 f'<p>{inline(it.sowhat)}</p></div>')
    foot = []
    if it.links:
        chips = "".join(ext_link(u, esc(t), "chip") for t, u in it.links)
        foot.append(f'<div class="chips">{chips}</div>')
    meta = []
    if it.score is not None:
        meta.append(f'<span class="score"><b>{it.score}</b>点</span>')
    if it.reason:
        meta.append(f'<span class="reason">{inline(it.reason)}</span>')
    meta.extend(votes)
    if meta:
        foot.append('<div class="meta">' + "".join(meta) + "</div>")
    if foot:
        p.append('<footer class="card-foot">' + "".join(foot) + "</footer>")
    # 👍/👎 ボタン。GitHub トークンを登録したブラウザでだけ vote.js が表示する
    p.append(f'<div class="vote-bar" data-rank="{it.rank}" hidden>'
             '<button type="button" class="vote-btn" data-vote="👍" aria-pressed="false">👍 <span>Good</span></button>'
             '<button type="button" class="vote-btn" data-vote="👎" aria-pressed="false">👎 <span>Bad</span></button>'
             "</div>")
    p.append("</div></article>")
    return "\n".join(p)


def page(title: str, body: str, description: str = "", digest_path: str = "") -> str:
    vote = (f'<script src="vote.js" data-digest="{esc(digest_path)}" defer></script>' if digest_path else "")
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="color-scheme" content="light dark">
<meta name="referrer" content="no-referrer">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Noto+Serif+JP:wght@700;900&display=swap">
<link rel="stylesheet" href="style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%F0%9F%93%B0%3C/text%3E%3C/svg%3E">
</head>
<body>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html">{SITE_TITLE}<span>毎朝のテックニュース</span></a>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="site-footer"><div class="wrap">Generated {esc(dt.datetime.now().strftime('%Y-%m-%d %H:%M'))} · <a href="index.html">一覧へ</a> · <a href="settings.html">👍/👎 の設定</a></div></footer>
{vote}
</body>
</html>
"""


def day_nav(prev: Digest | None, nxt: Digest | None) -> str:
    left = (f'<a class="nav-prev" href="{prev.date.isoformat()}.html">← {esc(fmt_date(prev.date))}</a>'
            if prev else '<span class="nav-prev disabled">← 前の日</span>')
    right = (f'<a class="nav-next" href="{nxt.date.isoformat()}.html">{esc(fmt_date(nxt.date))} →</a>'
             if nxt else '<span class="nav-next disabled">次の日 →</span>')
    return f'<nav class="day-nav">{left}<a class="nav-home" href="index.html">一覧</a>{right}</nav>'


def render_day(d: Digest, prev: Digest | None, nxt: Digest | None) -> str:
    b = [day_nav(prev, nxt)]
    stats = []
    if d.meta.get("input"):
        stats.append(f"収集 {esc(d.meta['input'])} 件")
    if d.meta.get("selected"):
        stats.append(f"選定 {esc(d.meta['selected'])} 件")
    b.append('<section class="hero">'
             f'<p class="eyebrow">{esc(d.date.isoformat())}</p>'
             f'<h1>{esc(fmt_date(d.date))}</h1>'
             + (f'<p class="stats">{" · ".join(stats)}</p>' if stats else "")
             + "</section>")
    if d.preamble:
        cls = "notice" if not d.items else "preamble"
        b.append(f'<div class="{cls}">{render_markdown(d.preamble)}</div>')

    main_items = [i for i in d.items if not i.explore]
    explore_items = [i for i in d.items if i.explore]
    if main_items:
        b.append('<section class="grid">' + "\n".join(render_item(i) for i in main_items) + "</section>")
    if explore_items:
        b.append('<section class="explore"><div class="section-head"><h2>🧭 Explore</h2>'
                 '<p>ふだんの関心の外から、あえて拾った話題</p></div>'
                 '<div class="grid">' + "\n".join(render_item(i) for i in explore_items) + "</div></section>")
    for heading, lines in d.sections:
        if any(ln.strip() for ln in lines):
            b.append(f'<section class="misc"><h2>{inline(heading)}</h2>{render_markdown(lines)}</section>')
    if d.stack or d.stack_extra:
        rows = "".join(
            f'<li>{ext_link(u, esc(t))}<span>{inline(x)}</span></li>' for t, u, x in d.stack
        )
        b.append('<section class="stack"><h2>🔧 Stack メモ</h2>'
                 + (f"<ul>{rows}</ul>" if rows else "")
                 + (render_markdown(d.stack_extra) if d.stack_extra else "")
                 + "</section>")
    if not d.items and not d.preamble and not d.sections and not d.stack:
        b.append('<div class="notice"><p>この日のダイジェストは空です。</p></div>')
    b.append(day_nav(prev, nxt))
    heads = " / ".join(strip_inline(i.title) for i in d.items[:3])
    return page(f"{d.date.isoformat()} | {SITE_TITLE}", "\n".join(b), heads, f"Digest/{d.date.isoformat()}.md")


def render_index(digests: list[Digest], weeklies: list[tuple[str, str]]) -> str:
    b = ['<section class="hero"><p class="eyebrow">Daily archive</p><h1>テックニュースの毎朝ダイジェスト</h1>'
         f'<p class="stats">{len(digests)} 日分</p></section>']
    if weeklies:
        chips = "".join(f'<a class="chip" href="{esc(fn)}">{esc(name)}</a>' for name, fn in weeklies)
        b.append(f'<section class="weekly-list"><h2>Weekly</h2><div class="chips">{chips}</div></section>')
    cards = []
    for i, d in enumerate(digests):
        first = d.items[0] if d.items else None
        lead = " lead" if i == 0 else ""
        c = [f'<a class="day-card{lead}" href="{d.date.isoformat()}.html">']
        c.append(media(first.image if first else None, first.domain if first else "", "media"))
        c.append('<div class="day-body">')
        c.append(f'<p class="eyebrow">{esc(d.date.isoformat())}</p><h2>{esc(fmt_date(d.date))}</h2>')
        if d.items:
            c.append('<ol class="heads">' + "".join(
                f'<li><span class="rank">{it.rank:02d}</span>{esc(strip_inline(it.title))}</li>'
                for it in d.items[:3]) + "</ol>")
            more = len(d.items) - 3
            if more > 0:
                c.append(f'<p class="more">ほか {more} 件</p>')
        else:
            msg = strip_inline(" ".join(ln.strip() for ln in d.preamble)) or "記事なし"
            c.append(f'<p class="more warn">{esc(msg[:120])}</p>')
        c.append("</div></a>")
        cards.append("".join(c))
    if cards:
        b.append('<section class="day-grid">' + "\n".join(cards) + "</section>")
    else:
        b.append('<div class="notice"><p>まだダイジェストがありません。</p></div>')
    return page(SITE_TITLE, "\n".join(b), "毎朝のテックニュースダイジェスト")


def render_weekly(name: str, path: Path) -> str:
    meta, body = parse_frontmatter(path.read_text(encoding="utf-8").replace("\r\n", "\n"))
    lines = body.split("\n")
    title = name
    for i, ln in enumerate(lines):
        m = re.match(r"^#\s+(.*)$", ln)
        if m:
            title = strip_inline(m.group(1))
            lines = lines[:i] + lines[i + 1:]
            break
    content = (f'<nav class="day-nav"><a class="nav-home" href="index.html">一覧</a></nav>'
               f'<section class="hero"><p class="eyebrow">Weekly</p><h1>{esc(title)}</h1></section>'
               f'<article class="prose">{render_markdown(lines)}</article>')
    return page(f"{title} | {SITE_TITLE}", content)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def render_settings() -> str:
    body = """<section class="hero"><p class="eyebrow">Settings</p><h1>👍/👎 の設定</h1></section>
<div class="settings">
<p>この端末で 👍/👎 を押せるようにするには、GitHub のトークンを登録します。トークンはこのブラウザの中にだけ保存され、GitHub 以外には送られません。</p>
<ol>
<li>GitHub → Settings → Developer settings → <b>Fine-grained tokens</b> → Generate new token</li>
<li>Repository access：<b>Only select repositories</b> → <code>news-catchup</code></li>
<li>Permissions → Repository permissions → <b>Contents：Read and write</b>（ほかは不要）</li>
<li>発行された <code>github_pat_…</code> を下に貼って保存</li>
</ol>
<form id="token-form">
<input id="token-input" type="password" autocomplete="off" placeholder="github_pat_..." aria-label="GitHub トークン">
<div class="settings-actions"><button type="submit" class="vote-btn">保存して確認</button>
<button type="button" id="token-clear" class="vote-btn">この端末から削除</button></div>
</form>
<p id="token-status" class="token-status" role="status"></p>
</div>"""
    return page(f"設定 | {SITE_TITLE}", body, "👍/👎 ボタンの設定").replace(
        "</body>", '<script src="vote.js" data-settings="1" defer></script>\n</body>')


def build(root: Path, out: Path) -> list[Digest]:
    digest_dir = root / "Digest"
    weekly_dir = root / "Weekly"
    css_src = Path(__file__).resolve().parent.parent / "site-src" / "style.css"
    if (root / "site-src" / "style.css").exists():
        css_src = root / "site-src" / "style.css"

    digests: list[Digest] = []
    for p in sorted(digest_dir.glob("*.md")) if digest_dir.is_dir() else []:
        try:
            date = dt.date.fromisoformat(p.stem)
        except ValueError:
            print(f"skip (not YYYY-MM-DD): {p.name}", file=sys.stderr)
            continue
        digests.append(parse_digest(p, date))
    digests.sort(key=lambda d: d.date)

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    shutil.copyfile(css_src, out / "style.css")
    shutil.copyfile(css_src.parent / "vote.js", out / "vote.js")
    (out / "settings.html").write_text(render_settings(), encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")

    for i, d in enumerate(digests):
        prev = digests[i - 1] if i > 0 else None
        nxt = digests[i + 1] if i + 1 < len(digests) else None
        (out / f"{d.date.isoformat()}.html").write_text(render_day(d, prev, nxt), encoding="utf-8")

    weeklies: list[tuple[str, str]] = []
    for p in sorted(weekly_dir.glob("*.md"), reverse=True) if weekly_dir.is_dir() else []:
        fn = "weekly-" + re.sub(r"[^A-Za-z0-9_-]", "_", p.stem) + ".html"
        (out / fn).write_text(render_weekly(p.stem, p), encoding="utf-8")
        weeklies.append((p.stem, fn))

    newest_first = list(reversed(digests))
    (out / "index.html").write_text(render_index(newest_first, weeklies), encoding="utf-8")
    return digests


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    repo = Path(__file__).resolve().parent.parent
    ap.add_argument("--root", type=Path, default=repo, help="Digest/ と Weekly/ を含むディレクトリ")
    ap.add_argument("--out", type=Path, default=None, help="出力先（既定: <root>/_site）")
    a = ap.parse_args()
    out = a.out or a.root / "_site"
    digests = build(a.root, out)
    for d in digests:
        print(f"{d.date}: {len(d.items)} items, {len(d.stack)} stack")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
