# Roses

An unsolicited concept website for **Roses**, 10551 E. Jefferson Ave., Detroit, plus the research it was built from.

Detroit Free Press 2026 Restaurant of the Year. New York Times, 50 favorite restaurants in America. Detroit News three stars. Hour Detroit Best New Restaurants 2026. Chef and owner Molly Mitchell.

**Not affiliated with Roses.** The restaurant's live site is [rosesdetroit.com](https://rosesdetroit.com/). Every page here carries a banner saying so and is marked `noindex, nofollow`.

- **Concept site:** https://ryankolean.github.io/roses/
- **Research package:** https://ryankolean.github.io/roses/research/
- **Palette and type specimen:** https://ryankolean.github.io/roses/specimen.html
- **Ticket:** [SUMMIT-179](https://ryan-kolean.atlassian.net/browse/SUMMIT-179)

## Why it exists

The current site is an unedited Toast Sites template whose only real content is one JPEG of the menu. That image is unreadable at phone width and invisible to search engines, screen readers and AI crawlers. Three of its pages publish facts that are wrong: `/contact` carries the hours of the diner that closed in 2023, `/our-story` claims the business dates from 1964 when it opened in 2014, and `/gallery` advertises breakfast and lunch at a dinner-only restaurant. There is no reservation link, though the restaurant books on Resy, and none of the four awards are mentioned anywhere.

The brand itself is good. It is on the printed menu, and nobody has put it on the web.

## The site

Five pages, static HTML, no framework. Two small Python scripts run at deploy: the menu renderer and the stage step that decides what gets published.

| Page | What |
|---|---|
| `index.html` | Hero, awards, menu teaser, the room, the week's produce, hours |
| `menu.html` | The whole menu as text, dated, with `Menu` JSON-LD |
| `story.html` | 2014 to 2023, September 2025, the producers |
| `visit.html` | Hours, reservations, map, what to expect |
| `press.html` | Four awards, pull quotes, links to the originals |

What it fixes, against the live site: correct hours with Tuesday closed, a Resy link in the header on every page, the awards on the homepage, the true 2014 founding, complete `Restaurant` JSON-LD with `alternateName`, `geo`, `award` and `openingHoursSpecification`, real social cards, and a menu that is text.

## The menu is one text file

`content/menu.md` is the source of truth. It renders into three places, so nothing can drift:

1. the menu block on the homepage,
2. the full menu on `menu.html`,
3. the `Menu` JSON-LD in `menu.html`'s `<head>`.

**To change the menu**, edit [`content/menu.md`](content/menu.md) on github.com, change the `updated:` date at the top, and commit. The `Build and deploy` workflow regenerates the pages and republishes the site in about a minute. No HTML, no local setup.

Locally:

```bash
python3 tools/build_menu.py
```

Deployment runs from GitHub Actions rather than from the branch on purpose. A commit pushed by `GITHUB_TOKEN` does not trigger the branch-based Pages build, so a commit-back approach would look fine and silently never publish.

## Publishing and checks

`tools/build_site.py` copies the public files into `_site/`, the only directory GitHub Pages serves, and writes `robots.txt` and `sitemap.xml`. Research, tooling and framework files in the repo root are never published. A new page or asset folder has to be added to its allowlist.

The launch build is the same script in production mode: URLs moved to the real domain, `noindex` removed, the research and specimen pages left out.

```bash
SITE_MODE=production SITE_URL=https://rosesdetroit.com/ python3 tools/build_site.py
```

The site is adopted into the Summit website framework (SUMMIT-253, Level 2). `site/entity.json` and `site/brand.json` are the public facts the framework reads; decisions and the security report live in Summit's private intake repo. Every pull request runs:

| Workflow | What it checks |
|---|---|
| `ci` | `summit verify-split` (public facts only), menu pages in sync with `content/menu.md`, the framework's preview checks on `_site`, and a launch dry run against the production checks |
| `security` | The site-security gate: secrets, workflow and built-output scans. A Monday run monitors the live preview |

GitHub Pages cannot send headers, so the content security policy and referrer policy ship as meta tags. HSTS and clickjacking protection need real headers and wait for the production host.

**The hero** is the framework's `@summit/hero` component, rendered once and committed, since the site has no page build. `tools/build_hero.mjs` writes the component's markup into `index.html` (with a `<picture>` around its image, so the AVIF sources stay) and `assets/css/summit-hero.css` (the `--summit-*` tokens from `site/brand.json`, then the component's stylesheet). `style.css` maps those tokens onto the Roses palette. To change the hero, edit the script and run `npm ci --prefix tools && node tools/build_hero.mjs`.

**Photos.** `python3 tools/build_images.py` writes an AVIF for every width plus the smaller JPEGs. To add a photo, put the full-size JPEG in `assets/img/photos`, add it to the script's table, run it, and reference it with a `<picture>` like the others.

## Research

Written before a line of the site. Every color is measured from a Roses brand surface or derived from one by a stated blend, every contrast ratio is computed, and anything unverifiable is labeled rather than guessed.

| Path | What |
|---|---|
| [`design-catalog/rosesdetroit-com-design-spec.md`](design-catalog/rosesdetroit-com-design-spec.md) | Audit of the live site, including what Toast's Cloudflare layer does to crawlers |
| [`design-catalog/instagram-brand-intel.md`](design-catalog/instagram-brand-intel.md) | @roses_detroit: identity, voice, collaborators, gaps |
| [`design-catalog/press-and-story.md`](design-catalog/press-and-story.md) | Awards, pull quotes, the real lineage, photography leads |
| [`design-catalog/competitive-scan.md`](design-catalog/competitive-scan.md) | How ten Detroit peers publish a changing menu |
| [`design-catalog/site-elements.md`](design-catalog/site-elements.md) | Prioritized element inventory, plus the transcribed menu |
| [`design-catalog/brand-guidelines.md`](design-catalog/brand-guidelines.md) | Palette, type, style guide, motif system, logo rules, voice |
| [`design-catalog/build-recommendation.md`](design-catalog/build-recommendation.md) | Stack, menu-update path, DNS position, estimate |
| [`design-catalog/assets-needed.md`](design-catalog/assets-needed.md) | Everything we need from the owner, in one list |
| [`docs/dns-rosesdetroit.md`](docs/dns-rosesdetroit.md) | Zone capture. Mail is Google Workspace on IONOS, so the registrar stays put |

## Brand system

Four measured anchors, from [`brand-guidelines.md`](design-catalog/brand-guidelines.md):

| Token | Value | Source |
|---|---|---|
| `--sage` | `#B3CDB4` | Printed menu ground, dominant of ~128k sampled pixels |
| `--crimson` | `#9C1B22` | Printed menu ink and illustration |
| `--ember` | `#F97743` | `redbow.png`, the logo bow |
| `--paper` | `#F0ECE6` | The live site's page background |

Type is EB Garamond and Montserrat, both visual matches to the printed menu's faces. The menu's ornate display face could not be identified from a JPEG and is deliberately absent rather than half-matched.

Every text and background pair in use passes WCAG AA. Three combinations fail and are documented as forbidden, including paper on ember at 2.30:1, which is why primary buttons take forest text.

## Known placeholders

Marked on the pages themselves, and tracked in [`assets-needed.md`](design-catalog/assets-needed.md):

- **Photography** is the restaurant's own, from [@roses_detroit](https://www.instagram.com/roses_detroit/), used to demonstrate a direction. Authorship is not credited in their captions, so rights are unconfirmed.
- **The drinks list** has never been published anywhere, so there was nothing accurate to reproduce.
- **Parking, transit and accessibility** specifics are unconfirmed, so the pages say so instead of guessing.
- **The bow mark** is their 2.1MB PNG. It needs redrawing as SVG.
- **The story page** quotes Molly Mitchell's own Instagram post and would need her permission.

## Local preview

```bash
python3 tools/build_site.py
python3 -m http.server 4323 --directory _site
```

Then `http://localhost:4323/`.

## Precedent

Mirrors [`ryankolean/umbo`](https://github.com/ryankolean/umbo) and [`ryankolean/meantime`](https://github.com/ryankolean/meantime): static multi-page HTML on GitHub Pages. The one deviation is the Markdown-sourced menu, because this menu changes and the owner has to be able to change it.
