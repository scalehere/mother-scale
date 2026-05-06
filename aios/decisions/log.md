# Decisions Log

Append-only record of meaningful decisions and why they were made. `/level-up` Phase 2 (Method interview) writes scoped automation specs here. You can also append manually whenever you decide something worth remembering.

**Format per entry:**

```
## YYYY-MM-DD — Short title

**Decision:** what was decided.

**Why:** the reasoning, constraints, and what would change your mind.

**Alternatives considered:** what else was on the table.

**Owner:** who's accountable.
```

Keep it terse. Future-you will thank present-you for capturing the *why*, not just the *what*.

---

## 2026-05-04 — Adopt the AIS-OS framework as the operator layer for Scale SD

**Decision:** Install Nate Herk's AIS-OS starter kit at `/Users/ashenafew/Desktop/SCALE/aios/` as the operator brain for the agency. Keep the existing Karpathy-style wiki at `scale-business/` as the knowledge layer. The AIOS's `CLAUDE.md` points to the wiki for queryable business knowledge.

**Why:** The brief and SWOT identified that SOPs aren't standardized and delivery feels custom per client — this is a Capabilities + Cadence problem that the AIS-OS framework directly addresses. Skills, decisions log, audits, and recurring rituals turn one-off work into compounding leverage. Building on top of the existing wiki means we don't lose the 62 pages of business context already captured.

**Alternatives considered:**
- Build the operator layer inside `scale-business/` (rejected — mixes operating system code with business knowledge files; CLAUDE.md schema would conflict).
- Replace `scale-business/` with the new structure (rejected — destroys working second brain).
- Build a custom equivalent from scratch (rejected — Nate's kit is MIT-licensed and already battle-tested; no reason to reinvent).

**Owner:** Ashenafew (Ashen).

---

## 2026-05-04 — Prioritize fulfillment automation over growth (outbound + agency content)

**Decision:** Build the AIOS to automate per-client full-stack fulfillment (website → GBP → Yelp → social organic → paid ads → GHL automation) BEFORE scaling outbound or producing agency-owned content. Skills built first will map directly to the offer ladder (Foundation → Growth → Scale → CRM Add-On), not to internal ops. Once fulfillment runs as a system, capacity expands and growth motions can re-engage.

**Why:** Per Q7 of the intake, the binding constraint is client capacity, not lead supply. Adding clients without automating fulfillment would degrade the full-package quality bar that defines the revenue-partner positioning. Ashen explicitly: *"right now, we need to focus on our system and making sure we build that operating system that can fulfill every single individual task... so that we can make it repeatable and make it a system and make it an SOP."*

This also aligns with the SWOT (Months 1-2 = "fix internal systems, close 3-5 contractors") and matches Serge Gatari's playbook thesis (codify the playbooks that replace whole functions in client businesses, then sell them).

**Alternatives considered:**
- Growth-first: ramp outbound + post agency content + close more clients (rejected — would compound the existing fulfillment bottleneck and damage quality/retention).
- Single-service narrow offer: drop full-package commitment, sell only one service (rejected — kills the revenue-partner positioning that differentiates Scale SD from generic agencies).
- Hire to scale: add a junior person to absorb fulfillment (rejected — token-max not headcount-max per the Cormac constitution; also slower than building skills).

**First five skills targeted (replaces earlier guess in Task #6):**
1. Website-build skill (Foundation tier)
2. GBP + Yelp setup skill (Foundation tier)
3. Social organic management skill — content planning, scripting, scheduling across multiple client brands (Growth tier)
4. Paid ads campaign skill — build, run, analyze, retarget via Meta Ads MCP + Higgsfield for creative (Scale tier)
5. GHL automation snapshot skill — missed-call text-back, lead followup, booking, review automation (CRM Add-On)

These are the same five layers the agency sells. Building them as skills means the AIOS doesn't just help Ashen do fulfillment — it *becomes* the fulfillment system, and at the end of the path each skill is also productizable as a client-facing snapshot.

**Owner:** Ashenafew (Ashen).

---

## 2026-05-05 — Install the 6 skills before building any custom skill (Skill Creator first)

**Decision:** Before writing the first social-os skill (`client-strategy-session`), install Nate Herk's recommended 6 skills + bonus globally in Claude Code. Build all subsequent custom skills *through* Skill Creator (don't hand-write SKILL.md files). Run `/review` on every shipped skill. Install: Skill Creator, Superpowers, GSD, Context Mode, ClaudeMem, Front-End Design (bonus). `/review` and `/ultra-review` are already built-in (Claude Code 2.1.86+).

**Why:**
- **Skill Creator** is the factory that builds every other skill. Hand-writing SKILL.md means re-learning the structure and reliability rules every time. Building through Skill Creator compresses the learning curve and produces consistent, testable, packaged skills.
- **Context Mode + ClaudeMem** address the two failure modes that kill long Claude Code sessions: context rot (raw tool output flooding the window) and zero-memory cold starts (re-explaining the project every session). The social-os build will involve many long sessions across 4 clients with 12-16 posts/month each — these two skills extend session length 30min → 3hrs and eliminate the startup tax.
- **Superpowers + GSD** are the right tools when we get to skills that touch real APIs or run multi-step (post-scheduler, monthly-content-plan). Less critical for pure Markdown skills (client-strategy-session, brand-voice-profile) but harmless to have installed.
- **/review** is free, already built in. Use on every shipped skill.
- The selling lesson Nate closes with — *"don't sell workflows, sell outcomes (save 10 hours/week, cut admin mistakes, more leads)"* — directly reinforces Scale SD's revenue-partner positioning and should anchor the CRM Add-On product pitch.

**Alternatives considered:**
- Skip the skills, hand-write SKILL.md files (rejected — slower, less reliable, doesn't compose with the rest of the ecosystem).
- Install only Skill Creator and skip the rest (rejected — Context Mode and ClaudeMem solve real session-degradation problems we'll hit on day one of the build).

**Source:** Nate Herk, *"I Tried 100+ Claude Code Skills. These 6 Are The Best,"* YouTube 2026-05-03. Saved at `os/I Tried 100+ Claude Code Skills. These 6 Are The Best 1.md`.

**Owner:** Ashenafew (Ashen).

---

## 2026-05-04 (evening) — Reorder fulfillment skills: social organic first, not website-build

**Decision:** Within the fulfillment-automation roadmap, ship the **social organic management sub-OS** (`social-os/`) first instead of the website-build skill. The first shipped skill will be one of: `client-strategy-session`, `brand-voice-profile`, or `monthly-content-plan` (TBD via `/level-up`).

**Why:** Social organic is recurring monthly per client and applies to all 4 active clients (vs. website which is one-time and largely already built for active clients). Per Q7, the actual weekly time bleed is content scripting, planning, and posting — not website builds. The leverage compounds across clients faster: one well-built voice/pillar/plan engine multiplies cleanly to the next client. The wiki already has the operational SOPs (5 Content Pillars, 100 contractor hooks, Month-1 Strategy Session template, 20-item shot list, 2.5-hr shoot schedule), so the skills are *automating existing manual processes*, not inventing new ones.

**Sub-OS scaffolded:** `social-os/CLAUDE.md` + `social-os/templates/` (client-strategy-session, monthly-content-plan, shot-list) + `social-os/clients/` (per-client config folders to be populated). Skill ladder of 9 planned, shipped one per week via `/level-up`.

**Alternatives considered:**
- Website-build first (rejected — one-time pain, smaller compounding leverage).
- Build all skills in flat `.claude/skills/social-*/` without a sub-OS folder (rejected — sub-OS keeps client configs scoped + isolates the workflow per Nate's EXPANSIONS.md guidance).
- Wait for a new Foundation client to onboard before building anything (rejected — slow, unnecessary; existing clients already need this leverage).

**Owner:** Ashenafew (Ashen).

---

## 2026-05-04 — Discovery: GoHighLevel MCP is already connected to Claude

**Decision:** Treat GHL as an existing live connection, not a Day-2+ wire-up. Inventory GHL MCP tool surface, write `references/gohighlevel-mcp.md` documenting available endpoints / objects / common query patterns, and reorder the connection backlog (Meta Ads now #2, Higgsfield #3).

**Why:** Per Q7, Ashen confirmed: "I have the Go High Level MCP connected to Claude." This means live pipeline, opportunity, contact, and conversation data is already reachable from any Claude Code session pointed at this AIOS. Massive head start — the typical AIOS Day-2 task (wire the most important domain) is already done.

**Alternatives considered:**
- Wire GHL fresh via API + script (rejected — duplicates existing MCP).
- Defer GHL inventory until first skill needs it (rejected — cheaper to do once, save the reference, reuse forever per the "researched-once-saved-forever" principle).

**Owner:** Ashenafew (Ashen).
