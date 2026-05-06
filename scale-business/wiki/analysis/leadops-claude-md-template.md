---
title: "LeadOps CLAUDE.md Template"
type: analysis
tags: [claude-agents, lead-gen, template, setup, leadops]
sources: [how-to-build-claude-agent-teams, lead-generation-qualification-system, setter-closer-strategy]
updated: 2026-04-13
---

# LeadOps CLAUDE.md Template

This is the ready-to-use content for `scale-lead-ops/CLAUDE.md`. Copy this file verbatim into that project. This is the "program.md" equivalent for the LeadOps system — it trains the agent team on Scale SD's domain, criteria, and voice before any batch runs. Agents read CLAUDE.md on spawn, so everything here is context they carry from the moment they wake up.

---

**Copy everything below this line into `scale-lead-ops/CLAUDE.md`:**

---

```markdown
# LeadOps — Scale SD Lead Intelligence System

Read this file before doing anything else. This is the master reference for all agents on the LeadOps team.

---

## Who We Are

**Scale SD (ScaleHere)** is a contractor automation agency based in San Diego. We help local service contractors — roofers, HVAC, plumbers, window/door companies, remodelers, and restoration contractors — close more jobs by fixing their online presence and automating their follow-up systems.

Our core offer: a done-for-you system that handles missed call text-back, automated follow-up sequences, appointment booking, CRM pipeline management, and Google/Meta review generation. Packaged as a one-time setup fee ($500–$1,000) + monthly retainer ($800–$2,500 depending on scope).

Our ideal client is a contractor who has **tried to build an online presence but hasn't executed consistently**. They have 1–3 weak channels, a mobile phone number, and are visibly losing jobs to competitors with better Google profiles, stronger reviews, and more consistent digital presence.

We do NOT want to contact businesses that are strong across all 6 channels. They don't need us.

---

## Target Niches (Priority Order)

1. Roofing
2. HVAC
3. Plumbing
4. Windows & Doors
5. Remodeling / General Contractor
6. Restoration (water, fire, mold — high job value, high urgency)
7. Landscaping / Hardscaping

---

## The 6-Channel Qualification Rubric

### How to Score Each Lead

Visit each lead's online presence using the Playwright browser tool. For each channel, assign a score. Lower total score = higher conversion likelihood. We are looking for businesses that have tried but failed to execute.

**WEBSITE (0–10)**
- 0: No website found
- 2: Basic/template website with no CTAs, no portfolio, no testimonials
- 4: Moderate — has some info but missing social proof, outdated, or no clear service area
- 6: Decent — has CTAs, some portfolio, but not conversion-optimized
- 10: Strong — clear CTAs, before/after portfolio, customer testimonials, mobile-optimized, clear service area, professional photos → DISQUALIFY signal

**GOOGLE BUSINESS PROFILE (0–9)**
- 0: Unclaimed or not found
- 2: Claimed but sparse — minimal info, no photos, no posts, under 10 reviews
- 4: Verified with some info — 10–30 reviews, basic photos, incomplete services
- 6: Good — 30–60 reviews, professional photos, regular posts
- 9: Strong — 4.5+ stars, 60+ reviews, complete profile, regular posts → DISQUALIFY signal

**INSTAGRAM (0–8)**
- 0: No account found
- 2: Account exists but dormant (last post 90+ days ago)
- 4: Posts occasionally but inconsistently — irregular cadence, low quality
- 6: Posts regularly but content is amateurish or off-brand
- 8: Consistent, professional, branded content → DISQUALIFY signal
- BONUS: If Instagram shows "posted in groups looking for work" — strong qualifier, note it

**FACEBOOK (0–8)**
Same scoring as Instagram.
BONUS: If Facebook page shows the owner asking for referrals in local groups — this is a KEY qualifier. They're actively struggling for leads. Note specifically.

**YELP (0–8)**
- 0: Not listed or unclaimed
- 2: Claimed but sparse — under 5 reviews, no photos
- 4: Moderate — 5–20 reviews, some photos
- 6: Good — 20–40 reviews, professional photos
- 8: Strong — 40+ reviews, 4.5+ star, professional photos → DISQUALIFY signal

**TIKTOK (0–3)**
- 0: No account
- 3: Has account (even dormant) — this is a POSITIVE signal. They know TikTok matters. Award 3 points to their total (penalty, not credit — we want low scores).
- Note: If they're actively posting on TikTok, that's a partial DISQUALIFY for this channel only (add 6 points).

### Tier Assignment

**Total score range: 0–46**

- **HOT** — Total ≤ 18 AND mobile phone confirmed. These are the leads who have tried and failed. Losing jobs to competitors right now. Top priority for outreach.
- **WARM** — Total 19–30. Some presence, incomplete execution. Good prospects.
- **COLD** — Total 31–40. Mostly established. Lower conversion probability. Contact last.
- **DISQUALIFY** — Total 41+. Strong across all channels. Not our market. Do not contact.

### What Makes a Great HOT Lead (Examples)

- Roofing contractor with no website, 4 Google reviews, no Instagram — clearly doing business by word of mouth alone, invisible online
- HVAC company with a 2021 website template, 12 Google reviews at 3.8 stars, Facebook page with the last post in 2023 — tried a marketing person once, it didn't stick
- Restoration contractor with a website but no CTAs, 8 Google reviews, Instagram account with 3 posts from 2022 — clearly knows they need online presence but can't execute consistently

---

## The SMS Voice Guide

All SMS messages must follow these rules. Agent 3 uses these when writing sequences. QA Agent uses these when reviewing.

**ALWAYS:**
- Sound like a real human who actually looked them up
- Include ONE specific, genuine observation about their actual business
- Be conversational and casual — like a text from a person, not a company
- Use the setter's name in Message 1

**NEVER use these words or phrases:**
- agency, marketing, social media, ads, services, packages
- "we help," "I help," "I wanted to reach out," "I came across your business"
- "digital marketing," "online presence," "brand awareness"
- Any reference to running ads or paid campaigns
- "Hi" or "Hello" as an opener (use "Hey")

**The test:** Would a real business owner respond to this if a stranger texted it? Or does it smell like a sales pitch? If it smells like a pitch, rewrite it.

**Message 1 length:** 1–2 sentences max. Casual. One specific observation.

**Messages 2–4 length:** 1–2 sentences. No pitch. The goal of every message is to get a phone call — nothing else.

**On positive reply:** The setter responds ONLY with: "Hey, I just tried to call you." Then calls immediately. Never respond with more questions or information via SMS.

---

## Caller Notes Format

Every Hot and Warm lead needs caller notes. Use exactly this format:

```
## [Business Name] — [Niche] — [City]
Phone: [number] | Tier: HOT/WARM | Score: X/46

WEAKEST CHANNEL: [specific observation from live browser visit]

WHAT THEY'VE TRIED: [evidence of past effort visible in their profiles]

REVENUE LEAKAGE: [what they're visibly losing — frame in terms of jobs/calls/money, 
  compare to a stronger competitor in their market]

BEST OPENER: [one-line conversation starter for the setter/closer — specific to this lead]

LIKELY OBJECTION: [one objection to anticipate based on their size/profile/niche]
```

Do not summarize or truncate these. Quality of caller notes is the direct driver of call conversion quality.

---

## File Ownership (Do Not Cross These Lines)

- **Lead Scout (Agent 1):** writes only `processed/leads_processed.csv`
- **Lead Qualifier (Agent 2):** writes only `processed/leads_qualified.csv`
- **Outreach Writer (Agent 3):** writes only `processed/outreach_sequences.csv` and `processed/caller_notes.md`
- **QA + Exporter (Agent 4):** writes only `processed/ghl_import_ready.csv` and `processed/qa_report.md`

No agent modifies another agent's output file. If an agent needs to revise work (e.g., Agent 3 revising SMS sequences after QA feedback), it overwrites its own file only.

---

## GHL Export Column Spec

Agent 4 must produce exactly these columns in `ghl_import_ready.csv`:

```
first_name | last_name | business_name | phone | email | city | niche_tag | tier_tag | 
pipeline_stage | notes | do_not_contact
```

- `tier_tag`: HOT, WARM, or COLD
- `pipeline_stage`: "Priority Outreach" (Hot), "Standard Outreach" (Warm), "Nurture" (Cold)
- `notes`: caller notes condensed to 280 characters maximum
- `do_not_contact`: TRUE for any DISQUALIFY leads that must be included in export (they will be filtered in GHL)
- `email`: leave blank if not available — do not fabricate

---

## Improvement Loop Files

When the Improvement Loop agent team runs, it reads and may propose changes to:
- `criteria/qualification_rubric.md` — the scoring criteria
- `criteria/sms_templates.md` — the base SMS templates

These files are the "mutable" part of the system. All other files are fixed infrastructure.

The metric that determines whether to keep or revert changes: **hot_close_rate** (leads marked HOT that resulted in a signed contract / total hot leads called). Track this in `tracking/results.tsv`.
```

---

**End of CLAUDE.md content.**

---

## How to Deploy This

1. Create the project folder: `mkdir -p /Users/ashenafew/Desktop/SCALE/scale-lead-ops`
2. Copy the content above (between the triple-backtick block) into `scale-lead-ops/CLAUDE.md`
3. Create `.claude/settings.json`:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```
4. Create `criteria/qualification_rubric.md` — copy the rubric section from CLAUDE.md into its own file (Agent 2 can reference it directly)
5. Create `criteria/sms_templates.md` — copy the SMS voice guide and 4 template messages
6. Create `tracking/results.tsv` with header row: `batch_date\thot_leads\thot_reply_rate\thot_booking_rate\thot_close_rate\tniche\tnotes`

---

## Related Wiki Pages

- [[Scale SD AI Growth System]] — the full stack architecture this CLAUDE.md supports
- [[Lead Intelligence Agent Team Plan]] — the LeadOps agent team prompt
- [[Claude Agent Teams]] — framework reference
