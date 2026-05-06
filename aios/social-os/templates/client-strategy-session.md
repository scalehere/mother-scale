---
title: Client Strategy Session — Month 1 Intake Template
type: template
sources: [scale-business/wiki/sources/social-media-content-optimization.md]
updated: 2026-05-04
---

# Month-1 Strategy Session — {Client Name}

> 45-minute session before the first content shoot. Outputs go into `clients/{client-slug}/` as separate config files. This template is what the `client-strategy-session` skill walks the client through.

**Date:** {YYYY-MM-DD}
**Attendees:** {client name + role}, {Scale SD attendee}
**Recording:** Fathom link
**Client wiki entity:** [[../../scale-business/wiki/entities/{slug}]]

---

## 1. Brand voice & personality → `clients/{slug}/brand-voice.md`

- How would you describe how your company talks to customers? Friendly + technical? Formal? Bold?
- Who's the main human voice on social — owner? team? mix?
- Which adjectives describe your brand: trustworthy, fast, premium, approachable, expert, scrappy, family, modern, traditional?
- Any words/phrases you DO want associated with you? Any you DON'T?
- Past content that sounded right — examples (pull URLs)?
- Past content that sounded wrong — examples?

## 2. Content pillars (tailor the 5) → `clients/{slug}/content-pillars.md`

The 5-pillar framework (`The Work / The Team / Education / Social Proof / Local Presence`). For each, describe specifically what this client's version looks like:

- **The Work** — what kinds of jobs photograph well? Before/after possible? Process documentation possible?
- **The Team** — owner-led? Crew-led? Who's comfortable on camera?
- **Education** — what 3 things does this client wish their customers knew? (becomes monthly tip topics)
- **Social Proof** — best-performing reviews? Strong testimonials? Milestone moments coming?
- **Local Presence** — which SD neighborhoods are hot for this client? Community involvement?

## 3. Target audience → `clients/{slug}/audience.md`

- Primary homeowner profile: age range, income range, neighborhoods, life stage (young family, empty nester, etc.)
- Pain point that triggers them to call a contractor like this client?
- Where do they spend time online? FB? IG? Nextdoor? TikTok?
- What objections do they have before hiring? (price, trust, timeline)

## 4. Platform priority → `clients/{slug}/platform-config.md`

Default for contractors: **Facebook first.** Then Instagram, GBP, TikTok (if owner is comfortable on camera), Nextdoor (if community-engaged).

- Confirm primary platform
- Posting cadence per platform (default: 3-4/wk on primary, 2/wk on secondary)
- Posting times per platform (default: weekday 7-9am or 5-7pm local)
- Platform-specific notes (e.g., "FB owner page only, not personal," "IG bio link goes to GHL booking page")

## 5. Competitor & inspiration review → `clients/{slug}/competitors.md`

- 2-3 LOCAL competitor profiles (other contractors in the same trade in San Diego)
- 1-2 NATIONAL inspiration accounts (best-in-class for this trade, even if out of market)
- For each: what's working, what's missing, what would we do differently

## 6. Offer & CTA → `clients/{slug}/offers-and-ctas.md`

- Current primary offer (e.g., "Free in-home estimate")
- Phone number / booking link to drive to
- CTA library — 5-7 different ways to ask for the call/click that we'll rotate (avoid CTA fatigue)
- Promo cadence (max 1 promotional post per month per the SOP)

## 7. Shot wishlist → `clients/{slug}/shot-wishlist.md`

For the upcoming first shoot — what specifically do they want captured?

- Signature jobs they're proud of (recent or upcoming)
- Equipment / fleet that looks good on camera
- Team members worth featuring (with their consent)
- Recurring locations they have access to
- Any branded material (uniforms, trucks, vans, banners)

---

## Output checklist (skill writes these files at end of session)

- [ ] `clients/{slug}/brand-voice.md`
- [ ] `clients/{slug}/content-pillars.md`
- [ ] `clients/{slug}/audience.md`
- [ ] `clients/{slug}/platform-config.md`
- [ ] `clients/{slug}/competitors.md`
- [ ] `clients/{slug}/offers-and-ctas.md`
- [ ] `clients/{slug}/shot-wishlist.md`
- [ ] `clients/{slug}/hashtag-bank.md` (seeded from session, expanded by `monthly-content-plan` over time)
- [ ] Append decision entry to root `decisions/log.md` ("Onboarded {client} into social-os")
