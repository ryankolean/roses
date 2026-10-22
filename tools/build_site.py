#!/usr/bin/env python3
"""Stage the public site into _site/, the only directory that gets published.

The repo root also holds research, tooling and framework metadata. Publishing
the root would serve all of it, so this copies an explicit allowlist instead.

Two modes, chosen by SITE_MODE:

  preview     (default) the concept on ryankolean.github.io/roses: every page
              stays noindex, concept-package pages included.
  production  the launch build: SITE_URL replaces the preview URL everywhere,
              the noindex meta is removed, and the concept-package pages
              (research, specimen) are left out.

Both modes write robots.txt and sitemap.xml. Pages are kept out of search by
their noindex meta, never by robots.txt, so crawlers can still read the meta.

Run it with:  python3 tools/build_site.py
              SITE_MODE=production SITE_URL=https://rosesdetroit.com/ python3 tools/build_site.py
"""

import os
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"
PREVIEW_URL = "https://ryankolean.github.io/roses/"

PAGES = ["index.html", "menu.html", "story.html", "visit.html", "press.html"]
CONCEPT_PAGES = ["specimen.html", "research/index.html"]
FILES = ["favicon.ico", "site.webmanifest"]
DIRS = ["assets"]

# Text files that carry absolute URLs and are rewritten in production.
REWRITE = {".html", ".txt", ".xml", ".webmanifest", ".json"}
NOINDEX = re.compile(r'[ \t]*<meta name="robots" content="noindex, nofollow">\n')


def settings():
    mode = os.environ.get("SITE_MODE", "preview")
    if mode not in ("preview", "production"):
        sys.exit("error: SITE_MODE must be preview or production, not %r" % mode)
    url = os.environ.get("SITE_URL", PREVIEW_URL if mode == "preview" else "")
    if not re.fullmatch(r"https://[^/\s]+/(?:[^\s]*/)?", url):
        sys.exit("error: SITE_URL must be an https URL ending in /, got %r" % url)
    return mode, url


def stage(mode):
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    pages = PAGES + (CONCEPT_PAGES if mode == "preview" else [])
    for rel in pages + FILES:
        src = ROOT / rel
        if not src.exists():
            sys.exit("error: %s is in the allowlist but missing" % rel)
        dest = OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    for rel in DIRS:
        shutil.copytree(ROOT / rel, OUT / rel)
    return pages


def rewrite(mode, url):
    """Point absolute URLs at SITE_URL, and open production pages to search."""
    for path in OUT.rglob("*"):
        if not path.is_file() or path.suffix not in REWRITE:
            continue
        text = path.read_text(encoding="utf-8")
        new = text.replace(PREVIEW_URL, url)
        if mode == "production" and path.suffix == ".html":
            new = NOINDEX.sub("", new)
        if new != text:
            path.write_text(new, encoding="utf-8")


def page_url(url, rel):
    return url + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)


def write_crawl_files(url, pages):
    (OUT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % url, encoding="utf-8"
    )
    rows = "\n".join(
        "  <url><loc>%s</loc></url>" % page_url(url, rel) for rel in pages
    )
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        "%s\n</urlset>\n" % rows,
        encoding="utf-8",
    )


def main():
    mode, url = settings()
    pages = stage(mode)
    rewrite(mode, url)
    write_crawl_files(url, pages)
    files = sum(1 for p in OUT.rglob("*") if p.is_file())
    print("_site: %s build for %s, %d pages, %d files" % (mode, url, len(pages), files))


if __name__ == "__main__":
    main()
