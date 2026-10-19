#!/usr/bin/env python3
"""Cutroom Notes — multilingual static site builder.

content/<lang>/<slug>.md  ->  /<lang>/posts/<slug>/index.html
Same <slug> across languages = translations of each other (hreflang linked).

Front matter:
---
title: ...
date: 2026-10-18
series: video-archive-ai   # optional
part: 1                    # optional
cover: /images/...webp     # optional
summary: ...
---
"""
import html
import re
import shutil
from datetime import date, datetime
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).parent
LAYOUT = (ROOT / "_layout" / "base.html").read_text(encoding="utf-8")
CFG = yaml.safe_load((ROOT / "content" / "site.yml").read_text(encoding="utf-8"))
SITE_URL = CFG["url"]
LANGS = CFG["langs"]  # ordered dict: code -> strings
GENERATED = list(LANGS.keys()) + ["index.html", "sitemap.xml", "robots.txt", "404.html"]


def parse(f):
    raw = f.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", raw, re.S)
    meta, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, raw)
    d = meta.get("date") or date.today()
    if isinstance(d, str):
        d = datetime.strptime(d[:10], "%Y-%m-%d").date()
    elif isinstance(d, datetime):
        d = d.date()
    meta["date"] = d
    return meta, body


def load(lang):
    posts = []
    for f in sorted((ROOT / "content" / lang).glob("*.md")):
        meta, body = parse(f)
        if meta.get("draft"):
            continue
        slug = f.stem
        posts.append({**meta, "slug": slug, "lang": lang, "url": f"/{lang}/posts/{slug}/",
                      "html": markdown.markdown(body, extensions=["extra", "sane_lists"])})
    posts.sort(key=lambda p: (p["date"], p.get("part") or 0, p["slug"]), reverse=True)
    return posts


def fmt(d, L):
    return L["date_fmt"].format(d=d.day, m=L["months"][d.month - 1], y=d.year)


def lang_nav(cur):
    return " · ".join(
        f'<a href="/{c}/" lang="{c}"{" class=on" if c == cur else ""}>{html.escape(L["name"])}</a>'
        for c, L in LANGS.items())


def page(lang, title, body, desc=None, image=None, alternates=None, path="/"):
    L = LANGS[lang] if lang else None
    site = CFG["title"]
    full = site if title == site else f"{title} · {site}"
    head = ""
    if alternates:
        for c, u in alternates.items():
            head += f'<link rel="alternate" hreflang="{c}" href="{SITE_URL}{u}">\n'
    if image:
        head += f'<meta property="og:image" content="{image if image.startswith("http") else SITE_URL + image}">\n'
    head += f'<link rel="canonical" href="{SITE_URL}{path}">\n'
    if lang:
        head += f'<link rel="alternate" type="application/rss+xml" title="{site}" href="/{lang}/feed.xml">\n'
    vals = {
        "LANG": lang or "en", "DIR": (L or {}).get("dir", "ltr"),
        "TITLE": html.escape(full), "DESC": html.escape(desc or (L or LANGS["id"])["desc"]),
        "HEAD": head, "HOME": f"/{lang}/" if lang else "/", "SITE": site,
        "ALL": html.escape(L["all"]) if L else "", "SERIES_NAV": html.escape(L["series"]) if L else "",
        "SERIES_HREF": f"/{lang}/series/" if lang else "/",
        "BODY": body, "LANGS": lang_nav(lang), "YEAR": str(date.today().year), "AUTHOR": CFG["author"],
    }
    out = LAYOUT
    for k, v in vals.items():
        out = out.replace("{{" + k + "}}", v)
    return out


def write(rel, content):
    out = ROOT / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")


def card(p, L):
    thumb = f'<img class="thumb" loading="lazy" alt="" src="{p["cover"]}">' if p.get("cover") else ""
    part = f'<span class="part">{html.escape(L["part"].format(n=p["part"]))}</span>' if p.get("part") else ""
    return (f'<article class="card"><a href="{p["url"]}" class="card-link"><div class="card-text">'
            f'<div class="meta">{part}<time datetime="{p["date"]}">{fmt(p["date"], L)}</time></div>'
            f'<h2>{html.escape(p["title"])}</h2><p>{html.escape(p.get("summary", ""))}</p></div>{thumb}</a></article>')


def series_box(p, posts, L):
    sid = p["series"]
    info = L["series_titles"].get(sid, {"title": sid})
    rows = sorted([q for q in posts if q.get("series") == sid], key=lambda q: q["part"])
    items = ""
    for q in rows:
        lab = html.escape(L["part"].format(n=q["part"]))
        if q is p:
            items += f'<li class="now"><span>{lab}</span>{html.escape(q["title"])}</li>'
        else:
            items += f'<li><span>{lab}</span><a href="{q["url"]}">{html.escape(q["title"])}</a></li>'
    return (f'<aside class="series-box"><a class="series-name" href="/{p["lang"]}/series/{sid}/">'
            f'{html.escape(L["series"])} · {html.escape(info["title"])}</a><ol>{items}</ol></aside>')


def alternates_for(slug):
    alt = {c: f"/{c}/posts/{slug}/" for c in LANGS if (ROOT / "content" / c / f"{slug}.md").exists()}
    return alt


def build_lang(lang, urls):
    L = LANGS[lang]
    posts = load(lang)
    # index
    body = (f'<header class="list-head"><h1>{html.escape(CFG["title"])}</h1><p>{html.escape(L["desc"])}</p></header>'
            + ('<div class="list">' + "".join(card(p, L) for p in posts) + "</div>" if posts else f'<p class="empty">{html.escape(L["empty"])}</p>'))
    alt_home = {c: f"/{c}/" for c in LANGS}
    alt_home["x-default"] = "/"
    write(f"{lang}/index.html", page(lang, CFG["title"], body, alternates=alt_home, path=f"/{lang}/"))
    urls.append(f"/{lang}/")
    # posts (chronological within series reading: prev/next by date order)
    for i, p in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i + 1 < len(posts) else None
        sb = series_box(p, posts, L) if p.get("series") else ""
        pager = '<nav class="pager">'
        pager += f'<a href="{older["url"]}"><span>{html.escape(L["prev"])}</span>{html.escape(older["title"])}</a>' if older else "<span></span>"
        pager += f'<a href="{newer["url"]}" class="r"><span>{html.escape(L["next"])}</span>{html.escape(newer["title"])}</a>' if newer else "<span></span>"
        pager += "</nav>"
        others = [(c, LANGS[c]["name"]) for c in alternates_for(p["slug"]) if c != lang]
        trline = ""
        if others:
            trline = (f'<p class="tr-line">{html.escape(L["also_in"])} ' + " · ".join(
                f'<a href="/{c}/posts/{p["slug"]}/" lang="{c}">{html.escape(n)}</a>' for c, n in others) + "</p>")
        body = (f'<article class="post"><header><time datetime="{p["date"]}">{fmt(p["date"], L)}</time>'
                f'<h1>{html.escape(p["title"])}</h1>{trline}</header>{sb}'
                f'<div class="prose">{p["html"]}</div>{sb}</article>{pager}')
        alt = alternates_for(p["slug"])
        write(f"{lang}/posts/{p['slug']}/index.html",
              page(lang, p["title"], body, p.get("summary"), p.get("cover"), alt, p["url"]))
        urls.append(p["url"])
    # series pages
    sids = sorted({p["series"] for p in posts if p.get("series")})
    cards = ""
    for sid in sids:
        info = L["series_titles"].get(sid, {"title": sid, "desc": ""})
        rows = sorted([q for q in posts if q.get("series") == sid], key=lambda q: q["part"])
        lst = "".join(f'<li><a href="{q["url"]}"><span>{html.escape(L["part"].format(n=q["part"]))}</span>'
                      f'{html.escape(q["title"])}<time>{fmt(q["date"], L)}</time></a></li>' for q in rows)
        body = (f'<header class="list-head"><h1>{html.escape(info["title"])}</h1><p>{html.escape(info.get("desc", ""))}</p></header>'
                f'<ol class="series-list">{lst}</ol>')
        write(f"{lang}/series/{sid}/index.html", page(lang, info["title"], body, info.get("desc"), path=f"/{lang}/series/{sid}/"))
        urls.append(f"/{lang}/series/{sid}/")
        cards += (f'<article class="card"><a href="/{lang}/series/{sid}/" class="card-link"><div class="card-text">'
                  f'<h2>{html.escape(info["title"])}</h2><p>{html.escape(info.get("desc", ""))}</p></div></a></article>')
    write(f"{lang}/series/index.html", page(lang, L["series"], f'<header class="list-head"><h1>{html.escape(L["series"])}</h1></header><div class="list">{cards}</div>', path=f"/{lang}/series/"))
    # feed
    items = "".join(
        f"<item><title>{html.escape(p['title'])}</title><link>{SITE_URL}{p['url']}</link><guid>{SITE_URL}{p['url']}</guid>"
        f"<pubDate>{p['date'].strftime('%a, %d %b %Y 00:00:00 +0000')}</pubDate><description>{html.escape(p.get('summary', ''))}</description></item>"
        for p in posts[:30])
    write(f"{lang}/feed.xml", f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>{CFG["title"]}</title>'
          f'<link>{SITE_URL}/{lang}/</link><description>{html.escape(L["desc"])}</description><language>{lang}</language>{items}</channel></rss>')
    return len(posts)


def main():
    for g in GENERATED:
        t = ROOT / g
        if t.is_dir():
            shutil.rmtree(t)
        elif t.exists():
            t.unlink()
    urls = ["/"]
    counts = {c: build_lang(c, urls) for c in LANGS}
    # root: language picker
    picks = "".join(
        f'<a class="pick" href="/{c}/" lang="{c}" dir="{L.get("dir", "ltr")}"><strong>{html.escape(L["name"])}</strong>'
        f'<span>{html.escape(L["desc"])}</span></a>' for c, L in LANGS.items())
    alt = {c: f"/{c}/" for c in LANGS}
    alt["x-default"] = "/"
    write("index.html", page(None, CFG["title"], f'<header class="list-head"><h1>{CFG["title"]}</h1></header><div class="picks">{picks}</div>',
                             desc=CFG["desc"], alternates=alt, path="/"))
    write("404.html", page(None, "404", '<div class="empty"><h1>404</h1><p><a href="/">Cutroom Notes</a></p></div>'))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
          + "".join(f"<url><loc>{SITE_URL}{u}</loc></url>" for u in urls) + "</urlset>")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    print("built:", counts)


if __name__ == "__main__":
    main()
