# Site Element Inventory: Roses

**Version:** 1.0, 2026-09-20.

Every element the new site needs, tagged **must** / **nice** / **out**, with the content or asset it depends on. A build ticket should be writable straight from this list.

Priority legend: **must** ships in v1 · **nice** ships if the content exists · **out** explicitly deferred, recorded so it is not rediscovered later.

## Page set and IA

| Page | Path | Priority | Why |
|---|---|---|---|
| Home | `/` | **must** | Menu is the reason people come; put it above the fold |
| Menu | `/menu` | **must** | Deep-linkable, indexable, the SEO asset |
| Story | `/story` | **must** | Replaces `/our-story`, which currently publishes a false history |
| Visit | `/visit` | **must** | Hours, address, parking, accessibility, reservations. `/contact` currently publishes the wrong hours |
| Press | `/press` | **must** | Four major awards in twelve months, currently mentioned nowhere |
| Private events | `/events` | **nice** | Depends on the owner wanting the 120-seat garden publicised |
| Producers | `/producers` | **nice** | Depends on owner sign-off to name farm partners publicly |
| Careers | `/careers` | **nice** | Only if roles are live; a stale careers page is worse than none |
| Gift cards | — | **out** | Deep link to the existing Toast gift-card page; do not rebuild |
| Online ordering | — | **out** | Currently broken and disabled. Not a v1 concern |

Nav, five items: **Menu · Story · Visit · Press · Reservations**. Reservations is a button, not a link, and it goes to Resy.

## Home

| Element | Priority | Content dependency |
|---|---|---|
| Hero line: "Enchanting Polish restaurant using the best of Michigan produce on Detroit's East Side" | **must** | None. Owner's own words, from the Linktree |
| Hero image: the room, candlelit, flowers in frame | **must** | **Blocked.** No usable photography exists. See assets-needed |
| Primary CTA: **Reserve on Resy** | **must** | None. `resy.com/cities/detroit-mi/venues/roses` |
| Secondary CTA: View the menu | **must** | None |
| The menu, in full, on the homepage | **must** | Menu text (below, already transcribed) |
| "Last updated" date stamp next to the menu | **must** | A convention, not an asset |
| Hours block with "closed Tuesday" explicit | **must** | None, verified |
| Award strip: Free Press · New York Times · Detroit News · Hour Detroit | **must** | None, verified. Logos are **nice**, text is enough |
| One story paragraph linking to `/story` | **must** | Anniversary post, pending owner permission |
| Producer credits line | **nice** | Owner sign-off |
| Instagram feed embed | **out** | Adds a third-party script for content that is one click away. Link the account instead |

## Menu system

**The core requirement.** Everything else on this list is ordinary restaurant-website work; this is the part that decides the stack.

| Element | Priority | Notes |
|---|---|---|
| Menu as **real HTML text** | **must** | Not an image, not a PDF-only. The current JPEG is invisible to search, to screen readers and to AI answer engines, and is unreadable at 359px on a phone |
| Section structure: Snacks/Salads/Sides · Mains · Desserts | **must** | Matches the printed menu |
| Dish name, description, price, dietary tags inline | **must** | Exactly as printed. No dot leaders, no price column |
| Visible "as of" date | **must** | The honesty mechanism for a menu that changes |
| One line setting expectations | **must** | e.g. "The menu changes with what the farms have." |
| Printable / downloadable version | **nice** | Marrow offers a PDF alongside the text; low cost |
| Drinks: cocktails, beer, wine | **nice** | **Not captured.** No drinks menu is published anywhere. Press mentions pickle martinis and a tomato horseradish martini. Owner must supply |
| `Menu` JSON-LD | **must** | Derived from the same source data |

### Menu update path (the decision)

**Recommendation: a single Markdown file in the repo, edited through the GitHub web UI, which rebuilds the page on push.**

Why not the alternatives:

- **Toast partner API.** Evaluated and **rejected for v1.** The Toast menu is currently disabled (`/order` returns "Menu items unavailable") and the ordering menu would not match the dining-room menu even if it worked. It also requires partner credentials and a sync job for a restaurant that changes its menu a few times a month, not a few times a day. Revisit only if Toast online ordering is turned back on and the dining menu is mirrored there. **Never scrape `toasttab.com`** — partner API or nothing, per the Fly Trap precedent.
- **A hosted CMS.** Adds a monthly cost and a vendor for one file.
- **Hand-editing HTML.** Not something a non-technical owner will do, and the menu will go stale.

The concrete path, for whoever performs the update:

1. Open one file, `content/menu.md`, in the browser on GitHub.
2. Edit dish names, descriptions and prices as plain text. The format is the same shape as the printed menu.
3. Change the `updated:` date at the top.
4. Press "Commit changes". The site rebuilds and publishes in about a minute.

**Who:** Molly or Aaron, whoever prints the new menu. **How often:** the printed menu is versioned monthly (`Roses_menu_web_Aug_26.jpg`), so assume monthly, with ad-hoc edits when a dish drops. **Fallback:** if neither wants to touch GitHub, the same file can be edited in a hosted Markdown editor pointed at the repo, or Summit updates it on a text message. Decide this **with the owner**, and document the chosen path in the repo README.

### Menu content as of 2026-09-20

Transcribed from `Roses_menu_web_Aug_26.jpg`. This is the real content for the build, and the first proof that a text menu is possible.

**SNACKS, SALADS & SIDES**

| Dish | Description | Price |
|---|---|---|
| Bread Platter | Lillian's Loaves sourdough, caraway butter, Babcia's pickles, dill oil, pickled red onion | $24 |
| Polish Nachos | house-made potato chips, Ma Coen's smoked whitefish, cucumbers, caramelized onion, pickled red onion, trout roe and herbed creme fraiche (gf) | $22 |
| Pole Town Salad | Detroit grown greens, dill pickle dressing, parmesan, croutons | $16 |
| Pomidory i Ogórki | local tomatoes and cucumbers dressed with herbs (v) | $17 |
| Chłodnik | chilled beet soup, cucumber, creme fraiche, herbs and egg | $17 |
| Local Kiełbasa | caramelized onion, pickled red onion, whole grain mustard, dill, creme fraiche | $26 |
| Oysters | rotating selection, half dozen / dozen | $27/54 |

**MAINS**

| Dish | Description | Price |
|---|---|---|
| Roses Burger | sourdough, Marrow dry aged ground beef, bacon jam, mustard, pickled red onion and cabbage slaw | $23 |
| Makrela Świeża | whole fish, crispy skin, dill butter, pickled lemon, herbs (gf) | $52 |
| Pierogi Ruskie | classic pierogi filled with potato, creme fraiche, bacon jam | $36 |
| Kotlet | organic chicken, squash mizeria, Calabrian chili crème fraiche, pickle onions, dill | $42 |
| Kluski Dumpling | green herb sauce, braised local greens, toasted pumpkin seeds (v, gf) | $26 |
| Lamb Gołąbki | tomato pepper broth, dill oil, preserved lemon creme fraiche (gf) | $26 |
| Uszka | fresh cheese filled dumplings, lemon butter sauce, roasted beets, dill | $24 |

**DESSERTS**

| Dish | Description | Price |
|---|---|---|
| Seasonal Berries | (v, gf) | $13 |
| Naleśniki Layer Cake | with sour cream and seasonal berries | $22 |
| Chocolate Mousse | rose whip cream, tart cherries, poppy seeds (gf) | $16 |

Menu header artwork reads **"Menu"** with **"Witamy!"** alongside.

> **Correction to the ticket's price assumptions.** SUMMIT-179 cites press bands of "entrees $18-34". The measured August 2026 menu runs **$23-$52** for mains. The press figures are from early-2026 coverage and are stale. Use the measured menu.

> **Not captured:** drinks. No cocktail, beer or wine list is published on the site, the Linktree, or Instagram. This is a required owner input, not a research gap that more searching would close.

## Reservations

| Element | Priority | Notes |
|---|---|---|
| Resy deep link in the nav as a button | **must** | `resy.com/cities/detroit-mi/venues/roses` |
| Resy widget embed on `/visit` | **nice** | Adds a third-party script; deep link first, embed only if the owner wants it |
| Reservation policy text | **must** | Verified from Resy: bookable 30 days out, dining room and bar, 15-minute grace period, call 24h ahead for party-size changes |
| Walk-in policy | **must** | Verified: walk-ins welcome |
| Phone as an alternative | **must** | (313) 332-0404 |

## Visit

| Element | Priority | Content dependency |
|---|---|---|
| Address, 10551 E. Jefferson Ave, Detroit, MI 48214 | **must** | Verified |
| **Correct** hours: 4-10p Sun/Mon/Wed/Thu, 4-11p Fri/Sat, closed Tue | **must** | Verified. The live site's `/contact` is wrong |
| Map embed | **must** | OpenStreetMap, matching the Umbo/Meantime precedent. No Google Maps key needed |
| Parking and transit | **must** | **Unverified.** Owner input |
| Accessibility: entrance, restroom, seating | **must** | **Unverified.** Owner input. Do not publish specifics we have not confirmed; use the Meantime pattern of an honest "ask us" section until they do |
| Phone, tel: link | **must** | Verified |
| The garden | **nice** | Tied to private events |

## Story

| Element | Priority | Content dependency |
|---|---|---|
| The reopening story in Molly's voice | **must** | The 2026-08-30 anniversary post, **pending her permission** |
| Rose's Fine Food lineage: 2014-2023, correct | **must** | Verified |
| "My third business in this space" | **must** | Her words, pending permission |
| Molly and Aaron, named with roles | **must** | Verified |
| The living-wage commitment | **nice** | Reported by the Free Press; confirm with the owner before publishing |
| Portrait photography | **nice** | **Blocked.** No licensed imagery |

## Press

| Element | Priority | Notes |
|---|---|---|
| Free Press 2026 Restaurant of the Year, linked | **must** | Verified |
| New York Times 50 favourite places 2026, linked | **must** | Verified |
| Detroit News three stars, linked | **must** | Rating verified; **pull quotes not retrieved**, article is paywalled |
| Hour Detroit Best New Restaurants 2026, linked | **must** | Verified |
| Pull quotes with attribution | **must** | Collected in press-and-story.md |
| Outlet logos | **nice** | Licensing per outlet; text-only is safe and ships |

## Private events

| Element | Priority | Notes |
|---|---|---|
| The garden, ~120 guests | **nice** | Press-reported, needs owner confirmation |
| Buyout of the 28-29 seat room | **nice** | Owner input |
| Enquiry path | **nice** | Email or form. Owner must supply an address |

Currently there is no way to enquire about an event. Press describes a 120-guest garden. That is a revenue line the website does not serve at all.

## Producers

| Element | Priority | Notes |
|---|---|---|
| Named partners with links | **nice** | Lillian's Loaves, Amalgam Farms, Seedling Fruit, Sown In Peace Detroit, Order Up Organics, Ma Coen's, Marrow, The Flowering Hearth. **Owner sign-off required** before publishing a supplier list |

## Global

| Element | Priority | Notes |
|---|---|---|
| Header: bow mark, five-item nav, Reserve button | **must** | Bow must be **vectorised** first |
| Footer: address, hours, phone, social, legal | **must** | Must link **Roses'** legal pages, not Toast's |
| Social links: Instagram, Facebook, Threads | **must** | The current site links Instagram only |
| Mailing list capture | **nice** | Provider undecided. Toast's email tool exists; a plain provider is cleaner if leaving Toast Sites |
| Privacy policy | **must** | Currently points at `pos.toasttab.com/privacy` |
| Favicon, apple-touch-icon, web manifest | **must** | From the vectorised bow. Current favicon is a 2.1MB PNG |
| 404 page | **must** | In brand |
| Skip link | **must** | The current site has one; keep it |

## SEO and AI discovery

| Element | Priority | Notes |
|---|---|---|
| `Restaurant` JSON-LD, complete | **must** | Must include `openingHoursSpecification`, `geo`, `sameAs`, `servesCuisine: "Polish"`, `priceRange: "$$$"`, `acceptsReservations`, and **`alternateName: "Rose's Fine Food"`**. Current schema has none of these |
| `Menu` / `hasMenu` JSON-LD | **must** | Generated from the menu source |
| `award` property on the Restaurant node | **must** | Four awards, all verifiable |
| Unique title and description per page | **must** | Current description is Toast boilerplate, identical network-wide |
| OG image, 1200x630 | **must** | Current OG image is the bare logo at 2236x1073 |
| `twitter:card` | **must** | Absent today |
| Sitemap **on the site's own domain** | **must** | Current one is on a Toast CDN the restaurant cannot verify in Search Console |
| `robots.txt`, permissive | **must** | |
| `llms.txt` | **nice** | Absent today. Cheap, and this is a restaurant people ask assistants about |
| FAQ block | **nice** | Hours, parking, reservations, dietary |
| **Bot-protection posture: leave it behind** | **must** | Moving off Toast Sites removes the Cloudflare managed challenge that currently 403s every link-preview and AI crawler tested. This is a reason to migrate, not a setting to change |

### Name-change SEO

The restaurant's name is rendered **five different ways** across surfaces it owns or appears on:

| Surface | Name it carries |
|---|---|
| rosesdetroit.com `<title>`, `h1`, `og:site_name` | Rose's Fine Food |
| Instagram display name | Roses |
| Linktree | RosesDetroit |
| Resy | Rose's (slug `roses`) |
| Toast ordering | "Rose's 10551 E Jefferson Ave", slug `roses-fine-food-…` |
| Facebook | Rose's Fine Food (`/rosesfinefood`) |
| Yelp | ROSE'S FINE FOOD, **two separate listings**, categorised **Breakfast & Brunch** |
| Tripadvisor | ROSE'S FINE FOOD, neighbourhood "Marina District" |
| Press | "Roses" (Free Press, NYT), "Rose's" (Detroit News, Hour Detroit) |

| Action | Priority | Notes |
|---|---|---|
| Pick one canonical rendering and write it down | **must** | Recommendation: **Roses**, matching Instagram, the Free Press and the NYT |
| `alternateName: "Rose's Fine Food"` in schema | **must** | Keeps the legacy name working in search without putting it in the title |
| Keep every current URL working through the migration | **must** | `/menu`, `/order`, `/our-story`, `/gallery`, `/careers`, `/contact`, `/gift-cards`, `/email-marketing` → 301 to their new equivalents |
| Fix the Yelp duplicate and the Breakfast & Brunch category | **must-do, out of scope here** | Yelp lists a dinner-only restaurant under breakfast. Owner action; SUMMIT-179 explicitly excludes touching third-party listings |
| Reconcile Google Business Profile, Tripadvisor, Facebook, Toast | **out of scope here** | Same reason. Hand the owner the list |

## Analytics and performance

| Element | Priority | Notes |
|---|---|---|
| Privacy-respecting analytics | **nice** | Current site ships Datadog RUM, reCAPTCHA Enterprise, Ethyca and Sift, all Toast's. A rebuild should ship near-zero third-party JS |
| Performance budget | **must** | Under 150KB for the homepage excluding images; no framework. The current homepage loads 15 JS bundles to show one picture |
| Image budget | **must** | Responsive `srcset`, WebP/AVIF, lazy below the fold |

## Explicitly out of scope for v1

- Online ordering. Currently broken and disabled by the restaurant.
- Gift cards beyond a deep link to Toast.
- A Toast partner-API menu sync. Revisit only if online ordering returns.
- An Instagram feed embed.
- Multi-language. The Polish on the menu is flavour, not localisation.
- Anything that changes a third-party listing. Owner action, documented and handed over.
