# GoHighLevel MCP — Reference Guide

> Researched-once-saved-forever. Every social-os and scale-os skill reads this before making GHL calls.
> Last updated: 2026-05-05 | MCP scope: Location `EUZYYp8JaL4XPDDe7Ihq`

## Connection

- **Mechanism:** MCP (already live in Claude Code)
- **Project scope:** `/Users/ashenafew/Desktop/SCALE/scale-business` (prod-ghl-mcp)
- **Auth:** Private Integration Token (PIT) — stored in scale-business project MCP config
- **Location ID:** `EUZYYp8JaL4XPDDe7Ihq`

When working from the `aios/` project, GHL MCP tools are accessible because Claude Code shares MCP context across projects in the same workspace. If a skill can't reach GHL, confirm the `scale-business` project is open in the same VS Code window.

## Tool Categories (39 official tools)

### Contacts
| Tool | What it does |
|---|---|
| `get_contact` | Get a contact by ID |
| `search_contacts` | Search contacts by name, email, phone, or tag |
| `create_contact` | Create a new contact |
| `update_contact` | Update contact fields |
| `add_tag` | Add a tag to a contact |
| `remove_tag` | Remove a tag from a contact |
| `get_contact_notes` | Get all notes on a contact |
| `create_note` | Add a note to a contact |

### Opportunities / Pipeline
| Tool | What it does |
|---|---|
| `get_opportunity` | Get an opportunity by ID |
| `search_opportunities` | Search opportunities in a pipeline |
| `create_opportunity` | Create a new opportunity |
| `update_opportunity` | Update opportunity status, stage, value |
| `get_pipelines` | List all pipelines in the location |

### Conversations
| Tool | What it does |
|---|---|
| `get_conversations` | List recent conversations |
| `get_conversation` | Get a conversation by ID |
| `send_message` | Send SMS or email via a conversation |
| `get_messages` | Get message history for a conversation |

### Calendars & Appointments
| Tool | What it does |
|---|---|
| `get_calendars` | List all calendars in the location |
| `get_appointments` | List appointments (date range filter) |
| `create_appointment` | Book an appointment |
| `update_appointment` | Reschedule or update an appointment |
| `delete_appointment` | Cancel an appointment |

### Workflows & Automation
| Tool | What it does |
|---|---|
| `get_workflows` | List all workflows |
| `add_contact_to_workflow` | Enroll a contact in a workflow |
| `remove_contact_from_workflow` | Remove a contact from a workflow |

### Custom Fields
| Tool | What it does |
|---|---|
| `get_custom_fields` | List all custom fields for the location |
| `update_custom_field_value` | Set a custom field value on a contact |

### Forms & Surveys
| Tool | What it does |
|---|---|
| `get_forms` | List all forms |
| `get_form_submissions` | Get submissions for a form |

### Tags
| Tool | What it does |
|---|---|
| `get_tags` | List all tags in the location |
| `create_tag` | Create a new tag |

### Locations & Sub-accounts
| Tool | What it does |
|---|---|
| `get_location` | Get current location details |
| `get_location_users` | List all users in the location |

### Payments / Invoices
| Tool | What it does |
|---|---|
| `get_invoices` | List invoices |
| `get_transactions` | List payment transactions |

## Common Skill Patterns

### Find a contact by name + check their pipeline stage
```
search_contacts(query="Victor Castellanos") 
→ get contact ID
→ search_opportunities(contact_id="{id}")
→ returns current stage + value
```

### Enroll a new lead into a follow-up workflow
```
create_contact(name, email, phone, tags=["new-lead"])
→ add_contact_to_workflow(contact_id, workflow_id)
```

### Pull all open opportunities for a monthly pipeline review
```
get_pipelines() → find pipeline ID
→ search_opportunities(pipeline_id, status="open")
→ returns all deals with stage + value + owner
```

### Send an SMS follow-up
```
search_contacts(query="phone number or name")
→ get_conversations(contact_id)
→ send_message(conversation_id, type="SMS", message="...")
```

## Known limits

- **Rate limiting:** GHL API is rate-limited at ~100 req/min per location. Skills that loop over all contacts should use pagination and add a small delay between batches.
- **Write operations:** All create/update/send calls are live — they hit the real account immediately. No sandbox mode. Always confirm before running bulk operations.
- **Workflow enrollment:** `add_contact_to_workflow` triggers the full workflow including SMS/email sends. Don't test with real contacts unless intended.
- **Social Planner:** GHL's social planner (for scheduling organic posts) is available via the `social_posts` endpoint in the v2 API — not yet in the standard MCP tool list. Use the GHL REST API directly via `$GHL_API_KEY` for social scheduling until the MCP adds it.

## GHL REST API (for tools not in MCP)

Base URL: `https://services.leadconnectorhq.com`
Auth header: `Authorization: Bearer {GHL_API_KEY}` + `Version: 2021-07-28`

Key endpoints not in the MCP:
- `POST /social-media-posting/{locationId}/post` — schedule a social post
- `GET /social-media-posting/{locationId}/posts` — list scheduled posts
- `GET /reporting/revenue` — revenue reporting
- `GET /funnels/funnel/list` — list funnels

Full API docs: https://highlevel.stoplight.io/docs/integrations

## Social Planner — Script Pattern

For the `post-scheduler` skill, use the REST API directly:

```bash
curl -X POST "https://services.leadconnectorhq.com/social-media-posting/{GHL_LOCATION_ID}/post" \
  -H "Authorization: Bearer $GHL_API_KEY" \
  -H "Version: 2021-07-28" \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Post caption here",
    "platforms": ["facebook", "instagram"],
    "scheduleDate": "2026-06-01T10:00:00Z",
    "mediaUrls": ["https://..."]
  }'
```
