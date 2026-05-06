---
title: GHL Workflow Troubleshooting
type: concept
tags: [ghl, automation, troubleshooting, testing]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-getting-started-workflows, ghl-workflow-ai-builder-docs]
---

# GHL Workflow Troubleshooting

Official checklist and best practices for diagnosing when a [[GoHighLevel]] workflow isn't firing or behaving as expected.

## Official Troubleshooting Checklist

**✅ Use a fresh contact for testing**
After testing multiple times with the same contact, the workflow may skip steps or behave unexpectedly due to prior enrollment history. Delete the contact and test with a new one.

**✅ Test live, not just with "Test Workflow"**
The "Test Workflow" button in the builder has limitations. For reliable testing, use an actual contact and trigger the workflow through the real trigger event (submit the actual form, make the actual call, etc.).

**✅ Check all filters**
Filters narrow the trigger and action scope. Over-broad filters fire unexpectedly. Over-narrow filters prevent firing altogether. Check every filter at both trigger and action level.

**✅ Check "Allow Reentry" in Workflow Settings**
If disabled (the default), a contact that has already been through the workflow will not re-enter it. During testing, this silently skips the workflow. Either:
- Enable "Allow Reentry" while testing, then disable for production, OR
- Delete the test contact between test runs

## Error Checker

The workflow builder sidebar shows a red error indicator when the workflow has a configuration problem (e.g., missing "From" email, unconfigured action). Check this before publishing.

## AI Builder Troubleshooting

When AI-generated workflows don't match intent:
- Refine the prompt — add more specific detail (timing, channel, condition)
- Split complex goals into smaller individual prompts
- Wrong trigger? Specify the exact trigger type in the next prompt
- Missing actions? List them explicitly
- Wrong timing? Use precise references: "after 2 days" not "soon"

## Relationships

- [[GHL Workflow Settings]] — Allow Reentry setting
- [[GHL AI Automation Builder]] — AI builder troubleshooting
- [[GHL Automation Builder (Basic)]]
