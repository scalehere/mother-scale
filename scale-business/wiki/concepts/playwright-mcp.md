---
title: "Playwright MCP"
type: concept
tags: [playwright, mcp, browser-automation, tools, claude-agents, lead-qualification]
sources: [how-to-build-claude-agent-teams]
updated: 2026-04-13
---

# Playwright MCP

A Model Context Protocol (MCP) server that gives Claude Code agents a live browser they can navigate, read, and interact with. It uses Playwright's accessibility tree — structured data from the DOM — rather than screenshots or pixel-based input, making it fast, token-efficient, and compatible with any site that renders text content.

Scale SD uses Playwright MCP as the core tool for Agent 2 (Lead Qualifier) in the LeadOps agent team: instead of guessing at lead quality from URL metadata, the agent visits each business's website, Google Business Profile, and social pages in a real browser and reads what's actually there.

---

## How It Works

Playwright MCP exposes browser tools to Claude Code agents. The agent can:
- Navigate to a URL (`browser_navigate`)
- Read the page's accessibility tree (structured DOM content — headers, buttons, links, text, form labels)
- Click elements, fill forms, scroll
- Get a snapshot of the current page state

It does NOT require:
- Screenshots or image processing
- A vision-capable model
- Any API keys

It reads web content the same way a screen reader does — as structured text. This is exactly what's needed for lead qualification: checking if a website has CTAs, reading review counts on a Google Business Profile, checking the last post date on an Instagram page.

---

## Setup for Scale SD

Add to `.claude/settings.json` in the `scale-lead-ops/` project:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  },
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

Or run from the terminal (within the project directory):
```bash
claude mcp add playwright -- npx @playwright/mcp@latest
```

Requirements: Node.js 18+

---

## What Agent 2 Does With It

For each lead in `leads_processed.csv`:

1. Navigate to their website URL → read accessibility tree → look for: CTAs, portfolio images (alt text), testimonial sections, service area mentions, copyright year (signals last update)
2. Search Google Maps for `[business name] [city]` → navigate to their GMB listing → read: star rating, review count, last post date, photo count, claimed/unclaimed status
3. Navigate to their Instagram URL (if available) → read: last post date, follower count, bio
4. Navigate to their Facebook URL (if available) → read: last post date, follower count, about section

Agent 2 then applies the scoring rubric from `criteria/qualification_rubric.md` to what it actually found — not inferred from the URL.

**Fallback behavior:** If a site blocks headless browser access (common on some modern sites with Cloudflare/bot detection), Agent 2 flags the lead as "browser-blocked" and scores conservatively from any available metadata. The score is marked "estimated" in the notes field.

---

## Why Not Screenshots

The Playwright MCP README explicitly notes that for coding agents, MCP is better than CLI + SKILLS when the workflow requires "persistent state, rich introspection, and iterative reasoning over page structure." Lead qualification is exactly this: the agent needs to reason across multiple page attributes, navigate to multiple pages per lead, and maintain context across all of them within one task. Screenshots would require a vision model and consume far more tokens per page. Accessibility tree snapshots are text-only and typically 10–20× more token-efficient.

---

## Limitations

- Some sites block headless browser access (Cloudflare anti-bot, aggressive CSP headers)
- Instagram and Facebook may require login for full profile view — Agent 2 reads what's publicly visible without login
- Speed: visiting 5 pages per lead × 150 leads = 750 browser navigations per batch. This is the main time cost in a batch run. Estimated batch time with Playwright: 45–90 minutes.
- Token cost: Playwright accessibility trees can be verbose for complex pages. Keep Agent 2's context focused — it should navigate, read, score, and move on. No lingering on pages.

---

## Related Concepts

- [[Claude Agent Teams]] — the framework Playwright MCP is used within
- [[Autonomous Improvement Loop]] — the monthly cycle that improves qualification criteria over time
- [[Lead Intelligence Agent Team Plan]] — the LeadOps prompt using Playwright MCP
- [[Scale SD AI Growth System]] — the full stack architecture
