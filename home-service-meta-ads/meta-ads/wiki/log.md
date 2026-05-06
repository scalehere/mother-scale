# Wiki Log

Append-only. Newest entries at the bottom.
Parse with: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-11] init | Wiki initialized
- Created directory structure: wiki/, raw/, raw/assets/
- Created schema: CLAUDE.md
- Created: wiki/index.md, wiki/log.md, wiki/overview.md
- Pages created: 3, pages updated: 0
- Domain: not yet defined — awaiting first ingest

## [2026-04-11] ingest | Do Facebook Ads Work for Home Service Companies?
- Source: raw/Do Facebook Ads Work for Home Service Companies?.md
- Author: Matt Watson | Publisher: WatsonCo Marketing
- Pages created: 7 (source page, 2 entity pages, 5 concept pages)
- Pages updated: 3 (overview, index, log)
- Key additions: CPL benchmarks by vertical, Google-first budget rule, Facebook ad format rankings, lead response time data
- Domain established: home services digital marketing / paid advertising strategy

## [2026-04-11] ingest | 7 sources (batch ingest)
- Sources: Dimsey 2025, Claeys 2026, Hunsaker ×3 (Dec 2025 / Mar 2026 ×2), Jonas Olson 2026, meta-ads-campaign-skill-freebie
- Domain updated: agency running Facebook ads for home service businesses (HVAC, plumbing, pools, solar, remodeling, etc.)
- Pages created: 7 source pages, 5 entity pages, 7 new concept pages
- Pages updated: 2 existing concept pages (facebook-ads-home-services, cost-per-lead), overview, index, log
- Total pages touched: ~24
- Key additions: owner intro video template, 3-creative-type framework, 7-step ad copy formula, full Ads Manager settings reference, lead form friction strategy, CPL→CPA→CAC math, creative testing structure, Meta API automation concept

## [2026-04-12] delete | meta-ads-campaign-skill-freebie (incomplete)
- Deleted: raw/meta-ads-campaign-skill-freebie.pdf.md (only 3 of 20 pages captured)
- Deleted: wiki/sources/meta-ads-campaign-skill-freebie.md
- Updated: wiki/index.md (sources 8→7, pages 31→29)
- Pending: full re-ingest when complete PDF is available

## [2026-04-12] ingest | The Meta Ads Campaign Deployment Guide (full 20 pages)
- Source: raw/meta-ads-campaign-skill-freebie.pdf (Kyle Whitrow, nustimulus.com)
- Pages created: 2 (source page, kyle-whitrow entity)
- Pages updated: 2 (meta-api-automation concept fully rewritten with complete pipeline details, index)
- Key additions: full 6-phase pipeline spec, system user token setup, resume support, Advantage+ always-on, CBO defaults, pixel auto-discovery, multi-format creative logic, geo targeting validation rules, UTM conventions, Supabase DB schema requirements, post-deploy verification queries, troubleshooting guide
