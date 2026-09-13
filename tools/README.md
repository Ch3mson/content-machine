# Tools

Runnable utilities. Run everything from the repo root; paths may be
repo-relative or absolute.

| Tool | Path | Used by |
| --- | --- | --- |
| Avatar face-swap | `fal/swap_avatar.py` | `avatar-face-swap` skill. Anchor + board(s) through Seedream edit, review folder + contact sheet, `--post N` for a fresh render directly into a post. |
| Caption overlay | `fal/caption.py` | `caption-overlay` skill. Approved lines onto a still (TikTok Sans, centered, outlined). Local Pillow only. |
| Still generate / edit | `fal/generate.py` | Free-form Seedream text-to-image or multi-ref edit. |
| Image to video | `fal/video.py` | Optional Kling clip from a still. |
| fal client | `fal/_client.py` | Shared helpers (FAL_KEY, data URIs, sync/queue runs, uploads). Not a CLI. |
| TikTok Photo Sourcer | `tiktok-photo-sourcer/` | Boards and reference posts from TikTok photo URLs. |
| TikTok Transcript Sourcer | `tiktok-transcript-sourcer/` | Hook-idea transcripts for TikTok videos through Supadata (`SUPADATA_API_KEY`). |
| Slideshow Transcriber | `slideshow-transcriber/` | Slide-by-slide text scaffolds for reference carousels during hook extraction. |

Scratch output: `fal/out/` and `accounts/*/outputs/` are gitignored.

Strategy docs, templates, and product files do not belong here.
