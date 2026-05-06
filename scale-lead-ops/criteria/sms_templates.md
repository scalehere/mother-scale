# SMS Templates & Voice Guide — Scale SD LeadOps v2

---

## The One Rule That Overrides Everything

Every Message 1 must reference something so specific that the business owner
thinks "how did they know that?" That specificity only comes from the
leads_processed.csv data that Agent 1 collected by actually visiting their pages.

If Agent 1 did not visit the page, you do not have a real observation.
Do not fabricate one. Do not send a generic message. Flag the lead and wait.

---

## Voice Rules

**Always:**
- Open with "Hey" — never "Hi" or "Hello"
- Use the setter's first name in Message 1
- Reference one specific, verifiable observation from the enrichment data
- Write like a person texting, not a company messaging
- Keep Message 1 to 1–2 sentences maximum
- Keep Messages 2–4 to 1 sentence each

**Never use these words or phrases — not even close variations:**
- agency, marketing, digital marketing, brand awareness, online presence
- social media (name the platform instead — Instagram, Yelp, TikTok)
- ads, paid campaigns, advertising, promotion
- services, packages, solutions, offerings
- "we help," "I help," "I specialize in," "I work with"
- "I wanted to reach out," "I came across your business," "I noticed your company"
- "I'd love to connect," "let's hop on a call," "would you be open to"

**The one test:** Read the message out loud. If it sounds like it came from
a marketing person, rewrite it. If it sounds like a neighbor who happened to
notice something, send it.

**On a positive reply:** Setter responds ONLY with "Hey, I just tried to call you."
Then calls immediately. Never answer questions over SMS. Never send more info.

---

## Message Templates

> Agent 3: Fill in the [BRACKETS] from the leads_processed.csv data.
> Never send a message with a bracket still in it.
> Never reuse the same observation across two leads in the same batch.

**Message 1 — Day 1 (Initial contact)**
```
Hey [owner first name or generic if unknown], this is [Setter Name] —
[SPECIFIC OBSERVATION]. Quick question for you.
```

**Message 2 — Day 3 (Follow-up)**
```
Hey [first name] — just wanted to make sure this didn't get buried.
Got 2 minutes this week?
```

**Message 3 — Day 6 (Last real attempt)**
```
Hey [first name] — last time reaching out. Worth a quick call?
```

**Message 4 — Day 10 (Soft close)**
```
Hey [first name] — no worries if timing's off.
I'll check back in a few months.
```

---

## How to Write the Specific Observation

The observation in Message 1 comes directly from the leads_processed.csv fields.
The best observations reference a gap between two data points — something they
have that should be working but isn't, or something they're clearly missing.

**The observation hierarchy — use the highest one that applies:**

### Tier 1 — Direct pain signals (use these first, they hit hardest)

These come from the new data fields Agent 1 now collects.
They reference something the owner can feel right now.

| Data field | Example observation |
|---|---|
| `yelp_response_rate` under 50% | "saw you've got 89 Yelp reviews but your response rate is sitting at 34% — quick question for you." |
| `facebook_owner_seeking_referrals` = yes | "noticed you were asking for referrals in the [group name] group last week — quick question for you." |
| `google_ads_running` = yes | "saw you're running ads but your Google reviews page only shows 23 reviews — quick question." |
| `google_lsa_badge` = yes | "saw the Google Guaranteed badge — noticed something on your profile worth a quick call about." |
| `google_profile_status` = unclaimed | "noticed [Business Name]'s Google listing isn't claimed yet — quick question for you." |

### Tier 2 — Gap signals (strong, specific, easy to verify)

These reference a visible mismatch between what they have and what they're missing.

| Data field | Example observation |
|---|---|
| High Google reviews + `instagram_status` = not_found | "saw you've got [X] Google reviews but zero Instagram — quick question." |
| High Google reviews + `instagram_last_post_days_ago` > 90 | "saw [Business Name]'s last Instagram post was [X] months ago — quick question." |
| High Google reviews + low `yelp_review_count` | "saw [X] Google reviews but only [Y] on Yelp — quick question for you." |
| `instagram_status` = not_found + decent website | "noticed [Business Name] doesn't have an Instagram yet — quick question." |
| `facebook_last_post_days_ago` > 90 | "saw the last post on [Business Name]'s Facebook was [X] months ago — quick question." |
| Low Google reviews + `google_rating` = 5.0 | "saw a perfect 5.0 rating but only [X] reviews showing — quick question for you." |

### Tier 3 — Effort signals (good, shows you looked closely)

These reference something specific you saw that shows real attention.

| Data field | Example observation |
|---|---|
| `instagram_notes` mentions dormant Highlights | "noticed your Instagram has a 'Before & After' Highlight but the last post was [X] months back — quick question." |
| Two Instagram accounts found | "noticed [Business Name] has two Instagram accounts — quick question for you." |
| `website_platform` = Scorpion/Thryv but weak social | "saw the website's dialed in but the Instagram hasn't had a post since [date] — quick question." |
| `google_posts_last_date` = none or very old | "noticed [Business Name]'s Google profile hasn't had an update in a while — quick question." |
| `website_status` = no_website_found | "noticed [Business Name] doesn't have a website yet — quick question for you." |

---

## Observation Rules

**One observation per message. Never two.**
"saw you have no Instagram and your Yelp is unclaimed" — too much. Pick one.

**Name the specific thing, not the category.**
Bad: "saw some gaps in your online presence"
Good: "saw your last Instagram post was from February"

**Reference real numbers when you have them.**
Bad: "saw you don't have many Yelp reviews"
Good: "saw 312 Google reviews but only 18 on Yelp"

**Never reference something you cannot verify.**
If Agent 1 marked a field UNVERIFIED, you cannot use it as an observation.
Go to the next tier down.

**Never frame it as a problem.**
Bad: "noticed your Instagram is dead"
Good: "noticed the last post on your Instagram was about 8 months ago"

---

## Lead-Tier Tone Guide

**HOT leads (score 0–15):**
The observation is usually about what's completely missing — no website, no GBP,
no Instagram at all. Keep it simple and factual. Don't editorialize.
They already know. They just haven't had a reason to act.

Example:
"Hey, this is Sarah — noticed Jakobsen Plumbing doesn't have a Google listing
set up yet. Quick question for you."

**WARM-A leads (score 16–24):**
The observation is about a visible effort that didn't stick — dormant social,
unanswered Yelp quotes, GBP with no posts. Reference the specific gap.

Example:
"Hey, this is Sarah — saw your Yelp response rate is sitting at 28%.
Quick question for you."

**WARM-B leads (score 25–33):**
The observation is about a specific mismatch — high Google reviews but dead
Instagram, strong website but no Yelp, established brand with no TikTok footprint.
Be more precise because these owners are more sophisticated.

Example:
"Hey, this is Sarah — saw Collins Pacific has been around since '89 but the
website has no reviews or project photos on it. Quick question for you."

---

## QA Checklist for Agent 3

Before writing each sequence, confirm:

- [ ] observation comes from a verified field in leads_processed.csv
- [ ] observation references a specific number, date, or named platform
- [ ] none of the banned words appear anywhere in the sequence
- [ ] Message 1 is 1–2 sentences maximum
- [ ] Messages 2–4 are 1 sentence each
- [ ] no two leads in this batch share the same observation
- [ ] no brackets or placeholders remain unfilled
- [ ] the lead's phone is verified before the sequence is flagged ready-to-send
