# Quality Gate Iteration Notes

## Iteration 3 (Isolated Run)

- Date: 2026-04-28
- Account: `athlete-max`
- Workflow: A3 writing/design quality gate, isolated session
- Slide type: non-hero body slide
- Sport: soccer (user-selected)
- Topic: why your first touch fades in the final 20 minutes of a match
- Reader avatar: competitive soccer player who trains hard but loses first-touch precision late in matches and blames tired legs
- Style choices tested: lowercase section labels, two-line bold contrarian title, bold inline `the fix:` and `the payoff:`, no red accent on body slide
- Product mention: none
- Image handling: placeholder frame only
- Status: rendered, pending user review

## Extraction Summary Tested

- Writing must make the athlete care within 2 seconds, then translate the mechanism into a tangible match moment.
- One reader carries the whole slide; the desire stack is "keep clean possession late, when the defender expects you to lose it."
- Mechanism precedes protocol: CNS dialing precision down → in-fatigue first-touch drilling.
- Strong biological claims must be sourced, softened, or marked for verification.
- Design must keep the fixed `800x450` body image frame at `x=140`, `y=515` and solve fit through copy and line breaks, not layout hacks.

## Three-Persona Critique Before Render

### Persona 1: The Bored Athlete

- Blocking failures: none.
- Non-blocking improvements: original title ("blaming your legs for a sloppy late-game touch") was longer and read more like a lesson than a contrarian reframe.
- Rewrite action applied: tightened to two short lines: `your late-game touch / is not a leg problem`. Contrarian shape preserved; instant value sharper.

### Persona 2: The Account-Native Scroller

- Blocking failures: none.
- Non-blocking improvements: original lower section was a single block; risked weak swipe rhythm.
- Rewrite action applied: split lower section into a `the fix:` paragraph and a separated `the payoff:` paragraph so the in-match moment lands as its own beat — matches verified_byhumans Post 1 cadence.

### Persona 3: The Athlete Skeptic

- Blocking failures on terminology: none after rewrites.
- Rewrite actions applied:
  - "motor plan" → "the signal from your brain to your foot" (lab-leaning → coach-plausible).
  - "protective dampening" → "dialing down precision to protect you from total exhaustion" (AI-polished → observable).
- Source: real foundational soccer-fatigue paper (Mohr, Krustrup & Bangsbo, *J Sports Sci* 2003). PMID lookup flagged for `sources.md` before final use. Sample passes the gate; final posts must verify.
- w(inner) mention: none. Product placement deferred per camouflage rule.

## Flagged Sport Terms

| Term | Confidence | Decision |
| --- | --- | --- |
| first touch | Native | Keep |
| late-game | Native | Keep |
| minute 70 / minute 80 | Native | Keep |
| repeat sprints (implicit) | Native | Keep |
| nervous system | Acceptable | Keep |
| central fatigue (avoided in copy) | Too niche | Replaced with plain language |

## Review Checklist

- [ ] Slide reads like an athlete-max post, not a generic sports-science deck.
- [ ] Title carries instant value without a hero opener doing the work first.
- [ ] Mechanism is accessible; no jargon leak.
- [ ] `the fix:` bold-label transition reads cleanly under the photo frame.
- [ ] Placeholder frame has the correct visual priority (centered, not background, not decorative).
- [ ] Source line is legible but secondary.
- [ ] Typography hierarchy holds at realistic copy density.

## Render Audit Finding (Surfaced By Iteration 3)

- The first render (Iteration 3a) overflowed the photo frame at the top and the source line at the bottom.
- Copy was tightened (top from 6 lines to 5; lower from 8 lines to 6) per the workflow rule "shorten copy or adjust line breaks; do not shrink text or move the frame." The second render (Iteration 3b) is clean.
- Real audit finding for `design.md`: at the upper end of the typography ranges (label 32, title 60, body 30, source 20), the body-slide vertical budget allows roughly 5 lines of top explanation and 6 lines of lower section before colliding with the fixed frame or source line. Recommend either:
  - tightening the typography ranges (e.g., body 28-30 not 28-34), or
  - documenting an explicit per-slide line budget in `design.md` so future copy is drafted to fit, or
  - allowing minor frame y-position flex (currently locked at y=515) only when source line is omitted.
- This finding does not block approval of the current sample. It should be folded into `design.md` after the user approves the gate.

## User Review Feedback

- Date: 2026-04-29
- Criticism: "each line should have a minimum of 9 words. this needs to be consistent throughout as it does not make sense for one line to have 9 words and another line to only have 3. Make sure you edit this for the bottom and top part as well."
- Classification: Account-Native Scroller / Design feedback
- Impact: Blocking failure on visual consistency and swipe rhythm. Short lines (3-8 words) break the dense, substantive feel of the reference accounts and create an unprofessional, sparse layout.
- Affected lines:
  - Label: "what to avoid:" (3 words)
  - Title line 1: "your late-game touch" (3 words)
  - Title line 2: "is not a leg problem" (5 words)
  - Top line 2: "your touch lands" (3 words) + bold phrase
  - Top line 3: "than it did in the first half." (8 words)
  - Top line 4: "your nervous system is dialing precision down" (8 words)
  - Top line 5: "to protect you from total exhaustion." (7 words)
  - Fix line 1: "the fix: drill 6-8 first touches into a" (8 words)
  - Fix line 2: "shoebox-sized target in the last 15 minutes" (8 words)
  - Fix line 3: "of training, when your legs are gone." (8 words)
  - Payoff line 3: "you to lose it." (4 words)
- Rewrite action: Combine or expand every rendered line to a minimum of 9 words. Apply to label, title, top explanation, lower fix/payoff, and source line.
- Durable rule needed: yes — add to `design.md` as a line-consistency rule.

## Approval

- Latest approved sample: none yet.
- User decision: rejected — line length consistency.

## Prior Iteration Notes

- Iteration 1 and Iteration 2 (hydration / repeat-sprint slides) superseded by this isolated run on user instruction.
