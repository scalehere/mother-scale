# Scale SD AIOS

The operator-layer AI Operating System for **Scale SD / ScaleHere** — a marketing & automation agency for contractors and local service businesses.

This repo is built on top of [AIS-OS](https://github.com/nateherkai/AIS-OS) — Nate Herk's MIT-licensed starter kit — customized for Scale SD's stack and team. It's paired with the existing knowledge wiki at `../scale-business/` (Karpathy-style second brain).

---

## The two-layer architecture

```
SCALE/
├── aios/             ← THIS REPO. Operator layer. Skills, decisions, connections.
│   ├── CLAUDE.md     ← Root operating manual. Points to the wiki for knowledge.
│   ├── context/      ← About you, the business, current priorities.
│   ├── references/   ← Frameworks (3Ms), voice samples, API guides.
│   ├── connections.md← Every system the AIOS can reach.
│   ├── decisions/log.md
│   ├── archives/
│   └── .claude/skills/
│       ├── onboard/   ← Day-1 wizard
│       ├── audit/     ← Weekly Four-Cs gap report
│       └── level-up/  ← Weekly Three-Ms ritual; one shipped automation per run
└── scale-business/   ← Knowledge layer. Karpathy-style second brain.
    └── wiki/         ← 60+ pages: sources, entities, concepts, analysis. Already mature.
```

The AIOS asks "**how do I operate?**" The wiki answers "**what do I know?**" Together they're the full system.

---

## Quick start (Day 1)

1. **Open this folder in Claude Code.**
2. **Paste 1-2 raw writing samples** into `aios-intake.md` Q2 (must be raw — see the rule in the file).
3. **Run `/onboard`.** The wizard will confirm the pre-filled answers (Q1, Q3, Q4-Q7 are already populated from the existing business brief), scaffold `context/` files, populate `references/voice.md`, and finalize `CLAUDE.md`.
4. **Try the wow prompt:** *"what should I focus on this week?"*
5. **Day 7:** run `/audit` for the Four-Cs scoreboard.
6. **Day 14:** run `/level-up` to surface and ship one automation. Then weekly.

---

## The Three Ms — operator brain

| M | One-liner |
|---|---|
| **Mindset** | Default Shift, Function Breakdown, Curiosity Rule. *To what extent can AI be leveraged here?* |
| **Method** | Find Constraint → EAD (Eliminate, Automate, Delegate) → Map Process → Pick Autonomy Level → Tie to KPI. |
| **Machine** | Lego Principle, Validation Chain, Bike Method, Intern Rule, Kill Switch. *Boring is beautiful. Workflows beat agents.* |

Full breakdown in `references/3ms-framework.md`.

> *The Three Ms of AI™ is a trademark of Nate Herk. © 2026 Nate Herk.*

## The Four Cs — architecture

| # | Layer | "This layer is in place" test |
|---|---|---|
| 1 | **Context** | Fresh Claude session answers "what does Scale SD do and who works here?" without browsing |
| 2 | **Connections** | "What's in the GHL pipeline today?" → live data, no paste |
| 3 | **Capabilities** | A short phrase triggers a multi-step workflow that produces an artifact |
| 4 | **Cadence** | Laptop closed. Monday morning lead pull lands in Slack on its own |

> *The Four Cs of an AIOS™ is a trademark of Nate Herk. © 2026 Nate Herk.*

---

## Cormac principles (the constitution)

We're building toward a Cormac-style AI-first company. The principles that shape every design decision:

1. **Everything queryable** — every action produces an artifact that goes back into the system.
2. **Token-max, not headcount-max** — uncomfortably high API spend is cheaper than hiring.
3. **Closed loops** — every system has a defined outcome and feeds its result back in.
4. **AI OS** — every workflow runs through the OS. No middleman.
5. **Software factories** — write the test that defines success; let AI implement.
6. **Most advantageous early stage** — design from the ground up to operate this way.
7. **Never outsource conviction or judgment.**

These live in `CLAUDE.md` so the agent reads them on every session.

---

## License + attribution

The AIS-OS framework is MIT-licensed by Nate Herk. The Three Ms of AI™ and The Four Cs of an AIOS™ are his trademarks. Both ship in this repo with attribution. Scale SD's customizations are © Scale SD, LLC.
