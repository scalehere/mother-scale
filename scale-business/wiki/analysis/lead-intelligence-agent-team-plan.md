---
title: "Lead Intelligence Agent Team — Implementation Plan & Prompt"
type: analysis
tags: [claude-agents, lead-gen, automation, outreach, ai, implementation]
sources: [how-to-build-claude-agent-teams, unlimited-website-clients-outreach, lead-generation-qualification-system, lead-warming-system, setter-closer-strategy]
updated: 2026-04-12
---

# Lead Intelligence Agent Team — Implementation Plan & Prompt

This document defines the architecture, implementation roadmap, and ready-to-use Claude Code prompt for building Scale SD's AI-powered lead intelligence system using Claude agent teams.

---

## The Problem This Solves

Scale SD's current lead process has one fatal bottleneck: **manual analysis**. Ashen and Tad scrape leads, then must manually open each business's website, Instagram, Facebook, Google Business Profile, Yelp, and TikTok — evaluate all of them, write notes, score quality, and decide pass/fail. This is:

- Slow: 150 leads/week is the target; manual review limits throughput
- Inconsistent: note quality is the direct driver of call conversion, and it varies person-to-person
- Low-leverage: the team's most time-consuming work is exactly the kind of repetitive analysis AI is best at

Meanwhile, Daniel's calling window is fixed at 10 hours/week (11am–1pm, Tue–Sat). Every minute he spends on a poorly-qualified or poorly-prepped lead is wasted. The constraint isn't time — it's **lead quality and preparation**.

The agent team replaces manual analysis entirely, and adds a layer the current system doesn't have at all: **conversion likelihood scoring** that ranks leads so the hottest ones get called first.

---

## What the Agent Team Does

Takes a raw scraped CSV (from Google Maps / Yelp / tryoutscraper.com) and produces:

1. A **qualified leads file** with 6-channel scores, tier (Hot/Warm/Cold), and prioritized ranking
2. **Caller notes** for each lead — specific weaknesses, sales angles, conversation starters
3. **Personalized SMS sequences** (4 messages per lead) written in the setter's voice
4. A **GHL-ready import file** formatted for direct upload and tagged by tier
5. A **batch summary report** — stats, top 10 hottest leads, and quality flags

---

## Agent Team Architecture: "LeadOps"

Four agents. Each owns specific outputs. They communicate directly. The main session orchestrates and produces final deliverables.

```
┌─────────────────────────────────────────────────────────┐
│                    MAIN SESSION                          │
│              (orchestrates, produces final files)        │
└─────────────┬─────────────────────────────┬─────────────┘
              │                             │
    ┌─────────▼──────────┐     ┌────────────▼────────────┐
    │   AGENT 1          │     │   AGENT 2               │
    │   Lead Scout       │────▶│   Lead Qualifier        │
    │  (Data Processor)  │     │  (Scoring & Triage)     │
    └────────────────────┘     └────────────┬────────────┘
                                            │
                               ┌────────────▼────────────┐
                               │   AGENT 3               │
                               │   Outreach Writer       │
                               │  (SMS + Caller Notes)   │
                               └────────────┬────────────┘
                                            │
                               ┌────────────▼────────────┐
                               │   AGENT 4               │
                               │   QA + Exporter         │
                               │  (Review & GHL Format)  │
                               └─────────────────────────┘
```

---

### Agent 1 — Lead Scout (Data Processor)

**Role:** Takes the raw scraped CSV, cleans it, enriches it, and hands off a standardized file.

**Responsibilities:**
- Remove rows missing phone number OR any online presence URL
- Standardize columns: `business_name`, `phone`, `website`, `instagram`, `facebook`, `google_business`, `yelp`, `tiktok`, `city`, `niche`, `scrape_source`
- Deduplicate by phone number
- Detect and flag mobile vs. landline (mobile = prioritized; landline = lower priority, still included but flagged)
- Tag each lead with the contractor niche (roofing, HVAC, plumbing, windows/doors, remodeling, restoration, landscaping, etc.)

**Owns:** `leads_processed.csv`

**When done:** Message Lead Qualifier with the file path and a count of leads processed.

---

### Agent 2 — Lead Qualifier (Scoring & Triage)

**Role:** Evaluates each lead's online presence across Scale SD's 6-channel rubric and assigns a tier.

**Scale SD's Qualification Criteria (from internal system):**

| Channel | Disqualify (mark red) | Qualify (pass) |
|---------|----------------------|----------------|
| Website | Strong, conversion-optimized, has social proof | Outdated, poorly designed, missing, no CTA, no portfolio |
| Instagram | 3K+ followers, consistent professional content | Posted in 90 days but inconsistent; low quality; no brand |
| Facebook | Consistent, professional presence | Inconsistent; posts in groups to find work (signals desperation) |
| Google Business | Complete, verified, strong reviews | Missing info, low reviews, unclaimed, no posts, low-quality photos |
| Yelp | Strong reviews, professional photos | Low reviews, bad images, sparse/unmanaged |
| TikTok | — | Has account, tried posting in last 90 days |

**Tier Assignment:**
- **HOT** — weak on 3+ channels, no active ad spend detected, phone is mobile. Perfect prospect: they've tried, failed, and are actively losing jobs to competitors.
- **WARM** — weak on 1–2 channels, some presence but inconsistent execution.
- **COLD** — mostly established online, only minor gaps. Harder sell, call last.
- **DISQUALIFY** — all channels strong. Remove. Do not call.

**Score components (0–10):**
- Website quality: 0 (none), 2 (outdated/basic), 4 (moderate), up to 10 (excellent — disqualify)
- GMB score: reviews count, completeness, photo quality
- Social consistency score: recency and regularity of posts across IG/FB/TikTok
- **Inversion rule:** low scores = higher conversion likelihood. Sort ascending to surface hottest leads.

**Owns:** `leads_qualified.csv` with columns: all of Agent 1's columns + `website_score`, `gmb_score`, `social_score`, `overall_warmth_score`, `tier`, `qualification_notes`

**When done:** Message Outreach Writer with file path and count by tier.

---

### Agent 3 — Outreach Writer (SMS + Caller Notes)

**Role:** For every Hot and Warm lead, write a personalized 4-message SMS sequence AND detailed caller prep notes. This replaces the manual note-writing that currently bottlenecks the team.

**SMS Sequence Structure (per lead):**

Message 1 — Initial touch (casual, no pitch):
> "Hey [first name if available / "man"], this is [Setter Name], was looking you guys up on Google. [One specific, genuine observation about their business — a compliment or recognition that shows they were actually looked up]."

Message 2 — First follow-up (if no reply after 24–48h):
> "Hey — still [business name]? Just wanted to make sure you got my message."

Message 3 — Second follow-up (add light value):
> "Totally understand if you're slammed. Lots of contractors we work with in [city] are getting crushed with jobs this time of year. Wanted to share something quick — [1-line hook related to their specific gap, e.g., 'your Google Business has room to pull in more calls without spending on ads'].

Message 4 — Final follow-up (low pressure close):
> "No worries if timing isn't right. If you ever want to see what a few quick fixes to [specific gap] could do for your call volume, just say the word."

**Caller Notes Structure (per lead):**
- **Their weakest channel** — what specifically is wrong (e.g., "website has no CTAs, no before/after photos, no testimonials")
- **What they've tried** — evidence of effort (e.g., "Has Instagram, posted 6 weeks ago, then stopped — likely tried hiring someone")
- **Revenue leakage signal** — estimate of what they're losing (e.g., "3.2-star GMB with 8 reviews vs. competitors at 4.7 with 80+ — they're invisible in map pack")
- **Best opener** — the single best conversation-starting line for Daniel or the setter to open the call with
- **Objection to anticipate** — based on their profile, the most likely pushback (see [[Objection Handling Guide — SD Contractors]])

**Owns:** `outreach_sequences.csv`, `caller_notes.md`

**When done:** Message QA Agent with both file paths.

---

### Agent 4 — QA + Exporter

**Role:** Reviews all SMS sequences for tone, compliance, and quality. Rejects and sends back anything that reads like a pitch or is too generic. Formats approved leads for GHL import.

**QA Checklist per lead:**
- [ ] Message 1 does NOT contain words: "agency," "marketing," "social media," "ads," "services," "packages," "we help," "I wanted to reach out"
- [ ] Message 1 feels like it came from a human who actually looked them up
- [ ] The specific observation in Message 1 is genuinely specific to that business (not copy-pasted language)
- [ ] Follow-up messages escalate value without escalating pressure
- [ ] Caller notes include all 5 required fields
- [ ] No duplicate business names in the final file

**If QA fails:** Send the flagged rows back to Outreach Writer with specific feedback. Do not approve generic sequences.

**GHL Export Format:**
```
first_name, last_name (business owner name if available, else blank),
business_name, phone, email (if available), city, niche_tag, tier_tag,
website, notes (caller notes condensed to 300 chars for GHL notes field),
pipeline_stage (Hot=Stage 1 Priority, Warm=Stage 2, Cold=Stage 3),
do_not_contact (flag any disqualified leads)
```

**Owns:** `ghl_import_ready.csv`, `qa_report.md`

**Final message to main session:** QA complete. Approval rate, rejection rate, top 10 hottest leads by name + score, any batch-level observations.

---

## The Example Prompt

This is the exact prompt to paste into Claude Code to run a full lead batch. Adjust `[BATCH FILE]`, `[SETTER NAME]`, and `[CITY]` per run.

---

```
Goal: Process a batch of contractor leads scraped from Google Maps and produce a 
GHL-ready import with prioritized qualification scores and personalized SMS sequences 
for every Hot and Warm lead. The end result should be a file I can import directly 
into GoHighLevel, a set of caller notes for the setter/closer, and a QA report. 
We are Scale SD — a contractor automation agency based in San Diego. We help 
contractors in roofing, HVAC, plumbing, windows/doors, remodeling, and restoration 
close more jobs by fixing their online presence and automating their follow-up. 
Our ideal prospect has tried to build an online presence but isn't executing 
consistently — they have 1-3 weak channels, a mobile phone number, and are losing 
jobs to competitors with better Google profiles and websites. We do NOT want to 
contact businesses with a strong, consistent online presence across all 6 channels.

The raw leads CSV is at: [BATCH FILE PATH]
The setter's name is: [SETTER NAME]
Primary city/region: [CITY]

Create a team of 4 agents using Sonnet called LeadOps.

Agent 1 — Lead Scout: You are the Lead Scout on the LeadOps team. Your job is to 
take the raw scraped CSV at [BATCH FILE PATH] and produce a clean, standardized file. 
Remove any lead missing a phone number AND a website/social URL. Deduplicate by phone. 
Standardize all columns to: business_name, phone, phone_type (mobile/landline/unknown), 
website, instagram, facebook, google_business_url, yelp, tiktok, city, niche, 
scrape_source. Detect phone type where possible — flag mobile lines as priority. 
Tag each lead's niche based on their business name or category. 
Save your output to leads_processed.csv. 
When done, message Lead Qualifier with the file path and the total number of 
leads processed.

Agent 2 — Lead Qualifier: You are the Lead Qualifier on the LeadOps team. 
Wait for Lead Scout's message before starting. 
Your job is to visit each lead's online presence and score them using Scale SD's 
6-channel rubric. For each lead, visit their website, Google Business Profile, 
Instagram, Facebook, Yelp, and TikTok (if URLs available). Assign scores:
- Website (0=none, 2=basic/outdated, 5=moderate, 8+=strong — strong means clear CTAs, 
  portfolio, testimonials, mobile-optimized)
- GMB (0=unclaimed, 2=claimed but sparse, 5=verified with moderate reviews, 
  8+=strong — strong means 4.5+ stars, 50+ reviews, professional photos, regular posts)
- Social (0=no accounts, 2=accounts but dormant 90+ days, 5=occasional posts, 
  8+=consistent and professional)
Tier assignment: HOT = total score under 10 and has mobile phone. 
WARM = total score 10–17. COLD = total score 18–22. DISQUALIFY = 23+.
Write a brief qualification_notes field (2–3 sentences) explaining the tier assignment 
and the single most obvious revenue leakage signal for each lead.
Sort output by total_score ascending (lowest = hottest).
Save to leads_qualified.csv with all original columns plus your new score columns, 
tier, and qualification_notes.
When done, message Outreach Writer with the file path and counts by tier.

Agent 3 — Outreach Writer: You are the Outreach Writer on the LeadOps team. 
Wait for Lead Qualifier's message before starting. 
For every HOT and WARM lead in leads_qualified.csv, write:
(1) A 4-message SMS sequence personalized to that specific business. 
Message 1 must feel like a real human looked them up — include one genuine, 
specific observation (a real weakness or something that shows you noticed their 
business). DO NOT use any of these words: agency, marketing, social media, ads, 
services, packages, "we help", "I wanted to reach out." The sender name is [SETTER NAME].
Follow up messages should escalate value, not pressure.
(2) Caller notes in exactly this format:
- WEAKEST CHANNEL: [specific detail]
- WHAT THEY'VE TRIED: [evidence of past effort from their profiles]
- REVENUE LEAKAGE: [what they're visibly losing, framed in jobs/calls/money]
- BEST OPENER: [one-line conversation starter for the setter/closer]
- LIKELY OBJECTION: [one objection to anticipate based on their profile]
Save SMS sequences to outreach_sequences.csv (one row per lead, 4 message columns).
Save caller notes to caller_notes.md (one section per lead, business name as header).
When done, message QA Agent with both file paths.

Agent 4 — QA + Exporter: You are the QA Agent and Exporter on the LeadOps team. 
Wait for Outreach Writer's message before starting.
Review every SMS sequence in outreach_sequences.csv. Reject any sequence where:
- Message 1 contains pitch language (agency, marketing, ads, services, packages)
- Message 1's specific observation is generic or copy-pasted (not specific to that business)
- Any message feels like a sales pitch instead of human curiosity
For rejected leads, send a message back to Outreach Writer with specific feedback 
on what to fix, then wait for the corrected version before proceeding.
Once all sequences pass QA, export ghl_import_ready.csv with these exact columns: 
first_name, last_name, business_name, phone, city, niche_tag, tier_tag (Hot/Warm/Cold), 
pipeline_stage (Hot=Priority Outreach, Warm=Standard Outreach, Cold=Nurture), 
notes (caller notes condensed to 280 characters), do_not_contact (TRUE for disqualified).
Save a qa_report.md with: total leads reviewed, approval rate, rejection rate, 
list of top 10 hottest leads by name and score, and any patterns you noticed across 
the batch (common weaknesses, common niches, etc.).
When done, message the main session with a summary: QA complete, approval rate, 
top 10 hottest leads, and any critical flags.

Final deliverables the main session should produce once all agents complete:
1. ghl_import_ready.csv — ready for direct GHL import
2. outreach_sequences.csv — personalized 4-message SMS sequence per Hot/Warm lead
3. caller_notes.md — setter/closer prep notes per lead
4. qa_report.md — QA summary with top 10 hottest leads and batch stats
5. A brief batch_summary.md: total processed, qualified by tier, any contradictions 
   or data quality issues worth flagging, and recommended next steps
```

---

## Implementation Roadmap

### Phase 1 — Setup (Day 1–2)

**Step 1: Enable agent teams in Claude Code**

Create or edit `.claude/settings.json` in your leads project:
```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```
Note: the correct variable is `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` (already set in `agent-teams/.claude/settings.json`). Add Playwright MCP in the same file — see [[LeadOps CLAUDE.md Template]] for the full settings block.

**Step 2: Create project structure**

```
scale-lead-ops/
├── .claude/
│   └── settings.local.json
├── CLAUDE.md              ← agent reference doc (Scale SD criteria + voice guide)
├── raw/                   ← drop scraped CSVs here
├── processed/             ← agent outputs land here
└── ghl-exports/           ← final GHL import files
```

**Step 3: Write the project CLAUDE.md**

This is critical. Per Nate Herk's guidelines, agents inherit file access and should be trained on domain context. The project CLAUDE.md for `scale-lead-ops` should include:
- Scale SD's 6-channel qualification rubric (exact disqualifier/qualifier criteria)
- The setter's voice guide (conversational, not corporate, no pitch language)
- Target niches and priority markets (San Diego, contractor types)
- The setter's name and sign-off style
- GHL field mapping guide

**Step 4: Test with a 20-lead mini-batch**

Before running 150 leads, test with a small batch. Review every output manually. Calibrate scores and check SMS quality. Adjust the prompt as needed.

---

### Phase 2 — Pilot Batch (Week 1)

Run a full 150-lead batch. Have Ashen or Tad review the outputs against their current manual process.

Key things to validate:
- Are the tier assignments accurate compared to manual review?
- Are caller notes detailed enough for Daniel to use without opening the lead's profiles?
- Do the SMS sequences pass the "would I reply to this?" test?
- Is the GHL import file clean and staging correctly?

---

### Phase 3 — Optimize & Integrate (Week 2–3)

**Add warmth scoring integration:**
Scale SD already tracks warmth scores across 6 channels (0–10) via Python scripts. Connect this output to the agent team's qualification step. Leads with existing warmth scores above 6 should auto-tier as HOT regardless of online presence score — they've already shown intent.

**Add SMS scheduling context:**
Tell Agent 4 to tag leads with a `best_contact_window` field. Based on contractor behavior patterns (contractors are usually on-site 6am–10am, responsive 12pm–6pm), flag optimal SMS send times.

**Build the GHL automation on the back end:**
Once leads are imported with tier tags:
- HOT → trigger immediate setter notification + power dialer queue entry
- WARM → enter 4-message drip sequence with 48h delays
- COLD → enter 30-day nurture sequence, re-score at end

---

### Phase 4 — Scale (Month 2+)

At full capacity:
- Ashen and Tad shift to **scraping volume only** — no manual analysis
- Agent team runs 3 batches per week (450+ leads/week vs. current 150 target)
- Setter handles only the outreach execution — no copywriting
- Daniel's calling window is fed with pre-sorted Hot leads only
- Weekly QA review: spot-check 10% of outputs manually to catch model drift

**Revenue math:**
- 450 leads/week → ~18 positive SMS replies (4% rate) → 18 calls → 3–7 closes (20–40% rate)
- At $1,500/month average: potential $4,500–$10,500 in new MRR per week at full throughput
- Current bottleneck (manual analysis) was capping Ashen + Tad at 150/week
- Agent team removes that cap entirely

---

## Key Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Agent scores are inconsistent across batches | Anchor scores with 10 manually-scored examples in CLAUDE.md as reference calibration |
| SMS sequences read too generic | QA agent loop catches this; also add 5 "do not write" examples to project CLAUDE.md |
| GHL import fields misalign | Test import on a 5-lead file first; fix column mapping before full batch |
| Agents overwrite each other's files | Strict file ownership in prompt — each agent writes to a uniquely named file |
| Token cost is too high per batch | Use Haiku for Agents 1 and 4 (mechanical tasks); keep Sonnet for Agents 2 and 3 (judgment-heavy) |

---

## What This Changes About the Team's Roles

| Role | Before | After |
|------|--------|-------|
| Ashen | Scraping + manual analysis + qualification | Scraping only + batch QA review (10% spot check) |
| Tad | Scraping + manual analysis + qualification | Scraping only + batch QA review (10% spot check) |
| Setter | Outreach + copywriting follow-up messages | Outreach execution only (messages pre-written) |
| Daniel (Closer) | Calling whatever leads are ready | Calling pre-sorted HOT leads with full prep notes |

---

## Related Wiki Pages

- [[Lead Generation and Qualification System]] — the manual process this automates
- [[Lead Warming System]] — warmth scoring that feeds priority tiers
- [[Setter-Closer Sales Model]] — the human execution layer these outputs feed into
- [[Claude Agent Teams]] — concept page for agent teams framework
- [[GoHighLevel]] — CRM receiving the final export
- [[Objection Handling Guide — SD Contractors]] — referenced in caller notes objection field
