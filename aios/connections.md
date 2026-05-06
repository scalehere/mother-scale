# Connections

Registry of every system this AIOS can reach. Pre-populated from Scale SD's actual stack. `/audit` checks this file for domain coverage and freshness. Update on every new wire-up.

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| 1 | Revenue / Financials | **GoHighLevel** (Location: `EUZYYp8JaL4XPDDe7Ihq`) | **mcp** (live) — see `references/gohighlevel-mcp.md` | live | 2026-05-05 |
| 1b | Revenue / Financials | Stripe (payments via GHL) | via GHL MCP (indirect) | — | — |
| 2 | Customer interactions | GoHighLevel CRM (pipelines, contacts, opportunities) | **mcp** (live — same as #1) | live | 2026-05-05 |
| 2b | Customer interactions | Instagram DMs (@scalenowsd) | not yet connected | — | — |
| 3 | Calendar | Google Calendar (Google Workspace, media@scalehere.com) | **mcp** — `uvx workspace-mcp` registered ⚠️ needs OAuth | needs `uvx workspace-mcp --auth` | 2026-05-05 |
| 3b | Calendar | GHL Calendar (discovery + onboarding bookings) | via GHL MCP (included) | live | 2026-05-05 |
| 4 | Communication | Slack (internal team) | **mcp** — registered ⚠️ needs bot token in `.env` | needs `SLACK_BOT_TOKEN` + `SLACK_TEAM_ID` | 2026-05-05 |
| 4b | Communication | Gmail (media@scalehere.com) | **mcp** — `uvx workspace-mcp` registered ⚠️ needs OAuth | needs `uvx workspace-mcp --auth` | 2026-05-05 |
| 4c | Communication | GHL Conversations (SMS, missed-call text-back) | via GHL MCP (included) | live | 2026-05-05 |
| 5 | Project / task tracking | GHL pipelines + tasks | via GHL MCP | live | 2026-05-05 |
| 6 | Meeting intelligence | **Fathom** | **mcp** — `npx mcp-remote https://api.fathom.ai/mcp` registered ⚠️ needs OAuth | needs browser auth via Fathom | 2026-05-05 |
| 7 | Knowledge / files | Google Drive (Google Workspace) | **mcp** — `uvx workspace-mcp` registered ⚠️ needs OAuth | needs `uvx workspace-mcp --auth` | 2026-05-05 |
| 7b | Knowledge / files | Local filesystem — `../scale-business/` (Karpathy wiki) | local read | live | 2026-05-05 |

## Tier-2 (paid media + content distribution)

| # | Domain | Tool | Mechanism | Auth | Last checked |
|---|---|---|---|---|---|
| T2.1 | Paid ads | Meta Ads Manager (Facebook + Instagram) | **planned** — `npm install -g @meta/ads-cli` then `meta auth login` | pending — Phase 2b | — |
| T2.2 | Paid ads | TikTok Ads Manager | not yet connected | — | — |
| T2.3 | Content / publishing | Instagram Graph API (@scalenowsd) | not yet connected | — | — |
| T2.3b | Creative gen | **Higgsfield** (AI ad video creative) | **mcp** — registered ⚠️ needs `HF_API_KEY` in `.env` | needs API key from cloud.higgsfield.ai | 2026-05-05 |
| T2.4 | Content / publishing | YouTube Data API (any channels in use) | not yet connected | — | — |
| T2.5 | AI services | Anthropic API (Claude) | not yet connected | needs `ANTHROPIC_API_KEY` in `.env` | — |
| T2.6 | DNS / domains | GoDaddy (DNS for scalehere.com) | not yet connected | — | — |

---

**Mechanism options:** `mcp` (MCP server), `script` (Python/Bash hitting an API, in `scripts/`), `cli` (e.g. GWS CLI), `export` (CSV/JSON dump pipeline), `key+ref` (`.env` key + `references/{tool}-api.md` guide), `local read` (file-system access only), `not yet connected`.

**When you wire a new tool, also save `references/{tool}-api.md`** capturing endpoints, auth flow, common queries, and pagination rules — researched-once-saved-forever. The `/audit` skill rewards this; future skills don't re-research.

---

## Suggested connection order (highest leverage first)

**Updated 2026-05-04 — GHL MCP is already connected. Re-prioritized for fulfillment automation.**

1. ✅ **GoHighLevel** — already live via MCP. Next move is to inventory which GHL endpoints/objects the MCP exposes and write `references/gohighlevel-mcp.md` so future skills don't re-research.
2. **Meta Ads** — highest next-leverage target per Q7. Goal: launch + analyze + retarget campaigns through Claude. Use the official Meta Ads MCP (recently released — referenced in `os/All Posts • Instagram.md`).
3. **Higgsfield** — AI ad-creative generation via Claude. Closes the "creative → campaign → analyze" loop end-to-end inside the OS.
4. **Fathom** — pulls every client + team call into the OS. Plugs into the existing `scale-business/wiki/sources/calls/` ingest workflow already running.
5. **Slack** — internal team comms; lets the AIOS read context from threads and post digests.
6. **Google Workspace CLI** — Gmail, Drive, Calendar, Docs, Sheets all through one CLI. Mirrors what Nate's course recommends.
7. **Instagram Graph API** — for inbound DM monitoring + content scheduling.
8. **TikTok Ads** — secondary to Meta but already in use for EMSR.
9. **Anthropic API** — for skills that need raw model calls (separate from the Claude Code session).
