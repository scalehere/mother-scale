# Google Workspace MCP — Reference Guide

> Researched-once-saved-forever. Every skill that touches Gmail, Drive, Calendar, Docs, or Sheets reads this first.
> Last updated: 2026-05-05 | Account: ashen@scalehere.com (admin)

## Connection

- **Mechanism:** MCP — `uvx workspace-mcp --tool-tier core`
- **Auth:** OAuth 2.0 — token cached after browser auth flow
- **Account:** `ashen@scalehere.com`
- **Always pass:** `user_google_email: "ashen@scalehere.com"` on every tool call

## Tool Categories (100+ tools — core tier)

### Gmail
| Tool | What it does |
|---|---|
| `search_gmail_messages` | Search by query string (same syntax as Gmail search) |
| `get_gmail_message_content` | Get full email by message ID |
| `get_gmail_thread_content` | Get full thread |
| `get_gmail_messages_content_batch` | Batch fetch multiple messages |
| `send_gmail_message` | Send an email |
| `draft_gmail_message` | Create a draft |
| `modify_gmail_message_labels` | Archive, mark read, label |
| `list_gmail_labels` | List all labels |
| `list_gmail_filters` | List inbox filters |

### Google Drive
| Tool | What it does |
|---|---|
| `list_drive_items` | List files/folders in a directory |
| `search_drive_files` | Search Drive by name or content |
| `get_drive_file_content` | Get file content (Docs, Sheets, etc.) |
| `get_drive_file_download_url` | Get a download URL |
| `create_drive_file` | Create a new file |
| `create_drive_folder` | Create a folder |
| `update_drive_file` | Update file content |
| `copy_drive_file` | Duplicate a file |
| `manage_drive_access` | Share / set permissions |

### Google Calendar
| Tool | What it does |
|---|---|
| `list_calendars` | List all calendars |
| `get_events` | Get events in a date range |
| `manage_event` | Create / update / delete events |
| `query_freebusy` | Check availability |
| `manage_focus_time` | Set focus time blocks |
| `manage_out_of_office` | Set OOO |

### Google Docs
| Tool | What it does |
|---|---|
| `get_doc_content` | Get doc content |
| `get_doc_as_markdown` | Get doc as markdown |
| `create_doc` | Create a new doc |
| `modify_doc_text` | Edit doc text |
| `insert_doc_elements` | Insert headings, tables, lists |
| `find_and_replace_doc` | Find and replace text |
| `export_doc_to_pdf` | Export to PDF |
| `search_docs` | Search Docs |

### Google Sheets
| Tool | What it does |
|---|---|
| `read_sheet_values` | Read a range |
| `modify_sheet_values` | Write to a range |
| `create_spreadsheet` | Create new spreadsheet |
| `get_spreadsheet_info` | Get sheet metadata |
| `list_spreadsheets` | List spreadsheets in Drive |
| `format_sheet_range` | Format cells |
| `append_table_rows` | Add rows to a table |

### Google Tasks
| Tool | What it does |
|---|---|
| `list_task_lists` | List all task lists |
| `list_tasks` | List tasks in a list |
| `manage_task` | Create / update / complete tasks |
| `manage_task_list` | Create / delete task lists |

### Contacts
| Tool | What it does |
|---|---|
| `list_contacts` | List all contacts |
| `search_contacts` | Search by name/email |
| `get_contact` | Get a specific contact |
| `manage_contact` | Create / update contacts |

## Common Skill Patterns

### Search Gmail for a client's emails before discovery call
```
search_gmail_messages(
  query="from:{client_email} OR to:{client_email}",
  max_results=10
)
→ get_gmail_thread_content(thread_id)
→ extract context, open questions, last communication date
```

### Save a monthly content plan to Drive
```
create_doc(
  title="Scale SD — {client} Content Plan {YYYY-MM}",
  folder_id="..."
)
→ modify_doc_text(doc_id, content=plan_markdown)
→ manage_drive_access(doc_id, email=client_email, role="reader")
```

### Check upcoming client meetings from Calendar
```
get_events(
  calendar_id="ashen@scalehere.com",
  time_min="{today}",
  time_max="{7_days_from_now}"
)
→ filter for client names
→ return agenda for weekly planning
```

### Log a decision to a running Sheets tracker
```
read_sheet_values(spreadsheet_id="...", range="Decisions!A:D")
→ append_table_rows(spreadsheet_id, sheet_name="Decisions", rows=[...])
```

## Known Limits

- OAuth token expires — if tools start failing, re-run `uvx workspace-mcp --auth`
- Drive search only returns files owned by or shared with `ashen@scalehere.com`
- Gmail send quota: 500 emails/day for Google Workspace accounts
- Batch operations (get_gmail_messages_content_batch) max 100 per call
- Calendar: `get_events` requires explicit `calendar_id` — use `list_calendars` first if unsure

## Key File Locations (update as discovered)

| What | Drive location | ID |
|---|---|---|
| Client proposals | TBD | — |
| SOPs folder | TBD | — |
| Agency email templates | TBD | — |

Update this table as you discover important Drive folders during operations.
