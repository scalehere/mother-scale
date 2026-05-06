# Fathom MCP — Reference Guide

> Researched-once-saved-forever. Every skill that reads call transcripts reads this first.
> Last updated: 2026-05-05 | Account: Ashenafew Daniel

## Connection

- **Mechanism:** MCP — `@lukas-bekr/fathom-mcp`
- **Auth:** API key in `.env` → `FATHOM_API_KEY`
- **Base URL:** `https://api.fathom.ai/external/v1`
- **Auth header:** `X-Api-Key: {FATHOM_API_KEY}` (NOT Bearer)
- **Rate limit:** 60 calls/minute across all API keys

## MCP Tools

| Tool | What it does |
|---|---|
| `list_meetings` | List recent meetings with date/title filters |
| `search_meetings` | Search meetings by title or keyword |
| `get_transcript` | Full transcript of a recording |
| `get_summary` | AI-generated summary with topics, takeaways, next steps |

## REST API Fallback (if MCP tool missing)

```bash
# List meetings
curl -X GET "https://api.fathom.ai/external/v1/meetings?limit=10" \
  -H "X-Api-Key: $FATHOM_API_KEY"

# Get transcript for a specific recording
curl -X GET "https://api.fathom.ai/external/v1/meetings/{recording_id}/transcript" \
  -H "X-Api-Key: $FATHOM_API_KEY"
```

## Response Shape (meetings)

```json
{
  "items": [
    {
      "title": "Jeff Go High Level Workflow Setup",
      "meeting_title": "...",
      "url": "https://fathom.video/calls/654271814",
      "created_at": "2026-04-28T16:40:50Z",
      "scheduled_start_time": "2026-04-28T16:00:10Z",
      "scheduled_end_time": "2026-04-28T16:45:10Z",
      "recording_id": 141753456,
      "recording_start_time": "...",
      "recording_end_time": "...",
      "calendar_invitees": [...]
    }
  ]
}
```

## Known Calls (as of 2026-05-05)

| Title | Date | Recording ID |
|---|---|---|
| Jeff Go High Level Workflow Setup | 2026-04-28 | 141753456 |
| Impromptu Zoom Meeting (×9) | Apr 14–25 | various |

## Common Skill Patterns

### Pull onboarding call transcript for a client before strategy session
```
search_meetings(query="{client name}")
→ get recording_id
→ get_transcript(recording_id)
→ extract: voice signals, stated preferences, pain points, service scope
→ pre-fill client-strategy-session answers (confirm, don't re-ask)
```

### Generate weekly call summary for Slack
```
list_meetings(limit=7, after="{last_monday}")
→ for each: get_summary(recording_id)
→ format as digest
→ post to #call-recordings via Slack MCP
```

### Mine client calls for content ideas
```
search_meetings(query="{client name}")
→ get_transcript(recording_id)
→ extract: client's own words about their work, team, results
→ use as raw material for caption-writer skill (client's voice, not ours)
```

## Integration with wiki

Fathom transcripts that have been manually ingested already live in:
`../../scale-business/wiki/sources/calls/`

Before calling Fathom MCP, check if the transcript already exists in the wiki. If it does, read from the wiki (cheaper, faster). Only call Fathom MCP for transcripts not yet ingested.

## Known Limits

- API keys access only meetings recorded by you or shared to your Team.
- Transcripts only available for recorded meetings (not all Zoom/Meet calls auto-record).
- No webhook support in v1 — polling only.
