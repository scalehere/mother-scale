# LAUNCH 1 — 2026-05-08 (Friday)
## First Scale SD Self-Promo Campaign

> Source shoot: 2026-05-06 Victor / VIP General Contractor (Vista CA)
> Total budget: $1,000/month, $50/day
> Goal: establish baseline data on Track / Trade / Angle / Format / Length
> Status: PRE-LAUNCH

---

## The 6 ads at launch

Selected from `creative-library/2026-05-05-spark-batch/` + new cuts from Victor shoot.
Held constant: Audience, Geography, Budget per Track.
Variables: Angle, Format, Length.

| # | Ad name | Angle | Format | Length | Track |
|---|---|---|---|---|---|
| 1 | `SCALE_2026-05-08_C_GC_PickingJobs_H41_15s_v1` | Story | UGC dialogue | 15s | C (DM) |
| 2 | `SCALE_2026-05-08_A_GC_HyperLocal_H22_30s_v1` | Identity (Vista) | Talking Head | 30s | A (form) |
| 3 | `SCALE_2026-05-08_B_GC_BurnedBob_H49_45s_v1` | Confession | Talking Head | 45s | B (video LP) |
| 4 | `SCALE_2026-05-08_A_GC_Mechanism_H17_30s_v1` | Mechanism | B-Roll + VO | 30s | A (form) |
| 5 | `SCALE_2026-05-08_C_GC_TooBusy_H42_5s_v1` | Story (anchor) | UGC | 5s | C (DM) |
| 6 | `SCALE_2026-05-08_A_All_Static_H92_static_v1` | Contrarian | Static | n/a | A (form) |

**Cut sources:** Cuts 1, 5 from Victor+Peter conversational (Block 2 of shoot brief). Cut 2 from hyper-local talking head (Block 4). Cut 3 from Peter solo confession (Block 5). Cut 4 from job-site walkthrough (Block 7). Cut 6 from Tad static design.

---

## Hypotheses

Each ad ships with one testable hypothesis.

| # | Hypothesis | Success metric (Day 7) |
|---|---|---|
| 1 | Cesar's 145-day winner format works in our market when adapted to GC + DM funnel | CPL < $15 + 7+ leads |
| 2 | Hyper-local "Vista" framing beats generic "San Diego" by 25%+ on CTR | CTR > 2.5% |
| 3 | Burned-Bob confession angle pre-qualifies high-intent leads (lower volume, higher quality) | CPL $20-$30, ≥40% form-completion rate |
| 4 | Mechanism reveal works on solution-aware audience without on-camera talent | CPL < $20 |
| 5 | 5-second teaser at $5/day delivers more impressions than longer cuts at same spend | 4x impression count of #1 |
| 6 | Static beats video on CPL even though video wins on CTR | CPL beats avg of 1-5 by 20%+ |

---

## Audience (LOCKED across all 6 ads)

**Why locked:** we're testing creative, not audience. Audience changes only after Cycle 1 debrief.

| Setting | Value |
|---|---|
| Location | San Diego County |
| Geo radius | 30 miles from San Diego city center, includes Vista, Carlsbad, Oceanside, La Mesa, Chula Vista, El Cajon, Escondido |
| Age | 30-60 |
| Gender | All |
| Languages | English |
| Detailed interests | "General Contractor" + "Construction" + "Remodeling" + "Home Improvement" + "Small Business Owners" |
| Income proxy | $200k+ HHI (Meta's "top 10% household income" segment) |
| Excluded | Already-engaged ScaleHere followers (warm audience handled separately) |

---

## Budget split (Day 1 default, reweight after Day 14)

| Track | Daily | Allocated to | Rationale |
|---|---|---|---|
| A — Lead Form | $20 | Cuts 2, 4, 6 (~$6.50/day each) | Volume play. Most data fastest. |
| B — Video LP | $15 | Cut 3 ($15/day) | Single-creative concentrated test on the long confession. |
| C — DM Funnel | $15 | Cuts 1, 5 ($10/day + $5/day) | Test 15s vs 5s on cheapest CPC mechanism. |

**Total:** $50/day. **Total monthly:** $1,500 (over by $500 vs $1k cap — accept for cycle 1 to get clean data, normalize Cycle 2).

Wait — re-checking. $50/day × 30 = $1,500/month. **Cap is $1,000/month per Fathom decision.**

**Adjusted budget:** $33/day = $1,000/month. Reallocated:

| Track | Daily | Allocated to |
|---|---|---|
| A — Lead Form | $14 | Cuts 2, 4, 6 (~$4.70/day each) |
| B — Video LP | $10 | Cut 3 |
| C — DM Funnel | $9 | Cuts 1, 5 ($6 + $3) |

**Total:** $33/day. $990/month. Within cap.

(Note for Dani: this is significantly below Spark's recommended $4k/mo starting spend. Accept as cycle-1 learning budget. Scale to $50/day after first booked client.)

---

## Tracking & infrastructure

### Pre-launch checklist (Ashen, must complete before pressing live)

- [ ] BM slot freed (window-guy account removed) — confirm Tuesday
- [ ] Two ad accounts active: Peter BM (handles Cuts 1, 5 — Track C) + Ashen BM (Cuts 2, 3, 4, 6)
- [ ] Lead form built in Meta with EXACT 3 questions:
  1. What trade are you in?
  2. What's your monthly revenue range? ($0-$50k / $50k-$200k / $200k+)
  3. What's your biggest bottleneck right now? (Slow phone / Bad leads / No system / Other)
- [ ] Form auto-routes to GHL pipeline `Scale-Self-Promo-2026-05-08` via native Meta integration
- [ ] GHL workflow: form fill → SMS to Dani's phone (760-XXX) within 60 seconds → email to ashen@scalehere.com
- [ ] Pixel firing on www.scalehere.com (Meta Pixel Helper passes)
- [ ] DM keyword "SCALE" automation built in IG: incoming DM with "SCALE" → auto-reply with 1-paragraph + Calendly link
- [ ] UTMs locked: `?utm_source={meta|tiktok}&utm_campaign=2026-05-launch&utm_content={cut-id}`
- [ ] Slack channel `#new-leads` ready
- [ ] Test one form submission end-to-end. Confirm SMS arrives.
- [ ] Test one IG DM with "SCALE" keyword. Confirm auto-reply fires.

### What goes wrong if these aren't done
- No pixel = no retargeting later, no audience-build, dead campaign
- No GHL routing = leads sit in Meta inbox, Dani doesn't see them, deals lost
- No DM auto-reply = Track C dies in 24 hours (audience expects instant response on IG)

---

## Review cadence (auto-scheduled in calendar)

| Date | Day # | Action | Document in |
|---|---|---|---|
| 2026-05-11 | Day 3 | Early-signal review. Kill anything CPL > $50 or CTR < 0.5%. | `_daily-log.md` |
| 2026-05-15 | Day 7 | Real-signal review. Scale winners. Kill losers. Iterate v2 on near-misses. | `_daily-log.md` |
| 2026-05-22 | Day 14 | Track decision. Reweight A/B/C budgets. | `_daily-log.md` |
| 2026-05-29 | Day 21 | Mid-cycle. Iteration check. | `_daily-log.md` |
| 2026-06-08 | Day 30 | Cycle close. Full debrief. | `_debrief.md` |

---

## Day 0 setup (Friday 2026-05-08)

| Time | Action | Owner |
|---|---|---|
| 9:00 | Final pre-launch checklist run | Ashen |
| 10:00 | Pixel + GHL routing end-to-end test | Ashen |
| 11:00 | Build campaigns in Meta Ads Manager | Ashen |
| 13:00 | Dani final review of 6 cuts. Approval per cut. | Dani |
| 14:00 | Press LIVE on Cuts 1-6 | Ashen |
| 14:30 | Slack post in #all-tools: "🚀 Launch 1 live. 6 ads, 3 tracks, $33/day." | Ashen |
| 15:00 | First-form submission test from Ashen's phone (lead form Track A) | Ashen |
| 15:30 | First DM "SCALE" test from Ashen's IG (Track C auto-reply) | Ashen |
| 16:00 | Verify all metrics dashboards live + accessible | Ashen |

---

## Decision tree at Day 7 (the most important review)

```
For each ad:
  │
  ├─ Spent ≥ $40 AND CPL < $15 AND ≥7 leads?
  │     YES → SCALE to $20/day. Mark winner.
  │     NO → continue
  │
  ├─ Spent ≥ $40 AND CPL between $15-$25?
  │     → HOLD. Monitor to Day 14.
  │     
  ├─ Spent ≥ $40 AND CPL between $25-$35?
  │     → ITERATE. Swap hook. Ship v2.
  │     
  ├─ Spent ≥ $40 AND CPL > $35?
  │     → KILL. Document reason. Free budget.
  │
  └─ Spent < $40?
        → Spend distribution issue. Reallocate budget within Track.
```

---

## Cycle 1 success criteria

Cycle 1 succeeds (regardless of MRR generated) if we exit Day 30 with documented answers to:

1. **Best Track** — A, B, or C wins on lead-to-call conversion?
2. **Best Trade** — GC tested. Pool/HVAC/Roof inferred from extrapolation. Plan Cycle 2 around #1.
3. **Best Angle** — Story, Confession, Hyper-Local, or Mechanism wins on CPL?
4. **Best Format** — Talking head, UGC dialogue, B-roll, or static wins on CPL?
5. **Best Length** — 5s, 15s, 30s, or 45s wins on engagement?

If we exit Day 30 unable to answer ANY of these 5, the launch was a methodology failure, not a market failure. Diagnose process before re-running.

---

## What we DON'T do in Cycle 1

- Don't test Spanish (saved for Cycle 2 after Bilingual Beto talent confirmed)
- Don't test multiple audiences (audience locked)
- Don't test multiple Trades simultaneously (focus on GC for first cycle, generalize after)
- Don't test multiple geos (San Diego County only, hyper-local within)
- Don't bring in TikTok yet (Meta-only Cycle 1, TikTok Cycle 2 if EN signal is positive)
- Don't change creative mid-cycle without an iteration log entry

Discipline beats optionality on $1k/mo.

---

## What success looks like at Day 30

| Metric | Target | Stretch |
|---|---|---|
| Total leads | 90+ (matches our guarantee) | 130+ |
| Blended CPL | < $20 | < $12 |
| Discovery calls booked | 8+ | 15+ |
| Closed deals | 1 | 2-3 |
| New MRR | $1,500-$2,500 | $5,000+ |
| Ads to graduate to Cycle 2 | 2-3 winners | 4 |

**ROI math:** $1,000/month spent + $1,500/month retainer cost = $2,500 cost. One closed $1,500/mo retainer for 4 months = $6,000 revenue. Break-even at month 2. Profit at month 3.

---

## Launch 1 hard rules (specific to this launch)

- Track C (DM funnel) requires Daniel checking IG inbox 3x/day during cycle. If he can't, kill Track C.
- Track B (video LP) requires the LP to load in <2 seconds. If it doesn't, kill until fixed.
- All 6 ads use the LOCKED guarantee: "90 exclusive leads in 12 weeks. Yours alone, never shared. If we miss, you don't pay."
- Comment "SCALE" CTA only on Track C ads. Track A uses "Tap below." Track B uses "Apply below."
- If a single ad spends > 40% of total budget on Day 1-2 alone (before review), pause and rebalance immediately. Meta's algorithm sometimes runaway-spends on one ad.

---

## Hand-off

### To Dani (must read)
- Approve 6 cuts before Day 0 launch
- Be reachable 9-6 PT on Day 1-3 for inbound calls
- Check IG DMs 3x/day during Cycle 1 for Track C handoffs
- Don't change ad copy or audience without Slack-thread alignment

### To Peter (must read)
- Available for hook reshoots if Day 7 review shows hook iteration needed
- Watch all 6 ads on launch day to confirm voice/register feels right
- Flag if any cut sounds "too AI" — we'll reshoot

### To Tad (must read)
- Static design (Cut 6) must match brand kit + voice register A
- 1 static + 1 alternate version submitted by Day -1
- Repurpose any winning ad for IG Stories / TikTok organic in week 2

### To Editor (must read)
- 48-hour SLA on cuts from raw shoot files
- File naming per convention. Strict.
- One Slack ping when each cut is delivered

---

*Built per `testing-framework.md v1.0`. Last updated: 2026-05-06.*
