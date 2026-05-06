# Wiki Log

Append-only chronological record of all operations.
Parse last 10 entries: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-12] ingest | Batch — 5 sources from raw/articles/ (official docs & blog)

- Files ingested:
  - Did You Know Workflow AI Can Create Workflows For You Just Using Text?.md (GHL blog, Ryan Howell)
  - Getting Started with Workflows.md (Official GHL help doc)
  - GoHighLevel Workflows The Ultimate Guide to CRM Automation.md (Third-party, hireghldeveloper.com)
  - Introduction to Workflows and Automations in HighLevel.md (Official GHL help doc)
  - Workflow AI Builder Generate and Edit Workflows with AI.md (Official GHL help doc — definitive AI builder reference)
- Pages created: 5 source pages, 3 concept pages (ghl-workflow-recipes, ghl-workflow-chaining, ghl-workflow-troubleshooting), 2 entity pages (ryan-howell, hire-ghl-developer)
- Pages updated: ghl-ai-automation-builder.md (Point and Edit, Chat Mode, 3 entry points, autosave, <30s, prompt best practices, beta limitations), index.md, overview.md
- Key insights: (1) Official docs confirm Point and Edit and Chat Mode — entirely new AI builder features not in any video source; (2) Workflow chaining (one-workflow-per-pipeline-stage) is a key advanced pattern; (3) "Allow Reentry" setting is a common testing gotcha; (4) AI builder now averages <30s generation with autosave

---

## [2026-04-12] ingest | Batch — 5 sources from raw/articles/ (videos)

- Files ingested:
  - GoHighLevel AI Automations - Build Workflows Instantly & Save Hours.md
  - The Best GoHighLevel Workflows to Grow and Automate Your Social Media.md
  - GoHighLevel Workflows Tutorial 2026 (Beginner to Advanced).md
  - The Ultimate GoHighLevel Automations Tutorial 4+ HOUR FREE COURSE.md (partial — first ~700 lines; 4hr video)
  - GoHighLevel Tutorial Ultra In-Depth FREE COURSE.md (partial — first ~600 lines; platform overview)
- Pages created: 5 source pages, 5 new concept pages (ghl-social-media-automations, ghl-saas-configurator, ghl-agency-view, ghl-fast-five, missed-call-text-back)
- Pages updated: automation-trigger.md (full trigger reference), automation-action.md (full action reference), ghl-ai-automation-builder.md (Labs enable step + AI sidebar), go-high-level.md (pricing tiers, revenue model), overview.md (full synthesis), index.md
- Key insights: (1) Automations automate *other GHL features* — learn features first; (2) Social media automations replace ManyChat natively; (3) $497 plan unlocks SaaS Configurator and white-label reselling; (4) Field mapping is a common failure point for social lead forms
- Note: Two large files only partially read. Ultra In-Depth course has more subaccount tab content not yet ingested.

---

## [2026-04-12] ingest | Stop Wasting Hours! Master GHL Automations in 10 Minutes

- File: `raw/Stop Wasting Hours! Master GHL Automations in 10 Minutes.md`
- Pages created: sources/ghl-automation-builder-intro.md, entities/go-high-level.md, entities/ghl-wizard.md, concepts/ghl-automation-builder-basic.md, concepts/ghl-advanced-automation-builder.md, concepts/ghl-ai-automation-builder.md, concepts/automation-trigger.md, concepts/automation-action.md
- Pages updated: wiki/index.md, wiki/overview.md, wiki/log.md
- Key insight: GHL has a three-tier automation system (Basic → Advanced → AI); AI amplifies knowledge but can't replace foundational understanding

---

## [2026-04-12] schema-update | Initial Setup

- Action: Created wiki scaffold from LLM Wiki idea file
- Files created: CLAUDE.md, wiki/index.md, wiki/log.md, wiki/overview.md
- Directories: raw/{articles,papers,notes,data,assets}, wiki/{entities,concepts,sources,outputs}
- Status: Ready for first ingest
