# DNS: rosesdetroit.com

**Captured:** 2026-09-21T00:51:03Z, resolver `1.1.1.1`.
**Raw:** [`dns-rosesdetroit-zone-capture.txt`](dns-rosesdetroit-zone-capture.txt)

This file exists because the Umbo cutover taught us that a domain transfer destroys the DNS zone, and the zone is what carries mail. Capture first, change later, and change as little as possible.

## Current state

```
; SOA
rosesdetroit.com.  86400  IN  SOA  ns1030.ui-dns.com. hostmaster.1und1.com. 2017060112 28800 7200 604800 600

; NS  — IONOS / 1&1
rosesdetroit.com.  86400  IN  NS   ns1030.ui-dns.com.
rosesdetroit.com.  86400  IN  NS   ns1055.ui-dns.biz.
rosesdetroit.com.  86400  IN  NS   ns1106.ui-dns.de.
rosesdetroit.com.  86400  IN  NS   ns1125.ui-dns.org.

; Web — Toast, fronted by Toast's Cloudflare
rosesdetroit.com.      3600  IN  A      162.120.94.90        ; OrgName: Toast, Inc.
www.rosesdetroit.com.  3600  IN  CNAME  sites.toasttab.com.  ; → fallback.sites.toasttab.com.cdn.cloudflare.net → 104.18.38.40, 172.64.149.216

; Mail — Google Workspace.  THE FRAGILE PART.
rosesdetroit.com.  3600  IN  MX  1   aspmx.l.google.com.
rosesdetroit.com.  3600  IN  MX  5   alt1.aspmx.l.google.com.
rosesdetroit.com.  3600  IN  MX  5   alt2.aspmx.l.google.com.
rosesdetroit.com.  3600  IN  MX  10  alt3.aspmx.l.google.com.
rosesdetroit.com.  3600  IN  MX  10  alt4.aspmx.l.google.com.

; TXT
rosesdetroit.com.  3600  IN  TXT  "v=spf1 include:_spf.google.com ~all"
rosesdetroit.com.  3600  IN  TXT  "google-site-verification=-G632jz8oLkiOWVwOjffz01JtBDW7EiDy5NFPbbskpY"

; Absent
;   AAAA     none
;   CAA      none
;   _dmarc   none          <- gap
;   DKIM     none at google._domainkey or any common selector   <- gap
;   no other subdomains found
```

## Notes

- **The zone predates the current restaurant.** SOA serial `2017060112` and a 1&1 hostmaster address: this zone has been at IONOS since the first Rose's Fine Food site.
- **Toast is hosting only.** The apex A record points at an IP registered to Toast, Inc., and Toast fronts it with their own Cloudflare account. That Cloudflare managed challenge is not the restaurant's and cannot be disabled by them. Leaving Toast Sites is the only way to remove it.
- **Mail is Google Workspace.** Five MX records and an SPF include. There is no DMARC record and no DKIM selector published, which is a deliverability gap worth fixing regardless of the website work.
- **Two different Google verification tokens exist**: this apex TXT, and a separate `<meta name="google-site-verification">` in the Toast-rendered HTML. Find out who holds each before the URLs change.

## Cutover rules

1. **Do not transfer the registrar.** The zone dies with the registration and takes the MX records with it. The Google Workspace subscription survives; the routing does not.
2. Re-capture the zone immediately before making any change.
3. Change exactly two things at IONOS: the apex `A` records (to GitHub Pages' four addresses) and the `www` `CNAME` (to `ryankolean.github.io`).
4. Do not delete or "tidy" the MX or TXT records. Do not let a control panel's "point this domain at a new site" wizard rewrite the zone.
5. Send a test message in and out before and after.
6. While in the zone, add DMARC and DKIM.
7. Purge resolver caches after the change rather than waiting out the TTL.
