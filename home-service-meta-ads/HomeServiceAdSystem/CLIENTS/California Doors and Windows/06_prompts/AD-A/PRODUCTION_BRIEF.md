# PRODUCTION BRIEF — AD-A · CONCEPT-A: Mike's Hands-On 35 Years

**Prepared by:** Agent 10 (Production Brief)
**Date:** 2026-04-26
**Client:** California Doors and Windows
**Mode:** CLONE MODE (99% structural adherence to REF-001) · Path D active for V1
**Round:** Round 1
**Status before launch:** ready to generate; pre-launch consent gate must pass before paid deployment

Cross-checks passed before save:
- ✅ V1.json, V2.json, V3.json all valid JSON
- ✅ Locked copy byte-identical across V1/V2/V3 (compliance fine print + rendered Google review card spec)
- ✅ Hero photo subject differs across V1 (Mike portrait via Path D) / V2 (anonymous installer mid-install, no face) / V3 (anonymous installer, completion gesture, no face)
- ✅ Path D attachment requirement correctly flagged on V1 only — `reference_photo_attachment_required: true` + `reference_photo_path: /CLIENTS/California Doors and Windows/03_assets/photos/mike_founder.png`
- ✅ V2 and V3 have `reference_photo_attachment_required: false` and no `reference_photo_path`
- ✅ REF-001 exists at `/SHARED/04_reference-library/REF-001/` (ref.png + ref.json + metadata.md, banked 2026-04-26 from Meta Ad Library)
- ✅ Brand system consistent across all three (CDW yellow #FFC72C primary, warm red #C8102E secondary, off-white, soft black; 1440×1800 4:5 vertical; full-bleed bottom edge; no footer)

---

## 1. Concept summary

| Field | Value |
|---|---|
| Concept name | Mike's Hands-On 35 Years |
| Concept ID | CONCEPT-A → AD-A |
| Reference cloned | REF-001 (Brothers Home Improvement testimonial-led layout — installer left + Google review right + circular green-ribbon "30 YEARS" badge bottom-left + brand wordmark lockup bottom-right + 5-yellow-star row above wordmark) |
| Reference path | `/SHARED/04_reference-library/REF-001/ref.png` + `/SHARED/04_reference-library/REF-001/ref.json` |
| Reference adherence target | 99% |
| Reference adherence self-score | 99% (0% structural flex used; only allowed asset swaps applied — see §5) |
| Lead avatar | Burned-Once Bob (Zoran's "press 1, press 4, press 8 maze" review names the chain phone-tree pattern verbatim) → also lands Pacific Beach Pat and Coronado Karen |
| Awareness stage | Solution Aware |
| Primary angle | STORY (1988 founder, same phone since) + ANTI-CHAIN (real-person-picks-up vs. virtual-outfit phone-tree) |
| Family | clones REF-001 testimonial-led layout (Family 1 social-proof × Family 3A founder-authority hybrid as the reference reads it) |
| Predicted strength | **Highest-fit-ratio concept in the Round 1 slate.** Three avatars converge on V1: Bob's anti-virtual-outfit pain is named verbatim in the review body; Pat reads Mike as a Pacific Beach neighbor; Karen reads Mike-as-craftsman aesthetic. Predicted Round 1 winner among the 3-concept slate. |

---

## 2. Locked copy (verbatim from `/CLIENTS/California Doors and Windows/05_copy/AD-A_copy.md`)

**This copy is byte-identical across V1, V2, and V3. Do not modify across variations.**

- **Headline:** NONE — REF-001 has no separately written headline. The rendered Zoran K. Google review card serves as the headline area.
- **Sub-headline:** NONE.
- **Trust strip (text element):** NONE — the rendered Google review card itself IS the trust strip.
- **CTA:** NONE — REF-001 has no CTA, the clone inherits the restraint.
- **Compliance fine print (zone 4 bottom edge):** **`CSLB #537570 · Family-owned in Southern California since 1988.`**

**Rendered Google review card content (Path 2 — verbatim Zoran K. Google review, anonymized attribution):**

| Field | Value |
|---|---|
| Reviewer display name | `San Diego homeowner` (NOT "Zoran K.", NOT first-name-last-initial) |
| Profile avatar | Neutral generic circle — solid gray or muted blue, NO letter, NO initial. Generic person-silhouette icon acceptable. |
| Date stamp | `4 weeks ago` |
| Star row | 5 yellow stars (#FFC72C), single horizontal row above body |
| Platform mark | Google "G" multicolor logo, top-right of card |
| Review body (preferred — full text) | `"We had doors replaced about 6 years ago by a 'virtual' outfit and it turned into constant repairs, service calls, and headaches once the warranty ended. This time we wanted a real local company... when you call, a real person picks up and gets things handled. No 'press 1, press 4, press 8' maze."` |
| Review body (truncation fallback if full text doesn't fit) | `"We had doors replaced about 6 years ago by a 'virtual' outfit and it turned into constant repairs... This time we wanted a real local company... when you call, a real person picks up and gets things handled. No 'press 1, press 4, press 8' maze."` |
| Visual focal-point sentence | `"When you call, a real person picks up and gets things handled. No 'press 1, press 4, press 8' maze."` |
| Verbatim accuracy lock | Path 2 — review text and reviewer details are EXACT. If the generator drifts a word, swaps "virtual" for "online," renders an avatar initial, or mis-stamps the date, the variation FAILS QA and must be regenerated. |

---

## 3. The 3 variations table

| Variation | Hero subject (the only axis that varies) | Path | Image input required | Asset to attach at generation time |
|---|---|---|---|---|
| **V1** | Mike Marohnic (founder) walking with or holding a window frame in a residential exterior. Identity supplied by the attached `mike_founder.png`; JSON describes scene/composition only. | **Path D** + Path 2 (rendered review card) | YES | `mike_founder.png` (`/CLIENTS/California Doors and Windows/03_assets/photos/mike_founder.png`) — attached as identity reference |
| **V2** | Anonymous installer, back-view or three-quarter-back-view, seating/fastening a window into an existing residential exterior opening. NO face, NO Path D. | Pure AI-gen + Path 2 | NO real-photo attachment | None (review card is rendered as part of the AI pass) |
| **V3** | Anonymous installer, three-quarter-back-view, completing a finished install (final shim, sealant pass, step-back inspection). Finished window visible at the install point as outcome cue. NO face. Pose/moment subtly different from V2 so the variation reads as a clearly different moment. | Pure AI-gen + Path 2 | NO real-photo attachment | None |

**Locked across V1/V2/V3:**
- Layout — left ~50% installer-in-action photo · right ~50% rendered Google review card
- Rendered review-card content (verbatim Zoran K. text, anonymized attribution, neutral generic avatar, 5 stars, "4 weeks ago," Google G mark)
- Circular "35 YEARS" CDW-yellow ribbon-seal in bottom-left corner with `CALIFORNIA DOORS & WINDOWS · SINCE 1988` outer-ring sub-arc copy
- 5-yellow-star row above bottom-right wordmark lockup zone
- Bottom-right wordmark lockup zone — clean negative space in the AI pass (uninterrupted exterior background, no placeholder box, no dashed outline, no white wordmark zone marker); CDW logo composited in Canva post-generation
- Compliance fine print at bottom edge — `CSLB #537570 · Family-owned in Southern California since 1988.`
- Lighting / camera setup — 50mm equivalent, f/4, eye-level slightly off-axis, late-morning Californian daylight ~5200K, warm cast
- Footer policy — NONE; full-bleed bottom edge

---

## 4. Brand system applied

| Element | Value | Source |
|---|---|---|
| Canvas | 1440 × 1800 px, 4:5 vertical, Meta-native | `/CLIENTS/California Doors and Windows/00_intake/brand_assets/CDW_design_system.json` `canvas` block |
| Primary color | CDW Yellow `#FFC72C` (verified:false — eyedropped from raster logo, flagged for vector verification) | `palette.primary` |
| Secondary color | CDW Red `#C8102E` (verified:false) | `palette.secondary` |
| Neutrals | Black `#000000` + White `#FFFFFF` | `palette.neutral_dark` + `palette.neutral_light` |
| Typography (compliance line) | Inter, ~10–12 pt soft-grey or off-white sans-serif (verified:false — pending DevTools confirmation on live site) | `typography.trust_strip` / system designer note |
| Typography (review card body) | Card-standard body weight + size — readable at 100% zoom on Meta feed mobile | Path 2 spec |
| Photography mood | Warm Californian craft — natural daylight, warm cast, golden-hour preference, real people / real worksites / hands-on craftsmanship; NEVER showroom polish, AI-uncanny faces, luxury-mansion-only framing | `photography_mood` |
| Voice register | Warm, plainspoken, craftsman-direct — NOT polished marketing-agency. Voice anchor = customer testimonial cadence. | `voice` |
| Banned phrases (must not appear anywhere) | elevate, unlock, transform, leverage, premium experience, in the realm of, uncompromising, timeless design, precision-crafted, refined home solutions, today only, bare "lifetime warranty," starting from $X, generic "energy efficient" | `voice.forbidden_phrases` + Strategic Lever Round 1 banned list |
| Compliance line | `CSLB #537570 · Family-owned in Southern California since 1988.` | Project Instructions Compliance Locks |

---

## 5. Reference adherence

| Field | Value |
|---|---|
| REF used | REF-001 — `/SHARED/04_reference-library/REF-001/ref.png` (Banked 2026-04-26 from Meta Ad Library — Brothers Home Improvement testimonial-led layout) |
| Adherence target | 99% (CLONE MODE) |
| Self-score | 99% — no structural 1% flex used |
| Cloned elements (must match REF-001) | Layout (50/50 split installer-left + review-card-right); photo composition framing logic (subject walking-with-window-frame, partial three-quarter view, real-world residential — NOT posed studio); review-card right-half occupancy + top-right platform mark + top-left avatar + body text + reviewer attribution rhythm; star row above wordmark lockup; circular ribbon-seal anniversary badge in bottom-left corner; bottom-right wordmark lockup with subcategory line; absence of separately written headline / CTA / footer |
| Allowed asset swaps applied (NOT flex) | Installer person → Mike (V1, Path D) / anonymous installer (V2/V3); reviewer name "Tony Wallace" → "San Diego homeowner" (CDW Round 1 anonymization lock); review body → verbatim Zoran K. Google review (Path 2 rendered); platform mark → Google "G" retained; "30 YEARS" → "35 YEARS" (truthful tenure); "Brothers Home Improvement" → "California Doors & Windows"; Brothers green-and-white → CDW yellow + warm red + off-white + soft black |
| Documented 1% structural flex deviations | **NONE.** The clone is at 99% structural adherence with no permitted-flex deviations. Every deviation from REF-001 falls inside the CLONE MODE allowed-asset-swap budget, not the 1% structural-flex budget. |

---

## 6. Step-by-step generation instructions per variation

**Recommended primary generator: ChatGPT Image** (handles attached identity references for Path D and renders review cards with high typographic fidelity at 4:5 vertical scale).

### V1 — Mike portrait (Path D)

1. Open ChatGPT Image (or equivalent generator that accepts an attached identity reference).
2. **Attach** `/CLIENTS/California Doors and Windows/03_assets/photos/mike_founder.png` as the identity reference. Generator uses attached photo as facial-identity reference; JSON controls scene/composition.
3. **Paste** the JSON prompt from `/CLIENTS/California Doors and Windows/06_prompts/AD-A/V1.json` as the prompt body.
4. Generate at 1440 × 1800 (4:5 vertical Meta-native).
5. **Verify the rendered review card before accepting the output:** body text matches the verbatim Zoran K. spec (no paraphrasing, no "virtual" → "online" drift); reviewer name reads "San Diego homeowner" (NOT "Zoran K.", NOT an initial); avatar is a neutral generic circle with no letter; date reads "4 weeks ago"; Google G mark is in the top-right of the card; 5 yellow stars sit above the body; the visual focal-point sentence is the most readable focal point. If any field drifts, regenerate. **Path 2 verbatim accuracy lock applies.**
6. **Verify the bottom-right wordmark lockup zone is clean negative space** — uninterrupted exterior background, no placeholder box, no dashed outline, no white wordmark zone marker (CDW logo composited in Canva post-generation).
7. **Verify Mike's facial identity** matches the attached photo at acceptable likeness — no plastic AI skin, no warped fingers, no uncanny eye treatment. If identity drifts, regenerate.
8. Expected output filename: `AD-A_V1_AI_RAW.png` — save to `/CLIENTS/California Doors and Windows/07_generated/`.

### V2 — Anonymous installer (mid-install, AI-gen)

1. Open ChatGPT Image. **Do NOT attach** any reference photo (V2 is fully AI-gen, no Path D, no Mike likeness).
2. Paste the JSON prompt from `/CLIENTS/California Doors and Windows/06_prompts/AD-A/V2.json`.
3. Generate at 1440 × 1800.
4. **Verify the installer is anonymous** — back-view or three-quarter-back-view, NO recognizable face, NO Mike likeness, NO claim of depicting an actual install or named individual.
5. Verify the rendered review card matches V1 byte-identical (same Path 2 spec).
6. Verify the wordmark lockup zone is clean negative space (uninterrupted background, no placeholder box, no dashed outline, no white card).
7. Expected output filename: `AD-A_V2_AI_RAW.png` — save to `/CLIENTS/California Doors and Windows/07_generated/`.

### V3 — Anonymous installer (completion gesture, AI-gen)

1. Open ChatGPT Image. **Do NOT attach** any reference photo.
2. Paste the JSON prompt from `/CLIENTS/California Doors and Windows/06_prompts/AD-A/V3.json`.
3. Generate at 1440 × 1800.
4. **Verify the moment differs from V2** — V3 is a completion / step-back / final-shim moment with a finished window visible as outcome cue; V2 is a mid-install moment. If V3 reads as the same moment as V2, regenerate.
5. Verify the rendered review card matches V1 and V2 byte-identical.
6. Verify the wordmark lockup zone is clean negative space (uninterrupted background, no placeholder box, no dashed outline, no white card).
7. Expected output filename: `AD-A_V3_AI_RAW.png` — save to `/CLIENTS/California Doors and Windows/07_generated/`.

---

## 7. Step-by-step Canva composition instructions per variation

The same Canva composite is applied to V1, V2, and V3 — only the AI-generated background plate changes.

1. Open Canva at 1440 × 1800 (4:5 vertical).
2. Drop the AI-generated raw plate (`AD-A_V[1|2|3]_AI_RAW.png`) as a full-bleed background layer.
3. **CDW logo composite — bottom-right wordmark lockup zone:**
   - Asset: `/CLIENTS/California Doors and Windows/00_intake/brand_assets/CDW_logo.png` (raster — vector .svg/.ai/.eps requested for Round 2; usable at Round 1 prototype quality).
   - Place over the clean negative space the AI pass left in the bottom-right corner (no placeholder to erase first — the AI pass renders uninterrupted background here).
   - Two-line lockup rhythm — CDW logo on top, "Windows & Doors" subcategory line beneath, matching the REF-001 "Brothers Home Improvement / Windows & Doors" treatment.
   - Verify the 5-yellow-star row sits directly above the wordmark — adjust vertical placement only if the AI plate's star row is not centered above the lockup zone.
4. **Logo top-left zone:** NONE. REF-001 has no top-of-frame wordmark; the cloned creative inherits the restraint. Do NOT drop a logo into the top-left.
5. **Footer:** NONE. Standard Meta ad — no branded footer composite. Frame extends full-bleed to bottom edge.
6. **Compliance line:** the AI pass renders the compliance line at the bottom edge. Verify legibility at Meta feed mobile zoom (100%); if illegible, retype the line in Canva at ~10–12 pt soft-grey or off-white sans-serif over the AI plate's bottom edge.
7. Export as PNG at 1440 × 1800.
8. Expected final filenames:
   - `AD-A_V1_FINAL.png`
   - `AD-A_V2_FINAL.png`
   - `AD-A_V3_FINAL.png`
9. Save to `/CLIENTS/California Doors and Windows/08_final/`.

---

## 8. QA checklist (must pass before launch)

**Across V1/V2/V3 (locked-element identity):**

- [ ] Compliance fine print byte-identical across V1/V2/V3 — exact string `CSLB #537570 · Family-owned in Southern California since 1988.`
- [ ] Rendered review card byte-identical across V1/V2/V3 (display name "San Diego homeowner", neutral generic avatar, 5 stars, Google G mark, "4 weeks ago," verbatim Zoran K. body)
- [ ] Layout identical — left ~50% installer / right ~50% review card; circular 35 YEARS ribbon bottom-left; star row + wordmark zone bottom-right
- [ ] Brand system identical — same palette, same lighting, same camera setup, same compliance line, same wordmark lockup composite
- [ ] Hero subject differs across V1/V2/V3 — Mike portrait vs. mid-install anonymous installer vs. completion-gesture anonymous installer (and V2 ≠ V3 by clearly different moments, not noise)

**Real-photo authenticity & Path D (V1 specifically):**

- [ ] V1 was generated with `mike_founder.png` attached as the identity reference (Path D)
- [ ] V1 Mike likeness reads as recognizable to the attached photo — no plastic AI skin, no uncanny eyes, no warped fingers
- [ ] V2 and V3 do NOT show a recognizable face — anonymous back-view / three-quarter-back-view only
- [ ] V2 and V3 do NOT depict a recognizable address, neighborhood, or named individual

**Path 2 review card verbatim accuracy:**

- [ ] Review body is verbatim Zoran K. — no paraphrasing; "virtual" stays "virtual"; "press 1, press 4, press 8 maze" reads exactly
- [ ] Visual focal-point sentence (`When you call, a real person picks up and gets things handled. No 'press 1, press 4, press 8' maze.`) is the most readable focal point in the card
- [ ] Reviewer display name reads `San Diego homeowner` — NOT "Zoran K.", NOT "Z." with a period, NOT first-name-last-initial
- [ ] Profile avatar is a neutral generic circle with NO letter and NO initial; generic person silhouette acceptable
- [ ] Date stamp reads `4 weeks ago`
- [ ] No separate city subtitle line beneath the display name
- [ ] Platform mark is the Google "G" multicolor logo (NOT Houzz, NOT Yelp)

**Logo + wordmark quality:**

- [ ] CDW logo composited cleanly in the bottom-right wordmark lockup zone — no AI-generated logo trace, no "Brothers Home Improvement" residue
- [ ] "Windows & Doors" subcategory line sits beneath the CDW logo in the two-line lockup
- [ ] Wordmark zone in the AI pass was clean negative space — uninterrupted exterior background, no placeholder box, no dashed outline, no white wordmark zone marker, no auto-generated wordmark residue
- [ ] Top-left of frame has NO logo (REF-001 has none; clone inherits)

**Compliance line legibility:**

- [ ] Compliance line is legible at 100% Meta feed mobile zoom
- [ ] Compliance line carries CSLB #537570 + family-owned/since-1988 phrasing, no banned phrases, no 25C reference, no brand-dealer claim

**Anonymization compliance (CDW Round 1 lock):**

- [ ] No customer name or initial visible anywhere in the cloned creative
- [ ] Real source reviewer (Zoran Knezevic) name does NOT appear in the rendered card or in metadata
- [ ] Trust attribution reads `San Diego homeowner` only
- [ ] R-001 signed name "Clifferd R. Helwig" does NOT appear anywhere (BLOCKED — consent not collected)

**Banned phrase scan (manual read of every legible line in the AI plate + Canva composite):**

- [ ] `elevate`, `unlock`, `transform`, `leverage`, `premium experience`, `in the realm of`, `uncompromising`, `timeless design`, `precision-crafted`, `refined home solutions` — NONE present
- [ ] `today only`, bare `lifetime warranty`, `starting from $X`, generic `energy efficient` — NONE present
- [ ] No 25C / federal-tax-credit reference
- [ ] No brand-dealer claim (Milgard / Andersen / Anlin)

**Vague-terms disclaimer (Concept C only):** N/A — Concept A is not offer-led.

---

## 9. Hypothesis & test plan

**Predicted winner: V1 (Mike portrait, Path D).**

Burned-Once Bob's burn was a faceless virtual outfit; Zoran's review names exactly that pattern (`'press 1, press 4, press 8' maze`). Pairing the verbatim anti-virtual-outfit review with a real, named, verifiable founder closes the loop in a single frame: customer voice naming the chain phone-tree pattern, sitting next to the disconfirming evidence (Mike, the real person who picks up). V1 hits all three lead avatars — Bob (anti-virtual-outfit), Pat (founder she's heard of), Karen (craftsman aesthetic). Highest-fit-ratio variation in the slate.

**V2** is the disciplined process / proof-of-craft control — does the anonymous-installer-at-work image carry the same conversion lift as the founder portrait when paired with the same review? If V2 wins, the lever is the review (not Mike's face), and Round 2 can scale anonymous-installer creative with the same review card.

**V3** tests whether outcome / completion imagery converts better than process imagery — does the "job done" moment hit harder than the "job in progress" moment? If V3 outperforms V2, Round 2 should weight outcome / finished-install creative.

**Round 1 budget split recommendation (within Concept A):** lean V1 at ~50% of Concept A spend; V2 and V3 each at ~25%. Run all three in the same ad set. Read after 10–14 days.

---

## 10. Filenames for launch

| File | Path |
|---|---|
| Locked copy source | `/CLIENTS/California Doors and Windows/05_copy/AD-A_copy.md` |
| V1 JSON | `/CLIENTS/California Doors and Windows/06_prompts/AD-A/V1.json` |
| V2 JSON | `/CLIENTS/California Doors and Windows/06_prompts/AD-A/V2.json` |
| V3 JSON | `/CLIENTS/California Doors and Windows/06_prompts/AD-A/V3.json` |
| Variation notes | `/CLIENTS/California Doors and Windows/06_prompts/AD-A/variation_notes.md` |
| V1 Path D identity reference | `/CLIENTS/California Doors and Windows/03_assets/photos/mike_founder.png` |
| Reference cloned | `/SHARED/04_reference-library/REF-001/ref.png` |
| AI raw output — V1 | `/CLIENTS/California Doors and Windows/07_generated/AD-A_V1_AI_RAW.png` |
| AI raw output — V2 | `/CLIENTS/California Doors and Windows/07_generated/AD-A_V2_AI_RAW.png` |
| AI raw output — V3 | `/CLIENTS/California Doors and Windows/07_generated/AD-A_V3_AI_RAW.png` |
| Canva final — V1 | `/CLIENTS/California Doors and Windows/08_final/AD-A_V1_FINAL.png` |
| Canva final — V2 | `/CLIENTS/California Doors and Windows/08_final/AD-A_V2_FINAL.png` |
| Canva final — V3 | `/CLIENTS/California Doors and Windows/08_final/AD-A_V3_FINAL.png` |

---

Saved to `/CLIENTS/California Doors and Windows/06_prompts/AD-A/PRODUCTION_BRIEF.md`. Next: AD-B PRODUCTION_BRIEF.md.
