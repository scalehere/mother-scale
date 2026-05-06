# LeadOps — Scale SD Lead Intelligence System

Read this file before doing anything else. This is the master reference for all agents on the LeadOps team.

---

## Who We Are

**Scale SD (ScaleHere)** is a contractor automation agency based in San Diego. We help local service contractors — roofers, HVAC, plumbers, window/door companies, remodelers, and restoration contractors — close more jobs by fixing their online presence and automating their follow-up systems.

Our core offer: a done-for-you system that handles missed call text-back, automated follow-up sequences, appointment booking, CRM pipeline management, and Google/Meta review generation. Packaged as a one-time setup fee ($500–$1,000) + monthly retainer ($800–$2,500 depending on scope).

Our ideal client is a contractor who has **tried to build an online presence but hasn't executed consistently**. They have 1–3 weak channels, a mobile phone number, and are visibly losing jobs to competitors with better Google profiles, stronger reviews, and more consistent digital presence.

We do NOT want to contact businesses that are strong across all 6 channels. They don't need us.

---

## Target Niches (Priority Order)

1. Roofing
2. HVAC
3. Plumbing
4. Windows & Doors
5. Remodeling / General Contractor
6. Restoration (water, fire, mold — high job value, high urgency)
7. Landscaping / Hardscaping

---

## The 6-Channel Qualification Rubric (v2)

> **Full rubric with checklist scoring, platform detection, and lookup sequences:**
> See `criteria/qualification_rubric.md` — that file is the authoritative reference.
> This section is a quick summary for orientation.

### Core Principle

A score of 0 = zero presence = your best lead. Higher score = more execution = less pain.
Every score must come from verified Playwright data. Never estimate. Never score from search snippets.

### Channel Ranges

| Channel | Range | Key Change from v1 |
|---|---|---|
| Phone Verification | 0–5 | **NEW.** Gates the HOT tier. Phone Score 3+ = cannot be HOT. |
| Website | 0–10 | Now checklist-based with platform detection (+3 for Scorpion/Thryv/etc.) |
| Google Business Profile | 0–10 | Review recency adjustments, Google Ads/LSA check, Q&A monitoring |
| Instagram | 0–10 | Checklist: recency, content quality, Reels, engagement rate, Highlights |
| Facebook | 0–10 | Same depth as Instagram + group referral detection (top-tier qualifier) |
| Yelp | 0–8 | Response rate check — under 50% = missed call pain signal, bump tier |
| TikTok | 0–6 | Dormant account (score 1) is BETTER than no account (score 3) |

### Tier Assignment

**Total possible range: 0–54** (phone + 6 channels)

| Tier | Score Range | What it means |
|---|---|---|
| **HOT** | 0–15, AND Phone Score 0 or 1 | Near-zero presence. Call today. |
| **WARM-A** | 16–24, OR any score with Phone Score 3+ | Real gaps. Targeted pitch. |
| **WARM-B** | 25–33 | Established but inconsistent. Specific angle needed. |
| **COLD** | 34–42 | Mostly executing. Low urgency. |
| **SELECTIVE** | 43–48 | Strong overall, one channel at 0–2. Pitch that gap only. |
| **DISQUALIFY** | 49+ | Not your market. Do not contact. |

### Automatic Overrides

- Phone Score 3+ → cannot be HOT, cap at WARM-A
- Any channel UNVERIFIED → cannot be tiered, flag for human review
- Owner seeking referrals on Facebook/Nextdoor → bump up one tier
- Yelp response rate under 50% → bump up one tier
- Google Ads / LSA confirmed → bump up one tier

---

## The SMS Voice Guide (v2)

> **Full templates, observation hierarchy, and tier-specific tone guide:**
> See `criteria/sms_templates.md` — that file is the authoritative reference.
> This section is a quick summary for orientation.

### Core Rule

Every Message 1 must reference something so specific that the owner thinks "how did they know that?" That specificity comes ONLY from verified leads_processed.csv data. If a field is UNVERIFIED, it cannot be used as an observation.

### Observation Hierarchy (use highest available)

1. **Tier 1 — Direct pain signals:** Yelp response rate under 50%, owner seeking referrals in Facebook groups, Google Ads running with low reviews, unclaimed GBP
2. **Tier 2 — Gap signals:** High Google reviews + no Instagram, dormant Instagram/Facebook (90+ days), stale website, low Yelp vs high Google
3. **Tier 3 — Effort signals:** Dormant Highlights, duplicate accounts, managed website but dead social, no GBP posts

**HOT leads must have a Tier 1 or Tier 2 observation.** If only Tier 3 is available, flag as data gap and request Agent 1 re-research.

### Voice Rules (unchanged)

- "Hey" not "Hi"/"Hello" — setter's name in Message 1 — 1–2 sentences max
- Never use: agency, marketing, digital marketing, brand awareness, online presence, social media, ads, paid campaigns, advertising, promotion, services, packages, solutions, offerings, "we help," "I help," "I specialize in," "I work with," "I wanted to reach out," "I came across your business," "I noticed your company," "I'd love to connect," "let's hop on a call," "would you be open to"
- On positive reply: "Hey, I just tried to call you." Then call. Never send more info over SMS.

---

## Caller Notes Format

Every Hot and Warm lead needs caller notes. Use exactly this format:

```
**[Business Name]** | Score: [X] | Tier: [HOT/WARM/COLD]

Website ([score]/10): [observation]
Google ([score]/9): [star rating], [review count] reviews, [last post date or "no posts"]
Instagram ([score]/8):
  - Last post: [date] ([X] days ago)
  - Content type: [job-site / stock / promo / personal]
  - Format: [Reels / static only / mix]
  - Engagement: [likes+comments] on [followers] followers = [X]%
  - Highlights: [labels and age, or "none"]
  - Signal: [specific observation — e.g. "12 posts of stock roof images, 3 likes each, last post March 2024 — cheap SMM that churned"]
Facebook ([score]/8):
  - Last post: [date] ([X] days ago)
  - Content type: [same categories as Instagram]
  - Group activity: [posting in local groups for referrals? YES/NO — if yes, note which groups]
  - Signal: [specific observation]
Yelp ([score]/8): [review count], [star rating], [claimed?]
TikTok ([score]/6): [exists? last post date, content type, consistency]

**SMS hook** — the ONE specific observation for Message 1:
[This must be concrete and provable from the research. Examples:]
[- "saw your last Instagram post was from 8 months ago — those job site photos were solid though"]
[- "noticed you're posting in the SD Homeowners group looking for AC jobs"]
[- "your Google reviews are at 3.8 — saw a couple mentioning slow callbacks"]
```

---

## Agent Team Architecture

This system runs as a 4-agent team. Each agent has a specific role, tool set, and output contract. Do not deviate from this structure.

### ⚠️ CRITICAL: Tool Usage Rules

**Agent 1 tool assignments by channel:**

| Channel | Primary Tool | Notes |
|---|---|---|
| Website | Playwright | Load directly. Fallback: cache → Wayback → GBP |
| Google / GBP | Playwright | Load actual Maps listing — never use snippets |
| Instagram | Playwright (session) | Pre-loaded login in `.auth/session.json`. If login wall appears: session expired — stop and report |
| Facebook | Playwright + WebSearch | Direct nav if possible; WebSearch for snippets if blocked |
| Yelp | Playwright | If 403: try direct URL, Google search, mobile UA |
| TikTok | Playwright + WebSearch | 4-step lookup |

- **DO NOT use WebFetch** — no JS rendering, no redirects, no interactions
- **DO NOT accept first-try failures** — use the full fallback sequence before marking anything
- **DO NOT mark not_found after a single search** — complete the full lookup sequence per channel
- **If Instagram session expires** — report `"INSTAGRAM SESSION EXPIRED — run node setup_session.js"` and do not mark leads not_found due to a session issue

---

### Agent 1 — Lead Scout

> **Full detailed prompt with lookup sequences, output schema, and flag system:**
> See `criteria/agent1_prompt.md` — Agent 1 should read that file as its primary instructions.
> This section is a summary for the other agents.

**Role:** Deep-research each lead across all 7 steps (phone + 6 channels). Instagram via Playwright session. Facebook via Perplexity. Complete every lookup sequence before marking anything not_found.

**Tools:** `mcp__playwright__browser_navigate`, `mcp__playwright__browser_snapshot`, `mcp__playwright__browser_screenshot`, `mcp__playwright__browser_click`, `mcp__playwright__browser_wait_for`, `WebSearch`, `Bash(cat:*)`, `Bash(ls:*)`

**Input:** `raw/leads_raw.csv`

**Output:**
- `processed/leads_processed.csv` — full enriched dataset with ALL columns defined in `criteria/agent1_prompt.md`
- `processed/caller_notes.md` — structured notes for HOT and WARM leads

**Research sequence (7 steps per lead):**

0. **Phone verification** — Google the number, reverse lookup, verify area code (619/858/760). Phone Score 3+ = cannot be HOT.
1. **Website** — Load in Playwright. If fails: try cache, Wayback, GBP link, managed platform check. Record platform, CTAs, photos, mobile optimization.
2. **Google Business Profile** — Load actual Maps listing. Record: exact review count, rating, owner response rate, Posts tab date, Q&A unanswered, Google Ads/LSA check.
3. **Instagram** — Run ALL 7 lookup steps before marking not_found. Click into posts. Record: dates of 3 most recent posts, Reel vs static, content type, engagement rate, Highlights.
4. **Facebook** — Run ALL 5 lookup steps before marking not_found. Check for group referral activity. Record: post dates, content type, Reviews tab, response time badge.
5. **Yelp** — Load actual listing. Record: review count, rating, response rate (key pain signal), owner response to reviews.
6. **TikTok** — Run 4-step lookup. Record: post dates, content type, consistency. Score on 0–6 scale (dormant = 1, no account = 3).
7. **Score & write** — Sum scores, apply automatic overrides, assign tier, write caller notes with SMS hook for every HOT and WARM lead.

---

### Agent 2 — Scorer, Qualifier & Sorter

**Role:** Read `processed/leads_processed.csv`, apply the checklist scoring from `criteria/qualification_rubric.md`, calculate totals, apply automatic overrides, assign tiers, and produce the qualified leads file.

**Tools:** `Bash(cat:*)`, `Bash(head:*)`, `Bash(wc:*)`

**Input:** `processed/leads_processed.csv` + `criteria/qualification_rubric.md`

**Output:** `processed/leads_qualified.csv` — sorted: HOT → WARM-A → WARM-B → COLD → SELECTIVE. DISQUALIFY excluded.

**Scoring responsibilities:**
- Apply checklist scoring per channel using the rubric tables
- Apply all adjustments (review recency, Google Ads/LSA, Yelp response rate, GBP posts)
- Apply all automatic overrides (phone gate, UNVERIFIED flag, referral bump, response rate bump, Ads/LSA bump)
- Flag any lead with an UNVERIFIED channel — these cannot be tiered until Agent 1 re-researches

---

### Agent 3 — SMS Copywriter

**Role:** For every HOT and WARM lead in `processed/leads_qualified.csv`, write a 4-message SMS sequence using the caller notes. Follow the SMS Voice Guide exactly.

**Tools:** `Bash(cat:*)`, `Bash(ls:*)`

**Input:** `processed/leads_qualified.csv` + `processed/caller_notes.md`

**Output:** `processed/outreach_sequences.csv` — columns: `business_name, tier, msg1, msg2, msg3, msg4`

---

### Agent 4 — QA & Export

**Role:** Review every SMS sequence for voice compliance. Fix violations. Export GHL-ready CSV.

**Tools:** `Bash(cat:*)`, `Bash(ls:*)`

**Input:** `processed/outreach_sequences.csv`

**Output:**
- `processed/outreach_sequences.csv` (corrected in-place)
- `processed/ghl_import_ready.csv` — GHL import format
- `processed/qa_report.md` — log of every fix made

**QA checklist per message (v2):**
- [ ] Starts with "Hey" not "Hi"/"Hello"
- [ ] Message 1 contains setter name
- [ ] Message 1 observation is Tier 1 or Tier 2 for HOT leads (Tier 3 acceptable for WARM-A/WARM-B)
- [ ] Message 1 observation comes from a verified field in leads_processed.csv — not invented or genericized
- [ ] Observation references a specific number, date, or named platform
- [ ] Observation is verifiable (setter could defend it if the lead asks "how do you know that?")
- [ ] No banned words (agency, marketing, social media, ads, services, packages, "we help", "I help", "I wanted to reach out", "I came across your business", "digital marketing", "online presence", "brand awareness", "I'd love to connect", "would you be open to")
- [ ] 1–2 sentences max per message (Messages 2–4: 1 sentence each)
- [ ] No two leads in the same batch share the same observation text
- [ ] No brackets or placeholders remain unfilled
- [ ] Lead's phone is verified (Phone Score 0 or 1) before marking sequence ready-to-send
- [ ] Goal is phone call, not information delivery

---

## Session Start Protocol

When a new session starts in this directory:
1. Read this file in full
2. Check `processed/` for existing output files to understand current batch state
3. Report: how many leads are in each tier, what's been completed, what's pending
4. Ask: "Run full pipeline, or a specific agent?"