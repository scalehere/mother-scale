---
title: "AI Ad Pipeline"
type: concept
tags: [ai, ads, video, automation, production, optimization]
sources: [lead-warming-system]
updated: 2026-04-12
---

A 3-stage AI-powered video ad creation loop designed to minimize cost-per-lead by grounding ad production in actual performance data rather than guesswork. The master objective of the entire pipeline: *"How do we get this ad to have the lowest cost per lead possible?"*

## The 3 Stages

### Stage 1 — Script & Shot Ideas

- **Inputs**: Client identity, desired customer profile, target geographic area, recent ad performance data
- **Output**: Video scripts and shot ideas/editing style formats calibrated to what has actually performed well
- The model draws on a library of organic and paid ad performance data — not generic creative instinct

### Stage 2 — Shot Outline

- **Inputs**: Human review and selection from Stage 1 suggestions (iterative back-and-forth with model)
- **Output**: A JSON object containing a shot outline with media URLs and text timestamps; model validates whether the final assembled script is likely to work before any footage is shot
- The JSON format enables downstream automation — the outline can feed directly into editing tools

### Stage 3 — Edited Ad

- **Inputs**: Raw footage captured following the Stage 2 shot outline
- **Output**: Finished edited ad with:
  - Auto-transcription converted to captions
  - Timing and pacing optimization
  - Multiple editing style variants tested
- The model also generates shot templates and specifies exactly what footage is needed during this stage

## Why This Matters

Traditional ad production is iterative and expensive: shoot → edit → run → measure → guess at improvements. The AI pipeline front-loads the intelligence: measure first (Stage 1), plan precisely (Stage 2), then shoot and edit with high confidence (Stage 3). The result should be a lower cost-per-lead and faster creative iteration.

## Data Requirements

The pipeline is only as good as its training data. Required inputs:
- **Paid ad performance data** (internal) — owned by [[Ashen]]
- **Organic metrics (external)** — wide-variety ad and video performance data, owned by [[Tad]]
- **Organic metrics (internal)** — what converts from Scale SD's own organic content, owned by [[Justin]]

Initial data collection targets two industries: pools (Tony's business) and marketing agencies (Scale SD itself).

## Related Concepts

- [[Lead Warming System]]
- [[Revenue Partner Positioning]]
- [[Contractor Automation System]]
