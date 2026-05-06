# Client Onboarding Checklist

Gather everything below BEFORE starting Agent 1. Missing items are blockers downstream — Agents 4, 7, and 10 all depend on this context.

Total gathering time: ~20 minutes (mostly client communication).

---

## Required from the client

### 1. Website URL
- The public marketing site (not a portal, not a Linktree)
- Note any subdomains or alternate sites if relevant

### 2. Brand assets (file uploads)
- [ ] Logo PNG with transparent background — high-res, ideally vector-derived
- [ ] Founder/owner photo — high-res, recent, ideally a portrait shot they're comfortable using
- [ ] Brand color hex codes (if they have a brand book) — otherwise we extract from logo
- [ ] Brand fonts (if they have brand standards) — otherwise we use category defaults

Save to: `/CLIENTS/[ClientName]/00_intake/brand_assets/`

### 3. Real install / project photos
- [ ] At least 10 finished install photos (high-res, well-lit)
- [ ] At least 3 in-progress / action photos (workers visible, branded shirts, real job site)
- [ ] At least 3 before/after pairs (same angle, same framing)
- [ ] Founder-with-customer photos if available
- [ ] Showroom or office photos if they have a physical location

Save to: `/CLIENTS/[ClientName]/03_assets/photos/`

**If photo inventory is thin:** stop here. Schedule a one-day photo shoot before running Agent 1.

### 4. Customer review platform URLs
- [ ] Google Business Profile URL
- [ ] Yelp page URL
- [ ] Houzz profile URL (if active)
- [ ] BBB profile URL (if active)
- [ ] Angi / HomeAdvisor URL (if active)
- [ ] Facebook page URL
- [ ] Any other review platforms relevant to category

### 5. Active offers and promotions
For each current offer:
- [ ] Offer headline
- [ ] Eligible products/services
- [ ] Quantity threshold (e.g., minimum 10 units)
- [ ] Geographic restrictions
- [ ] Stacking rules (combinable with financing? with other offers?)
- [ ] Expiration date
- [ ] Required disclaimers (legal, regulatory)

If terms are unverified, mark "TERMS UNVERIFIED — pending client confirmation."

---

## Required from the client (operational context)

### 6. Capacity & operational limits
- [ ] How many measure/quote appointments can the owner sustainably do per day?
- [ ] How many crew teams can the client field simultaneously?
- [ ] Service area radius (in miles or by ZIP list)
- [ ] Any seasons/times when capacity is constrained

### 7. Legal / regulatory exposure
- [ ] License number(s) and licensing body
- [ ] Active lawsuits or pending claims
- [ ] Trademark sensitivities
- [ ] Restricted advertising claims (e.g., "Best in town" requires verification in some states)

### 8. Customer-quote consent status
This is critical for Family 1 (social proof) ads.
- [ ] Has the client obtained written consent from any customers for use of their reviews in paid advertising?
- [ ] If yes, list which customers
- [ ] If no, we have to obtain consent before any Family 1 ad with named customer goes live

### 9. Marketing budget context
- [ ] Total monthly Meta ads budget
- [ ] Is this incremental or replacing existing spend?
- [ ] Existing CRM / lead-routing setup
- [ ] Speed-to-lead capability (5-min response = 100x conversion lift)

---

## Optional but high-value

### 10. Past campaign data
- [ ] Any prior Meta campaign results (CTR, CPL, CAC if known)
- [ ] What worked / what didn't from past efforts
- [ ] Existing audiences (lookalike sources, retargeting pixels installed)

### 11. Competitive intelligence the client has
- [ ] Competitors they specifically want to attack
- [ ] Local market context they have that won't show up in research
- [ ] Industry quirks (permit requirements, regional preferences, etc.)

---

## Pipeline kickoff readiness check

You're ready to run Agent 1 when:

- [✓] Client website URL is documented
- [✓] Brand assets folder has at minimum: logo + founder photo
- [✓] Photo inventory has at minimum 10 install photos
- [✓] Review platform URLs are listed
- [✓] At least 1 offer has fully locked terms (or you've confirmed proof-only campaign)
- [✓] Capacity numbers are documented
- [✓] Consent status is documented
- [✓] Service area is defined

If any of the ✓ items are missing, surface to client and resolve BEFORE Agent 1.

---

## Setup the client folder

```
1. Copy /SHARED/06_client-template/ to /CLIENTS/[ClientName]/
2. Drop brand assets into 00_intake/brand_assets/
3. Drop install photos into 03_assets/photos/
4. Save this onboarding checklist (filled in) to 00_intake/onboarding_checklist.md
5. Open Cowork Orchestrator chat (see Agent 0)
6. Ask: "Where do I start?" — orchestrator will point to Agent 1
```

You're now in the pipeline.
