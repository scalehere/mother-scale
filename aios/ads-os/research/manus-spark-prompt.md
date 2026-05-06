# Manus AI Prompt — Spark Marketing Ad Library Deep-Dive

> Drop this whole prompt into Manus AI. It will scrape the Meta Ads Library, analyze every active Spark Marketing ad, and return a structured intel report.
> Manus is used because Claude is blocked from the Meta Ads Library (treated as competitor). Manus is Meta-affiliated and has access.
> Last updated: 2026-05-05.

## How to use

1. Open Manus AI in browser.
2. Start a new task.
3. Paste the prompt block below verbatim.
4. Manus will work for ~15-30 min and return a structured report.
5. Save the output to `research/manus-spark-{YYYY-MM-DD}.md`.
6. Distill the top insights into the Spark Marketing row of `../competitors.md`.

## The prompt (copy from here ↓)

```
ROLE
You are a senior performance-marketing strategist analyzing a competitor's full Meta ad library for a contractor-marketing agency in San Diego, California.

TARGET
Agency name: Spark Marketing
Owner: Cesar Gonzalez
Niche: Marketing services for home-service contractors (general contracting, roofing, HVAC, pools, plumbing, remodeling)
Estimated active ads: 67
Estimated monthly ad spend: ~$12,000

PRIMARY SOURCES
- Meta Ads Library: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&search_type=keyword_unordered&q=Spark%20Marketing
- Search variants to try: "Spark Marketing", "Cesar Gonzalez", "Spark Marketing Agency", "Spark Marketing contractors"
- Filter: active ads only, all platforms (Facebook + Instagram + Audience Network), all media types
- Sort by: oldest first (the long-runners are the proven winners)

WHY I NEED THIS
I am building a competing agency, Scale SD, in the same San Diego market. I am about to launch my own self-promotional Meta + TikTok campaign with a $1k/mo budget targeting San Diego home-service contractors with $200k+ in annual revenue. I need to learn what is already working in this niche before I spend my first dollar.

DELIVERABLES — return all of the following

1) AD INVENTORY TABLE
For every active ad you can access, extract:
- Ad ID (or library URL)
- Start date
- Days running (from start date to today)
- Format (static image / single video / carousel / collection)
- Length (if video)
- Platforms running on
- Headline (primary text first ~150 chars)
- Body copy
- CTA button label
- Destination URL or lead-form preview
- Visible language (English / Spanish / both)
- On-camera talent (Cesar himself / client / actor / no person)
- If on-camera: setting (office / job site / studio / car / outdoor)

2) HOOK ANALYSIS
List every distinct first-3-seconds hook used across all video ads. For each:
- Verbatim hook line
- How many ads use this hook (or close variants)
- Which trade(s) it targets
- Pattern type: pain-led / curiosity / authority / direct-claim / question / data-led / FOMO / other
- Estimated effectiveness signal (long-running = high, recently launched = unknown, paused = low)

2a) FULL VIDEO TRANSCRIPTS (verbatim, every video ad)
For EVERY video ad, transcribe the full spoken script word-for-word using your built-in transcription. Use this exact format per ad:

---
AD ID: {meta_ads_library_id}
START DATE: {YYYY-MM-DD}
DAYS RUNNING: {n}
LENGTH: {seconds}
LANGUAGE: {EN/ES/mixed}
ON-CAMERA: {who}

HOOK (0-3s, verbatim):
"{exact words}"

BODY (verbatim, full transcript):
"{exact words, every word, with [pause] markers where natural}"

CTA (verbatim):
"{exact words}"

ANGLE BREAKDOWN:
- Pain hit: {what pain point in their words}
- Proof shown: {what credibility marker, what number, what client name}
- Offer structure: {3-part / 4-part / problem-agitate-solve / etc.}
- Mechanism: {what makes the offer believable}
- Urgency: {if any, what kind}
- CTA pattern: {form / DM / link / call}

WHY THIS WORKS (your hypothesis):
{2-3 sentences}
---

This is the most important deliverable. Without verbatim transcripts and angle breakdowns I cannot write rewrites. Do not skip ads. Do not summarize. Word-for-word.

3) PAIN-POINT MAP
List every contractor pain point mentioned across all ads. For each:
- Verbatim phrasing they use
- How many ads hit this pain
- Whether they reframe it (problem → solution) or just leave it sitting (pain → urgency)

4) OFFER ARCHITECTURE
- What is the core offer? (services bundled, guarantee, pricing if disclosed)
- Is there a guarantee? Verbatim wording.
- What lead count or revenue claim do they make? (verbatim numbers + what client / what time window)
- What anti-positioning do they use? (e.g., "not Angi," "not shared leads," "not a vendor")

5) CTA & FUNNEL ANALYSIS
- What CTA buttons appear, ranked by frequency
- What CTA copy appears in the ad text itself ("DM us ADS," "Tap below," etc.)
- Where does the lead go? (Meta lead form / external landing page / Calendly / WhatsApp / Messenger)
- If landing page: describe its structure (video LP / written LP / VSL / form-only)
- Number of qualification questions on the lead form (if visible)

6) STATIC vs VIDEO BREAKDOWN
- % static / % video
- Average length of video ads (count buckets: 0-15s / 15-30s / 30-60s / 60s+)
- Any apparent winning format (longest-running creative format)

7) THE LONGEST-RUNNING 5 ADS
The ads that have been live the longest are the validated winners. For each of the top 5:
- Full breakdown: hook, body, CTA, format, what makes it work
- Hypothesis on WHY this specific creative has survived

8) OVERALL CREATIVE STRATEGY
- Tone of voice (formal / casual / aggressive / educational / boastful)
- How much they use Cesar himself on camera vs other talent
- Visible production quality (phone-shot / DSLR / studio / mix)
- B-roll patterns (job sites / CRM screens / phone notifications / calendars / dollar figures)
- Cesar's English / Spanish split (he is bilingual; what % of ads are in each)

9) WHAT I SHOULD STEAL (specific recommendations)
Given my context (Scale SD, San Diego, $1k/mo, 4-6 launch creatives, English + Spanish, on-location video at a Carlsbad GC site tomorrow), give me a ranked list of:
- The 3 hooks I should adapt for my launch (with my voice, not his exact words)
- The 1 funnel structure I should mirror
- The 1 format (static vs video, length) I should prioritize for max ROI on a small budget
- The 1 thing they're doing that I should explicitly NOT copy (because of fit, ethics, or claim verification risk)

10) GAPS — WHAT THEY ARE NOT DOING
What's missing from their ad mix? Niches, languages, formats, funnels they have NOT tested. These are my opening to differentiate.

OUTPUT FORMAT
- Markdown
- Tables wherever data is comparable
- Verbatim quotes wrapped in quotation marks
- All numerical claims clearly attributed (whose number is it, what time period)
- A 200-word executive summary at the very top
- Followed by the 10 sections above
- Ending with a single sentence: "Highest-confidence single takeaway from this analysis is: ____"

CONSTRAINTS
- Do not invent ad copy. If you cannot read it, mark "unreadable" and continue.
- Do not infer engagement / spend numbers Meta does not publicly show. Mark as "not disclosed."
- If the ads library returns fewer than 67 active ads when you search, report the actual count and note any access limitations.
- Take as long as you need. Quality over speed. This report informs a $1k/mo budget decision.
```

## Adapt for other competitors

To run the same deep-dive on another agency, swap these fields in the prompt:
- `Agency name`
- `Owner` (if known)
- `Niche` (if different)
- `Estimated active ads` (rough count from ads library)
- `Search variants`
- `WHY I NEED THIS` paragraph (keep it relevant to what we're learning from THIS competitor specifically)

Save adapted versions as `manus-{agency}-prompt.md` in this folder.

## Cross-runs to do after Spark

| Priority | Agency | Why |
|---|---|---|
| 1 | Spark Marketing | done above |
| 2 | Velocity Marketing (Rodrigo) | Spanish funnel, video LP we're mirroring |
| 3 | Local SD competitor (TBD) | proximity threat |
| 4 | One Hispanic-market national contractor agency | broader ES patterns |

## Output integration

After Manus returns the report:
1. Save raw to `research/manus-spark-{YYYY-MM-DD}.md`
2. Open `competitors.md`. Update the Spark Marketing row with new findings.
3. Pull the top 3 adaptable hooks into `scripts.md` Script 7 hook bank.
4. If the deep-dive surfaces a CTA we don't have, add it to `strategy.md` CTA bank.
5. Log the run in `competitors.md` ad-library research log.
