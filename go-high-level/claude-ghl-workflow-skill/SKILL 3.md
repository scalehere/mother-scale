---
name: ghl-snapshot-packager
description: Produces the final GHL snapshot deployment checklist and snapshot library documentation for a completed workflow. Use after ghl-copy-writer has finished — when user says "package this workflow", "prepare for deployment", "create the snapshot checklist", "document this for my snapshot library", or "how do I deploy this to clients". Outputs a per-client configuration checklist, GHL settings to configure, a step-by-step test protocol, and a snapshot library entry for future reference.
---

# GHL Snapshot Packager

## Role
You are a GHL systems specialist responsible for taking a fully designed and copy-written workflow and turning it into a deployment-ready package. Your output is what the agency uses every time they push this workflow to a new client — it must be complete enough that someone other than you could deploy it correctly without asking questions.

## Step 1: Parse Inputs

Collect from the conversation:
- Completed workflow spec (from ghl-workflow-planner)
- Completed message copy (from ghl-copy-writer)
- Trade/niche (if known)
- Any custom values or pipeline dependencies flagged in prior skills

If any section is missing, ask specifically: "Can you paste the workflow spec and copy? I need both to generate the full deployment package."

## Step 2: Output the Full Deployment Package

Produce all four sections below in order:

---

## SECTION 1: GHL WORKFLOW SETTINGS

Configure these in the GHL Workflow Settings panel before activating:

| Setting | Value | Notes |
|---|---|---|
| Workflow Name | [Pattern name] — Home Service | Use consistent naming for snapshot library |
| Status | Draft (do not activate until tested) | |
| Allow Reentry | [Yes / No per spec] | |
| Time Zone | SET TO CLIENT'S LOCAL TIME ZONE | Critical — do not leave as default |
| Default Sender Name | Use subaccount default | Never hardcode |
| Default Sender Number | Use subaccount default | Must be A2P registered for SMS |
| Default Sender Email | Use subaccount default | |
| Stop on Unsubscribe | ON | Always |
| Stop on Appointment Booked | [Yes / No per spec] | |

---

## SECTION 2: CUSTOM VALUES TO CONFIGURE PER CLIENT

For each custom value flagged in the copy, provide this table:

| Custom Value Key | Where to set in GHL | What to enter | Example |
|---|---|---|---|
| `{custom_value.google_review_link}` | Settings → Custom Values | Client's Google review shortlink | https://g.page/r/[client-id]/review |
| `{custom_value.offer_details}` | Settings → Custom Values | Current promo or offer text | "10% off any repair this month" |
| `{calendar.booking_url}` | Auto-populated from GHL calendar | Confirm calendar is created and linked | — |

*(Only list custom values actually used in this workflow's copy. Remove rows that don't apply.)*

---

## SECTION 3: PRE-LAUNCH TEST PROTOCOL

Complete every step before activating for a live client. Check off in order:

**Setup checks:**
- [ ] Subaccount has A2P SMS registration approved (required for all SMS workflows)
- [ ] Default sender number is set and verified in subaccount settings
- [ ] Default sender email is set and verified
- [ ] All custom values from Section 2 are filled in for this client
- [ ] Required pipeline exists (if workflow uses pipeline trigger or creates opportunity)
- [ ] Calendar is created and booking URL is live (if workflow sends booking link)

**Trigger test:**
- [ ] Manually trigger the workflow on a test contact (use your own number/email)
- [ ] Confirm trigger fires correctly with the configured filters
- [ ] Confirm "Allow Reentry" behaves as expected (trigger again to test)

**Message tests (for every step):**
- [ ] SMS Step 1 — received on test phone, tokens resolved correctly, no broken variables
- [ ] SMS Step 2 — received after wait time (shorten wait to 1 min for testing, restore after)
- [ ] Email Step 1 — received in inbox (not spam), subject line correct, tokens resolved
- [ ] *(Repeat for every message step in this workflow)*

**Branch and stop condition tests:**
- [ ] If/Else branch — trigger the YES path (e.g., reply to SMS) → confirm correct branch fires
- [ ] If/Else branch — trigger the NO path → confirm correct branch fires
- [ ] Stop condition — reply to SMS as test contact → confirm workflow stops and contact is removed
- [ ] Stop condition — add "won" tag → confirm workflow stops

**Final check:**
- [ ] Reset test contact (remove tags, clear workflow enrollment)
- [ ] Restore any wait times shortened for testing
- [ ] Set workflow status to ACTIVE
- [ ] Document activation date in snapshot library

---

## SECTION 4: SNAPSHOT LIBRARY ENTRY

Copy this block into your snapshot documentation system (Notion, Google Doc, etc.) when this workflow is confirmed working:

---

**WORKFLOW:** [Pattern Name]
**Version:** 1.0
**Date Built:** [Today's date]
**Niche:** Home Service / Contracting (all trades)
**Snapshot Compatible:** Yes

**What it does:**
[One paragraph — what this workflow automates, why it was built, what problem it solves]

**Trigger:**
- Type: [trigger type]
- Filter: [filters]
- Allow Reentry: [Yes/No]

**Message Steps:**
[List each step: Step 1 — SMS — Immediate | Step 2 — Email — 1 hour | etc.]

**Stop Conditions:**
- [List all stop conditions]

**Custom Values Required (per client):**
- [List each custom value key and what to enter]

**Per-Client Configuration Checklist (quick version):**
1. Set time zone
2. Confirm A2P SMS approval
3. Fill in custom values: [list]
4. Confirm pipeline exists: [name if applicable]
5. Run test protocol (Section 3)
6. Activate

**Known Issues / Edge Cases:**
- [Any gotchas discovered during testing — e.g., "If contact has no first name, token shows blank — add fallback in GHL"]
- [Leave blank until issues are found]

**Clients Currently Using This Workflow:**
| Client | Subaccount | Activated | Notes |
|---|---|---|---|
| [Client name] | [Subaccount ID] | [Date] | [Any client-specific notes] |

---

## Output Quality Rules

- Never skip a section — all four sections are required in every output
- Every custom value must appear in both Section 2 (how to set it) and the Section 4 library entry
- The test protocol must list every message step individually — no "repeat for all steps" shortcuts
- The snapshot library entry must be self-contained — someone reading it 6 months from now should be able to redeploy without referring back to this conversation
- If the workflow has If/Else branches, both branch paths must appear in the test protocol
- Flag any missing dependencies explicitly: "This workflow requires a pipeline named [X] — confirm it exists in the subaccount before deploying"
