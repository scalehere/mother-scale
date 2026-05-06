# Fathom Transcripts — Drop Zone

Drop all Fathom call transcripts here. Do not edit files after dropping them.

## Naming Convention

```
YYYY-MM-DD_[client-or-contact-slug]_[call-type].md
```

**Examples:**
```
2026-04-13_joseph-fiasco_onboarding.md
2026-04-15_daniel_strategy.md
2026-04-18_california-doors-and-windows_check-in.md
2026-04-20_prospect-name_sales-call.md
```

**Call types:** `onboarding` | `sales-call` | `check-in` | `strategy` | `team` | `other`

## How to Ingest

After dropping a file here, go to Claude Code in `scale-business/` and say:

> "ingest transcript [filename]"

Claude will extract the full summary, action items, and update the relevant entity pages.
