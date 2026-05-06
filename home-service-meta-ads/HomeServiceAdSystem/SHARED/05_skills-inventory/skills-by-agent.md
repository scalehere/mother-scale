# Skills Inventory — Which Skill Each Agent Uses

Every agent in the pipeline references one or more skills from `/mnt/skills/`. This is the authoritative source for which agent uses what skill, where it lives, and what it does in the pipeline.

When you copy this folder to a real Drive, replace `/mnt/skills/...` paths with whatever skill location works in your Cowork environment.

---

## Skills by Agent

| Agent | Skill | Skill Path | Purpose |
|---|---|---|---|
| Agent 0 — Orchestrator | _(none)_ | _(uses Drive folder inspection only)_ | Tracks project state |
| Agent 1 — Intake Researcher | _(none)_ | _(uses web_search, web_fetch, image_search)_ | Deep client + competitor + market research |
| Agent 2 — Creative Bible Builder | `creative-bible` | `/mnt/skills/user/creative-bible/SKILL.md` | Builds the 12-sheet xlsx that becomes the strategic source-of-truth |
| Agent 3 — Strategic Lever | _(none)_ | _(reasoning across bible + intake)_ | Picks awareness stage, avatars, angles, budget split |
| Agent 4 — Asset Curator | `bible-reader` | `/mnt/skills/user/bible-reader/SKILL.md` | Cross-references reviews/avatars/angles for quote scoring |
| Agent 5 — Reference Library Manager | `competitive-ads-extractor` | `/mnt/skills/user/competitive-ads-extractor/SKILL.md` | Converts competitor image-to-JSON into reusable structural REFs |
| Agent 6 — Concept Architect | `bible-reader` | `/mnt/skills/user/bible-reader/SKILL.md` | Generates 8-12 concept candidates with reference-hunt instructions |
| Agent 7 — Stress Tester | `stress-test` | `/mnt/skills/user/stress-test/SKILL.md` | Pressure-tests every concept; HARD GATE before image gen |
| Agent 8 — Copy Writer | `sound-human` | `/mnt/skills/user/sound-human/SKILL.md` | Writes natural-speech copy for headlines, taglines, CTAs |
| Agent 9 — Brand Translator / Visual Director | `json-prompt-generator` | `/mnt/skills/user/json-prompt-generator/SKILL.md` | Produces 3 JSON variations per concept rebranded to client |
| Agent 10 — Production Brief | _(none)_ | _(synthesizes upstream outputs)_ | Final launch brief with budget, KPIs, kill criteria |

---

## Skills by Function

### Research / Discovery
- **Agent 1** — built-in web tools, no external skill
- **Agent 5** — `competitive-ads-extractor` for converting competitor ad images

### Strategy / Synthesis
- **Agent 2** — `creative-bible` for building the 12-sheet bible
- **Agent 4** + **Agent 6** — `bible-reader` for pulling structured data out of the bible
- **Agent 7** — `stress-test` for adversarial concept evaluation

### Production / Output
- **Agent 8** — `sound-human` for spoken-style copy quality
- **Agent 9** — `json-prompt-generator` for image-gen-ready JSON prompts

---

## What if a skill is missing or fails?

Each agent's prompt has fallback behavior in case the skill isn't accessible:

- **`creative-bible` missing:** Agent 2 will use a built-in 12-sheet structure, output may be less rigorous — flag for re-run when skill restored
- **`bible-reader` missing:** Agents 4 and 6 fall back to direct xlsx reading
- **`stress-test` missing:** Agent 7 falls back to a 4-lens framework documented in its prompt
- **`sound-human` missing:** Agent 8 will produce competent copy but may read more "ad-like"
- **`json-prompt-generator` missing:** Agent 9 will produce JSON using `/SHARED/03_templates/ad-json-template.json` directly
- **`competitive-ads-extractor` missing:** Agent 5 has the conversion logic baked into its prompt as fallback

---

## Adding new skills to the system

If you build or acquire a new skill that benefits the pipeline:

1. Save it to your skills location
2. Identify which agent should use it
3. Update that agent's prompt in `/SHARED/02_agents/` to reference the new skill
4. Update this inventory file
5. Document the fallback behavior

Skills compound the system the same way the reference library does — each new skill makes future client work faster and higher-quality.

---

## Future skills that would slot cleanly

- `lead-form-optimizer` — Agent 10 lead form qualifying questions
- `meta-audience-builder` — Agent 10 Meta interest/behavior targeting
- `creative-fatigue-detector` — post-launch Agent 11 to auto-flag fatiguing winners and trigger new variation rounds
- `client-deliverable-packager` — post-launch client-facing summary PDF
