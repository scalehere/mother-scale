---
title: GHL Social Media Automations
type: concept
tags: [ghl, social-media, facebook, instagram, tiktok, linkedin, automation]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-social-media-workflows, ghl-workflows-tutorial-2026]
---

# GHL Social Media Automations

[[GoHighLevel]]'s suite of social media triggers and actions. Described by [[GHL Wizard]] as the most underrated feature in GHL — most people use ManyChat or similar tools when GHL can handle it natively.

## Comment Keyword Trigger → DM Workflow

The most powerful social media automation pattern:
1. **Trigger:** Someone comments a specific keyword on an Instagram or Facebook post
2. **Action 1:** Reply to the comment (publicly) — e.g., "I just sent you a DM!"
3. **Action 2:** Like the comment (boosts engagement, double-notifies user)
4. **Action 3:** Send a DM with offer/info

**Best practice:** Use a specific keyword (not "all comments") so you can direct it in content ("comment HAIRCUT for a free coupon"). Toggle "send only once per contact" to prevent duplicate sends.

**Escalation:** After DM is sent, enable [[GHL AI Chatbot]] to handle the conversation automatically — fully automated social sales funnel.

Works identically for Facebook (use Facebook Comment trigger + Messenger DM).

## Social Lead Form Automation

Triggers from ad platform lead forms across all four supported platforms:
- Facebook lead form submitted
- Instagram lead form submitted
- TikTok form submitted
- LinkedIn form submitted

**Critical step — Field Mapping:** Go to Settings → Integrations and map platform form fields to GHL contact fields. Mismatch = lost contact data. Most common beginner mistake.

**After trigger fires:** Create opportunity → add to pipeline → send SMS/email sequence → optionally hand off to AI chatbot.

## Recurring Review Post (Social Planner)

Not technically in the automation builder — accessed via Marketing → Social Planner → Post Reviews.
- Pulls 5-star Google/Facebook reviews
- Posts to social feeds + stories on a configurable schedule
- Takes ~2 minutes to set up, runs forever
- Useful as a "social media management" service to sell to clients

## Social Triggers (Full List)

From [[GHL Automation Builder (Basic)]]:
- Instagram comment on post
- Facebook comment on post
- Instagram DM received
- Facebook Messenger received

## Relationships

- [[Automation Trigger]] — social triggers are a subset
- [[GHL AI Chatbot]] — natural escalation after social DM
- [[Comment Keyword Trigger]] — specific trigger pattern
- [[GoHighLevel]]'s social planner (separate from automation builder)

## Open Questions

- Does the comment trigger work on Reels/Stories or only static posts?
- Is there a TikTok comment trigger (only seen TikTok form trigger)?
- Rate limits on automated DMs from ad platforms?
