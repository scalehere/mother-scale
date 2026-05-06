---
title: Automation Trigger
type: concept
tags: [ghl, automation, workflow, fundamentals]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-automation-builder-intro]
---

# Automation Trigger

The opening event of an automation workflow. The trigger is what causes the workflow to start — nothing happens until the trigger fires.

## How It Works

In [[GoHighLevel]], every workflow begins with at least one trigger. When the triggering condition is met, the workflow activates and executes its [[Automation Action|actions]] in sequence.

**Full trigger categories (from [[sources/ghl-workflows-tutorial-2026|Workflows Tutorial 2026]]):**

- **Contact:** birthday reminder, contact changed/created, contact DND, tag added/removed, custom date reminder, note added/changed, task added/reminder/completed, engagement score
- **Events:** inbound webhook (premium), call status, email events, customer replied, conversational AI trigger, custom trigger, form submitted, survey submitted, trigger link clicked, Facebook lead form, TikTok form, video tracking, number validation, messaging error, LinkedIn lead form, funnel/website page view, quiz submitted, new review received, prospect generated, Click-to-WhatsApp ads, internal tracking event
- **Appointments:** appointment status, show/no-show, customer booked appointment, service booking, rental booking
- **Opportunities:** status changed, opportunity created, pipeline stage changed, stale opportunities
- **Affiliates:** affiliate created, new affiliate sale, enrolled in campaign, lead created
- **Courses:** category/lesson started/completed, new signup, offer granted/removed, product access changes, user login
- **Payments:** invoice event, payment received, order form submission, documents/contracts, estimates, subscription, refund, coupon events (applied, limit reached, expired, redeemed)
- **E-commerce:** Shopify order placed/fulfilled (abandoned cart being deprecated), product review submitted, abandoned checkout
- **IVR:** IVR start
- **Social (FB/IG):** comment on post, DM received
- **Communities:** group access granted/revoked, private channel access, leaderboard
- **Certificates:** certificate issued
- **Google Ads:** Google Ads event

**Filters:** Every trigger supports filters (e.g., "form submitted" → filter to a specific form). This is how you scope triggers precisely.

**Premium triggers:** Inbound webhook is premium (costs extra). Look for the crown icon.

In the [[GHL Automation Builder (Basic)]], there is one trigger per workflow. In the [[GHL Advanced Automation Builder]], multiple triggers can feed into a single workflow.

## Relationships

- Paired with [[Automation Action]] — trigger starts, actions execute
- Fundamental building block of [[GHL Automation Builder (Basic)]]
