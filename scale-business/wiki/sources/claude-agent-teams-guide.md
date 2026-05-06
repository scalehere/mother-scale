---
title: "How to Build Claude Agent Teams Better Than 99% of People"
type: source
tags: [ai, claude, agent-teams, automation, prompting, tooling]
sources: [claude-agent-teams-guide]
updated: 2026-04-12
---

A practical guide (via YouTube transcript) covering how Claude Code agent teams work, how to set them up, how to prompt them effectively, when to use them vs sub-agents, and common pitfalls with fixes.

## What Agent Teams Are

Agent teams differ from sub-agents in one critical way: **teammates can talk to each other directly** without routing through the main session. The main orchestrator (your Claude Code session) creates the team, assigns roles, and manages a shared task list — but individual agents can send messages to each other, hand off work, and loop back (e.g., a QA agent can reject work and send it back to the author).

Sub-agents work independently and return results to the main session. Agent teams work in parallel, communicate laterally, and are ideal when you need coordination across specialized roles.

## Setup

Enable in `settings.local.json` (project-level):
```json
{
  "experimental": {
    "agentTeams": true
  }
}
```
Feature is disabled by default (experimental). Agents inherit all permissions, file access, MCP servers, and skills from the main session.

## How to Prompt Agent Teams

Follow this structure:

1. **State the GOAL** — agents wake up with no prior context; give them the mission and why they have teammates
2. **Declare the team**: "Create a team of X agents using [Haiku/Sonnet/Opus]"
3. **Per agent**: name, role, what they do, what they output, who they message and when
4. **Final deliverables**: what the main session should receive at the end

### Example Pattern
```
GOAL: [what you're trying to accomplish and why]

Create a team of 3 agents using Sonnet:
- Agent 1 [Name]: [role]. Does: [tasks]. Outputs: [file/deliverable]. 
  When done, message Agent 2.
- Agent 2 [Name]: [role]. Waits for Agent 1. Does: [tasks]. Outputs: [file].
  When done, message Agent 3.
- Agent 3 [Name/QA]: Reviews outputs from Agents 1 and 2. If issues found, 
  sends back to original agent. When all pass, finalize.

Final deliverables: [list what the main session should produce]
```

## Dos and Don'ts

**Do:**
- Each agent owns specific files — no shared file editing
- Define outputs explicitly — no vague deliverables
- Name recipients — tell each agent exactly who to message and when
- Use 3–5 agents max
- Give full context in the goal statement (no history is pre-loaded)
- Use plan approval mode — agents plan before executing; main session or QA agent approves

**Don't:**
- Run swarms of 10+ agents (cost scales linearly)
- Let agents share files (causes overwrites)
- Assume agents know who their teammates are without being told
- Use agent teams for simple or sequential tasks (sub-agents are cheaper)

## Key Rules for Better Teams

1. **Territory**: Each agent owns and edits only its own files
2. **Direct messaging**: Agents send messages to each other — no middleman needed
3. **Parallelism**: Agents should be working simultaneously, not in a rigid handoff chain

## Common Pitfalls and Fixes

| Problem | Fix |
|---------|-----|
| Agents keep asking permissions | Pre-approve specific tools in `settings.json` |
| Deliverables are overwritten | Assign strict file ownership per agent |
| An agent is idle/doing nothing | Assign it a specific dependency or parallel task |
| Burning too many tokens | Use fewer agents; drop to 2–3 |
| Agents losing work | Tell them to save everything to temp files |
| Wrong approvals | Be the human approver until you understand the flow |

## When to Use Agent Teams

**Use when:**
- Task has multiple distinct areas that can be parallelized
- Agents need to react to and communicate with each other
- High quality output is required (QA loops add quality gates)
- The task is complex enough to warrant specialization

**Don't use when:**
- Steps are strictly sequential (1 → 2 → 3 with no parallelism)
- Everything needs one shared context window
- Agents would be editing the same files
- Task is simple — sub-agents or a single session is enough

## Visibility: tmux Split-Pane

Running Claude Code in a tmux terminal enables a split-pane view where each agent's thinking and activity is visible in real time. You can also send messages directly to individual agents from the terminal, not just through the main session.

## Key Claims

- Agent teams produce meaningfully higher quality output than single sessions when used correctly — the cost is worth it for complex, parallel work
- The QA loop pattern (agent reviews and rejects/approves work from peers) is the highest-leverage structure
- Plan approval mode before execution significantly reduces wasted tokens from agents going down the wrong path
- 3–5 agents is the practical sweet spot; beyond that, cost and coordination overhead outweigh quality gains
- **Token cost note:** This video estimates agent teams at ~3–5× the token cost of a standard session. However, real-world testing with `settings.json` configurations (per [[Claude Agent Teams]] concept page) shows the actual multiplier closer to **7×**. The 7× figure supersedes the 3–5× estimate for planning purposes.

## Entities Mentioned

- [[Scale SD / ScaleHere]] (applied context)
