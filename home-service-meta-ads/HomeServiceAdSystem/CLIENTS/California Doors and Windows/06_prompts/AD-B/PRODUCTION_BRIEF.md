# PRODUCTION BRIEF — AD-B · CONCEPT-B: Before/After

**Prepared by:** Agent 10 (Production Brief)
**Date:** 2026-04-26
**Client:** California Doors and Windows
**Mode:** CLONE MODE (99% structural adherence to REF-002) · Path D NOT used (no founder hero in this concept) · V1 uses real-photo composite of `before_after_001.png`
**Round:** Round 1
**Status before launch:** ready to generate after V1 production audit on `before_after_001.png` completes; pre-launch consent gate must pass before paid deployment

Cross-checks passed before save:
- ✅ V1.json, V2.json, V3.json all valid JSON
- ✅ Locked copy byte-identical across V1/V2/V3 — headline lines, compliance fine print, sub-headline-NONE, trust-strip-NONE, CTA-NONE
- ✅ Hero photo subject differs across V1 (real CDW install — `before_after_001.png` divided-light window in stucco wall) / V2 (AI-gen alternate window style — casement / sliding / fixed-pane in stucco) / V3 (AI-gen third asset class — sliding-glass door OR window in board-and-batten / stone-facade / lap siding)
- ✅ Real-photo attachment correctly flagged on V1 only — `reference_photo_attachment_required: true` + `reference_photo_path: /CLIENTS/California Doors and Windows/03_assets/photos/before_after_001.png`
- ✅ V2 and V3 have `reference_photo_attachment_required: false` and no `reference_photo_path`
- ✅ REF-002 exists at `/SHARED/04_reference-library/REF-002/` (ref.png + ref.json + metadata.md, banked 2026-04-26 from Meta Ad Library)
- ✅ Brand system consistent across all three (CDW palette, 1440×1800, full-bleed bottom edge, no footer)

**Note on Path D for AD-B V1.** Strict Path D applies to AI-generated founder likeness using a real photo as identity reference (per `/CLIENTS/California Doors and Windows/00_intake/path_d_approval.md` — applies to V1 founder hero only, on Concept A). AD-B V1 is NOT a Path D variation — it is a real-photo composite workflow where the source photo is rendered as the hero rather than used as an AI identity reference. The system designer's "Path D attachment requirements correctly flagged for AD-A V1 and AD-B V1" cross-check is read here as: V1 of both ads carries a real-photo attachment requirement, and that attachment requirement is correctly flagged in each V1 JSON. AD-A V1 is Path D (founder identity reference); AD-B V1 is real-photo composite. Both are correctly flagged with `reference_photo_attachment_required: true` and the correct `reference_photo_path`.

---

## 1. Concept summary

| Field | Value |
|---|---|
| Concept name | Before/After |
| Concept ID | CONCEPT-B → AD-B |
| Reference cloned | REF-002 (BEFORE/AFTER 40% Spring Special — black-line-1 + red-line-2 ALL CAPS headline · 50/50 horizontal BEFORE/AFTER window split · yellow rectangular BEFORE/AFTER badges · Google Business Review badge top-right with 5.0 stars) |
| Reference path | `/SHARED/04_reference-library/REF-002/ref.png` + `/SHARED/04_reference-library/REF-002/ref.json` |
| Reference adherence target | 99% |
| Reference adherence self-score | 99% with one documented 1% structural flex (headline line 2 wording — see §5) |
| Lead avatar | Burned-Once Bob ("how do I know your installs hold up" objection resolved by the photo before any copy fires) → also lands Pacific Beach Pat and Coronado Karen |
| Awareness stage | Solution Aware |
| Primary angle | COMPARISON / TRANSFORMATION — real proof; the install IS the argument |
| Family | clones REF-002 before/after-with-headline layout (Family 4A transformation × Family 2 offer hybrid as the reference reads it) |
| Predicted strength | **Strong second to Concept A in the Round 1 slate.** V1 is the only variation in the slate that ships a verifiable transformation artifact rather than a render — proof-of-craft mechanic carries the test. AI-gen V2/V3 alternates measure whether the dramatic-transformation format converts independent of real-photo authenticity. |

---

## 2. Locked copy (verbatim from `/CLIENTS/California Doors and Windows/05_copy/AD-B_copy.md`)

**This copy is byte-identical across V1, V2, and V3. Do not modify across variations.**

- **Headline line 1 (BLACK ALL CAPS, top of frame, bold sans-serif):** **`TIRED OF YOUR OLD WINDOWS?`**
- **Headline line 2 (RED ALL CAPS, directly beneath line 1, bold sans-serif, same display scale, CDW warm red `#C8102E`):** **`GET 40% OFF — LIMITED TIME`**
- **Sub-headline:** NONE.
- **Trust strip (text element):** NONE — the trust strip is the visual Google Business Review badge in the top-right corner.
- **CTA:** NONE — REF-002 has no CTA, the clone inherits the restraint.
- **Compliance fine print (zone 4 bottom edge, ~10–12 pt soft-grey or off-white sans-serif):** **`Limited-time offer — see in-home estimate for details. CSLB #537570. Family-owned in Southern California since 1988.`**

**BEFORE/AFTER badges (visual element, locked across all three):**
- BEFORE — yellow rectangular badge, bold black sans-serif, bottom-left of LEFT panel
- AFTER — yellow rectangular badge, bold black sans-serif, bottom-right of RIGHT panel
- Yellow may shift to CDW mustard-yellow `#FFC72C` within the brand-color swap budget (NOT 1% flex)

**Top-right Google Business Review badge (Path 1 — user-attached at generation):**
- Visual badge / screenshot with CDW's actual rating + 5-star row
- **Fallback:** Houzz 5.0 badge if no qualifying Google rating is available — CDW is Best of Houzz 2026 (Service Excellence) + Best of Houzz 2025

---

## 3. The 3 variations table

| Variation | Hero subject (the only axis that varies) | Path | Image input required | Asset(s) to attach at generation time |
|---|---|---|---|---|
| **V1** | Real CDW install — side-by-side BEFORE/AFTER from `before_after_001.png`. Left = peeling original frame; right = fresh white-frame divided-light window in the same opening. Stucco wall context. | Real-photo composite + Path 1 (Google badge attached) | YES | `before_after_001.png` (`/CLIENTS/California Doors and Windows/03_assets/photos/before_after_001.png`) — AND CDW Google Business Review badge image (or Houzz 5.0 fallback) |
| **V2** | AI-gen alternate BEFORE/AFTER pair, **DIFFERENT WINDOW STYLE** from V1 (casement, sliding, OR fixed-pane picture window). Same dramatic transformation logic; clearly distinct window style. Generic SoCal residential, no recognizable address. | Pure AI-gen for the panels + Path 1 (Google badge attached) | NO real-photo for panels | CDW Google Business Review badge image (or Houzz 5.0 fallback) |
| **V3** | AI-gen alternate BEFORE/AFTER pair, **THIRD STYLE VARIANT** — sliding-glass door OR window in a different exterior wall context (board-and-batten siding, stone facade, OR painted wood lap siding instead of beige stucco). | Pure AI-gen for the panels + Path 1 (Google badge attached) | NO real-photo for panels | CDW Google Business Review badge image (or Houzz 5.0 fallback) |

**Locked across V1/V2/V3:**
- Layout — top of frame two-line ALL CAPS headline · middle 50/50 horizontal BEFORE/AFTER split · yellow rectangular badges at panel bottom corners · Google Business Review badge top-right · compliance fine-print at bottom edge · full-bleed
- Headline line 1 (`TIRED OF YOUR OLD WINDOWS?`) byte-identical
- Headline line 2 (`GET 40% OFF — LIMITED TIME`) byte-identical
- Compliance fine print byte-identical
- Yellow BEFORE/AFTER badge style + placement
- Google Business Review badge top-right placement (or Houzz fallback)
- Lighting / camera setup — ~35–50 mm equivalent, head-on / square-to-wall, natural daylight ~5200K, warm cast
- Zone 1 logo strip — clean negative space 360 × 140 px top-left, 60 px margin in the AI pass (uninterrupted background, no placeholder box, no dashed outline, no white card, no visible zone marker); CDW logo composited in Canva post-generation
- Footer policy — NONE; full-bleed bottom edge

---

## 4. Brand system applied

| Element | Value | Source |
|---|---|---|
| Canvas | 1440 × 1800 px, 4:5 vertical, Meta-native | `CDW_design_system.json` `canvas` block |
| Primary color | CDW Yellow `#FFC72C` (verified:false) — applies to BEFORE/AFTER badge fill (allowed shift from generic yellow within brand-color swap budget) | `palette.primary` |
| Secondary color | CDW Red `#C8102E` (verified:false) — applies to headline line 2 ALL CAPS text | `palette.secondary` |
| Neutrals | Black `#000000` (headline line 1 + BEFORE/AFTER badge type). Zone 1 top-left is clean negative space in the AI pass (no white card; logo composited in Canva post-generation) | `palette.neutral_dark` + `palette.neutral_light` |
| Typography (headline) | Heavy sans-serif (e.g., Inter Bold or equivalent), ALL CAPS, bold weight, large display scale | system designer note + REF-002 type spec |
| Typography (BEFORE/AFTER badge type) | Bold black sans-serif on yellow background | REF-002 spec |
| Typography (compliance line) | ~10–12 pt soft-grey or off-white sans-serif | system designer note |
| Photography mood | Real-photo authenticity on the BEFORE/AFTER panels — slightly imperfect (reflection artifacts read as authenticity, NOT carelessness); never staged-real-estate-glossy | `photography_mood` + asset audit Section 3 |
| Voice register | Direct-response cadence per REF-002 — question on line 1 + offer/urgency answer on line 2 (NOT website-hero voice) | `voice` |
| Banned phrases (must not appear anywhere) | elevate, unlock, transform, leverage, premium experience, in the realm of, uncompromising, timeless design, precision-crafted, refined home solutions, today only, bare "lifetime warranty," starting from $X, generic "energy efficient" | `voice.forbidden_phrases` + Strategic Lever Round 1 banned list. **Note:** internal angle name is "TRANSFORMATION" but the word "transform" does NOT appear in any output copy. |
| Compliance line | `Limited-time offer — see in-home estimate for details. CSLB #537570. Family-owned in Southern California since 1988.` | Project Instructions Compliance Locks + offer audit vague-terms lock |

---

## 5. Reference adherence

| Field | Value |
|---|---|
| REF used | REF-002 — `/SHARED/04_reference-library/REF-002/ref.png` (Banked 2026-04-26 from Meta Ad Library — BEFORE/AFTER 40% Spring Special) |
| Adherence target | 99% (CLONE MODE) |
| Self-score | 99% with one documented 1% structural flex |
| Cloned elements (must match REF-002) | Layout (top-of-frame headline · middle 50/50 BEFORE/AFTER split · yellow rectangular badges at panel bottom corners · Google Business Review badge top-right · compliance fine print at bottom edge · full-bleed); headline structure (TWO LINES, ALL CAPS, line 1 BLACK + line 2 RED, question + offer/urgency rhythm); BEFORE/AFTER 50/50 split with identical proportions; yellow rectangular badge style + placement; Google Business Review badge placement; typography hierarchy (headline largest → BEFORE/AFTER badges secondary → Google badge tertiary → compliance smallest); no CTA; no footer |
| Allowed asset swaps applied (NOT flex) | Photo content (V1 real CDW install / V2 AI-gen alternate window style / V3 AI-gen third asset class); brand colors (line 2 red picks up CDW warm red rather than reference's generic red; badge yellow may shift to CDW mustard-yellow); Google Business Review badge content (CDW's actual rating + 5-star row, Houzz 5.0 fallback acceptable); zone 1 logo strip Canva composite (REF-002 has no top wordmark — locked CDW design-system zone 1 logo strip is the brand-fit improvement, NOT 1% flex) |
| Documented 1% structural flex deviations | **ONE FLEX:** Headline line 2 wording — `GET 40% OFF WITH OUR SPRING SPECIAL` (REF-002, 7 words) → `GET 40% OFF — LIMITED TIME` (CDW, 6 words). **Justifications:** (1) Seasonal "SPRING SPECIAL" dates the creative; "LIMITED TIME" carries equivalent urgency without dating the ad. (2) Pairs with the locked vague-terms compliance language so the disclosure shows up at two reading heights (headline + fine print). (3) Word count delta within ±1–2 word 1% flex budget. (4) Direct-response energy preserved — question + offer/urgency rhythm + black/red ALL CAPS treatment + same line count. |

---

## 6. Step-by-step generation instructions per variation

**Recommended primary generator: ChatGPT Image** (composites attached real photos cleanly into a layout slot and renders type/badge layers at high fidelity; for V1 specifically, ChatGPT Image's image-conditioning behavior preserves the real BEFORE/AFTER panels without re-rendering them).

### V1 — Real CDW install (real-photo composite)

**Pre-flight production audit on `before_after_001.png` (asset audit Section 3 requirement) — must complete BEFORE generation:**

1. **Reflection cleanup on right (after) panel** — visible glare/reflection on the new window's glass; retouch or accept as authenticity signal at production review.
2. **Framing tightening** — slight crop / horizon correction to lock the 50/50 split for the 1440 × 1800 hero zone.
3. **Resolution audit** — confirm pixel dimensions are sufficient; if undersized for the locked hero zone, upscale via a non-face-aware path.
4. **Anonymization** — confirm no readable house numbers, street signs, or recognizable architectural features in the final crop.
5. **Homeowner consent** — confirm separately that the homeowner whose install this is has authorized use of the install imagery for advertising. **DO NOT LAUNCH V1 if consent is unverified** — see §8 pre-launch consent gate.

**Generation steps (after audit completes):**

1. Open ChatGPT Image (or equivalent generator that accepts attached image input + supports real-photo composite into a layout slot).
2. **Attach** `/CLIENTS/California Doors and Windows/03_assets/photos/before_after_001.png` (post-audit version). Generator composites the source asset's BEFORE half into the left panel and AFTER half into the right panel — **do NOT re-render the install panels.**
3. **Attach** the CDW Google Business Review badge image (top-right corner). Use Houzz 5.0 fallback if no qualifying Google rating is available.
4. Paste the JSON prompt from `/CLIENTS/California Doors and Windows/06_prompts/AD-B/V1.json` as the prompt body.
5. Generate at 1440 × 1800 (4:5 vertical Meta-native).
6. **Verify the headline reads `TIRED OF YOUR OLD WINDOWS?` (BLACK ALL CAPS) on line 1 and `GET 40% OFF — LIMITED TIME` (RED ALL CAPS) on line 2** — exact strings, no paraphrasing, no "Spring Special" residue from the reference.
7. **Verify the BEFORE/AFTER 50/50 split** — left panel BEFORE, right panel AFTER, identical aspect, real CDW install panels NOT re-rendered.
8. Verify yellow rectangular BEFORE/AFTER badges sit at panel bottom corners (BEFORE bottom-left of LEFT panel, AFTER bottom-right of RIGHT panel).
9. Verify Google Business Review badge sits in the top-right corner with CDW's rating + 5-star row.
10. Verify compliance fine print at bottom edge reads exactly: `Limited-time offer — see in-home estimate for details. CSLB #537570. Family-owned in Southern California since 1988.`
11. Verify zone 1 top-left is clean negative space — uninterrupted background, no placeholder box, no dashed outline, no white card, no visible zone marker (CDW logo composited in Canva post-generation; the AI pass should leave clean background here so no placeholder needs erasing first).
12. Expected output filename: `AD-B_V1_AI_RAW.png` — save to `/CLIENTS/California Doors and Windows/07_generated/`.

### V2 — AI-gen alternate window style (no real-photo for panels)

1. Open ChatGPT Image. **Do NOT attach** `before_after_001.png`. Attach only the CDW Google Business Review badge image (or Houzz 5.0 fallback).
2. Paste the JSON prompt from `/CLIENTS/California Doors and Windows/06_prompts/AD-B/V2.json`.
3. Generate at 1440 × 1800.
4. **Verify the AFTER window style is CLEARLY DIFFERENT from V1's divided-light sash** — should read as casement, sliding double-pane, OR fixed-pane picture window. If V2's window style reads as the same style as V1, regenerate.
5. **Verify panels do NOT depict a recognizable address, neighborhood, or named individual.** No readable house numbers, no street signs, no specific neighborhood signage.
6. Verify headline + badges + Google badge + compliance line match V1 byte-identical.
7. Expected output filename: `AD-B_V2_AI_RAW.png` — save to `/CLIENTS/California Doors and Windows/07_generated/`.

### V3 — AI-gen third style variant (no real-photo for panels)

1. Open ChatGPT Image. **Do NOT attach** `before_after_001.png`. Attach only the CDW Google Business Review badge image (or Houzz 5.0 fallback).
2. Paste the JSON prompt from `/CLIENTS/California Doors and Windows/06_prompts/AD-B/V3.json`.
3. Generate at 1440 × 1800.
4. **Verify V3 is a clearly different transformation from BOTH V1 and V2** — sliding-glass door OR window in board-and-batten / stone-facade / lap-siding wall context (NOT V1's stucco + divided-light, NOT V2's stucco + casement/sliding/fixed-pane window). If V3's asset class or exterior context overlaps V1 or V2, regenerate.
5. Verify no recognizable address.
6. Verify headline + badges + Google badge + compliance line match V1 and V2 byte-identical.
7. Expected output filename: `AD-B_V3_AI_RAW.png` — save to `/CLIENTS/California Doors and Windows/07_generated/`.

---

## 7. Step-by-step Canva composition instructions per variation

The same Canva composite is applied to V1, V2, and V3 — only the AI-generated background plate changes.

1. Open Canva at 1440 × 1800 (4:5 vertical).
2. Drop the AI-generated raw plate (`AD-B_V[1|2|3]_AI_RAW.png`) as a full-bleed background layer.
3. **CDW logo composite — zone 1 top-left:**
   - Asset: `/CLIENTS/California Doors and Windows/00_intake/brand_assets/CDW_logo.png` (raster — vector requested for Round 2).
   - Place over the clean negative space the AI pass left in the top-left, 360 × 140 px footprint with 60 px margin from the canvas top and left edges (no placeholder to erase first — the AI pass renders uninterrupted background here).
   - Verify logo does NOT cross over headline line 1 — adjust placement only if the AI plate's headline starts too high; do not move the headline.
4. **Top-right Google Business Review badge:** the AI pass renders this from the attached badge image. Verify the rating + 5-star row read clearly at Meta feed mobile zoom; if illegible, drop the badge image as a Canva layer over the AI plate's top-right corner with 60 px margin.
5. **Footer:** NONE. Standard Meta ad — no branded footer composite.
6. **Compliance line:** the AI pass renders this. Verify legibility at 100% Meta feed mobile zoom; if illegible, retype in Canva at ~10–12 pt soft-grey or off-white sans-serif over the AI plate's bottom edge.
7. Export as PNG at 1440 × 1800.
8. Expected final filenames:
   - `AD-B_V1_FINAL.png`
   - `AD-B_V2_FINAL.png`
   - `AD-B_V3_FINAL.png`
9. Save to `/CLIENTS/California Doors and Windows/08_final/`.

---

## 8. QA checklist (must pass before launch)

**Across V1/V2/V3 (locked-element identity):**

- [ ] Headline line 1 byte-identical — exact string `TIRED OF YOUR OLD WINDOWS?` (BLACK ALL CAPS)
- [ ] Headline line 2 byte-identical — exact string `GET 40% OFF — LIMITED TIME` (RED ALL CAPS)
- [ ] Compliance fine print byte-identical — exact string `Limited-time offer — see in-home estimate for details. CSLB #537570. Family-owned in Southern California since 1988.`
- [ ] Layout identical — top-of-frame two-line headline · middle 50/50 BEFORE/AFTER split · yellow rectangular badges at panel bottom corners · Google Business Review badge top-right · compliance fine print bottom edge · full-bleed
- [ ] Brand system identical across V1/V2/V3 — same palette, same lighting, same camera angle (head-on / square-to-wall), same compliance line, same zone 1 logo composite
- [ ] Hero subject differs across V1/V2/V3 — real CDW install vs. AI alternate window style vs. AI third asset class / exterior context (and V2 ≠ V3 — different window style or asset class, not noise)

**Real-photo authenticity (V1 specifically):**

- [ ] V1 was generated with `before_after_001.png` (post-audit version) attached as the source for the BEFORE/AFTER panels
- [ ] V1 install panels are NOT re-rendered — the attached real photo composites cleanly into the layout slot
- [ ] V1 panels carry no readable house numbers, street signs, or specific neighborhood signage
- [ ] V2 and V3 do NOT claim to depict actual CDW installs — generic SoCal residential, no recognizable address

**BEFORE/AFTER badge quality:**

- [ ] BEFORE badge in bottom-left of LEFT panel — yellow rectangular, bold black sans-serif, identical placement V1/V2/V3
- [ ] AFTER badge in bottom-right of RIGHT panel — yellow rectangular, bold black sans-serif, identical placement V1/V2/V3
- [ ] Headline does NOT cross the vertical gutter between BEFORE and AFTER panels

**Top-right Google Business Review badge quality:**

- [ ] Google badge sits in top-right corner with rating + 5-star row legible at Meta feed mobile zoom
- [ ] If Google badge unavailable, Houzz 5.0 fallback is in place — top-right corner, Best of Houzz 2026 / 2025 source

**Logo quality (zone 1 top-left):**

- [ ] CDW logo composited cleanly in zone 1 top-left at 360 × 140 px, 60 px margin
- [ ] No AI-generated logo trace, no auto-generated wordmark residue
- [ ] Logo does not cross over headline line 1

**Compliance line legibility:**

- [ ] Compliance line legible at 100% Meta feed mobile zoom
- [ ] Compliance line carries CSLB #537570, family-owned/since-1988 phrasing, no banned phrases, no 25C reference, no brand-dealer claim

**Anonymization compliance:**

- [ ] No customer name or initial visible anywhere
- [ ] V1 install image carries no readable identifiers (house numbers, street signs)
- [ ] Trust attribution (any visible source) reads as anonymous SoCal homeowner if at all

**Banned phrase scan (manual read of every legible line):**

- [ ] `elevate`, `unlock`, `transform`, `leverage`, `premium experience`, `in the realm of`, `uncompromising`, `timeless design`, `precision-crafted`, `refined home solutions` — NONE present (the angle name is internally "TRANSFORMATION" but the word `transform` does NOT appear in any output copy field)
- [ ] `today only`, bare `lifetime warranty`, `starting from $X`, generic `energy efficient` — NONE present
- [ ] No 25C / federal-tax-credit reference
- [ ] No brand-dealer claim (Milgard / Andersen / Anlin)

**Vague-terms disclaimer (offer-bearing creative — REQUIRED):**

- [ ] `Limited-time offer — see in-home estimate for details` is present in the compliance line at the bottom edge
- [ ] `LIMITED TIME` is present in headline line 2 (echoes the disclaimer at headline reading height)
- [ ] No specific calendar end date is printed anywhere

**Pre-launch consent gate (V1 — REAL CDW INSTALL):**

- [ ] Homeowner consent for use of `before_after_001.png` install imagery is verified IN WRITING and filed in `/CLIENTS/California Doors and Windows/03_assets/consent/`
- [ ] **DO NOT LAUNCH V1 if homeowner consent is unverified.** Block the variation; ship V2 + V3 only and re-add V1 once consent lands.

**Pre-launch offer terms verification:**

- [ ] "10 windows for 40% off" offer terms are confirmed by Mike on file (asset audit Section 2 — confirmed 2026-04-26)
- [ ] Vague-terms disclosure language is the locked spec — `Limited-time offer — see in-home estimate for details`
- [ ] No specific end date printed; no off-of-MSRP-vs-list specification; no minimum spend disclosed

---

## 9. Hypothesis & test plan

**Predicted winner: V1 (real CDW install — `before_after_001.png`).**

The whole mechanic of Concept B is "the install IS the argument" — Burned-Once Bob's "how do I know your installs hold up" objection gets resolved by a real photo before any copy fires. V1 is the only variation in the slate that ships a verifiable transformation artifact rather than a render. AI-generated before/afters look like AI-generated before/afters at feed scale; real install photos look like real install photos. If V1 hits its lift target, that's evidence the proof-of-craft mechanic is working and Round 2 should weight real-photo creative.

**V2** is the AI-gen disciplined alternate — does the same dramatic transformation work when the install is generic / AI-gen and the window style differs from V1? If V2 outperforms V1, the lever is the BEFORE/AFTER format itself (not the realness of the photo), and Round 2 can scale-out AI-gen variations more aggressively.

**V3** tests whether shifting the asset class (sliding-glass door OR alternate exterior wall context) opens a new audience segment — homeowners with patio doors or non-stucco exteriors who didn't see themselves in V1/V2's window-in-stucco pair. If V3 reaches a different audience segment with similar conversion economics, Round 2 can fan out into asset-class-specific creative (door-led ads, multi-trade ads, etc.).

**Round 1 budget split recommendation (within Concept B):** lean V1 at ~50% of Concept B spend assuming consent lands; V2 and V3 each at ~25%. If V1 consent does not land before launch, run V2 and V3 at 50/50 and re-introduce V1 once consent is filed. Read after 10–14 days.

---

## 10. Filenames for launch

| File | Path |
|---|---|
| Locked copy source | `/CLIENTS/California Doors and Windows/05_copy/AD-B_copy.md` |
| V1 JSON | `/CLIENTS/California Doors and Windows/06_prompts/AD-B/V1.json` |
| V2 JSON | `/CLIENTS/California Doors and Windows/06_prompts/AD-B/V2.json` |
| V3 JSON | `/CLIENTS/California Doors and Windows/06_prompts/AD-B/V3.json` |
| Variation notes | `/CLIENTS/California Doors and Windows/06_prompts/AD-B/variation_notes.md` |
| V1 real-photo source | `/CLIENTS/California Doors and Windows/03_assets/photos/before_after_001.png` (post-audit version) |
| Reference cloned | `/SHARED/04_reference-library/REF-002/ref.png` |
| AI raw output — V1 | `/CLIENTS/California Doors and Windows/07_generated/AD-B_V1_AI_RAW.png` |
| AI raw output — V2 | `/CLIENTS/California Doors and Windows/07_generated/AD-B_V2_AI_RAW.png` |
| AI raw output — V3 | `/CLIENTS/California Doors and Windows/07_generated/AD-B_V3_AI_RAW.png` |
| Canva final — V1 | `/CLIENTS/California Doors and Windows/08_final/AD-B_V1_FINAL.png` |
| Canva final — V2 | `/CLIENTS/California Doors and Windows/08_final/AD-B_V2_FINAL.png` |
| Canva final — V3 | `/CLIENTS/California Doors and Windows/08_final/AD-B_V3_FINAL.png` |
| Homeowner consent file (V1 — must be filed before launch) | `/CLIENTS/California Doors and Windows/03_assets/consent/before_after_001_consent.[pdf|md]` |

---

Saved to `/CLIENTS/California Doors and Windows/06_prompts/AD-B/PRODUCTION_BRIEF.md`. Next: AD-C PRODUCTION_BRIEF.md.
