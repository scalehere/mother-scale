---
title: "Lead Warming System"
type: concept
tags: [leads, automation, outreach, scoring, retargeting, multi-channel]
sources: [lead-warming-system]
updated: 2026-04-12
---

A structured multi-channel lead nurturing system that tracks prospect engagement across six platforms, assigns a numerical warmth score, and triggers tiered outreach actions based on that score. The goal is to move cold prospects to a state of readiness for text or direct sales contact — without burning them with premature hard outreach.

## How It Works

Leads are entered into Google Sheets and tracked by a Python script across six channels:

1. **Instagram** — engagement, story views, profile visits
2. **Facebook** — engagement, page interactions
3. **LinkedIn** — connection and message engagement
4. **Email** — opens, clicks, replies
5. **GoHighLevel (LVL 2)** — CRM-tracked interactions
6. **Text** — response tracking (used only once warmed)

The script monitors responses, engagement signals, and profile views, then assigns a **warmth score out of 10**.

## Warmth Score Tiers

| Score | Status | Action |
|-------|--------|--------|
| 0–3 | Cold | Organic outreach only (comments, story replies) |
| 4–6 | Warming | Add to retargeting audience; continue multi-channel touches |
| 7–9 | Warm | Retargeting ads active; email sequences intensified |
| 10 | Hot | Text outreach triggered — once every two weeks |

## Outreach Priority Order

1. Comments on the lead's own content
2. Emails
3. Story replies
4. Retargeting ads

Text is the final and most direct step, used sparingly to avoid contact fatigue.

## Organic → Paid Integration

Warm leads feed into a **retargeting audience** for platform-specific paid ads. Organic engagement thus directly informs paid targeting — the two systems are linked, not siloed. High-performing organic content can also become ad creative (see [[AI Ad Pipeline]]).

## Related Concepts

- [[AI Ad Pipeline]]
- [[Contractor Automation System]]
- [[Client Pipeline (Lead to Fulfillment)]]
- [[Setter-Closer Sales Model]]
