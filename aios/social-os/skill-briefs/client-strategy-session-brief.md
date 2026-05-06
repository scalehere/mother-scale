# Skill Brief — `client-strategy-session`

> Feed this entire file to `/skill-creator` inside Claude Code (run from `aios/` working directory). Skill Creator will produce `social-os/.claude/skills/client-strategy-session/SKILL.md` packaged correctly. Then run `/review` before shipping.

---

## What I want this skill to do

Automate the Month-1 client strategy session that Scale SD runs every time a new client signs up for organic social media management. Today this is a 45-minute manual conversation between the client and a Scale SD team member, and the outputs (brand voice, content pillars, audience profile, platform priority, competitor list, offer/CTA library, shot wishlist) end up scattered in Slack, Fathom transcripts, and Google Docs — never assembled into anything the rest of the agency can actually run from.

The skill should walk a Scale SD operator (Ashen, Daniel, or Justin) through the same 7-section interview the manual SOP already defines, ask each question conversationally, accept answers in any format (typed, dictated, pasted from a Fathom transcript), and at the end write 7 structured config files into `social-os/clients/{client-slug}/` so every other social-os skill (`monthly-content-plan`, `caption-writer`, `reel-script`, etc.) can read them.

The skill should be **idempotent** — if config files already exist, it offers to refresh them and backs the originals up to `social-os/clients/{client-slug}/archives/{YYYY-MM-DD-HHMM}/`.

## When the skill should trigger

- Slash command: `/client-strategy-session`
- Natural language triggers: "run the strategy session for {client}", "onboard {client} into social-os", "set up the social config for {client}", "Month-1 intake for {client}", "we just signed {client}, get them set up"

If no client slug is provided, the skill should ask which client. If a slug is provided that doesn't match an existing entity in `../scale-business/wiki/entities/`, the skill should offer to create a new entity stub there.

## Inputs the skill reads at the start of every run

1. The current working CLAUDE.md (root) and `social-os/CLAUDE.md` (sub-OS scope)
2. `../scale-business/wiki/entities/{client-slug}.md` — existing client knowledge (don't ask the client questions we already have answers to)
3. Any existing `social-os/clients/{client-slug}/*.md` files — if any exist, this is a refresh run, not a fresh run
4. `../scale-business/wiki/sources/calls/` — any Fathom call transcripts where this client appears (especially onboarding calls), so the skill can pre-fill answers and confirm rather than ask cold

## The 7-section flow

The full template lives at `social-os/templates/client-strategy-session.md`. Read that template at the start of each run; use it as the source of truth for the flow.

Brief recap of sections:

1. **Brand voice & personality** → outputs `clients/{slug}/brand-voice.md`
2. **Content pillars (tailor the 5)** → outputs `clients/{slug}/content-pillars.md`
3. **Target audience** → outputs `clients/{slug}/audience.md`
4. **Platform priority** → outputs `clients/{slug}/platform-config.md`
5. **Competitor & inspiration review** → outputs `clients/{slug}/competitors.md`
6. **Offer & CTA library** → outputs `clients/{slug}/offers-and-ctas.md`
7. **Shot wishlist** → outputs `clients/{slug}/shot-wishlist.md`

Plus a derived 8th output: `clients/{slug}/hashtag-bank.md` — seeded from sections 2 + 3 + 5, expanded over time by `monthly-content-plan`.

## Conversational rules

- **Pre-fill, don't re-ask.** If the wiki entity page already says the client's address, owner name, services, or anything section-relevant, surface it as a confirmation: *"Joseph at EMSR is the owner — does the brand voice come from him personally, or do you want it more agency-neutral?"* — not *"who's the owner?"*
- **Quote Fathom call moments back at the operator.** If an onboarding call transcript exists, pull lines that reveal voice or audience preferences and ask the operator to confirm/refine: *"From the Apr 13 call, Victor said: 'we want it to feel like neighborhood guys, not corporate.' Use that as the brand voice anchor?"*
- **Push back on lazy answers.** If the operator answers "trustworthy and professional" for brand voice, ask for the next layer: *"Trustworthy is the floor for any contractor. What's the differentiator? Bold? Quiet expert? Family-owned-and-proud? Pick the one that's true and unique to this client."*
- **The 5 Content Pillars are non-negotiable as the framework.** Don't let the operator invent new pillars. They tailor the 5 (The Work, The Team, Education, Social Proof, Local Presence + bonus Offer/CTA) to this client. If pushed to add a custom pillar, refuse and explain — the framework is documented in `../scale-business/wiki/sources/social-media-content-optimization.md`.
- **Default platform priority for contractors is Facebook first.** Don't change it without a strong reason from the operator (e.g., a younger trade like landscape design where IG outperforms FB).
- **Cap promotional content.** Per the SOP, max 1 offer/CTA post per month. Don't let the operator over-promise.

## Output rules

- Each of the 7+1 output files uses YAML frontmatter (matching the wiki schema):
  ```yaml
  ---
  title: "{section title} — {client name}"
  type: client-config
  client: {client-slug}
  source: client-strategy-session
  generated: YYYY-MM-DD
  ---
  ```
- Files are written in a single batch at the end of the interview, not incrementally during. (Lets the operator stop mid-flow without leaving partial files.)
- After writing, append an entry to root `decisions/log.md`: *"Onboarded {client name} into social-os via client-strategy-session. Output files: ..."*
- After writing, update `../scale-business/wiki/entities/{client-slug}.md` with a new section: *"Social-OS config: see `aios/social-os/clients/{slug}/`"* (if not already linked).

## Output of the closing screen

Three lines max, then stop:

```
✓ Strategy session captured for {client name}. 8 config files written to social-os/clients/{slug}/.

Next: /shot-list {slug} (1 week before next monthly shoot) or /monthly-content-plan {slug}.
Or: /review to audit this strategy session before passing it to the rest of the team.
```

## Critical implementation rules

1. **The 7-section cap is non-negotiable.** Don't add an 8th section in conversation, and the derived hashtag-bank doesn't count as an asked section.
2. **Default to existing wiki data.** Don't ask the operator anything the wiki already answers — confirm, don't ask cold.
3. **One-shot file write at the end.** Don't write incremental drafts mid-interview. Lets the operator abort cleanly.
4. **Idempotent.** Re-running with edits backs up originals to `clients/{slug}/archives/{ts}/`.
5. **Bike-Method Phase 1.** Mark the output files with a `phase: 1` flag in frontmatter. They get human-reviewed before being passed to `monthly-content-plan` on the first run for any client.
6. **Read-only on `../scale-business/`** unless explicitly updating the entity page's social-os link section.
7. **Voice rule — agency voice ≠ client voice.** When proposing brand voice candidates, never use Ashen's voice from `references/voice.md`. The agency's voice is the operator interviewing; the client's voice is what we're capturing.

## Verification (for the implementer / Skill Creator's tests)

- **Cold-test on a new client (e.g., Tyler Biddick / BDK General Construction Inc):** wiki entity doesn't exist yet. Expected: skill offers to create entity stub, asks questions to fill all 7 sections, writes 8 config files, logs decision, updates entity. Generic output ("trustworthy contractor") = fail.
- **Refresh test on an existing client (e.g., EMSR):** existing config files present. Expected: skill detects them, offers refresh path, backs up to archives/{ts}/, refreshes only changed sections.
- **Pre-fill test (e.g., Victor / VIP General Contractor):** wiki entity exists, two onboarding call transcripts exist. Expected: skill quotes specific lines from those transcripts back at the operator and asks for confirmation rather than asking cold.
- **Lazy-answer pushback:** operator answers "trustworthy and professional" for brand voice. Expected: skill pushes back, asks for differentiator, won't accept the lazy answer.
- **Custom-pillar refusal:** operator tries to add "Sustainability" as a 6th pillar. Expected: skill refuses, explains the 5-pillar framework is the SOP, suggests folding sustainability into "Education" or "The Team."

## Reference materials Skill Creator should read while building

- `social-os/templates/client-strategy-session.md` — the section-by-section template
- `social-os/CLAUDE.md` — sub-OS scope, per-client schema, voice rules
- `aios/CLAUDE.md` — root operating manual (Cormac constitution, two-layer architecture)
- `../scale-business/wiki/sources/social-media-content-optimization.md` — the canonical Month-1 SOP
- `../scale-business/wiki/sources/social-media-strategy-for-sales.md` — the 100 contractor hooks (used to seed `clients/{slug}/content-pillars.md` examples)
- `references/voice.md` — Ashen's three registers (only used to ensure the skill doesn't accidentally use Ashen's voice for client content)

---

*Skill brief — © Scale SD 2026. Generated for `/skill-creator` consumption. Skill output should ship with `bike-method-phase: 1` and `three-ms-attribution` per the `level-up` skill's contract.*
