# Iteration Notes

## Pre-Render Persona Critique

Each persona reviewed the full 12-slide flow before render.

### Persona 1: The Bored Athlete

**Pass criteria met:**
- Slide 1 makes the value clear within 3 seconds. Opens on Liston's concrete threat — mob ties, prison record, 124-second knockout. The reader immediately knows this is about something real.
- The hook leads with an athlete-specific fact, not generic motivation.
- The mental edge (identity rehearsal, visualization) feels earned by Slide 10 because the reader has watched the strange behavior, seen it misinterpreted, and witnessed the payoff.

**Blocking failures: none.**

**Non-blocking notes:**
- Slide 4 ("But that was the game...") could feel like backfill psychology. But the preceding setup (weigh-in antics) earns the explanation, and the payoff (Slide 9) validates it. Keep it.
- Slide 10 is the longest slide (6 lines). At 36pt centered this is near the density limit. If the render shows it's crowded, consider splitting into two slides. Leaving as-is for the sample to test the limit.

**Rewrite actions before render: none.**

### Persona 2: The Account-Native Scroller

**Pass criteria met:**
- The flow is a clear descendant of @legendperform compact fact rhythm (Slides 1-2, 7-9) and @asdicipline pressure/suspense (Slides 3-6), adapted into account-native voice.
- Each slide creates a reason to continue. Slide 3 (antics) → Slide 4 (why). Slide 5-6 (strange behavior) → Slide 7-8 (what it means). Slide 9 (payoff) → Slide 10 (identity reveal).
- Sentence flow reads smoothly aloud. Short staccato in pressure slides, slightly longer in the reveal slides.
- Density per slide: 2-5 lines. Slide 10 pushes to 6, flagged as a design-density risk but not a writing failure.

**Blocking failures: none.**

**Non-blocking notes:**
- The "I" in Slide 11 switches to first-person narrator. This is correct per `writing.md` product-bridge rules, but the voice shift is abrupt. It should land as a deliberate move — the reader has been hearing a narrator's voice all along; Slide 11 is that narrator stepping into frame.
- Slide 8 ("He was planting the future...") is short but carries the entire thematic hinge. The reader needs a pause here — the shortness works in its favor.

**Slippery-slope verification (each slide makes the next feel necessary):**
- Slide 1 (monster) → Slide 2: who would fight this man?
- Slide 2 (22yo underdog) → Slide 3: what did he do about it?
- Slide 3 (antics) → Slide 4: was he crazy or smart?
- Slide 4 (strategy) → Slide 5: what else did he do?
- Slide 5 (2 AM) → Slide 6: what exactly did he do?
- Slide 6 (chant) → Slide 7: what did people think?
- Slide 7 (breakdown theory) → Slide 8: what was it really?
- Slide 8 (planting future) → Slide 9: did it work?
- Slide 9 (payoff) → Slide 10: what does this mean about him?
- Slide 10 (identity) → Slide 11: how do I use this?
- Slide 11 (bridge) → Slide 12: what did Ali say?

**Rewrite actions before render: none.**

### Persona 3: The Athlete Skeptic

**Flagged-term scan:**

| Term | Slide | Verdict | Notes |
|------|-------|---------|-------|
| "Mob ties" | 1 | Acceptable | Broad public-knowledge claim about Liston's known associations. Common sports-history knowledge. |
| "Prison record" | 1 | Acceptable | Public record — Liston served time for armed robbery. |
| "124 seconds" | 1 | Native | Public fight record — Liston vs. Patterson I, first-round KO at 2:06. |
| "Jordan Rules" | — | N/A | Not used in this flow. Was flagged in attempt-001. |
| "Floyd Patterson" | 1 | Native | Well-known former champion. |
| "The odds said" | 2 | Acceptable | Broad reference. The actual odds were 7-1 Liston; if we want to be precise, state the number. Leaving as-is for the sample. |
| "Muhammad Ali" | 10 | Native | Born Cassius Clay, changed name after the Liston fight. Slide 10's phrasing "Before Clay was Muhammad Ali" is historically accurate and emotionally correct. |
| "Round seven" | 6, 9 | Native | Liston did not answer the bell for round 7. Public fight record. |
| "Rewired my brain" | 11 | Acceptable | First-person common expression. Not a clinical claim. Flagged in prior quality-gate feedback as acceptable when used as first-person narration. |
| "Visualization tracks" | 11 | Acceptable | Approved `product/claim-bank.md` wording. |

**Blocking failures: none.**

**Non-blocking notes:**
- Slide 2 mentions "the odds" without a number. For final post, consider specifying "7-1" for precision. Acceptable for the quality gate.
- The product claim in Slide 11 uses approved direction: "personalized visualization tracks." No performance guarantee, no medical claim, no claim that w(inner) made Ali great.

**Rewrite actions before render: none.**

### Persona Consensus

All three personas pass the flow. No blocking failures. Two non-blocking notes for the render:
1. Slide 10 is 6 lines — at 36pt centered, this may push the visual density limit. The persona team agreed to test it in the sample render before deciding on a split.
2. The voice shift to first-person on Slide 11 is correct per account rules but should be evaluated by the designer during render review.

## Render Notes

- Pre-review fit fixes: none required.
- Script: `render_sample.py` — processes distinct Ali images from `accounts/athlete-stories/Muhammad Ali/sourced/` and uses `product/assets/phone-holding/9x16-boxing-02.jpeg` for Slide 11.
- Font: Arial Bold 36pt from `C:/Windows/Fonts/arialbd.ttf`.
- All slides use the same paper overlay seed (`5032026`) for visual consistency.
- Render depends on the mapped Ali source images and the Slide 11 product phone image.
- 2026-05-02 revision: replaced repeated fallback images with a one-image-per-slide source map. Added a local Lanczos upscale plus UnsharpMask sharpening pass before the 9:16 crop and B&W treatment.
- 2026-05-02 render verification: `slide_1.png` through `slide_12.png` regenerated at `1080x1920`.
- 2026-05-02 fit fix: Slide 6 had one long line leaking past the safe margin. Split `A 22-year-old screaming like he was predicting the future` into two manual lines and regenerated the deck.
- 2026-05-02 copy fit fix: Added quotation marks around Slide 6's repeated `Round seven` chant to make clear those are Clay's spoken words, then regenerated the deck.

## Designer Review

PENDING — user will source images and run the render script.

## User Feedback

PENDING — awaiting user approval after render.

## Revision Decisions

PENDING — will be recorded after user feedback round.
