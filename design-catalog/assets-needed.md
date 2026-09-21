# Assets and Answers Needed from Roses

**Version:** 1.0, 2026-09-20.

One consolidated list, so nothing gets discovered piecemeal mid-build. Items are ordered by what blocks the most work.

**Nobody has contacted the owner yet.** SUMMIT-179 excludes owner contact. This list is the handover.

## Blocking the build

### 1. Source artwork for the brand

The entire visual identity currently exists as a **2.1MB PNG of a bow** and a **flattened JPEG of a printed menu**. Neither is usable at build quality.

- `redbow.png` as **vector** (AI, EPS, SVG or PDF)
- The six *wycinanki* illustrations from the menu as vector: the rose rosette, the wheat sheaves, the peacock, the woman with the bread basket, the footed fruit bowl, the wavy rule
- The menu's **layered source file**, which would also settle the font question below
- **Who designed it?** They are the right person to ask for all of the above, and to draw anything new.

### 2. Fonts

Three faces are used on the printed menu and none can be identified from a JPEG.

| Where | What we need |
|---|---|
| The ornate "Menu" display face | Name and licence. Currently **unidentified** |
| The "Witamy!" script | Name and licence. Currently **unidentified** |
| Dish names and section heads | Confirm or correct our visual match, **Montserrat** |
| Dish descriptions | Confirm or correct our visual match, **EB Garamond** |

Without answers we ship the two Google Fonts matches and leave the ornate display face out of live text entirely. That is a real downgrade and it is avoidable with one reply.

### 3. Photography

**There is not one usable photograph of this restaurant available to us.** The current website has zero. The Instagram feed carries no photographer credit, so ownership is unknown.

Needed, at minimum:

- Three to five room shots: the pressed-tin ceiling, the melted-wax candles, the vintage mirrors, the open counter, flowers on the tables
- Six to ten plate shots on the real mismatched crockery
- One portrait of Molly, one of the crew
- **The garden.** It seats roughly 120 and has never been photographed for public use. It is the entire private-events pitch
- Anything from the **Jacob Lewkow** Hour Detroit shoot the restaurant can license

**Question:** who owns the Instagram photography, and can we use it on the site?

### 4. Permission for the story copy

The anniversary post of 2026-08-30 is the best writing that exists about this restaurant. *"This place is alive, my diner phoenix."*

**Ask:** may we use it, lightly edited, as the story page, under Molly's byline?

Without it we write something plainer and truthful. We will not publish the invented 1964 history that is on the site now.

## Content we cannot research

### 5. The drinks list

Not published on the website, the Linktree, or Instagram. Press mentions pickle martinis and a tomato horseradish martini. We need cocktails, beer and wine with prices, or a decision to leave drinks off the site.

### 6. Accessibility facts

Do not publish what we have not confirmed. Needed: step-free entrance or not, restroom accessibility, seating types, whether the garden is accessible. Until confirmed, the site carries an honest "message us and a person will answer" section, the same pattern used on Meantime.

### 7. Parking and transit

Street parking, a lot, or both. Anything guests should know about arriving on East Jefferson at night.

### 8. Private events

Is the 120-guest garden something to publicise? Are room buyouts offered? What is the enquiry address, and who answers it?

### 9. Producer credits

May we publish the supplier list? Lillian's Loaves, Amalgam Farms, Seedling Fruit, Sown In Peace Detroit, Order Up Organics, Ma Coen's, Marrow, The Flowering Hearth. Some restaurants guard their sourcing; this one credits it publicly on Instagram, but a website list is more permanent.

### 10. The living wage

The Free Press reported it. It is a genuine differentiator. Confirm before publishing, and confirm how they want it said.

## Decisions only the owner can make

### 11. The name

Five renderings are live across surfaces the restaurant owns. **Pick one.** Our recommendation is **Roses**, matching Instagram, the Free Press and the New York Times, with "Rose's Fine Food" kept in the structured data so old searches still land.

### 12. The bow

Is it the permanent mark or a placeholder? The filename says "red" and the artwork is orange. Would they like a proper wordmark pairing the bow with "Roses"?

### 13. The menu update path

Who edits the menu, and are they willing to use a GitHub page to do it? If not, we pick a different mechanism. **This decides the stack**, so it needs answering before the build, not after.

### 14. Mailing list

Is there one? Toast's email tool exists on the current site. If they are leaving Toast, they need a provider, or we drop the capture.

## Access and accounts

### 15. Google Search Console

There are **two** Google verification tokens: one TXT at the apex, and a different one in the Toast-rendered HTML. Who controls each? If Toast holds the property, the restaurant has never seen its own search data, and it will lose continuity at cutover.

### 16. Google Business Profile

Who manages it? It needs the category and hours checked against the current dinner-only operation.

### 17. IONOS

Who has the DNS login? Two records change at cutover and nothing else. **Do not transfer the registrar.**

### 18. The domain itself

Confirm `rosesdetroit.com` is registered to the restaurant and not to a former agency or to Toast.

## Things they should fix themselves, whatever happens here

Worth handing over even if the website project goes nowhere.

1. **`/contact` publishes the wrong hours** — "Tuesday-Sunday, 8am to 3pm. Closed Mondays" is the 2014-2023 brunch operation. The restaurant is dinner-only and closed Tuesday. It contradicts the hours widget on the same page.
2. **`/our-story` claims the business dates from 1964.** It opened in 2014.
3. **`/gallery` advertises breakfast and lunch menus** at a dinner-only restaurant.
4. **`/order` is broken** — "Menu items unavailable" — and is linked from the main nav as "Shop + Events".
5. **Yelp has two listings for the restaurant**, both named "Rose's Fine Food", both categorised **Breakfast & Brunch**.
6. **The site has no reservation link**, while Resy is the actual booking path.
7. **No DMARC and no DKIM** on the domain. A deliverability risk unrelated to the website.

Items 1 through 4 are wrong facts published under their own name during the year they won Restaurant of the Year. They are fixable inside Toast today, in about twenty minutes, without waiting for anything else.
