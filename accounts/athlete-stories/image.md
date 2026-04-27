# Image Rules: Athlete Stories Account

## Design System

- **Layout**: Full-bleed photo, centered text.
- **Aspect Ratio**: 9:16 (1080x1920). All images normalized before any other processing.
- **Text**: White, centered, bold sans-serif. Black outline for readability.
- **Color Treatment**: All photos converted to black and white with high contrast, then paper overlay applied.
- **Typography**: Arial Bold at 36pt. No decorative fonts.
- **Spacing**: Text centered vertically and horizontally. 140px margin on left and right edges.
- **Line breaks**: Respect manual line breaks from `flow.md` exactly. Do not auto-wrap.
- **Consistency**: Same font size, same text treatment, same B&W filter, same paper overlay across all slides.

## Pipeline Order

The processing pipeline must run in this exact order. Do not skip or reorder steps.

1. **Normalize to 9:16** — Crop and resize every image to 1080x1920.
2. **Convert to B&W** — Grayscale + 1.3x contrast enhancement.
3. **Apply paper overlay** — Vintage paper texture with warm sepia grain, darker grain spots, and vignette edges.
4. **Add text overlay** — Centered white text with black outline.

## Text Overlay Rules

- **Font**: Arial Bold, 36pt.
- **Color**: White (#FFFFFF).
- **Outline**: Black stroke, 3px width.
- **Alignment**: Centered horizontally and vertically.
- **Line spacing**: 16px between lines.
- **Side margin**: 140px on left and right. Text must not touch the edges.
- **Line breaks**: Respect manual line breaks from `flow.md`. Do not auto-wrap based on pixel width.

## Paper Overlay Rules

- Apply the same paper overlay to all slides in a slideshow for consistency.
- Warm sepia grain: random pixels with R 180-220, G 160-195, B 130-160, alpha 15-35.
- Darker grain spots: small clusters of R 100-150, G 80-130, B 60-100, alpha 10-30.
- Vignette: dark edges that increase in opacity toward corners. Max alpha 120.
- The overlay must be subtle enough to not obscure faces or text, but visible enough to create a vintage feel.

## B&W Conversion Rules

- Convert all images to grayscale.
- Increase contrast by 1.3x to make text pop.
- Ensure faces and key details remain clear after conversion.
- Apply the same contrast setting to all images in a slideshow for consistency.

## 9:16 Normalization Rules

- Target resolution: 1080x1920 pixels.
- Crop from center. Never stretch or distort the image.
- If the source image is wider than 9:16, crop the sides to fit.
- If the source image is taller than 9:16, crop the top and bottom to fit.
- If the source image is narrower than 9:16, pad with black bars on the sides. Do not stretch.

## Product Slide Treatment

- The product slide uses a native phone-in-hand photo.
- Keep the B&W and paper overlay treatment for consistency.
- Text overlay follows the same centered style.
- No additional branding or logos on the image.
- Product mention is woven into the copy, not the design.

## Slide Role Mapping

Each slideshow follows this role structure. The specific athlete photos change per post, but the roles stay the same.

| Slide | Role | Image Direction | Copy Rhythm |
|-------|------|-----------------|-------------|
| 1 | The Beginning | Athlete in struggle/origin context | Short. Staccato. 2-5 words per sentence. |
| 2 | The Grind | Athlete training/working | Medium. 8-14 words. Building context. |
| 3 | The Weight | Athlete under pressure/isolated | Medium. Tension rising. |
| 4 | The Peak | Athlete meditating/visualizing/focused | Longest. 15-25 words. The visualization reveal. |
| 5 | The Transformation | Athlete triumphant/unleashed | Medium. The payoff. |
| 6 | The Product | Phone in hand on court/field | Short. Grounded product mention. |
| 7 | The Legend | Athlete iconic moment | Athlete quote. |