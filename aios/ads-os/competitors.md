# Scale SD Meta Ads — Competitor Tracking

> Mining intel from Spark Marketing, Velocity Marketing, and other contractor-marketing agencies.
> Source method: Meta Ads Library (manual) + Foreplay (manual) + Manus AI deep dives.
> Updated: 2026-05-05.

## Why this exists

Spark Marketing is running 67 ads at ~$12k/mo and surviving. Velocity Marketing built a video-LP funnel that converts in Spanish. They've already paid for the experiments we'd otherwise pay for. Mine their library, steal the structure, write our own copy.

## Active competitors tracked

### 1. Spark Marketing — Cesar Gonzalez

| Attribute | Value |
|---|---|
| Owner | Cesar Gonzalez |
| Niche | Contractors (broad) |
| Stack | Meta-heavy, static + video |
| Active ads (as of 2026-05-05) | 67 |
| Estimated spend | ~$12,000 / month |
| Recommended starting spend (Cesar's advice to Dani) | $4,000 / month |
| Funnel | Mostly lead form. Some long-form ads that double as content. |
| Signature pattern | Long-running static ads. Same creative for months. Tells us the static format actually works for this audience. |
| Meta Ads Library link | search "Spark Marketing" or "Cesar Gonzalez" in https://www.facebook.com/ads/library |
| Status | Manus deep-dive prompt ready. Run tonight. See `research/manus-spark-prompt.md`. |

**What we believe works for him:**
- Direct claim ads: "I made [client] $1M, here's how"
- "Free training" follow-bait. Worst case: gets a follow.
- Static images with photo-of-himself + headline + plain-English benefit
- Heavy volume = constant testing = he never has to guess

**What to steal:**
- The static format (cheap to produce, already validated)
- Long-running ad mindset: don't kill creative early, the audience hasn't seen it yet
- Direct claim hooks (with verified numbers only)

### 2. Velocity Marketing — Rodrigo

| Attribute | Value |
|---|---|
| Owner | Rodrigo |
| Niche | Hispanic contractors, multi-city US |
| Stack | TikTok + Meta, Spanish-first |
| Funnel | Video landing page → 3-question form → calendar booking |
| Revenue | ~$70k/mo (Dani's intel) |
| Signature pattern | Direct-to-camera Rodrigo. Data-driven. Shows CRM screens, lead counts, dollar figures. Frames CRM as "an app that has everything." |
| Anti-pattern | Doesn't post organic content (until recently). Ads carry the whole load. |

**What we believe works for him:**
- Spanish, not English. Most Hispanic contractors prefer Spanish content.
- Speaking the contractor's language ("una app que tiene todo") not the agency's language ("CRM software")
- Video LP that pre-qualifies BEFORE the form, not after
- Showing actual results (screenshots of leads, dollar figures, calendar) instead of testimonials
- 3-question form (matches our locked rule)

**What to steal:**
- The video LP funnel structure (Track B in our launch)
- Contractor-language framing for technical features
- 3-question form pattern
- Spanish on TikTok (not Meta) for highest organic-to-paid leverage

### 3. Spark Marketing Coach (TBD)

The "guy who coaches agencies" Dani mentioned. Identify and add when found. Likely Cesar himself or someone in his orbit.

---

## How to mine new competitors

### Step 1: Find them

- Meta Ads Library: search by keyword ("contractor leads," "home services marketing," "construction ads") + region (San Diego or US national)
- Filter: active ads only, sort by start date (oldest first = longest-running = working)
- Look for: 20+ active ads, multi-month runtime, agency-style branding

### Step 2: Quick-scan with Foreplay

- foreplay.co. Save anything with high comment counts or visible reach
- Tag with: niche, language, format (static/video), funnel type

### Step 3: Deep-dive with Manus AI

- Use the prompt in `research/manus-spark-prompt.md`. Adapt the agency name + ad library URL.
- Manus output goes in `research/manus-{agency}-{date}.md`
- Distill insights here in `competitors.md` under that agency's row

### Step 4: Distill into ours

- What hook do they reuse? → add to our hook bank in `scripts.md`
- What CTA wording? → check against our CTA bank in `strategy.md`
- What funnel? → match to Track A or Track B
- What proof points? → cross-check against ours, never copy claims we can't verify

---

## Ad-library research log

| Date | Competitor | Method | Output file |
|---|---|---|---|
| 2026-05-05 | Spark Marketing | Manus AI prompt drafted | `research/manus-spark-prompt.md` (run pending) |

Append rows as new mining runs complete.

---

## Hard rules

- Never copy a competitor's exact claim. Verify every dollar figure with our own client before use.
- Never copy creative pixel-for-pixel. Copy structure, write our own copy.
- Foreplay swipes are inspiration only. Always rewrite in Scale SD voice (Register C for spoken, Register A for static).
