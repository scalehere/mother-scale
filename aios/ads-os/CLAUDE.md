# ads-os — Scale SD Meta Ads sub-OS

> Self-promotional Meta + TikTok ads for Scale SD. Owns the full lifecycle: strategy lock, competitor mining, script generation, shoot, launch, monitor, iterate, lead handling.
> Started: 2026-05-05 | Sub-OS to: `aios/`

## What this sub-OS owns

Running paid acquisition for the agency itself. Not for clients. (Client paid ads live elsewhere.)

## North-star numbers (locked 2026-05-05 call)

- Budget: $1,000 / month → $50 / day
- Split: ~50% Meta (English-led) / ~50% TikTok (Spanish-led)
- Launch creative count: 4-6 ads
- Funnel A: lead form (volume play)
- Funnel B: video landing page, Velocity-style (quality play)
- Ad accounts: one Peter BM, one Ashen BM (need to remove window-guy slot first)
- Goal: bookings into Dani's calendar with $200k+ revenue contractor leads

## Folder map

| Path | What's there |
|---|---|
| `strategy.md` | LOCKED audience, offer, differentiator, pain, CTAs, voice |
| `voice.md` | Ad-writing voice spec. Loaded BEFORE every script. Eddie pattern. |
| `product.md` | Exact offer + verified proof points. Loaded BEFORE every script. |
| `icp.md` | 7 ICPs with verbatim pain language per trade. The script multiplier. |
| `writing-rules.md` | Anti-AI-slop filter. Banned words + 5-pass quality check. |
| `scripts.md` | Script library. The 7 hand-written scripts + hook bank. Source of truth for hand-crafted copy. |
| `competitors.md` | Spark Marketing, Velocity Marketing, Manus mining workflow |
| `research/` | Manus AI prompts, ad-library snapshots, verbatim-transcript dumps |
| `shoots/{date}-{subject}/` | One folder per shoot. Brief, run-of-show, shot list, raw asset index |
| `testing-framework.md` | LOCKED methodology. Every launch follows this. Naming, tracks, decision rules. |
| `launches/{YYYY-MM-DD}-launch-{N}/` | One folder per launch. plan.md + _daily-log.md + _debrief.md + screenshots/ |
| `campaigns/{YYYY-MM}-{lang}-{angle}/` | (deprecated, use launches/) Final creative, copy, audience config, perf log |
| `creative-library/{date}-{agency}-batch/` | Mass-generated scripts from Manus research, indexed by ad ID + ICP |
| `skill-briefs/` | Briefs for `/skill-creator` to convert into runnable skills |

## The 4 foundation files (Eddie pattern)

Every script-generation run loads these in order. Order matters.

1. **`writing-rules.md`** — slop filter (loaded first, sets the no-go zones)
2. **`voice.md`** — register + structure
3. **`product.md`** — offer + verified proof
4. **`icp.md`** — 7 personas, swap target per script

Then the source material (Manus research file or user prompt). Then write.

## The 9-skill ladder

| # | Skill | Status |
|---|---|---|
| 1 | `ads-strategy-lock` | not yet built. Quarterly. |
| 2 | `ads-competitor-mine` | brief written 2026-05-05. Uses Manus AI for Meta Ads Library scrape. |
| 3 | `ads-script-generate` | brief written 2026-05-05. Trade + lang + length + angle → single script in voice. One-off use. |
| 3b | `ads-script-mass-generate` | brief written 2026-05-05. Manus research → 200+ scripts via ICP multiplier (Eddie pattern). |
| 4 | `ads-shoot-brief` | brief written 2026-05-05. Script → shoot brief, run-of-show, shot list. |
| 5 | `ads-campaign-setup` | not yet built. Launch checklist + naming + UTMs. |
| 6 | `ads-launch` | not yet built. Publish manifest + Slack post. |
| 7 | `ads-daily-check` | not yet built. 9am pulse. |
| 8 | `ads-weekly-review` | not yet built. Kill / scale / iterate. |
| 9 | `ads-lead-handler` | not yet built. Form fill → score → route. |

Build order locked: 2, 3, 3b, 4 first (this week, for tomorrow's Victor shoot + Spark research run). Rest in week 2 after first launch.

## Voice rules (inherited from `aios/references/voice.md`)

- No em dashes. Ever.
- On-camera scripts use Register C (spoken, working-mind disfluencies preserved). Sound like Peter or Dani actually talking, not memorized.
- Ad copy headlines use Register A (polished, direct, plain English).
- Spanish scripts: Rodrigo / Velocity register. Direct-to-camera, data-driven, contractor-language ("una app que tiene todo" not "un CRM").

## Roles

- **Dani**: sales, on-site shoot lead, post-shoot upload, closing.
- **Peter**: creative direction, on-camera talent (EN), funnel/landing-page builds, BM owner.
- **Ashen**: systems, strategy, ads ops, campaign setup, daily check, lead routing.
- **Tad**: graphic design, static ad creative, social repurposing.

## Connections used

- Higgsfield (when activated) for AI b-roll + variants
- Google Drive for raw uploads (`/SCALE/Ads/`)
- Slack `#all-tools` for launch posts, `#new-leads` for routed form fills
- Fathom for strategy calls (auto-ingest to `research/`)
- GHL for lead pipeline + form
- Meta Ads Library + Foreplay + Manus AI for competitor mining (no MCP yet, manual)

## Hard rules

- Never publish to Scale SD's owned accounts without Dani approval.
- Strategy.md changes require a logged decision in `aios/decisions/log.md`.
- Every campaign folder must have an audience config and perf log before going live.
- Lead-form questions: max 3. Always: trade, monthly revenue range, biggest bottleneck.
