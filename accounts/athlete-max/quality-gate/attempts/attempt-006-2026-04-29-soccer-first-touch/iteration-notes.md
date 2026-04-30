# Quality Gate Iteration Notes

## Iteration 1 (Attempt 006)

- Date: 2026-04-29
- Account: `athlete-max`
- Workflow: A3 writing/design quality gate
- Slide type: non-hero body slide
- Sport: soccer
- Topic: why your first touch fades in the final 20 minutes of a match
- Status: rendered, pending user review
- Trigger: user criticism of attempt-005 for photo not feeling centered and missing the listing format label.

## User Feedback From Attempt 005

- Raw criticism: "make sure that the reference photo is more centered. If it is like a listing format like verified_byhumans post 1, then there should be a simple label like what to avoid: as can be seen in the reference post."
- Classification: Account-Native Scroller / Design feedback
- Key insight: verified_byhumans Post 1 uses a listing format with:
  1. Label: "what to avoid:" (small regular)
  2. Title: short topic name (large bold, e.g., "mouth breathing while distracted")
  3. Explanation
  4. Photo (centered)
  5. Fix
  6. Source

## Changes Applied For Attempt 006

- **Added label:** "what to avoid:" at 30px regular, positioned above the title.
- **Shortened title:** "late-game touch" at 56px bold (2 words, like verified_byhumans's short topic titles).
- **Contrarian hook embedded:** "your late-game touch is not a conditioning problem" now lives in the first line of the explanation.
- **Photo frame:** Positioned at y=444 with **80px equal spacing** above and below. Frame is horizontally centered (x=140, width=800, equal 140px margins).
- **Structure matches Post 1:** Label → Title → Explanation → Photo → Fix → Source.

## Pre-Review Fit Fixes (Render 2 & 3)

### Spacing Fix (Render 2)
- **Issue:** Attempt 006 initial render had unequal spacing — 125px above frame vs 14px below.
- **Fix:** Recalculated for equal 80px gaps. Frame moved to y=444. Lower section starts at y=974.
- **Result:** Equal 80px spacing above and below photo frame.

### Label Congruence Fix (Render 3)
- **Issue:** User noted "what to avoid:" + "late-game touch" does not make grammatical sense.
- **Fix:** Title changed from "late-game touch" to "losing your late-game touch" — the title now IS the thing to avoid, matching verified_byhumans Post 1 format (e.g., "what to avoid: mouth breathing while distracted").

### Bold Label-Only Fix (Render 3)
- **Issue:** User noted bolding the entire first line of the fix section was wrong — only structural labels should be bold.
- **Fix:** Bold reduced to `the fix:` and `constraint:` only. All content words ("10 minutes", "wall passes", "one-timed", etc.) are now regular weight.
- **Result:** Bold count = 2 terms (the fix:, constraint:), within design.md 3-5 max.

## Structural Comparison

| Element | Attempt 005 | Attempt 006 (Post 1 Style) |
|---|---|---|
| Label | None | "what to avoid:" (30px regular) |
| Title | "late-game touch (motor cortex)" (60px) | "late-game touch" (56px) |
| Title length | 4 words + parenthetical | 2 words, short and punchy |
| Format | Topic-only title | Listing format label + title |
| Photo spacing | Unequal (150px/14px) | Equal (80px/80px) |
| Reference | Post 5 (topic as title) | Post 1 (listing format) |

## Approval

- **Approved:** 2026-04-29
- **User decision:** Approved. Quality gate passed for writing.md and design.md.
- **Locked files updated:** `writing.md` status → Locked, `design.md` status → Locked.
- **Next step:** Workflow A4 (Angle Extraction to Presets) or Workflow B (New Post).
