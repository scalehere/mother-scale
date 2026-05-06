# CONCEPT-A — Variation Notes (CLONE MODE · REF-001 clone)

**Concept:** CONCEPT-A — Mike's Hands-On 35 Years
**Mode:** CLONE MODE — 99% structural adherence to REF-001 (Brothers Home Improvement testimonial-led layout)
**Reference cloned:** REF-001 — `/SHARED/04_reference-library/REF-001/ref.png`
**Copy source:** `/CLIENTS/California Doors and Windows/05_copy/AD-A_copy.md`
**Approvals consulted:** `/CLIENTS/California Doors and Windows/00_intake/path_d_approval.md` (Path D + CLONE MODE)
**Author:** Agent 9 — Brand Translator
**Date:** 2026-04-26

---

## What's locked across V1 / V2 / V3 (everything except hero photo subject)

- **Layout:** left ~50% installer-in-action photo · right ~50% rendered Google review card overlay. Identical zone proportions, identical alignment, identical cropping logic across all three.
- **Headline / sub / trust strip / CTA:** NONE on the cloned creative — REF-001 has none, the clone inherits the restraint. The rendered review card serves as the headline-and-trust area.
- **Compliance fine print:** byte-identical V1 / V2 / V3 — `CSLB #537570 · Family-owned in Southern California since 1988.`
- **Review card content (Path 2 rendered):** byte-identical V1 / V2 / V3.
  - Display name: `San Diego homeowner`
  - Date: `4 weeks ago`
  - Stars: 5 yellow
  - Platform: Google `G` logo top-right
  - Avatar: neutral generic circle, NO letter
  - Body text: VERBATIM Zoran K. Google review per Path 2 spec
  - Visual focal-point sentence: `When you call, a real person picks up and gets things handled. No 'press 1, press 4, press 8' maze.`
- **35 YEARS anniversary ribbon-seal:** identical CDW-yellow circular ribbon, bottom-left corner, ~280–320px diameter, with `CALIFORNIA DOORS & WINDOWS · SINCE 1988` outer-ring sub-arc copy.
- **5-yellow-star row above logo lockup:** identical placement and treatment.
- **Bottom-right wordmark lockup zone:** EMPTY in the AI pass; identical Canva-composite call across V1 / V2 / V3 (CDW logo + `Windows & Doors` subcategory line).
- **Brand palette:** CDW sun-yellow `#FFC72C` + warm red `#C8102E` + off-white + soft black per `/CLIENTS/California Doors and Windows/00_intake/brand_assets/CDW_design_system.json`.
- **Lighting / time of day / camera setup:** identical across all three (50mm equivalent · f/4 · eye level slightly off-axis · late-morning Californian daylight ~5200K · warm cast).
- **Footer policy:** NONE — full-bleed bottom edge.

## What varies V1 / V2 / V3 — hero photo subject only

| Variation | Hero subject | Path | Image input required |
|---|---|---|---|
| **V1** | **Mike Marohnic founder** in install context (workwear + tool belt, walking with or holding a window frame in residential exterior). Identity supplied by attached `mike_founder.png` per Path D. | **Path D** (AI-gen scene + real-photo identity reference) | YES — `mike_founder.png` |
| **V2** | **Anonymous installer back-view** seating / fastening a window into an existing exterior opening. NO face. | Pure AI-gen, generic process | NO |
| **V3** | **Anonymous installer in completion gesture** (final shim / sealant pass / step-back inspection / hands-dusted). Finished window visible at install point as outcome cue. NO face. Pose / moment subtly different from V2. | Pure AI-gen, generic outcome | NO |

This menu corresponds to the standard variation framework: V1 founder authority · V2 install-in-progress (proof of craft) · V3 finished install (outcome / social proof). Per the locked variation rule, hero photo subject is the ONLY variable that changes.

## Reference adherence self-score

- **Target:** 99% (CLONE MODE)
- **Self-score:** 99%
- **Cloned elements (must match REF-001):** layout (50/50 split), photo composition framing logic, review-card placement and full right-half occupancy, review-card top mark + star row + body + attribution rhythm, star row above logo lockup, anniversary-badge shape and bottom-left corner placement, brand-logo lockup style and bottom-right placement, typography hierarchy (review-text-as-hero), absence of headline/CTA/footer.
- **Allowed asset swaps applied (not flex):** installer person → Mike (V1) / anonymous (V2/V3); reviewer name `Tony Wallace` → `San Diego homeowner` (CDW anonymization lock); review body → verbatim Zoran K.; platform mark → Google `G` retained; `30 YEARS` → `35 YEARS`; `Brothers Home Improvement` → `California Doors & Windows`; Brothers green-and-white → CDW yellow + red + off-white + soft black.

## Documented 1% structural flex deviations

**None.** Concept A clones REF-001 at 99% with no permitted-flex deviations. All differences from REF-001 are allowed asset swaps under the CLONE MODE workflow (see `clone_mode_swap_log` block in each JSON), not structural flex.

## Path D / Path 2 / Path 1 execution paths used per variation

| Variation | Path D (AI-gen founder likeness w/ real-photo reference) | Path 2 (rendered review card) | Path 1 (review-screenshot attachment) |
|---|---|---|---|
| **V1** | YES — Mike portrait | YES — verbatim Zoran K. card | NO |
| **V2** | NO — anonymous installer | YES — verbatim Zoran K. card (IDENTICAL TO V1) | NO |
| **V3** | NO — anonymous installer | YES — verbatim Zoran K. card (IDENTICAL TO V1/V2) | NO |

## Hypothesis — which variation predicted to win in market and why

**Predicted winner: V1 (Mike portrait, Path D).**

Burned-Once Bob's burn was a faceless, virtual outfit — Zoran's review names exactly that pattern (`'press 1, press 4, press 8' maze`). Pairing the verbatim anti-virtual-outfit review with a real, named, verifiable founder closes the loop in a single frame: a customer's literal voice naming the chain phone-tree pattern, sitting next to the disconfirming evidence (Mike, the real person who picks up). V1 hits all three lead avatars — Burned-Once Bob (anti-virtual-outfit), Pacific Beach Pat (founder she's heard of), Coronado Karen (craftsman aesthetic). It's the highest-fit-ratio variation in the slate.

**V2** is the disciplined process / proof-of-craft control — does the "anonymous installer at work" image carry the same conversion lift as the founder portrait when paired with the same review? If V2 wins, the lever is the review (not Mike's face), and Round 2 can scale-out anonymous-installer creative with the same review card.

**V3** tests whether outcome / completion imagery converts better than process imagery — does the "job done" moment hit harder than the "job in progress" moment? If V3 outperforms V2, Round 2 should weight outcome / finished-install creative.

Spend prediction: lean V1 first; confirm against V2 and V3 in the same ad set after 10–14 days of read.

## Assets the user must attach at generation time (per variation)

### V1 (Path D)
1. **`mike_founder.png`** — `/CLIENTS/California Doors and Windows/03_assets/photos/mike_founder.png`. Path D identity reference. Generator uses attached photo as identity reference; JSON describes scene/composition only.
2. **CDW logo** — for Canva post-pass composite into the bottom-right wordmark lockup zone (Agent 9 does NOT generate logos).

### V2
1. NO real-photo attachment. Pure AI-gen anonymous installer.
2. **CDW logo** — for Canva post-pass composite (same placement as V1).

### V3
1. NO real-photo attachment. Pure AI-gen anonymous installer + finished window.
2. **CDW logo** — for Canva post-pass composite (same placement as V1/V2).

### Universal (all variations)
- **No review screenshot required.** Concept A uses Path 2 — the rendered Google review card is generated as part of the AI pass per the verbatim Zoran K. spec carried in each JSON's `review_card.spec` block.

## Compliance check — passed before save

- ✅ CSLB `#537570` appears in compliance fine print on V1 / V2 / V3.
- ✅ Banned phrases (`elevate`, `transform`, `unlock`, `leverage`, `premium experience`, `in the realm of`, `uncompromising`, `timeless design`, `precision-crafted`, `refined home solutions`, `today only`, bare `lifetime warranty`, `starting from $X`, generic `energy efficient`) — NONE present.
- ✅ No 25C / federal-tax-credit references.
- ✅ No brand-dealer claims (no Milgard / Andersen / Anlin name attached).
- ✅ Anonymization lock honored — review-card display name reads `San Diego homeowner`, avatar is a neutral generic circle with NO letter or initial. Real source reviewer on file is Zoran Knezevic; the displayed attribution does NOT carry his name, initials, or any identifying detail.
- ✅ Locked copy across V1 / V2 / V3 is byte-identical (compliance fine print + review card spec).
- ✅ CLONE MODE approval and Path D approval verified in `/CLIENTS/California Doors and Windows/00_intake/path_d_approval.md`.
- ✅ Path 2 verbatim accuracy lock — review body and reviewer details are EXACT per spec; if generation drifts, regenerate.

Saved to `/CLIENTS/California Doors and Windows/06_prompts/AD-A/`. Next: generate in ChatGPT Image (V1 with `mike_founder.png` attached as identity reference), composite logo in Canva post-pass.
