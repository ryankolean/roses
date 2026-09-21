# Build Recommendation

**Version:** 1.0, 2026-09-20.

## Stack

**Static multi-page HTML, no build step, GitHub Pages**, matching Umbo and Meantime. One deviation from those two: **the menu is generated from a single Markdown file**, because the menu changes and the owner has to be able to change it.

### Why static

- The whole site is nine pages of mostly-fixed content and one list that changes monthly. There is nothing here that needs a server, a database or a framework.
- The current site loads fifteen JavaScript bundles, Datadog RUM, reCAPTCHA Enterprise, a consent platform and a fraud SDK to display a single picture. A static build ships none of that.
- GitHub Pages is free, and Summit already runs two restaurant sites on it.
- **It removes the Cloudflare managed challenge.** That challenge belongs to Toast, cannot be turned off by the restaurant, and currently returns 403 to every link-preview fetcher and AI crawler tested. Migrating is the only way out of it.

### The one moving part

```
content/menu.md   →  build step  →  /menu + the homepage menu block + Menu JSON-LD
```

`menu.md` holds a date and three sections of `name / description / price`. One small script renders it into the page and into the structured data, so the visible menu and the schema can never disagree.

This is the only reason a build step exists at all. Everything else is hand-written HTML.

### How a non-technical owner updates the menu

1. Open `content/menu.md` on github.com and click the pencil.
2. Edit the text. It looks like the printed menu.
3. Change `updated: 2026-09-20` at the top.
4. Click "Commit changes". Live in about a minute.

Expected frequency, inferred from the printed menu's filename convention (`Roses_menu_web_Aug_26.jpg`): **monthly**, plus ad-hoc single-dish edits.

**This must be agreed with the owner before the build starts.** If GitHub is a non-starter for Molly or Aaron, the fallback options in order of preference are: a hosted Markdown editor pointed at the repo, a Google Doc the build reads, or Summit making the edit on request. Do not ship a menu system nobody will use. See [`site-elements.md`](site-elements.md#menu-update-path-the-decision).

### Explicitly not chosen

| Option | Why not |
|---|---|
| Toast partner API menu sync | Toast online ordering is **currently disabled** and the ordering menu would not match the dining-room menu anyway. Revisit if ordering returns. **Never scrape the public ordering page** (Fly Trap precedent) |
| Staying on Toast Sites | Cannot fix the bot challenge, the boilerplate, the schema, or the monospace type. No CMS to inherit and nothing to export |
| Squarespace / Webflow | Monthly cost, and the peers on them (Freya, Barda, Coriander) are not producing better sites than a static build would |
| Astro / Next | A framework for nine static pages and one Markdown file |

## Domain, DNS and hosting position

**Capture the zone before touching anything.** Done, 2026-09-21T00:51Z, from `1.1.1.1`. Raw capture in [`../docs/dns-rosesdetroit.md`](../docs/dns-rosesdetroit.md).

| Record | Value |
|---|---|
| Authoritative NS | `ns1030.ui-dns.com`, `ns1055.ui-dns.biz`, `ns1106.ui-dns.de`, `ns1125.ui-dns.org` |
| SOA | `ns1030.ui-dns.com. hostmaster.1und1.com. 2017060112` |
| Apex A | `162.120.94.90` (Toast, Inc.) |
| `www` CNAME | `sites.toasttab.com` → `fallback.sites.toasttab.com.cdn.cloudflare.net` → `104.18.38.40`, `172.64.149.216` |
| **MX** | `aspmx.l.google.com` (1), `alt1`/`alt2` (5), `alt3`/`alt4` (10) — **Google Workspace** |
| TXT | `v=spf1 include:_spf.google.com ~all` · `google-site-verification=-G632jz8oLkiOWVwOjffz01JtBDW7EiDy5NFPbbskpY` |
| DMARC | **none** |
| DKIM | **none** at any common selector |
| CAA | none |
| AAAA | none |

**Reading:**

- **DNS is at IONOS (1&1)**, not at Toast and not at Cloudflare. The `hostmaster.1und1.com` SOA and a 2017 serial say the zone has been there since the first Rose's Fine Food site.
- **Toast is hosting only.** They own the A record target and they front it with their own Cloudflare account. The restaurant points DNS at them.
- **Mail is Google Workspace, and it is the thing that breaks.** Per the Umbo cutover: a registrar transfer destroys the DNS zone, and the zone is what carries the MX records. The mail subscription survives; the routing does not. **Do not transfer the registrar.** Change two records at IONOS and leave everything else alone.
- There are two separate Google verification tokens in play: one TXT at the apex, and a different one in the site's `<meta name="google-site-verification">`. The meta tag is almost certainly Toast's. **Establish who holds Search Console** before the cutover, or the restaurant loses visibility of its own search performance at the exact moment its URLs change.

### Cutover, minimal-risk version

1. Build and verify on `ryankolean.github.io/roses`.
2. Confirm who controls the IONOS account and who controls Search Console.
3. Re-capture the zone immediately before the change.
4. At IONOS, change **only** the apex `A` (to GitHub Pages' four addresses) and the `www` `CNAME` (to `ryankolean.github.io`). **Touch nothing else. Do not delete the MX or TXT records.**
5. Verify mail flow before and after by sending a test message in both directions.
6. Add DMARC and DKIM while in there. They are missing today, which is a live deliverability risk independent of this project.
7. Watch 301s from the eight legacy paths for a fortnight.

**Never** move the registrar as part of a website launch.

## Estimate and ticket breakdown

Sizes are for a single engineer, assuming the research package is accepted as-is and the owner-blocked items land on time.

| Ticket | Scope | Size |
|---|---|---|
| Repo scaffold, tokens, base CSS | Palette, type scale, spacing, buttons, forms from `brand-guidelines.md` | S |
| Vectorise the brand assets | Bow → SVG, six *wycinanki* motifs → SVG, favicon set, web manifest | M, **blocked on source art** |
| Menu pipeline | `content/menu.md`, renderer, `Menu` JSON-LD, date stamp | M |
| Home | Hero, menu block, hours, awards strip, story teaser | M, **blocked on photography** |
| Menu page | Full text menu, printable version | S |
| Visit page | Hours, map, transit, accessibility, reservation policy | S, **partly blocked on owner input** |
| Story page | Lineage, Molly's words | S, **blocked on permission** |
| Press page | Four awards, pull quotes, links | S |
| SEO and AI layer | Restaurant JSON-LD with awards, OG images, sitemap, robots, llms.txt, per-page meta | M |
| 301 map and cutover | Eight legacy paths, DNS change, mail verification | M |
| Private events, producers | Both optional | S each, **blocked on owner** |

**Roughly 3 to 4 days of build** once assets and permissions are in hand. The critical path is not code; it is **photography, the vector source art, and the owner's sign-off on the story copy**. Those should be requested now, not when the build starts. See [`assets-needed.md`](assets-needed.md).

### Suggested ticket shape

An epic with the above as children, and a hard dependency edge from "vectorise brand assets" and "photography" into every page ticket. Do not start page tickets against placeholder imagery; Meantime showed how much rework that causes.

## Risks

| Risk | Mitigation |
|---|---|
| No usable photography exists | Request from Jacob Lewkow and from the owner before the build. Design the pages to work with three good photos, not thirty |
| The menu-update path is never used | Agree it with the owner in writing first; pick the workflow they will actually do |
| Search Console is Toast's | Establish ownership before cutover; claim the property early |
| Mail breaks at cutover | Never move the registrar. Change two records. Test both directions |
| The story copy needs Molly's permission | Ask early. Without it the story page ships thinner, not false |
| Toast re-enables ordering mid-build | Scope it out of v1 explicitly; deep link if it returns |
