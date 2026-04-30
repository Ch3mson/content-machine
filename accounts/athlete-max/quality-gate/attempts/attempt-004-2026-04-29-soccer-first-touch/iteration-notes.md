# Quality Gate Iteration Notes

## Iteration 1 (Attempt 004)

- Date: 2026-04-29
- Account: `athlete-max`
- Workflow: A3 writing/design quality gate
- Slide type: non-hero body slide
- Sport: soccer
- Topic: why your first touch fades in the final 20 minutes of a match
- Status: rendered, pending user review
- Trigger: user criticism of attempt-003 for text going off screen, reference photo overlapping text, and overall spacing needing massive improvement.

## User Feedback From Attempt 003

- Raw criticism: "the text is going off screen, the reference photo is overlapping, and the overall spacing needs massive improvement"
- Classification: Design feedback
- Root causes identified:
  1. Title at 48px bold with 9-word lines exceeded canvas width (1081px > 936px safe width).
  2. Top explanation at 30px with 7 lines overflowed vertically into the photo frame (y=527 vs frame at y=515).
  3. Lower section at 30px with combined bold+regular segments in one line created 1372px wide text.
  4. Insufficient vertical buffers between text blocks and frame/source.

## Changes Applied For Attempt 004

- **Title:** Reduced from 48px to 40px bold. Split into 3 lines instead of 2 to keep each line under 936px. Word count per line: 7, 8, 9.
- **Body text:** Reduced from 30px to 28px regular. This is the lower bound of design.md's 28-34px body range but necessary to fit 9-11 word lines within width.
- **Top explanation:** Reduced from 7 lines to 5 lines. Ends at y=482, providing 33px buffer above frame at y=515.
- **Lower section:** Split combined bold+regular segment into separate lines. 7 lines total. Ends at y=1241, providing 39px buffer above source line at y=1280.
- **Width checking:** Renderer now prints warnings if any line exceeds 936px safe width.
- **Vertical spacing:** Label at y=92, title at y=138, top explanation starts after 20px gap, lower section starts 24px after frame, source at y=1280.

## Open Issues

- Title word count (7-9 words) does not meet the strict 9-word minimum because 9 words at 40px bold exceeds canvas width with average English word length. If the 9-word minimum is absolute for titles, title font must drop to 32px or below, which may feel too small for hierarchy.
- Body at 28px is at the bottom of design.md's 28-34px range. If approved, design.md should document 28px as the validated minimum for dense body slides.

## Approval

- Latest approved sample: none yet.
- User decision: pending.
