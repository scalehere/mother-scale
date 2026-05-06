# Social Organic — Sub-OS for Scale SD

> Scoped operating manual for the social organic management vertical. The root `../CLAUDE.md` is canonical for identity, voice, and constitution. This file is read AFTER the root, when work is scoped to social organic.

## Why this sub-OS exists

All 4 active Scale SD clients pay for organic social management. Per Q7 (May 2026), this is the recurring fulfillment work that eats the most time and caps client capacity. This sub-OS turns the existing manual SOPs into executable skills so the agency can serve more clients without losing per-client brand integrity.

## Scope

**In scope:** organic content planning, scripting, captioning, scheduling, engagement monitoring, and reporting across Instagram, Facebook, TikTok, YouTube, and Google Business Profile. Per-client.

**Out of scope:** paid ads (eventual `paid-ads-os/`), website builds (eventual `web-os/`), GHL automation snapshots (eventual `crm-snapshot-os/`).

## The grounding SOPs (already ingested in the wiki)

These are the manual processes the skills here automate. **Read these first.**

- `../../scale-business/wiki/sources/social-media-content-optimization.md` — the 5 Content Pillars, the Month-1 Strategy Session template, the 20-item shot-list framework, the 2.5-hour shoot day schedule, equipment checklist.
- `../../scale-business/wiki/sources/social-media-strategy-for-sales.md` — 100 contractor-specific content hooks across 8 thematic buckets.

## The 5 Content Pillars (from the wiki SOP)

Every post a client publishes maps to one of these. Monthly mix targets:

| Pillar | Theme | Monthly % | Posts |
|---|---|---|---|
| 1 — The Work | Before/after, in-progress, finished installs | 35% | 4–6 |
| 2 — The Team | Owner/crew photos, behind-the-scenes | 20% | 2–3 |
| 3 — Education | Tips, how-to, warning signs, seasonal advice | 20% | 2–3 |
| 4 — Social Proof | Reviews, testimonials, milestones | 15% | 2 |
| 5 — Local Presence | San Diego community, neighborhood callouts | 10% | 1–2 |
| Bonus — Offer/CTA | Promotions, free estimates | Max 1/mo | 1 |

12–16 posts/month total = ~3–4 posts/week. Plus 7 Reels/month (Growth/Scale tier).

## The skill ladder (planned)

Build one per week via root `/level-up`. Each skill is also packageable as a productized client snapshot once stable.

| # | Skill | What it does | Reads from | Outputs to |
|---|---|---|---|---|
| 1 | `client-strategy-session` | Runs the Month-1 intake — captures voice, pillars, audience, platforms, competitors, offers, shot wishlist | client conversation + existing posts | `clients/{slug}/` config files |
| 2 | `brand-voice-profile` | Extracts a client's voice from existing posts/captions into a config doc | past posts (raw or scraped) | `clients/{slug}/brand-voice.md` |
| 3 | `monthly-content-plan` | Generate next month's full calendar mapped to the 5 pillars | client config + last month's performance | `clients/{slug}/monthly-plans/{YYYY-MM}.md` |
| 4 | `shot-list` | 20-item shot list for the next monthly shoot, 1 week before | monthly plan | `clients/{slug}/monthly-plans/{YYYY-MM}-shotlist.md` |
| 5 | `caption-writer` | Per-post platform-specific captions in client voice | brand-voice + post topic | drafted posts in `clients/{slug}/scheduling/` |
| 6 | `reel-script` | 30–60s Reel script in client voice from a content-pillar topic | brand-voice + pillar topic | drafted reel script |
| 7 | `post-scheduler` | Loads approved posts into the scheduling tool of record | drafted posts after Ashen approval | scheduler API |
| 8 | `weekly-engagement-digest` | Pulls comments/DMs/mentions across platforms for triage | platform APIs | Slack digest or markdown report |
| 9 | `monthly-client-report` | Performance + insights + next-month preview for the client meeting | platform APIs + monthly plan | `clients/{slug}/reports/{YYYY-MM}.md` |

## Per-client folder schema

Each client gets a folder under `clients/{client-slug}/` with these files:

```
clients/{slug}/
├── brand-voice.md          ← voice profile (registers, tells, anti-patterns)
├── content-pillars.md      ← the 5 pillars tailored for this client + example post types
├── platform-config.md      ← platforms, posting cadence, posting times, platform-specific notes
├── audience.md             ← target homeowner profile (neighborhoods, age, income, pain points)
├── competitors.md          ← 2-3 local competitor accounts to watch
├── offers-and-ctas.md      ← current offer, CTA library
├── shot-wishlist.md        ← signature jobs, equipment, team members worth featuring
├── hashtag-bank.md         ← clusters by topic
├── assets/                 ← logos, brand colors (hex), fonts, font files
├── monthly-plans/
│   ├── 2026-06.md
│   ├── 2026-06-shotlist.md
│   └── ...
├── scheduling/             ← drafted posts awaiting Ashen/client approval
└── reports/
    ├── 2026-06.md
    └── ...
```

The `clients/{slug}/` folder name should match the slug used in `../../scale-business/wiki/entities/{slug}.md`.

## Reading order at session start

When working on social-os tasks, read in this order:

1. Root `../CLAUDE.md` (parent — identity, voice, constitution, priorities)
2. This file (sub-OS scope, pillars, skill ladder, schema)
3. `../../scale-business/wiki/entities/{client-slug}.md` (current client knowledge)
4. `clients/{client-slug}/*` (current client config + recent plans/reports)
5. The relevant skill SOP from the wiki (`social-media-content-optimization.md` or similar)

## Voice on social posts

**Per-client. Not Ashen's.** Each client has their own `brand-voice.md`. Never use Ashen's voice from the root `references/voice.md` for client posts. The agency's voice is for internal docs, agency-owned content (`@scalenowsd`), and Ashen's personal LinkedIn/IG (`@ashenafew`) only.

When drafting client content, classify the audience: client's homeowners, not Ashen's network. Different tone, different vocabulary, different stakes.

## Approval workflow

Bike-Method Phase 1 by default: every drafted post goes through Ashen review before publication. As skills mature and a client's voice profile validates well over a few months, a specific skill (e.g. `weekly-engagement-digest` for low-stakes auto-replies) can move to Phase 2/3. Phase changes are logged in `decisions/log.md`.

## Cross-references

- Root: `../CLAUDE.md`, `../references/voice.md` (Ashen's voice — internal only), `../decisions/log.md`
- Wiki: `../../scale-business/wiki/entities/{slug}.md`, `../../scale-business/wiki/sources/social-media-content-optimization.md`, `../../scale-business/wiki/sources/social-media-strategy-for-sales.md`
- GHL: live MCP, used by `post-scheduler` if GHL's social planner becomes the system of record
