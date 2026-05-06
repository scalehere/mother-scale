---
campaign: 01
name: Cold Outbound — 700 Contractor Leads (v1 Generic)
status: building
owner: Daniel / Scale SD
sending_domain: s.scalehere.com
from_email: media@scalehere.com
created: 2026-04-16
version: 1.0
---
 
# Campaign #1 — Cold Outbound (700 Contractor Leads)

**Goal:** Book 15-min discovery calls on Daniel's calendar from a cold list of 700 San Diego contractor leads (mobile phone + email). Generic contractor copy for v1 — niche-split in v2 after we see which leads reply.

**Channels:** SMS-first, email in-between. Link/artifact delivery is SMS-only to protect email deliverability on Stage 1 warmup domain.
**Hook:** Pavel-style reciprocity — "noticed 3 things the top SD contractors do that most local guys don't. Wanna hear them?" Value delivered as an inline text reply (no landing page, no PDF, no link) when they reply yes.
**Sequence length:** 5 touches over 12 days + 1 auto-reply (Touch 1.5) triggered by positive reply. Touch 6 dropped for TCPA safety — see Section 3.
**Send pacing:** Native GHL **Drip Mode** — 25/50/100/150 contacts-per-day ramp via workflow settings (no manual batching).
**Geography:** All 700 leads are San Diego-based → single timezone (PT). All send windows below are PT.

---

## 0. Pre-Flight Checklist

Confirm in GHL before starting:
- [x] Sending domain `s.scalehere.com` verified
- [x] A2P 10DLC approved
- [x] GHL sub-account designated for agency's own outreach (separate from client sub-accounts)
- [ ] From-address user configured: `media@scalehere.com`
- [ ] Default SMS number assigned to sub-account
- [ ] Calendar created: "Discovery Call – Daniel" (15 min)
- [ ] Physical mailing address on file for CAN-SPAM footer
- [x] Setter assignment: all 4 (Daniel, Ashane, Tad, Justin) — first-to-respond claims
- [x] Physical mailing address for CAN-SPAM footer: **345 E Park Ave, Escondido, CA 92025**

---

## 1. CSV Import Plan

### Clean the CSV first

Required columns (map to GHL standard fields):

| CSV Column | GHL Field | Notes |
|---|---|---|
| First Name | first_name | Title-case, strip junk |
| Last Name | last_name | Title-case |
| Phone | phone | E.164 format: `+1XXXXXXXXXX` |
| Email | email | Validate via ZeroBounce / NeverBounce before import — bounces torch deliverability |
| Business Name | company_name | Title-case |
| City | city | |
| State | state | 2-letter code |
| Website | website | |

### Custom fields to create (Settings → Custom Fields)

| Field Name | Type | Purpose |
|---|---|---|
| `niche` | Dropdown | Roofing / HVAC / Plumbing / Windows / Remodeling / Restoration / Landscaping / Other |
| `lead_source` | Text | "Scrape – April 2026" |
| `lead_score` | Number | From LeadOps rubric (0–52) if available |
| `lead_tier` | Dropdown | HOT / WARM / COLD |
| `city_state` | Text | "San Diego, CA" format — used in merge tags |
| `sequence_start_date` | Date | When they entered the sequence |
| `last_touch_type` | Text | email / sms |
| `reply_intent` | Dropdown | Positive / Negative / Question / OOO / None |

### Tags on import
- `cold-outbound-v1`
- `batch-april-2026`
- `source-scraped`

### Import in staged batches
Upload the CSV but **don't apply the `cold-outbound-v1` tag to all 700 at once**. Tag in daily waves per the pacing schedule in Section 5 — the tag is what triggers sequence entry.

---

## 2. Pipeline + Stages

Create pipeline: **Cold Outbound – Agency**

| Stage | Entry Trigger | Exit |
|---|---|---|
| 1. New Lead | Imported | Sequence starts |
| 2. Sequence Active | Day 0 sent | Reply OR sequence complete |
| 3. Positive Reply | Tag: `reply-positive` | Booked OR disqualified |
| 4. Call Booked | Calendar appt booked | Show / no-show |
| 5. Showed | Appt status: showed | Proposal / close / DQ |
| 6. Closed Won | Client signed | — |
| 7. Closed Lost / DQ | Rejected | — |
| 8. Nurture | Sequence ended, no reply | Re-engage 90d |

---

## 3. The Copy — All 6 Touches + Auto-Reply

**From:** `media@scalehere.com` (Daniel / Scale SD)
**Voice:** Casual, direct, human. Low-status, no agency posture. Reads like a local guy texting another local guy. Pavel-style.
**Hook mechanic:** Pavel reciprocity — "noticed 3 things, wanna hear them?" The 3 observations are delivered inline via SMS when they reply yes. Zero links, zero artifact production, fully automated.

---

### TOUCH 1 — Day 0, SMS (Pavel hook)
*Send window: Tue–Thu, 10am–12pm PT.*

```
Hey {{first_name}}, this is Daniel — local San Diego. Been watching the top contractors in SD and noticed 3 things they're all doing that most local guys aren't. Wanna hear them? Reply STOP to opt out.
```

~210 chars = 2 segments. Low-status framing + curiosity tease + one-word reply CTA.

---

### TOUCH 1.5 — Auto-Reply (triggered by positive reply keywords)

**Trigger:** Reply received on SMS or email containing any of: `yes`, `yeah`, `yep`, `sure`, `ok`, `send it`, `send`, `show me`, `let's hear it`, `hit me`, `lmk`, `share`, `spill`, `go`

**Send channel:** SMS (keeps link off the warmup email domain)

```
Alright here's the 3:

1. A review system on their website that asks customers "how'd we do?" first. Happy ones get auto-routed to Google. Unhappy ones go to a private feedback form so the owner can fix it direct — instead of it nuking their Google rating publicly.

2. Face-to-cam Reels posted weekly, then tracking which ones actually pop. The top performers get turned into paid ads — but the ads run behind a qualifying form, not a "learn more" button. Means real booked leads, not vanity views.

3. Responding to inbound leads in under 5 min. Most SD guys take 4–6 hrs. First-to-respond closes ~80% of the time.

Any of these feel off for {{company_name}}? Happy to dig into whichever hurts most.

— Daniel
```

**Why this works:**
- Value delivered inline, no link, no page, no PDF
- Zero deliverability risk on `s.scalehere.com`
- Ends with a specific question about *their* business — transitions into setter conversation naturally
- Same message for every lead — fully automated, no per-niche customization needed

---

### TOUCH 2 — Day 2, Email *(if no reply to Touch 1)*
*Send window: Tue–Thu, 9am–11am PT. No link.*

**Subject:** `that thing I mentioned`

**Body:**
```
{{first_name}} —

Daniel here — texted you the other day about 3 things the top SD contractors are doing differently.

Not trying to be a hassle — wasn't sure if my text hit. Wanna hear them? Reply "yes" and I'll send them over.

— Daniel
Scale SD
```

---

### TOUCH 3 — Day 5, SMS *(if still no reply)*

```
{{first_name}} - Daniel. Don't wanna be annoying but those 3 things are just sitting there. Wanna hear them or should I let it go? STOP to opt out.
```

~150 chars. Escalates soft urgency + gives them an out.

---

### TOUCH 4 — Day 8, Email *(if still no reply)*

**Subject:** `closing the loop`

**Body:**
```
{{first_name}},

Don't wanna be a hassle — if hearing the 3 things the top SD contractors are doing differently sounds worth 30 sec, just reply "yes."

If not, all good, I'll leave you be.

— Daniel
```

Near-verbatim Pavel message 2 structure.

---

### TOUCH 5 — Day 12, Email (soft breakup)

**Subject:** `last one from me`

**Body:**
```
{{first_name}},

Last ping. If the 3 things sound worth hearing, reply and I'll send them over.

Otherwise I'll move on.

— Daniel
```

---

### ~~TOUCH 6~~ — DROPPED for v1

**Decision:** Touch 6 SMS (Day 21 resurrection ping) removed from the sequence.

**Reason:** 3 SMS to a cold scraped number is on the higher-risk side of TCPA exposure. Late-sequence SMS also has the lowest reply rate. Tradeoff of ~5–10% of late replies is worth the reduced legal risk + cleaner sender reputation on the A2P number.

**May reintroduce in v2** if:
- List has been DNC-scrubbed
- Touches 1–5 show reply rates supporting a resurrection attempt
- A2P sender reputation is clean after 4 weeks of sending

Sequence is now **5 touches over 12 days** (Day 0, 2, 5, 8, 12) + Touch 1.5 auto-reply.

---

## 4. Workflow Structure (GHL)

**Main Workflow:** `CO-v1 — 700 Cold Contractors`
**Trigger:** Contact tag added = `cold-outbound-v1`

Three architectural nodes at the top control the entire workflow:
1. **Business Hours Gate** — blocks all downstream sends outside Tue–Fri 9am–5pm PT
2. **Drip Mode** — native GHL throttling, 25–150 contacts/day ramp
3. **3-way reply condition** at each wait step — Positive / Negative / None

```
1. Business Hours Filter: Only run Tue–Fri, 9am–5pm PT
   (TCPA-safe + no Mon/weekend sends — governs ALL downstream actions)

2. Drip Mode: [25 → 50 → 100 → 150] contacts per day (weekly ramp)
   (native GHL node — replaces manual tag-batching)

3. Send SMS: Touch 1 (Pavel hook)
4. Set field: last_touch_type = "sms"
5. Wait: 2 days

6. Condition (3-way inline branch on Touch 1 reply):
   ├─ "Positive" — Replied message contains positive keywords:
   │                "yes", "yeah", "yep", "sure", "ok", "send it", "send",
   │                "show me", "let's hear it", "hit me", "lmk", "share", "go"
   │     → Trigger sub-workflow: "CO-v1 — Touch 1.5 Auto-Reply" (sends 3 observations via SMS)
   │     → Add tag: reply-positive
   │     → Internal notification to setter
   │     → Move to pipeline stage: "Positive Reply"
   │     → Remove from main workflow
   │     → END (setter takes over conversation)
   │
   ├─ "Negative" — Replied message contains negative keywords (see list below)
   │     → Add tag: reply-negative + do-not-contact
   │     → Move to pipeline stage: "Closed Lost / DQ"
   │     → END
   │
   └─ "None" — No reply received
         → Send Email: Touch 2 (no link)
         → Set field: last_touch_type = "email"
         → Continue to step 7

7. Wait: 3 days
8. Condition (same 3-way branch on Touch 2 reply)
   └─ None → Send SMS: Touch 3 → step 9

9. Wait: 3 days
10. Condition (same 3-way branch)
    └─ None → Send Email: Touch 4 → step 11

11. Wait: 4 days
12. Condition (same 3-way branch)
    └─ None → Send Email: Touch 5 (Breakup) → step 13

13. (Touch 6 dropped — sequence ends after Touch 5)

14. Move to pipeline stage: "Nurture"
15. Remove tag: cold-outbound-v1
16. Add tag: nurture-90d
```

---

### Sub-Workflow: `CO-v1 — Touch 1.5 Auto-Reply`

**Trigger:** Called by main workflow when positive reply detected
**Purpose:** Auto-send the 3 observations via SMS (not email — protects domain warmup)

```
1. Send SMS: Touch 1.5 (3 observations text — see Section 3)
2. Set field: touch_1.5_sent = true
3. END (main workflow also routes to setter at this point)
```

**Why SMS not email:** Protects `s.scalehere.com` Stage 1 warmup. Zero links ever touch the email domain in this campaign. Reintroduce in-thread email links in Campaign v2 once domain is warmed to Stage 3+.

---

### Positive Keyword List (triggers Touch 1.5)

```
yes | yeah | yep | yup | sure | ok | okay | send it | send | show me |
let's hear it | hit me | lmk | share | spill | go | shoot | please |
interested | tell me | what are they
```

### Negative Keyword List (ends sequence, adds DNC tag)

```
stop | not interested | remove | remove me | no thanks | no thank you |
unsubscribe | go away | f off | fuck off | don't | do not | never |
wrong number | wrong person | leave me alone | fuck you | stfu
```

**Why inline branching instead of a separate reply workflow:**
Checking reply intent at each wait step (vs. a parallel listener) keeps state simpler, bails faster on negatives, and lets the positive branch immediately trigger Touch 1.5 without race conditions. The standalone Email Reply Handler (Section 6) covers email-specific edge cases (OOO auto-replies, forwards).

---

## 5. Warmup-Safe Send Pacing (Native Drip Mode)

`s.scalehere.com` is Stage 1 warmup. Blasting 700 torches the domain.

**Execution — use GHL's native Drip Mode node (top of workflow, step 2):**

| Week | Drip Mode Setting | Daily Entry | Running Total in Sequence |
|---|---|---|---|
| 1 | **25 contacts/day** | 25 enter workflow | 125 |
| 2 | **50 contacts/day** | 50 enter | 375 |
| 3 | **100 contacts/day** | 100 enter | 675 |
| 4 | **150 contacts/day** | 25 remaining | 700 (complete) |

**Operational steps:**
1. Import all 700 contacts with tag `cold-outbound-v1` applied at once (no manual batching).
2. Drip Mode node throttles entry — GHL holds excess contacts in queue automatically.
3. Every Monday, bump the Drip Mode number to the next tier in the workflow settings.
4. Send-time spreading within each day: Business Hours Filter (step 1) already clamps 9am–5pm PT. GHL distributes sends across that window automatically.

**Note vs. previous version:** Earlier draft used manual tag-batching (applying `cold-outbound-v1` in daily waves). Drip Mode replaces that entirely — cleaner, fewer moving parts, less room for human error.

### Deliverability guardrails (check daily)

| Metric | Target | Action if breached |
|---|---|---|
| Open rate | >30% | If <20%, pause + review subject lines |
| Reply rate | >3% | If <1%, copy is off — iterate |
| Bounce rate | <3% | If >3%, PAUSE, re-validate list |
| Unsubscribe rate | <0.5% | If >1%, copy too aggressive |
| SMS delivery | >95% | If <90%, carrier issue — check A2P |

---

## 6. Reply-Handling Workflow (Email Only)

> SMS reply branching is handled **inline** in the main workflow (Section 4). This reply handler covers **email replies only** — they need richer classification (OOO auto-replies, bounce messages, forwarded threads) than simple keyword matching can handle.

**Workflow:** `CO-v1 — Email Reply Handler`
**Trigger:** Inbound email received AND contact has tag `cold-outbound-v1`

```
1. Remove contact from main sequence workflow (stops further touches)
2. If/Else: email body contains auto-reply keywords
   ("out of office", "on vacation", "away until", "auto-reply")
   → Add tag: reply-ooo
   → Snooze 14 days → re-add tag: cold-outbound-v1 → END
3. If/Else: email body contains negative keywords (see Section 4 list)
   → Add tag: reply-negative + do-not-contact
   → Move to pipeline stage: "Closed Lost / DQ"
   → END
4. Default (positive or question):
   → Add tag: reply-positive (setter re-classifies if needed)
   → Internal notification to setter (SMS + email w/ conversation link)
   → Create task: "Review and respond — {{first_name}}"
   → Move to pipeline stage: "Positive Reply"
```

### Manual setter process (for positive replies)

1. Read reply → confirm intent
2. Re-tag if needed: `reply-question` for questions requiring an answer before booking
3. Respond per intent:
   - **Positive** → reply with calendar link → move to "Call Booked" on booking
   - **Question** → answer + soft CTA to call
   - **OOO** (missed by auto-detection) → tag `reply-ooo`, snooze 14 days

---

## 7. Calendar + Confirmation

**Calendar:** `Discovery Call – Daniel` (15 min)
**Availability:** **Mon–Sun, 8am–8pm PT** (wide availability — maximize booking capture)

> Note: This expands from the earlier 10 hrs/week calling window. Tradeoff: more bookings captured vs. more of Daniel's time gated. If booking volume overwhelms, narrow back in v2.

**Booking form fields:**
- First name (prefill)
- Last name (prefill)
- Phone (prefill)
- Email (prefill)
- "What's the #1 bottleneck right now?" (open text)

### Appointment Confirmed workflow
- **Immediate:** Email confirm w/ calendar invite + Zoom link
- **Immediate:** SMS "Daniel here — booked for {{appt_date}} at {{appt_time}}. Text me back with one thing you want to solve and I'll come prepped."
- **T-24h:** SMS reminder
- **T-1h:** SMS reminder + Zoom link
- **T-5min:** SMS "Jumping on — {{link}}"

(This is the seed for future Campaign #5 — Appt Confirmation + Reminders.)

---

## 8. Compliance

### CAN-SPAM (email)
- Physical mailing address in footer ✓ (need from you)
- Unsubscribe link (GHL auto-includes)
- Accurate "From" name + domain
- No deceptive subject lines
- Honor unsubscribes within 10 days (GHL automatic)

### TCPA (SMS)
- "Reply STOP to opt out" in every first SMS ✓
- Honor STOP within 10 min (GHL automatic)
- No SMS before 8am or after 9pm contact local time ✓
- Scrub against DNC registry before send
- Keep opt-out records 5 years

### Risk note — scraped list + SMS
B2B-to-business-mobile is defensible if:
1. Number is publicly listed as business contact (your scrape source does this)
2. Opt-out honored immediately
3. Reasonable cadence (not spamming)

Violations are $500–$1,500/message. Mitigations:
- DNC scrub before import
- Consider dropping Touch 6 (reduces SMS count from 3 → 2 per lead)
- Never send SMS to a number that's opted out at any point

---

## 9. KPIs

### Weekly dashboard

| Metric | Source |
|---|---|
| Leads entered sequence | Tag count |
| Email sent / open / reply / bounce / unsub | GHL email report |
| SMS sent / delivered / reply / opt-out | GHL SMS report |
| Positive replies | Tag `reply-positive` count |
| Calls booked | Pipeline stage 4 |
| Calls showed | Pipeline stage 5 |
| Closes | Pipeline stage 6 |
| MRR booked | Sum of signed deals |

### v1 baseline funnel (research-backed, 2025/2026 benchmarks)

Sources: Instantly Cold Email Benchmark Report 2026, Snov.io 2026, DigitalBloom 2025, Prospeo SMS 2026.

```
700 leads
  → ~5% reply rate              = 35 replies
  → ~40% positive intent        = 14 conversations
  → ~50% book                   = 7 discovery calls
  → ~60% show                   = 4 showed
  → ~30% close                  = 1–2 clients
  → $1,500–$4,000 new MRR
```

Note: Earlier draft estimated 3% reply / 8 booked. Updated after research — realistic cold B2B benchmarks (not guru-claimed) land at ~3.4% average, top-quartile ~10%. The Pavel-style reciprocity hook should trend toward top-quartile but we budget conservatively at 5%.

If v1 hits or beats this, v2 = niche-split + iterated observations → target 7–10% reply rate.

---

## 10. Launch Sequence (Day-by-Day)

### Day 1 — Build
- [ ] Clean CSV (dedupe, E.164 format phone, ZeroBounce email validation)
- [ ] DNC scrub on phone numbers (reduces TCPA risk)
- [ ] Create pipeline + 8 stages
- [ ] Create custom fields (see Section 1)
- [ ] Build 2 SMS templates (Touches 1, 3) + Touch 1.5 auto-reply SMS
- [ ] Build 3 email templates (Touches 2, 4, 5) — NO LINKS in any
- [ ] Build main workflow (`CO-v1 — 700 Cold Contractors`) with Business Hours Gate + Drip Mode + inline 3-way branching
- [ ] Build sub-workflow (`CO-v1 — Touch 1.5 Auto-Reply`)
- [ ] Build email reply handler workflow (`CO-v1 — Email Reply Handler`)
- [ ] Build appt-confirmed workflow
- [ ] Create Daniel's discovery call calendar

### Day 2 — Test
- [ ] Add Daniel's own email + phone as a test contact
- [ ] Apply `cold-outbound-v1` tag on test contact → verify all 6 touches fire on compressed timeline
- [ ] Test positive-reply path: reply "yes" → verify Touch 1.5 auto-reply fires with 3 observations
- [ ] Test negative-reply path: reply "not interested" → verify DNC tag + end
- [ ] Test STOP: reply STOP → verify GHL opt-out carrier-level
- [ ] Test calendar booking → verify confirmation sequence fires

### Day 3 — Soft launch
- [ ] Import full 700 CSV with `cold-outbound-v1` tag applied (Drip Mode handles pacing)
- [ ] Confirm Drip Mode is set to 25/day for Week 1
- [ ] Monitor first 25 sends hourly for first 4 hours
- [ ] Watch bounce rate — if >3%, PAUSE and clean list

### Day 4+ — Ramp
- [ ] Every Monday, bump Drip Mode: Week 2 = 50/day, Week 3 = 100/day, Week 4 = 150/day
- [ ] Daily deliverability check against Section 5 guardrails
- [ ] Weekly KPI review

---

## Decisions Still Open

**None. Spec is build-ready.**

## Decisions Locked In

- ✅ Artifact approach: inline text 3-observations, no landing page, no PDF
- ✅ Hook style: Pavel-reciprocity, "wanna hear them?"
- ✅ Channel order: SMS-first (Touch 1), email in-between
- ✅ Link policy: ZERO links in cold emails. Touch 1.5 is SMS-only.
- ✅ Drip Mode pacing: 25 → 50 → 100 → 150 per day
- ✅ Business Hours Gate at top of workflow: Tue–Fri 9am–5pm PT
- ✅ Inline 3-way reply branching at each step (no separate reply workflow for SMS)
- ✅ Timezone: San Diego only → all times PT
- ✅ **Touch 1.5 observations approved** (review gating / reels→paid ads / <5 min response)
- ✅ **Calendar window: Mon–Sun 8am–8pm PT** (wide-open booking availability)
- ✅ **Setter assignment: all 4 team members** — notifications broadcast to Daniel + Ashane + Tad + Justin via GHL internal notification (first to respond claims the lead)
- ✅ **Touch 6 dropped** for v1 — TCPA safety, may reintroduce in v2
- ✅ **Physical mailing address:** 345 E Park Ave, Escondido, CA 92025

---

## Next Campaigns (Post-#1)

Once Campaign #1 is live and ramped:
- **#2 Speed-to-Lead** — reuses email/SMS infrastructure, ~1 hour to build
- **#3 Missed Call Text-Back** — ~1 hour to build
- **#5 Appt Confirmation** — already seeded in Section 7, formalize as standalone
- **#4 Nurture** — for the `nurture-90d` bucket that Campaign #1 produces

See `/scale-business/campaigns/` for specs as they're built.
