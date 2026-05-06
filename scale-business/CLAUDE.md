# Wiki Schema — scale-business

This file is the authoritative schema for this LLM Wiki. Every Claude Code session
operating in this directory must read and follow these rules before doing anything else.

---

## Purpose

This wiki is a persistent, compounding second brain for **scale-business** — a domain
to be defined by the owner as sources are ingested. The LLM maintains all wiki files.
The human curates sources, directs analysis, and asks questions.

---

## Directory Layout

```
scale-business/
├── CLAUDE.md          ← this file; the schema (read first, every session)
├── raw/               ← immutable source documents (human drops files here)
│   ├── assets/        ← downloaded images referenced by raw sources
│   └── transcripts/   ← Fathom call transcripts (named YYYY-MM-DD_slug_type.md)
└── wiki/
    ├── index.md       ← catalog of all wiki pages (LLM keeps current)
    ├── log.md         ← append-only chronological record (LLM appends only)
    ├── overview.md    ← high-level synthesis of the whole wiki (LLM maintains)
    ├── sources/       ← one summary page per ingested source
    │   └── calls/     ← one summary page per ingested call transcript
    ├── entities/      ← pages for specific named things (people, companies, products)
    ├── concepts/      ← pages for ideas, frameworks, themes, terms
    └── analysis/      ← comparisons, syntheses, explorations, output formats
```

**Rules:**
- `raw/` is read-only. The LLM reads from it, never modifies it.
- `raw/transcripts/` naming convention: `YYYY-MM-DD_[contact-slug]_[call-type].md`
  - Call types: `onboarding` | `sales-call` | `check-in` | `strategy` | `team` | `other`
- Everything under `wiki/` is LLM-owned. The human reads it; the LLM writes it.
- File names: lowercase, hyphens for spaces, `.md` extension (e.g. `network-effects.md`).
- All wiki pages use the frontmatter format defined below.

---

## Page Frontmatter Format

Every wiki page (except `index.md` and `log.md`) must begin with YAML frontmatter:

```yaml
---
title: "Page Title"
type: source | entity | concept | analysis | overview
tags: [tag1, tag2]
sources: [source-slug-1, source-slug-2]   # which raw sources this page draws from
updated: YYYY-MM-DD
---
```

- `type` determines which subdirectory the file lives in.
- `sources` lists the slug(s) of raw source(s) that contributed to this page.
  A slug is the filename of the raw source without extension (e.g. `my-article`).
- `updated` is set to today's date any time the page is modified.

---

## Operations

### 1. Ingest

Triggered when the human drops a file in `raw/` and says "ingest [filename]"
or equivalent.

**Steps (in order):**
1. Read the source file in full.
2. If it contains image references, note them for later viewing if relevant.
3. Discuss key takeaways with the human — ask 1-3 clarifying questions if needed.
4. Write a summary page to `wiki/sources/<slug>.md`.
5. Identify all entities mentioned (people, companies, products, places).
   - For each: create the entity page if it doesn't exist, or update it if it does.
6. Identify all concepts mentioned (frameworks, ideas, terms, themes).
   - For each: create the concept page if it doesn't exist, or update it if it does.
7. Update `wiki/overview.md` if the source shifts the big picture.
8. Update `wiki/index.md` — add the new source page and any new entity/concept pages.
9. Append an entry to `wiki/log.md`.

**After ingest**, tell the human:
- Which pages were created (new)
- Which pages were updated (and what changed)
- Any contradictions found with existing wiki content
- Suggested follow-up questions or sources to find

### 1b. Ingest Transcript

Triggered when the human drops a file in `raw/transcripts/` and says "ingest transcript [filename]" or equivalent.

**Steps (in order):**
1. Read the transcript file in full.
2. Identify: date of call, all participants (names + roles), primary contact/client.
3. Write a call summary page to `wiki/sources/calls/<YYYY-MM-DD-slug-type>.md`.
   - Include: Participants, Summary (3–5 bullet key points), Action Items (owner + task), Decisions Made, and Context Notes (anything that updates understanding of the client/project).
4. For each participant who has an entity page: update their entity page with any new info (status changes, stated goals, concerns, next steps).
5. If the call reveals a new entity (client, prospect, vendor): create their entity page.
6. If an action item is owned by the human (Ashenafe): flag it explicitly in your response.
7. Update `wiki/index.md` — add the call page under a **Calls** section.
8. Append an entry to `wiki/log.md`.

**Call summary page format (`wiki/sources/calls/<slug>.md`):**

```yaml
---
title: "Call — [Contact Name] — [YYYY-MM-DD]"
type: source
tags: [call, transcript, contact-slug, call-type]
sources: [YYYY-MM-DD_contact-slug_call-type]
updated: YYYY-MM-DD
---
```

```markdown
## Participants
- [Name] — [Role]

## Summary
- Key point 1
- Key point 2

## Action Items
| Owner | Task | Due |
|-------|------|-----|
| Ashenafe | ... | ... |
| [Other] | ... | ... |

## Decisions Made
- ...

## Context Notes
Anything that updates the picture on this client, project status, or ongoing initiatives.
```

**After ingest**, tell the human:
- The call summary location
- All action items flagged with their owners (highlight Ashenafe's items)
- Which entity pages were updated
- Any contradictions with existing wiki content (e.g., a client's status has changed)

---

### 2. Query

Triggered when the human asks a question about wiki content.

**Steps:**
1. Read `wiki/index.md` to identify relevant pages.
2. Read those pages in full.
3. If the answer requires synthesis across multiple pages, do it explicitly.
4. Deliver the answer with citations (link to wiki pages, not raw sources directly).
5. **Offer to file the answer** — if the answer is non-trivial, offer to save it
   as a new page in `wiki/analysis/`. Good analyses compound; chat history doesn't.

### 2b. Action Item Query

Triggered when the human asks "what are my open action items", "what's pending for [client]", or equivalent.

**Steps:**
1. Read all pages in `wiki/sources/calls/`.
2. Aggregate all Action Items tables across all call summaries.
3. Group by owner and filter by what's been mentioned as completed vs. still open.
4. Deliver a clean list grouped by: **Your Items (Ashenafe)** → **Client Items** → **Team Items**.
5. Offer to save the output as `wiki/analysis/action-items-YYYY-MM-DD.md`.

---

### 3. Lint

Triggered when the human says "lint the wiki" or equivalent.

**Check for:**
- Contradictions between pages (note both pages and the conflict)
- Stale claims superseded by newer sources (check `sources` frontmatter dates)
- Orphan pages with no inbound links from other wiki pages
- Important named entities mentioned in multiple pages but lacking their own page
- Missing cross-references (A mentions B but doesn't link to B's page)
- Data gaps: concepts with thin pages that a web search could fill
- `index.md` entries that are missing or out of date

**Deliver:** a lint report filed as `wiki/analysis/lint-YYYY-MM-DD.md`, plus a
summary to the human with prioritized action items.

### 4. Add Analysis

Triggered when the human requests a comparison, synthesis, chart, table, etc.

**Steps:**
1. Read relevant wiki pages.
2. Produce the output in the requested format.
3. Save it to `wiki/analysis/<descriptive-slug>.md`.
4. Add it to `wiki/index.md`.
5. Append to `wiki/log.md`.

---

## Cross-Referencing Convention

- Always use wiki-internal links: `[[Page Title]]` (Obsidian-style) when referencing
  another wiki page within prose. Example: `See [[Network Effects]] for background.`
- In frontmatter `sources` field, use the raw file slug (no brackets, no extension).
- Do not link to raw source files from within wiki pages — link to the source summary
  page in `wiki/sources/` instead.

---

## index.md Format

`wiki/index.md` has no frontmatter. Structure:

```markdown
# Wiki Index

_Last updated: YYYY-MM-DD — N pages total_

## Sources
| Page | Summary | Date |
|------|---------|------|
| [[Source Title]](sources/slug.md) | one-line summary | YYYY-MM-DD |

## Entities
| Page | Summary |
|------|---------|
| [[Entity Name]](entities/slug.md) | one-line summary |

## Concepts
| Page | Summary |
|------|---------|
| [[Concept Name]](concepts/slug.md) | one-line summary |

## Analysis
| Page | Summary | Date |
|------|---------|------|
| [[Analysis Title]](analysis/slug.md) | one-line summary | YYYY-MM-DD |
```

The LLM updates this file on every ingest, analysis, or lint operation.

---

## log.md Format

`wiki/log.md` has no frontmatter. Entries are prepended (newest first) in this format:

```markdown
## [YYYY-MM-DD] operation | Title or Description

- **Type:** ingest | query | lint | analysis
- **Files touched:** list of wiki files created or updated
- **Notes:** brief summary of what happened and any notable findings
```

This file is append-only in spirit — never edit or delete past entries.

---

## Session Start Protocol

At the start of every Claude Code session in this directory:

1. Read this file (`CLAUDE.md`) in full.
2. Read `wiki/index.md` to orient yourself on the current state of the wiki.
3. Read the last 3 entries in `wiki/log.md` to understand recent activity.
4. Greet the human with a one-paragraph status summary:
   - How many pages the wiki has (by type)
   - What was ingested or changed most recently
   - Any open threads or suggested next steps from the last log entry

Do not skip this protocol even if the human jumps straight to a task.

---

## Style Rules for Wiki Pages

- Write in clear, dense prose. No fluff. No filler phrases.
- Use headers (`##`, `###`) to organize long pages.
- Use bullet lists for enumerations; prose for analysis and synthesis.
- Always include at least one `[[Link]]` to another wiki page if one is relevant.
- For entity pages: include a "Sources" section at the bottom listing which source
  pages mention this entity.
- For concept pages: include a "Related Concepts" section at the bottom.
- For source pages: include a "Key Claims" section (bulleted) and an "Entities
  Mentioned" section with links.

---

## Versioning

This is a plain git repo of markdown files. Commit after each major operation
(ingest, lint, significant analysis). Commit message format:

```
[wiki] operation: brief description

e.g.
[wiki] ingest: "The Cold Start Problem" — added 3 entity pages, 2 concept pages
[wiki] lint: 2026-04-12 — found 3 orphans, 1 contradiction
[wiki] analysis: network effects comparison table
```

---

## Domain

The domain of this wiki is: **ScaleHere / Scale SD** — a marketing agency (scalehere.com)
providing paid ads, social media management, lead generation, client onboarding, and
automation services. Primary target market: contractors and local service businesses.
Tech stack includes GoHighLevel. Team includes setters and closers.

_Schema version: 1.0 | Created: 2026-04-12_
