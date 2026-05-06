---
title: "Claude Agent Team: Scale SD Lead Intelligence Pipeline"
type: analysis
tags: [ai, agent-teams, leads, automation, claude, scraping, qualification, outreach]
sources: [claude-agent-teams-guide, unlimited-website-clients-outreach, lead-warming-system, lead-generation-qualification-system, setter-closer-strategy]
updated: 2026-04-12
---

A full implementation plan for a Claude agent team that automates Scale SD's lead pipeline — from raw scraping through intelligent prioritization — so Daniel's 10-hour calling window is spent exclusively on the hottest, most conversion-ready prospects.

---

## The Problem This Solves

Scale SD's current process:
- Ashen and Tad manually scrape Google Maps and Yelp
- Manual filtering from Sheet 1 → Sheet 2 (qualifying)
- The [[Lead Warming System]] Python tracker monitors multi-channel engagement
- Daniel calls during a 10-hour window (11am–1pm Tue–Sat)

**The constraint**: Daniel's calling time is fixed. The only lever is who he calls. Right now, qualification is mostly manual and largely based on whether a business shows up in the scrape — not on how likely they are to convert. The agent team replaces guesswork with scored, enriched intelligence.

---

## What the Agent Team Does

Four specialized agents run in parallel to produce a single output: a prioritized, enriched call list ready for Daniel's power dialer each morning.

```
Raw Niche + Geo Input
         ↓
[Agent 1: Scraper] ─────────────────────────────────────────┐
         ↓                                                    │
[Agent 2: Qualifier] ← ─ ─ asks for more leads if needed ──┘
         ↓
[Agent 3: Intelligence Enricher] (parallel with Qualifier on top leads)
         ↓
[Agent 4: QA + Priority Ranker]
         ↓
Prioritized Call List + GHL Import File + Daniel's Daily Brief
```

---

## The Four Agents

### Agent 1 — The Scraper

**Role**: Raw lead acquisition across target contractor niches in San Diego.

**What it does**:
- Uses web search tools to pull business listings from Google Maps for specified niches: roofing, HVAC, plumbing, restoration, remodeling, pools, general contracting
- Captures: business name, phone, address, website URL (if exists), Google rating, review count, GBP verification status
- Targets mobile numbers specifically (business owner's direct line — bypasses front desk)
- Runs across multiple sub-areas of San Diego to overcome Google's per-search caps

**Outputs**: `raw-leads.json` — structured list of all scraped businesses

**Territory**: `raw-leads.json` only

**Messages**: When batch complete, sends count and niche breakdown to Agent 2

---

### Agent 2 — The Qualifier

**Role**: Filter raw leads against Scale SD's ICP and assign a fit score.

**What it does**:
Applies the following qualification criteria, each worth points on a 0–10 fit score:

| Criterion | Points | Rationale |
|-----------|--------|-----------|
| Has a mobile number | Required (filter, not scored) | Must be owner's direct line |
| In target niche | +2 | Roofing, HVAC, plumbing, restoration, pools, remodeling, GC |
| Has 10+ Google reviews | +2 | Established business, not a ghost |
| Rating between 3.5–4.5 | +2 | Pain point: not perfect, but cares about reputation |
| Has a website | +1 | Already invested in marketing; easier sell |
| No active paid ads visible | +2 | Untapped paid channel = opportunity |
| GBP not fully optimized | +1 | Explicit gap Scale SD can fix |

Leads scoring 6+ move to Agent 3 for enrichment. Leads scoring 3–5 are batched for lower-priority outreach. Leads below 3 are discarded.

If high-fit leads are insufficient (<30 in a batch), communicates back to Agent 1 for additional niche/geo targeting.

**Outputs**: `qualified-leads.json` — scored leads with qualification reasoning

**Territory**: `qualified-leads.json` only

**Messages**: Sends top-scored leads to Agent 3 for enrichment

---

### Agent 3 — The Intelligence Enricher

**Role**: For every qualified lead, build a dossier that makes Daniel's call feel tailored and informed.

**What it does**:
- Checks the business's social media presence (active? dormant? what platforms?)
- Reviews recency — when did they last get a Google review? Are they responding to reviews?
- Looks for obvious automation gaps: does their GBP have the "text us" feature? Auto-replies? Booking link?
- Checks if they appear in any ad libraries (Meta Ad Library, Google Ads search)
- Identifies their best-performing content angle (based on what exists publicly)
- Writes a 2–3 sentence "conversation hook" for Daniel — the specific pain point to open with

**Pain point score (0–10)**:

| Signal | Points |
|--------|--------|
| No social media or dormant (6+ months inactive) | +3 |
| Unanswered negative reviews | +2 |
| No website or outdated website (pre-2022) | +2 |
| No booking or contact form | +1 |
| No visible paid ads | +2 |

Combined fit score (Agent 2) + pain point score (Agent 3) = **priority score out of 20**.

**Outputs**: `lead-intelligence.json` — enriched profiles with conversation hooks

**Territory**: `lead-intelligence.json` only

**Messages**: Sends completed enrichment profiles to Agent 4

---

### Agent 4 — QA + Priority Ranker

**Role**: Quality gate and final deliverable producer.

**What it does**:
- Reviews all enrichment profiles from Agent 3 for completeness and accuracy
- Flags any leads where data seems thin or contradictory — sends back to Agent 3 for re-enrichment if needed
- Sorts all leads by final priority score (highest first)
- Writes Daniel's **Daily Call Brief** — a short, scannable doc he opens each morning
- Produces a GHL-ready import CSV for the power dialer

**Daily Call Brief format** (per lead):
```
#1 — [Business Name] | [Niche] | Score: 18/20
Phone: [mobile number]
Hook: "I was looking at your Google profile — noticed you've got 47 reviews 
       but no way for people to book on your listing. With HVAC heading into 
       summer, you're probably missing 3-4 calls a day from that alone."
Quick facts: 4.2★, 47 reviews, no social media in 8 months, no ads running
```

**Outputs**:
- `priority-call-list.md` — Daniel's daily brief, sorted by score
- `ghl-import.csv` — ready to drag into GoHighLevel contacts

**Territory**: `priority-call-list.md` and `ghl-import.csv`

**Messages**: Sends back to Agent 3 if profiles are incomplete; signals main session when final deliverables are ready

---

## Implementation Plan

### Phase 1 — Set Up (Week 1)

**Step 1: Enable agent teams in your Claude Code project**
In `.claude/settings.local.json`:
```json
{
  "experimental": {
    "agentTeams": true
  }
}
```

**Step 2: Create project folder structure**
```
lead-pipeline/
├── .claude/
│   └── settings.local.json
├── docs/
│   └── agent-teams-reference.md    ← paste Claude agent teams docs here
├── prompts/
│   └── lead-pipeline-prompt.md     ← the master prompt (see below)
├── outputs/
│   ├── raw-leads.json
│   ├── qualified-leads.json
│   ├── lead-intelligence.json
│   ├── priority-call-list.md
│   └── ghl-import.csv
└── CLAUDE.md                       ← project context for agents
```

**Step 3: Write `lead-pipeline/CLAUDE.md`**
Give the agents full context on Scale SD's ICP, target niches, qualification criteria, and what a good lead looks like for Daniel. This is what the agents read when they wake up.

**Step 4: Pre-approve tools to prevent interruptions**
In settings, pre-approve: web search, file read/write, bash (for CSV generation).

---

### Phase 2 — Run and Calibrate (Weeks 2–3)

- Run the agent team on one niche (e.g., HVAC in San Diego) as a test batch
- Compare the output priority list against leads Daniel has previously called
- Adjust scoring weights based on what Daniel says about lead quality
- Calibrate the conversation hooks — does the framing land? Does Daniel use them?

---

### Phase 3 — Full Daily Operation (Week 4+)

Daily workflow:
1. Ashen or Tad (or eventually the Scraper agent automatically) drops target niches/geos into the input
2. Agent team runs overnight or first thing in the morning
3. Daniel opens `priority-call-list.md` at 11am — top 20 leads, briefed and ready
4. GHL import CSV loaded into power dialer
5. Call window: work top-to-bottom, already sorted by conversion likelihood

Weekly: Agent 3 reviews which conversation hooks led to booked calls → feed back into hook refinement.

---

### Phase 4 — Connect to Lead Warming System (Month 2)

Once the calling pipeline is optimized, connect outputs to the [[Lead Warming System]]:
- Leads who don't answer calls get added to the 6-channel warming sequence
- Leads who engage on social (the warmth tracker picks this up) get re-surfaced in the priority list with an updated score
- Warm leads who then show up in a new scrape get auto-elevated to the top of the call list

This closes the loop: scrape → qualify → enrich → call → warm → re-surface.

---

## Roles and Ownership

| Task | Owner |
|------|-------|
| Run agent team daily / provide niche inputs | Ashen or Tad |
| Review and calibrate priority scores | Ashen |
| Work the call list | Daniel |
| Refine conversation hooks based on call outcomes | Daniel + Justin |
| Maintain agent team prompt and scoring weights | Ashen + Justin |
| Connect outputs to Lead Warming System | Justin |

---

## Cost and Token Considerations

Following the [[Claude Agent Teams]] guidelines:
- Use **Sonnet** for Agents 1–3 (cost-effective for structured tasks)
- Use **Sonnet** for Agent 4 QA as well — Opus only if hook quality needs upgrading
- 4 agents × daily run = roughly 4× single-session cost
- Offset: Daniel saves 30–40% of his calling window by not dialing unqualified leads

At scale, the agent team's cost should be measured against Daniel's time value, not API cost alone.

---

## Key Success Metrics

| Metric | Baseline | Target |
|--------|----------|--------|
| Qualified leads/week | 150 (manual) | 300+ (agent-assisted) |
| Time spent qualifying | ~5 hrs/week (Ashen+Tad) | <1 hr/week (review only) |
| Daniel's call-to-booked-call rate | Unknown | Track and improve 10%/month |
| Cost per booked call | Unknown | Establish baseline in Week 2 |
| Avg priority score of booked calls vs no-shows | — | Use to recalibrate scoring |

---

## Example Agent Team Prompt

See [[Scale SD Lead Pipeline — Example Agent Prompt]] for the full ready-to-use prompt.

---

## Related Pages

- [[Lead Warming System]]
- [[Lead Generation and Qualification System]]
- [[Setter-Closer Sales Model]]
- [[Claude Agent Teams]]
- [[GoHighLevel]]
- [[Daniel J Loarca]]
- [[Ashen]]
- [[Tad]]
- [[Justin]]
