# Roses

Research and design package for a new website for **Roses**, 10551 E. Jefferson Ave., Detroit.

Detroit Free Press 2026 Restaurant of the Year. New York Times 2026 list of its 50 favourite restaurants in America. Detroit News three stars. Hour Detroit Best New Restaurants 2026. Chef/owner Molly Mitchell.

**Status:** research only. No production code, no domain changes, no contact with the owner. Tracked as [SUMMIT-179](https://ryan-kolean.atlassian.net/browse/SUMMIT-179).

## The short version

The current site, `rosesdetroit.com`, is an unedited Toast Sites template. Its only real content is one JPEG of the menu, which is unreadable at phone width and invisible to search engines, screen readers and AI crawlers. Every prose page is machine-written boilerplate, and three of those pages publish **facts that are wrong**: the hours belong to the diner that closed in 2023, the story page claims the business dates from 1964 when it opened in 2014, and the gallery advertises breakfast and lunch at a dinner-only restaurant. There is no reservation link, although the restaurant books on Resy. None of the four awards are mentioned.

The brand itself is good. It is on the printed menu, which nobody has put on the web.

## Contents

| Path | What |
|---|---|
| [`design-catalog/rosesdetroit-com-design-spec.md`](design-catalog/rosesdetroit-com-design-spec.md) | Full audit of the live site: platform, IA, measured palette and type, accessibility, SEO, and what Toast's Cloudflare layer does to crawlers |
| [`design-catalog/instagram-brand-intel.md`](design-catalog/instagram-brand-intel.md) | @roses_detroit: identity, voice, collaborators, and the gap between the feed and the site |
| [`design-catalog/press-and-story.md`](design-catalog/press-and-story.md) | Awards timeline, pull quotes, the real Rose's Fine Food lineage, photography leads |
| [`design-catalog/competitive-scan.md`](design-catalog/competitive-scan.md) | How ten Detroit peers publish a menu that changes |
| [`design-catalog/site-elements.md`](design-catalog/site-elements.md) | Every element the new site needs, prioritised, plus the full transcribed menu |
| [`design-catalog/brand-guidelines.md`](design-catalog/brand-guidelines.md) | Palette, type, style guide, motif system, logo rules, voice |
| [`design-catalog/build-recommendation.md`](design-catalog/build-recommendation.md) | Stack, the menu-update path, DNS position, estimate |
| [`design-catalog/assets-needed.md`](design-catalog/assets-needed.md) | One list of everything we need from the owner |
| [`docs/dns-rosesdetroit.md`](docs/dns-rosesdetroit.md) | Zone capture and cutover rules. Mail is Google Workspace; do not transfer the registrar |
| [`specimen.html`](specimen.html) | Rendered palette and type specimen, for visual approval |

## Method

Every colour is **measured** from a Roses brand surface, or derived from a measured one by a stated blend. Every contrast ratio is computed, not eyeballed. Anything that could not be verified is labelled unverified rather than guessed, including the three fonts on the printed menu, which cannot be identified from a JPEG.

The live site sits behind Cloudflare's managed challenge, which returns 403 to plain HTTP clients. That challenge is **Toast's**, not the restaurant's, and a normal browser clears it with no interaction, so the audit was done in a rendered session. Nothing was bypassed.

## Precedent

Mirrors [`ryankolean/umbo`](https://github.com/ryankolean/umbo) and [`ryankolean/meantime`](https://github.com/ryankolean/meantime): static multi-page HTML, no build step, GitHub Pages. The one deviation is a Markdown-sourced menu, because this menu changes and the owner has to be able to change it.

## Local preview

```bash
python3 -m http.server 4323 --directory ~/roses
```

Then open `http://localhost:4323/specimen.html`.
