---
title: Automation Action
type: concept
tags: [ghl, automation, workflow, fundamentals]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-automation-builder-intro]
---

# Automation Action

The steps that execute after a workflow is triggered. Actions define what the automation actually does.

## How It Works

In [[GoHighLevel]], actions are chained sequentially after the [[Automation Trigger]]. Multiple actions can be stacked, with optional Wait steps between them.

**Full action categories (from [[sources/ghl-workflows-tutorial-2026|Workflows Tutorial 2026]]):**

- **Contact:** create, find, update field, add/remove tag, assign/remove user, enable/disable DND, add notes, copy contact, edit conversation, add task, delete contact, modify engagement score, add/remove followers
- **Custom Objects:** create/update/clear associated records, add/remove from workflow
- **Communication (heavy hitters):** send email, send SMS, Slack, call, voicemail drop, Messenger, Instagram DM, manual SMS/call action, send internal notification, send review request, conversational AI, Facebook/Instagram reply to comment, WhatsApp (service, flows, live chat, media, interactive), appointment booking AI, TikTok interactive messenger
- **Send Data (premium):** Zapier webhook, custom webhook, Google Sheets
- **Internal Logic:** if/else branching, wait step, goal event, A/B split test, update custom value, go-to (loop), date/time formatter, math operations, lead scoring, set events, start date, add/remove from workflow, array functions, drip text, custom code
- **AI (external legacy):** ChatGPT integration (mostly superseded by native AI)
- **Appointments:** update appointment status, create appointment, booking note, generate one-time booking link
- **Opportunities:** create/update/remove opportunity, add/remove owner, add/remove followers, find opportunity
- **Payments:** Stripe one-time charge, send invoice/estimate/document/contract/recurring invoice
- **Marketing:** Add to Google Analytics/Ads, Facebook Custom Audience add/remove, Meta Conversation API, generate marketing audit report
- **Affiliates:** add to manager, update affiliate, add/remove from campaign, add leads, manual sales
- **Memberships/Courses:** grant/revoke course offer
- **IVR:** gather input on call, play message, contact call, call record voicemail
- **Agent Studio:** AI translate, AI summarize, AI intent detection, AI decision maker
- **Communities:** smart push notification, grant/revoke group access, private channel access, leaderboard points
- **Conversation AI (chatbot):** AI capture info, AI book appointment, AI splitter, AI message, custom message, transfer bot, continue conversation
- **Voice (inbound AI):** AI voice agent call

**Premium actions:** Marked with crown icon — third-party integrations (Zapier, webhooks, Google Sheets) cost extra.

**If/Else branching** enables conditional paths — actions can split into different sequences based on contact data or response.

## Relationships

- Follows [[Automation Trigger]] — trigger fires, then actions execute
- Core building block of all three [[GoHighLevel]] automation builders
- If/else branching makes complex multi-path flows possible
