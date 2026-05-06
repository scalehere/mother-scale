# Scale SD — Ad Testing & Launch Framework

> The repeatable system for how Scale SD launches, tests, kills, scales, and iterates ads.
> Built once. Used every shoot. No re-inventing.
> Version: 1.0 — locked 2026-05-06.

## Core principles

1. **Every ad is a test.** No ad ships without a hypothesis and a kill threshold.
2. **Budget is a constraint, not a target.** $1k/mo means we test cheap, decide fast.
3. **Naming is destiny.** Bad naming = no learning. Every ad has a parsable name.
4. **Decisions on schedule.** Day 3 review. Day 7 review. Day 14 review. Not when you feel like it.
5. **The bible is the source of truth.** Every angle, hook, and avatar pulls from `Scale_SD_Creative_Bible.xlsx`.

---

## The 3 funnel tracks

| Track | Mechanism | When to use | Spark validation |
|---|---|---|---|
| **A — Lead Form** | Meta on-platform form, 3 questions. Auto-routes to GHL → SMS to Dani's phone. | Volume play. Cold audience. Maximum leads, qualify after. | Spark's recent ads (May 2026) all switched to this. |
| **B — Video LP** | Pre-qualification video on landing page → 3-question form → calendar booking. Velocity-style. | Quality play. Higher cost-per-lead, higher show rate, higher close rate. Pre-qualifies. | Velocity's $70k/mo system. |
| **C — DM Funnel** | Comment "SCALE" or DM "SCALE" → IG keyword auto-DM → 1-on-1 conversation → Calendly. | Lowest budget. Relationship-build. Best ROI when budget is small and salesperson is available. | Spark's 140-145 day longest-runners are this format. |

**Default split for any new shoot:**
- 40% Track A (form) — most volume, lowest CPL benchmark
- 30% Track B (video LP) — quality / pre-qualification test
- 30% Track C (DM) — relationship + low-friction test

After 14 days of data, reweight to the winner. After 30 days of data, lock the dominant track.

---

## Naming convention (LOCKED)

Every campaign, ad set, and ad name follows this exact format:

```
SCALE_{YYYY-MM-DD}_{TRACK}_{TRADE}_{ANGLE}_{HOOK#}_{LENGTH}_v{N}
```

Example:
```
SCALE_2026-05-08_A_GC_PickingJobs_H41_15s_v1
SCALE_2026-05-08_C_GC_BurnedBob_H49_30s_v1
SCALE_2026-05-08_B_Pool_Urgency_H72_45s_v1
```

| Slug | What it means | Source |
|---|---|---|
| `SCALE` | Brand prefix | Always |
| `YYYY-MM-DD` | Launch date | Day campaign goes live |
| `TRACK` | A / B / C | Funnel track (above) |
| `TRADE` | GC / Pool / HVAC / Roof / Plumb / Win / Land / All | Avatar from Sheet 2 |
| `ANGLE` | PickingJobs / BurnedBob / HyperLocal / Mechanism / Urgency / Story / Confession / Education | Sheet 5 |
| `HOOK#` | H1-H100 | Hook reference number from Sheet 7 |
| `LENGTH` | 5s / 15s / 30s / 45s / 60s | Ad duration |
| `v{N}` | Version | v1 = first cut, v2 = iteration after kill/edit |

**Why this matters:** when you pull a Meta report 6 months from now, you can filter by any slug to learn what worked. "Show me every GC PickingJobs angle across all shoots" is a one-line filter.

---

## Test cell taxonomy

Every launch is a 5-dimension matrix. We never fire an ad without specifying all 5.

| Dimension | Options |
|---|---|
| **Trade** | GC / Pool / HVAC / Roof / Plumb / Win / Land / All-Trades |
| **Angle** | Problem / Mechanism / Identity / Story / Social Proof / Urgency / Risk Reversal / Education |
| **Format** | Talking Head / UGC / B-Roll+VO / Static / Carousel / Reels |
| **Length** | 5s / 15s / 30s / 45s / 60s |
| **Track** | A (form) / B (video LP) / C (DM) |

**Rule of 1:** when running A/B tests, hold 4 of 5 dimensions constant. Vary only ONE. Otherwise you can't attribute the win.

**Rule of 6:** at any one time, never run more than 6 active ads per ad account. Past 6, you can't see signal in the noise on $50/day.

---

## The 4-phase launch protocol (every shoot uses this)

### Phase 1 — POST-SHOOT (Days 0-2: edit + setup)

| Day | Action | Owner |
|---|---|---|
| 0 (shoot day) | Raw to Drive `/SCALE/Ads/{date}-{subject}/raw/`. Slack ping in `#all-tools`. | Dani |
| 1 (edit day) | Editor cuts 6-8 versions matching shoot brief. Each cut named per convention. | Editor |
| 1-2 | Ad accounts confirmed clean. Pixel verified firing. Lead form built (3 Qs). DM automation built (if Track C). | Ashen |
| 2 | Final review by Dani. Approve/edit each cut. Move to `/SCALE/Ads/{date}-{subject}/approved/`. | Dani |

**Hard rule:** nothing goes live without Dani's written approval per cut.

### Phase 2 — LAUNCH (Day 3: go live)

| Action | Detail |
|---|---|
| Build campaign in Meta Ads Manager | Campaign name = `SCALE_{date}_{shoot-slug}_LaunchWeek` |
| Build campaign in TikTok Ads Manager (if Spanish) | Same naming |
| Set ad sets per Track (A, B, C) | One ad set per track |
| Place 4-6 ads inside each ad set (max 6 per Rule of 6) | Each named per convention |
| Daily budget: $50/day total, split per Track default | $20 A / $15 B / $15 C |
| Audience: SD County, 30-mile radius from city center, age 30-60, contractor + home-services interests, $200k+ HHI proxy | Locked across all shoots — only test creative, not audience |
| Pixel + GHL routing verified BEFORE pressing go live | Test one form submission end-to-end |
| Slack post in `#all-tools`: "🚀 Launch live. {N} ads, 3 tracks, $50/day. Day 3 review on calendar." | Ashen |

### Phase 3 — REVIEW (Days 6, 9, 16, 23, 30)

Three review cadences, three different decisions.

#### Day 3 review (early signal — kill the worst)
- Pull report: spend, impressions, CTR, CPL per ad
- **Kill rule:** any ad with CPL > $50 OR CTR < 0.5% on $20+ spent → pause it
- **Hypothesis check:** is one Track outperforming? Note in launch doc.
- Reallocate killed budget to top performer

#### Day 7 review (real signal — scale the best)
- Same metrics, larger sample
- **Scale rule:** any ad with CPL < $15 AND ≥7 leads → increase budget to $40/day
- **Kill rule:** any ad with CPL > $35 OR fewer than 3 leads on $50+ spend → pause
- **Iterate rule:** any ad with promising CTR (1.5%+) but high CPL → swap hook only, ship as v2

#### Day 14 review (track decision)
- Compare Track A vs B vs C lead-to-call conversion rates
- **Reweight rule:** dominant track gets 60% of budget. Second-best gets 30%. Third gets 10%.
- Document in launch debrief

#### Day 30 review (campaign close)
- Calculate: total spend, total leads, blended CPL, calls booked, deals closed, MRR generated
- Mark winners for next-shoot inspiration
- Mark losers for never-do-again list
- Update `Scale_SD_Creative_Bible.xlsx`: any new hook that won goes into Sheet 7 with awareness stage + MS reference

---

## Decision rules — kill / scale / iterate

| Metric on $20+ spend | Action |
|---|---|
| CPL < $15 | **SCALE** to $40/day |
| CPL $15-$25 | Hold, monitor |
| CPL $25-$35 | Iterate (swap hook) |
| CPL $35-$50 | Kill at Day 7 if no improvement |
| CPL > $50 at Day 3 | **KILL** immediately |
| CTR < 0.5% on $20 spent | **KILL** immediately |
| CTR 1.5%+ but CPL > $35 | Iterate (hook is working, body or CTA is breaking) |
| 7+ leads in first 7 days | **SCALE** |

These thresholds are San Diego contractor benchmarks. Update quarterly based on accumulated data.

---

## Per-launch documentation

Every launch creates a folder: `ads-os/launches/{YYYY-MM-DD}-launch-{N}/`

Required files:
- `plan.md` — pre-launch (audience, ad list, budgets, hypotheses)
- `_daily-log.md` — every review day's notes (Day 3, 7, 14, 30)
- `_debrief.md` — written post Day 30. Top 3 wins, top 3 losses, top 3 learnings, what to test next.
- `screenshots/` — pixel-fire confirmation, ad-set screenshots, Meta Lead Form preview, GHL pipeline view

Without all four, the launch is not "complete." Don't archive until done.

---

## Budget envelope (locked from Fathom 2026-05-05 strategy call)

| Bucket | Monthly | Daily |
|---|---|---|
| Total ad spend | $1,000 | $50 |
| Meta (English-led) | $600 | $20 (Track A) + $15 (Track B) + $5 (Track C) |
| TikTok (Spanish-led, when launched) | $400 | $13 (varies, EN testing first) |

**Scaling rule:** the $1k/mo cap holds for 12 weeks. After the first booked client from ads, scale ad spend to 8% of new MRR.

---

## What we test in cycle 1 (the FIRST shoot's purpose)

The first shoot establishes baselines. We're not optimizing yet. We're learning:

1. **Which Track converts in our market** — A, B, or C?
2. **Which Trade has lowest CPL** — GC, Pool, or generic?
3. **Which Angle resonates** — Story, Confession, Hyper-Local, or Mechanism?
4. **Which Format wins** — talking head, UGC dialogue, B-roll, or static?
5. **Which Length wins** — 5s, 15s, 30s, 45s?

After cycle 1 (30 days), we know the answer to 3-4 of these. Cycle 2 doubles down on what worked.

---

## Library evolution

After every launch debrief:

- Winning hooks → into Sheet 7 of the Bible (with stage + MS reference + creator's slug)
- Winning angles → into Sheet 5 of the Bible (with new brand example)
- Winning customer language → into Sheet 11 (verbatim from form responses)
- New objections from form responses → into Sheet 12 with crushers
- Killed-ads' lessons → into `_debrief.md`, never re-tested without a hypothesis change

The Bible gets smarter every cycle. By cycle 4 it's a moat.

---

## Roles per launch

| Person | Job |
|---|---|
| Dani | Approve cuts, own client communication, monitor inbound calls |
| Peter | Creative lead, on-camera, weekly review participant |
| Ashen | Build campaigns, run reviews, decide kill/scale/iterate, document |
| Tad | Static-format ads, organic repurposing |
| Editor | 48-hour cut turnaround per shoot |

---

## Hard rules

- No ad goes live without a kill threshold.
- No ad goes live without a campaign tag in our naming convention.
- No campaign runs past Day 7 without a documented review.
- No ad uses an unverified specific dollar claim.
- No campaign exceeds 6 active ads per ad account.
- No funnel ships without a working pixel + GHL routing test.
- All proof claims must trace to Sheet 10 of the Bible.

## Update log

- 2026-05-06: Initial framework. v1.0. Locked from Fathom call + Spark Manus deep-dive + Bible build.
