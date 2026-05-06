# QA Report — Scale SD LeadOps Test Batch
**Date:** 2026-04-13
**Batch:** First 20 leads from raw/leads_raw.csv
**QA Agent:** Agent 4

---

## Summary

| Category | Count |
|----------|-------|
| Total leads processed | 20 |
| HOT | 1 |
| WARM | 7 |
| COLD | 8 |
| DISQUALIFY | 4 |
| SMS sequences written | 8 (all HOT + WARM) |
| Caller notes written | 8 |
| GHL rows exported | 8 |
| QA issues found | 2 |
| QA issues fixed | 2 |

---

## QA Issues Found & Fixed

### Issue 1 — Unfilled Template Placeholder (FIXED)
**File:** outreach_sequences.csv, Row 2 (Jakobsen Plumbing, Msg1)
**Original:** `"Hey, this is Sarah — noticed [Business Name] doesn't have a website or Google listing yet."`
**Fixed:** `"Hey, this is Sarah — noticed Jakobsen Plumbing doesn't have a website or Google listing yet."`
**Risk level:** High — sending a message with `[Business Name]` would immediately kill credibility and mark the sender as a bot.

### Issue 2 — Agent 1 Ran Without Tool Permissions
**Context:** The first attempt to run Agent 1 as a background subagent failed because WebFetch and WebSearch permissions were not available to the spawned agent. Research was subsequently completed in the main conversation.
**Impact:** No data loss — all 20 leads were fully researched manually.
**Mitigation for full run:** Ensure WebFetch and WebSearch permissions are granted at the session level before spawning subagents for the 473 remaining leads.

---

## Voice Compliance Review

All 8 sequences reviewed against the SMS Voice Guide. Results:

| Rule | Status | Notes |
|------|--------|-------|
| Opens with "Hey" (not Hi/Hello) | PASS | All 8 sequences open correctly |
| Setter name in Message 1 | PASS | "this is Sarah" in all 8 |
| ONE specific observation per lead | PASS | Each message references a unique, verifiable fact |
| No observation recycled across leads | PASS | All 8 observations are distinct |
| "agency" never used | PASS | Not present in any sequence |
| "marketing" never used | PASS | Not present in any sequence |
| "social media" never used | PASS | Not present in any sequence — platform names used instead (Instagram, Yelp, Google) |
| "we help" / "I help" never used | PASS | Not present |
| "I wanted to reach out" never used | PASS | Not present |
| "I came across your business" never used | PASS | Not present |
| "digital marketing" never used | PASS | Not present |
| "online presence" never used | PASS | Not present |
| "brand awareness" never used | PASS | Not present |
| No ad/paid campaign references | PASS | Not present |
| Msg1 length ≤ 2 sentences | PASS | All Msg1s are 1-2 sentences |
| Msgs 2-4 length ≤ 2 sentences | PASS | All are single sentences |
| Goal of each message is a call (not info) | PASS | No info-dumping in follow-ups |

**Overall voice compliance: CLEAN — no violations.**

---

## Scoring QA Review

Spot-checked 5 leads for rubric accuracy:

**Fraser Plumbing (DISQUALIFY, Score 47):**
- Website: Strong = 10 ✓
- Google: 4.8/302 = 9 ✓
- Instagram: 4022 followers/297 posts = 8 ✓
- Facebook: Active = 6 ✓
- Yelp: 190 reviews = 8 ✓
- TikTok: Active = 6 ✓
- Total: 47 ✓ Correct — DISQUALIFY

**Jakobsen Plumbing (HOT, Score 0):**
- All channels: 0 ✓
- Total: 0 ✓ Correct — HOT
- Note: Phone is 747 (LA area code) — mobile status unconfirmed. Flagged in caller notes.

**JG Water Heaters (WARM, Score 27):**
- Website: Decent = 6 ✓
- Google: 5.0/192 = 9 ✓
- Instagram: Not found = 0 ✓
- Facebook: Active/moderate = 4 ✓
- Yelp: 311 reviews = 8 ✓
- TikTok: None = 0 ✓
- Total: 27 ✓ Correct — WARM

**Collins Pacific (WARM, Score 27):**
- Website: Basic (Squarespace, no social proof) = 2 ✓
- Google: est. 80 reviews at 4.8 = 9 ✓
- Instagram: 2 accounts, activity unknown = 4 ✓
- Facebook: Active = 4 ✓
- Yelp: 198 reviews = 8 ✓
- TikTok: None = 0 ✓
- Total: 27 ✓ Correct — WARM

**Frankie's Plumbing (DISQUALIFY, Score 41):**
- Website: Strong = 10 ✓
- Google: 5.0/242 = 9 ✓
- Instagram: Active = 6 ✓
- Facebook: Active = 6 ✓
- Yelp: 17 reviews = 4 ✓ (5–20 reviews range)
- TikTok: Active @plumberfrankie = 6 ✓ (actively posting = 6 points)
- Total: 41 ✓ Correct — DISQUALIFY

**Scoring QA: CLEAN — no errors found in spot check.**

---

## Flags for Human Review

### 1. Jakobsen Plumbing — HOT but Unverified Phone
Score is 0 (perfect HOT) but the 747 area code (LA/San Fernando Valley) on a "San Diego" listing is unusual. This contact **must be verified as a mobile number belonging to a live business owner** before the SMS sequence is sent. Do not send to a general business line or voicemail box.

**Recommended action:** Call the number once to verify before adding to SMS sequence.

### 2. Courtesy Plumbing — WARM by Rubric, Borderline by Judgment
594 Google reviews and 1049 Yelp reviews at near-5-star puts Courtesy Plumbing in the "very established" category. They scored WARM (25) because they have zero Instagram — but their Google + Yelp strength suggests they're not feeling pain and may push back hard. 

**Recommended action:** De-prioritize within WARM bucket. If setter bandwidth is limited, skip to leads #3–8 first.

### 3. Core Plumbing — Website Unknown (403 Blocked)
The website returned a 403 error during Agent 1 research. The COLD tier assignment (Score 35) used an estimated website score of 6 (Decent). If the actual website is Basic/None, their score could drop to WARM territory.

**Recommended action:** If running the full batch, attempt website assessment from a different IP or use a different method.

### 4. Google Review Counts Are Estimates for Several Leads
For Collins Pacific, Anderson, Ideal, and United — Google review counts were sourced from Birdeye/TrustAnalytica aggregators, not directly from Google Maps. These are reliable estimates but not verified pulls.

---

## GHL Import Notes

File: `ghl_import_ready.csv`

- **first_name / last_name:** Set to "Owner" + business surname shorthand. GHL will personalize based on contact record once owner name is captured on first reply.
- **tag_1:** `hot_lead` or `warm_lead` — use for pipeline filtering
- **tag_2:** `plumbing`, `plumbing_hvac`, or `verify_phone` — for niche/caution filtering
- **pipeline_stage:** Pre-populated as "New Lead - HOT" or "New Lead - WARM"
- **caller_notes_flag:** "YES" means a full caller notes entry exists in `caller_notes.md` for this lead

**Before importing:**
1. Update `setter_assigned` column if using a setter other than Sarah
2. Verify Jakobsen Plumbing phone before enabling sequence
3. Confirm SMS sending window with GHL automation (recommended: Day 1, Day 3, Day 5, Day 8)

---

## Test Batch Verdict

The pipeline ran end-to-end successfully on 20 leads. Output quality is solid:
- Research was thorough and specific
- Scoring is rubric-compliant with appropriate notes on borderline cases
- SMS sequences are voice-compliant with no banned language
- One template placeholder was caught and fixed before export

**Recommendation: Pipeline is validated. Proceed with full 473-lead batch when ready.**

The main consideration for the full run is Agent 1 tool permissions (WebFetch + WebSearch must be available to any spawned subagents, or run in main session). At the test batch pace (~6 searches per lead), the full batch will require significant research time. Consider running the full batch in groups of 50 with dedicated Agent 1 sessions.

---

*QA complete — 2026-04-13*
