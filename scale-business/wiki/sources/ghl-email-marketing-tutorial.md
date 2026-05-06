---
title: "The Ultimate GoHighLevel Email Marketing Tutorial"
type: source
tags: [ghl, email, automation, deliverability, campaigns, workflows]
sources: [The Ultimate GoHighLevel Email Marketing Tutorial]
updated: 2026-04-16
---

# The Ultimate GoHighLevel Email Marketing Tutorial

Full walkthrough of GHL email marketing by GHL Wizard. Covers setup, deliverability, the email builder, strategy (3 sequence types), automations, and analytics.

---

## Key Claims

- **Lead Connector is the preferred sending system** over Mailgun (cheaper, white-labeled, built into GHL)
- **Dedicated domain is mandatory** — without it, you send from GHL's shared `msgsndr.com` domain with terrible reputation
- **Simple text-based emails outperform image-heavy ones** for deliverability — especially on a new domain
- **Warm up your domain** — follow GHL's staged warmup guide (Stage 1: 100/hr → build up over weeks)
- **Unsubscribe link is legally required** — turn on in Business Profile so it auto-appends to every email
- **Email verification** (0.025¢/email) reduces bounces — enable in Business Profile settings
- **Hard bounce marking** should be turned on — prevents repeatedly hitting bad emails that hurt domain score

---

## Three Email Sequence Types

### 1. Welcome Sequence
- Triggered when someone opts into a form/list
- Goal: introduce brand, deliver lead magnet, build trust
- Structure: thank you + freebie delivery → value emails → final CTA
- **Not for cold email** — for warm opt-ins

### 2. Sales Follow-Up Sequence
- Triggered when a lead enters the pipeline or fills out a form
- Goal: convert interested leads into paying clients
- This is the primary revenue-generating email sequence
- Runs automatically once set up — works for every new lead without manual intervention

### 3. Newsletter Sequence
- Ongoing, value-based emails to keep subscribers engaged
- Free checklists, tips, audits, resources
- Keeps people on the list and builds long-term trust
- Created fresh each week (unlike welcome/sales which recycle)

---

## GHL Email Builder — How It Works

- **Marketing → Emails → Templates** — create reusable templates first
- **Marketing → Emails → Campaigns** — campaigns are built from templates
- Template types: Design Editor (drag/drop), Code Editor, Plain Editor, Import from other tools
- **Recommended approach:** Plain text template → paste AI-generated copy → add custom value fields (e.g., `{{contact.first_name}}`)
- **Naming convention:** E1, E2, E3... for easy reference in automations
- **Clone templates** to speed up building sequences — just swap subject line and body

---

## GHL Automation Setup (Email Sequences)

Location: **Automations → Create Workflow → Start from Scratch**

Basic structure for a 3-email welcome sequence:
```
Trigger: Form Submitted
→ Wait: 5 minutes
→ Action: Send Email (template E1)
→ Wait: 2 days
→ Action: Send Email (template E2)
→ Wait: 2 days
→ Action: Send Email (template E3)
→ Publish
```

- Templates pre-fill all email settings in automations — no manual configuration per send
- Build templates once → reuse across all sub-accounts and clients forever
- Use "Copy all actions" to quickly duplicate steps in the workflow builder

---

## Campaign Settings (Important)

- **Settings → Verified Sender Emails** — verify `media@scalehere.com` or sending email to improve deliverability
- **Settings → Sender Preferences** — set default From Name and From Email for all campaigns
- **Settings → Tracking** — enable Click Performance Tracking + UTM parameters for campaign attribution
- **Settings → Statistics** — view campaign-level performance data

---

## Email Deliverability — The No-Nos

| ❌ Don't | ✅ Do |
|----------|-------|
| Skip domain warmup | Follow GHL's staged warmup guide |
| Use spammy words (FREE, ACT NOW, $$$) | Write natural, value-first copy |
| Leave out unsubscribe link | Always include — auto-enable in Business Profile |
| Ignore bounce emails | Enable hard bounce marking in Business Profile |
| Send image-only emails | Text-based first; images only after warmup |
| Send inconsistently | Send daily/regularly on a schedule |

---

## Analytics — Where to Look

1. **Marketing → Statistics** — campaign-level: delivered, bounces, unsubscribes, spam complaints, open rate
2. **Settings → Email Services → Email Analytics** — sub-account overview: all metrics in one view
3. **Google Postmaster Tools** (advanced) — domain-level reputation data direct from Google; connect once domain is established

**Key metrics to watch:**
- High delivered rate + high open rate = healthy list
- High bounces + spam complaints = list quality problem

---

## AI Email Generation — Prompt Framework

Use AI (Claude, ChatGPT, etc.) with structured prompts, not generic requests. Fill in bracketed fields:

```
Create [N] email [sequence type] for my business [Business Name].
My product/service is [description].
Tone: [professional/conversational].
Over a timeframe of [X days].
Start with [thank you email / first email goal].
Include emails sharing [value topics].
End with a call to action to [desired action].
```

Output should be short, text-only, one CTA per email. Edit for authenticity before loading into GHL.

---

## Entities Mentioned

- [[GoHighLevel]] — the platform this entire system runs on
- [[GHL Wizard]] — source author (YouTube channel)

## Related Concepts

- [[Contractor Automation System]] — GHL automation framework Scale SD uses
- [[Client Pipeline (Lead to Fulfillment)]] — the pipeline email sequences support
