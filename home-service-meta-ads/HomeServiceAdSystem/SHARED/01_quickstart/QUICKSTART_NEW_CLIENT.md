# Quickstart — New Client Onboarding (10 minutes)

Use this every time you start a new home-service client. Total active time: ~10 minutes. Total elapsed time including agent runs: ~3-4 hours of mostly-passive work spread across a day.

---

## Before you start — gather these (5 minutes)

1. **Client website URL** (the public marketing site)
2. **Brand assets:** logo PNG (transparent bg), founder photo, license number, brand colors
3. **Real install photos** — download to `/CLIENTS/[Name]/03_assets/photos/`
4. **Customer review URLs** — Google profile URL, Yelp, Houzz, BBB, Angi
5. **Current offers** the client wants to push — write down headline, terms, expiration, exclusions
6. **Operational context:**
   - Daily measure/quote capacity
   - Service area radius
   - Legal exposures
   - Customer-quote consent status
   - Current marketing budget

See `/SHARED/03_templates/client-onboarding-checklist.md` for the full intake list.

---

## Setup — 2 minutes

```
1. In Drive, copy /SHARED/06_client-template/ to /CLIENTS/[ClientName]/
2. Drop client logo PNG + founder photo into /CLIENTS/[ClientName]/00_intake/brand_assets/
3. Drop install photos into /CLIENTS/[ClientName]/03_assets/photos/
4. Open a new Cowork chat. Connect to Google Drive with access to:
   - /SHARED/ (read)
   - /CLIENTS/[ClientName]/ (read + write)
```

---

## Run the pipeline

For each agent, open the prompt file in `/SHARED/02_agents/`, copy the system prompt, paste into the appropriate Cowork chat, fill in bracketed inputs, run.

### Heavy agents — persistent chats (open one chat each, keep alive)

| Step | Agent | Chat | Time |
|---|---|---|---|
| 1 | Agent 1 — Intake Researcher | New chat: `[Client] Intake` | 30-45 min |
| 2 | Agent 2 — Creative Bible Builder | New chat: `[Client] Bible` | 45 min |
| 6 | Agent 6 — Concept Architect | New chat: `[Client] Concepts` | 30 min |
| 9 | Agent 9 — Brand Translator / Visual Director | New chat: `[Client] Visuals` | 20 min × N concepts |

### Light agents — one-shot prompts in the orchestrator chat

| Step | Agent | Time |
|---|---|---|
| 0 | Agent 0 — Orchestrator | Tells you what to run next |
| 3 | Agent 3 — Strategic Lever | 10 min |
| 4 | Agent 4 — Asset Curator | 15 min |
| 5 | Agent 5 — Reference Library Manager | 5 min per REF you save |
| 7 | Agent 7 — Stress Tester (HARD GATE) | 10 min |
| 8 | Agent 8 — Copy Writer | 15 min |
| 10 | Agent 10 — Production Brief | 10 min |

---

## The reference-hunting step (between Agent 6 and Agent 7)

After Agent 6 outputs concepts, it ALSO outputs a "reference hunt list" — for each concept, what type of competitor ad you should go find as visual inspiration.

You then:
1. Open Meta Ad Library: https://www.facebook.com/ads/library
2. Search competitors from Agent 1's intake brief
3. Find ads matching the visual pattern Agent 6 described
4. Screenshot them
5. Run them through your image-to-JSON tool
6. Hand the raw JSON to Agent 5 (Reference Library Manager) → outputs REF-XXX
7. Hand REF-XXX + concept ID to Agent 9 → outputs 3 JSON variations rebranded to your client

This is the single step where YOUR aesthetic taste enters the system. Don't skip it.

---

## Image generation step (after Agent 9)

For each AD-XXX.json (3 variations per concept):

1. Open ChatGPT Image
2. Paste the JSON prompt
3. Upload reference images if the JSON requires (founder photo for portraits)
4. Generate
5. Download to `/CLIENTS/[Name]/07_generated/`

---

## Canva compositing step

Each generated image has an empty white-card placeholder in zone 1 (top-left) for the logo.

1. Open generated image in Canva
2. Drop client's real logo PNG into the placeholder zone
3. Export at 1440×1800
4. Save to `/CLIENTS/[Name]/08_final/`

For flyer-mode ads only: also drop in branded footer PNG built once during Agent 4.

---

## Launch

`/CLIENTS/[Name]/09_launch/launch_brief.md` contains:
- Round-one budget split per concept
- Audience targeting parameters
- Lead form qualifying questions
- KPI targets
- Kill criteria with day-10 thresholds
- Consent verification checklist

Follow it exactly.

---

## What if a step breaks?

| Issue | Fix |
|---|---|
| Agent 1 can't access the website | Paste About + Services pages directly |
| Agent 7 kills more than half the concepts | Correct behavior — return to Agent 6 with kill reasons |
| Agent 9 outputs weak variations | Reference JSON wasn't strong enough — find a different competitor ad |
| Generated image has gibberish text | Keep text big or composite in Canva |
| Generated image has wrong logo | Always — composite real logo in Canva |

---

## Total time per client

- Active hands-on time: ~3 hours
- Total elapsed time: ~6-8 hours over 1-2 days
- Output: 3-5 stress-tested concepts × 3 JSON variations = 9-15 ad assets ready to launch

By client #3 you'll be running this in your sleep.
