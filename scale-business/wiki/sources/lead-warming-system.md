---
title: "Lead Warming System"
type: source
tags: [leads, automation, ai, ads, outreach, retargeting]
sources: [lead-warming-system]
updated: 2026-04-12
---

A planning document outlining Scale SD's lead warming infrastructure and AI-powered ad production pipeline. The document combines two distinct systems: a multi-channel lead nurturing tracker and a 3-stage AI video ad creation loop.

## Lead Warming System

Leads are added to Google Sheets and tracked by a Python script across six channels: Instagram, Facebook, LinkedIn, Email, GoHighLevel (LVL 2), and Text. The script monitors responses, engagement, and email/profile views, and assigns each lead a **warmth score out of 10**.

Warm leads are added to a **retargeting audience** for platform-specific paid ads.

Primary outreach tactics (in priority order):
- Comments on leads' content
- Emails
- Story replies
- Retargeting ads

Once a lead is sufficiently warmed, text outreach begins — **once every two weeks**.

## AI Ad Production Pipeline

A 3-stage loop designed to minimize cost-per-lead on video ads. The master goal: *"How do we get this ad to have the lowest cost per lead possible?"*

**Stage 1 — Script & Shot Ideas**
- Input: Client + desired customer + target area
- Output: Video scripts and shot ideas/editing style formats based on recent ad performance data

**Stage 2 — Shot Outline**
- Input: Choosing the right ad (user iterates with model on suggestions)
- Output: JSON object — shot outline with media URLs and text timestamps; model validates whether the final script will likely work

**Stage 3 — Edited Ad**
- Input: Raw footage
- Output: Edited ad (transcriptions to captions, timing/pacing optimization, multiple editing style tests)

MODEL also creates shot templates and lays out exact footage needed during Stage 3.

## Team Data Assignments

| Role | Owner | Responsibility |
|------|-------|---------------|
| Organic Metrics (External) | Tad | Wide-variety data on video content and ads — what patterns are working |
| Paid Ads Analytics (Internal) | Ashen | Which internal ads perform better and by what criteria |
| Organic Metrics (Internal) | Justin / Daniel | What converts from organic — hooks, value props, scripts, tone by industry |
| Software / AI Training | Justin / Ashen / Tad | Data collection, model training, application logic |

Initial data collection target: two industries — **Tony (pools)** and **marketing agencies like Scale SD**.

## Key Claims

- Lead warmth score (0–10) enables tiered outreach frequency and retargeting precision
- The AI pipeline reduces guesswork on ad creation by grounding outputs in performance data
- Content posted organically can feed into ad creative selection — organic and paid are linked systems
- Need proprietary-free organic data and an ad library to train the model effectively

## Entities Mentioned

- [[Scale SD / ScaleHere]]
- [[Daniel J Loarca]]
- [[Ashen]]
- [[Tad]]
- [[Justin]]
- [[GoHighLevel]]
