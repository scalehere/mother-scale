# Slack MCP — Reference Guide

> Researched-once-saved-forever. Every skill that reads or posts to Slack reads this first.
> Last updated: 2026-05-05 | Workspace: Scalehere (T0AUVF2M7RC) | Bot: scale_aios (U0B1KSCPJSH)

## Connection

- **Mechanism:** MCP — `@modelcontextprotocol/server-slack`
- **Auth:** Bot token in `.env` → `SLACK_BOT_TOKEN` (xoxb-...)
- **Workspace ID:** `T0AUVF2M7RC`
- **Bot user:** `scale_aios` (U0B1KSCPJSH)

## Available Channels

| Channel | Purpose | Use in skills |
|---|---|---|
| `#general` | General team | Weekly digests, announcements |
| `#new-leads` | Inbound leads | Lead-followup audit, missed-call alerts |
| `#content-drops` | Content output | Post when content plan is approved |
| `#all-tools` | Tool updates | AIOS status posts |
| `#client-tony-pools` | Tony (pool contractor) | Per-client digests |
| `#client-micheal-doors_windows` | CDW client | Per-client digests |
| `#call-recordings` | Meeting links | Fathom call summaries |
| `#upcoming-meetings` | Meeting prep | Pre-call briefs |

## MCP Tools

| Tool | What it does |
|---|---|
| `slack_list_channels` | List all channels the bot can see |
| `slack_get_channel_history` | Get recent messages from a channel (limit param) |
| `slack_get_thread_replies` | Get all replies in a thread |
| `slack_post_message` | Post a message to a channel |
| `slack_reply_to_thread` | Reply to an existing thread |
| `slack_add_reaction` | Add emoji reaction to a message |
| `slack_get_users` | List workspace members |
| `slack_get_user_profile` | Get a specific user's profile |

## Common Skill Patterns

### Post a weekly digest to #general
```
slack_post_message(
  channel_id="C...",   # get from slack_list_channels
  text="*Weekly digest*\n- ...",
)
```

### Post a per-client content drop notification
```
slack_post_message(
  channel_id="C...",   # #content-drops
  text="✅ Tony's June content plan ready for review → [link]"
)
```

### Read #new-leads for context before running lead audit
```
slack_get_channel_history(channel_id="C...", limit=20)
→ parse messages for new lead names, sources, statuses
```

### Post a Fathom call summary to #call-recordings
```
slack_post_message(
  channel_id="C...",   # #call-recordings
  text="*Call summary — {client} {date}*\n{summary}\n\nAction items:\n{items}"
)
```

## Getting Channel IDs

Channel IDs aren't stored here because they can change. Always resolve at runtime:
```
slack_list_channels() → find channel by name → extract id
```

Or cache them in `context/slack-channels.md` after first lookup.

## Known Limits

- Bot only sees channels it's been invited to. To add a channel: type `/invite @Scale AIOS` in Slack.
- `slack_get_channel_history` returns max 100 messages per call. Use `cursor` param for pagination.
- Bot cannot read DMs unless explicitly added to an IM conversation.
- Rate limit: Slack Tier 3 = 50 req/min for history reads, Tier 1 = 1 req/min for `post_message` bursts.
