---
title: "Claude Agent Teams"
type: concept
tags: [claude, ai, automation, agent-teams, tools, prompting]
sources: [how-to-build-claude-agent-teams]
updated: 2026-04-12
---

# Claude Agent Teams

A feature in Claude Code that allows multiple AI agents to work simultaneously on a shared task list, communicate directly with each other, and produce high-quality outputs through parallel specialization and internal QA loops.

---

## How They Work

The main Claude Code session acts as an orchestrator. It spawns 3–5 specialized agents, each with:
- A specific role and set of responsibilities
- Files/outputs they exclusively own
- The ability to message other agents directly (without routing through the main session)
- A plan-first mode where they must get approval before executing

Agents inherit all permissions, MCP servers, and file access from the main session. They do NOT inherit conversation history — they only know what the main session explicitly passes in their spawn prompt.

---

## Agent Teams vs Sub-Agents

| Dimension | Agent Teams | Sub-Agents |
|-----------|-------------|------------|
| Communication | Agents talk to each other | Each agent reports only to main session |
| Parallelism | True parallel; agents react to each other | Independent, no cross-talk |
| Cost | ~7× more tokens than a standard session (each teammate has its own context window) | Lower |
| Best for | Complex, multi-domain, QA-intensive | Sequential, focused, single-output tasks |
| Context | Each agent starts fresh | Each agent starts fresh |

---

## The Prompting Formula

1. **State the goal** — agents need this to understand why they have teammates and what success looks like
2. **Name the team and model** — `Create a team of N agents using Sonnet called [Name]`
3. **Define each agent** — role, owned files, who to message when done
4. **Define final deliverables** — what the main session should produce at the end

---

## Rules for High-Quality Teams

- One agent = one territory (no shared file editing)
- Name recipients explicitly in the prompt (don't assume agents know who to contact)
- 3–5 agents max — beyond that, cost exceeds quality gains
- Build QA loops deliberately — assign one agent as reviewer, authorize it to send work back
- Pre-approve tools in project settings to reduce interruptions
- Shut down agents cleanly (let them confirm work is saved before closing)

---

## Enabling Agent Teams

Set in `.claude/settings.json` (project-level):
```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```
Already configured in `agent-teams/.claude/settings.json`. Note: the correct variable is `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` — not `CLAUDE_CODE_ENABLE_TEAMS`.

Use Sonnet for judgment-heavy agents (qualification, copywriting) and Haiku for mechanical agents (data cleaning, formatting). This reduces the 7× token cost significantly.

---

## Applications for Scale SD

The full lead intelligence system uses agent teams as its core automation layer. Four agents — Lead Scout, Lead Qualifier (with [[Playwright MCP]]), Outreach Writer, and QA Exporter — run in parallel to process a scraping batch end-to-end. A separate monthly [[Autonomous Improvement Loop]] team analyzes batch performance and proposes updates to qualification criteria and SMS templates.

See [[Scale SD AI Growth System]] for the complete stack and [[Lead Intelligence Agent Team Plan]] for the LeadOps prompt.

---

## Related Concepts

- [[Playwright MCP]] — browser automation tool used by Lead Qualifier agent
- [[Autonomous Improvement Loop]] — monthly self-improvement cycle using a separate agent team
- [[Scale SD AI Growth System]] — full stack architecture for Scale SD's lead system
- [[Contractor Automation System]] — end-to-end automation Scale SD builds for clients
- [[Lead Warming System]] — multi-channel warmth scoring that feeds prioritization
- [[Setter-Closer Sales Model]] — human execution layer that agent outputs feed into
- [[Client Pipeline (Lead to Fulfillment)]] — downstream pipeline the leads enter once qualified
