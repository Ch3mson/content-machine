# Slideshow Transcriber

Creates a slide-by-slide transcript scaffold from a folder of slideshow images.
The agent then visually inspects each image and fills in the visible text.

## Usage

```powershell
python tools/slideshow-transcriber/prepare_slideshow_transcript.py `
  "references/hook-ideas/inbox/slideshows/my-post/images" `
  --source-url "https://www.tiktok.com/@creator/photo/1234567890"
```

Default output:

```text
references/hook-ideas/inbox/slideshows/YYYY-MM-DD-my-post.md
```
