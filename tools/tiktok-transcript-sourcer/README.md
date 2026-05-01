# TikTok Transcript Sourcer

Fetches transcripts for public TikTok videos using Supadata. It does not
download the video.

## Setup

Set your Supadata key as an environment variable or in local `.env`:

```powershell
$env:SUPADATA_API_KEY = "your_key_here"
```

or:

```text
SUPADATA_API_KEY=your_key_here
```

Do not commit `.env`.

## Usage

```powershell
python tools/tiktok-transcript-sourcer/download_tiktok_transcript.py `
  "https://www.tiktok.com/@creator/video/1234567890"
```

Default output:

```text
references/hook-ideas/inbox/transcripts/YYYY-MM-DD-tiktok-1234567890.md
```

Use `--mode native` to avoid AI generation costs. Use `--mode auto` or
`--mode generate` when you want Supadata to generate a transcript if needed.
