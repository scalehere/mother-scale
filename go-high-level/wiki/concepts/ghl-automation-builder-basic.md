---
title: GHL Automation Builder (Basic)
type: concept
tags: [ghl, automation, workflow, trigger, action]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-automation-builder-intro]
---

# GHL Automation Builder (Basic)

The standard workflow editor in [[GoHighLevel]]. The entry point for building automations — linear, single-trigger, sequential action chains.

## How It Works

Every automation follows the same structure:
```
[Trigger] → [Action 1] → [Wait?] → [Action 2] → ...
```

**Trigger** — the event that starts the automation. Examples: form submitted, contact created, appointment booked, tag added, payment received. Only one trigger per workflow in the basic builder.

**Actions** — everything that happens after. Can include: send email, send SMS, create contact, add tag, call webhook, wait (time delay), add to calendar, and many others.

**Key settings:**
- Set default sender name/number in workflow Settings to avoid re-entering per action (pro tip)
- Always test before publishing
- Publish = make live; Save = draft

## Examples & Evidence

- Form submitted → send confirmation email → wait 1 min → send SMS follow-up
- Lead created from Facebook → assign to rep → send welcome sequence

## Relationships

- Part of [[GoHighLevel]]'s three-tier automation system
- Prerequisite for [[GHL Advanced Automation Builder]] and [[GHL AI Automation Builder]]
- [[Automation Trigger]] and [[Automation Action]] are the building blocks

## Open Questions

- What is the full list of available triggers?
- Are there limits on number of actions per workflow?
