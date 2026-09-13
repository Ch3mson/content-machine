#!/usr/bin/env python3
"""Face-swap the locked avatar onto composition boards with Fal Seedream edit.

Figure 1 = accounts/{account}/avatar/asian-girl-avatar.jpg (identity lock).
Figure 2 = each board you pass (file, folder, or glob).

Batch mode writes one still per board (plus a contact sheet) into
accounts/{account}/outputs/{stamp}/ so you can pick keepers. --post N writes a
single board's result straight to accounts/{account}/posts/N/image.jpg.

Examples:
  python tools/fal/swap_avatar.py accounts/antigpt/boards
  python tools/fal/swap_avatar.py accounts/antigpt/boards/study-selfie-03.jpg --post 3
  python tools/fal/swap_avatar.py "accounts/antigpt/boards/study-*.jpg" --variants 2 --scene "golden hour window light"
"""

from __future__ import annotations

import argparse
import concurrent.futures
import glob
import sys
from datetime import datetime
from pathlib import Path

from _client import (
    PROJECT_ROOT,
    SEEDREAM_EDIT,
    FalError,
    download,
    file_to_data_uri,
    first_image_url,
    get_api_key,
    list_images,
    parse_size,
    resolve_repo_path,
    run_sync,
)

DEFAULT_ACCOUNT = "antigpt"
DEFAULT_SIZE = "1080x1440"

IDENTITY_LOCK = (
    "Figure 1 is our Asian girl avatar. Keep her EXACT identity: the same unique face (same eyes, "
    "nose, mouth, jawline, and skin tone), and the same silver hoop earrings. Do not change her "
    "identity, age, or ethnicity. Do not keep Figure 2's face. Hair must be HER hair from Figure "
    "1: long dark wavy messy hair with the loose side part and face-framing layers. If the pose "
    "needs hair up, put that same hair in a bun — same dark color and wavy texture, not a sleek "
    "different-person bun and not Figure 2's hair."
)
COMPOSITION = (
    "Figure 2 is the composition board. Replace the person in Figure 2 with the Figure 1 girl. "
    "Match Figure 2's camera angle, framing, crop, pose, body position, outfit, lighting, and "
    "setting exactly. Preserve the exact torso lean, shoulder angles, arms, fingers, hand-to-face "
    "contact, and leg placement. Keep glasses, hats, headphones, held objects, and face occlusions "
    "in the same positions. Do not rotate, recenter, zoom, or reveal hidden parts of her face. "
    "Keep every other element of the Figure 2 scene unchanged."
)
EXPRESSION = (
    "Keep Figure 2's exact facial expression, gaze, and head angle. If she is looking down "
    "at a screen or page, keep that. Match eyelid openness, brow position, mouth shape, smile, "
    "and lip tension to Figure 2. Closed eyes must stay closed; downcast eyes must stay downcast. "
    "Transfer Figure 1's identity only, never her reference pose or expression. "
    "Do not add the Figure 1 puckered pout. Only swap "
    "identity: face, ears, hair, and earrings."
)
STYLE = (
    "Authentic handheld iPhone photo, amateur snapshot aesthetic, slightly imperfect, no "
    "retouching. Pure photograph."
)
STRIP_TEXT = (
    "Remove added on-screen text, captions, graphic stickers, emoji overlays, and watermarks "
    "from the source. Do not add text. Preserve real scene details, including physical stickers "
    "on the laptop, clothing, equipment, and background objects."
)


def build_prompt(scene: str | None, keep_text: bool) -> str:
    parts = [IDENTITY_LOCK, COMPOSITION, EXPRESSION, STYLE]
    if not keep_text:
        parts.append(STRIP_TEXT)
    if scene:
        parts.append(f"Scene notes: {scene.strip()}")
    return " ".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Face-swap the locked avatar onto composition boards.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__.split("Examples:", 1)[-1] if __doc__ else None,
    )
    parser.add_argument("boards", nargs="+", help="Board image(s): file, folder, or glob")
    parser.add_argument("--account", default=DEFAULT_ACCOUNT, help="Account folder under accounts/")
    parser.add_argument("--avatar", "--anchor", dest="avatar", help="Identity still (default accounts/{account}/avatar/asian-girl-avatar.jpg); --anchor is a compatibility alias")
    parser.add_argument("--scene", help="Extra scene / styling notes appended to the prompt")
    parser.add_argument("--variants", type=int, default=1, help="Renders per board (default 1)")
    parser.add_argument("--workers", type=int, default=3, help="Parallel fal calls (default 3)")
    parser.add_argument("--size", default=DEFAULT_SIZE, help=f"WIDTHxHEIGHT or source to request each board's dimensions (default {DEFAULT_SIZE})")
    parser.add_argument("--format", choices=("jpeg", "png"), default="jpeg")
    parser.add_argument("--keep-text", action="store_true", help="Do not ask the model to strip source text")
    parser.add_argument("--out-dir", help="Override the batch outputs folder")
    parser.add_argument("--post", type=int, help="Write the single result to accounts/{account}/posts/N/image.jpg")
    parser.add_argument("--force", action="store_true", help="Allow --post to overwrite an existing image.jpg")
    parser.add_argument("--no-sheet", action="store_true", help="Skip the contact sheet")
    parser.add_argument("--prompt-only", action="store_true", help="Print the prompt and exit")
    parser.add_argument("--dry-run", action="store_true", help="List planned outputs without calling fal")
    return parser.parse_args()


def collect_boards(patterns: list[str]) -> list[Path]:
    boards: list[Path] = []
    for pattern in patterns:
        path = resolve_repo_path(pattern)
        found = list_images(path)
        if not found:
            matches = glob.glob(pattern) if Path(pattern).is_absolute() else glob.glob(str(PROJECT_ROOT / pattern))
            if not matches:
                matches = glob.glob(pattern)
            for match in sorted(matches):
                found.extend(list_images(Path(match)))
        if not found:
            raise SystemExit(f"No board images found for: {pattern}")
        for item in found:
            item = item.resolve()
            if item not in boards:
                boards.append(item)
    return boards


def swap_one(
    board: Path,
    out_path: Path,
    prompt: str,
    avatar_uri: str,
    size: tuple[int, int],
    fmt: str,
    api_key: str,
) -> Path:
    payload = {
        "prompt": prompt,
        "image_size": {"width": size[0], "height": size[1]},
        "num_images": 1,
        "output_format": fmt,
        "enable_safety_checker": True,
        "image_urls": [avatar_uri, file_to_data_uri(board)],
    }
    body = run_sync(SEEDREAM_EDIT, payload, api_key, timeout=240)
    return download(first_image_url(body), out_path)


def build_contact_sheet(items: list[tuple[str, Path]], out_path: Path, size: tuple[int, int]) -> Path:
    from PIL import Image, ImageDraw, ImageFont

    thumb_w = 360
    thumb_h = round(thumb_w * size[1] / size[0])
    pad, label_h = 16, 34
    cols = min(4, len(items))
    rows = (len(items) + cols - 1) // cols
    sheet = Image.new(
        "RGB",
        (pad + cols * (thumb_w + pad), pad + rows * (thumb_h + label_h + pad)),
        (24, 24, 27),
    )
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.load_default(size=16)
    except TypeError:  # older Pillow without size support
        font = ImageFont.load_default()

    for index, (label, path) in enumerate(items):
        x = pad + (index % cols) * (thumb_w + pad)
        y = pad + (index // cols) * (thumb_h + label_h + pad)
        try:
            with Image.open(path) as image:
                image = image.convert("RGB")
                image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
                sheet.paste(image, (x + (thumb_w - image.width) // 2, y + (thumb_h - image.height) // 2))
        except OSError:
            draw.rectangle([x, y, x + thumb_w, y + thumb_h], fill=(60, 30, 30))
        draw.text((x + 6, y + thumb_h + 8), label[:40], fill=(235, 235, 235), font=font)

    sheet.save(out_path, "JPEG", quality=88)
    return out_path


def write_caption_stub(post_dir: Path, post_number: int, board: Path) -> None:
    caption_path = post_dir / "caption.md"
    if caption_path.exists():
        return
    caption_path.write_text(
        "\n".join(
            [
                f"# Post {post_number} — {board.stem}",
                "",
                "- **Status**: Draft, not posted",
                "- **Format**: Selfie + text + CTA (single still)",
                f"- **Board**: `{board.relative_to(PROJECT_ROOT) if board.is_relative_to(PROJECT_ROOT) else board}`",
                "- **Image**: `image.jpg` (clean still)",
                "",
                "## Approved copy",
                "",
                "None yet. Paste candidate lines in chat, get approval, then render with",
                f"`python tools/fal/caption.py --image {post_dir.relative_to(PROJECT_ROOT) / 'image.jpg'} --text \"...\"`.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    args = parse_args()
    prompt = build_prompt(args.scene, args.keep_text)
    if args.prompt_only:
        print(prompt)
        return 0

    if args.variants < 1:
        raise SystemExit("--variants must be at least 1")
    size = None if args.size.lower() == "source" else parse_size(args.size)
    account_dir = PROJECT_ROOT / "accounts" / args.account
    avatar = resolve_repo_path(args.avatar) if args.avatar else account_dir / "avatar" / "asian-girl-avatar.jpg"
    if not avatar.exists():
        raise SystemExit(f"Asian girl avatar not found: {avatar}")

    boards = collect_boards(args.boards)
    board_sizes: dict[Path, tuple[int, int]] = {}
    for board in boards:
        if size is not None:
            board_sizes[board] = size
        else:
            from PIL import Image, ImageOps

            with Image.open(board) as image:
                board_sizes[board] = ImageOps.exif_transpose(image).size

    # Plan outputs.
    jobs: list[tuple[Path, Path]] = []
    post_dir: Path | None = None
    if args.post is not None:
        if len(boards) != 1 or args.variants != 1:
            raise SystemExit("--post takes exactly one board and --variants 1. Run a batch into outputs/ first.")
        post_dir = account_dir / "posts" / str(args.post)
        target = post_dir / f"image.{'jpg' if args.format == 'jpeg' else 'png'}"
        if target.exists() and not args.force:
            raise SystemExit(f"{target} already exists. Re-run with --force to overwrite a posted still.")
        jobs.append((boards[0], target))
        out_dir = post_dir
    else:
        stamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        out_dir = resolve_repo_path(args.out_dir) if args.out_dir else account_dir / "outputs" / stamp
        ext = "jpg" if args.format == "jpeg" else "png"
        for board in boards:
            for variant in range(1, args.variants + 1):
                suffix = f"-v{variant}" if args.variants > 1 else ""
                jobs.append((board, out_dir / f"{board.stem}{suffix}.{ext}"))

    print(f"avatar:  {avatar}")
    size_label = f"{size[0]}x{size[1]}" if size else "source (per board)"
    print(f"boards:  {len(boards)}  variants: {args.variants}  fal calls: {len(jobs)}  size: {size_label}")
    print(f"out:     {out_dir}")
    if args.dry_run:
        for board, out_path in jobs:
            width, height = board_sizes[board]
            print(f"  {board.name} ({width}x{height}) -> {out_path}")
        return 0

    api_key = get_api_key()
    avatar_uri = file_to_data_uri(avatar)
    out_dir.mkdir(parents=True, exist_ok=True)

    results: list[tuple[str, Path]] = []
    failures: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(swap_one, board, out_path, prompt, avatar_uri, board_sizes[board], args.format, api_key): (board, out_path)
            for board, out_path in jobs
        }
        for future in concurrent.futures.as_completed(futures):
            board, out_path = futures[future]
            try:
                future.result()
                results.append((out_path.stem, out_path))
                print(f"  ok   {board.name} -> {out_path}")
            except (FalError, OSError, TimeoutError) as exc:
                failures.append(f"{board.name}: {exc}")
                print(f"  FAIL {board.name}: {exc}", file=sys.stderr)

    results.sort(key=lambda item: item[1].name)

    if post_dir is not None and results:
        write_caption_stub(post_dir, args.post, boards[0])
        print(f"\nPromoted to {results[0][1]}. Add the row to accounts/{args.account}/README.md posts table.")
    elif len(results) > 1 and not args.no_sheet:
        sheet = build_contact_sheet(results, out_dir / "contact-sheet.jpg", size or (1080, 1440))
        print(f"\ncontact sheet: {sheet}")

    if failures:
        print(f"\n{len(failures)} failed:", file=sys.stderr)
        for line in failures:
            print(f"  {line}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
