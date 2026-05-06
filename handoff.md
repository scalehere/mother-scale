# Handoff Document
**Date:** 2026-04-13
**Project/Task:** SCALE / LeadOps Dashboard Orientation

## Context
Working inside the `/Users/ashenafew/Desktop/SCALE` monorepo. The user is getting familiar with the project structure, specifically the `leadops-dashboard` sub-project which is a real-time monitoring dashboard for the Scale SD LeadOps pipeline.

## What Was Done
- Identified what `leadops-dashboard` is: a React + Express real-time dashboard for monitoring the LeadOps pipeline and Claude agents.
- Located the GitHub repo: https://github.com/mukul975/claude-team-dashboard
- Found the localhost URLs:
  - Production/server mode: `http://localhost:3001`
  - Dev mode (Vite): `http://localhost:5173`
- Set up persistent session memory system so future sessions can resume with context.
- Established handoff.md convention: generated at end of every session.

## Current State
- `leadops-dashboard/` exists with a full Node/Express + React stack.
- No active server was started this session — URLs were found from config, not verified live.
- Memory system initialized at `~/.claude/projects/-Users-ashenafew-Desktop-SCALE/memory/`.

## Key Decisions
- User wants seamless session continuity — handoff.md will be generated every session going forward without being asked.

## Open Questions / Blockers
- It's unclear if the dashboard is currently running or needs to be started.
- No work was done on code changes — this was purely an orientation session.

## Next Steps
- Start the dashboard if needed: `cd leadops-dashboard && npm start` (port 3001) or `npm run dev` (port 5173)
- Clarify what the user actually wants to do with `leadops-dashboard` — explore it, fix something, add a feature?

## Key Files & References
- `leadops-dashboard/package.json` — scripts, dependencies
- `leadops-dashboard/config.js` — port config (3001), CORS origins
- `leadops-dashboard/server.js` — Express backend
- `scale-business/wiki/analysis/leadops-claude-md-template.md` — related LeadOps docs
- GitHub: https://github.com/mukul975/claude-team-dashboard
