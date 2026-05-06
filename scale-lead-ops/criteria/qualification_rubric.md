# Lead Qualification Rubric — Scale SD LeadOps v2

---

## How This Rubric Works

**A score of 0 means zero digital presence. That is your best possible lead.**

Higher score = stronger execution = less pain = lower chance they need you.
Lower score = tried and failed = active pain = high conversion likelihood.

Every single score must come from verified Playwright data — meaning the agent
actually visited the page and pulled real numbers. If a page cannot be reached
after exhausting every fallback method listed below, mark it UNVERIFIED and flag
for human review. Never estimate. Never guess. An estimated score that flows into
a tier assignment is worse than no score at all because it looks like real data.

---

## Step 0 — Phone Verification (Required Before Anything Else)

The phone number gates the entire HOT tier. Run this first.

**How to check:**
1. Google the number exactly as written — e.g. "(858) 354-8185 plumber"
2. Check if it appears on their website, GBP listing, or Yelp listing
3. Note the area code — flag any number that doesn't match San Diego
   (SD area codes: 619, 858, 760)
4. Run through a reverse lookup if needed (search the number + "owner" or "cell")

| What you find | Phone Score |
|---|---|
| Confirmed mobile — owner name on voicemail, reverse lookup shows personal cell | 0 |
| Likely mobile — local SD area code, personal voicemail greeting, no hold music | 1 |
| Unconfirmed — generic voicemail or no answer, but local SD area code | 3 |
| Business line — hold music, auto-attendant, or receptionist picks up | 4 |
| Out-of-area code (not 619/858/760) with no clear explanation | 4 |
| Disconnected or no answer after two attempts | 5 |

**Hard rule:** Phone Score 3 or higher = this lead cannot be HOT.
Cap at WARM-A and add this note to the GHL record:
*"Phone unverified — do not launch SMS sequence until owner mobile confirmed."*

---

## Step 1 — Website (0–10)

Use Playwright to load the page from the URL in the CSV.

**If the page fails (403, 404, timeout), try these in order before giving up:**
1. Search `cache:[url]` in Google to load a cached version
2. Try `web.archive.org/web/*/[url]` for a recent snapshot
3. Check the GBP listing — the description or posts often repeat site content
4. Check if the business runs on a managed platform (see Platform Detection below)

**Score using this checklist. Each checked item = points shown.**

| What to check | Points |
|---|---|
| Phone number visible in the header or hero on mobile | 1 |
| Clear CTA above the fold — Call Now, Book Online, Get a Quote, Schedule | 1 |
| Service area explicitly named — cities, zip codes, or neighborhoods | 1 |
| Before/after project photos or real job site gallery (not stock images) | 2 |
| Customer reviews or testimonials embedded on the page with real names | 1 |
| Individual service pages — not just a bulleted list, actual dedicated pages | 1 |
| Working contact form or online booking (click it and verify it loads) | 1 |
| Mobile-optimized layout (test by shrinking Playwright viewport to 390px) | 1 |
| Custom professional design — clearly not an unmodified free template | 1 |

**Platform detection — add these points on top of the checklist above:**

| Platform found | Add |
|---|---|
| Scorpion, Broadly, Thryv, ReachLocal, Hibu | +3 pts — they already pay a marketing agency |
| ServiceTitan, Jobber, or Housecall Pro site | +2 pts — they're already systemized |
| Unmodified free WordPress, Squarespace, or Wix template | +0 |

**If no website exists at all:** Score = 0. This is a strong HOT signal. Write it
explicitly in the enrichment notes.

---

## Step 2 — Google Business Profile (0–10)

**Do not use search snippet data or third-party aggregators (Birdeye, TrustAnalytica,
BrightLocal). Go to the actual listing every time.**

Load in Playwright: `https://www.google.com/maps/search/[business name]+San+Diego`

**Score using this checklist:**

| What to check | Points |
|---|---|
| Profile is claimed and verified | 1 |
| Review count 10–50 | 1 |
| Review count 51–200 | 2 — use this instead of the row above |
| Review count 201–500 | 3 — use this instead of the rows above |
| Review count 500+ | 4 — use this instead of the rows above |
| Rating is 4.5 stars or above | 1 |
| Real photos present — job site, team, equipment (not stock) | 1 |
| Owner responds to reviews (check the last 5 reviews for a response) | 1 |
| Services and hours fully filled out | 1 |

**Review recency — check separately and adjust:**

Click "Sort by: Newest" and note the date of the most recent review.

| Most recent review | Adjustment |
|---|---|
| Within the last 7 days | +1 |
| 8–30 days ago | no change |
| 31–90 days ago | −1 |
| 90+ days ago | −2 |

**Google Posts — check separately:**
Click the "Updates" or "Posts" tab on the GBP listing.
- Active post in the last 30 days: no change (expected baseline)
- No posts in 90+ days: −1 (they set it up and stopped)
- No posts ever: −1

**Google Ads check — run this search in Playwright:**
Search `[business name] plumber San Diego` and look at the top results.

| What you see | Adjustment |
|---|---|
| They appear as a Sponsored / Ad result | −2 (spending on leads = pain = high intent) |
| They have a Google Guaranteed or LSA badge | −3 (highest intent signal possible) |
| Neither | no change |

**Missed call / response gap check:**
Go to their GBP Q&A section. Count unanswered questions.
- 1 or more unanswered questions: −1 (they're not monitoring their profile)

**If no GBP found or listing is unclaimed:** Score = 0.

---

## Step 3 — Instagram (0–10)

**Never mark not_found after just one search. Run the full lookup sequence first.**

**Lookup sequence — do all of these before giving up:**
1. Check the business website footer and contact page for an Instagram link
2. Check their Facebook page "About" section — Instagram is often linked there
3. Check their Google Business Profile for linked social accounts
4. Search: `"[business name]" site:instagram.com`
5. Search: `"[business name]" San Diego instagram`
6. Try common handle patterns:
   - `instagram.com/[businessname]`
   - `instagram.com/[businessname]sd`
   - `instagram.com/[businessname]_sd`
   - `instagram.com/[businessname]plumbing`
   - `instagram.com/[firstword][secondword]` (e.g. pawsplumbing)
7. If the business has a known slogan, nickname, or owner's name — try those too

Only mark `not_found` after all 7 steps fail. If multiple accounts exist, score the
most active one and list the others in the notes.

**What to collect when you visit the profile:**
- Follower count
- Total post count
- Date of each of the 3 most recent posts (click into the post — the date is there)
- Likes and comments on each of those 3 posts
- Whether each of those 3 posts is a Reel or a static image
- What the content actually shows:
  - Job site / real work (before/afters, installs, job footage)
  - Stock images or promo graphics
  - Memes or shared content
  - Personal content / owner selfies
- Whether they have Story Highlights and what those Highlights are labeled

**Score using this checklist:**

| What to check | Points |
|---|---|
| Account exists | 1 |
| Last post within 30 days | 2 |
| Last post 31–90 days ago | 1 — use instead of above |
| Last post 90+ days ago | 0 — dormant is a qualifier signal, not a score |
| Posts show real job site content (not stock, not memes) | 2 |
| At least one of the last 3 posts is a Reel | 1 |
| Engagement rate above 2% — (avg likes + comments) / followers x 100 | 1 |
| Follower count 500–2,000 | 1 |
| Follower count 2,000+ | 2 — use instead of above |
| Consistent cadence — at least 2 posts per month for the last 3 months | 1 |

**Qualifier signals — note these in the enrichment notes, do not score:**
- Owner posting personally with informal captions and crew selfies
- Posts in local community groups asking for referrals or work
- Bio says "DM for quote" or similar — they're trying to use Instagram for leads
- Highlights labeled "Reviews," "Our Work," or "Before/After" but no recent posts —
  they set it up with intention and stopped. This is your ideal client in one image.

**If no account found after all 7 lookup steps:** Score = 0.
Write: *"No Instagram found — full 7-step lookup completed."*

---

## Step 4 — Facebook (0–10)

**Same principle as Instagram — exhaust all lookups before marking not_found.**

**Lookup sequence:**
1. Check the business website footer and contact page for a Facebook link
2. Check their Google Business Profile for a linked Facebook page
3. Search: `"[business name]" site:facebook.com`
4. Search: `"[business name]" San Diego facebook`
5. Try direct URL patterns:
   - `facebook.com/[businessname]`
   - `facebook.com/[businessnamesd]`
   - `facebook.com/[businessnameplumbing]`

**What to collect when you visit the page:**
- Page likes count
- Date of the 3 most recent posts
- Likes and comments on each of those 3 posts
- Whether any posts are videos (Reels or native video)
- What the content shows — real job site work vs stock images vs shared memes
- Whether the owner is personally active in the comments or posting themselves
- Whether the Reviews tab is visible and what the rating + count is

**Score using this checklist:**

| What to check | Points |
|---|---|
| Page exists | 1 |
| Last post within 30 days | 2 |
| Last post 31–90 days ago | 1 — use instead of above |
| Last post 90+ days ago | 0 — dormant is a qualifier signal |
| Posts show real job site content (not stock, not memes) | 2 |
| At least one of the last 3 posts is a video | 1 |
| Engagement rate above 1% — (avg likes + comments) / page likes x 100 | 1 |
| Page likes 300–1,500 | 1 |
| Page likes 1,500+ | 2 — use instead of above |
| Owner visibly active in comments or posting personally | 1 |

**Key qualifier signals — note these explicitly, they change the pitch:**
- Owner asking for referrals or work in local Facebook neighborhood groups —
  this is your single strongest pain signal. They are actively struggling for leads.
  Flag as: *"OWNER SEEKING REFERRALS — top priority."*
- Negative reviews visible on the Facebook Reviews tab with no response
- Posts getting zero engagement despite 500+ page likes — dead audience

**If no page found after all 5 lookup steps:** Score = 0.
Write: *"No Facebook found — full 5-step lookup completed."*

---

## Step 5 — Yelp (0–8)

Load the actual Yelp listing in Playwright. Do not use cached or aggregated data.
Search: `yelp.com/search?find_desc=[business name]&find_loc=San+Diego+CA`

**What to collect:**
- Review count and star rating
- Date of the most recent review
- Whether the business responds to reviews (check the last 5)
- Request a Quote response rate — this is shown publicly on the listing page
- Whether they have photos uploaded by the business (not just customer photos)

**Score using this checklist:**

| What to check | Points |
|---|---|
| Listed and claimed on Yelp | 1 |
| Review count 5–20 | 1 |
| Review count 21–75 | 2 — use instead of above |
| Review count 76–200 | 3 — use instead of above |
| Review count 200+ | 4 — use instead of above |
| Rating 4.0 stars or above | 1 |
| Business photos present (not just customer photos) | 1 |
| Owner responding to reviews | 1 |

**Response rate check — this is your missed call pain signal:**
Find the "Request a Quote" section. Yelp shows response rate and response time publicly.

| Response rate | Adjustment |
|---|---|
| 90%+ response rate | +1 |
| 50–89% | no change |
| Under 50% response rate | −2 (they are missing quote requests — direct pain signal for your product) |
| "Rarely responds" or response rate not shown | −1 |

**Review recency check:**
Note the date of the most recent review.
- Within 30 days: no change
- 31–90 days ago: −1
- 90+ days ago: −2

**If not listed or unclaimed:** Score = 0.

---

## Step 6 — TikTok (0–6)

**Lookup sequence:**
1. Check the business website for a TikTok link
2. Search: `"[business name]" site:tiktok.com`
3. Search: `"[business name]" San Diego tiktok`
4. Try: `tiktok.com/@[businessname]`, `tiktok.com/@[businessnamesd]`

**Scoring logic — read this carefully, it is intentional:**

A contractor with a dead TikTok account is a BETTER lead than one with no account.
It means they knew TikTok matters, tried to start, and gave up — exactly your client.
A contractor actively posting good TikTok content does not need you.

| What you find | Score |
|---|---|
| No TikTok account at all | 3 — they don't know the channel exists |
| Account exists but dormant (last post 90+ days ago) | 1 — tried and gave up, ideal signal |
| Posts occasionally but inconsistently | 3 — partial execution |
| Actively posting with good content and engagement | 6 — executing well, not your market |

---

## Tier Assignment

Add up all channel scores plus phone score.

**Total possible range: 0–54**

| Tier | Score Range | What it means |
|---|---|---|
| **HOT** | 0–15, AND Phone Score 0 or 1 | Near-zero presence. Actively losing jobs. Call today. |
| **WARM-A** | 16–24, OR any score with Phone Score 3+ | Real gaps, real pain. Needs a targeted pitch. |
| **WARM-B** | 25–33 | Established but inconsistent. Specific angle required. |
| **COLD** | 34–42 | Mostly executing. Low urgency, low close probability. |
| **SELECTIVE** | 43–48 | Strong overall but one channel at 0–2. Pitch that gap only. |
| **DISQUALIFY** | 49+ | Strong across all channels. Not your market. Do not contact. |

**Automatic overrides:**
- Phone Score 3+: cannot be HOT regardless of total. Cap at WARM-A.
- Any channel marked UNVERIFIED: cannot be tiered. Flag for human review first.
- Owner confirmed seeking referrals on Facebook/Nextdoor: bump up one tier regardless of score.
- Yelp response rate under 50%: bump up one tier — this is a direct missed call pain signal.
- Google Ads / LSA confirmed: bump up one tier — they're already spending on leads.

---

## What a Great HOT Lead Looks Like

- Plumber with no website, 8 Google reviews, no Instagram, no Facebook, answers their
  cell on the second ring — completely word-of-mouth, invisible online, losing every job
  where someone checks Google before calling
- HVAC contractor with a 2019 Wix template, 22 Google reviews at 4.2 stars, a Facebook
  page last posted in 2022, and a Yelp response rate of 30% — tried everything once,
  nothing stuck, now just answering the phone and hoping
- Restoration contractor with a decent website, 15 Google reviews, an Instagram account
  with 6 posts from 18 months ago, and Story Highlights labeled "Our Work" with zero
  recent content — they had a plan, hired someone cheap, it fell apart

These businesses share one thing: they know they need help and they have tried.
That's the difference between a HOT lead and a brand new business with nothing.

---

## Scoring Accuracy Rules

1. **Never score from search snippets.** Always visit the actual page.
2. **Never mark not_found without completing the full lookup sequence** for that channel.
3. **Never estimate review counts** from third-party aggregators. Pull from the source.
4. **Always note the date of the last post** — follower count alone is meaningless.
5. **Always calculate engagement rate** — do not just report likes as a number.
6. **If a website returns a 4xx error**, try cache and Wayback before marking unknown.
7. **If two accounts exist** for the same channel, score the most active and note both.
8. **Flag any anomaly** that changes the pitch — dormant highlights, duplicate accounts,
   owner posting for work, unanswered Q&A, response rate under 50%.
