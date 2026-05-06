---
title: GHL Workflow Chaining
type: concept
tags: [ghl, automation, workflow, pipeline, advanced]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-getting-started-workflows]
---

# GHL Workflow Chaining

A pattern for building multi-stage automation in [[GoHighLevel]] by connecting multiple workflows together — one per stage of a sales pipeline or process.

## The Pattern

**One workflow per pipeline stage.** When a contact advances to the next stage:
1. The new stage's workflow **removes the contact from the previous workflow** (prevents stale actions from firing out of turn)
2. Updates the **opportunity stage** in the pipeline
3. Triggers the **next stage's workflow**

## Example: Lead → Booking → Pitch → Contract

```
Workflow A (Lead)         → books → removes from A, moves opp to "Booking", adds to B
Workflow B (Booking)      → pitched → removes from B, moves opp to "Pitch", adds to C
Workflow C (Pitch)        → signed → removes from C, moves opp to "Contract", adds to D
Workflow D (Contract)     → onboard
Workflow E (Onboarding)   → ...
```

## Why Chain Instead of One Big Workflow

- Easier to manage and troubleshoot — each stage is isolated
- Clean handoffs — removing from previous workflow prevents duplicate or irrelevant actions
- Modular — can edit one stage without touching others

## Key Action: "Remove from Workflow"

The `Remove from Workflow` action in [[Automation Action]] is what makes chaining work — it pulls the contact out of the current workflow before adding them to the next.

## Relationships

- [[Automation Action]] — "Add to Workflow" and "Remove from Workflow" actions enable this pattern
- [[GHL Pipeline Automation]] — chaining is how you automate a full pipeline
- [[GHL Automation Builder (Basic)]] / [[GHL Advanced Automation Builder]]

## Open Questions

- Is there a visual way to see all chained workflows and their connections in GHL?
