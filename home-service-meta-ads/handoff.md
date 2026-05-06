# Handoff — home-service-meta-ads ingest

**Date:** 2026-04-27
**Working dir:** `/Users/ashenafew/Desktop/SCALE/home-service-meta-ads/`

## What was done this session

Ingested all 11 raw markdown sources at the root into a structured wiki under `injested/`, following the schema documented in `~/Desktop/SCALE/scale-business/CLAUDE.md` (treating `injested/` as the wiki root and the 11 root `.md` files as the immutable `raw/` source).

**Files preserved unchanged:** all 11 original `.md` files at the root.

**Files created:** 71 wiki pages under `injested/`:

```
injested/
├── overview.md          ← synthesis across the corpus
├── index.md             ← catalog of every wiki page
├── log.md               ← ingest record for this session
├── sources/    (11)     ← one summary per raw source
├── entities/   (22)     ← people / programs / agencies / businesses / platforms / vendors
├── concepts/   (35)     ← frameworks, creative types, metrics, psychology, organic/physical
└── analysis/   (empty)  ← reserved for comparisons / syntheses you commission later
```

## How to resume

If you open a new session in this directory, the schema-aligned protocol is:

1. Read `injested/index.md` to orient on what's in the wiki.
2. Read the latest entry in `injested/log.md` to understand recent activity.
3. Read `injested/overview.md` for the synthesis if you need to brief yourself fast.

If you drop a new raw file in `home-service-meta-ads/` and say *"ingest [filename]"*, follow the schema's ingest protocol: write a summary to `injested/sources/<slug>.md`, create or update relevant entity / concept pages, update `injested/overview.md` if the source shifts the big picture, append to `injested/index.md`, and prepend a new entry to `injested/log.md`.

## Open follow-ups (from `log.md`)

- Vendor pricing for HSA approved-vendor list ([[Stryker Digital]], [[Local Legend AI]], [[Dope Marketing]]) — only application URLs are in source material.
- HSA Pro tier pricing — never disclosed across the 11 sources.
- Google PPC unit economics for home services — only directional ("expensive — $2K–$4K agencies") in the corpus.
- An analysis page comparing CPL / CPA / CAC across documented case studies (Ledesma $11K → $400K, Steve $50K → $400K, Todd $200 → $2,800) would be a natural next ask — not built yet.

## Notes / contradictions worth knowing

- 10 of 11 sources are by Steve Hunsaker (Home Service Accelerator); 1 is by Mandelyn Miller (Hook Agency). They contradict on **post-boosting** (Hook permits, Hunsaker dismisses) and **lookalike audiences** (Hook emphasizes, Hunsaker barely uses — his thesis is that broad geo + creative variation does the same job post-Andromeda).
- HSA member count grows across the corpus chronology: 500 → 550 → 600 → 700 → 800. Useful as a rough timeline anchor for any source whose date you need to reason about.
- The corpus is internally consistent on operational rules — Hunsaker doesn't contradict himself across 18 months of content on creative count, friction questions, speed-to-lead, scaling cadence, or the [[Tri-Pillar Marketing System]] frame.
