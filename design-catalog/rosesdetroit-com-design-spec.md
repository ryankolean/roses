# Design Spec: rosesdetroit.com

## Meta

- **URL:** https://rosesdetroit.com/
- **Extracted:** 2026-09-20
- **Viewports captured:** 1024px and 390px (computed styles + screenshots, measured). 768px and 1440px not separately captured; the layout is a single centered column with no breakpoint behaviour worth a third capture (see Responsive Behavior).
- **Site type:** Restaurant, single-location, Toast Sites template
- **One-line character:** An unedited Toast template wrapped around one JPEG. Bone + Toast-green + Toast-orange, Inconsolata throughout, and every word of prose is AI-generated boilerplate that contradicts the restaurant's actual hours, age and concept.

> **Access note.** The site sits behind Cloudflare's managed challenge. Plain HTTP clients get `HTTP 403` with `cf-mitigated: challenge`. A real browser clears the JS challenge automatically with no interaction, so the full audit below is **measured in a rendered Chromium session**, not inferred. Nothing was bypassed. See "Bot protection" for who owns that layer, because it is not the restaurant.

## Platform and hosting (measured)

| Fact | Value | How measured |
|---|---|---|
| Platform | **Toast Sites** | `<meta name="author" content="Toast, Inc.">`, React bundles on `d28f3w0x9i80nq.cloudfront.net/app/*`, `powered by toast` footer badge |
| Apex A record | `162.120.94.90` | `dig`; `whois` → `OrgName: Toast, Inc.` |
| `www` CNAME | `sites.toasttab.com` | `dig +short www.rosesdetroit.com CNAME` |
| Authoritative NS | `ns1030.ui-dns.com`, `ns1106.ui-dns.de`, `ns1125.ui-dns.org`, `ns1055.ui-dns.biz` | `dig NS` — IONOS/1&1 nameservers, so DNS is administered at IONOS, not at Toast and not at Cloudflare |
| Edge | Cloudflare | `server: cloudflare`, `cf-ray: …-ORD`, `cf-mitigated: challenge` |
| Image pipeline | imgproxy on CloudFront (`d1w7312wesee68.cloudfront.net`) over `s3://toast-sites-resources-prod` | measured from `srcset` |
| Third-party JS | Datadog RUM, Google reCAPTCHA Enterprise, Ethyca Fides (consent), Sift (fraud) | measured `<script src>` |
| Restaurant GUID | `7c61bca7-bb31-4dac-8a9d-613d0e8eda15` | asset paths |

**Consequence:** the entire site is a rendered surface of the Toast POS account. There is no CMS to inherit, no theme repo, no exportable content. A rebuild starts from zero and the only thing that has to survive is the domain.

## Page and IA inventory

Sitemap is declared in `robots.txt` but points **cross-domain** to `https://d28f3w0x9i80nq.cloudfront.net/sitemaps/rosesdetroit.com/sitemap.xml`. A sitemap on a different host than the URLs it lists is routinely ignored unless that host is verified in Search Console, which is a Toast-controlled CDN the restaurant cannot verify. `https://rosesdetroit.com/sitemap.xml` returns the site's 404 page.

Nine URLs, all `priority 1.0`, all `changefreq daily`, all sharing one `lastmod`:

| Path | Title | What is actually on it |
|---|---|---|
| `/` | Rose's Fine Food | One menu JPEG, the address/hours widget, phone, IG icon |
| `/menu` | Menu | **Nothing.** "Currently not accepting online orders" and the location name. No menu. |
| `/order` | Order Online | **Broken.** "Currently not accepting online orders" plus "Menu items unavailable — We're unable to load menu items right now." |
| `/our-story` | Our Story | Template boilerplate, factually wrong (see Content defects) |
| `/gallery` | Gallery | Template boilerplate. **No photographs of the restaurant.** |
| `/careers` | Join Our Team | Template boilerplate, four role links |
| `/contact` | Contact | Template boilerplate, **wrong hours** |
| `/gift-cards` | — | Toast gift-card handoff |
| `/email-marketing` | — | Toast email capture |

Nav exposes only two items: "Location and Hours" (`/#footer`) and "Shop + Events" (`/order`). Six of the nine sitemap pages are unreachable from the navigation. There is **no reservation link anywhere on the site**, although the restaurant takes reservations on Resy.

## Content defects (measured, and the core finding)

These are verbatim from the live pages on 2026-09-20.

1. **`/contact` publishes the dead restaurant's hours.** "Open Tuesday-Sunday, 8am to 3pm. Closed Mondays." Rose's is dinner-only, 4-10p Sun/Mon/Wed/Thu, 4-11p Fri/Sat, **closed Tuesday**. The page is wrong on the days *and* the times, and it contradicts the Toast hours widget in the footer on the same page, which correctly reads "Closes at 10PM."
2. **The site claims the business is 62 years old.** `/our-story`: "A Detroit East Side Institution Since 1964" and "From our humble beginnings in 1964, Rose's has been serving comfort food with a Polish twist to generations of Detroit families." Rose's Fine Food opened in **2014**, closed 2023, reopened 2025. 1964 is the age of the cinderblock building. The copy invents a multi-generation family history that does not exist.
3. **`/gallery` sells breakfast and lunch.** "View Breakfast Menu" and "Lunch Specialties" on a dinner-only restaurant.
4. **`/gallery` contains no gallery.** Card headings with no photographs behind them.
5. **Every prose page is unedited template filler.** "Join Our Family", "Community Heart", "Take a peek into where the magic happens." None of it is the restaurant's voice, and it reads as machine-written. For a Free Press Restaurant of the Year with a New York Times listing, this is the highest-cost defect on the site.
6. **`/order` is broken**, and has been left linked as "Shop + Events" in the primary nav.

## The menu

The only real content on the site is **one JPEG**: `Roses_menu_web_Aug_26.jpg`, served through imgproxy as WebP, native 1072x1920.

- `alt="Menu featuring Polish cuisine with various traditional dishes"` — generic, does not contain a single dish, price or the word Polish-American.
- Rendered at **902x695 CSS px** at 1024 wide, and **359x408 CSS px at 390 wide**. On a phone, the entire menu is a 359px-wide image of ~40 lines of type. It is unreadable without pinch-zoom.
- Zero text for search engines, screen readers, or AI answer engines. Google cannot index a single dish. There is no `Menu` schema.
- The filename is the update mechanism: `_Aug_26`. The menu is republished as a new image whenever it changes, and the page carries no visible date, so a guest cannot tell whether what they are reading is current.

Full text of the August 2026 menu, transcribed from the image, is in [`site-elements.md`](site-elements.md#menu-content-as-of-2026-09-20) so the rebuild has real content to work with.

## Color Palette

Measured from computed styles on the live site. These are the theme values the restaurant chose inside Toast, not Toast defaults, and they line up with the printed menu.

| Role | Value | Notes |
|---|---|---|
| Page background | `#F0ECE6` | `rgb(240,236,230)` warm bone — `body` background (measured) |
| Text / primary | `#3D8B61` | `rgb(61,139,97)` mid green — body colour and almost all text (measured); also exposed as `--ds-icon-on-bg-primary-subtle` |
| Heading / brand | `#E8682D` | `rgb(232,104,45)` orange — `h1` colour (measured); also `--ds-background-primary` |
| Accent hover | `#ED6B46` | `rgb(237,107,70)` (measured) |
| Dark surface | `#2B2E35` | `rgb(43,46,53)` cool near-black (measured) — the one off-brand value, a Toast default |
| Light on dark | `#F3EFEA` | `rgb(243,239,234)` (measured) |
| Consent-widget greys | `#F7FAFC`, `#4A5568`, `#2D3748` | Ethyca defaults, not brand (measured) |

**Palette character:** a genuine three-colour scheme — bone field, green type, orange brand — deliberately picked to echo the printed menu. It is the one part of the current site that is on-brand. But the green is doing a job it cannot do: `#3D8B61` on `#F0ECE6` is **3.52:1**, which fails WCAG AA for normal text. Nearly all body copy on the site is unreadable-by-standard.

### Measured from the brand's own artwork

The printed menu is the real brand surface and is a different, better palette than the website's.

| Role | Value | How measured |
|---|---|---|
| Menu ground (sage) | `#B3CDB4` | dominant colour, 76k of 128k sampled pixels |
| Menu ink (crimson) | `#9C1B22` | clustered red pixels; JPEG spreads it across `#9A1C22`-`#9C1B22` |
| Logo mark (ember) | `#F97743` | `redbow.png`, dominant opaque colour across 41.5k px |

These three are the anchors for the new system. See [`brand-guidelines.md`](brand-guidelines.md).

## Typography

- **Loaded:** Inconsolata 400/600/700 and Poppins 400/600/700, both from Google Fonts (measured `<link>`).
- **Applied:** **Inconsolata on essentially everything.** `--tsw-font-family: "Inconsolata"`, `--ds-header-3-font-family: "Inconsolata"`, `--ds-header-4-font-family: "Inconsolata"`. Element census: Inconsolata 31 text nodes, Inter 17 (Toast chrome), Poppins 2.
- **Scale (measured, 1024px):** `h1` 20px/700, line-height 30px · `h2` 20px/700, line-height 30px · body and links 16px/400, line-height 20-24px. That is the entire scale. There is no display size, no h3, and no distinction between the page title and a section heading.
- **Mobile:** `h1` stays 20px at 390px. No fluid scaling.
- **Character:** Inconsolata is a **monospace** face. Setting an entire restaurant site in monospace at a flat 20px/16px reads as a terminal, not as a Free Press Restaurant of the Year. It also fights the printed menu, which uses a geometric sans for dish names and a Renaissance oldstyle serif for descriptions. Poppins is loaded on every page and barely used, so the site pays the request cost for a font it does not render.

## Layout & Grid

- **Container:** single centred column. `scrollHeight` 1088px at 1024 wide, 964px at 390 wide. The homepage is one image and a footer.
- **Grid:** none. Toast template stack.
- **Header:** logo (`redbow.png`, rendered 104x50) centred, "More" disclosure left, cart badge and a pill "View Menu" button right.
- **Footer:** heading, phone, address link to Google Maps, live open/closed state with "All hours" disclosure, an Instagram icon, "powered by toast", and Toast's own ToS/Privacy/Cookie links. The restaurant's footer links to Toast's legal pages, not its own.
- **Whitespace:** generous around the single image, because there is nothing else to lay out.

## Components

- **Buttons:** one pill CTA ("View Menu", "Roses Shop"), orange fill. On mobile "Roses Shop" is a fixed full-width bar pinned to the bottom of the viewport, pointing at the broken `/order` page.
- **Cards:** the boilerplate pages use a repeated title + paragraph + link card. No imagery.
- **Forms:** none on the public pages except Toast's email-marketing route.
- **Imagery treatment:** five images total site-wide. One is the logo, one is the menu JPEG, three are icons. The Instagram icon is recoloured with a CSS `filter: brightness(0) saturate(100%) invert(45%) …` chain to fake the green — a hack, not a token.
- **Iconography:** Toast's stock SVG set.

## Animations & Interactions

| Element | Trigger | Behavior | Measured or Estimated |
|---|---|---|---|
| Hours disclosure | click "All hours" | expands the weekly hours list | measured |
| "More" nav | click | reveals Location and Hours / Shop + Events | measured |
| Consent modal | first load | Ethyca Fides overlay | measured |
| Scroll reveals | — | none observed | measured |

Nothing else animates. There is nothing to animate.

## Responsive Behavior

- **390px (measured):** `scrollWidth === clientWidth === 390`, **no horizontal overflow**. `h1` stays 20px. Menu image collapses to 359x408, which is the failure described above. A fixed bottom CTA bar covers the footer.
- **768px / 1440px:** not separately captured. The page is a single centred column with one image and a footer; there is no multi-column layout, no nav collapse worth verifying (the nav is a disclosure at every width), and no breakpoint-specific component. Marked **not verified** rather than asserted.
- **Zoom:** `maximum-scale=5, user-scalable=yes`, so pinch-zoom on the menu image is at least permitted.

## Accessibility baseline

| Check | Result |
|---|---|
| `lang` | `en` (pass) |
| Skip link | present, `#main` (pass) |
| Heading order | `h1` "Rose's Fine Food", `h2` "Rose's Fine Food Location and Hours". No `h3`. Only two headings on the homepage (thin but not invalid) |
| Menu accessibility | **fail.** The menu is an image; its alt text names no dish and no price. A blind guest cannot read the menu at all |
| Body-text contrast | **fail.** `#3D8B61` on `#F0ECE6` = 3.52:1, below the 4.5:1 AA threshold for normal text |
| `h1` contrast | `#E8682D` on `#F0ECE6` = 2.77:1 — **fail**, and it is 20px so it does not qualify for the large-text exemption |
| Logo alt | `alt=""` on `redbow.png` inside a linked home anchor; the anchor has no accessible name |
| Touch targets | pill CTAs are adequately sized (measured) |

## SEO baseline

| Check | Result |
|---|---|
| `<title>` | "Rose's Fine Food" — legacy name, no city, no cuisine, no award |
| `meta description` | "See our latest menu, find our hours, and order online directly from us. Locations in Detroit, MI" — Toast boilerplate, identical across the network, plural "Locations" for a single site |
| Canonical | `https://rosesdetroit.com/` (pass) |
| `og:title` | **declared twice**, `10551 E Jefferson Ave` and `Rose's Fine Food` |
| `og:image` | `redbow.png`, 2236x1073 — the bare logo on transparency, not a 1200x630 social card |
| `twitter:card` | absent |
| Structured data | one `Organization` + nested `Restaurant` with address, phone, `OrderAction`, `BuyAction`. **No** `openingHoursSpecification`, **no** `geo`, **no** `sameAs`, **no** `servesCuisine`, **no** `priceRange`, **no** `Menu`, **no** `aggregateRating` |
| `robots.txt` | present, permissive, disallows `/admin /account /checkout /cart /confirm` |
| Sitemap | cross-domain on a CDN the restaurant cannot verify |
| `llms.txt` | absent |
| Google verification | `tVS6EoujdYch1EiPgXc0eeTyxTeKCeg6HaACdoL-x1M` present — **someone has Search Console access.** Find out who; it is probably Toast, and if so the restaurant has no view of its own search data |
| Core Web Vitals | not measured. Field data needs CrUX or a Search Console the restaurant controls; lab numbers on a page that is one image would be misleading. Marked **not verified** |

## Bot protection

This is the finding to lead with when talking to the owner, because the first-pass assumption was wrong.

**The Cloudflare challenge is Toast's, not the restaurant's.** The apex A record resolves to an IP registered to Toast, Inc., and the edge is Cloudflare. The restaurant did not configure this, cannot see it, and **cannot turn it off**. It applies to every restaurant on Toast Sites.

What it does, measured by user agent from an unverified client:

| User agent | Result |
|---|---|
| Real Chromium (JS enabled) | **200** — challenge clears silently |
| `facebookexternalhit/1.1` | **403** |
| `Twitterbot/1.0` | **403** |
| `Slackbot-LinkExpanding` | **403** |
| `GPTBot/1.2` | **403** |
| `ChatGPT-User/1.0` | **403** |
| `Googlebot/2.1` (unverified IP) | **403** |
| `bingbot/2.0` (unverified IP) | **200** |

**Caveat, stated plainly:** Cloudflare verifies well-known crawlers by reverse DNS and source IP, so a spoofed `Googlebot` UA from a residential address being challenged is correct behaviour and does **not** prove real Googlebot is blocked. Genuine Googlebot is very likely allowed. What it does prove:

- Every **link-preview** fetcher tested is challenged. Facebook, X and Slack all preview by URL fetch from their own ranges, and they do not execute JS. The practical read is that a shared `rosesdetroit.com` link renders without a card.
- **AI crawlers are blocked**, and unlike the search engines, OpenAI's fetchers are not on Cloudflare's allow-by-default verified list here. For a restaurant whose customers increasingly ask an assistant "what's on the menu at Roses in Detroit," the site contributes nothing to the answer. The menu being a JPEG means it would contribute nothing even if the crawler got in.
- `bingbot` passing while the social fetchers fail shows the policy is a **managed allow-list**, not a blanket block, and the restaurant has no say in what is on it.

Moving off Toast Sites removes this entirely. It is a reason to migrate, not a task to negotiate.

## Characteristic Elements

1. **One JPEG is the product.** The whole site exists to display a single menu image, and that image is unreadable on a phone and invisible to every machine.
2. **The brand is better than the site.** `redbow.png`, the sage-and-crimson printed menu, and the folk-art illustrations are a real identity. The site shows the bow at 104x50 in a header and nothing else.
3. **The prose actively lies.** Wrong hours, wrong founding year, wrong meal period, an invented family history. Not a gap: incorrect published facts on a nationally-reviewed restaurant.
4. **The legacy name is everywhere on their own site.** `<title>`, `h1`, `og:site_name` all say "Rose's Fine Food." The restaurant trades as Roses.
5. **No reservations.** Resy is the actual booking path and the site never mentions it.
6. **Monospace everything.** Inconsolata at a flat 16/20px, with Poppins loaded and unused.
7. **The footer belongs to Toast.** Terms, Privacy and Cookie Settings all point at `pos.toasttab.com`.
8. **Nothing about the awards.** Free Press 2026 Restaurant of the Year, a New York Times 2026 list placement, Hour Detroit Best New Restaurants, a Detroit News three-star review. The site mentions none of them.
