"""Refresh _data/substack.json from the Substack RSS feed.

Run by .github/workflows/substack.yml once a day, and by hand with
    python tools/fetch_substack.py
Only the standard library is used, so the GitHub runner needs no installs.
"""
import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED = "https://edgarcastrom.substack.com/feed"
OUT = Path(__file__).resolve().parent.parent / "_data" / "substack.json"
NS = {"content": "http://purl.org/rss/1.0/modules/content/"}

MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]
MONTHS_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
             "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
SPANISH_WORDS = {"el", "la", "los", "las", "que", "de", "y", "en", "un", "una",
                 "por", "para", "con", "es", "no", "se", "del", "más", "como"}
ENGLISH_WORDS = {"the", "and", "of", "to", "a", "in", "is", "that", "it",
                 "for", "with", "on", "as", "are", "was", "this", "but"}


def plain(fragment):
    text = re.sub(r"<br\s*/?>|</p>", " ", fragment or "")
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def excerpt(text, words=45):
    parts = text.split()
    return text if len(parts) <= words else " ".join(parts[:words]).rstrip(",;:") + "…"


def language(text):
    tokens = re.findall(r"[a-záéíóúñü]+", text.lower())[:400]
    es = sum(t in SPANISH_WORDS for t in tokens)
    en = sum(t in ENGLISH_WORDS for t in tokens)
    return "es" if es > en else "en"


def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "ecastrom.github.io site builder"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())

    posts = []
    for item in root.find("channel").findall("item"):
        body = plain(item.findtext("content:encoded", namespaces=NS))
        when = parsedate_to_datetime(item.findtext("pubDate"))
        posts.append({
            "title": html.unescape(item.findtext("title") or "").strip(),
            "subtitle": plain(item.findtext("description")),
            "url": item.findtext("link"),
            "date": when.strftime("%Y-%m-%d"),
            "date_en": f"{MONTHS_EN[when.month - 1]} {when.day}, {when.year}",
            "date_es": f"{when.day} de {MONTHS_ES[when.month - 1]} de {when.year}",
            "lang": language(body),
            "excerpt": excerpt(body),
        })
    posts.sort(key=lambda p: p["date"], reverse=True)

    new = json.dumps(posts, ensure_ascii=False, indent=2) + "\n"
    if OUT.exists() and OUT.read_text(encoding="utf-8") == new:
        print("No new essays.")
        return
    OUT.write_text(new, encoding="utf-8")
    print(f"Wrote {len(posts)} essays to {OUT.name}")


if __name__ == "__main__":
    main()
