---
title: "Campaign Metrics — What to Track and Report"
type: concept
tags: [metrics, kpis, cpl, cpa, cac, roas, reporting]
sources: [1-17m-year-facebook-ads-strategy, do-facebook-ads-work-home-service-companies]
updated: 2026-04-11
---

# Campaign Metrics — What to Track and Report

The right metrics to evaluate Facebook ad campaign performance for home service clients. CPL alone is a vanity metric. These are the metrics that actually matter.

---

## The Three Metrics (In Order of Importance)

### 1. Cost Per Lead (CPL)
**Role**: Sanity check and directional signal. Not a decision metric on its own.

**Why it's insufficient alone**:
- A $3 CPL from a messaging campaign is terrible (low intent, pixel trains wrong)
- A $65 CPL from a lead form with friction may generate better CAC than a $15 CPL with no friction
- CPL varies 10x between platforms, campaign types, and verticals

**Useful for**: Spotting when something is deeply wrong (CPL of $200+) or as input to the math below.

---

### 2. Cost Per Appointment / Booked Quote (CPA)
**Role**: First real signal that the campaign is generating qualified interest.

**Formula**:
```
CPA = Total spend ÷ number of booked appointments
```

**Example**:
- Spend: $2,500
- Leads: 100 (CPL = $25)
- Booked appointments: 20 (lead-to-appt rate = 20%)
- **CPA = $125**

**Benchmark**: Lead-to-appointment rate of 15–25% is reasonable for Facebook leads. Below 10% = either lead quality problem or speed-to-lead problem.

---

### 3. Customer Acquisition Cost (CAC)
**Role**: The metric that determines if the campaign is profitable.

**Formula**:
```
CAC = Total spend ÷ number of closed jobs
```

**Example**:
- From 20 appointments → 5 closed jobs (25% close rate)
- Spend: $2,500
- **CAC = $500**

---

## Full Marketing Math (6x ROAS Example)

```
Spend:          $2,500
Leads:          100        → CPL = $25
Booked:         20 (20%)   → CPA = $125
Closed:         5 (25%)    → CAC = $500
Avg ticket:     $3,000
Revenue:        $15,000
ROAS:           6x
```

You gave Meta $1, they returned $6 in revenue. That's a profitable campaign regardless of what the CPL looks like.

---

## ROAS Target Benchmarks

| Average Ticket | Acceptable CAC | Target ROAS |
|---|---|---|
| $100–300 (pressure wash, gutter clean) | $20–60 | 5–10x |
| $300–1,000 (HVAC tune-up, plumbing repair) | $50–150 | 4–8x |
| $1,000–5,000 (AC replacement, remodel phase) | $100–500 | 3–6x |
| $5,000–50,000 (pools, solar, ADU, full remodel) | $200–2,000 | 3–10x |

*Benchmarks estimated based on typical home service margins. Verify against client data.*

---

## LTV Adjustment for Recurring Services

For recurring/subscription businesses (pest control, pool service, window cleaning plans, lawn care), month-1 revenue doesn't tell the whole story.

**Calculate LTV first**:
```
LTV = Average monthly revenue × average customer lifespan (months)
```

Example: Pest control at $70/month × 36 months = $2,520 LTV
→ Acceptable CAC might be $200–400 (not $70)

**Don't declare a campaign unprofitable** if month-1 CAC exceeds first-job revenue on a recurring business.

---

## CPL Benchmarks by Vertical (Facebook)

From [[concepts/cost-per-lead]]:

| Vertical | Facebook CPL |
|---|---|
| HVAC | $40–$70 |
| Plumbing | $35–$60 |
| Electrical | $30–$55 |
| Landscaping | $25–$45 |
| Tree Service | $30–$55 |

These are agency-run benchmarks (WatsonCo). Self-managed accounts may differ.

---

## Reporting Template for Clients

Weekly report should include:
- Spend
- Leads generated + CPL
- Leads contacted (speed-to-lead compliance check)
- Booked appointments + CPA
- Closed jobs + CAC (where available — may lag 2–8 weeks)
- ROAS (where revenue data available)

---

## Sources

- [[sources/1-17m-year-facebook-ads-strategy]] — full math breakdown, CPL as vanity metric
- [[sources/do-facebook-ads-work-home-service-companies]] — CPL benchmarks by vertical
