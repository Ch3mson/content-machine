# Image Sourcing Tool

Uses [browser-harness](https://github.com/browser-use/browser-harness) (patched for Windows) to search Pinterest via your logged-in Chrome session, download candidate images, and select the best match per slide based on 9:16 aspect ratio.

## How It Works

1. **Preset** — Each slideshow folder has an `image_preset.json` that maps slides to search queries.
2. **Search** — The tool navigates Pinterest (using your logged-in session) for each query.
3. **Download** — It downloads candidate images and checks their actual dimensions.
4. **Filter** — Picks the image closest to 9:16 (0.5625 ratio) within tolerance.
5. **Save** — Writes one image per slide to the account's `sourced/` folder.

## Quick Start

### 1. Connect Your Chrome

The tool needs to control your Chrome. Close Chrome completely, then restart it with remote debugging:

**PowerShell:**
```powershell
# Close Chrome first
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

Then run the connector:
```bash
python tools/browser-harness/connect_my_chrome.py
```

This preserves all your logins, bookmarks, and Pinterest sessions.

### 2. Run Image Sourcing

```bash
python tools/image-sourcer/source_images.py accounts/athlete-stories/Lebron/image_preset.json
```

Images are saved to `accounts/athlete-stories/Lebron/sourced/`.

### 3. Process for Slideshows

After sourcing, run the account's `process_images.py` (or your equivalent pipeline) to normalize to 9:16, apply B&W, overlay text, etc.

## Preset Format

Create an `image_preset.json` in any account folder:

```json
{
  "account": "athlete-stories",
  "subject": "Lebron",
  "source": "pinterest",
  "output_dir": "accounts/athlete-stories/Lebron/sourced",
  "slides": [
    {
      "slide": 1,
      "role": "The Beginning",
      "queries": [
        "lebron james young akron childhood",
        "lebron james kid basketball childhood"
      ]
    }
  ],
  "filters": {
    "target_ratio": 0.5625,
    "ratio_tolerance": 0.35,
    "min_width": 350,
    "min_height": 450,
    "max_candidates_per_slide": 40,
    "download_timeout": 15
  }
}
```

| Field | Description |
|-------|-------------|
| `source` | `pinterest` or `duckduckgo` |
| `slides[].source` | Override preset source per slide. `"ask_user"` skips automated search and prompts you to provide the image manually. Useful for product shots. |
| `slides[].queries` | List of search strings. Tried in order until a match is found. |
| `target_ratio` | Desired aspect ratio (width / height). 9:16 = 0.5625. |
| `ratio_tolerance` | Max deviation from target ratio to accept a candidate. |
| `min_width` / `min_height` | Reject images smaller than this. |

## Windows Patch

browser-harness uses Unix domain sockets which don't work on native Windows. We patched it to use TCP sockets on Windows (`tools/browser-harness/_compat.py`). This is a local patch — don't push it upstream.

## Troubleshooting

**"No Chrome remote debugging detected"**
→ Chrome isn't running with `--remote-debugging-port=9222`. Run `connect_my_chrome.py`.

**"Daemon failed to start"**
→ The daemon from a previous run may be stale. Kill any Python processes running `daemon.py` and retry.

**Pinterest returns mostly small images**
→ The search query matters. Try more specific queries like `"lebron james portrait high resolution"` or `"lebron james 4k wallpaper"`.

**Images don't match 9:16 well**
→ Increase `ratio_tolerance` in the preset (e.g., 0.4) or add more query variations per slide.
