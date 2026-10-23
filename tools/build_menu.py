#!/usr/bin/env python3
"""Render content/menu.md and content/drinks.md into the pages that show them.

Two source files, four outputs: the menu block on the homepage, the menu and
drinks blocks on menu.html, and the Menu JSON-LD on menu.html. Nothing can
drift, because nothing is typed twice.

Run it with:  python3 tools/build_menu.py
"""

import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "content" / "menu.md"
DRINKS = ROOT / "content" / "drinks.md"

TARGETS = [
    (ROOT / "index.html", "MENU", "home"),
    (ROOT / "menu.html", "MENU", "full"),
    (ROOT / "menu.html", "DRINKS", "drinks"),
    (ROOT / "menu.html", "MENU_JSONLD", "jsonld"),
]

# Sections shown on the homepage teaser, in order, and how many dishes each.
HOME_TEASER = {"Przystawki": 4, "Danie główne": 4}


def parse(text):
    """-> (meta dict, [(section, [(name, desc, price)])])"""
    meta = {}
    if text.startswith("---"):
        _, front, text = text.split("---", 2)
        for line in front.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()

    sections, section, dish = [], None, None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("# "):
            section = (line[2:].strip(), [])
            sections.append(section)
            dish = None
        elif line.startswith("## "):
            if section is None:
                sys.exit("error: dish '%s' appears before any section heading" % line[3:])
            dish = {"name": line[3:].strip(), "desc": [], "price": ""}
            section[1].append(dish)
        elif line.startswith("$") and dish is not None:
            dish["price"] = line
        elif line and dish is not None:
            dish["desc"].append(line)

    out = []
    for name, dishes in sections:
        rows = [(d["name"], " ".join(d["desc"]), d["price"]) for d in dishes]
        out.append((name, rows))
    return meta, out


def pretty_date(iso):
    try:
        d = date.fromisoformat(iso)
    except ValueError:
        return iso
    return "%d %s %d" % (d.day, d.strftime("%B"), d.year)


def text(s):
    """Escape for HTML text nodes, and use a typographic apostrophe."""
    return html.escape(s, quote=False).replace("'", "’")


def dish_html(name, desc, price, indent):
    pad = " " * indent
    tail = " ".join(x for x in (desc, price) if x)
    return (
        '%s<div class="dish">\n'
        '%s  <p class="dish__name">%s</p>\n'
        '%s  <p class="dish__desc">%s</p>\n'
        "%s</div>" % (pad, pad, text(name), pad, text(tail), pad)
    )


def render_sections(sections, indent, limit=None):
    blocks = []
    for name, rows in sections:
        if limit is not None and name not in limit:
            continue
        shown = rows[: limit[name]] if limit else rows
        pad = " " * indent
        body = "\n".join(dish_html(n, d, p, indent + 4) for n, d, p in shown)
        blocks.append(
            '%s<div class="menu-section">\n'
            '%s  <p class="label">%s</p>\n'
            '%s  <svg class="wheat" aria-hidden="true"><use href="assets/img/motifs.svg#wheat"/></svg>\n'
            "%s\n"
            "%s</div>" % (pad, pad, text(name), pad, body, pad)
        )
    return "\n".join(blocks)


def stamp(meta, what="Menu", artist=False):
    parts = ["%s as of %s" % (what, pretty_date(meta.get("updated", "")))]
    if meta.get("note"):
        parts.append(html.escape(meta["note"]))
    # The printed menu features a Detroit artist each edition; credit them.
    if artist and meta.get("artist"):
        parts.append("Featured artist: %s" % html.escape(meta["artist"]))
    return '      <p class="menu-stamp">%s</p>\n' % " &middot; ".join(parts)


def render_home(meta, sections):
    grid = (
        '      <div class="menu-grid">\n%s\n      </div>'
        % render_sections(sections, 8, HOME_TEASER)
    )
    return stamp(meta) + grid


def render_full(meta, sections):
    grid = (
        '      <div class="menu-grid">\n%s\n      </div>'
        % render_sections(sections, 8)
    )
    return stamp(meta, artist=True) + grid


def render_drinks(meta, sections):
    grid = (
        '      <div class="menu-grid">\n%s\n      </div>'
        % render_sections(sections, 8)
    )
    return stamp(meta, "Drinks") + grid


def menu_item(name, desc, price):
    item = {"@type": "MenuItem", "name": name, "description": desc}
    # Only a single plain amount is a valid Offer price. "$27/54" is two prices,
    # so it stays in the description rather than becoming invalid structured data.
    if re.fullmatch(r"\$\d+(\.\d{2})?", price):
        item["offers"] = {
            "@type": "Offer",
            "price": price.lstrip("$"),
            "priceCurrency": "USD",
        }
    else:
        item["description"] = " ".join(x for x in (desc, price) if x)
    return item


def menu_section(name, rows):
    return {
        "@type": "MenuSection",
        "name": name,
        "hasMenuItem": [menu_item(n, d, p) for n, d, p in rows],
    }


def render_jsonld(menu, drinks):
    (meta, sections), (dmeta, dsections) = menu, drinks
    doc = {
        "@context": "https://schema.org",
        "@type": "Menu",
        "name": "Roses dinner menu",
        "dateModified": max(meta.get("updated", ""), dmeta.get("updated", "")),
        "inLanguage": "en-US",
        "hasMenuSection": [menu_section(n, rows) for n, rows in sections]
        + [
            {
                "@type": "MenuSection",
                "name": "Drinks",
                "hasMenuSection": [menu_section(n, rows) for n, rows in dsections],
            }
        ],
    }
    body = json.dumps(doc, indent=2, ensure_ascii=False)
    return '<script type="application/ld+json">\n%s\n</script>' % body


RENDERERS = {
    "home": lambda menu, drinks: render_home(*menu),
    "full": lambda menu, drinks: render_full(*menu),
    "drinks": lambda menu, drinks: render_drinks(*drinks),
    "jsonld": render_jsonld,
}


def splice(path, marker, block):
    text = path.read_text(encoding="utf-8")
    start, end = "<!-- %s:START -->" % marker, "<!-- %s:END -->" % marker
    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end), re.DOTALL
    )
    if not pattern.search(text):
        sys.exit("error: %s has no %s block" % (path.name, marker))
    new = pattern.sub(lambda _: "%s\n%s\n%s" % (start, block, end), text, count=1)
    if new == text:
        return False
    path.write_text(new, encoding="utf-8")
    return True


def load(path):
    if not path.exists():
        sys.exit("error: %s is missing" % path)
    meta, sections = parse(path.read_text(encoding="utf-8"))
    if not sections:
        sys.exit("error: no sections parsed from %s" % path.name)
    print(
        "%s: %d sections, %d items, updated %s"
        % (path.name, len(sections), sum(len(r) for _, r in sections), meta.get("updated", "?"))
    )
    return meta, sections


def main():
    menu, drinks = load(SOURCE), load(DRINKS)

    changed = []
    for path, marker, kind in TARGETS:
        if splice(path, marker, RENDERERS[kind](menu, drinks)):
            changed.append("%s (%s)" % (path.name, marker))

    print("changed: %s" % (", ".join(changed) if changed else "nothing"))


if __name__ == "__main__":
    main()
