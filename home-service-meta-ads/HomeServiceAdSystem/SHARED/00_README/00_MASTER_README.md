# Home Service Static Ad System — Master README

A repeatable agent-team pipeline that takes a home-service client website URL as input and produces launch-ready, stress-tested, on-brand Meta static ad creative concepts with generation-ready JSON prompts.

---

## The system in one sentence

**Input:** client website URL → **Output:** 3-5 launch-ready Meta static ad variation sets (3 variations per concept), each grounded in research, validated by stress test, and structurally cloned from a proven competitor reference but rebranded to the client.

---

## Why this works

What you built ad-hoc once is now formalized so it works on every client:

- **Shared infrastructure persists** across every client (templates, skills, reference library, agent prompts)
- **Per-client work** structured into a 10-folder pipeline that maps 1:1 to the agents
- **Aesthetic taste decisions stay with you** — you hunt for reference ads in the wild that match each strategic concept
- **Technical execution is automated** — agents handle research, strategy, copy, and JSON craft
- **A stress-test gate prevents waste** — concepts get killed BEFORE expensive image generation
- **The reference library compounds** — every competitor ad you save makes the next client's work easier

---

## The pipeline

```
URL ──▶ Agent 1 (Intake Researcher)
         │
         ▼
        Agent 2 (Creative Bible Builder)
         │
         ▼
        Agent 3 (Strategic Lever)
         │
         ▼
        Agent 4 (Asset Curator)  ◀── photos, quotes, offers
         │
         ▼
        Agent 6 (Concept Architect) ──▶ outputs concepts + reference-hunt instructions
         │
         ▼  ◀── YOU hunt for matching competitor ads in Meta Ad Library
         ▼      Convert images to JSON, feed to Agent 5
         │
        Agent 5 (Reference Library Manager) ──▶ banks REF-XXX
         │
         ▼
        Agent 7 (Stress Tester) ◀── HARD GATE: kill weak concepts before image gen
         │
         ▼
        Agent 8 (Copy Writer)
         │
         ▼
        Agent 9 (Brand Translator / Visual Director) ──▶ 3 JSON variations per concept
         │
         ▼
        Agent 10 (Production Brief) ──▶ delivery package: JSONs + refs + handoff
         │
         ▼
        ChatGPT Image (generate) ──▶ Canva (drop logo + footer) ──▶ LAUNCH
         │
         ▼
        Agent 11 (Launch Packager) ◀── OPTIONAL: audiences, KPIs, budget,
                                       lead form questions, kill criteria
```

Agent 0 (Orchestrator) tracks state across the whole pipeline. Agents 1–10 are the **core creative pipeline**. Agent 11 is **optional** — run it when you want a full launch plan, skip it if you handle launch separately.

---

## Folder structure

```
/HomeServiceAdSystem/                       ← Drive root
│
├── /SHARED/                                ← Persists across every client (this folder)
│   ├── 00_README/                          ← System docs
│   ├── 01_quickstart/                      ← New-client onboarding
│   ├── 02_agents/                          ← 11 paste-ready agent prompts
│   ├── 03_templates/                       ← Locked design system, JSON templates
│   ├── 04_reference-library/               ← REF-XXX structural patterns from competitors
│   ├── 05_skills-inventory/                ← Which skills each agent uses
│   └── 06_client-template/                 ← Empty 10-folder template for new clients
│
└── /CLIENTS/
    └── /[ClientName]/                      ← Created per client (copy of 06_client-template)
        ├── 00_intake/                      ← Research dump, brand assets
        ├── 01_bible/                       ← Creative Bible xlsx
        ├── 02_strategy/                    ← Awareness allocation, angle picks
        ├── 03_assets/                      ← Quote bank, offer bank, photos, consent
        ├── 04_concepts/                    ← Concept library + stress test results
        ├── 05_copy/                        ← Headlines, taglines, trust strips per concept
        ├── 06_prompts/                     ← AD-XXX.json files (3 variations each)
        ├── 07_generated/                   ← ChatGPT Image outputs
        ├── 08_final/                       ← Canva-composited final ads
        └── 09_launch/                      ← Budget split, KPIs, kill criteria
```

---

## The locked design system (4-zone, footer-free)

Every standard static ad uses this canvas spec. Branded footer is opt-in only for flyer/print placements, not Meta cold traffic.

| Zone | Height | Purpose | Source |
|---|---|---|---|
| 1 — Brand Mark | top 8% (~145px) | Logo placeholder | Composite in Canva |
| 2 — Hero Visual + Headline | 60% (~1080px) | The pitch | AI generates |
| 3 — Trust Strip | 11% (~200px) | Credibility | AI generates |
| 4 — CTA Block (full-bleed) | 21% (~375px) | The action | AI generates |

**Canvas:** 4:5 vertical, 1440×1800 pixels (Meta feed mobile-first).

The CTA block extends to the bottom edge — no reserved footer zone for standard ads. Meta's platform CTA button + business name handle contact.

---

## The two ad families

The system explicitly separates concepts into two families with different input requirements:

**Family 1 — Social Proof Ads**
- Hero element: customer review card or quote pull-out
- Required input: verbatim quote + customer consent
- Default REF patterns: review-card-on-lifestyle, split-layout-worker-plus-review

**Family 2 — Offer Ads**
- Hero element: offer tag/headline + supporting visual
- Required input: a specific offer with locked terms (numeral, modifier, fine print, expiration)
- Default REF patterns: offer-stack-feature-list, offer-tag-on-action-bg

Concept Architect routes each concept down the right family's path. Visual Director never asks for a customer quote on an offer ad or an offer headline on a proof ad.

---

## The 3-variation framework

Every concept that survives stress test outputs 3 production-ready JSON prompts. The 3 variations differ on **ONE controlled variable: Hero Subject**. Everything else stays locked. A/B data tells you which subject converts best — clean signal, no confounds.

| What changes across variations | What stays locked |
|---|---|
| Hero photo subject only — e.g. **V1 = Founder portrait**, **V2 = Install in progress**, **V3 = Finished install with happy customer** | Headline, all copy, trust strip, CTA, palette, typography, layout, reference structure |

All 3 variations share ~90% structural DNA with the reference image — same layout architecture, same hierarchy, same brand system. They feel like one campaign, not three random ads. Reference adherence target: **90%+** (preserves what made the reference work; small flexibility for brand-fit improvements).

See `/SHARED/03_templates/variation-framework.md` for full rules and approved subject menus by industry.

---

## The reference library compounds

`/SHARED/04_reference-library/` is the system's competitive memory. Every competitor ad you save as REF-XXX benefits every future client. By the 5th client you'll have 30+ structural patterns to compose from.

Reference files contain ONLY structural DNA — zone proportions, hierarchy, design accent positions, photo treatment style. No competitor brand colors, copy, logos, or phone numbers. That's what makes them reusable across clients in different categories.

---

## How to start a new client

See `/SHARED/01_quickstart/QUICKSTART_NEW_CLIENT.md` for the 10-minute onboarding flow.

Short version:
1. Copy `06_client-template/` to `/CLIENTS/[ClientName]/`
2. Open a new Cowork chat with the client's website URL + Drive access
3. Paste Agent 1 (Intake Researcher) prompt
4. Follow the orchestrator pattern through Agents 2–10
5. Hunt for reference ads when Agent 6 says to
6. Generate AD JSONs in ChatGPT Image, drop logos in Canva, launch

---

## What lives where — quick map

| Need to... | Open... |
|---|---|
| Onboard a new client | `01_quickstart/QUICKSTART_NEW_CLIENT.md` |
| Run an agent | `02_agents/AgentXX_*.md` (paste system prompt) |
| Build an ad JSON | `03_templates/ad-json-template.json` |
| Save a competitor ad pattern | `04_reference-library/` + run Agent 5 |
| Know which skill an agent uses | `05_skills-inventory/skills-by-agent.md` |
| Start a new client folder | Copy `06_client-template/` |

---

## Maintenance notes

- **Reference library:** add REFs as you encounter winning competitor ads. Never remove old ones.
- **Agent prompts:** treat as locked. Improve through additions, not rewrites.
- **Templates:** the 4-zone layout is locked. Changes propagate to every future ad — be deliberate.
- **Per-client folders:** never delete. Old work is reference material for future strategy.
