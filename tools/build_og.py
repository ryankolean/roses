#!/usr/bin/env python3
"""Compose the 1200x630 social cards from a photo plus the brand type.

Needs ImageMagick 7 and two variable fonts on disk. Run it when a card's
photo or wording changes:

    python3 tools/build_og.py
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHOTOS = ROOT / "assets" / "img" / "photos"
OUT = ROOT / "assets" / "img"

EB = Path("/tmp/rfonts/eb.ttf")
MONT = Path("/tmp/rfonts/mont.ttf")

PAPER = "#F0ECE6"
FOREST = "#2D332D"
EMBER = "#F97743"

W, H = 1200, 630

# name, photo, kicker, headline
CARDS = [
    ("og-default", "room-counter.jpg", "Detroit", "Witamy."),
    ("og-menu", "table-nachos.jpg", "The menu", "Written after\nthe delivery."),
    ("og-story", "kitchen.jpg", "Story", "My third business\nin this space."),
    ("og-press", "produce-peaches.jpg", "Press", "A good first year."),
]


def run(args):
    subprocess.run(args, check=True)


def build(name, photo, kicker, headline):
    src = PHOTOS / photo
    if not src.exists():
        sys.exit("error: missing photo %s" % src)
    dest = OUT / ("%s.jpg" % name)

    # Photo fills the right 46%, darkened band on the left carries the type.
    run([
        "magick", str(src),
        "-auto-orient", "-strip",
        "-resize", "%dx%d^" % (W, H), "-gravity", "center", "-extent", "%dx%d" % (W, H),
        "-fill", FOREST, "-colorize", "18%",
        # Opaque left column so the type always clears contrast. Gravity must be
        # NorthWest *before* the composite or the panel lands centred.
        "(", "-size", "%dx%d" % (int(W * 0.56), H), "xc:" + FOREST, ")",
        "-gravity", "NorthWest", "-geometry", "+0+0", "-compose", "over", "-composite",
        "-font", str(MONT), "-pointsize", "26", "-fill", EMBER,
        "-gravity", "NorthWest", "-annotate", "+72+108", kicker.upper(),
        "-font", str(EB), "-pointsize", "86", "-fill", PAPER,
        "-interline-spacing", "10",
        "-annotate", "+72+170", headline,
        "-font", str(MONT), "-pointsize", "24", "-fill", PAPER,
        "-gravity", "SouthWest", "-annotate", "+72+84",
        "10551 E Jefferson Ave, Detroit",
        "-font", str(MONT), "-pointsize", "20", "-fill", EMBER,
        "-annotate", "+72+48", "Concept by Summit Software Solutions",
        "-quality", "84", str(dest),
    ])
    return dest


def main():
    if not shutil.which("magick"):
        sys.exit("error: ImageMagick 7 (magick) not on PATH")
    for f in (EB, MONT):
        if not f.exists():
            sys.exit(
                "error: %s missing. Fetch the variable fonts first:\n"
                "  mkdir -p /tmp/rfonts && cd /tmp/rfonts\n"
                "  curl -sSL -o eb.ttf 'https://raw.githubusercontent.com/google/fonts/"
                "main/ofl/ebgaramond/EBGaramond%%5Bwght%%5D.ttf'\n"
                "  curl -sSL -o mont.ttf 'https://raw.githubusercontent.com/google/fonts/"
                "main/ofl/montserrat/Montserrat%%5Bwght%%5D.ttf'" % f
            )
    for card in CARDS:
        print("wrote", build(*card).relative_to(ROOT))


if __name__ == "__main__":
    main()
