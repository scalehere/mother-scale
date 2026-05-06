# Skill Brief: `ads-script-mass-generate`

> The Eddie pattern, Scale SD edition. Takes Manus competitor research → produces hundreds of scripts in our voice across all our ICPs.
> Run after `ads-competitor-mine` returns Manus output.

## Trigger

"mass generate scripts", "rewrite competitor ads", "build the script library from spark research", "give me 50 scripts", or scheduled after every Manus deep-dive run.

## Inputs (ask if missing)

- Source competitor research file (default: most recent `research/manus-{agency}-{date}.md`)
- Target ICPs (default: all 7 from `icp.md`)
- Languages (default: EN + ES)
- Length variants (default: 15s, 30s, 60s)
- Variation count for top performers (default: 10 per top-5 ad)
- Output destination (default: `creative-library/{date}-{agency}-batch/`)

## Hard preconditions (skill refuses to run unless ALL exist)

- `voice.md` exists and was loaded
- `product.md` exists and was loaded
- `icp.md` exists and was loaded
- `writing-rules.md` exists and was loaded
- Source Manus research file exists and contains the verbatim-transcript section (2a)

If any missing, halt and tell the user what's missing.

## The 4-stage pipeline

### Stage 1 — Read everything

Load in this exact order (order matters for context priority):
1. `writing-rules.md` (slop filter rules)
2. `voice.md` (register + structure)
3. `product.md` (offer + proof + verified claims)
4. `icp.md` (the 7 personas)
5. Source Manus research file

### Stage 2 — Per-ad rewrite (1:1 from competitor library)

For EVERY competitor ad in the Manus file's section 2a:

Output two artifacts side-by-side in `creative-library/{date}-{agency}-batch/{ad-id}/`:

**File A: `original-breakdown.md`**
Verbatim copy of the competitor ad transcript + angle breakdown from Manus. Untouched. This is our reference.

**File B: `rewrite-default.md`**
Same angle, same structure, our voice, our offer, our proof, default ICP (the one the original ad seemed to target). Includes:
- Frontmatter with: source ad ID, source agency, source angle, target ICP, length, language
- Hook (3-5 variants, hot-swappable)
- Body (full script in Register C)
- CTA
- 1-line "why this version" note

Constraints on rewrite:
- Same fundamental angle as original
- Same emotional beat sequence
- Different words (zero copy-paste)
- Run through 5-pass slop check from `writing-rules.md`
- Use only verified proof points from `product.md`
- Match `voice.md` register

### Stage 3 — ICP multiplier

For each rewrite from Stage 2, generate 6 additional variants by swapping the ICP:

- ICP 1 GC → ICP 2 Pool → ICP 3 HVAC → ICP 4 Roofing → ICP 5 Plumbing → ICP 6 Windows → ICP 7 Landscaping

For each ICP variant:
- Swap the verbatim pain phrasing to match that ICP's pain language from `icp.md`
- Swap the trade-specific buying triggers
- Keep the angle, structure, offer, guarantee identical
- File: `creative-library/{date}-{agency}-batch/{ad-id}/icp-{n}-{trade}.md`

If an ICP doesn't fit the angle (e.g. "summer urgency" doesn't fit roofing in SD), skip it and note "skipped: angle mismatch."

### Stage 4 — Top-performer variation explosion

From the Manus research, pull the longest-running 5 ads (Manus section 7). For each:

Generate 10 variations on the proven angle:
- Variation 1-3: hook swaps (different hook, same body)
- Variation 4-5: length variants (15s, 30s, 60s)
- Variation 6-7: language variants (EN + ES)
- Variation 8-9: talent variants (Peter / Victor / Tony / generic VO)
- Variation 10: "what if we said this in front of a job site / in a truck / in a finished home" (setting variant)

Output: `creative-library/{date}-{agency}-batch/top-performers/{ad-id}-v{n}.md`

## Math (typical run)

| Input | Multiplier | Output |
|---|---|---|
| 30 competitor ads from Manus | 1x | 30 default rewrites |
| 30 default rewrites | x6 ICPs (avg, after skip-on-mismatch) | ~150 ICP variants |
| 5 top performers | x10 variations | 50 explosion variants |
| **Total** | | **~230 scripts per Manus run** |

## Output structure

```
creative-library/2026-05-06-spark-batch/
├── _index.md                               summary table of all scripts
├── _approved.md                            (empty at start, fill as Dani approves)
├── ad-{spark-id-1}/
│   ├── original-breakdown.md
│   ├── rewrite-default.md
│   ├── icp-1-gc.md
│   ├── icp-2-pool.md
│   ├── icp-3-hvac.md
│   ├── icp-4-roofing.md
│   ├── icp-5-plumbing.md
│   ├── icp-6-windows.md
│   └── icp-7-landscaping.md
├── ad-{spark-id-2}/
│   └── ...
└── top-performers/
    ├── {ad-id-1}-v1.md
    ├── {ad-id-1}-v2.md
    └── ...
```

## The `_index.md` format

A single table summarizing the batch. Used by Dani to scan and pick.

| ID | Source ad | Angle | ICP | Lang | Length | Status |
|---|---|---|---|---|---|---|
| spark-001-default | spark-001 | guarantee | GC | EN | 60s | draft |
| spark-001-icp-2 | spark-001 | guarantee | Pool | EN | 60s | draft |
| ... | ... | ... | ... | ... | ... | ... |

After Dani reviews, status moves through: draft → approved → shot → live → killed.

## Quality gates per script (run before writing each file)

1. Banned-words scan (`writing-rules.md` ban list)
2. Em-dash scan (zero tolerance)
3. Verified-claim audit (every number traced to `product.md` proof table)
4. ICP language match (every script sounds like that ICP would talk)
5. Length match (word count matches target seconds at contractor pace ~150 wpm)

If any gate fails, retry up to 2x. If still fails, skip and log to `_skipped.md` with reason.

## Output to user

After the batch completes:

1. Print summary in chat:
```
Generated {N} scripts from {agency} research.
- {n} default rewrites
- {n} ICP variants (across {m} ICPs)
- {n} top-performer variations
- {n} skipped (see _skipped.md)
Output folder: creative-library/{date}-{agency}-batch/
```

2. Post Slack to `#all-tools`:
```
🎬 Script library refreshed.
Source: {agency} ({date})
{N} scripts ready for Dani review.
{drive_or_repo_link}
```

3. Optionally write top 5 highest-conviction scripts inline in chat for immediate Dani feedback.

## What this skill does NOT do

- Does NOT run the Manus deep-dive itself (that's `ads-competitor-mine`)
- Does NOT shoot or edit anything (that's the shoot brief + editor)
- Does NOT publish ads (that's `ads-launch`, week 2)
- Does NOT score ads against ICPs after they run (that's `ads-weekly-review`, week 2)

## Connections used

- File system (read all `.md` foundation files, write to `creative-library/`)
- Slack (`slack_post_message` to `#all-tools`)
- Optional: Google Drive (`create_doc` if user wants the index in Drive too)

## Known limits

- Quality scales with Manus output quality. Garbage in, garbage out. If Manus skips transcripts, scripts come out generic.
- Top-performer variation count is capped at 10 because >10 starts producing diminishing-returns near-duplicates.
- Spanish quality requires native review (Dani or Rodrigo). Skill flags ES variants as "needs ES native review" until Dani signs off.

## Update log

- 2026-05-05: Initial brief. Eddie pattern adapted to Manus (no Apify, no Whisper, Manus does both natively).
