---
title: "Scale SD Lead Pipeline — Example Agent Prompt"
type: analysis
tags: [ai, agent-teams, claude, prompt, leads, template]
sources: [claude-agent-teams-guide, lead-generation-qualification-system, lead-warming-system, setter-closer-strategy]
updated: 2026-04-12
---

Ready-to-use Claude Code agent team prompt for Scale SD's lead intelligence pipeline. Copy this into Claude Code. Requires agent teams enabled in `.claude/settings.local.json`. See [[Claude Agent Team: Scale SD Lead Intelligence Pipeline]] for full implementation plan.

---

## The Prompt

```
GOAL: Build a prioritized, enriched lead call list for Scale SD (a San Diego contractor 
marketing agency). We need to scrape raw contractor leads, qualify them against our ICP, 
enrich each qualified lead with intelligence about their specific pain points, QA the 
output, and produce a daily call brief that Daniel (our closer) can open at 11am and 
work through in priority order.

Context on Scale SD:
- We sell marketing automation, paid ads, and social media management to contractors
- Target niches: roofing, HVAC, plumbing, restoration, pools, remodeling, general contracting
- Target geography: San Diego County
- Ideal client: established contractor (10+ Google reviews), NOT running paid ads, 
  has social media gaps or a neglected Google Business Profile
- Daniel's calling window is 11am–1pm Tue–Sat — only 10 hours/week. Every call must count.
- We reach out via mobile number only — bypasses front desk, reaches the business owner directly
- Our value prop: we recover missed revenue (missed calls, no follow-up, no booking flow)
  and grow it further with content + ads

Today's target batch:
- Niche: [INSERT NICHE — e.g., "HVAC contractors"]
- Geography: [INSERT AREA — e.g., "San Diego County, CA"]
- Minimum batch size: 40 qualified leads

---

Create a team of 4 agents called "LeadForce" using Sonnet.

---

AGENT 1 — THE SCRAPER
Name: Scraper
Role: Raw lead acquisition from Google Maps for the specified niche and geography.

Tasks:
- Use web search to find contractor listings in the target niche across San Diego County
- Zoom into multiple sub-areas (North County, East County, South Bay, Central SD) to overcome 
  Google's per-search caps and build a large raw list
- For each business capture: business name, phone number, phone type (mobile/landline/fixed), 
  address, website URL (if exists), Google rating, review count, GBP verified status
- Target mobile numbers specifically — flag and deprioritize landlines and fixed lines
- Target minimum: 200 raw leads before passing to Qualifier

Output file: outputs/raw-leads.json
Format:
{
  "leads": [
    {
      "name": "",
      "phone": "",
      "phone_type": "mobile|landline|fixed|unknown",
      "address": "",
      "website": "",
      "google_rating": 0.0,
      "review_count": 0,
      "gbp_verified": true|false
    }
  ]
}

When done: message the Qualifier agent with total lead count and breakdown by phone type.
Own only: outputs/raw-leads.json

---

AGENT 2 — THE QUALIFIER
Name: Qualifier
Role: Score all raw leads against Scale SD's ICP and filter down to the best prospects.

Wait for: Scraper to send raw lead count before starting.

Qualification scoring (0–10 fit score per lead):
- Has mobile number: REQUIRED — remove any lead without a mobile number entirely
- Target niche match: +2 (already filtered by Scraper, but verify)
- 10+ Google reviews: +2 (established business, has reputation to protect)
- Rating 3.5–4.5: +2 (cares about quality but has room to improve — pain point)
- Has a website: +1 (already investing in marketing; easier sell)
- No active paid ads visible (search Google for their business name + "ads"): +2
- GBP appears incomplete (missing hours, no booking link, sparse description): +1

Scoring tiers:
- Score 7–10: Priority tier — send to Enricher immediately
- Score 5–6: Secondary tier — include in output but flag as lower priority
- Score 0–4: Discard

If Priority tier count is below 30, message the Scraper and request an additional 
scrape pass in underrepresented areas or adjacent niches.

Output file: outputs/qualified-leads.json
Format:
{
  "priority": [...leads with fit_score, score_breakdown, and disqualification notes],
  "secondary": [...leads],
  "discarded_count": 0
}

When done: send the priority-tier leads to the Enricher agent with a note on total counts.
Own only: outputs/qualified-leads.json

---

AGENT 3 — THE INTELLIGENCE ENRICHER
Name: Enricher
Role: Build a dossier on each priority-tier lead so Daniel's calls feel researched, 
not cold.

Wait for: Qualifier to send priority-tier leads before starting.

For each priority-tier lead, research and record:
1. Social media presence — what platforms? When was their last post? Is it dormant?
2. Review recency — when was the last Google review? Are they responding to reviews?
3. Automation gaps — do they have a "text us" or booking link on GBP? Any chatbot?
4. Ad activity — search Meta Ad Library and Google for evidence of paid ads running
5. Website quality — does it have a contact form? Is it mobile-optimized? How old does it look?
6. One specific recent thing about their business (new project, recent review, seasonal context)

Pain point scoring (0–10):
- No social media or dormant 6+ months: +3
- Negative reviews unanswered: +2
- No website or clearly outdated: +2
- No booking/contact flow on GBP: +2
- No paid ads: +1 (already in fit score but doubles as pain point signal)

Combined score = fit_score (from Qualifier) + pain_point_score (from Enricher) = priority out of 20.

For each lead, write a "conversation hook" — 2 sentences Daniel says in the first 
30 seconds of a call. It must:
- Name a SPECIFIC observable gap (not a generic pitch)
- Frame it as lost revenue or missed opportunity, not "you need marketing"
- Sound like something a person would say, not a script

Example hook:
"Hey [Name], I was looking at your Google profile — you've got 63 reviews which is 
solid for HVAC in SD, but I noticed you have no booking link and your last post was 
from January. With summer coming up, you're probably missing 4-5 calls a week from 
people who click off before they find your number."

Output file: outputs/lead-intelligence.json
Format (extends qualified-leads.json entries):
{
  "name": "",
  "phone": "",
  "fit_score": 0,
  "pain_point_score": 0,
  "priority_score": 0,
  "social_media": { "platforms": [], "last_active": "", "status": "active|dormant|none" },
  "review_status": { "last_review_date": "", "owner_responding": true|false },
  "automation_gaps": [],
  "ads_running": true|false,
  "website_status": "good|outdated|none",
  "conversation_hook": "",
  "quick_facts": ""
}

When done: send all enriched profiles to the QA agent for review.
If Qualifier sends back a lead that needs re-enrichment, prioritize it immediately.
Own only: outputs/lead-intelligence.json

---

AGENT 4 — QA + PRIORITY RANKER
Name: QA
Role: Quality gate, final ranker, and deliverable producer.

Wait for: Enricher to send completed profiles.

Quality checks — for each lead, verify:
- Conversation hook is specific (references an actual observable detail, not generic)
- Priority score math is correct (fit + pain = total)
- Phone number is mobile type (reject any non-mobile that slipped through)
- All required fields populated (no empty hooks, no missing scores)

If a lead fails QA: send it back to the Enricher with specific notes on what's missing 
or vague. Do NOT pass a lead with a generic or placeholder hook.

Once all leads pass QA:
1. Sort all leads by priority_score descending
2. Write the Daily Call Brief (priority-call-list.md) in this format per lead:

---
#[RANK] — [BUSINESS NAME] | [NICHE] | Score: [X]/20
Phone: [mobile number]
Hook: "[conversation hook]"
Quick facts: [rating]★, [N] reviews, [social status], [ads running: yes/no], [website status]
---

3. Write the GHL import CSV (ghl-import.csv) with columns:
   First Name, Last Name (use business owner name if found, else blank), 
   Business Name, Phone, Email, Tags (include: "agent-lead", score tier, niche, date)

4. Write a 5-line summary for the main session:
   - Total leads scraped
   - Total qualified (priority + secondary)
   - Total passed QA
   - Average priority score of top 10
   - One flag or insight (e.g., "HVAC leads scored highest — strong ICP match today")

Output files:
- outputs/priority-call-list.md (Daniel's daily brief)
- outputs/ghl-import.csv (power dialer ready)

Own only: outputs/priority-call-list.md and outputs/ghl-import.csv

When all deliverables are complete and saved: signal the main session that the 
LeadForce run is complete and ready for review.

---

FINAL DELIVERABLES (main session collects from agents):
1. outputs/priority-call-list.md — sorted call list with hooks, ready for Daniel at 11am
2. outputs/ghl-import.csv — drag-and-drop into GoHighLevel power dialer
3. A brief summary from QA: total leads, scores, and one key insight

Do not shut down any agent until it has confirmed all files are saved and the main 
session has acknowledged receipt of deliverables.
```

---

## Usage Notes

**Before running:**
1. Replace `[INSERT NICHE]` and `[INSERT AREA]` with today's target (e.g., "HVAC contractors", "San Diego County, CA")
2. Make sure agent teams are enabled in `.claude/settings.local.json`
3. Have a `CLAUDE.md` in the project root with Scale SD context (ICP, value props, niche list) — the agents will read this on wake-up

**Calibrating over time:**
- After Daniel's calls, note which leads actually converted to booked calls
- Feed the priority scores of converting leads back to Ashen/Justin — adjust scoring weights accordingly
- Refine hook formulas based on what Daniel says resonates on calls

**Scaling:**
- Increase batch size by adjusting "Minimum batch size: 40" to higher numbers
- Run multiple niche batches in parallel by spawning separate LeadForce runs with different niche inputs
- Connect `ghl-import.csv` output directly to a GHL workflow that auto-loads the power dialer

---

## Related Pages

- [[Claude Agent Team: Scale SD Lead Intelligence Pipeline]]
- [[Claude Agent Teams]]
- [[Lead Generation and Qualification System]]
- [[Lead Warming System]]
- [[Setter-Closer Sales Model]]
- [[GoHighLevel]]
