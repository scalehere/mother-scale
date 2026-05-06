---
title: "Workflow AI Builder: Generate and Edit Workflows with AI"
type: source
tags: [ghl, ai, workflow, official-docs, point-and-edit, chat-mode]
created: 2026-04-12
updated: 2026-04-12
---

# Workflow AI Builder: Generate and Edit Workflows with AI

- **Type:** Official GHL help documentation
- **Author:** HighLevel (no individual author)
- **Source:** help.gohighlevel.com/support/solutions/articles/155000006100
- **Published:** (undated — official docs, most recent AI builder reference)
- **Ingested:** 2026-04-12
- **File:** `raw/articles/Workflow AI Builder Generate and Edit Workflows with AI.md`

## Summary

The definitive official reference for GHL's Workflow AI Builder. Covers all three entry points, the full build → review → edit cycle, two advanced editing features (Point and Edit, Chat Mode), prompt best practices, beta limitations, and troubleshooting. Most authoritative source on the AI builder in the wiki.

## Key Takeaways

**Three entry points:**
1. Automation → Workflows list page → "Build using AI" button
2. Inside Workflow Builder (new workflow from scratch) → AI prompt box
3. Inside Workflow Builder → AI Chatbot Assistant panel

**Generation speed:** Under 30 seconds on average (improved from ~60s). If it takes longer, simplify the prompt and try again.

**Autosave:** AI-generated workflows autosave the moment they're created, and every subsequent AI edit autosaves.

**Full build cycle:** Prompt → Generate → Review (structure, trigger config, action settings) → Edit via AI conversation

**Conversational editing — what you can edit:**
- **Actions:** add, remove, replace, modify, move
- **Triggers:** add, remove, replace, modify
- **If/Else:** update branch logic, change AND/OR operators, add/remove branches
- **Wait steps:** update wait duration, reply/window settings, add/remove timeout branches, change wait type
- **Multi-change prompts:** combine multiple changes in a single message

**Point and Edit (key feature for large workflows):**
- Click to select specific action(s) in the workflow canvas
- Then describe the change in chat → AI applies it only to the selected steps
- Supports single, multiple, or drag-selected actions
- Best for: workflows with 10+ actions, multiple branches, or where verbal descriptions of "which action" would be ambiguous
- Example: select 3 email actions → "Change all these to SMS"

**Chat Mode:**
- Enables brainstorming without building — plan with AI before committing
- Toggle "Chat Mode" on → discuss triggers, actions, branches, timing freely
- When plan is finalized → toggle Chat Mode off → ask AI to build it
- Useful for complex workflows where you want to think through logic before generating

**Prompt best practices:**
- Be specific: include timing, channels, conditions/filters, content type
- Use action verbs: *Send, Notify, Create, Update, Wait, Check if*
- Good example: "When a contact books an appointment, wait 24 hours, then send a confirmation email and a reminder SMS one day before the appointment"
- Example prompts: "Send a welcome email series when someone fills out my contact form", "Create a birthday reminder workflow that sends SMS greetings", "Notify my team on Slack when a high-value opportunity is created", "Follow up with webinar attendees 24 hours after the event"

**Beta limitations:**
- Manual review required before publishing — verify triggers, actions, configs
- AI cannot test workflows — manual testing required
- Some complex configurations may need manual adjustment

**Troubleshooting:**
- Refine prompt / split complex goals into smaller parts
- Wrong trigger → specify exact trigger type in prompt or edit via AI
- Missing actions → list desired actions explicitly
- Incorrect timing → use precise time references ("after 2 days" not "soon")

## Entities Mentioned

- [[GoHighLevel]]

## Concepts Mentioned

- [[GHL AI Automation Builder]]
- [[Automation Trigger]]
- [[Automation Action]]
- [[GHL If/Else Branching]]

## Contradictions & Tensions

**Updates existing wiki knowledge:**
- Confirms 3 entry points (wiki had 2 from video sources — now confirmed plus a third)
- Generation speed: <30 seconds average (not mentioned in video sources)
- Autosave: not previously documented
- Point and Edit: entirely new feature, not in any video source
- Chat Mode: entirely new feature, not in any video source
- Conversational If/Else and Wait editing: not previously documented

## Notes

Highest-authority source on the AI builder in the wiki. Official GHL documentation. Should supersede video-source descriptions of the AI builder where they conflict.
