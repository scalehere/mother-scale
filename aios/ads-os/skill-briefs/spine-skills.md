# ads-os Spine Skill Briefs

> Three skill briefs for the launch spine. Run `/skill-creator` on each section to convert into a runnable skill in `~/.claude/skills/`.
> Built: 2026-05-05.

---

## Skill 1: `ads-competitor-mine`

### Trigger
"mine spark marketing", "competitor scan", "what are {agency} running", "deep-dive {agency} ads", or weekly Monday cadence.

### Inputs (ask if missing)
- Agency name (default: Spark Marketing)
- Niche (default: home services contractors)
- Geography (default: US national, SD-priority)
- Why-this-matters context (default: pulled from `ads-os/strategy.md`)

### Behavior
1. Read `aios/ads-os/competitors.md` for current state on this agency.
2. Read `aios/ads-os/research/manus-spark-prompt.md` as the prompt template.
3. Adapt the prompt template with input agency name and context.
4. Save adapted prompt to `aios/ads-os/research/manus-{agency-slug}-prompt.md`.
5. Output to user: paste-ready prompt block + 1-line instructions for running it in Manus.
6. After user pastes Manus output back, save to `aios/ads-os/research/manus-{agency-slug}-{YYYY-MM-DD}.md`.
7. Distill: top 3 hooks, 1 funnel insight, 1 thing to NOT copy. Update `competitors.md` agency row. Append hooks to `scripts.md` Script 7 hook bank with attribution.
8. Post a 5-line summary to Slack `#all-tools` with the highest-confidence takeaway.

### Outputs
- Adapted Manus prompt (file)
- Manus output (file, after user paste)
- Updated `competitors.md`
- Optional new hooks in `scripts.md`
- Slack digest

### Reference files
- `aios/references/google-workspace-mcp.md` (if writing to Drive)
- `aios/references/slack-mcp.md`
- `aios/ads-os/competitors.md`
- `aios/ads-os/research/manus-spark-prompt.md`

---

## Skill 2: `ads-script-generate`

### Trigger
"write me an ad script", "new script for {trade}", "spanish version of script {N}", "generate {N} hook variants".

### Inputs (ask if missing)
- Trade (GC / Pool / HVAC / Roofing / Plumbing / Windows / Landscaping / Generic)
- Language (EN / ES)
- Length (15s / 30s / 45s / 60s)
- Angle (guarantee / pain / proof / curiosity / data / urgency / authority)
- Talent (Peter / Victor / Tony / generic / TBD)
- Setting (job site / studio / outdoor / car)

### Behavior
1. Read `aios/ads-os/strategy.md` for locked offer, pain points, CTAs, voice rules.
2. Read `aios/ads-os/scripts.md` to know what already exists. Don't duplicate.
3. Read `aios/references/voice.md` for register.
4. Generate the script with this structure: hook → problem → credibility → offer → guarantee (if applicable) → CTA.
5. Apply hard rules: no em dashes, Register C for spoken, contractor language not agency jargon, plain English (or contractor Spanish if ES).
6. Write to `scripts.md` BELOW the existing block, never replace. Use next available script number. Mark status "draft, needs Dani approval."
7. Output the script in chat for immediate review.
8. If the user accepts, change status to "locked" and timestamp it.

### Hard rules
- No em dashes.
- No unverified dollar figures. If using a proof point, only use ones flagged "verified" in `strategy.md` proof table.
- 90-leads-in-12-weeks guarantee can only appear in scripts where the trade fits and only after explicit confirmation it's still the locked offer.
- ES scripts: write in contractor Spanish, not academic Spanish. Match Rodrigo / Velocity register.

### Outputs
- New script appended to `scripts.md`
- Script printed in chat for review

---

## Skill 3: `ads-shoot-brief`

### Trigger
"build shoot brief for {date}", "we're shooting {subject} tomorrow", "prep shoot {date}".

### Inputs (ask if missing)
- Shoot date
- Subject / location (e.g. "Victor Carlsbad job site")
- Scripts to capture (default: all locked, EN, that fit the location)
- Talent on site (Peter / Victor / Tony / Dani / etc.)
- Constraints (time on site, weather, client availability)

### Behavior
1. Create folder `aios/ads-os/shoots/{YYYY-MM-DD}-{subject-slug}/`.
2. Read `aios/ads-os/scripts.md` and pull the requested scripts into the brief.
3. Read `aios/ads-os/strategy.md` for proof-point and offer guardrails.
4. Read prior shoot briefs in `aios/ads-os/shoots/` to inherit gear list, run-of-show defaults, file-naming convention.
5. Generate a single file `{date}-{subject-slug}.md` (or `brief.md` inside the folder) with these sections:
   - One-line objective
   - Pre-shoot checklist (Dani's confirmations)
   - Roles
   - Gear list
   - Capture format and specs
   - Run of show (shooting order, timed)
   - Shot list (A-roll + B-roll + BTS)
   - Coaching notes per talent
   - Locked scripts (full text or pointer to scripts.md)
   - Post-shoot deliverables
   - 48-hour edit deliverables
   - Risk register
   - Pre-launch checklist
6. Print a tight summary in chat: shoot date, location, talent, # of cuts expected, top 3 risks.
7. Post to Slack `#all-tools`: "Shoot brief ready: {date} {subject}. {N} cuts planned. Link: {drive or repo path}."

### Outputs
- New folder + brief file in `shoots/`
- Slack post
- Chat summary

### Defaults baked in (from `2026-05-06-victor-carlsbad.md`)

- 4 hours on site, pad to 5
- Vertical 9:16, 4K, 60fps for movement
- File naming: `{date}_{subject}_{ScriptN}_take{N}.mp4`
- Drive upload path: `/SCALE/Ads/{date}-{subject}/raw/`
- 48-hour editor turnaround

---

## How these three connect

```
Monday    /ads-competitor-mine spark        → fresh hooks land in scripts.md hook bank
Monday pm /ads-script-generate x4           → 4 new locked scripts
Tuesday   /ads-shoot-brief 2026-05-06       → full shoot package
Wednesday SHOOT (manual, on site)
Thursday  edit (manual or AI-assisted)
Friday    /ads-campaign-setup (week 2 skill) → launch
```

Three skills cover Mon-Tue. The other six skills (5-9) cover Wed-Fri-onward and get built next week after the first launch teaches us what's actually needed.

## To install as runnable skills

```
cd ~/.claude/skills
# For each section above, run /skill-creator and paste the brief.
# Skill creator will output SKILL.md, manifest, and trigger config.
```

Or build manually: copy each section into `~/.claude/skills/{skill-name}/SKILL.md` with proper frontmatter (name, description, trigger).
