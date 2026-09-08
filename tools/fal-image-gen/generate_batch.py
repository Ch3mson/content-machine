#!/usr/bin/env python3
"""Generate a batch of 10 dorm mirror selfie stills (5 Asian, 5 White) with Fal Seedream 5.0 Pro.
Also builds a labeled contact sheet grid for quick review.
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TEXT_MODEL = "bytedance/seedream/v5/pro/text-to-image"
OUT_DIR = PROJECT_ROOT / "tools" / "fal-image-gen" / "out" / "batch_crying_girls"


def load_dotenv_value(name: str) -> str | None:
    env_path = PROJECT_ROOT / ".env"
    if not env_path.exists():
        return None
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip() == name:
            return value.strip().strip('"').strip("'")
    return None


def get_api_key() -> str:
    api_key = os.environ.get("FAL_KEY") or load_dotenv_value("FAL_KEY")
    if not api_key:
        raise SystemExit("Missing FAL_KEY. Set it in the repo .env file.")
    return api_key


PROMPT_SPECS = [
    # 5 Asian Girls
    {
        "id": "asian_01",
        "title": "Asian 1 - Navy Crewneck / Classic Dorm",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a college dorm room. "
            "A 20-year-old East Asian college student girl with a dark brown shoulder-length bob haircut and wispy curtain bangs "
            "is lying on her stomach on an unmade dorm bed, propped up on her elbows facing directly into a bedroom mirror. "
            "She holds a black smartphone pointed into the mirror to take the photo, with the back of the phone and camera lenses clearly visible in the reflection. "
            "Her face is oriented toward the camera/mirror, but her eyes look slightly downward and to the side, gazing away from the camera lens with a quiet, defeated, sad expression. "
            "Natural melancholy with subtle glistening moist eyes, but calm and relatable without bloodshot eyes, without swollen red eyelids, and without extreme redness. "
            "Wearing an oversized navy blue university crewneck sweatshirt. "
            "Dorm room background with a white waffle-weave duvet, wooden desk with laptop in the background, and soft warm string lights. "
            "Amateur smartphone snapshot aesthetic, relatable TikTok UGC style. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
    {
        "id": "asian_02",
        "title": "Asian 2 - Cream Zip-Up / Chin in Hand",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a college dorm room. "
            "A 21-year-old East Asian college girl with long wavy black hair loosely gathered in a tortoiseshell claw clip with face-framing strands "
            "is lying on her stomach on her dorm bed, propping her chin thoughtfully in one palm, facing toward the bedroom mirror. "
            "With her other hand she holds a dark smartphone taking the mirror photo, phone camera visible in the reflection. "
            "Her face is turned toward the mirror, but her eyes look pensively off to the side, lost in sad contemplation. "
            "Gently sad, vulnerable and overwhelmed, subtle sheen on eyes, but natural clear eyes without heavy swelling or red bloodshot circles. "
            "Wearing a cozy cream ribbed knit zip-up hoodie over a simple white tee. "
            "Warm lived-in dorm room with an olive green comforter, cork bulletin board with polaroids on the wall, warm amber bedside lamp. "
            "Authentic handheld TikTok snapshot aesthetic. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
    {
        "id": "asian_03",
        "title": "Asian 3 - Oatmeal Hoodie / Subtle Glasses",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a university dorm room. "
            "A 19-year-old East Asian student girl with straight dark hair in a low messy ponytail and delicate thin metal wire glasses "
            "is lying on her stomach on her twin-XL dorm bed, propped up on her forearms facing a full-length mirror. "
            "She holds an iPhone in front of her taking the mirror selfie, the phone chassis visible in reflection. "
            "Her face is facing the mirror/camera, but her gaze is cast downward toward her bedsheets with a tired, heartbroken, deflated look. "
            "Understated authentic sadness, subtle moisture in eyes, but clean natural eyes without swollen bloodshot redness. "
            "Wearing an oversized heather oatmeal slouchy fleece hoodie. "
            "Dorm room background with blue plaid flannel bedsheets, textbooks stacked on the floor, soft daylight from a window mixed with desk lamp. "
            "Raw candid smartphone camera quality. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
    {
        "id": "asian_04",
        "title": "Asian 4 - Charcoal Graphic Tee / Lob",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a college dorm room. "
            "A 22-year-old East Asian young woman with a medium brown dyed lob haircut and natural soft features "
            "is lying on her stomach on a dorm bed, propped up on her elbows facing directly into a mirror. "
            "She holds a silver iPhone in one hand pointed at the mirror reflection. "
            "Her face is positioned toward the camera/mirror, but she stares slightly off-camera with a quiet numb sadness, subtle downturned mouth and soft melancholy eyes. "
            "Realistic sad expression, subtle glisten on lower lash, but calm and natural without heavy puffy swelling or bloodshot eyes. "
            "Wearing an oversized washed vintage charcoal grey t-shirt. "
            "Modern college dorm backdrop with burnt-orange terracotta bed throw, metal frame, nightstand with water bottle and study notes. "
            "Unfiltered relatable TikTok UGC aesthetic. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
    {
        "id": "asian_05",
        "title": "Asian 5 - Forest Green Fleece / Shag Cut",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a dorm bedroom. "
            "A 20-year-old East Asian girl with a dark layered wolf cut / textured shag haircut "
            "is lying on her stomach on a bed, propped up on her left elbow facing toward the mirror. "
            "She holds a black smartphone in her right hand aimed into the mirror, phone clearly visible in reflection. "
            "Her face is turned toward the mirror, but her gaze drops downward and slightly away with an emotionally vulnerable, somber look, biting her lip slightly. "
            "Relatable quiet heartbreak, subtle glossy eyes, but clear natural skin around eyes without heavy crying redness or puffy bloodshot veins. "
            "Wearing an oversized slouchy forest green quarter-zip fleece pullover. "
            "Dorm room setting with painted cinderblock wall, floral quilt, soft bedside lamp giving a gentle ambient glow. "
            "Candid authentic mobile photo aesthetic. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },

    # 5 White Girls
    {
        "id": "white_01",
        "title": "White 1 - Grey Hoodie / Messy Bun",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a college dorm room. "
            "A 20-year-old Caucasian college student girl with dirty blonde hair swept into a messy high bun with loose strands framing her face "
            "is lying on her stomach on an unmade dorm bed, propped up on her elbows facing a full-length mirror. "
            "She holds a black iPhone pointed into the mirror to take the photo, phone back and cameras clearly reflected. "
            "Her face faces the mirror/camera, but her eyes look slightly down and away from the camera lens with a somber, overwhelmed expression. "
            "Quiet emotional exhaustion, subtle glisten in eyes, but natural clear eyes without heavy redness, no bloodshot veins, and no extreme puffiness. "
            "Wearing an oversized light heather grey hooded sweatshirt with drawstring. "
            "Dorm room background with an unmade beige linen duvet, white cinderblock wall with small art postcards, warm bedside reading lamp. "
            "Casual amateur smartphone snapshot aesthetic, relatable TikTok UGC style. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
    {
        "id": "white_02",
        "title": "White 2 - Burgundy Crewneck / Long Brunette",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a dorm bedroom. "
            "A 21-year-old Caucasian girl with long straight brunette hair parted down the middle falling over her shoulders "
            "is lying on her stomach on a dorm bed, resting her cheek in the palm of one hand, facing directly toward the mirror. "
            "With her other hand she holds a dark smartphone in front of her chest taking the mirror selfie, phone visible in reflection. "
            "Her face is directed toward the mirror, but her eyes gaze off into the distance past the camera with a defeated, sad, contemplative look. "
            "Vulnerable and heartbroken, soft tearful sheen, but natural eyes without swollen bloodshot redness or extreme crying irritation. "
            "Wearing a vintage faded burgundy college crewneck sweatshirt. "
            "Lived-in dorm background with striped blue and white bedsheets, desk with an open textbook and coffee mug in soft focus. "
            "Authentic handheld social media photo quality. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
    {
        "id": "white_03",
        "title": "White 3 - Sage Waffle Knit / Light Freckles",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a university dorm room. "
            "A 19-year-old Caucasian student girl with wavy honey-light brown hair and subtle light freckles across her nose "
            "is lying on her stomach on a twin bed, propped up on both forearms facing the bedroom mirror. "
            "She holds an iPhone in her hand pointing directly into the mirror reflection. "
            "Her face is pointed toward the mirror, but she looks downward toward her hands with a pensive, disappointed, sad expression. "
            "Subtle quiet sadness, slight moisture in eyes, but clean natural eyes without swollen eyelids or bloodshot red marks. "
            "Wearing a cozy slouchy sage green waffle-knit long-sleeve sweater. "
            "Autumn dorm setting with a warm tan quilt, wooden nightstand with small alarm clock and desk lamp glowing warmly. "
            "Raw candid smartphone camera snapshot aesthetic. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
    {
        "id": "white_04",
        "title": "White 4 - Black Zip-Up / Wavy Dark Brunette",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a college dorm. "
            "A 22-year-old Caucasian young woman with dark wavy brunette hair tucked casually behind one ear "
            "is lying on her stomach on her dorm bed, propped up on her elbows facing toward a mirror. "
            "She holds a silver smartphone vertically in hand taking the mirror selfie, phone reflection clearly visible. "
            "Her face faces the mirror/camera, but her eyes stare pensively off-axis, with a melancholy, overwhelmed, vulnerable gaze. "
            "Emotional vulnerability and quiet sadness, subtle moisture on lower eyelashes, but natural clear eyes without puffy red rings or heavy swelling. "
            "Wearing a slouchy black zip-up hoodie over a heather grey t-shirt. "
            "Dorm room background with grey jersey knit sheets, a wooden loft bed post visible, small string fairy lights on the wall. "
            "Relatable unfiltered TikTok UGC aesthetic. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
    {
        "id": "white_05",
        "title": "White 5 - Baby Blue Crewneck / Honey Blonde",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a collegiate dorm bedroom. "
            "A 20-year-old Caucasian girl with shoulder-length warm honey-blonde wavy hair "
            "is lying on her stomach on her dorm bed, propped up on one elbow with chin resting lightly near her wrist, facing the mirror. "
            "She holds a dark smartphone in her hand aimed into the mirror, phone camera lenses reflected. "
            "Her face is oriented toward the camera/mirror, but she looks slightly away and down with a wistful, tearful, sad look. "
            "Understated relatable sadness, glassy eyes, but clean and natural without extreme bloodshot redness or severe swollen eyes. "
            "Wearing an oversized pastel baby-blue vintage fleece crewneck sweatshirt. "
            "Classic dorm room background with a muted patterned paisley comforter, bulletin board with sticky notes in background, warm table lamp glow. "
            "Authentic handheld amateur mobile photo aesthetic. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
    },
]


def generate_single_image(spec: dict, api_key: str) -> Path:
    img_id = spec["id"]
    out_path = OUT_DIR / f"{img_id}.jpg"
    if out_path.exists() and out_path.stat().st_size > 10000:
        print(f"[{img_id}] Already exists: {out_path}")
        return out_path

    print(f"[{img_id}] Generating: {spec['title']}...")
    payload = {
        "prompt": spec["prompt"],
        "image_size": {"width": 1080, "height": 1920},
        "num_images": 1,
        "output_format": "jpeg",
        "enable_safety_checker": True,
    }

    request = urllib.request.Request(
        f"https://fal.run/{TEXT_MODEL}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Key {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    start_t = time.time()
    try:
        with urllib.request.urlopen(request, timeout=240) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"[{img_id}] Fal request failed ({exc.code}): {detail}") from exc

    images = body.get("images") or []
    if not images or not images[0].get("url"):
        raise RuntimeError(f"[{img_id}] No image URL in Fal response: {body}")

    image_url = images[0]["url"]
    with urllib.request.urlopen(image_url, timeout=120) as image_response:
        out_path.write_bytes(image_response.read())

    dur = time.time() - start_t
    print(f"[{img_id}] Saved in {dur:.1f}s -> {out_path}")
    return out_path


def build_contact_sheet(image_paths: list[tuple[str, str, Path]]) -> Path:
    """Build a 2-row x 5-column contact sheet grid."""
    print("Building contact sheet...")
    # 2 rows, 5 cols: Row 1 = Asian 1-5, Row 2 = White 1-5
    thumb_w = 400
    thumb_h = int(thumb_w * 1920 / 1080)  # ~711
    pad = 20
    header_h = 60
    label_h = 50

    total_w = pad + 5 * (thumb_w + pad)
    total_h = header_h + pad + 2 * (thumb_h + label_h + pad)

    sheet = Image.new("RGB", (total_w, total_h), color=(24, 24, 27))
    draw = ImageDraw.Draw(sheet)

    # Header
    draw.text((pad, 18), "Dorm Mirror Selfies — 5 Asian & 5 White (Seedream 5.0 Pro)", fill=(255, 255, 255))

    for idx, (img_id, title, path) in enumerate(image_paths):
        row = 0 if idx < 5 else 1
        col = idx % 5

        x = pad + col * (thumb_w + pad)
        y = header_h + pad + row * (thumb_h + label_h + pad)

        try:
            with Image.open(path) as img:
                thumb = img.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
                sheet.paste(thumb, (x, y))
        except Exception as e:
            print(f"Error loading {path} for contact sheet: {e}")
            draw.rectangle([x, y, x + thumb_w, y + thumb_h], fill=(50, 50, 50))

        # Label box
        draw.rectangle([x, y + thumb_h, x + thumb_w, y + thumb_h + label_h], fill=(35, 35, 40))
        draw.text((x + 10, y + thumb_h + 10), title, fill=(240, 240, 240))
        draw.text((x + 10, y + thumb_h + 28), img_id, fill=(160, 160, 160))

    contact_sheet_path = OUT_DIR / "contact_sheet.jpg"
    sheet.save(contact_sheet_path, "JPEG", quality=90)
    print(f"Contact sheet saved -> {contact_sheet_path}")
    return contact_sheet_path


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    api_key = get_api_key()

    print(f"Starting generation of {len(PROMPT_SPECS)} images using max_workers=3...")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future_to_spec = {
            executor.submit(generate_single_image, spec, api_key): spec
            for spec in PROMPT_SPECS
        }
        for future in concurrent.futures.as_completed(future_to_spec):
            spec = future_to_spec[future]
            try:
                out_path = future.result()
                results[spec["id"]] = (spec["id"], spec["title"], out_path)
            except Exception as exc:
                print(f"FAILED {spec['id']}: {exc}", file=sys.stderr)

    # Build sorted list
    image_paths = []
    for spec in PROMPT_SPECS:
        if spec["id"] in results:
            image_paths.append(results[spec["id"]])

    if len(image_paths) == len(PROMPT_SPECS):
        build_contact_sheet(image_paths)
    else:
        print(f"Only generated {len(image_paths)}/{len(PROMPT_SPECS)}, skipping contact sheet.")


if __name__ == "__main__":
    main()
