# AGENTS.md

Concept site for Roses, adopted into the Summit website framework (SUMMIT-243,
adoption SUMMIT-253 Level 2). Read `README.md` first.

## Rules

- **This repo is public.** `site/entity.json` and `site/brand.json` hold public
  facts only. Private intake, decisions and the security report live in the
  private `summit-intake` repo under `roses/`, never here. CI runs
  `summit verify-split` to enforce this.
- **Every page says it is a concept and is `noindex, nofollow`** until the owner
  signs. Do not remove the concept banner or the robots meta in a preview build.
- **The menu has one source:** `content/menu.md`. Never hand-edit the blocks
  between `MENU:START`/`MENU:END` or `MENU_JSONLD:START`/`MENU_JSONLD:END`; run
  `python3 tools/build_menu.py`.
- **The homepage hero is `@summit/hero`.** Never hand-edit the block between
  `HERO:START`/`HERO:END` or `assets/css/summit-hero.css`; change
  `tools/build_hero.mjs` or `site/brand.json` and run
  `npm ci --prefix tools && node tools/build_hero.mjs`. The token remaps and
  layout that make it look like Roses are in `style.css`.
- **Publish `_site/`, never the repo root.** `python3 tools/build_site.py` stages
  the public files. A new top-level page or asset folder must be added to its
  allowlist or it will not ship.
- **No inline `style` attributes or inline executable scripts** on the five site
  pages; the Content-Security-Policy meta tag allows `'self'` only. JSON-LD
  data blocks are fine. Keep the policy identical on all five pages.
- **Photos go through `tools/build_images.py`** and a `<picture>` with AVIF
  first, like the existing ones.
- **Motion is one page crossfade and nothing else** (`brand-guidelines.md`,
  Motion). No scroll reveals, no animation or smooth-scroll library.
- Branch and open a PR for every change; CI must pass before merging.
- Conventional commits, no emojis, no em dashes.

## Verify before opening a PR

`summit` is the Summit CLI; install it from the pinned commit in
`.github/workflows/ci.yml` (`npm install --global <that URL>`).

```bash
python3 tools/build_menu.py && git diff --exit-code
python3 tools/build_site.py
summit verify-split .
summit check gate _site --mode preview --base /roses/
```

UI changes: serve `_site` (launch config `roses`), check 375, 768 and 1280 px,
no horizontal overflow at 375, no console errors.
