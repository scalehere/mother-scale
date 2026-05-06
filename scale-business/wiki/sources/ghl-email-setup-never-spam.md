---
title: "Never Land in Spam: GoHighLevel Email Setup Tutorial"
type: source
tags: [ghl, email, deliverability, dns, sending-domain, lead-connector]
sources: [Never Land in Spam GoHighLevel Email Setup Tutorial]
updated: 2026-04-16
---

# Never Land in Spam: GoHighLevel Email Setup Tutorial

By ItsKeaton (Keaton Walker). Covers the four levels of GHL email setup for agencies — from default shared domain to full client DNS control. This is the source that informed Scale SD's DNS and GHL email infrastructure setup session on 2026-04-15/16.

---

## Key Claims

- Most agencies send from GHL's default `msgsndr.com` domain — shared with thousands of users, terrible reputation
- There are four distinct levels of email setup in GHL, each with different tradeoffs
- Level 3 (per-client subdomains under your DNS) is the recommended default for agencies
- Level 4 (client's own DNS) is ideal but requires a 40-min setup call or credential handoff — 80–90% of contractor clients won't do this easily

---

## The Four Levels

### Level 1 — Lead Connector Default
- No setup required
- Sends from `msgsndr.com` (GHL's shared domain)
- Shared reputation with every GHL user globally
- Almost certain to land in spam or trigger "suspicious message" warnings
- **Never use long-term**

### Level 2 — Software-Wide White-Label Domain
- One subdomain for all clients on your GHL (e.g., `s.scalehere.com`)
- Better than Level 1 — reputation shared only among your clients
- Risk: one rogue client damages deliverability for all others
- Same mechanism as MailChimp, ConvertKit — "via s.scalehere.com" appears in headers
- **Good temporary solution. Scale SD's current setup.**

### Level 3 — Per-Client Subdomain (Under Your DNS)
- Each client gets their own subdomain (e.g., `emsr.scalehere.com`, `victor.scalehere.com`)
- Set up in your DNS — no need to access client's DNS
- Reputation isolation: one client's bad sends don't affect others
- 5 DNS records per client: 2 TXT, 1 CNAME, 2 MX
- **Recommended default for growing agencies**

### Level 4 — Client's Own DNS
- Each client sends from their own domain (e.g., `mail.emsrrestoration.com`)
- Best deliverability — fully authentic sender domain
- Requires: 40-min setup call with client OR credential handoff + 2FA appointment
- 80–90% of small business clients won't easily provide DNS access
- **Do only when client provides credentials voluntarily**

---

## Key Setup Notes

- DNS records required per subdomain (Levels 2–4):
  - 2× TXT (SPF + DKIM)
  - 1× CNAME (`email.[subdomain]` → `mailgun.org`)
  - 2× MX (`mxa.mailgun.org` + `mxb.mailgun.org`, priority 10)
- GHL verification may require clicking "Verify Domain" multiple times — this is normal
- SSL issued = domain is secure and ready

---

## Scale SD Application

Scale SD completed Levels 1 → 2 during the April 15–16 infrastructure session:

| Step | Status |
|------|--------|
| Level 1 (default) | Bypassed |
| Level 2 (`s.scalehere.com`) | ✅ Active sending domain |
| Level 3 (per-client subdomains) | 🔜 Next step when client volume grows |
| Level 4 (client DNS) | 🔜 Only if client provides credentials |

See [[Email & DNS Setup — Scale SD]] for all current DNS records and verification status.

---

## Entities Mentioned

- [[GoHighLevel]] — platform
- ItsKeaton / Keaton Walker — source author

## Related Concepts

- [[Contractor Automation System]] — the broader GHL system this email setup supports
