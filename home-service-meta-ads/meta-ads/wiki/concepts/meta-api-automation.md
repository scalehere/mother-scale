---
title: "Meta API Automation for Agency Campaign Deployment"
type: concept
tags: [meta-api, automation, claude-code, agency-tools, campaign-deployment, utm, supabase]
sources: [meta-ads-campaign-skill-freebie]
updated: 2026-04-12
---

# Meta API Automation for Agency Campaign Deployment

Using the Meta Marketing API + Claude Code to automate campaign deployment — bypassing the manual 45-minute Ads Manager process. Client-agnostic and designed for agency scale.

---

## The Problem It Solves

Every new campaign requires ~45 minutes in Meta Ads Manager per client: video upload, campaign structure, targeting, pixel, UTMs. At agency scale (10+ clients), this is hours per week of repetitive work.

---

## The Solution: `/meta-ads-campaign` Skill

A 6-phase pipeline run from the terminal:

1. **Gather Context** — client lookup from DB, ad account mapping, ask for targeting/budget/assets
2. **Create Campaign Record** — draft campaign + video assets saved to DB
3. **Generate Ad Copy** — primary text, headline (25 char limit), CTA per video; human review before save
4. **Generate UTMs** — baked into creative link; never use `url_tags`
5. **Pre-Deploy Checklist** — 10-point verification; requires explicit approval
6. **Deploy to Meta** — upload videos, create campaign (PAUSED), ad set, ads via API; return Ads Manager URL

---

## Key Technical Rules

- **Always deploys PAUSED** — activate manually in Ads Manager after review
- **System user tokens** — don't expire; personal tokens expire in 60 days; always use system users
- **Resume support** — re-running a failed deploy skips already-uploaded videos; no re-uploading gigabytes
- **Advantage+ audience always on** — `targeting_automation: { advantage_audience: 1 }` on every ad set
- **CBO default** — budget at campaign level; API value in cents; pipeline converts automatically
- **Pixel auto-discovery** — pipeline finds active pixel on ad account; attaches automatically; deploy continues (with warning) if no pixel found
- **Multi-format creatives** — vertical 1080×1920, feed 1080×1080, landscape 1920×1080; Meta serves best per placement; falls back to single-video if multi-format fails

---

## Geographic Targeting Gotcha

Getting region keys wrong is the #1 deployment mistake.

- Always validate via API before deploying:
  `GET /search?type=adgeolocation&location_types=region&q={name}&access_token={token}`
- Verify: key matches, country_code is correct, name is right region
- **Never set both `countries` and `regions`** — Meta targets all of country; use one or the other
- Example pitfall: key `3901` looks Canadian but targets Uruguay

---

## UTM Convention

**Campaign:** `{client-slug}-{month}-{year}-{objective}` (e.g., `acme-roofing-march-2026-leads`)
**Content:** `v{version}-{funnel_stage}-{slug}` (e.g., `v1-tof-rate-hikes-news`)
- Lowercase, hyphen-separated; no internal tool names; no redundant date suffixes

---

## Database Requirements (Supabase)

Tables: `clients`, `ad_account_mappings`, `video_ad_units`, `ad_campaigns`, `ad_deploy_log`
- Each client needs a row in `clients` + a row in `ad_account_mappings` (platform: `meta_ads`, is_active: true)
- All API calls logged to `ad_deploy_log` — complete audit trail per campaign

---

## Agency Scalability

Adding a new client = one DB row + one ad account mapping. Same pipeline handles all clients, all verticals. The skill is templatable by vertical (HVAC, roofing, solar, etc.).

---

## Post-Deploy Checks

1. Query `video_ad_units` — all rows should have `meta_ad_id`, `meta_campaign_id`, `meta_adset_id` populated
2. Query `ad_deploy_log` — look for `status = 'failed'`
3. Verify pixel via API: `GET /{adset_id}?fields=promoted_object`
4. Verify targeting via API: `GET /{adset_id}?fields=targeting`

---

## Sources

- [[sources/meta-ads-campaign-skill-freebie]] — primary source; full 20-page technical guide
