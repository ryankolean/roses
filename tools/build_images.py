#!/usr/bin/env python3
"""Write the responsive variants of each photo.

The full-size JPEG in assets/img/photos is the source. For every width listed
below, write <name>@<w>.jpg if it is missing, and write <name>@<w>.avif plus a
full-size <name>.avif. Pages load them through <picture>: AVIF first, the
JPEGs as the fallback srcset. Widths come from the rendered sizes at 375, 768
and 1280px, at 1x and 2x.

Existing files are left alone, so re-running only fills gaps. Needs
ImageMagick 7 built with AVIF. Run it when a photo is added or replaced:

    python3 tools/build_images.py
"""

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PHOTOS = ROOT / "assets" / "img" / "photos"

# Same settings as the original derivatives: q78, 4:2:0, progressive.
JPEG = ["-quality", "78", "-sampling-factor", "4:2:0", "-interlace", "JPEG"]
AVIF = ["-quality", "55"]

# photo -> widths below full size. Split-column photos render at 343 to 720px
# on a phone or tablet and 428px on a desktop; gallery photos at 229 to 343px.
WIDTHS = {
    "room-counter.jpg": [900],
    "counter-candles.jpg": [450, 900],
    "table-nachos.jpg": [450, 900],
    "kitchen.jpg": [450, 900],
    "produce-shelf.jpg": [450, 900],
    "produce-peaches.jpg": [600, 900],
    "produce-cabbage.jpg": [600, 900],
    "produce-cucumbers.jpg": [600, 900],
    "produce-cabbages.jpg": [600, 900],
}


def write(src, dest, width, fmt):
    if dest.exists():
        return False
    args = ["magick", str(src), "-auto-orient", "-strip"]
    if width:
        args += ["-resize", "%dx" % width]
    subprocess.run(args + fmt + [str(dest)], check=True)
    return True


def main():
    if not shutil.which("magick"):
        sys.exit("error: ImageMagick 7 (magick) not on PATH")
    wrote = []
    for name, widths in WIDTHS.items():
        src = PHOTOS / name
        if not src.exists():
            sys.exit("error: missing photo %s" % src)
        stem = src.stem
        targets = [(PHOTOS / ("%s.avif" % stem), None, AVIF)]
        for w in widths:
            targets.append((PHOTOS / ("%s@%d.jpg" % (stem, w)), w, JPEG))
            targets.append((PHOTOS / ("%s@%d.avif" % (stem, w)), w, AVIF))
        for dest, w, fmt in targets:
            if write(src, dest, w, fmt):
                wrote.append(dest)
    for path in wrote:
        print("wrote %s (%d KB)" % (path.relative_to(ROOT), path.stat().st_size // 1024))
    print("%d new files" % len(wrote))


if __name__ == "__main__":
    main()
