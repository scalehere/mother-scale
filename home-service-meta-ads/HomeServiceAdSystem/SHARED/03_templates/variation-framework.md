# Variation Framework — How the 3 Variations Differ

This is the rulebook Agent 9 (Brand Translator) follows when producing 3 JSON variations per concept.

**The locked rule: 3 variations of a concept share ~90% structural DNA with the reference image and differ on ONE axis only — Hero Photo Subject.**

This rule exists because A/B test data is only readable when one variable changes between variations. If copy varies AND photo varies AND layout varies across your 3 variations, the data tells you nothing — you can't isolate which lever drove the win.

---

## What stays LOCKED across V1, V2, V3

These elements are 100% identical across all three variations of a concept:

- All copy from `AD-XXX_copy.md`:
  - Headline (exact words, punctuation, line breaks)
  - Sub-headline (if used)
  - Trust-strip line
  - CTA line
- Brand color palette (every HEX code)
- Typography (every font, every weight, every size)
- Layout (zone proportions, alignments, hierarchies)
- Reference structural DNA (~90% adherence to REF-XXX)
- 4-zone Meta-vertical canvas (1440 × 1800)
- Trust strip composition and placement
- CTA bar composition and placement
- Logo zone (always Canva-composited, never AI)
- Footer (none for standard ads; Canva-composited for flyer mode)

If any of these change across variations, the test is broken.

---

## What VARIES across V1, V2, V3 — Hero Photo Subject ONLY

The Zone 2 photo subject is the single variable.

### Standard subject menu (default for home-service contractors)

| Variation | Hero Subject | What it tests |
|---|---|---|
| **V1** | Founder / installer portrait | Does the brand's human authority drive conversion? |
| **V2** | Install in progress / behind-the-scenes | Does proof-of-craft drive conversion? |
| **V3** | Finished install + happy customer (or before/after pair) | Does outcome / social proof drive conversion? |

This menu is the default. The user can override the 3 subjects per concept if the concept demands different ones — for example, an offer concept might use:
- V1: Offer artifact (e.g. quote sheet, invoice with savings highlighted)
- V2: Founder holding offer artifact
- V3: Customer's reaction to receiving offer

In every case, the subjects must be **genuinely distinct categories** — three founder portraits at slightly different angles is NOT 3 variations. That's noise, not signal.

---

## The 90% reference adherence rule

Each variation mirrors the reference image's structure at ~90%. The 10% flexibility is for brand-fit improvements only:

**Allowed deviations (10% flex):**
- Swap reference's typography for client's locked brand typography
- Swap reference's palette for client's locked brand palette
- Adjust trust-strip wording length to match client's actual review/credential text
- Adjust headline word-count if client's locked copy is slightly longer/shorter than reference's
- Adjust photo crop slightly to fit client's actual photo asset

**Forbidden deviations:**
- Changing layout structure (don't move zones around)
- Changing reading order or hierarchy
- Changing which element gets visual emphasis (e.g. don't make the headline smaller than the reference made it)
- Adding zones the reference doesn't have
- Removing zones the reference does have

If you find yourself deviating beyond 10%, you're picking the wrong reference for this concept. Send the user back to hunt a better one.

---

## Naming convention

```
/CLIENTS/[CLIENT NAME]/06_prompts/AD-XXX/
├── V1.json    ← founder subject (or first agreed subject)
├── V2.json    ← install-in-progress subject (or second agreed subject)
├── V3.json    ← finished-install subject (or third agreed subject)
├── variation_notes.md  ← what's locked, what varies, hypothesis, adherence score
└── PRODUCTION_BRIEF.md ← Agent 10 output: single doc the user works from
```

---

## What to do with the test results

After 10–14 days of round-one testing:

**One variation wins clearly (>30% better cost-per-result):**
1. Lock the winner. Kill V2 and V3.
2. Push budget to the winner.
3. Generate 3 NEW concepts (different reference, different angle) for the next round. Don't iterate this concept further unless the win was marginal.

**No clear winner:**
- The hero subject isn't the bottleneck. The concept may not be the lever — return to Agent 6.
- Or the audience may be wrong — adjust targeting before changing creative.

**All three fail (kill criteria triggered):**
- Concept failed at the strategic level, not the visual level.
- Pull the next-strongest concept off the stress-test list.

---

## Why this discipline matters

Most contractor Meta accounts run "creative variation" that's actually noise — different copy, different photo, different layout across each "test." The data is uninterpretable.

The single-axis Hero Subject rule + 90% reference adherence is what makes the test scientifically valid. Combined with the reference library (a compounding bank of proven references) and the stress test (which kills weak concepts before generation), this is what separates a repeatable creative system from one-off ad production.

You will know within 14 days which photo subject converts. That insight compounds across every future client in the same vertical.
