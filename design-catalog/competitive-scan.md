# Competitive Scan: Detroit chef-driven seasonal restaurants

**Scanned:** 2026-09-20. Platform, reservation vendor and menu-delivery method measured by fetching each site and inspecting the markup.

The question this scan exists to answer: **how do Roses' actual peers publish a menu that changes constantly?** Because that is the one hard problem in the rebuild.

## The field

| Restaurant | Platform (measured) | Reservations | Menu delivery |
|---|---|---|---|
| **Marrow** | Custom build, no vendor fingerprint | Own "Book a table" | **Full HTML text**, ~28k chars, tabbed by service, season-stamped, with PDFs as a secondary download |
| **Barda** | Webflow | OpenTable | Menu **images** (6 image refs on `/menu`) |
| **Freya** | Squarespace | OpenTable | Not on `/menu`; menu lives elsewhere in the site |
| **Selden Standard** | WordPress | OpenTable | `/menus` is a thin hub; menus load separately |
| **Coriander Kitchen & Farm** | Squarespace | Tock + OpenTable | Not on `/menu` |
| **Takoi** | Squarespace, Toast for ordering | Tock + OpenTable | — |
| **SheWolf** | WordPress, Toast for ordering | Tock | — |
| **Ladder 4** | Custom | Tock + OpenTable | — |
| **Leña** | Wix, Toast for ordering | OpenTable | — |
| **Roses (today)** | **Toast Sites** | **None on site** (Resy, unlinked) | **One JPEG** |

## What the field tells us

**1. Nobody in this tier is on Toast Sites.** Toast is ubiquitous for the POS and for online ordering, and four of the nine peers embed Toast for ordering. Not one uses Toast to run the website. Roses is the outlier, and it is the outlier in the wrong direction: the restaurant with the best reviews in the group has the weakest site.

**2. Reservations are always first-class.** Every peer with a dining room surfaces a booking vendor on the homepage. OpenTable dominates, Tock is the chef-driven preference. Roses uses **Resy** and does not link it from its own site at all. This is the single cheapest fix available and probably the most valuable.

**3. Menu-as-image is common, and it is still wrong.** Barda does it too. That does not make it defensible, it makes it the default failure of restaurants on visual-first page builders. The comparison that matters is Marrow.

**4. Marrow is the model, and it is the most relevant peer for a specific reason:** Marrow supplies the dry-aged beef in the Roses Burger. They are a butcher's brasserie with a menu driven by what partner farms bring in, which is exactly Roses' constraint, and they solved it with:

- **Real HTML text**, not images and not PDF-only
- **Season-stamped** at the top of the menu ("Spring & Summer 2026") so a reader knows how current it is
- **Tabbed by service** (Dinner, Lunch, Brunch, Butcher's Block, Kids) rather than one long scroll
- **PDFs offered as a download**, secondary to the text, for people who want to print
- One sentence setting expectations: "Seasonal, regional cooking built from what our partner farms provide"

That is the pattern to copy, minus the tabs, because Roses runs one service.

**5. The honesty problem has a standard solution.** Peers who change constantly do not pretend the page is live. They date it and they say so in a sentence. "Menu as of 20 September 2026, and it changes with what the farms bring" is more trustworthy than an undated menu that might be six weeks stale, and it costs nothing to maintain.

## Where a rebuild puts Roses

On the measured evidence, a static text menu with a visible date and a Resy link would put Roses **ahead of every restaurant in this scan except Marrow** on the two things that matter for discovery: indexable menu content and a reservation path a search engine can follow.

Two further advantages no peer currently holds:

- **The awards.** Free Press Restaurant of the Year, a New York Times top-50 placement, a Detroit News three-star and Hour Detroit Best New. No peer in this scan has that run in a single year, and none of them would leave it off the homepage.
- **The illustration system.** The *wycinanki* folk-art world on the printed menu is a genuine visual asset. Squarespace and Webflow peers are all working from stock templates and photography. Roses can look like nothing else in the city for the cost of vectorising art it already owns.

## Out-of-market reference

Not scanned in depth, noted as direction: the restaurants that handle a daily-changing menu best are ones that treat the menu as the homepage rather than a subpage, and commit to a date stamp. That pattern suits Roses better than a conventional hero-image homepage, because the menu *is* the reason people visit the site, and it is currently the only thing on it.

## Sources

Platform and reservation data measured directly from each site on 2026-09-20 by fetching the homepage and, where it exists, the menu page, then inspecting markup for vendor fingerprints (`squarespace`, `wix`, `wordpress`, `webflow`, `toasttab`, `_next`) and booking links (`resy.com`, `opentable`, `exploretock`, `sevenrooms`). Sites returning 404 on a guessed menu path are marked "—" rather than assumed.
