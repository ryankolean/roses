# Brand Guidelines: Roses

**Version:** 1.0, 2026-09-20. Research output, pending owner approval.

Every value here is either **measured** from a brand surface Roses already owns, or **derived** from a measured value by a stated operation. Nothing is invented. Where a source asset could not be identified, it says so.

## Principle

Roses already has a brand. It is on the printed menu, not on the website. The job is not to design an identity; it is to extract the one that exists and give it a system.

Three measured anchors carry everything:

| Anchor | Value | Source | How measured |
|---|---|---|---|
| **Sage** | `#B3CDB4` | The printed menu's ground | Dominant colour, 75,996 of ~128,000 sampled pixels in `Roses_menu_web_Aug_26.jpg` |
| **Crimson** | `#9C1B22` | The printed menu's ink, and every illustration | Clustered red pixels; JPEG compression spreads it `#9A1C22`-`#9C1B22` |
| **Ember** | `#F97743` | `redbow.png`, the logo mark | Dominant opaque colour across 41,562 sampled pixels |

A fourth is measured from the live site: **Bone `#F0ECE6`**, the page background the restaurant chose in Toast's theme editor.

## Color

### Tokens

```css
:root {
  /* Measured from brand surfaces */
  --paper:        #F0ECE6;  /* page field. Measured: live site body background */
  --sage:         #B3CDB4;  /* section alternation. Measured: printed menu ground */
  --crimson:      #9C1B22;  /* primary ink. Measured: printed menu type + illustration */
  --ember:        #F97743;  /* accent, CTA fill. Measured: redbow.png */

  /* Derived, with the operation stated */
  --sage-pale:    #D5DED0;  /* --sage blended 55% toward --paper. Quiet tint blocks */
  --forest:       #2D332D;  /* --sage blended 75% toward black. Dark sections, footer */
  --crimson-deep: #701318;  /* --crimson blended 28% toward black. Link hover, pressed */
  --ink-mute:     #5C6B5C;  /* desaturated --forest. Secondary text on --paper only */
}
```

**Roles.** `--paper` is the default page. `--sage` and `--sage-pale` alternate sections. `--forest` is the one dark section per page plus the footer. `--crimson` is body text, headings and links. `--ember` is reserved: primary CTA fill, the logo, and the active state. Using ember for anything else dilutes the only mark the brand has.

### Why these and not the site's current values

The live site's green `#3D8B61` and orange `#E8682D` are Toast theme picks that gesture at the menu without matching it, and both fail contrast (`3.52:1` and `2.77:1` on bone). The menu's own sage and crimson are the real colours, they are darker and more saturated, and crimson clears AA on every background in the system. Adopting the menu's palette is both more accurate to the brand and the fix for the accessibility failure.

### WCAG AA contrast, every pair in use

Computed to WCAG 2.1 relative luminance. **AA** requires 4.5:1 normal text, 3:1 large text (≥18.66px bold or ≥24px).

| Foreground | Background | Ratio | AA normal | AA large | AAA |
|---|---|---|---|---|---|
| `--crimson` `#9C1B22` | `--paper` `#F0ECE6` | **6.88** | pass | pass | — |
| `--crimson` | `--sage` `#B3CDB4` | **4.75** | pass | pass | — |
| `--crimson` | `--sage-pale` `#D5DED0` | **5.86** | pass | pass | — |
| `--crimson-deep` `#701318` | `--paper` | **9.94** | pass | pass | pass |
| `--crimson-deep` | `--sage` | **6.86** | pass | pass | — |
| `--forest` `#2D332D` | `--paper` | **11.00** | pass | pass | pass |
| `--forest` | `--sage` | **7.58** | pass | pass | pass |
| `--forest` | `--sage-pale` | **9.36** | pass | pass | pass |
| `--forest` | `--ember` `#F97743` | **4.77** | pass | pass | — |
| `--paper` | `--forest` | **11.00** | pass | pass | pass |
| `--paper` | `--crimson` | **6.88** | pass | pass | — |
| `--paper` | `--crimson-deep` | **9.94** | pass | pass | pass |
| `--sage` | `--forest` | **7.58** | pass | pass | pass |
| `--ember` | `--forest` | **4.77** | pass | pass | — |
| `--ink-mute` `#5C6B5C` | `--paper` | **4.81** | pass | pass | — |

### Forbidden pairs

Three combinations fail and must never ship. They are listed here so nobody reinvents them.

| Foreground | Background | Ratio | Rule |
|---|---|---|---|
| `--paper` | `--ember` | **2.30** | **Never.** Ember buttons take `--forest` text, not white or cream |
| `--crimson` | `--ember` | **2.99** | **Never.** Red on orange fails and also looks bad |
| `--ink-mute` | `--sage` | **3.32** | Large text only. Secondary text on sage uses `--forest` |

## Typography

### What the brand actually uses

The printed menu sets three distinct voices, and identifying the exact licensed files from a JPEG is not possible. Each is described by its letterforms, then matched.

| Role on the menu | Observed characteristics | Status |
|---|---|---|
| The word **"Menu"** | Ornate Victorian display. Heavy stems, fine inline curls, a spiral swash on the `M`, looping terminals | **Unidentified.** Get the source file from whoever designed the menu |
| **"Witamy!"** | Bouncy monoline script, widely letter-spaced, letters separated rather than joined | **Unidentified** |
| **Section heads and dish names** (`MAINS`, `Pierogi Ruskie`) | Geometric sans, heavy. Double-storey `a`, pointed `A` apex, straight-legged `R`, single-storey `g` with an open tail | **Visual match: Montserrat Bold / ExtraBold.** Not confirmed |
| **Dish descriptions** | Renaissance oldstyle serif. High stroke contrast, sharp calligraphic terminals, **oldstyle figures** (`$24`, `$16` sit at x-height), a distinctive angled hyphen | **Visual match: EB Garamond.** Not confirmed |

### The system to build with

Both matches are on Google Fonts, both are free to self-host, and together they reproduce the menu's feel closely enough to read as the same brand. Swap them for the licensed originals the moment the owner supplies them.

```css
--font-display: "EB Garamond", Georgia, "Times New Roman", serif;  /* headings, pull quotes, dish descriptions */
--font-ui:      "Montserrat", system-ui, -apple-system, sans-serif; /* dish names, section labels, buttons, nav */
```

**Why this pairing and not the site's Inconsolata:** the current site sets a Free Press Restaurant of the Year in a monospace terminal font at a flat 16/20px. The menu sets dish names in a heavy geometric sans and descriptions in an oldstyle serif. The menu is right and the site is wrong; the type system should follow the menu.

**The ornate display face is a deliberate gap.** Until the original is recovered, headings use EB Garamond and the Victorian display face appears **only** in the logo lockup as artwork, not as live text. Do not substitute a lookalike Victorian webfont: half-matching an ornate display face looks worse than not using one.

### Scale

Desktop (≥900px):

| Element | Family | Size | Weight | Line height | Tracking |
|---|---|---|---|---|---|
| Display / hero | EB Garamond | 68px | 500 | 1.05 | -0.01em |
| h1 | EB Garamond | 52px | 500 | 1.1 | -0.01em |
| h2 | EB Garamond | 38px | 500 | 1.15 | normal |
| h3 | EB Garamond | 27px | 600 | 1.25 | normal |
| Lede | EB Garamond | 22px | 400 | 1.5 | normal |
| Body | EB Garamond | 19px | 400 | 1.65 | normal |
| Dish name | Montserrat | 19px | 700 | 1.3 | normal |
| Dish description | EB Garamond | 17px | 400 | 1.5 | normal |
| Section label | Montserrat | 13px | 700 | 1.2 | **0.14em, uppercase** |
| Button | Montserrat | 15px | 700 | 1 | 0.04em |
| Small / caption | Montserrat | 14px | 400 | 1.45 | normal |

Mobile (<640px): display 40px · h1 34px · h2 28px · h3 22px · lede 19px · body 18px · dish name 18px · description 16px. Labels, buttons and captions do not shrink.

**Body is 19px, not 16px.** EB Garamond has a small x-height; at 16px it reads smaller than a 16px sans. 19px is the equivalent optical size.

### Usage rules

- **EB Garamond for everything readable.** Montserrat is only for dish names, uppercase labels, buttons and nav.
- **Oldstyle figures on the menu, lining figures for prices in running text.** EB Garamond defaults to oldstyle, which matches the printed menu exactly. Keep them on the menu page.
- **Never set body copy in Montserrat.** It is a display weight in this system.
- Uppercase is for section labels only. Never uppercase a heading or a dish name.

## Motif system

The equivalent of Umbo's scallop shell, and it already exists.

**Polish papercut folk art, *wycinanki*.** Observed on the printed menu, all in a single crimson ink weight:

1. A rose rendered as a symmetrical papercut rosette with leaves
2. Wheat sheaves, used as a repeating horizontal separator
3. A peacock among stylised foliage
4. A woman in a headscarf carrying a basket of bread
5. A footed bowl heaped with fruit
6. Wavy stacked rules as a section divider

### Rules

- **One ink, always.** Crimson on light grounds, paper on `--forest`. Never two-colour, never gradient, never drop-shadow.
- **The wavy rule is the section divider** across the whole site. It is the cheapest, most repeatable piece of the system.
- **Wheat is the list separator** between menu sections.
- **Figures are punctuation, not illustration.** One per section, set small in a margin, the way the menu uses them. Never a hero image, never a background pattern.
- Vectorise all six from the source artwork. Do not trace from the JPEG; get the originals.
- **Do not add new motifs.** If something new is needed, commission it from whoever drew these.

**Why this and not flowers:** flowers are the room, and the room should be photographed, not illustrated. The papercut world is the menu, it is specifically Polish, it is unique in Detroit dining, and it scales to a divider at 24px and a page ornament at 400px without changing character.

## Logo

- **The mark is the bow**, `redbow.png`, ember `#F97743`, native 2236x1073.
- **There is no wordmark.** One does not exist in any surface captured. The site sets the name in Inconsolata, which is not a wordmark, it is a fallback.
- **Clear space:** one bow-height on all four sides.
- **Minimum size:** 72px wide. Below that the ribbon loops fill in.
- **Colour:** ember on `--paper`, `--sage` or `--sage-pale`. Paper on `--forest`. Never crimson-on-ember, never on a photograph.
- **The bow must be redrawn as SVG.** A 2.1MB PNG is the current favicon and the current header logo. This is a required deliverable before any build.

**Open question for the owner:** the bow reads as a gift ribbon, and its filename says "red" while the artwork is orange. Is it the intended permanent mark, or a placeholder? A wordmark pairing the bow with "Roses" set in the menu's Victorian display face would be the strongest version, and needs both the bow source and the display font. Logged in [`assets-needed.md`](assets-needed.md).

## Style guide

### Spacing

An 8px base, geometric rather than linear so section rhythm has room.

```css
--s-1: 4px;  --s-2: 8px;   --s-3: 12px;  --s-4: 16px;
--s-5: 24px; --s-6: 32px;  --s-7: 48px;  --s-8: 64px;
--s-9: 96px; --s-10: 128px;
```

Section padding: `--s-9` desktop, `--s-7` mobile. Container max-width **1120px**, gutter `--s-5` desktop / `--s-4` mobile.

### Radii, borders, shadows

```css
--radius-sm: 2px;   /* inputs, small chips */
--radius-pill: 999px; /* buttons only */
--border: 1px solid var(--crimson);
--border-hair: 1px solid color-mix(in srgb, var(--crimson) 25%, transparent);
```

**No shadows anywhere.** The brand is printed matter in one ink. Depth comes from the sage/paper/forest alternation, not from elevation. A shadow on a papercut motif would break the whole conceit.

Radii are near-zero on purpose. The one exception is the pill button, which is measured from the current site's CTA and is the one Toast-era shape worth keeping.

### Buttons

| Variant | Fill | Text | Border | Hover | Focus |
|---|---|---|---|---|---|
| Primary | `--ember` | `--forest` (**4.77:1**) | none | fill darkens 8% | 2px `--crimson` outline, 2px offset |
| Secondary | transparent | `--crimson` (**6.88:1** on paper) | `--border` | fill `--crimson`, text `--paper` (**6.88:1**) | same |
| Ghost | transparent | `--crimson` | none, underline on hover | `--crimson-deep` | same |
| On forest | `--ember` | `--forest` | none | fill lightens 8% | 2px `--paper` outline |

Padding `--s-3` / `--s-6`. Montserrat 700, 15px, `0.04em`. Minimum target 44x44.

**Primary buttons take forest text, never paper.** Paper on ember is 2.30:1. This is the rule most likely to be broken by someone eyeballing it.

### Forms

Transparent field on `--paper`, `--border-hair` on three sides and `--border` on the bottom, `--radius-sm`. Label above in the section-label style. Focus: bottom border thickens to 2px `--crimson` plus a 2px offset outline. Error text in `--crimson-deep`, never ember. Placeholders are **not** labels.

### Cards, menu rows, dividers

- **Menu row:** dish name (Montserrat 700) on its own line, price inline at the end of the description, matching the printed menu exactly — the menu does not use dot leaders or a right-aligned price column, and neither should the site. Dietary tags `(v)`, `(gf)` inline in the description, as printed.
- **Menu section:** uppercase label, wheat separator, then rows. `--s-7` between sections.
- **Card:** `--sage-pale` fill, no border, no shadow, `--s-6` padding, `--radius-sm`.
- **Divider:** the wavy rule motif, full container width, crimson, `--s-8` above and below.

### Image treatment

- Photographs are **untreated**. No duotone, no overlay, no filter. The room is candlelit and warm already; the palette was pulled from it.
- Square or 4:5 for plates, 3:2 for the room.
- Every image gets real alt text naming the dish or what is happening. The current site's `"Menu featuring Polish cuisine with various traditional dishes"` is the standard to beat.
- Illustration and photography never overlap in the same block.

### Motion

- Transitions **150ms ease-out** on colour and border only.
- No scroll reveals, no parallax, no carousels.
- `@media (prefers-reduced-motion: reduce)` sets every duration to `0.01ms`.

The restraint is the point: a menu is the primary content and motion between a reader and a menu is friction.

## Voice and tone

Derived from captions in [`instagram-brand-intel.md`](instagram-brand-intel.md). The register already exists and it is Molly's.

**Do**
- Write in her voice, first person where it is her speaking. Sign story copy with her name.
- Lead with the food and the people who grew it. The NYT post spent more words thanking farms than celebrating the award; the site should behave the same way.
- Name names. Lillian's Loaves, Amalgam Farms, Ma Coen's, Marrow, The Flowering Hearth.
- Keep the Polish. *Witamy.* *Uszka.* *Gołąbki.* Diacritics correct, no translations in parentheses on the menu; a short glossary elsewhere if wanted.
- Be plain about the practical things. Closed Tuesday. Walk-ins welcome. Reservations 30 days out.
- Say when the menu changed. A date is a kindness.

**Don't**
- No third-person restaurant-speak. Not "Rose's invites you to experience."
- No template warmth. "Join Our Family", "Community Heart" and "where the magic happens" are currently on the live site and all three have to go.
- **Never claim 1964.** The building is from 1964; the restaurant opened in 2014. The current copy invents sixty years of family history.
- No "elevated", "nestled", "culinary journey", "farm-to-table" as a slogan.
- Don't oversell the awards. List them once, on a press page, with attribution. The restaurant's own voice never brags; the bio says it once with an exclamation mark and moves on.

**Register examples**

| Instead of | Write |
|---|---|
| "A Detroit East Side Institution Since 1964" | "A diner on East Jefferson since 2014. Closed in 2023. Open again since September 2025." |
| "Experience our culinary journey" | "Polish American food, cooked with what Michigan farms have this week." |
| "Book your table today!" | "Reservations open 30 days out on Resy. Walk-ins welcome." |
| "Our chef-driven seasonal menu" | "The menu changes when the farms change. Last updated 20 September 2026." |

**How much Rose's Fine Food nostalgia to carry:** name the lineage, do not trade on it. The brand is **Roses**. Rose's Fine Food belongs in one paragraph on the story page and in the `alternateName` field of the structured data, where it does SEO work for people still searching the old name. It does not belong in the `<title>`, the `h1`, or the logo, all of which currently carry it.

## Photography direction

- Candlelight, warm, shot at service. Never styled in daylight on a white sweep.
- The mismatched vintage crockery is a brand asset; it should be visible in every plate shot.
- **The flowers go in every room shot.** Cut from the garden out back and named by the New York Times.
- The pressed-tin ceiling, the melted wax, the mirrors and the open counter are the four room details press keeps describing. Get all four.
- People in frame. The comment thread on the feed is about the staff, not the plates.
- The garden that seats 120 has never been photographed for public use, and it is the whole private-events pitch.

## Traceability

| Decision | Evidence |
|---|---|
| Sage `#B3CDB4` | Measured, printed menu ground, dominant of ~128k sampled pixels |
| Crimson `#9C1B22` | Measured, printed menu ink |
| Ember `#F97743` | Measured, `redbow.png`, 41.5k opaque pixels |
| Paper `#F0ECE6` | Measured, live site `body` background |
| Forest, sage-pale, crimson-deep, ink-mute | Derived by stated blend from measured anchors |
| Rejecting `#3D8B61` / `#E8682D` | Measured 3.52:1 and 2.77:1 on paper, both fail AA |
| Montserrat | Visual match to menu section heads and dish names. **Unconfirmed** |
| EB Garamond | Visual match to menu descriptions, incl. oldstyle figures. **Unconfirmed** |
| Rejecting Inconsolata | Measured as the live site's face; contradicts the printed menu |
| *Wycinanki* motif system | Observed, six distinct figures on the printed menu |
| Bow as mark | Measured, `redbow.png` used as logo and favicon |
| Pill button radius | Measured from the live site CTA |
| Voice rules | Derived from captured captions, quoted in the IG intel |
| No shadows | Design decision from the single-ink printed-matter conceit |
