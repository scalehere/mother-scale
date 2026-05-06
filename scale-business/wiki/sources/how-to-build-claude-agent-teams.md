---
title: "How to Build Claude Agent Teams Better Than 99% of People"
type: source
tags: [claude, ai, agent-teams, automation, prompting, tools]
sources: [how-to-build-claude-agent-teams]
updated: 2026-04-13
---

> **⚠️ Duplicate — use [[How to Build Claude Agent Teams Better Than 99% of People]](claude-agent-teams-guide.md) instead.** This is an earlier draft of the same source. The canonical summary is `claude-agent-teams-guide.md` (listed in the index). This file is retained for reference but should not be cited or linked in new pages.

# How to Build Claude Agent Teams Better Than 99% of People

Source: `raw/claude-agents/How to Build Claude Agent Teams Better Than 99% of People.md`
Author: Nate Herk (AI Automation) | Published: 2026-03-23

Video tutorial covering the full setup, prompting strategy, dos/don'ts, and live demos for Claude Code's agent teams feature.

---

## What Agent Teams Are

Agent teams differ from sub-agents. **Sub-agents** work independently and return a single result to the main session. **Agent teams** share a task list, can talk directly to each other, work in parallel, and have a main orchestrator ("project manager") managing them.

The key unlock: individual teammates can message each other without routing through the main agent. This enables QA loops — one agent sends work to another agent for review, the reviewer rejects it, and the originator revises.

---

## Setup

Enable by adding one environment variable to `.claude/settings.local.json`:

```json
{
  "env": {
    "CLAUDE_CODE_ENABLE_TEAMS": "true"
  }
}
```

Agent teams are disabled by default (experimental feature). Agents inherit all permissions, MCP servers, skills, and file access from the main session.

---

## Prompting Framework

Nate's pattern for invoking agent teams:

1. **State the goal** — agents wake up with no context. The goal is what gets passed to them so they understand what they're working toward and why they have teammates.
2. **Define the team** — `Create a team of X agents using [Haiku/Sonnet/Opus] called [TeamName]`
3. **Define each agent** — role, specific responsibilities, what files they own, who they message when done, and what triggers their work
4. **Define final deliverables** — what the main session should produce at the end (not what individual agents produce — what you actually want)

### Example Structure
```
Goal: [1–3 sentences on what success looks like]

Create a team of [N] teammates using Sonnet called [TeamName].

Agent 1 — [Name]: [role description]. Owns [file/output]. When done, message [Agent 2].
Agent 2 — [Name]: [role description]. Waits for [Agent 1] message before starting. Owns [file/output].
Agent 3 — [QA/Reviewer]: Reviews all outputs. Sends back to [Agent 1/2] if quality bar not met.

Final deliverables: [list of files/reports the main session should produce]
```

---

## Dos and Don'ts

| Do | Don't |
|----|-------|
| Give each agent their own files to own | Let multiple agents write to the same file |
| Define outputs clearly | Use vague deliverables |
| Name who each agent should message | Assume agents know who to talk to |
| Use 3–5 agents | Build swarms of 10+ |
| Give full context in the goal | Rely on agents having prior conversation history |
| Pre-approve tools in settings to reduce interruptions | — |

---

## Key Rules for Better Teams

1. **Territory** — each agent should own their own files and deliverables exclusively
2. **Direct messaging** — agents can and should talk to each other, not everything routes through the main session
3. **True parallel work** — agent teams shine when agents work simultaneously and react to each other's outputs (not sequential 1→2→3 handoffs)

---

## When to Use Agent Teams vs Sub-Agents

**Use agent teams when:**
- The task has multiple specialized areas
- Those areas need to run in parallel
- Agents need to react to and communicate with each other
- High quality output requires back-and-forth QA loops
- You can afford higher cost for higher quality

**Use sub-agents (not teams) when:**
- Steps are purely sequential and dependent
- You need everything in one context window
- Agents are editing the same files
- The task is simple
- You want to minimize token cost (teams = ~3–5× the cost)

---

## Common Pitfalls and Fixes

| Problem | Fix |
|---------|-----|
| Agents keep stopping to ask permissions | Pre-approve tools in project settings |
| Deliverables feel disjointed/overwritten | Assign strict file owners per agent |
| One agent isn't doing much | Add explicit work assignment or dependency in the prompt |
| Burning too many tokens | Use fewer agents |
| Agents losing their work | Tell them to save everything to temp files they can call on later |
| Wrong approvals | Have yourself approve plans at the start until you understand the flow |

---

## Plan Approval Mode

Agents can be configured to plan first before executing, requiring approval from either the main session or a designated "reviewer" agent before proceeding. Best practice: start with the main session doing approvals, then shift to a dedicated reviewer agent once the flow is understood.

---

## Key Claims

- Agent teams are more expensive and slower than single-agent runs, but produce significantly higher quality when used correctly
- The biggest advantage is the QA feedback loop — agents catching and correcting each other's work
- Tmux terminal enables split-pane view so you can watch each agent think in real time and message them individually
- Context is not inherited — agents only get what the main session explicitly passes in the spawn prompt
- Skill limit: 3–5 agents is the practical ceiling for cost-quality balance

---

## Entities Mentioned

- [[Nate Herk]] (external — AI automation educator)
