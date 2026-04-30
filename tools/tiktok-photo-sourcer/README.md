# TikTok Photo Sourcer

Downloads TikTok photo carousels into `references/social-accounts/...` using
`gallery-dl`. The wrapper intentionally does not use `tiktok-cookies.txt`.

## Quick Start

```powershell
python tools/tiktok-photo-sourcer/download_tiktok_photos.py `
  --account legendperform `
  --post 5 `
  "https://www.tiktok.com/@legendperforming/photo/7553359406495288598"
```

This saves files as:

```text
references/social-accounts/legendperform/Post 5/1.jpg
references/social-accounts/legendperform/Post 5/2.jpg
references/social-accounts/legendperform/Post 5/3.jpg
```

Use a direct folder when needed:

```powershell
python tools/tiktok-photo-sourcer/download_tiktok_photos.py `
  --out "references/social-accounts/legendperform/Post 5" `
  "https://www.tiktok.com/@legendperforming/photo/7553359406495288598"
```

## Dependency

The script uses the local Python module first if `gallery-dl` is not on PATH.
If neither is installed:

```powershell
python -m pip install gallery-dl
```
