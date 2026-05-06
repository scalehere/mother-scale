# Agent Teams — Master Reference Guide

> Source: https://code.claude.com/docs/en/agent-teams  
> Last updated: 2026-04-12  
> Requires: Claude Code v2.1.32+, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

---

## Table of Contents

1. [What Are Agent Teams](#1-what-are-agent-teams)
2. [Agent Teams vs Subagents](#2-agent-teams-vs-subagents)
3. [Enabling Agent Teams](#3-enabling-agent-teams)
4. [Architecture](#4-architecture)
5. [Starting a Team](#5-starting-a-team)
6. [Display Modes](#6-display-modes)
7. [Controlling the Team](#7-controlling-the-team)
8. [Task System](#8-task-system)
9. [Communication & Context](#9-communication--context)
10. [Hooks for Quality Gates](#10-hooks-for-quality-gates)
11. [Permissions](#11-permissions)
12. [Token Costs](#12-token-costs)
13. [Best Practices](#13-best-practices)
14. [Use Case Examples](#14-use-case-examples)
15. [Limitations](#15-limitations)
16. [Troubleshooting](#16-troubleshooting)
17. [Quick Reference Cheatsheet](#17-quick-reference-cheatsheet)

---

## 1. What Are Agent Teams

Agent teams coordinate multiple Claude Code instances working together. One session is the **team lead** — it creates the team, spawns teammates, assigns tasks, and synthesizes results. **Teammates** each run in their own context window and can communicate directly with each other (not just back to the lead).

**Key distinction from subagents:** teammates can message each other laterally. Subagents only report back to the caller.

**Best for:**
- Research/review tasks requiring parallel investigation
- New modules/features that can be owned independently
- Debugging with competing hypotheses
- Cross-layer work (frontend + backend + tests)

**Not ideal for:**
- Sequential tasks
- Same-file edits
- Work with many inter-dependencies
- Routine tasks (single session is more cost-effective)

---

## 2. Agent Teams vs Subagents

| Dimension | Subagents | Agent Teams |
|:---|:---|:---|
| Context | Own context window; results return to caller | Own context window; fully independent |
| Communication | Report results back to main agent only | Teammates message each other directly |
| Coordination | Main agent manages all work | Shared task list with self-coordination |
| Best for | Focused tasks where only the result matters | Complex work requiring discussion and collaboration |
| Token cost | Lower — results summarized back to main context | Higher — each teammate is a separate Claude instance |

**Rule of thumb:** Use subagents when you need quick focused workers. Use agent teams when teammates need to share findings, challenge each other, and coordinate autonomously.

---

## 3. Enabling Agent Teams

Set the environment variable in `.claude/settings.json` (project-level) or `~/.claude.json` (global):

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Or in your shell environment:
```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

---

## 4. Architecture

| Component | Role |
|:---|:---|
| **Team lead** | The main Claude Code session — creates the team, spawns teammates, coordinates work |
| **Teammates** | Separate Claude Code instances, each working on assigned tasks |
| **Task list** | Shared list of work items that teammates claim and complete |
| **Mailbox** | Messaging system for direct communication between agents |

**File locations (auto-managed, do not edit by hand):**
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

The `config.json` holds runtime state (session IDs, tmux pane IDs). It is overwritten on every state update — do not pre-author or manually edit it.

The `members` array in the team config contains each teammate's name, agent ID, and agent type. Teammates can read this file to discover each other.

> There is no project-level team config. A file like `.claude/teams/teams.json` in the project directory is not recognized — Claude treats it as an ordinary file.

---

## 5. Starting a Team

Tell Claude to create a team in natural language. Specify the task and the team structure:

```
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Create an agent team to explore this from different angles: one
teammate on UX, one on technical architecture, one playing devil's advocate.
```

Claude will:
1. Create a team with a shared task list
2. Spawn teammates for each role
3. Have teammates explore in parallel
4. Synthesize findings
5. Attempt to clean up when finished

You can also specify teammate count and models explicitly:

```
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

**Two ways teams start:**
- **You request one** — Claude creates it based on your instructions
- **Claude proposes one** — Claude suggests a team and you confirm before it proceeds

Claude will never create a team without your approval.

---

## 6. Display Modes

### In-Process (default when not in tmux)
All teammates run inside your main terminal.
- `Shift+Down` — cycle through teammates
- Type to send a message directly to the active teammate
- `Enter` — view a teammate's session
- `Escape` — interrupt their current turn
- `Ctrl+T` — toggle the task list

### Split Panes (default when inside tmux)
Each teammate gets its own pane. Click into a pane to interact directly.
- Requires **tmux** or **iTerm2 with `it2` CLI**

### Configuration

Set globally in `~/.claude.json`:
```json
{
  "teammateMode": "in-process"
}
```

Or override per session:
```bash
claude --teammate-mode in-process
```

Valid values: `"auto"` (default), `"in-process"`, `"tmux"`

**`"auto"` behavior:** uses split panes if already inside a tmux session, otherwise in-process.

**Installing split-pane dependencies:**
- tmux: install via package manager (see [tmux wiki](https://github.com/tmux/tmux/wiki/Installing))
- iTerm2: install `it2` CLI, enable Python API in iTerm2 → Settings → General → Magic → Enable Python API

> Split-pane mode is NOT supported in VS Code's integrated terminal, Windows Terminal, or Ghostty.

---

## 7. Controlling the Team

All control is through natural language to the lead.

### Require Plan Approval Before Implementation

```
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

Flow:
1. Teammate works in read-only plan mode
2. Teammate sends plan approval request to lead
3. Lead reviews — approves or rejects with feedback
4. If rejected, teammate revises and resubmits
5. Once approved, teammate exits plan mode and begins implementation

To influence the lead's approval criteria:
```
Only approve plans that include test coverage. Reject plans that modify the database schema.
```

### Talk to Teammates Directly

Any teammate is a full independent Claude Code session — message them directly without going through the lead.

### Naming Teammates

The lead assigns names when spawning. For predictable names you can reference later:
```
Spawn a teammate named "security-reviewer" to audit the auth module.
```

### Using Subagent Definitions as Teammates

Reference a defined subagent type by name:
```
Spawn a teammate using the security-reviewer agent type to audit the auth module.
```

The teammate honors that definition's `tools` allowlist and `model`. The definition body is **appended** to the teammate's system prompt (not replacing it). Team coordination tools (`SendMessage`, task management tools) are always available even when `tools` restricts others.

> `skills` and `mcpServers` frontmatter in subagent definitions are **not** applied when running as a teammate. Teammates load these from project/user settings like a regular session.

### Shutting Down a Teammate

```
Ask the researcher teammate to shut down
```

The lead sends a shutdown request. The teammate can approve (graceful exit) or reject with an explanation.

### Cleaning Up the Team

```
Clean up the team
```

This removes all shared team resources. **Always use the lead to clean up** — teammates should not run cleanup because their team context may not resolve correctly. The lead checks for active teammates first and fails if any are still running (shut them down first).

---

## 8. Task System

The shared task list coordinates work across the team.

### Task States
- **Pending** — not yet claimed
- **In progress** — claimed by a teammate
- **Completed** — done

### Task Dependencies
Tasks can depend on other tasks. A pending task with unresolved dependencies cannot be claimed until those dependencies complete. The system resolves this automatically — no manual intervention needed.

### Task Claiming
- **Lead assigns** — tell the lead which task to give to which teammate
- **Self-claim** — after finishing, a teammate picks up the next unassigned, unblocked task on its own

Task claiming uses **file locking** to prevent race conditions when multiple teammates try to claim the same task simultaneously.

### Task Sizing Guidelines

| Size | Problem |
|:---|:---|
| Too small | Coordination overhead exceeds benefit |
| Too large | Teammates work too long without check-ins; risk of wasted effort |
| Just right | Self-contained units with a clear deliverable (a function, a test file, a review) |

Target **5-6 tasks per teammate**. This keeps everyone productive and lets the lead reassign work if someone gets stuck.

---

## 9. Communication & Context

### What Teammates Load on Spawn
- Same project context as a regular session: `CLAUDE.md`, MCP servers, skills
- Spawn prompt from the lead
- **Does NOT inherit the lead's conversation history**

Always include task-specific context in the spawn prompt:
```
Spawn a security reviewer teammate with the prompt: "Review the authentication module
at src/auth/ for security vulnerabilities. Focus on token handling, session
management, and input validation. The app uses JWT tokens stored in
httpOnly cookies. Report any issues with severity ratings."
```

### How Information Flows

| Mechanism | Description |
|:---|:---|
| Automatic message delivery | Teammate messages are delivered automatically to recipients — the lead does not need to poll |
| Idle notifications | When a teammate finishes, it automatically notifies the lead |
| Shared task list | All agents can see task status and claim available work |

### Messaging Types

| Type | Behavior | Cost |
|:---|:---|:---|
| `message` | Send to one specific teammate | Standard |
| `broadcast` | Send to all teammates simultaneously | Scales with team size — use sparingly |

---

## 10. Hooks for Quality Gates

Three hook events are specific to agent teams. All fire on every occurrence (no matcher support).

### `TeammateIdle`

Fires when a teammate is about to go idle.

**Input fields (in addition to common fields):**
```json
{
  "hook_event_name": "TeammateIdle",
  "teammate_name": "implementer",
  "team_name": "my-project"
}
```

**Exit code behavior:**
| Exit | Effect |
|:---|:---|
| `0` | Teammate goes idle |
| `2` | Teammate continues working; stderr is fed back as feedback |
| JSON `{"continue": false}` | Stops the teammate entirely (same as Stop hook) |

---

### `TaskCreated`

Fires when a task is being created via the `TaskCreate` tool.

**Input fields:**
```json
{
  "hook_event_name": "TaskCreated",
  "task_id": "task-001",
  "task_subject": "Implement user authentication",
  "task_description": "Add login and signup endpoints",
  "teammate_name": "implementer",
  "team_name": "my-project"
}
```

**Exit code behavior:**
| Exit | Effect |
|:---|:---|
| `0` | Task is created |
| `2` | Task creation prevented; stderr feedback to Claude |
| JSON `{"continue": false}` | Stops the teammate entirely |

**Example — enforce naming conventions:**
```bash
#!/bin/bash
SUBJECT=$(jq -r '.task_subject' < /dev/stdin)

if [[ ! "$SUBJECT" =~ ^[A-Z] ]]; then
  echo "Task subject must start with a capital letter" >&2
  exit 2
fi

exit 0
```

---

### `TaskCompleted`

Fires when a task is being marked as completed.

**Input fields:**
```json
{
  "hook_event_name": "TaskCompleted",
  "task_id": "task-001",
  "task_subject": "Implement user authentication",
  "task_description": "Add login and signup endpoints",
  "teammate_name": "implementer",
  "team_name": "my-project"
}
```

**Exit code behavior:**
| Exit | Effect |
|:---|:---|
| `0` | Task marked complete |
| `2` | Task completion prevented; stderr feedback to Claude |
| JSON `{"continue": false}` | Stops the teammate entirely |

**Example — require test coverage:**
```bash
#!/bin/bash
TASK_ID=$(jq -r '.task_id' < /dev/stdin)

if ! grep -q "test.*$TASK_ID" test-coverage.log; then
  echo "Task must have test coverage before completion" >&2
  exit 2
fi

exit 0
```

---

### Hook Exit Code Summary

| Hook | Exit 0 | Exit 2 | `{"continue": false}` |
|:---|:---|:---|:---|
| `TeammateIdle` | Teammate goes idle | Teammate keeps working | Stops teammate entirely |
| `TaskCreated` | Task created | Task creation blocked | Stops teammate entirely |
| `TaskCompleted` | Task marked complete | Completion blocked | Stops teammate entirely |

---

## 11. Permissions

- Teammates start with the **lead's permission settings**
- If lead runs `--dangerously-skip-permissions`, all teammates do too
- You can change individual teammate permission modes after spawning
- You **cannot** set per-teammate modes at spawn time

**Reducing permission friction:** Pre-approve common operations in permission settings before spawning teammates so requests don't bubble up constantly.

---

## 12. Token Costs

Agent teams are significantly more expensive than single sessions.

**Cost multiplier:** Agent teams use approximately **7x more tokens** than standard sessions when teammates run in plan mode (each teammate maintains its own full context window).

### Cost Reduction Strategies

| Strategy | Detail |
|:---|:---|
| Use Sonnet for teammates | Balances capability and cost for coordination tasks |
| Keep teams small | Token usage is roughly proportional to team size |
| Keep spawn prompts focused | Everything in the spawn prompt adds to teammate context from the start |
| Clean up when done | Active teammates continue consuming tokens even when idle |
| Keep tasks small and self-contained | Limits per-teammate token usage |

### When the Extra Cost Is Worth It
- Research, review, and parallel exploration tasks
- New feature development with clearly separated domains
- Debugging with competing hypotheses that need parallel investigation

### When to Use a Single Session Instead
- Routine, sequential tasks
- Any task where teammates would block on each other
- Simple tasks that don't benefit from parallel exploration

---

## 13. Best Practices

### Team Size
- **Start with 3-5 teammates** for most workflows
- Scale up only when work genuinely benefits from simultaneous work
- Three focused teammates often outperform five scattered ones
- Beyond ~5 teammates: coordination overhead and costs increase, returns diminish

### Task Design
- Target **5-6 tasks per teammate**
- Each task should have a clear, self-contained deliverable
- Break work so each teammate owns **different files** — two teammates editing the same file leads to overwrites

### Context
- Always include task-specific details in the spawn prompt — teammates don't inherit the lead's history
- `CLAUDE.md` works normally — teammates read it from their working directory

### Steering
- Monitor progress actively; don't let the team run unattended too long
- If the lead starts implementing instead of delegating: `"Wait for your teammates to complete their tasks before proceeding"`
- Redirect approaches that aren't working early, before tokens are wasted

### First-Time Use
Start with tasks that have clear boundaries and don't require code changes: reviewing a PR, researching a library, investigating a bug. These show the value of parallel exploration without coordination challenges.

---

## 14. Use Case Examples

### Parallel Code Review

Split review criteria into independent domains so each gets thorough attention:

```
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

### Parallel Feature Development

Each teammate owns a separate piece without file conflicts:

```
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

### Competing Hypothesis Debugging

Force adversarial investigation — each teammate tries to disprove the others:

```
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```

Why this works: Sequential investigation suffers from anchoring — once one theory is explored, subsequent investigation is biased toward it. Adversarial parallel investigation finds the theory that survives challenge.

### Multi-Perspective Research

Use for design decisions requiring exploration from different angles:

```
I'm designing a CLI tool that helps developers track TODO comments across
their codebase. Create an agent team to explore this from different angles: one
teammate on UX, one on technical architecture, one playing devil's advocate.
```

---

## 15. Limitations

These are current known limitations of the experimental feature:

| Limitation | Detail |
|:---|:---|
| No session resumption | `/resume` and `/rewind` do not restore in-process teammates. After resuming, the lead may try to message non-existent teammates — spawn new ones |
| Task status can lag | Teammates sometimes fail to mark tasks complete, blocking dependent tasks. Check if work is actually done and update manually or nudge via the lead |
| Slow shutdown | Teammates finish their current request/tool call before shutting down |
| One team per session | A lead can only manage one team at a time. Clean up before starting a new one |
| No nested teams | Teammates cannot spawn their own teams or teammates — only the lead can |
| Fixed lead | The session that creates the team is lead for its lifetime. No promoting teammates or transferring leadership |
| Permissions set at spawn | All teammates start with lead's permission mode; can change individually after spawning but not at spawn time |
| Split panes limited | Not supported in VS Code integrated terminal, Windows Terminal, or Ghostty |

---

## 16. Troubleshooting

### Teammates Not Appearing
- In-process mode: press `Shift+Down` — they may be running but not visible
- Check if the task was complex enough to warrant a team (Claude decides whether to spawn)
- Verify tmux is installed: `which tmux`
- For iTerm2: verify `it2` CLI is installed and Python API is enabled in preferences

### Too Many Permission Prompts
Pre-approve common operations in permission settings before spawning.

### Teammates Stopping on Errors
Check their output (`Shift+Down` or click pane), then either give direct instructions or spawn a replacement.

### Lead Shuts Down Before Work Is Done
Tell it to keep going. Preemptively: tell the lead to wait for teammates before proceeding.

### Orphaned tmux Sessions
```bash
tmux ls
tmux kill-session -t <session-name>
```

### Task Stuck / Not Progressing
Teammate may have failed to mark a task complete. Verify work is done, then manually update the task status or tell the lead to nudge the teammate.

---

## 17. Quick Reference Cheatsheet

### Enable
```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

### Start
```
Create an agent team with [N] teammates to [task]. One focused on [X], one on [Y].
```

### Display Mode Config
```json
{ "teammateMode": "in-process" }   // in ~/.claude.json
```
```bash
claude --teammate-mode in-process  // per session
```

### Keyboard Shortcuts (in-process mode)
| Key | Action |
|:---|:---|
| `Shift+Down` | Cycle through teammates |
| `Ctrl+T` | Toggle task list |
| `Enter` | View teammate session |
| `Escape` | Interrupt teammate's current turn |

### Key Prompts

| Goal | Prompt |
|:---|:---|
| Require plan approval | `"Require plan approval before they make any changes"` |
| Stop lead from doing work itself | `"Wait for your teammates to complete their tasks before proceeding"` |
| Shut down a teammate | `"Ask the [name] teammate to shut down"` |
| Clean up | `"Clean up the team"` |
| Use a subagent definition | `"Spawn a teammate using the [type] agent type to [task]"` |

### Hook Registration (settings.json)
```json
{
  "hooks": {
    "TeammateIdle": [{ "hooks": [{ "type": "command", "command": "~/.claude/hooks/check-idle.sh" }] }],
    "TaskCreated":  [{ "hooks": [{ "type": "command", "command": "~/.claude/hooks/validate-task.sh" }] }],
    "TaskCompleted":[{ "hooks": [{ "type": "command", "command": "~/.claude/hooks/check-complete.sh" }] }]
  }
}
```

### Token Cost Rules of Thumb
- ~7x more tokens than a standard session (plan mode)
- Use Sonnet for teammates, not Opus
- Clean up immediately when done — idle teammates still consume tokens
- 3-5 teammates is the sweet spot for most workflows
