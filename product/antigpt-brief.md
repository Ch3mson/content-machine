# AntiGPT (antigpt.me) Product Brief

This is the product source of truth for antigpt.me. Account playbooks must read
this file before making product mentions, product claims, or product-adjacent
content choices.

## Status

- Last updated: 2026-09-05
- Product name: AntiGPT
- Product category: AI text humanizer + AI detector + original-draft writer
- URL: https://www.antigpt.me
- Instagram: https://www.instagram.com/antigpt.me/
- Contact: hello@antigpt.me
- Codebase: `~/dev/Humanizer` (Next.js 15, Supabase, Stripe, OpenAI)
- Current priority: run the antigpt Instagram account (TikTok second) as
  single stills of the locked avatar plus one first-person study line, with
  AntiGPT only in the CTA line
- Pricing model: subscription (monthly and annual), word-based credits
- Not to be confused with: `antigpt.app` (a different company with a LinkedIn
  and Product Hunt presence). Never cite its posts, stats, or handles.

## Product One-Liner

AntiGPT rewrites AI-generated text so it sounds human and bypasses AI detectors
like Turnitin and GPTZero.

## Positioning

Site headline: "LESS AI. MORE YOU." / "Make AI Writing Sound Human."

Site subline: "Made to preserve what's human. AntiGPT humanizes writing from
Claude, ChatGPT, Gemini, and more so every word sounds natural and bypasses AI
detectors."

- AntiGPT is not a paraphraser or synonym swapper (the blog explicitly
  positions it against QuillBot-style tools).
- AntiGPT is a humanizer: it restructures sentences, varies vocabulary, and
  adjusts patterns that detectors flag (burstiness, perplexity, unnatural
  phrasing).
- The brand leans student-first: "Trusted by students around the world",
  "Loved by students worldwide", Back to School sale, university logo carousel
  (Harvard, MIT, Stanford, Yale, Princeton, Columbia, UPenn, Berkeley, Duke,
  UMich, Waterloo).
- Secondary audiences named on the site and in onboarding: marketers (SEO and
  engagement), businesses (emails that feel personal), professionals (reports,
  proposals, client communication), freelancers, founders.
- Tone of the product itself: clean, confident, slightly playful ("Less AI.
  More you."). Not edgy, not guru.

## Primary Users

| User segment | Pain | Desired outcome | Product value prop | Risky claim to avoid |
| --- | --- | --- | --- | --- |
| High school and college students | Essays drafted with ChatGPT/Claude get flagged by Turnitin or GPTZero; writing sounds robotic; false positives on their own writing. | Submit work that reads like them and passes detectors. | Paste, pick a writing level (high school / college / PhD), humanize, verify with the built-in checker. | Promising a specific grade or "never flagged ever". |
| Grad students and researchers | Long documents, dissertations, and literature reviews drafted with AI. | Natural academic prose that clears institutional checks. | Higher word allowances; PhD writing level; free checker to verify. | Claiming it fabricates or verifies citations. |
| Marketers and content teams | AI blog drafts read as AI and underperform on engagement and SEO. | Human-sounding content at volume. | Bulk word allowances; keeps meaning while changing detector-flagged patterns. | Guaranteeing rankings or traffic. |
| Professionals and job seekers | AI-assisted resumes, cover letters, emails, and reports sound stiff. | Communication that sounds personal and credible. | "One last pass before a recruiter reads it" (newsletter sponsor copy). | Guaranteeing job or client outcomes. |

## Core Product Flow

1. Paste AI-generated text (or upload .txt / .pdf).
2. Choose output language and writing level: `standard`, `highschool`,
   `college`, or `phd`. Optional `stealth` boost for more aggressive
   restructuring.
3. Humanize. Processing typically takes seconds to a couple of minutes
   depending on length.
4. Check the result with the built-in AI checker (returns a 0-100 human-written
   probability). Up to 500 words can be checked free without a subscription.

Additional tool: Stealth Writer generates original drafts from a prompt with a
`purpose` (essay, article, story, report) and `tone` (formal, casual, creative,
academic).

## Features (from codebase and site)

- AI Humanizer with four writing levels plus stealth boost.
- AI Checker (free up to 500 words, no login; larger allowances on paid plans).
- Stealth Writer for original drafts.
- Bypass claims on the pricing page: "Bypass all AI detectors (GPTZero,
  Originality.ai, Copyleaks, & more)".
- "Removes Claude hidden watermarks" (pricing page feature line).
- Detectors named on the site: Turnitin, GPTZero, ZeroGPT, Copyleaks,
  Originality.ai, QuillBot, Grammarly.
- Site claim: rewriting engine trained on over 1.2 million samples of academic
  writing, essays, and AI-generated text; tested against detectors and updated
  weekly.
- Privacy: content processed securely and deleted after processing; not used
  for training (site FAQ).
- Login: Google sign-in only.
- Creator program ("Earn with AntiGPT"): pays creators for TikTok, Instagram,
  and YouTube videos about AntiGPT via PayPal, ACH, Revolut. No payout cap.

## Pricing (as of 2026-09-05)

| Plan | Monthly | Annual (per month) | Annual total | Humanizer words / mo | Stealth Writer words / mo | AI Checker words / mo |
| --- | --- | --- | --- | --- | --- | --- |
| Basic | $9.99 (list $13.99) | $4.99 | $59.99 | 10,000 | 10,000 | 30,000 |
| Pro (Most Popular) | $19.99 (list $26.99) | $9.99 | $119.99 | 50,000 | 50,000 | 150,000 |
| Unlimited | $49.99 (list $68.99) | $24.99 | $299.99 | 500,000 | 500,000 | 1,500,000 |

- Trial: first-time customers get a 100-word free trial with a card on file.
  The trial ends after 100 words or 1 day, whichever comes first, then the
  chosen plan is charged. Cancel anytime from billing settings.
- Free AI checker: up to 500 words without a subscription.
- Current promo on site: "Back to School Sale! Save up to 45%! Offer ends
  September 30."
- Pricing changes often; re-check `src/components/pricing/pricing-section.tsx`
  and `src/lib/stripe-plans.ts` before quoting numbers in copy.

## Functional Claims

Factual product capabilities from the site and code.

- Humanizes text from ChatGPT, Claude, Gemini, and other AI models.
- Rewrites to bypass AI detectors including Turnitin, GPTZero, Copyleaks,
  ZeroGPT, and Originality.ai.
- Offers high school, college, and PhD writing levels.
- Includes a free AI checker (500 words) with no account required.
- Keeps the original meaning while changing detector-flagged patterns.
- Processes most documents in under two minutes.
- Deletes content after processing; does not train on user text.
- Plans start at $4.99/month on annual billing.
- Cancel anytime.

## Social Proof On Site (verify before reuse)

- "Trusted by 1,000,000+ Writers Worldwide" (homepage value prop).
- "Loved by 250,000+ students" (image alt text in value props).
- Comparison graphic: "ChatGPT 99% detection rate vs AntiGPT 1% detection rate".
- Testimonial carousel with named students at MIT, Stanford, Harvard, Wharton,
  Yale, Berkeley, Johns Hopkins, Columbia, Princeton, Caltech.

These numbers conflict with each other (1M writers vs 250K students) and the
testimonials are marketing copy. Do not put them on slides until the user
confirms which figures are real.

## Brand Assets

| Asset | Location | Notes |
| --- | --- | --- |
| Logo | `~/dev/Humanizer/public/logo.svg` | Primary mark |
| Mascot / illustration | `~/dev/Humanizer/public/AntiGPTWoman.png` | 512x512, used on Earn page |
| Landing page screenshots | `~/dev/Humanizer/public/AntiGPT landing page 1-4.png` | Product UI proof for last-slide CTA |
| Detector logos | `~/dev/Humanizer/public/detectors/` | Turnitin, GPTZero, Copyleaks, Originality, ZeroGPT |
| University logos | `~/dev/Humanizer/public/schools/` | Use carefully; implies endorsement |
| Demo videos | `~/dev/Humanizer/public/videos/sound_human.mp4`, `check_authenticity.mp4` | Screen captures of the product |

Brand colors and fonts are not yet recorded here. Pull from
`~/dev/Humanizer/src/styles/` if the on-image CTA ever needs brand styling. The
overlay font today is TikTok Sans (`accounts/antigpt/assets/fonts/`).

## Product Mention Rules For Stills

- AntiGPT appears only in the CTA: the post caption, or a short final on-image
  line under the hook line. Never in the hook line itself.
- The hook line must work on its own as a relatable student moment.
- The CTA names AntiGPT, says what it does (humanizes AI essays, bypasses
  Turnitin and AI detectors), and points to antigpt.me.
- Approved wording lives in `antigpt-claim-bank.md`.
