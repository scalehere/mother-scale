# Wiki Log

Append-only record of all wiki operations. Newest entries first.

---

## [2026-05-04] analysis | Full Business Context Brief created

- **Type:** analysis (new)
- **Files touched:**
  - `wiki/analysis/business-context-brief.md` (new — full AI handoff document combining website, wiki, and live GHL data)
  - `wiki/index.md` (updated — brief added to analysis table)
- **Notes:** GHL MCP connected (location ID: EUZYYp8JaL4XPDDe7Ihq). Live data pulled: 4 pipelines, 20 opportunities, full contact list. Key findings: SC Floors and UDG confirmed as real Closed Won clients in GHL. Lead sources: Instagram, scraper, cold call, referral, Facebook Group. Cold Outbound pipeline created April 17 — new addition. EMSR opportunity shows $3,500 vs signed contract $2,500 — possible data entry error. Address discrepancy: GHL shows Escondido apt vs website Technology Pl address.

---

## [2026-05-04] update | Website accuracy corrections + team clarification

- **Type:** update (manual corrections from owner)
- **Files touched:**
  - `wiki/entities/scale-sd.md` (updated — real team names + Instagram handles, website placeholder warnings, confirmed real client logos, open issues updated)
  - `wiki/overview.md` (updated — team table with Instagram handles, website accuracy note)
  - `wiki/index.md` (updated — corrected team descriptions, added 5 confirmed real clients from website logos)
- **Notes:**
  - Website (scalehere.com) contains placeholder content: fake team names, unverified trust metrics, placeholder portfolio case studies. Owner confirmed this.
  - Real team: Daniel J Loarca (owner), Justin (@justintgoff), Tad (@tadj.imenez), Ashenafew (@ashenafew).
  - Confirmed real clients via website logos: California Doors & Windows, Designer Window Supply, EMS Restoration, Gutierrez General Zone Construction, Star Builders Inc, United Design Group, World Pools Inc.
  - Client acquisition model clarified: outbound is narrow (contractors only), inbound is open to any industry.
  - Month-to-month vs 3-month minimum discrepancy still unresolved — pending owner clarification.
  - GHL MCP connected — awaiting location ID to pull live account data.

---

## [2026-04-16] ingest | GHL Email Tutorials (2 sources)

- **Type:** ingest (2 sources)
- **Files touched:**
  - `wiki/sources/ghl-email-marketing-tutorial.md` (new — full GHL email system: deliverability, 3 sequences, builder, automations, analytics)
  - `wiki/sources/ghl-email-setup-never-spam.md` (new — 4 levels of GHL email setup, Level 2 = Scale SD current)
  - `wiki/index.md` (updated — 60 → 62 pages)
- **Notes:** Two GHL workflow tutorial transcripts ingested. Third file (AutoResearch) is a stub with no content — skipped. Key findings:
  (1) Scale SD is currently on Level 2 (software-wide `s.scalehere.com`) — the correct default for agencies.
  (2) Level 3 (per-client subdomains) is the recommended upgrade when client volume grows — already unblocked since DNS moved to GoDaddy.
  (3) Three email sequence types to build: Welcome, Sales Follow-Up, Newsletter.
  (4) GHL automation structure documented — templates → workflows → publish.
  (5) Business Profile settings to enable: hard bounce marking, email verification, unsubscribe link auto-append.

---

## [2026-04-15] analysis | Email & DNS Setup — fully verified and live

- **Type:** analysis (updated)
- **Files touched:**
  - `wiki/analysis/email-dns-setup.md` (updated — full DNS migration completed, all records verified)
- **Notes:** Full DNS migration from Wix to GoDaddy completed. All records verified live:
  (1) Google Workspace SPF, DKIM, DMARC — team emails fully authenticated.
  (2) GHL Lead Connector `mail.scalehere.com` — SPF, 2× DKIM, DMARC, CNAME, MX all verified in GHL.
  (3) Wix website A records intact — site still working.
  (4) MX records for `mail.scalehere.com` now live (was blocked by Wix) — GHL can now route inbound replies.
  (5) Level 3 upgrade (per-client subdomains) is now unblocked — GoDaddy supports all record types.

---

## [2026-04-14] ingest | Transcripts — Victor Pilar Setup 1 & 2

- **Type:** ingest (2 call transcripts)
- **Files touched:**
  - `wiki/sources/calls/2026-04-13-victor-pilar-onboarding-1.md` (new — 40-min setup call: FB account creation, scope/pricing)
  - `wiki/sources/calls/2026-04-13-victor-pilar-onboarding-2.md` (new — 12-min follow-up: payment confirmed, strategy, pro shoot)
  - `wiki/entities/victor.md` (updated — now "Victor Pilar", full contract details, strategy, pain points, open items)
  - `wiki/overview.md` (updated — Victor added to Active Clients, MRR updated to $7,000/mo)
  - `wiki/analysis/action-items.md` (updated — Victor team tasks expanded from 3 to 10, new "Victor Pilar (Client)" section added)
  - `wiki/index.md` (updated — 2 call pages added, Victor entity updated, 57 → 59 pages)
- **Notes:** Victor Pilar is now a **signed, paying client** at $1,500/mo for content/organic on FB+IG. Payment confirmed during Setup 2 call. Key findings:
  (1) Signed MRR jumps from $5,500 to $7,000/mo.
  (2) Victor initially confused $1,500 as including ads — clarified that ads management is +$500/mo, ad spend (~$30/day) separate. Needs written confirmation in updated agreement.
  (3) Content-first strategy: 1–2 weeks organic warmup before ads.
  (4) Strategy review meeting: Wednesday April 15 at 6:00 PM.
  (5) Pro video shoot planned ~1–2 weeks out when current project finishes.
  (6) Potential upsells: ads management (+$500/mo), Google/Yelp ($200–$500), website/SEO (~$1,000).
  (7) "NRGY HUB" used as the agency name on both calls — unclear if this is a third brand alongside Scale SD and ScaleHere. Flagged for clarification.
  **Contradiction flagged:** Victor's entity previously listed as "New contact — Facebook account setup pending." Now confirmed as signed client with payment received.

---

## [2026-04-13] lint | Full cleanup — 15 of 17 issues resolved, 2 remain

- **Type:** lint
- **Files touched:**
  - `wiki/entities/scale-sd.md`, `wiki/entities/gohighlevel.md`, `wiki/concepts/revenue-partner-positioning.md` — broken slug `contractor-automation-growth-plan-v2` fixed
  - `wiki/entities/california-doors-and-windows.md`, `wiki/entities/vip-general-contractor.md`, `wiki/entities/daniel.md` — broken slug `scale-sd-propsals` fixed
  - `wiki/entities/daniel.md`, `wiki/concepts/setter-closer-model.md` — broken slugs `scale-sd-setter-closer-strategy` and `objection-handling-guide-sd-contractors` fixed
  - `wiki/sources/swot-analysis.md` — `[[Daniel]]` → `[[Daniel J Loarca]]`
  - `wiki/analysis/claude-agent-team-lead-pipeline.md`, `wiki/analysis/lead-pipeline-agent-prompt.md` — `[[Claude Agent Teams Guide]]` → `[[Claude Agent Teams]]`
  - `wiki/sources/claude-agent-teams-guide.md` — token cost note added (7× supersedes 3–5×)
  - `wiki/sources/how-to-build-claude-agent-teams.md` — deprecated as duplicate draft
  - `wiki/analysis/lint-2026-04-13.md` — status table updated to final state
- **Notes:** 15 of 17 lint issues resolved. 2 remain: (1) Nate Herk plain-text link (low priority); (2) Tony missing company name/location (needs human input).

---

## [2026-04-13] lint | Re-lint — 6 issues fixed, 7 still open

- **Type:** lint
- **Files touched:**
  - `wiki/analysis/lint-2026-04-13.md` (updated — re-lint status table added)
  - `wiki/overview.md` (updated — Tony added to Active Clients, MRR corrected to $5,500/mo, source count updated, EMSR paid ads question removed, broken slug fixed in frontmatter)
  - `wiki/entities/victor.md` (updated — full Meta account setup context added: wife's Facebook, Partner access structure, organic + paid ads scope)
  - `wiki/analysis/action-items.md` (updated — stale Victor meeting task replaced with 3 current Victor onboarding tasks)
  - `wiki/index.md` (updated — 2 orphan analysis pages added, page count 55 → 57)
- **Notes:** Re-lint triggered after Victor Facebook/Instagram onboarding session. 6 of 17 prior issues resolved. Remaining open: agent teams cost note, broken slugs in 6 entity/concept pages, 3 broken cross-reference links, Nate Herk link, possible duplicate source pages, Tony missing company name/location.

---

## [2026-04-13] lint | 2026-04-13 — 2 contradictions, stale MRR, 2 orphan pages, broken slugs

- **Type:** lint
- **Files touched:**
  - `wiki/analysis/lint-2026-04-13.md` (new — full audit report, 17 issues found)
  - `wiki/index.md` (updated — lint report added, page count 54 → 55)
- **Notes:** Full audit of all 54 pages. Top findings: (1) EMSR service agreement source page still says "no paid ads in scope" — contradicted by the General Strategy doc ingested today; (2) MRR in overview.md is understated — Tony ($1,000/mo) missing, actual signed MRR is $5,500+; (3) Two analysis pages (`claude-agent-team-lead-pipeline.md` + `lead-pipeline-agent-prompt.md`) exist on disk but are not in the index; (4) Multiple broken source slugs in frontmatter across entity and concept pages; (5) Possible duplicate source files for the Claude agent teams guide. Prioritized fix list in lint report.

---

## [2026-04-13] analysis | EMSR Foundation Phase tasks added to action items

- **Type:** analysis (action items update)
- **Files touched:**
  - `wiki/analysis/action-items.md` (updated — EMSR Foundation Phase tasks added across Ashen, Justin, and Team sections)
- **Notes:** Added ~20 Foundation Phase tasks from the EMSR General Strategy doc. Ashen owns: GHL setup (highest priority), Meta/IG access, ads setup, landing pages. Justin owns: TikTok access, media audit, profile remodel, cyclical posting. Team owns: Facebook Business Page admin access, competitive intelligence setup.

---

## [2026-04-13] ingest | EMS Restorations General Strategy

- **Type:** ingest (source)
- **Files touched:**
  - `wiki/sources/ems-restorations-general-strategy.md` (new — full ads strategy, growth plan, execution checklist)
  - `wiki/entities/emsr.md` (updated — ads scope confirmed, three-phase strategy, key metrics, two systems, portfolio context revised)
  - `wiki/entities/joseph-fiasco.md` (updated — communication style, goals, background context, client responsibilities)
  - `wiki/index.md` (updated — 53 → 54 pages)
- **Notes:** Internal strategy document for the EMSR ads team. Key findings:
  (1) Scope is broader than previously documented — $2,500/mo covers content + posting; 8% of ad spend covers ads management (paid ads IS in scope, contradicting earlier "no paid ads" note in EMSR entity).
  (2) Primary KPI: reduce cost per scheduled appointment from $456 (current minimum) to $250 or less.
  (3) Long-term goal: scale EMSR's ad spend to $40,000/month by end of 2026 — this makes EMSR potentially Scale SD's largest revenue driver.
  (4) Joseph is explicitly a numbers-first communicator — no jargon, data-grounded reports only.
  (5) GHL setup for Joseph flagged as highest-priority task (highlighted in source).
  (6) Peak season is January–June; approximately 6–8 weeks remain — speed of execution is the most important variable.
  (7) Two operational systems identified: Intelligence & Analysis Loop (informs what to produce) + Execution System (produces and posts).
  **Contradiction flagged:** Previous EMSR entity page stated "No paid ads management in current scope." This document confirms paid ads (Meta + TikTok) ARE in scope. EMSR entity updated accordingly.

---

## [2026-04-13] ingest | Transcript — Daily Team Check-In (Ashen, Justin, Daniel)

- **Type:** ingest (call transcript)
- **Files touched:**
  - `wiki/sources/calls/2026-04-13-daily-team-check-in.md` (new — call summary, action items, decisions)
  - `wiki/entities/tony.md` (new — pool contractor client, upsell plan)
  - `wiki/entities/victor.md` (new — new contact, FB account setup pending)
  - `wiki/entities/emsr.md` (updated — Facebook access status section added)
  - `wiki/entities/justin.md` (updated — EMSR content management role, FB account limitation)
  - `wiki/entities/ashane.md` (updated — lead qualification system status, Tony GHL deadline)
  - `wiki/entities/daniel.md` (updated — Tony upsell strategy and timeline)
  - `wiki/index.md` (updated — Calls section populated, Tony and Victor added to Entities)
- **Notes:** 16-min team check-in covering three threads: (1) EMSR Facebook access resolved via Dani's account — permanent fix pending Justin adding email to FB profile; (2) Ashen's lead qualification system (Claude agents + Playwright) 95% complete, ~150 leads due Apr 14 AM; (3) Tony upsell plan agreed — Dani to propose $500/mo add-on by Apr 15, 90-day target $1,750/mo total. Victor (new contact) scheduled for FB account setup same evening. No credentials stored in wiki.

---

## [2026-04-13] analysis | Full system synthesis — Scale SD AI Growth System master plan

- **Type:** analysis (master strategic document)
- **Files touched:**
  - `wiki/analysis/scale-sd-ai-growth-system.md` (new — **master document**, full 6-layer system architecture)
  - `wiki/analysis/leadops-claude-md-template.md` (new — ready-to-copy CLAUDE.md for scale-lead-ops project)
  - `wiki/concepts/playwright-mcp.md` (new — Playwright MCP concept page)
  - `wiki/concepts/autonomous-improvement-loop.md` (new — AutoResearch-adapted improvement loop concept page)
  - `wiki/concepts/claude-agent-teams.md` (updated — fixed env var, added Playwright MCP + Improvement Loop links, corrected 3–5× cost to ~7×)
  - `wiki/analysis/lead-intelligence-agent-team-plan.md` (updated — corrected env var from `CLAUDE_CODE_ENABLE_TEAMS` to `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`)
  - `wiki/index.md` (updated — 46 → 51 pages, Analysis section expanded)
- **Notes:** Synthesized everything in `agent-teams/` folder and `scale-business/raw/claude-agents/` into a single operating architecture. Key integrations beyond the prior plan:
  (1) Playwright MCP — Agent 2 (Lead Qualifier) visits each lead's website/GMB/social in a live browser instead of scoring from URL metadata. Transforms qualification accuracy.
  (2) AutoResearch pattern adapted as the Autonomous Improvement Loop — monthly agent team analyzes batch performance data, proposes specific changes to the qualification rubric and SMS templates, keeps only what measurably improves close rate. The qualification criteria and SMS copy become compounding assets.
  (3) Correct env var identified from agent-teams/.claude/settings.json: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (not `CLAUDE_CODE_ENABLE_TEAMS`).
  (4) Full revenue math documented: conservative target $3,000–$6,000 new MRR/month; aggressive target $8,000–$16,000/month at full throughput.
  (5) The master document includes a day-by-day Week 1 setup checklist and a week-by-week implementation timeline through Month 2+.
  Implementation starts at `/Users/ashenafew/Desktop/SCALE/scale-lead-ops/` — create this folder as Step 1.

---

## [2026-04-12] ingest + analysis | Claude Agent Teams guides → Lead Intelligence Agent Team Plan

- **Type:** ingest (2 sources) + analysis (1)
- **Files touched:**
  - `wiki/sources/claude-agent-teams-guide.md` (updated — confirmed existing page covers Nate Herk's framework)
  - `wiki/sources/unlimited-website-clients-outreach.md` (updated — confirmed existing page covers Pavlo's outreach system)
  - `wiki/concepts/claude-agent-teams.md` (new — concept page for agent teams framework with Scale SD applications)
  - `wiki/analysis/lead-intelligence-agent-team-plan.md` (new — full architecture, roadmap, and ready-to-use prompt)
  - `wiki/index.md` (updated — 42 → 46 pages, analysis section populated for first time)
- **Notes:** Owner requested a plan for implementing Claude agent teams to automate Scale SD's lead intelligence pipeline. Key synthesis: the manual analysis step (Ashen + Tad reviewing 6 channels per lead) is the primary bottleneck limiting Scale SD to 150 leads/week and creating inconsistent call prep quality. The agent team architecture ("LeadOps") replaces this with 4 specialized agents — Lead Scout (data processor), Lead Qualifier (6-channel scoring), Outreach Writer (SMS sequences + caller notes), and QA Exporter (review + GHL format). A complete, ready-to-use Claude Code prompt is included in the analysis page. Full roadmap: 4 phases from setup through scale. Revenue upside at full throughput: 450 leads/week → potential $4.5K–$10.5K new MRR per week. No contradictions with existing wiki content.

---

## [2026-04-12] ingest | Lead Warming System, Client Intake Form, Social Media Strategy for Sales, Strategic Marketing Management, EMSR Service Agreement, Social Media Content Optimization Process

- **Type:** ingest (6 sources)
- **Files touched:**
  - `wiki/sources/lead-warming-system.md` (new)
  - `wiki/sources/client-intake-form.md` (new)
  - `wiki/sources/social-media-strategy-for-sales.md` (new)
  - `wiki/sources/strategic-marketing-management.md` (new)
  - `wiki/sources/emsr-service-agreement.md` (new)
  - `wiki/sources/social-media-content-optimization.md` (new)
  - `wiki/entities/justin.md` (new — team member, internal organic metrics + AI training)
  - `wiki/entities/emsr.md` (new — signed client $2,500/mo, restoration contractor)
  - `wiki/entities/joseph-fiasco.md` (new — owner of EMSR)
  - `wiki/entities/ashane.md` (updated — added paid ads analytics and AI training roles)
  - `wiki/entities/tad.md` (updated — added external organic metrics and AI training roles)
  - `wiki/concepts/lead-warming-system.md` (new)
  - `wiki/concepts/ai-ad-pipeline.md` (new)
  - `wiki/concepts/g-stic-framework.md` (new)
  - `wiki/overview.md` (updated — team expanded, active client table added, MRR documented)
  - `wiki/index.md` (updated — 27 → 42 pages)
- **Notes:** Major ingest batch — all raw documents now processed. Key findings:
  (1) EMSR is a newly signed client at $2,500/mo (highest value to date), signed April 8, 2026 by Joseph Fiasco.
  (2) Justin is a previously undocumented team member; owns internal organic metrics and AI pipeline development.
  (3) The Lead Warming System and AI Ad Pipeline are two linked systems: organic engagement feeds warmth scores, warm leads feed retargeting, and best-performing organic content becomes ad creative.
  (4) Strategic Marketing Management introduces G-STIC as a formal planning framework applicable across all agency strategy work.
  (5) Confirmed Scale SD address: 10918 Technology PL, San Diego CA 92025.
  Current signed MRR: $4,500/month. All raw documents ingested — no unprocessed sources remaining.

---

## [2026-04-12] ingest | Complete Client Journey, Ads Onboarding, Lead Generation System

- **Type:** ingest (3 sources)
- **Files touched:**
  - `wiki/sources/complete-client-journey-ghl.md` (new)
  - `wiki/sources/ads-onboarding-fulfillment.md` (new)
  - `wiki/sources/lead-generation-qualification-system.md` (new)
  - `wiki/entities/ashane.md` (new)
  - `wiki/entities/tad.md` (new)
  - `wiki/entities/scale-sd.md` (updated — team expanded to 5–6 people)
  - `wiki/concepts/client-pipeline.md` (new)
  - `wiki/index.md` (updated)
- **Notes:** Key findings: Full operational SOPs now documented — 22-day client pipeline, ads build
  process, and lead gen system. New team members identified: Ashen and Tad own lead scraping/qualification
  (150 leads/week). Calling window is 11am–1pm Tue–Sat (10 hrs/week) — the core constraint the whole
  lead gen system is built around. ClickUp/Notion used for project management alongside GHL.
  5 sources remain in raw/.
  **Next batch:** Social Media Content Optimization, Lead Warming System, Social Media Strategy for Getting Sales.

---

## [2026-04-12] ingest | Proposals, Setter & Closer Strategy, Objection Handling Guide

- **Type:** ingest (3 sources)
- **Files touched:**
  - `wiki/sources/proposals.md` (new)
  - `wiki/sources/setter-closer-strategy.md` (new)
  - `wiki/sources/objection-handling-guide.md` (new)
  - `wiki/entities/california-doors-and-windows.md` (new)
  - `wiki/entities/vip-general-contractor.md` (new)
  - `wiki/entities/daniel.md` (updated — full name Daniel J Loarca, LLC confirmed)
  - `wiki/concepts/setter-closer-model.md` (new)
  - `wiki/index.md` (updated)
- **Notes:** Key findings: Scale SD is an LLC. One confirmed active client (California Doors & Windows,
  $2k/mo, Dec 2025). One hot prospect pending signature (VIP General Contractor, $1.5k/mo, April 8 2026).
  Sales system is setter (volume outreach) + closer (Daniel). Opening script targets missed-call pain.
  Objection handling is well-documented across 4 objection types. 8 sources remain in raw/.
  **Next batch:** Complete_Client_Journey_GoHighLevel, Ads_Onboarding_Fulfillment_Process, Lead Generation System.

---

## [2026-04-12] ingest | Packages, SWOT Analysis, Contractor Automation Growth Plan

- **Type:** ingest (3 sources)
- **Files touched:**
  - `wiki/sources/packages.md` (new)
  - `wiki/sources/swot-analysis.md` (new)
  - `wiki/sources/contractor-automation-growth-plan.md` (new)
  - `wiki/entities/scale-sd.md` (new)
  - `wiki/entities/daniel.md` (new)
  - `wiki/entities/gohighlevel.md` (new)
  - `wiki/concepts/revenue-partner-positioning.md` (new)
  - `wiki/concepts/contractor-automation-system.md` (new)
  - `wiki/overview.md` (updated)
  - `wiki/index.md` (updated)
- **Notes:** First 3 strategic sources ingested. Key finding: agency is mid-pivot from marketing vendor
  to revenue partner. Core offer is 5-component automation system on GoHighLevel. Tiered package
  structure: Foundation → Growth → Scale. Team is 4 people (Daniel + 2 + intern). Critical weakness:
  internal systems not yet fully dialed in before aggressive client acquisition. 11 sources remain in raw/.
  **Next batch:** Setter & Closer Strategy, Objection Handling Guide, and one of: Lead Gen System or Proposals.

---

## [2026-04-12] setup | Domain defined — ScaleHere / Scale SD

- **Type:** setup
- **Files touched:** `CLAUDE.md`, `wiki/overview.md`
- **Notes:** Domain clarified by owner. Wiki is the central operating brain for ScaleHere
  (scalehere.com / Scale SD), a marketing agency. 14 documents are queued in `raw/` awaiting
  ingest. Overview updated with agency description and open questions.
  **Next step:** Begin ingesting raw documents.

---

## [2026-04-12] setup | Wiki initialized

- **Type:** setup
- **Files touched:** `CLAUDE.md`, `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`
- **Notes:** Wiki created from scratch. Directory structure established:
  `raw/`, `raw/assets/`, `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`,
  `wiki/analysis/`. Schema v1.0 written. Domain is `scale-business` — to be refined
  after first ingests. No sources processed yet.
  **Next step:** Drop your first source file into `raw/` and say "ingest [filename]".
