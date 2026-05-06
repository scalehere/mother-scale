---
title: "Autonomous Improvement Loop"
type: concept
tags: [automation, ai, optimization, autoresearch, iteration, lead-gen]
sources: [how-to-build-claude-agent-teams]
updated: 2026-04-13
---

# Autonomous Improvement Loop

A self-modifying agent loop that tests changes against a fixed metric, keeps what improves results, and reverts what doesn't. Adapted from Andrej Karpathy's `autoresearch` project (stored at `agent-teams/AutoResearch/`) for Scale SD's lead qualification and outreach system.

The core insight from AutoResearch: instead of a human researcher iterating on a model, the agent iterates. You define the mutable files (what can change), the fixed infrastructure (what stays the same), and the metric (what determines success). The agent does the rest — continuously, overnight, without asking permission.

---

## The AutoResearch Pattern

In Karpathy's original:
- **Mutable file:** `train.py` — the model architecture and optimizer
- **Fixed infrastructure:** `prepare.py` — evaluation harness, data loading, constants
- **Metric:** `val_bpb` — validation bits per byte (lower = better)
- **Budget:** 5 minutes of training per experiment
- **Loop:** Modify → train → measure → keep if better, discard if not → repeat forever

The agent runs ~12 experiments per hour. You wake up to 100 experiments worth of results with a measurably better model.

---

## Scale SD's Adaptation

For the lead generation system:
- **Mutable files:** `criteria/qualification_rubric.md` + `criteria/sms_templates.md`
- **Fixed infrastructure:** the LeadOps agent team structure, GHL pipeline, setter-closer process
- **Metric:** `hot_close_rate` — percentage of Hot-tier leads that convert to signed clients
- **Budget:** one batch cycle (~150 leads)
- **Frequency:** monthly (driven by data accumulation, not a timer)

---

## The Loop in Detail

### What Gets Tracked

`tracking/results.tsv` — one row per batch:
```
batch_date    hot_leads    hot_reply_rate    hot_booking_rate    hot_close_rate    notes
```

After 4 weeks (4+ batches), there's enough signal to identify what's working.

### What the Improvement Team Analyzes

The Improvement Loop runs a 4-agent team called `ImprovementLoop`:

**Agent 1 — Data Analyst**
Reads all batch data and qa_reports. Identifies:
- Which niches have highest close rates?
- Which tiers are underperforming (HOT leads not converting as expected)?
- Which message variants (tracked via GHL reply tags) are getting the most replies?
- Any patterns in disqualified leads that are actually converting? (May indicate the rubric is too aggressive)

**Agent 2 — Rubric Optimizer**
Proposes specific changes to `qualification_rubric.md`. Each proposal must be:
- Specific (not "improve the scoring" — but "reduce the website score threshold for HOT from ≤4 to ≤6 because restoration contractors with basic websites are converting at 40%")
- Falsifiable (measurable in the next batch)

**Agent 3 — Copy Optimizer**
Proposes specific changes to `sms_templates.md`. Each proposal must include:
- Current template
- Proposed revision
- Why it should improve reply rate (based on what Data Analyst found)

**Agent 4 — Devil's Advocate**
Challenges every proposal from Agents 2 and 3. For each:
- What assumption does this rely on?
- What alternative explanation exists for the data?
- What could go wrong if we make this change?
Agents 2 and 3 must revise proposals that don't survive challenge.

### The Keep/Discard Rule (AutoResearch Rule)

After applying changes and running the next batch:
- If `hot_close_rate` improved → commit changes (update CLAUDE.md, commit to git)
- If `hot_close_rate` same or worse → revert to previous rubric/templates, log "discard" in results.tsv
- A **simplicity preference** applies (from AutoResearch): if a change achieves the same close rate but with a simpler rubric, keep the simpler version. Complexity is a cost.

---

## Why This Compounds

Most outbound systems plateau or degrade over time. Lists get exhausted, messages get stale, the team gets tired. The Improvement Loop inverts this:

- Month 1: Baseline system. Rubric is educated guesses.
- Month 2: First improvement cycle. Data shows restoration contractors convert better than landscapers at the same score. Rubric adjusts.
- Month 3: Second cycle. Data shows Message 3 with a GMB-specific observation gets 2× reply rate vs. generic version. Copy updates.
- Month 6: The system is no longer using educated guesses. It's using 6 months of real conversion data to define what "HOT" means and what messages work for San Diego contractors specifically.

This is the difference between a static outreach system and a learning one.

---

## Implementation Trigger

Run the Improvement Loop when:
- `results.tsv` has 4+ batch rows (enough signal)
- A new month starts
- Close rate drops noticeably (diagnostic run)
- Ashen or Tad notice a new pattern in the scraping data (new niche, new geography)

Do not run it more than once per month — the batch cycle is the budget constraint. More frequent iterations don't produce better signal, they just produce noisier data.

---

## Related Concepts

- [[Claude Agent Teams]] — the multi-agent framework this loop uses
- [[Scale SD AI Growth System]] — the full stack this loop improves
- [[Lead Intelligence Agent Team Plan]] — the LeadOps system that generates the data
- [[Playwright MCP]] — browser tool used by Lead Qualifier (produces the data this loop analyzes)
