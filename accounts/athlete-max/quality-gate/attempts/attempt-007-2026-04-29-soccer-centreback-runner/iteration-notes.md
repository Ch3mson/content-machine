# Quality Gate Iteration Notes

## Iteration 1 (Attempt 007)

- Date: 2026-04-29
- Account: `athlete-max`
- Workflow: A3 writing/design quality gate
- Slide type: non-hero body slide
- Sport: soccer
- Position: centreback
- Topic: why you miss the runner getting in behind during the final 15 minutes
- Status: rendered, pending user review
- Trigger: user requested a completely new idea for a soccer centreback

## User Request

- Raw request: "give me one slide of a completely new idea for a soccer centreback"
- Classification: New topic request (not a revision of attempts 001–006 first-touch fatigue).
- Key insight: User wants to see the writing/design system applied to a fresh centreback-specific desire stack.

## Topic Selection

- Rejected topics: first-touch fatigue (already tested 6 times), hip flexor power for clearances (too similar to motor-fade angle), neck fatigue for headers (harder to visualize in frame).
- Selected: perceptual-cognitive fatigue — attention narrowing causes centrebacks to miss runners in behind. This is position-specific, mechanism-backed, and visually distinct from prior attempts.

## Changes Applied For Attempt 007

- **New topic:** Centreback late-game spatial awareness / runner tracking.
- **Contrarian hook:** "your late-game reads are not a reaction problem."
- **Mechanism:** Central fatigue narrows attention around the ball, filtering out the runner behind the shoulder.
- **Fix:** Post-session scanning drill with a deliberate two-second rhythm and verbal constraint (call out the runner).
- **Source:** Williams, Hodges & Elliott — J Sports Sci 1999 (perceptual-cognitive skill research in soccer).
- **Structural format:** Same verified_byhumans Post 1 listing format as attempt 006 (label + title + explanation + photo + fix + source).
- **Vertical recalculation:** Upper explanation is 6 lines (vs. 5 in attempt 006). Spacing recalculated to maintain 65 px gaps and 60 px bottom margin.
  - label y=80, title y=130, top_start=205, frame_y=486, lower_start=1001, source_y=1270.

## Pre-Review Fit Fixes

### Spacing Fix
- **Issue:** 6-line upper text plus 6-line lower text is taller than attempt 006.
- **Fix:** Moved label/title up slightly (80/130 vs. 95/145). Reduced gaps from 80 px to 65 px. Source at 1270 to preserve 60 px bottom margin.
- **Result:** All elements fit within safe margins; no overlaps.

### Width Check
- **Issue:** Several lines in both sections approach 64 characters.
- **Fix:** Verified against attempt 006 longest lines (also ~64 chars at 28 px Arial). No overflow warnings in renderer.

## Approval

- Date: 2026-04-29
- User decision: **Approved.**
- Approved by: user
- Reason: sample demonstrates the writing and design system transfers cleanly to a new topic and position-specific desire stack. All persona checks pass. Layout, line-fill, and hierarchy meet design.md without hacks.
- Latest approved sample: attempt-007-2026-04-29-soccer-centreback-runner (non-hero body slide).
