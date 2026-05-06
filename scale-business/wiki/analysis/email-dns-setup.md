---
title: "Email & DNS Setup — Scale SD"
type: analysis
tags: [email, dns, ghl, google-workspace, deliverability, infrastructure]
sources: []
updated: 2026-04-16
---

# Email & DNS Setup — Scale SD

Reference doc for the agency's email infrastructure. Covers team email (Google Workspace) and automated client email (GHL Lead Connector). **Fully verified and live as of 2026-04-16.**

---

## Domain Infrastructure

| Component | Provider |
|-----------|----------|
| Domain registrar | GoDaddy |
| DNS (nameservers) | GoDaddy (`ns75.domaincontrol.com`, `ns76.domaincontrol.com`) |
| Website | Wix (A records point to Wix servers) |
| Team email | Google Workspace (`@scalehere.com`) |
| Automated email (GHL) | Lead Connector via `s.scalehere.com` ← active sending domain |
| Old sending domain | `mail.scalehere.com` — still live, delete once s.scalehere.com is fully stable |

---

## Google Workspace — Team Email Accounts

| Email | Type | Use |
|-------|------|-----|
| `daniel@scalehere.com` | User | Owner — strategy, closing |
| `ashen@scalehere.com` | User | Lead ops, ads, internal |
| `justin@scalehere.com` | User | Content, organic |
| `admin@scalehere.com` | User | GHL admin notifications |
| `tools@scalehere.com` | User | DMARC reports, third-party tool alerts |
| `media@scalehere.com` | Group (3) | Outreach — **convert to real user to use for SMTP/GHL sending** |
| `billing@scalehere.com` | Group (2) | Invoices, payment comms |
| `support@scalehere.com` | Group (3) | Client support replies |
| `team@scalehere.com` | Group (3) | Internal GHL notifications destination |

**Note:** Google Groups can receive email but cannot send via SMTP or authenticate with GHL. `media@scalehere.com` needs to be converted to a real user account (~$6–12/mo extra seat) to use as a clean GHL from address.

---

## DNS Records — Full Reference (GoDaddy)

### A Records (Wix Website)

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | `@` | 185.230.63.171 | 1 Hour |
| A | `@` | 185.230.63.186 | 1 Hour |
| A | `@` | 185.230.63.107 | 1 Hour |

### CNAME Records

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | `www` | cdn1.wixdns.net | 1 Hour |
| CNAME | `en` | cdn1.wixdns.net | 1 Hour |
| CNAME | `email.mail` | mailgun.org | 1 Hour |
| CNAME | `email.s` | mailgun.org | 1 Hour |

### MX Records

| Type | Name | Value | Priority | TTL |
|------|------|-------|----------|-----|
| MX | `@` | aspmx.l.google.com | 10 | 1 Hour |
| MX | `@` | alt1.aspmx.l.google.com | 20 | 1 Hour |
| MX | `@` | alt2.aspmx.l.google.com | 30 | 1 Hour |
| MX | `@` | alt3.aspmx.l.google.com | 40 | 1 Hour |
| MX | `@` | alt4.aspmx.l.google.com | 50 | 1 Hour |
| MX | `mail` | mxa.mailgun.org | 10 | 1 Hour |
| MX | `mail` | mxb.mailgun.org | 10 | 1 Hour |
| MX | `s` | mxa.mailgun.org | 10 | 1 Hour |
| MX | `s` | mxb.mailgun.org | 10 | 1 Hour |

### TXT Records

| Type | Name | Value | TTL |
|------|------|-------|-----|
| TXT | `@` | `v=spf1 include:_spf.google.com ~all` | 1 Hour |
| TXT | `@` | `google-site-verification=GEq3NGaHEv3uPLdzo-X0e6NgxdiyQGooXJgPGr6LE94` | 1 Hour |
| TXT | `_dmarc` | `v=DMARC1; p=none; rua=mailto:tools@scalehere.com` | 1 Hour |
| TXT | `google._domainkey` | `v=DKIM1; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwRHyP7NXaAyx1rtJ4gBVYZxkWS05FGi7BQqH3dH5Kq0KDhl/lNMVgffdgfsl8MYHTPr+G4n1ObluT93zXVhUtZnIKoY5h2ORqD8xniT5fF/1PWl252Zpkyqx9aF1llkfPE4lTltE7YHc/8YQ9i8nUCb5qFTUcSPO4B4PK92G6RcJ0gyIgq2VSY3PdcOZd7isrUMBd4mRmePZreT5qysc5PEeC05Oj3cJqtmPOYmRRDa19YW7HXgaMw4U954xQEJWCEkV8DCnQwvQsZwBIULA7CSwRGU+va06vbe+/WU39IYIdPHUcwm/wT9n2WmfzYmfrhQPl/8jNs57mCvlg0+gsQIDAQAB` | 1 Hour |
| TXT | `mail` | `v=spf1 include:spf.leadconnectorhq.com include:mailgun.org ~all` | 1 Hour |
| TXT | `_dmarc.mail` | `v=DMARC1; p=none;` | 1 Hour |
| TXT | `krs._domainkey.mail` | `k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCzKuxF2fhxuBYW3ESGmA6ZK4tU1SQhmncUSTAXUYN8fQlb3c1VIC7T90csDNWLyQUwTF8Xdlt1+lPPb8UhmWCiRueAuJp9OTa0fJbjF1F/n9GSV85xQm7o1UEGFVZx1/W+t6rB/zs9Jg5xMQ6ThA5BPLdAGMMb7vgEzct8McUBnQIDAQAB` | 1 Hour |
| TXT | `mx._domainkey.mail` | `k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdAn8DlRAI7nxL9Hp3rbikwai53o/YR3pPjlRsJ20NMq2Kwru4ZrKV+DpicFR/Zet+rhN72XR4LuGk9xhU8JbhZ8Gu9kQFhweafvwgb19DTYTuBcrmLAcea8jIUn/kZL24BfsVI9tuzMRc1rRBKEJH+R71qibPgZC3p243LuYYcwIDAQAB` | 1 Hour |
| TXT | `s` | `v=spf1 include:spf.leadconnectorhq.com include:mailgun.org ~all` | 1 Hour |
| TXT | `_dmarc.s` | `v=DMARC1; p=none;` | 1 Hour |
| TXT | `pic._domainkey.s` | *(DKIM key from GHL — verify in GHL dashboard)* | 1 Hour |

---

## GHL Email Configuration

### Sending Domain
- **Active:** `s.scalehere.com` ✅ verified in GHL
- **Old:** `mail.scalehere.com` — delete from GHL once s.scalehere.com is confirmed stable

### From Address Behavior (Lead Connector)
Lead Connector encodes the from address as `username+domain@s.scalehere.com` — this is normal and expected. Recipients see the display name, not the encoded address. No "via" warning appears.

### GHL Sub-Account Email Roles
| Email | Role in GHL |
|-------|-------------|
| `ashen@scalehere.com` | Profile email for manual sends from Conversations |
| `media@scalehere.com` | Intended outreach from address — **needs to be converted from Group to User first** |
| `team@scalehere.com` | Destination for internal GHL notifications (via workflows) |
| `support@scalehere.com` | Client-facing support replies |

### Internal Notifications Setup (Pending)
GHL has no global notification email setting. Route notifications to `team@scalehere.com` by building workflows:
- **New lead alert:** Trigger: Contact Created → Action: Internal Notification → `team@scalehere.com`
- **Pipeline update:** Trigger: Pipeline Stage Changed → Action: Internal Notification → `team@scalehere.com`
- **Forms/Surveys:** Bell icon in form editor → add `team@scalehere.com`
- **Documents/Contracts:** Settings → Payments → Documents & Contracts → Team Notifications → `team@scalehere.com`

---

## Open Items

- [x] Delete `mail.scalehere.com` from GHL — done, `s.scalehere.com` is now the only active sending domain
- [x] Convert `media@scalehere.com` from Google Group to real user — done, now usable for GHL/SMTP sending
- [ ] Build internal notification workflows routing to `team@scalehere.com`
- [ ] Set `media@scalehere.com` as the GHL profile/from email now that it's a real user
- [ ] Tighten DMARC from `p=none` to `p=quarantine` after a few weeks of data
- [ ] Upgrade to Level 3 (per-client subdomains) when client volume grows

---

## Key Notes

- **DNS is on GoDaddy** — all future DNS changes go there.
- **Wix website works** — A records intact, no changes needed in Wix.
- **DMARC reports** go to `tools@scalehere.com`.
- **Domain warmup** is in Stage 1 on `s.scalehere.com` — send consistently to build reputation. Don't stress test with empty emails.
- **Level 3 upgrade** is unblocked — GoDaddy supports all record types. Just add per-client subdomains when ready.
