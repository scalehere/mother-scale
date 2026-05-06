---
title: GHL AI Automation Builder
type: concept
tags: [ghl, automation, ai, natural-language, workflow]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-automation-builder-intro]
---

# GHL AI Automation Builder

A natural-language interface inside [[GoHighLevel]] for generating complete automation workflows from plain-language prompts. Builds on the [[GHL Advanced Automation Builder]] canvas.

## How It Works

1. Click "Build using AI" inside the automation editor
2. Describe what you want in plain language (e.g., "build an SMS + email + WhatsApp follow-up sequence for new leads from Facebook forms")
3. GHL generates the full workflow — triggers, actions, delays, AND all copy (email subject/body, SMS text, etc.)
4. Iterate via follow-up prompts: "change all emails to SMS", "make it Christmas-themed", "add a split test"

**Key insight from source:** AI amplifies existing knowledge — it cannot compensate for not understanding what you're asking it to build. A user who doesn't understand triggers/actions will get a plausible-looking but functionally wrong automation. Foundation first.

## Entry Points (3)

1. **Workflow list page** — Automation → Workflows → "Build using AI" button
2. **Inside workflow builder** — create new workflow from scratch → AI prompt box is present
3. **AI Chatbot Assistant** — inside any workflow builder session

## Enabling

If the "Build using AI" button is missing from the automation editor: Settings → Labs → enable AI Automation Builder.

## Generation Speed & Autosave

- Generates in **under 30 seconds** on average (improved from ~60s). If longer, simplify prompt.
- **Autosave is on by default** for AI-generated workflows — saves on creation and on every AI edit.

## Demonstrated Capabilities

- Generate multi-channel sequences (SMS + email + WhatsApp) from a one-line prompt
- Theme existing sequences ("make it Christmas promo themed")
- Swap action types ("change all emails to SMS") across an entire workflow in one pass
- Write full email/SMS copy as part of generation
- Generate complex sequences with wait periods and repeat logic (e.g., "send review request on email + SMS → wait 1 hour → repeat")
- Speed: complete workflow generation in seconds

## AI Assistant Sidebar (8 Panels)

Inside the automation editor, a separate AI assistant panel provides:
1. Ask questions / guidance on building workflows
2. Assist with building
3. Add an action
4. Configure action
5. Suggest next steps / improvements
6. Improve/optimize the current workflow
7. Describe the current workflow
8. Link to support articles

The AI builder (prompt-to-workflow) is the real power feature; the sidebar is supplementary.

## Relationships

- Requires understanding of [[GHL Automation Builder (Basic)]] and [[GHL Advanced Automation Builder]] to use effectively
- Generates workflows on the [[GHL Advanced Automation Builder]] canvas
- Part of [[GoHighLevel]]'s three-tier automation system

## Point and Edit (Official Feature)

For large workflows where verbal descriptions of "which action" are ambiguous:
1. Click to select specific action(s) on the workflow canvas
2. Describe the change in the chat — AI applies it only to the selected step(s)
- Works for single, multiple, or drag-selected actions
- Example: select 3 email actions → "Change all these to SMS"
- Best for: workflows with 10+ actions or multiple branches

## Chat Mode (Official Feature)

Plan before building — brainstorm with AI without committing changes:
1. Toggle "Chat Mode" on
2. Discuss triggers, actions, branches, timing freely
3. When the plan is finalized, toggle Chat Mode off → ask AI to build it

## Conversational Editing Scope (Official)

After generation, the AI can edit:
- **Actions:** add, remove, replace, modify, move
- **Triggers:** add, remove, replace, modify
- **If/Else branches:** update conditions, AND/OR operators, add/remove branches
- **Wait steps:** duration, reply/window settings, timeout branches, wait type
- **Multi-change:** combine multiple changes in one prompt

## Prompt Best Practices (Official)

- Be specific — include timing, channels, conditions, content type
- Use action verbs: *Send, Notify, Create, Update, Wait, Check if*
- Good example: "When a contact books an appointment, wait 24 hours, then send a confirmation email and a reminder SMS one day before the appointment"

## Beta Limitations

- Manual review required before publishing — AI can't guarantee correct config
- AI cannot test workflows — always test manually with a live contact
- Some complex configs need manual adjustment after generation

## Open Questions

- What models/providers does GHL use internally for this feature?
- Is Point and Edit available on mobile?
