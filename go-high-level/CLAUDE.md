# LLM Wiki — Schema & Operating Rules

This is the master configuration file for this wiki. Every session begins by reading this file. All operations follow these rules exactly.

---

## Directory Layout

```
/                        ← repo root (also Obsidian vault root)
├── CLAUDE.md            ← this file — schema & rules (never modify without user approval)
├── raw/                 ← immutable source documents (LLM reads, never writes)
│   ├── articles/        ← clipped web articles (.md)
│   ├── papers/          ← academic papers (.md or .pdf)
│   ├── notes/           ← personal notes, journal entries, voice transcripts
│   ├── data/            ← datasets, spreadsheets, CSV
│   └── assets/          ← images referenced by raw sources
└── wiki/                ← LLM-owned knowledge base (LLM writes, human reads)
    ├── index.md         ← master content index (updated on every ingest)
    ├── log.md           ← append-only chronological log
    ├── overview.md      ← evolving high-level synthesis of everything
    ├── entities/        ← pages for people, companies, products, places
    ├── concepts/        ← pages for ideas, methods, frameworks, topics
    ├── sources/         ← one summary page per ingested source
    └── outputs/         ← query answers, analyses, comparisons filed as pages
```

**Rules:**
- `raw/` is read-only for the LLM. Never create or modify files there.
- `wiki/` is fully owned by the LLM. The human reads; the LLM writes.
- Every wiki page must be linked from `index.md`.
- Every operation (ingest, query, lint) must be logged in `log.md`.

---

## Wiki Page Conventions

### Frontmatter (all pages)
```yaml
---
title: Page Title
type: entity | concept | source | output | overview
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-slug-1, source-slug-2]   # omit for source pages
---
```

### Page types and their structure

**entity** — a person, company, product, place, organization
```
# Name
One-paragraph description.
## Key Facts
## Relationships
## Appearances
Links to every source page that mentions this entity.
## Notes
Contradictions, open questions, gaps.
```

**concept** — an idea, method, framework, phenomenon, term
```
# Concept Name
Definition (1-3 sentences).
## How It Works
## Examples & Evidence
## Relationships
Links to related concepts and entities.
## Open Questions
```

**source** — summary of one ingested raw document
```
# Source Title
- **Type:** article | paper | note | data
- **Date:** YYYY-MM-DD (publication date if known)
- **Ingested:** YYYY-MM-DD
- **File:** raw/category/filename.md
## Summary
3-5 sentence summary.
## Key Takeaways
Bulleted list of the most important points.
## Entities Mentioned
Links to entity pages.
## Concepts Mentioned
Links to concept pages.
## Contradictions & Tensions
Any conflicts with existing wiki knowledge.
## Raw Excerpts
Optional: notable direct quotes.
```

**output** — a filed query answer, analysis, or comparison
```
# Output Title
- **Query:** The question that prompted this
- **Date:** YYYY-MM-DD
## Answer / Analysis
## Sources Used
## Confidence & Caveats
```

---

## Operations

### INGEST — adding a new source

Triggered by: user drops a file in `raw/` and says "ingest [filename]", or pastes content directly.

Steps (execute in order, do not skip):
1. Read the source thoroughly.
2. **Discuss** with the user: summarize key takeaways, ask if there are angles to emphasize or de-emphasize.
3. Create `wiki/sources/[slug].md` using the source page template.
4. Update or create entity pages for every significant entity mentioned.
5. Update or create concept pages for every significant concept mentioned.
6. Update `wiki/overview.md` if the source meaningfully shifts the overall picture.
7. Update `wiki/index.md` — add the new source page and any new entity/concept pages.
8. Append to `wiki/log.md` using this format:
   ```
   ## [YYYY-MM-DD] ingest | Source Title
   - File: raw/category/filename.md
   - Pages created: list
   - Pages updated: list
   - Key insight: one sentence
   ```
9. Report a brief summary of changes to the user.

**Ingest principles:**
- One source at a time by default. Ask before batch-ingesting.
- When new source contradicts existing wiki content, note the contradiction prominently in both pages — do not silently overwrite.
- Extract entities and concepts even if they don't yet have full pages — create stub pages with a note to expand.
- Prefer updating existing pages to creating redundant new ones.

### QUERY — answering questions from the wiki

Triggered by: user asks a question, requests an analysis, or asks for a comparison.

Steps:
1. Read `wiki/index.md` to identify relevant pages.
2. Read all relevant pages.
3. Synthesize and answer with inline citations (links to wiki pages and source slugs).
4. Ask the user: "Should I file this answer as a wiki page?" If yes, create `wiki/outputs/[slug].md` and update `index.md` and `log.md`.

**Query log format:**
```
## [YYYY-MM-DD] query | Question summary
- Pages consulted: list
- Filed as output: wiki/outputs/slug.md (or: not filed)
```

### LINT — health-checking the wiki

Triggered by: user says "lint the wiki" or "health check".

The LLM scans the wiki and reports:
- Contradictions between pages
- Stale claims (newer sources supersede old ones)
- Orphan pages (no inbound links)
- Missing pages (entities/concepts mentioned but lacking their own page)
- Missing cross-references
- Data gaps that a web search could fill
- Suggested new questions to investigate

After the report, ask the user which issues to fix. Execute fixes and log them:
```
## [YYYY-MM-DD] lint
- Issues found: N
- Issues fixed: list
- Deferred: list
```

---

## index.md Conventions

`index.md` is organized by category. Each entry: `- [Page Title](path/to/page.md) — one-line hook`

Categories:
- Overview
- Sources (by date ingested, newest first)
- Entities (alphabetical)
- Concepts (alphabetical)
- Outputs (by date, newest first)

The LLM reads `index.md` at the start of every query to navigate the wiki.

---

## log.md Conventions

- Append-only. Never delete entries.
- Each entry starts with `## [YYYY-MM-DD] type | title`
- Types: `ingest`, `query`, `lint`, `schema-update`
- Parseable: `grep "^## \[" wiki/log.md | tail -10` gives last 10 entries.

---

## Cross-Reference Style

In wiki pages, always link to other wiki pages using Obsidian-style wikilinks: `[[Page Title]]` or `[[path/to/page|Display Text]]`. This makes the Obsidian graph view meaningful.

---

## Session Start Protocol

At the start of every session:
1. Read `CLAUDE.md` (this file).
2. Read `wiki/log.md` (tail — last 5-10 entries) to understand recent activity.
3. Read `wiki/index.md` to know what's in the wiki.
4. Greet the user with a one-line status: what's in the wiki, what was done last session.
5. Ask: "What would you like to do? (ingest / query / lint / other)"

---

## Guiding Principles

- **The wiki is a compounding artifact.** Every ingest makes it richer. Every query can strengthen it. Never let information disappear into chat history if it could live in the wiki.
- **Contradictions are first-class.** Flag them prominently. Do not smooth them over.
- **The human sources, the LLM maintains.** Don't ask the user to do bookkeeping. Do it yourself.
- **Be a disciplined writer.** Keep pages focused. Avoid padding. A stub page is better than a bloated one.
- **Prefer updating to creating.** Before making a new page, check if an existing page should be expanded.
- **Log everything.** If it happened, it's in log.md.
