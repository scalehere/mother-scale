---
title: "Ads Onboarding & Fulfillment Process"
type: source
tags: [ads, google-ads, meta-ads, lsa, fulfillment, sop, operations]
sources: [ads-onboarding-fulfillment-process]
updated: 2026-04-12
---

# Ads Onboarding & Fulfillment Process

Source: `raw/SCALE SD STRATEGY DOCUMENTS/Ads_Onboarding_Fulfillment_Process.docx`

End-to-end SOP for onboarding contractor clients onto paid advertising and delivering ongoing fulfillment. Platforms: Google Search Ads, Google Local Service Ads (LSA), Meta Ads (Facebook/Instagram), Google Performance Max. Context: home service contractors in San Diego — roofing, HVAC, plumbing, electrical, remodeling, landscaping.

---

## Master Timeline

| Phase | Timeframe | Deliverable |
|-------|-----------|-------------|
| Phase 1 | Days 1–3 | Contract signed → kickoff call scheduled → access requests sent |
| Phase 2 | Days 4–7 | Intake form completed → strategy brief approved → assets collected |
| Phase 3 | Days 8–14 | Accounts built → campaigns configured → tracking verified |
| Phase 4 | Days 15–21 | Internal QA → client review → campaigns go live |
| Phase 5 | Ongoing | Weekly optimization → monthly reporting → quarterly strategy review |

---

## Phase 1 — Kickoff (Days 1–3)

**Day 1 checklist (Account Manager):**
- Welcome email within 2 hours of signing
- Create client folder in ClickUp/Notion
- Send Onboarding Intake Form
- Request Google Ads MCC access, Meta Business Manager access, GBP access, website access
- Schedule 60-min kickoff call within 48 hours

**Kickoff call attendees:** Account Manager (leads), Ad Specialist (listens/notes), Client (owner or decision maker). Record with consent via Zoom.

**Critical kickoff questions:**
- Target zip codes (and which ones to exclude)
- Average job value by service type
- Lead volume goal ("how many leads would make this a home run?")
- Follow-up process when a lead calls (affects conversion rate)
- Dedicated phone number for call tracking
- After-hours call handling

---

## Phase 2 — Intake & Asset Collection (Days 4–7)

No campaign build begins without a completed intake form.

**Required information:**
- Legal business name, DBA, license number
- Service categories (ranked by priority and margin)
- Full service area (cities and zip codes)
- Ad account IDs (Google Ads Customer ID, Meta Business Manager ID)
- GA4 property, GTM access, website CMS
- High-res logo, 5–10 before/after job photos, team/owner photo
- Primary offer/promotion, key differentiators, reviews/testimonials
- Confirmed monthly ad spend budget (separate from management fee)
- Primary campaign goal and max acceptable cost-per-lead

---

## Phase 3 — Campaign Build (Days 8–14)

### Tracking Setup (Do First — Always)
Running ads without verified conversion tracking is described as a "cardinal sin."

**Checklist:**
- Google Tag Manager installed and verified
- GA4 property with data flowing
- Google Ads conversion actions: phone call from ads (30-sec min), phone call from website (CallRail/GTM), form submission, quote request
- All conversions verified in Google Tag Assistant
- CallRail tracking number set up
- Meta Pixel installed and verified via Meta Pixel Helper
- Meta custom conversions: lead form submit, call button click
- Google Ads ↔ GA4 linked (auto-tagging ON)
- Google Search Console ↔ GA4 linked

**Do not proceed to campaign build until all conversions show "Active."**

### Google Search Ads Structure

**Account structure:** Separate campaigns by service category (never mix HVAC + Plumbing).

Example for full-service HVAC:
- Campaign 1: AC Repair (highest priority)
- Campaign 2: AC Installation/Replacement
- Campaign 3: Heating/Furnace
- Campaign 4: Brand terms (low budget)

Each campaign → 2–4 tightly themed ad groups → 10–20 keywords → 3 RSAs minimum.

**Keyword strategy:**
- EXACT and PHRASE match only — no Broad match in first 60 days
- High-intent terms: "[service] near me," "[service] San Diego," "emergency [service]," "best [service] [city]"
- Comprehensive negative keyword list from day one
- Location qualifiers: San Diego, Chula Vista, El Cajon, La Mesa, Santee, Escondido, Oceanside, etc.
- Never mix branded and non-branded campaigns

**Ad copy requirements (every RSA must include):**
- Headline: primary keyword + city
- Headline: call to action
- Headline: trust signal (e.g., "Licensed & Insured Since 2008")
- Headline: urgency/offer (e.g., "Same-Day Service Available")
- Description 1: main benefit + primary keyword
- Description 2: overcome a key objection (price, speed, reliability)

**Required ad extensions:** Call asset (CallRail), Location asset (linked to GBP), Sitelinks (4 min: Free Estimate, Our Services, Reviews, About Us), Callout assets (6 min), Structured Snippets (services list), Image assets (client's actual job photos — no stock).

**Bidding progression:**
- Month 1: Manual CPC (maintain control while gathering data)
- Later: transition to smart bidding as conversion data accumulates

---

## Phase 4 — QA & Launch (Days 15–21)

Internal QA → client review call → campaigns go live.

---

## Phase 5 — Ongoing Fulfillment

- Weekly optimization
- Monthly performance reporting
- Quarterly strategy review

---

## Key Claims
- Tracking verification is non-negotiable before any campaign goes live
- Google Search is primary driver of high-intent leads for contractors
- Separate campaigns by service category — never mix
- No Broad match in first 60 days
- Client's actual job photos outperform stock in contractor ads
- ClickUp or Notion used for project management (in addition to GHL)

## Entities Mentioned
- [[Scale SD]] — the agency this SOP governs
- [[GoHighLevel]] — pipeline and CRM management
