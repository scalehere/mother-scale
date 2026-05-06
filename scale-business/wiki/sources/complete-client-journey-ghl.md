---
title: "Complete Client Journey — GoHighLevel"
type: source
tags: [operations, ghl, fulfillment, onboarding, pipeline, sop]
sources: [complete-client-journey-gohighlevel]
updated: 2026-04-12
---

# Complete Client Journey — From First Contact to Ongoing Fulfillment

Source: `raw/SCALE SD STRATEGY DOCUMENTS/Complete_Client_Journey_GoHighLevel.docx`

Master operations guide for the entire client lifecycle. GHL is the single source of truth for all pipeline activity. Services covered: Google Ads, Meta Ads, Local Service Ads (LSA), Social Media & Content, CRM/pipeline management.

---

## Pipeline at a Glance

| Phase | Timeframe | What Happens |
|-------|-----------|--------------|
| Lead In | Day 0 | Lead enters GHL from any source. Auto sequences fire. |
| Sales Call | Day 1–3 | Discovery call booked via GHL calendar. |
| Proposal | Day 3–5 | Proposal sent via GHL. Auto follow-up until opened/signed. |
| Contract | Day 5–7 | Contract signed via GHL DocuSign. Payment collected. |
| Onboarding | Day 7–10 | Welcome email + intake form. Kickoff call. GHL sub-account created. |
| Build | Day 10–18 | Campaign build, tracking setup, content planning, automations configured. |
| Launch | Day 18–22 | Internal QA. Client review call. All campaigns go live. |
| Fulfillment | Day 22+ | Weekly optimization, monthly content shoot, monthly reporting. |

---

## Phase 1 — Lead Capture (Day 0)

**Rule:** Every lead enters GHL immediately. No leads in spreadsheets, sticky notes, or personal phones. GHL is the single source of truth.

**Inbound sources:** Google Ads, Meta Ads, website contact form, organic Google/GBP, client referrals, partner referrals, Instagram/Facebook DMs, Thumbtack/Bark/Angi.

**Outbound sources:** Cold calls, LinkedIn, door-to-door/job sites, networking (NARI, BNI, Chamber), cold email via GHL, dead lead re-engagement, direct mail, trade shows.

**GHL automation on new lead (fires immediately, no manual action needed):**
1. Tag: 'New Lead'
2. Immediate SMS to lead: personalized intro + ask for best time to connect
3. 5-min delay: automated email with calendar booking link
4. Create Opportunity in pipeline → Stage: 'New Lead' → assign to Sales Rep (round-robin)
5. Immediate Sales Rep notification (SMS + GHL app): "New lead: [Name] — [Business] — follow up within 5 min"
6. 1-hour follow-up SMS if no lead response

**Speed-to-contact rule (non-negotiable):** First personal contact within 15 minutes during business hours. After hours: GHL automation handles first touch, Sales Rep follows up first thing next morning.

---

## Phase 2A — Discovery Call (Days 1–3)

30–45 min. Not a pitch — a diagnosis.

**Framework:**
- **Open (5 min):** Build rapport. Ask about their business.
- **Diagnose (15 min):** Where does work come from? What happens during slow months? Have they tried marketing? What's an average job worth? What does success look like in 12 months?
- **Present (10 min):** Prescribe specific services based on their pain — not a menu.
- **Handle Objections (5 min):** Acknowledge and redirect. Never argue.
- **Close/Next Step (5 min):** Either close on the call or set a specific next step with date and time. Never end without a next step.

---

## Phase 2B — Proposal (Days 3–5)

Proposals go out within 24 hours of the discovery call. Proposals sitting more than 48 hours see dramatically lower close rates.

Sent via GHL (not PDF email) so opens are tracked. GHL automation triggers open notification to Sales Rep — act on it immediately.

**Proposal must include:**
1. Cover page with client name
2. The Problem: restate what they told you — prove you listened
3. Our Solution: specific services and why each fits their situation
4. Deliverables: exactly what they get
5. Timeline: key milestones
6. Investment: management fee + ad spend as separate line items
7. Social Proof: 1–2 local contractor case studies
8. Next Steps: clear CTA — "Sign below and we'll schedule your kickoff call"
9. FAQ: proactively address top 3 objections (cost, results timeline, contract length)

**Follow-up sequence:** 24-hr SMS if not opened → 48-hr auto nudge email if opened but unsigned → 72-hr direct call from Sales Rep.

---

## Phase 2C — Contract & Payment (Days 5–7)

No work begins until both contract is signed and payment is collected.

- Contract sent via GHL DocuSign integration
- Payment collected via GHL Payments (Stripe)
- First month: management fee + first month ad budget
- Recurring payments set up in GHL/Stripe for subsequent months
- Opportunity moved to 'Won'

---

## Phase 3 — Onboarding (Days 7–10)

- Welcome email within 2 hours of contract signing
- Intake form sent (business info, ad account access, creative assets, messaging, budget)
- Kickoff call scheduled within 48 hours — 60 min block
- GHL sub-account created for client
- Access requests: Google Ads MCC, Meta Business Manager, GBP, website

**Kickoff call covers:** Business overview, current marketing history, goals/KPIs for 90 days, competitive landscape, target customer profile, offer & differentiators, billing/reporting logistics.

**Critical kickoff questions:**
- "What zip codes do you want to target, and which ones are you NOT willing to drive to?"
- "What is your average job value?"
- "How many leads per month would make this a home run?"
- "What does your follow-up process look like when a lead calls?"
- "What time do you or your team answer calls?"

---

## Phase 4 — Build (Days 10–18)

Tracking must be verified before any campaign goes live.

**Tracking checklist:** Google Tag Manager, GA4, Google Ads conversion actions (call from ads, call from website, form submit, quote request), CallRail, Meta Pixel, Meta custom conversions, GA4 ↔ Google Ads link, Search Console ↔ GA4 link. **Do not proceed until all conversions show "Active."**

---

## Phase 5 — Launch (Days 18–22)

Internal QA → client review call → all campaigns go live → GHL lead notifications active.

---

## Phase 6 — Ongoing Fulfillment (Day 22+)

- Weekly campaign optimization
- Monthly in-person content shoot
- Monthly performance report
- Monthly reporting call
- GHL pipeline updates

---

## Key Claims
- GHL is the single source of truth — no parallel tracking in spreadsheets or personal phones
- Speed-to-contact within 15 minutes is a non-negotiable standard
- Proposals older than 48 hours close at dramatically lower rates
- Tracking verification before launch is described as a "cardinal sin" to skip
- Full client journey from lead to launch: 22 days

## Entities Mentioned
- [[Scale SD]] — the agency this SOP governs
- [[GoHighLevel]] — the platform running the entire pipeline
