# CDW Approvals — Path D + CLONE MODE

**Status:** Path D APPROVED for CDW Round 1 (2026-04-26) · CLONE MODE APPROVED for CDW Round 1 (2026-04-26)
**Approved by:** System designer

---

## Blocks to append to project instructions (CDW addendum)

Paste BOTH blocks below verbatim at the bottom of the **California Doors and Windows addendum** in the Cowork project instructions (Project Settings → Project Instructions → CDW addendum). They are independent — Path D governs founder-likeness AI generation; CLONE MODE governs reference adherence and the variation framework. Agent 9 reads both at runtime.

### Path D approval (paste into Cowork project instructions)

```
Path D approval (CDW-specific)
This client is approved for Path D: AI-generated founder likeness with real-photo reference. Agent 9 will write V1 JSON assuming the user attaches mike_founder.png at image-generation time. JSON describes scene/composition; attached photo provides identity. The system designer accepts the legal and Meta-policy exposure for this approach for CDW Round 1.
```

### CLONE MODE approval (paste into Cowork project instructions)

```
CLONE MODE approval (CDW Round 1)
This client is approved for CLONE MODE: 99% reference adherence with 1% flex for tiny brand-fit improvements. Agent 9 produces JSONs that clone each REF's layout, hierarchy, typography, badge placement, headline structure, and visual treatment. Only brand-specific assets swap (logo, hero subject, brand colors, numbers, review content, business identity). The system designer accepts that this is a rebranding-engine workflow, not original creative direction.
```

---

## Why this file exists

Project instructions live in the Cowork app's project settings, not in this workspace folder. This file is the canonical, version-controlled record of the Path D approval so future agents (and future system designers) can verify the approval and its scope without depending on the Cowork UI state.

If the Cowork project instructions are ever rebuilt, regenerated, or transferred, paste the block above back into the CDW addendum.

## Path D scope (operational reminder)

- Applies to CDW Round 1 only.
- Applies to **V1 founder hero only**. V2 and V3 are AI-generated generic process/finished imagery — never claim they depict actual installs or named individuals.
- Real photo asset for V1 reference attachment: `/CLIENTS/California Doors and Windows/03_assets/photos/mike_founder.png`
- Agent 9 writes V1 JSON with `reference_photo_attachment_required: true` and `reference_photo_path: [path to mike_founder.png]`. Hero photo prompt describes scene/composition, NOT facial features.
- This approval does NOT extend to other clients. Path D requires explicit per-client opt-in by the system designer.

## CLONE MODE scope (operational reminder)

- Applies to CDW Round 1 only.
- Applies to **all three Round 1 concepts** (Concept A / B / C). Each concept clones its matched REF at 99%:
  - CONCEPT-A clones REF-001 (Brothers Home Improvement testimonial-led layout).
  - CONCEPT-B clones REF-002 (BEFORE/AFTER 40% off layout).
  - CONCEPT-C clones REF-003 (Milele Motors giant-number 10% layout).
- 1% flex permitted ONLY for tiny brand-fit improvements (e.g., a 1–2 word headline length adjustment, an accent-color shift of a few percent). Anything beyond is a CLONE MODE violation — flag and escalate.
- Allowed asset swaps (per CLONE MODE workflow in Agent 9): logo, hero photo person, hero photo asset, brand colors, number treatments, review/testimonial content, phone/business name/city/address.
- NOT allowed to swap: layout structure, photo composition logic, typography hierarchy, trust badge placement, headline copy STRUCTURE (rhythm + line count + direct-response energy must match), CTA placement.
- CLONE MODE does NOT override compliance locks. CSLB #537570, vague-terms disclaimer (Concept C), anonymization of testimonials, no-25C, no banned phrases, no unverified brand-dealer claims — all CDW locks remain in force regardless of what the cloned REF contains.
- This approval does NOT extend to other clients. CLONE MODE requires explicit per-client opt-in by the system designer.

## Action required (system designer)

Both approval blocks above must be pasted into the Cowork project instructions UI for them to be active in future chats. Cowork project instructions are configured via Project Settings → Project Instructions; this workspace file is the canonical record but does NOT auto-sync. After pasting, verify the addendum contains both `Path D approval (CDW-specific)` and `CLONE MODE approval (CDW Round 1)` as separate paragraph blocks.
