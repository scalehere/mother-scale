---
title: GHL SaaS Configurator
type: concept
tags: [ghl, saas, agency, white-label, subaccount, 497-plan]
created: 2026-04-12
updated: 2026-04-12
sources: [ghl-ultra-indepth-free-course]
---

# GHL SaaS Configurator

The SaaS Configurator is a [[GoHighLevel]] agency feature (available on the **$497/month plan only**) that auto-provisions client subaccounts when a payment is made. Enables true SaaS reselling at scale — no manual setup per client.

## How It Works

1. Create a SaaS plan (name, price, feature set, optional snapshot)
2. Generate a sale link from the plan
3. Send link to client → they pay via Stripe (or NMI/Authorize.net/Square)
4. Subaccount auto-created with the plan's configured features, snapshot pre-loaded, and welcome email sent

## Plan Configuration Options

- Monthly + annual pricing
- User/contact limits (optional)
- Feature access toggles (what tabs the client can see)
- Snapshot injection (pre-loads your template/automation bundle)
- Custom menu links
- Free trial period + length
- Wallet credits (pre-load SMS/email/WhatsApp credits)
- Category (organize plans by niche, e.g., "SaaS for Plumbers")

## Advanced Settings

- **Pause on failed payment:** Suspends subaccount until payment clears
- **Allow client self-upgrade:** Client can upgrade their own plan
- **Allow client self-cancel:** Client can cancel subscription
- **Two-factor authentication:** Required on signup
- **Welcome email:** Fully customizable with agency branding

## Relationship to [[GHL Rebilling]]

SaaS Configurator handles subaccount provisioning; Rebilling handles usage markup. They work together: a client on a SaaS plan also has rebilling rates applied to SMS/email/call usage.

## Relationships

- [[GHL Agency View]] — where SaaS Configurator lives
- [[GHL Subaccount View]] — what gets auto-created
- [[GHL Snapshots]] — injected at plan provisioning
- [[GHL Rebilling]] — usage markup layer on top

## Open Questions

- Can existing manual subaccounts be migrated to a SaaS plan retroactively?
- Is there a limit on number of SaaS plans?
