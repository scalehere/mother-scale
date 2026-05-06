---
title: GHL Advanced Automation Builder
type: concept
tags: [ghl, automation, workflow, advanced, canvas]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-automation-builder-intro]
---

# GHL Advanced Automation Builder

A visual drag-and-drop automation canvas in [[GoHighLevel]], currently available via the Labs feature flag. Analogous to n8n or Make (Integromat) in interface style. Designed for complex, multi-path automation flows.

## How It Works

Same building blocks as the [[GHL Automation Builder (Basic)]] (triggers + actions), but with a fundamentally different interface and expanded capabilities:

- **Drag-and-drop canvas** — nodes can be repositioned freely; zoom in/out for overview
- **Multiple triggers** — a single workflow can have multiple independent trigger nodes feeding into shared action sequences
- **Multiple automation paths** — effectively multiple automations within one workflow
- **Keyboard shortcuts** — hotkeys for common operations (e.g., Shift+Cmd+S for stats view), speeding up navigation for power users

## Relationship to Basic Builder

- Same conceptual foundation; different execution surface
- Use Basic for simple linear flows; use Advanced when flows branch, have multiple entry points, or are large enough to benefit from a bird's-eye view

## Examples & Evidence

From source: a large Christmas-promo themed 21-day email sequence was built and modified via the AI builder on the Advanced canvas, demonstrating its capacity for complex multi-step sequences.

## Relationships

- Part of [[GoHighLevel]]'s three-tier system
- Prerequisite (conceptually) to [[GHL AI Automation Builder]] — AI builds on this canvas
- [[GHL Wizard]] recommends learning Basic first, then this

## Open Questions

- When will Advanced Builder exit Labs/become default?
- Are there limits on number of triggers per workflow?
- Full list of keyboard shortcuts?
