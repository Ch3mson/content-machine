# Sample Brief

## Slide Choice

- Slide type: Full 12-slide arc
- Athlete: Muhammad Ali (Cassius Clay) vs. Sonny Liston, 1964
- Why this works for A3: it tests the full account writing system end-to-end — pressure hook, identity rehearsal, misinterpretation, payoff, emotional identity reveal, product bridge, and quote closer. It also tests 12 consecutive renders through the same design pipeline.

## Arc Structure

| Slides | Role | What It Tests |
|--------|------|---------------|
| 1-2 | Threat setup | Fact-led opening, establishing stakes without throat-clearing |
| 3-4 | Antics + strategy | Show behavior, then reveal the strategy behind it |
| 5-6 | The strange night | Suspense-building, sensory detail, pacing |
| 7-8 | Misinterpretation vs. truth | Suspense maintains through a two-slide reveal |
| 9 | Payoff | The round hits — concrete proof the chanting mattered |
| 10 | Identity reveal | Emotional peak — the "mental turn" slide showing identity rehearsal |
| 11 | Product bridge | w(inner) as native continuation of the athlete's method |
| 12 | Quote closer | Athlete's own words restate the post's mental idea |

## Copy Goals

- Prove the writing system can produce more than flat fact lists
- Show that each slide creates a reason for the next
- Build the reader through: threat → pressure → confusion → insight → payoff → emotional peak → product → closure
- Keep each slide to one proof beat, 4-5 lines max

## Design Goals

- Render 12 full-bleed B&W photos with paper overlay
- Centered white Arial Bold text with black outline at 36pt
- Preserve manual line breaks from `sample-copy.md` exactly
- Verify readability across 12 different photo types

## Source Images

The render script reads Ali photos from `accounts/athlete-stories/Muhammad Ali/sourced/` and uses `product/assets/phone-holding/9x16-boxing-02.jpeg` for Slide 11. Every non-product slide is mapped to a distinct source image.

The script also runs a local upscale/sharpen pass before the crop and B&W treatment so the low-resolution archival images hold up better at `1080x1920`.

| Slide | Suggested image subject |
|-------|------------------------|
| 1 | Liston, menacing pose or fight stare | `liston_portrait.png` |
| 2 | Young Cassius Clay, pre-fight | `ali_young.png` |
| 3 | Weigh-in face-off, Clay shouting | `ali_liston_weighin.jpg` |
| 4 | Newspaper or odds context | `slide_7.jpg` |
| 5 | Night/lawn confrontation context | `ali_fight_1.jpg` |
| 6 | Clay shouting / predicting the future | `ali_liston_fight.jpg` |
| 7 | Reporters, press conference, or crowd | `slide_12.jpg` |
| 8 | Clay composed, sitting or training alone | `slide_8.jpg` |
| 9 | Liston on stool, Clay celebrating | `slide_9.jpg`, fallback `ali_liston_fight.jpg` |
| 10 | Ali triumphant, iconic pose | `slide_10.jpg`, fallback `ali_fight_1.jpg` |
| 11 | Native boxing phone-in-hand product image | `product/assets/phone-holding/9x16-boxing-02.jpeg` |
| 12 | Ali mid-speech, quote moment | `ali_portrait.jpg` |

## Claim Safety

- The sample uses broad public sports-history claims — Liston's record, the 1964 fight, weigh-in behavior — all well-documented.
- No medical, therapy, performance guarantee, scholarship, contract, or victory claims.
- Product claims use approved `product/claim-bank.md` wording: "personalized visualization tracks."
- "Rewired my brain" in Slide 11 passes the Athlete Skeptic because it's first-person narration using a common expression, not a clinical claim about a third party.
