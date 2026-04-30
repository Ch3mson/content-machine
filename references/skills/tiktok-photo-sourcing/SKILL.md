---
name: tiktok-photo-sourcing
description: Download TikTok photo carousel posts into slideshow reference folders using the project wrapper. Use when the user wants TikTok photo images saved, mentions TikTok carousel/source images/reference posts, or asks to avoid remembering the gallery-dl command.
---

# TikTok Photo Sourcing

## Overview

Use this skill to save TikTok photo carousel images into `references/social-accounts/{account}/{post}/` without cookies. Prefer the project wrapper instead of writing raw `gallery-dl` commands in chat.

## Command

Use:

```powershell
python tools/tiktok-photo-sourcer/download_tiktok_photos.py `
  --account {reference-account-folder} `
  --post {post-number-or-label} `
  "{tiktok-photo-url}"
```

Example:

```powershell
python tools/tiktok-photo-sourcer/download_tiktok_photos.py `
  --account legendperform `
  --post 5 `
  "https://www.tiktok.com/@legendperforming/photo/7553359406495288598"
```

This writes numbered files such as `1.jpg`, `2.jpg`, and `3.jpg`.

Use `--out` when the user provides an exact output folder:

```powershell
python tools/tiktok-photo-sourcer/download_tiktok_photos.py `
  --out "references/social-accounts/legendperform/Post 5" `
  "{tiktok-photo-url}"
```

## Rules

- Do not pass `-C`, `--cookies`, or `tiktok-cookies.txt`.
- Keep downloaded reference images in `references/social-accounts/` unless the user names a different folder.
- Use `--post 5` for normal reference folders; the wrapper normalizes it to `Post 5`.
- Use `--dry-run` to inspect the underlying `gallery-dl` command without downloading.
- If `gallery-dl` is missing, install it with `python -m pip install gallery-dl`.

## Underlying Behavior

The wrapper calls `gallery-dl` with TikTok audio and video disabled, TikTok photos enabled, `--sleep-request 2-5`, and filename template `{num}.{extension}`.
