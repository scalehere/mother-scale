---
title: "Scale SD — AI-Powered Lead Growth System: Full Stack Architecture"
type: analysis
tags: [strategy, lead-gen, ai, agent-teams, playwright, ghl, automation, scaling, master-plan]
sources: [how-to-build-claude-agent-teams, unlimited-website-clients-outreach, lead-generation-qualification-system, lead-warming-system, setter-closer-strategy, complete-client-journey-ghl]
updated: 2026-04-13
---

# Scale SD — AI-Powered Lead Growth System: Full Stack Architecture

This is the master strategic document for Scale SD's AI-powered lead acquisition system. It integrates every tool at our disposal — Claude Agent Teams, Playwright MCP, the AutoResearch improvement loop, GoHighLevel, and the setter-closer model — into a single coherent operating stack. Every layer feeds the next. Nothing is manual that can be automated. Nothing is automated that requires human judgment.

---

## The Core Constraint (And How We Break It)

Everything in Scale SD's growth is gated by one constraint: **Daniel's calling window** — 10 hours per week, 11am–1pm, Tuesday through Saturday. That's the ceiling.

The only way to grow is not to extend the calling window. It's to ensure that:
1. Every one of those 10 hours is spent on the highest-probability leads
2. Every call starts with Daniel already knowing the prospect's exact pain points
3. The pipeline feeding that window never runs dry

The current system caps qualified leads at 150/week because manual analysis is the rate limiter. The AI system described here removes that cap entirely. At full throughput: **450+ leads/week**, all pre-qualified, pre-scored, and pre-prepped with caller notes — with no increase in manual work from Ashen or Tad.

---

## The Full Stack: Six Layers

```
┌──────────────────────────────────────────────────────────────────┐
│  LAYER 6: AUTONOMOUS IMPROVEMENT LOOP (Monthly)                  │
│  AutoResearch pattern → Claude Agent Team analyzes batch data    │
│  → updates qualification criteria + SMS templates → iterates     │
└──────────────────────────────┬───────────────────────────────────┘
                               │ better criteria each cycle
┌──────────────────────────────▼───────────────────────────────────┐
│  LAYER 5: CLOSER — Daniel (10 hrs/week)                          │
│  Pre-sorted Hot leads + full prep notes + setter-closer framework│
└──────────────────────────────┬───────────────────────────────────┘
                               │ booked calls
┌──────────────────────────────▼───────────────────────────────────┐
│  LAYER 4: SETTER EXECUTION (GHL + Power Dialer)                  │
│  Works pre-written SMS sequences → positive replies → calls      │
└──────────────────────────────┬───────────────────────────────────┘
                               │ warm leads + outreach sequences
┌──────────────────────────────▼───────────────────────────────────┐
│  LAYER 3: GHL OUTREACH AUTOMATION                                │
│  Tier-tagged import → auto SMS by tier → notifications to setter │
└──────────────────────────────┬───────────────────────────────────┘
                               │ GHL-ready file
┌──────────────────────────────▼───────────────────────────────────┐
│  LAYER 2: LEADOPS — Claude Agent Team + Playwright MCP           │
│  4 agents: Scout → Qualifier (live browser) → Writer → QA/Export│
└──────────────────────────────┬───────────────────────────────────┘
                               │ raw CSV
┌──────────────────────────────▼───────────────────────────────────┐
│  LAYER 1: SCRAPING (Ashen + Tad)                                │
│  tryoutscraper.com + mobile filter → 500+ raw leads/week         │
└──────────────────────────────────────────────────────────────────┘
```

---

## Layer 1: Scraping

**Who:** Ashen + Tad
**Tools:** tryoutscraper.com (paid, ~$12/4,000 leads) or Chrome extension (free, manual area zooming)
**When:** Monday–Tuesday each week, delivering batch by Wednesday morning

**Process:**
1. Target niche + city: e.g., "roofers San Diego," "HVAC Chula Vista," "restoration contractors La Mesa"
2. Run Google Maps scraper — extract business name, phone, website, social URLs, city, niche
3. Run phone validator (tryoutscraper built-in, 100 free credits) → filter to **mobile lines only**
   - Why: mobile = owner's personal cell. Sidesteps front desk, reaches decision-maker directly.
4. Export CSV → drop into `scale-lead-ops/raw/batch-YYYY-MM-DD.csv`

**Volume target:** 500+ raw records → produces ~150 qualified after LeadOps filtering
**Cost:** ~$12–$18/week for paid scraper at this volume

**Niches to rotate (priority order):**
1. Roofing
2. HVAC
3. Plumbing
4. Windows & Doors
5. Remodeling / General Contractor
6. Restoration (mold, water, fire — high job value)
7. Landscaping / Hardscaping

---

## Layer 2: LeadOps — Claude Agent Team + Playwright MCP

This is the engine. Four agents working in parallel. The Playwright MCP gives Agent 2 a live browser — it doesn't just read URLs from a CSV, it actually visits each business's website, Google Business Profile, and social pages in real time, reads the accessibility tree, and scores what it finds.

### The Tech Stack for This Layer

**Enable agent teams** (already done in `agent-teams/.claude/settings.json`):
```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

**Add Playwright MCP** to the LeadOps project settings:
```bash
claude mcp add playwright -- npx @playwright/mcp@latest
```
Or manually in `.claude/settings.json`:
```json
{
  "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" },
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

**Why Playwright MCP over screenshots:**
Playwright MCP uses Playwright's accessibility tree — pure structured data, no vision model needed. It reads page headers, navigation links, button text, form fields, and content structure. For qualifying leads, this is ideal: we need to know if a website has CTAs, testimonials, and a portfolio — all text/structure signals that accessibility trees capture perfectly. Token-efficient. Works headless. No API keys required.

### The Four Agents

```
MAIN SESSION (orchestrates)
     │
     ├──► AGENT 1: Lead Scout
     │    Cleans, standardizes, deduplicates raw CSV
     │    Output: leads_processed.csv
     │    → messages Lead Qualifier when done
     │
     ├──► AGENT 2: Lead Qualifier (uses Playwright MCP)
     │    Visits each lead's website + GMB + social in a live browser
     │    Applies 6-channel scoring rubric
     │    Assigns Hot/Warm/Cold tier + score
     │    Output: leads_qualified.csv
     │    → messages Outreach Writer when done
     │
     ├──► AGENT 3: Outreach Writer
     │    Writes 4-message SMS sequence per Hot/Warm lead
     │    Writes 5-field caller notes per lead
     │    Output: outreach_sequences.csv, caller_notes.md
     │    → messages QA Agent when done
     │
     └──► AGENT 4: QA + Exporter
          Reviews SMS for pitch language and specificity
          Rejects and sends back to Agent 3 if QA fails
          Formats GHL import file
          Output: ghl_import_ready.csv, qa_report.md
          → messages main session when done
```

### Scoring Rubric (used by Agent 2)

Scale SD's 6-channel evaluation. Agent 2 uses Playwright to visit each channel in real time.

| Channel | What Agent 2 Checks | Score Logic |
|---------|---------------------|-------------|
| **Website** | Has it got CTAs? Portfolio/before-after photos? Testimonials? Mobile-friendly structure? Clear service area? | 0=none, 2=basic/template, 5=moderate, 8+=strong (inversion: 0–4 = HOT signal) |
| **Google Business Profile** | Rating, review count, photo quality, last post date, claimed/unclaimed, services listed | 0=unclaimed, 3=claimed/sparse, 6=verified/moderate, 9+=strong |
| **Instagram** | Last post date, follower count, content quality, consistency | 0=none, 2=dormant 90d+, 5=occasional, 8+=consistent |
| **Facebook** | Same as Instagram; bonus flag: "posts in groups looking for work" = STRONG qualifier | 0=none, 2=inactive, 5=occasional, 8+=active/professional |
| **Yelp** | Review count, rating, photo quality, business info completeness | 0=unclaimed, 3=claimed/sparse, 7+=strong |
| **TikTok** | Tried posting in last 90 days | 0=none, 3=tried (positive signal — they know it matters) |

**Total score range: 0–52 (lower = higher conversion likelihood)**

**Tier thresholds:**
- **HOT** — Total score ≤ 18, mobile phone confirmed. Has tried and failed. Losing jobs to better-marketed competitors right now.
- **WARM** — Total score 19–30. Some presence, inconsistent execution.
- **COLD** — Total score 31–42. Mostly established. Harder sell.
- **DISQUALIFY** — Total score 43+. Strong across all channels. Not our market.

### Caller Notes Format (Agent 3 output per lead)

```
## [Business Name] — [Niche] — [City]
Phone: [number] | Tier: HOT/WARM | Score: X/52

WEAKEST CHANNEL: [specific detail — e.g., "Website has no CTAs, no portfolio, 
  last update appears to be 2022 based on copyright footer"]

WHAT THEY'VE TRIED: [evidence of effort — e.g., "Instagram account exists with 
  12 posts from March 2025, then went silent — likely tried a content person 
  who left or got too busy"]

REVENUE LEAKAGE: [what they're visibly losing — e.g., "Competitor 'ABC Roofing' 
  has 4.8 stars / 210 reviews, ranks #1 in maps for 'roofer San Diego'. 
  This lead has 3.1 stars / 7 reviews and doesn't appear in map pack at all — 
  they're invisible to 85% of local search traffic"]

BEST OPENER: [one line for the call — e.g., "Hey [name], I was checking out 
  your Google listing and noticed you guys have some reviews that mention your 
  work is great but the photos don't really show it — wanted to ask about that"]

LIKELY OBJECTION: [one objection to anticipate — e.g., "Price — they're a 
  small operation, likely owner-operated. Frame in terms of jobs recovered, 
  not monthly retainer cost"]
```

### SMS Sequence Format (Agent 3 output per lead)

**Message 1 — Initial touch (fires within 1 hour of GHL import for Hot leads):**
Casual, no pitch, one genuine specific observation. Example:
> "Hey [name], this is [Setter], was looking you guys up on Google. Noticed you're in [city] — you guys do [niche], right?"

**Message 2 — Follow-up 1 (48h if no reply):**
Light, not pushy. Just a nudge.
> "Hey — still [Business Name]? Just making sure I got the right number."

**Message 3 — Follow-up 2 (Day 5, adds light value):**
One specific, genuine observation tied to their gap.
> "Totally get it if you're slammed. Just wanted to mention — [one-line observation about their specific gap, e.g., 'your Google reviews are showing some great feedback but the profile photos don't match the quality of your work']. Thought that might be worth a quick chat."

**Message 4 — Final (Day 9, low pressure):**
Closes the loop without burning the contact.
> "No worries if timing isn't right. We work with a few [niche] contractors in [city] — if you ever want to see what a few quick fixes could do for your call volume, just say the word."

**Rule for all messages:** Never use: agency, marketing, social media, ads, services, packages, "we help," "I wanted to reach out," "I came across your business." Every message must feel like a human who actually looked them up.

**On positive reply:** Setter responds ONLY: "Hey, I just tried to call you." Then calls immediately. Never sell on SMS. The goal of every SMS is to get a phone call. Nothing more.

---

## Layer 3: GHL Outreach Automation

After Agent 4 exports `ghl_import_ready.csv`, Ashen or Tad imports it into GHL. From there, automation handles everything.

### Import & Tag Structure

Each contact imports with:
- `niche_tag` — roofing, hvac, plumbing, etc.
- `tier_tag` — HOT, WARM, COLD
- `pipeline_stage` — Priority Outreach (Hot), Standard Outreach (Warm), Nurture (Cold)
- `notes` — condensed caller notes (280 chars for GHL notes field)

### Automation Workflows by Tier

**HOT lead workflow:**
1. Contact imported → tag "HOT" applied
2. Immediate notification to setter: SMS + GHL app push: "Hot lead: [Business] — [City] — [Niche] — call within 5 min if they reply"
3. 1 hour delay → SMS Message 1 fires
4. Positive reply detected → immediate setter notification → remove from auto sequence → setter takes over manually
5. No reply after 48h → Message 2 fires
6. No reply after Day 5 → Message 3 fires
7. No reply after Day 9 → Message 4 fires → tag "DND-Exhausted" → remove from outreach forever

**WARM lead workflow:**
1. Contact imported → tag "WARM" applied
2. Same-day SMS Message 1 fires (no immediate notification — setter monitors)
3. Follow-up cadence: 48h → Day 5 → Day 9
4. Positive reply → setter notification → manual takeover

**COLD lead workflow:**
1. Contact imported → tag "COLD" applied
2. Day 3: Message 1 fires
3. Cadence: Day 7 → Day 14 → Day 21
4. COLD leads are lower priority — setter works HOT/WARM first

### Power Dialer Setup

For any lead who replies positively:
1. GHL Conversations → Manual Actions → "Let's Start"
2. Auto-dials lead immediately
3. After call: mark outcome (booked / not interested / callback / no answer)
4. Outcome branches to pipeline stage updates automatically:
   - Booked → move to "Sales Call" stage → GHL calendar link sent
   - Not interested → tag "DND-Declined" → never contact again
   - Callback → schedule follow-up in GHL
   - No answer → auto-SMS: "Hey, just tried calling — want me to try back later?"

---

## Layer 4: Setter Execution

**Who:** Setter (intern or junior team member)
**Tools:** GHL conversations dashboard, power dialer, pre-written SMS sequences from Agent 3

**Daily Workflow:**
1. Log into GHL — check notification dashboard for positive replies first
2. For every positive reply: call immediately, say only "Hey, I just tried to call you." Book the call or get a callback time.
3. Check HOT tier contacts — any new imports that haven't engaged after 24h? Note for follow-up.
4. Power dialer: work through any scheduled callbacks from prior days
5. Monitor Message 3 and 4 sends — anything that replies late gets the same treatment

**KPIs:**
- 50–100 outbound touches/day (SMS + calls combined)
- 10–20 conversations/day
- 3–5 booked calls/day for Daniel

**The setter never:**
- Has a full SMS conversation
- Tries to sell on SMS
- Improvises message language (uses pre-written sequences only)
- Moves a lead to Daniel without a confirmed booked call

---

## Layer 5: Closer — Daniel

**Who:** Daniel
**Tools:** GHL calendar, caller notes from Agent 3, setter-closer framework

**Calling window:** 11am–1pm, Tuesday–Saturday (10 hours/week — the fixed constraint)

**What changes with this system:**
- Daniel only calls leads that have been scored HOT
- Every call starts with the 5-field caller notes already reviewed
- He knows their weakest channel, what they've tried, the revenue leakage signal, and the likely objection before the call begins

**Call framework (from [[Setter & Closer Strategy]]):**
1. Intro — build trust: "Just want to learn about your business and see if this makes sense"
2. Diagnose — most important: how many calls/week? Do they miss calls? How do they follow up? How many jobs are they closing?
3. Pain amplification: make them articulate what they're losing in jobs/month, not just acknowledge a problem
4. Pitch — simple: missed call text-back + follow-up automation + booking system + CRM + reviews
5. Close: "Based on what you said, I think this could help you pretty quickly. Do you want help setting this up?"

**Pricing delivery:** "It's a one-time setup + monthly to manage and optimize."
- Setup: $500–$1,000
- Monthly: $800–$1,500 (current packages go up to $2,500 for full stack)

---

## Layer 6: The Autonomous Improvement Loop

This is the highest-leverage layer and the one most agencies will never build. Adapted directly from the AutoResearch pattern (Karpathy's `program.md` approach): **a self-modifying loop that tests changes against a fixed metric and keeps only what improves results.**

In AutoResearch, the agent modifies `train.py` (the model/optimizer code), trains for a fixed 5-minute budget, checks `val_bpb`, and keeps or discards. In Scale SD's system, the "code" is the qualification rubric and SMS templates. The "metric" is close rate on Hot-tier leads. The "budget" is one batch cycle (150 leads).

### What Gets Iterated

The LeadOps project has two "mutable files" (like AutoResearch's `train.py`):
1. `qualification_rubric.md` — the scoring criteria Agent 2 applies. What makes a HOT lead? What channel weights matter most? What disqualifiers are actually correlated with "won't buy"?
2. `sms_templates.md` — the 4 base message templates Agent 3 uses. Which opener phrases get replies? Which follow-up structures book more calls?

Everything else is fixed (like AutoResearch's `prepare.py`): the pipeline structure, the GHL setup, the calling window, the closer framework.

### The Monthly Loop

**Trigger:** Run at the start of each month after 4+ weeks of batch data has accumulated.

**Step 1 — Track the metric:**
After each batch cycle, record in `results.tsv` (tab-separated):
```
batch_date    hot_leads    hot_reply_rate    hot_booking_rate    hot_close_rate    niche    notes
2026-04-14    45           4.4%              2.2%                33%               roofing   baseline
```

**Step 2 — Spawn the Improvement Team (monthly):**
```
Goal: Analyze 4 weeks of batch performance data and propose specific, testable 
improvements to our lead qualification rubric and SMS templates. We want higher 
close rates on Hot-tier leads. Do NOT propose vague improvements — every change 
must be specific and falsifiable (we can measure if it worked in the next batch).

Create a team of 4 agents using Sonnet called ImprovementLoop.

Agent 1 — Data Analyst: Read results.tsv and all batch qa_reports from the last 
4 weeks. Identify: which niches have the highest close rates? Which tiers are 
converting below expectation? Are there patterns in the leads that closed vs. 
those that didn't? Own: analysis_report.md

Agent 2 — Rubric Optimizer: Based on Data Analyst's findings, propose specific 
changes to qualification_rubric.md. For each proposed change: state what you're 
changing, why, and what metric should improve. Own: rubric_proposals.md

Agent 3 — Copy Optimizer: Based on Data Analyst's findings, propose specific 
changes to sms_templates.md. For each proposed change: state the current template, 
the proposed revision, why it should improve reply/booking rates. 
Own: copy_proposals.md

Agent 4 — Devil's Advocate: Challenge every proposal from Agents 2 and 3. 
For each proposal, state: what could go wrong, what assumption it relies on, 
whether there's a simpler explanation for the data. Send your critique back to 
Agents 2 and 3. They must revise proposals that don't survive your challenge.

Final deliverables: 
- final_rubric_v[N].md — updated qualification rubric ready to replace the current one
- final_templates_v[N].md — updated SMS templates ready to replace the current ones
- improvement_changelog.md — what changed, why, what metric we expect to move
```

**Step 3 — Apply and test:**
- Swap in `final_rubric_v[N].md` as the new `qualification_rubric.md`
- Swap in `final_templates_v[N].md` as the new `sms_templates.md`
- Run next batch cycle
- Record results in `results.tsv`

**Step 4 — Keep or revert (AutoResearch logic):**
- If hot_close_rate improved → commit changes, advance to next iteration
- If hot_close_rate stayed same or dropped → revert (restore previous rubric/templates), log "discard" in results.tsv, investigate why

**This is the compounding mechanism.** Every month the system gets more accurate at identifying the leads most likely to convert and better at writing the messages most likely to get replies. The humans don't have to figure out what's working — the agent team does it for them.

---

## Project Structure: `scale-lead-ops/`

This is the Claude Code project folder for the LeadOps system. Create it at:
`/Users/ashenafew/Desktop/SCALE/scale-lead-ops/`

```
scale-lead-ops/
├── .claude/
│   └── settings.json           ← agent teams enabled + Playwright MCP
├── CLAUDE.md                   ← agent reference doc (see wiki/analysis/leadops-claude-md-template.md)
├── raw/
│   └── batch-YYYY-MM-DD.csv    ← Ashen/Tad drop scraped files here
├── processed/
│   ├── leads_processed.csv     ← Agent 1 output
│   ├── leads_qualified.csv     ← Agent 2 output
│   ├── outreach_sequences.csv  ← Agent 3 output
│   ├── caller_notes.md         ← Agent 3 output
│   ├── ghl_import_ready.csv    ← Agent 4 output
│   └── qa_report.md            ← Agent 4 output
├── ghl-exports/
│   └── [archived final exports by date]
├── criteria/
│   ├── qualification_rubric.md ← the "mutable file" for Improvement Loop
│   └── sms_templates.md        ← the "mutable file" for Improvement Loop
└── tracking/
    └── results.tsv             ← batch performance log (the AutoResearch results file)
```

---

## Implementation Timeline

### Week 1 — Foundation

**Day 1:**
- [ ] Create `scale-lead-ops/` folder at `/Users/ashenafew/Desktop/SCALE/scale-lead-ops/`
- [ ] Copy `.claude/settings.json` from `agent-teams/` as the base
- [ ] Add Playwright MCP: `claude mcp add playwright -- npx @playwright/mcp@latest` (run from within scale-lead-ops)
- [ ] Create project folder structure (raw/, processed/, ghl-exports/, criteria/, tracking/)
- [ ] Write `CLAUDE.md` using the template in `wiki/analysis/leadops-claude-md-template.md`
- [ ] Write `criteria/qualification_rubric.md` (full rubric as standalone reference file)
- [ ] Write `criteria/sms_templates.md` (4 base templates as standalone reference file)

**Day 2:**
- [ ] Run first mini-batch: drop a 20-lead CSV into `raw/`
- [ ] Run LeadOps prompt (no Playwright yet — use URL-only scoring)
- [ ] Review all 20 outputs manually. How accurate are the tiers? How good are the notes?
- [ ] Calibrate rubric scores based on review

**Day 3–5:**
- [ ] Enable Playwright MCP for Agent 2 in the prompt
- [ ] Re-run the 20-lead test batch with live browser visits
- [ ] Compare outputs: does live browsing improve accuracy vs URL-only?
- [ ] Identify any Playwright navigation issues (some sites block headless browsers — note fallback behavior)

---

### Week 2 — First Full Batch

**Monday:**
- [ ] Ashen + Tad run scraper for 500+ raw contractor leads (San Diego area, mixed niches)
- [ ] Mobile filter applied — drop final CSV in `raw/`

**Tuesday:**
- [ ] Run LeadOps agent team on full batch
- [ ] Review qa_report.md — check approval rate, top 10 hottest leads
- [ ] Do a 10% manual spot-check of qualification accuracy

**Wednesday:**
- [ ] Import `ghl_import_ready.csv` into GHL
- [ ] Verify tier tags applied correctly on 10 sample contacts
- [ ] Confirm automation workflows fire correctly for a test Hot contact

**Thursday–Friday:**
- [ ] Setter begins working SMS sequences for first batch Hot leads
- [ ] Daniel reviews caller_notes.md for any calls that get booked
- [ ] Track: reply rate, booking rate on first batch

---

### Week 3 — GHL Automation Build

Build the full GHL automation stack (this can run parallel to batch 2 scraping):

- [ ] HOT lead workflow: import → notification → 1hr SMS → 48h follow-up → Day 5 → Day 9 → DND
- [ ] WARM lead workflow: Day 0 → 48h → Day 5 → Day 9 → DND
- [ ] COLD lead workflow: Day 3 → Day 7 → Day 14 → Day 21 → DND
- [ ] Positive reply detection → setter notification → remove from auto sequence
- [ ] Power dialer workflow: contacts → manual actions → outcome branching
- [ ] Add qualifying question notes field to power dialer view

---

### Week 4 — Full Operation

- [ ] 3 batches/week running (Monday + Wednesday + Friday scrapes)
- [ ] Ashen + Tad: scraping only, no manual analysis
- [ ] Setter: outreach execution only, no copywriting
- [ ] Daniel: Hot leads only, full prep notes for every call
- [ ] Begin `results.tsv` tracking: one row per batch

---

### Month 2 — First Improvement Loop

- [ ] 4 weeks of batch data collected in `results.tsv`
- [ ] Run Improvement Loop agent team
- [ ] Review proposals — apply changes to `qualification_rubric.md` and `sms_templates.md`
- [ ] Run next batch with updated criteria
- [ ] Measure delta in close rate
- [ ] Keep or revert (AutoResearch rule: keep only what moves the metric)

---

### Month 3+ — Scale

At this point the system is self-sustaining and self-improving:
- 450+ leads/week → 2–4% SMS reply rate → 9–18 positive replies/week → 3–7 closed per week
- Monthly improvement loop refining what "HOT" means and what messages work
- Daniel's pipeline permanently full — constrained only by his calling window
- Next unlock: hire a second closer or extend calling window with a trained setter-closer hybrid

---

## Revenue Math

| Metric | Conservative | Target |
|--------|-------------|--------|
| Raw leads scraped/week | 300 | 500+ |
| Qualified leads/week | 120 | 180+ |
| Hot leads/week (30%) | 36 | 54 |
| SMS sent/week | 120 | 180 |
| Positive replies (3%) | 3–4 | 5–7 |
| Calls booked/week | 2–3 | 4–6 |
| Closes/week (25%) | 0.5–1 | 1–2 |
| Avg deal value (MRR) | $1,500 | $2,000 |
| **New MRR/week** | **$750–$1,500** | **$2,000–$4,000** |
| **New MRR/month** | **$3,000–$6,000** | **$8,000–$16,000** |

Current baseline MRR: $4,500/month (3 clients). This system targets a 3–4× increase within 60 days of full operation.

---

## Key Risks and Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Playwright blocked by websites | Agent 2 can't visit some sites | Fallback: score from URL data + publicly visible metadata. Flag "browser-blocked" leads for manual review. |
| Agent teams ~7× token cost | Expensive at scale | Use Haiku for Agents 1 + 4 (mechanical tasks), Sonnet for Agents 2 + 3 (judgment tasks). Cost per batch estimated $3–8. |
| GHL SMS compliance (TCPA) | Legal exposure | Never use purchased lists for SMS without consent-acquisition step. Use organic Google Maps data (publicly listed phone numbers). Add DND automation on first negative response. |
| Agents overwrite each other's files | Data corruption | Strict file ownership: each agent writes only to its own named output file. QA agent reads but never modifies Agent 3's files — it produces its own export. |
| No session resumption | Can't restart a mid-run | Run batches during low-interruption windows. If a session dies mid-run, re-run from the last checkpoint file (processed/ folder shows what completed). |
| Improvement loop makes things worse | Lower close rate | AutoResearch rule strictly applied: if metric drops, revert. Keep `results.tsv` as the ground truth. Never discard a working version without proof the new one is better. |

---

## The Compound Effect

Most agencies treat outbound as a manual grind with diminishing returns — the system gets worse over time because people get tired, quality drops, and the list gets saturated. This system inverts that:

- Each batch produces **more data** about what converts → Improvement Loop gets smarter
- Each month the qualification rubric **gets more accurate** → fewer wasted calls
- Each month the SMS templates **get more effective** → higher reply rates
- Ashen + Tad's time **shifts entirely to scraping volume** → larger top-of-funnel
- Daniel's 10 calling hours **become more valuable** → higher close rate per hour

The ceiling isn't the technology. It's Daniel's 10 hours/week. When that becomes the bottleneck — when the pipeline is overflowing with Hot leads and Daniel can't take more calls — that's the signal to hire the next closer. That's when Scale SD scales.

---

## Related Wiki Pages

- [[Lead Intelligence Agent Team Plan]] — the LeadOps agent team prompt and detailed agent specs
- [[LeadOps CLAUDE.md Template]] — ready-to-use CLAUDE.md for the scale-lead-ops project
- [[Lead Generation and Qualification System]] — Scale SD's original manual process
- [[Lead Warming System]] — 6-channel warmth scoring that can feed into tier assignment
- [[Setter-Closer Sales Model]] — the human execution layer this system feeds
- [[Complete Client Journey — GoHighLevel]] — the downstream pipeline leads enter when they close
- [[Claude Agent Teams]] — concept page for agent teams framework
- [[Playwright MCP]] — concept page for browser automation tool
- [[Autonomous Improvement Loop]] — concept page for the AutoResearch-adapted improvement pattern
- [[GoHighLevel]] — CRM running all outreach automation
