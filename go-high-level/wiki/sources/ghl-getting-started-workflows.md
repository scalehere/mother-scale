---
title: "Getting Started with Workflows"
type: source
tags: [ghl, workflow, official-docs, beginner, recipes, troubleshooting]
created: 2026-04-12
updated: 2026-04-12
---

# Getting Started with Workflows

- **Type:** Official GHL help documentation
- **Author:** HighLevel (no individual author)
- **Source:** help.gohighlevel.com/support/solutions/articles/155000002288
- **Published:** (undated — official docs)
- **Ingested:** 2026-04-12
- **File:** `raw/articles/Getting Started with Workflows.md`

## Summary

Official GHL beginner's workflow guide. Covers: what workflows are, tasks worth automating, Workflow Recipes (pre-built templates), three-step creation process (trigger → filters → actions), advanced patterns (if/else, workflow chaining, webhooks), and a troubleshooting checklist. The most practical foundational reference in the wiki — official and undated (treated as evergreen).

## Key Takeaways

**Workflow Recipes:**
- GHL provides pre-built workflow templates called "Recipes" — accessible when creating a new workflow by selecting "Recipes" option
- Recommended for beginners: start with a recipe and edit it
- Reveals the most common use cases baked into the product

**Three-step creation process:**
1. Choose a trigger
2. Add trigger filters (optional but recommended — narrows scope, e.g., "call status" → filter to "inbound only, main number only")
3. Add workflow actions

**Tasks worth automating (official list):**
- Lead nurturing campaigns (email sequences by funnel stage)
- Appointment scheduling (direct booking + automated confirmation)
- Follow-up communications (triggered by page visits, download, etc.)
- Customer onboarding (welcome sequences, setup instructions)
- Feedback surveys (post-purchase or post-service)
- Lead scoring and segmentation
- Data entry / CRM updates (auto-capture from forms, third-party integrations)
- Event registration and follow-ups (webinars, workshops)
- Abandoned cart recovery

**Workflow chaining pattern:**
- Create one workflow per stage in a sales pipeline
- When a contact advances: new workflow removes contact from previous workflow (prevents stale actions) → updates opportunity stage → triggers next stage workflow
- Enables clean, maintainable multi-stage automation

**Webhooks:**
- Webhook trigger + action = connect non-GHL platforms to GHL
- Described as the key to "unlocking full power of workflows"
- Requires advanced knowledge — separate detailed guide exists

**Troubleshooting checklist (official):**
1. ✅ Test with a fresh contact (same contact re-used can cause unexpected results)
2. ✅ Test live — "Test Workflow" button has limitations; use real contact triggering live
3. ✅ Check trigger and action filters — over/under-broad filters are most common error
4. ✅ Check "Allow Reentry" in Workflow Settings — if disabled, same contact won't re-enter; easy to forget during testing

## Entities Mentioned

- [[GoHighLevel]]

## Concepts Mentioned

- [[GHL Automation Builder (Basic)]]
- [[Automation Trigger]]
- [[Automation Action]]
- [[GHL Workflow Recipes]]
- [[GHL If/Else Branching]]
- [[GHL Workflow Chaining]]
- [[GHL Webhooks]]
- [[GHL Workflow Settings]]

## Contradictions & Tensions

None. Adds: "Allow Reentry" setting — not mentioned in any video source. Important troubleshooting detail.

## Notes

Official GHL help documentation — highest authority source in the wiki. Undated but treated as current/evergreen. Links to detailed docs for each trigger and action exist at help.gohighlevel.com.
