---
title: "The Meta Ads Campaign Deployment Guide"
type: source
tags: [meta-api, automation, claude-code, campaign-deployment, agency-tools, utm, targeting, supabase]
sources: [meta-ads-campaign-skill-freebie]
author: Kyle Whitrow (nustimulus.com)
published:
updated: 2026-04-12
---

# The Meta Ads Campaign Deployment Guide

## Abstract

A 20-page technical guide by Kyle Whitrow for building a Claude Code skill (`/meta-ads-campaign`) that automates full Meta ad campaign deployment via the Marketing API — bypassing the 45-minute manual Ads Manager process. Campaigns always deploy PAUSED for human review before activation. The system is client-agnostic and designed for agency scale: adding a new client is a single database row + ad account mapping.

## Key Claims

- The typical manual campaign launch takes ~45 minutes of repetitive clicking; this pipeline eliminates that entirely
- Campaigns deploy **PAUSED** — human review always required before activation
- **System user tokens don't expire** (vs. personal tokens that expire in 60 days) — use system users for agency automation
- **Resume support**: if a deploy fails mid-way, re-running picks up where it left off — already-uploaded videos are skipped
- **Advantage+ audience is always enabled** on every ad set (Meta expands beyond seed audience)
- **CBO (Campaign Budget Optimization)** is the default — budget set at campaign level, API expects value in cents
- **Pixel auto-discovery**: pipeline finds the active Meta Pixel on the ad account and attaches it automatically
- **Multi-format creatives**: vertical (1080×1920), feed (1080×1080), landscape (1920×1080) — Meta serves best format per placement
- Getting the **region key wrong** is the #1 deployment mistake — always validate via API, never guess
- Country + region conflict: setting both `countries: ["CA"]` and a `regions` key targets all of Canada — use one or the other

## The 6-Phase Pipeline

1. **Gather Context** — pull client from DB by slug, find Meta ad account mapping, ask user for: objective, geo/age targeting, daily budget, landing page URL, funnel structure, video assets. Read `META_ACCESS_TOKEN` from `.env`
2. **Create Campaign Record** — insert draft campaign row to DB; register video assets with file paths + format labels; group multi-format assets
3. **Generate Ad Copy** — generate primary text, headline (25 char limit), description, CTA type per video; present for user review; allow rewrites before saving
4. **Generate UTMs** — build UTM URLs per ad; bake into creative link (do not use `url_tags`)
5. **Pre-Deploy Checklist** — 10-point verification: video files exist, copy approved, UTMs clean, geo validated, pixel connected, Instagram actor connected, budget confirmed, landing page live, ad account active, Page ID valid
6. **Deploy to Meta** — upload videos, create campaign (PAUSED), ad set with Advantage+, ads with pixel; log every API call; return Ads Manager URL

## Setup Requirements

- Claude Code (VS Code extension or CLI)
- Meta Developer Account → Business App → Marketing API enabled
- **System User** (not personal user) with role: Admin
- Permissions: `ads_management`, `ads_read`, `pages_read_engagement`, `pages_manage_ads`
- Token stored in `.env` as `META_ACCESS_TOKEN`
- Ad account ID (`act_123456789`) and Facebook Page ID
- Supabase DB with: `clients` table, `ad_account_mappings` table, `video_ad_units` table, `ad_deploy_log` table, `ad_campaigns` table

## UTM Conventions

**Campaign slug format:** `{client-slug}-{month}-{year}-{objective}`
- Example: `acme-roofing-march-2026-leads`
- Rules: lowercase, hyphen-separated; no internal tool names; no redundant date suffixes

**Content tag format:** `v{version}-{funnel_stage}-{descriptive-slug}`
- `v1-tof-rate-hikes-news` (top of funnel)
- `v1-mof-customer-testimonial` (mid funnel)
- `v1-bof-free-quote-offer` (bottom of funnel)

**Full URL:** `{landing_page}?utm_source=meta&utm_medium=paid_social&utm_campaign={slug}&utm_content={content}`

## Notable Quotes

> "The pipeline never loses work. If a deploy fails halfway, re-running picks up where it left off."

> "Scale to multiple clients. The skill is client-agnostic. Adding another client is just a database row and an ad account mapping."

## Connections

- [[concepts/meta-api-automation]] — this guide is the primary source for this concept
- [[concepts/campaign-setup-settings]] — the manual settings this pipeline automates
- [[concepts/campaign-metrics]] — UTM structure connects to attribution tracking
- [[concepts/creative-testing-strategy]] — multi-format creatives serve best format per placement
- [[entities/kyle-whitrow]] — author

## Open Questions

- Does the skill handle lead form creation, or only link-click / instant form ads?
- How does it handle Special Ad Categories (housing, employment) — any guardrails?
- Does the Supabase schema need to be set up from scratch or is it part of an existing project template?
