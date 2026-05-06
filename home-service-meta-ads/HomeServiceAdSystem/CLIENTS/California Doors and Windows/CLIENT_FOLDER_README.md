# /CLIENTS/[ClientName]/ — Per-Client Folder

This is a copy of `/SHARED/06_client-template/`. Each numbered subfolder maps 1:1 to a pipeline stage.

## Folder map

| Folder | Owner | Output |
|---|---|---|
| `00_intake/` | Agent 1 (+ user puts brand assets in `/brand_assets/`) | `intake_brief.md` |
| `01_bible/` | Agent 2 | `[Client]_Creative_Bible.xlsx` |
| `02_strategy/` | Agent 3 | `strategic_brief.md` |
| `03_assets/` | Agent 4 (+ user puts photos in `/photos/`, consent in `/consent/`) | `asset_bank.md` |
| `04_concepts/` | Agent 6 + Agent 7 | `concept_library.md`, `stress_test.md` |
| `05_copy/` | Agent 8 | `copy_per_concept.md` |
| `06_prompts/` | Agent 9 | `AD-XX_VAR-X_*.json` (3 per concept) |
| `07_generated/` | User (after running JSONs through ChatGPT Image) | Generated PNG files |
| `08_final/` | User (after Canva logo composite) | Launch-ready PNG files |
| `09_launch/` | Agent 10 | `launch_brief.md` |

## How to use this folder

1. Copy this entire `06_client-template/` folder to `/CLIENTS/[ClientName]/`
2. Drop client logo + founder photo into `00_intake/brand_assets/`
3. Drop install photos into `03_assets/photos/`
4. Open Cowork Orchestrator chat with this folder + `/SHARED/` connected
5. Follow the pipeline (see `/SHARED/01_quickstart/QUICKSTART_NEW_CLIENT.md`)

## Naming convention

Throughout this folder, use the actual client name (no spaces, dashes okay) wherever you see `[ClientName]` or `[Client]`. Examples:
- `California-Doors-and-Windows_Creative_Bible.xlsx`
- `AD-01_VAR-A_founder-subject.json`
- `consent/Sarah-G-Banker's-Hill_2026-04-26.pdf`

## What never gets deleted

Once a client folder is created, never delete anything in it. Old intake briefs, killed concepts, failed creative — all of it is reference material for future strategy decisions.
