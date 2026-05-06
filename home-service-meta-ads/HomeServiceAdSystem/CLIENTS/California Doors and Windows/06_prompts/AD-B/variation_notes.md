# CONCEPT-B — Variation Notes (CLONE MODE · REF-002 clone)

**Concept:** CONCEPT-B — Before/After
**Mode:** CLONE MODE — 99% structural adherence to REF-002 (BEFORE/AFTER 40% off layout)
**Reference cloned:** REF-002 — `/SHARED/04_reference-library/REF-002/ref.png`
**Copy source:** `/CLIENTS/California Doors and Windows/05_copy/AD-B_copy.md`
**Approvals consulted:** `/CLIENTS/California Doors and Windows/00_intake/path_d_approval.md` (CLONE MODE — Path D NOT used in this concept)
**Author:** Agent 9 — Brand Translator
**Date:** 2026-04-26

---

## What's locked across V1 / V2 / V3 (everything except hero photo subject)

- **Layout:** top of frame two-line ALL CAPS headline · middle 50/50 horizontal BEFORE/AFTER split · yellow rectangular BEFORE/AFTER badges at panel bottom corners · Google Business Review badge top-right · compliance fine-print line at bottom edge · full-bleed.
- **Headline line 1 (BLACK ALL CAPS):** `TIRED OF YOUR OLD WINDOWS?` — byte-identical V1 / V2 / V3.
- **Headline line 2 (RED ALL CAPS):** `GET 40% OFF — LIMITED TIME` — byte-identical V1 / V2 / V3.
- **Sub-headline / trust strip / CTA:** NONE — REF-002 has none, the clone inherits the restraint. The visible trust mark is the Google Business Review badge in the top-right.
- **Compliance fine print:** byte-identical V1 / V2 / V3 — `Limited-time offer — see in-home estimate for details. CSLB #537570. Family-owned in Southern California since 1988.`
- **Yellow BEFORE/AFTER badges:** identical placement, color, weight, casing across all three.
- **Google Business Review badge (top-right):** identical placement; user attaches CDW's actual badge or Houzz 5.0 fallback at generation across all three.
- **Brand palette:** CDW sun-yellow `#FFC72C` + warm red `#C8102E` + off-white + soft black per `/CLIENTS/California Doors and Windows/00_intake/brand_assets/CDW_design_system.json`.
- **Lighting / time of day / camera setup:** identical across all three (~35-50mm equivalent · head-on / square-to-wall · natural daylight ~5200K · warm cast).
- **Zone 1 logo strip:** EMPTY in the AI pass; identical Canva-composite call across V1 / V2 / V3.
- **Footer policy:** NONE — full-bleed bottom edge.

## What varies V1 / V2 / V3 — hero photo subject only

| Variation | Hero subject | Path | Image input required |
|---|---|---|---|
| **V1** | **Real CDW install — `before_after_001.png`** attached at generation. Generator composites the source asset's BEFORE half into the left panel and AFTER half into the right panel. Production audit per asset audit Section 3 must complete before V1 ships. | Real-photo composite | YES — `before_after_001.png` |
| **V2** | **AI-gen alternate BEFORE/AFTER**, DIFFERENT WINDOW STYLE from V1 (casement, sliding, OR fixed-pane picture window). Same dramatic transformation logic; clearly distinct window style. | Pure AI-gen, generic SoCal residential | NO |
| **V3** | **AI-gen alternate BEFORE/AFTER**, THIRD STYLE VARIANT — sliding-glass door OR window in a different exterior wall context (board-and-batten siding, stone facade, painted wood lap siding instead of beige stucco). | Pure AI-gen, generic SoCal residential | NO |

This menu adapts the standard variation framework to CONCEPT-B's per-concept hero subject plan: V1 real install, V2 AI alternate window style, V3 AI alternate asset class / exterior context. The variations differ on a single axis (the BEFORE/AFTER pair shown), and that axis is genuinely distinct across the three (real → AI window-style swap → AI asset-class / exterior swap), not noise.

## Reference adherence self-score

- **Target:** 99% (CLONE MODE)
- **Self-score:** 99%
- **Cloned elements (must match REF-002):** layout, headline structure (two lines, ALL CAPS, line 1 BLACK + line 2 RED, question + offer rhythm), BEFORE/AFTER 50/50 horizontal split with identical proportions, yellow rectangular BEFORE/AFTER badge style and placement, Google Business Review badge top-right corner, typography hierarchy, no CTA, no footer.
- **Allowed asset swaps applied (not flex):** photo content (V1 real CDW install / V2 AI window-style swap / V3 AI asset-class swap), brand colors, Google Business Review badge content (CDW's actual rating + 5-star row), V1 attaches real CDW install, V2/V3 are AI-gen alternates with no claim of depicting actual installs.

## Documented 1% structural flex deviations

**One flex used (per AD-B_copy.md):**

| Element | REF-002 value | CDW value | Flex justification |
|---|---|---|---|
| Headline line 2 wording | `GET 40% OFF WITH OUR SPRING SPECIAL` (7 words) | `GET 40% OFF — LIMITED TIME` (6 words) | Seasonal "SPRING SPECIAL" dates the creative; "LIMITED TIME" carries equivalent urgency without dating the ad and pairs with the locked vague-terms compliance language so the disclosure shows up at two reading heights (headline + fine print). Word count delta within the ±1–2 word 1% flex budget. Direct-response energy preserved (question on line 1 + offer/urgency answer on line 2; black/red ALL CAPS rhythm; same line count). |

No other flex used.

## Path D / Path 2 / Path 1 execution paths used per variation

| Variation | Path D (AI-gen founder likeness w/ real-photo reference) | Path 2 (rendered review card) | Path 1 (review-screenshot attachment) |
|---|---|---|---|
| **V1** | NO — no founder in concept | NO | YES — Google Business Review badge attached + real `before_after_001.png` attached |
| **V2** | NO | NO | YES — Google Business Review badge attached |
| **V3** | NO | NO | YES — Google Business Review badge attached |

## Hypothesis — which variation predicted to win in market and why

**Predicted winner: V1 (real CDW install — `before_after_001.png`).**

The whole mechanic of Concept B is "the install IS the argument" — Burned-Once Bob's "how do I know your installs hold up" objection gets resolved by a real photo before any copy fires. V1 is the only variation in the slate that ships with a verifiable transformation artifact rather than a render. AI-generated before/afters look like AI-generated before/afters at feed scale; real install photos look like real install photos. If V1 hits its lift target, that's evidence the proof-of-craft mechanic is working and Round 2 should weight real-photo creative.

**V2** is the AI-gen disciplined alternate — does the SAME dramatic transformation work when the install is generic / AI-gen and the window style differs from V1? If V2 outperforms V1, the lever is the BEFORE/AFTER format itself (not the realness of the photo), and Round 2 can scale-out AI-gen variations more aggressively.

**V3** tests whether shifting the asset class (sliding-glass door OR alternate exterior wall context) opens a new audience segment — homeowners with patio doors or non-stucco exteriors who didn't see themselves in V1/V2's window-in-stucco pair. If V3 reaches a different audience segment with similar conversion economics, Round 2 can fan out into asset-class-specific creative (door-led ads, multi-trade ads, etc.).

Spend prediction: lean V1 first; confirm against V2 and V3 in the same ad set after 10–14 days of read.

## Assets the user must attach at generation time (per variation)

### V1
1. **`before_after_001.png`** — `/CLIENTS/California Doors and Windows/03_assets/photos/before_after_001.png`. REAL CDW install. Production audit per asset audit Section 3 must complete before generation: reflection cleanup on right panel, framing tightening, anonymization (no readable house numbers / street signs), homeowner consent for use of install imagery.
2. **CDW Google Business Review badge** — visual badge / screenshot for top-right corner with CDW's actual rating + 5-star row. **Fallback: Houzz 5.0 badge** if no qualifying Google rating is available.
3. **CDW logo** — for Canva post-pass composite into zone_1 top-left placeholder.

### V2
1. NO real-photo attachment for the BEFORE/AFTER panels (pure AI-gen alternate window-style pair).
2. **CDW Google Business Review badge** (or Houzz 5.0 fallback) — same as V1.
3. **CDW logo** — same as V1.

### V3
1. NO real-photo attachment for the BEFORE/AFTER panels (pure AI-gen third style variant — sliding-glass door OR alternate exterior wall context).
2. **CDW Google Business Review badge** (or Houzz 5.0 fallback) — same as V1/V2.
3. **CDW logo** — same as V1/V2.

## Compliance check — passed before save

- ✅ CSLB `#537570` appears in compliance fine print on V1 / V2 / V3.
- ✅ Banned phrases (`elevate`, `transform`, `unlock`, `leverage`, `premium experience`, `in the realm of`, `uncompromising`, `timeless design`, `precision-crafted`, `refined home solutions`, `today only`, bare `lifetime warranty`, `starting from $X`, generic `energy efficient`) — NONE present. Note: the angle name internally is "TRANSFORMATION" but the word "transform" does NOT appear in any output copy field.
- ✅ "Limited-time" is allowed; the locked phrase is "Limited-time offer — see in-home estimate for details" in the compliance fine-print line, mirrored at headline reading height by "LIMITED TIME" in line 2.
- ✅ No 25C / federal-tax-credit references.
- ✅ No brand-dealer claims (no Milgard / Andersen / Anlin name attached).
- ✅ Anonymization lock honored — V1 BEFORE/AFTER panels require no readable house numbers / street signs / specific neighborhood signage per asset audit Section 3 (image_input_files list); V2 and V3 are AI-gen and explicitly do NOT claim to depict actual CDW installs.
- ✅ Locked copy across V1 / V2 / V3 is byte-identical (headline lines + compliance fine print).
- ✅ CLONE MODE approval verified in `/CLIENTS/California Doors and Windows/00_intake/path_d_approval.md`. Path D NOT used in this concept (no founder hero in any variation).
- ✅ No CTA bar — REF-002 has none, the clone inherits the restraint.
- ✅ Vague-terms disclaimer present at TWO reading heights: headline ("LIMITED TIME") and fine print ("Limited-time offer — see in-home estimate for details").

Saved to `/CLIENTS/California Doors and Windows/06_prompts/AD-B/`. Next: production audit `before_after_001.png` for V1, generate in ChatGPT Image with attached assets, composite logo in Canva post-pass.
