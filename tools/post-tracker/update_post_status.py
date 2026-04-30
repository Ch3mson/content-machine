from __future__ import annotations

import os
import re
import shutil
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[2]
ACCOUNTS_DIR = ROOT / "accounts"

NON_POST_DIRS = {
    "extractions",
    "posts",
    "quality-gate",
    "ready-to-post",
    "writing",
}

IMAGE_EXTENSIONS = {".jpeg", ".jpg", ".png", ".webp"}
SLIDE_RE = re.compile(r"^slide_(\d+)\.png$", re.IGNORECASE)
STATUS_RE = re.compile(r"^>\s*Status:\s*(.+)$", re.IGNORECASE | re.MULTILINE)
LEADING_NUMBER_RE = re.compile(r"^\d+[-_\s]+")

PENDING_FLOW_MARKERS = (
    "ready for image sourcing",
    "no photos sourced",
    "not sourced yet",
    "not_sourced_yet",
)


@dataclass
class PostRecord:
    account: str
    account_path: Path
    name: str
    workspace: Path
    workspace_type: str
    flow_path: Path | None
    slide_paths: list[Path]
    sourced_count: int
    concept_count: int
    has_preset: bool
    has_processor: bool
    flow_status: str
    status: str
    stage: str
    next_action: str
    ready_pack: Path | None = None


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def canonical_name(name: str) -> str:
    name = LEADING_NUMBER_RE.sub("", name)
    name = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return name or "post"


def md_escape(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", " ")


def md_link(label: str, target: Path, base: Path) -> str:
    rel = os.path.relpath(target, start=base).replace("\\", "/")
    href = quote(rel, safe="/#.")
    return f"[{md_escape(label)}]({href})"


def sorted_slide_paths(path: Path) -> list[Path]:
    slides = [item for item in path.glob("slide_*.png") if SLIDE_RE.match(item.name)]
    return sorted(slides, key=lambda item: int(SLIDE_RE.match(item.name).group(1)))


def count_files(path: Path, extensions: set[str] | None = None) -> int:
    if not path.exists():
        return 0
    files = [item for item in path.rglob("*") if item.is_file()]
    if extensions is None:
        return len(files)
    return sum(1 for item in files if item.suffix.lower() in extensions)


def is_post_candidate(path: Path) -> bool:
    markers = ["flow.md", "image_preset.json", "process_images.py"]
    if any((path / marker).exists() for marker in markers):
        return True
    if any((path / marker).is_dir() for marker in ["concept", "processed", "sourced"]):
        return True
    return bool(sorted_slide_paths(path))


def is_flat_ready_pack(path: Path) -> bool:
    has_flow = (path / "flow.md").exists()
    has_direct_slides = bool(sorted_slide_paths(path))
    has_workspace_files = any(
        (path / marker).exists()
        for marker in ["concept", "image_preset.json", "process_images.py", "processed", "sourced"]
    )
    return has_flow and has_direct_slides and not has_workspace_files


def inspect_post(account_path: Path, path: Path, workspace_type: str) -> PostRecord:
    flow_path = path / "flow.md"
    flow_text = read_text(flow_path) if flow_path.exists() else ""
    flow_status_match = STATUS_RE.search(flow_text)
    flow_status = flow_status_match.group(1).strip() if flow_status_match else ""

    processed_slides = sorted_slide_paths(path / "processed")
    direct_slides = sorted_slide_paths(path)
    slide_paths = processed_slides or direct_slides

    sourced_count = count_files(path / "sourced", IMAGE_EXTENSIONS)
    concept_count = count_files(path / "concept")
    has_preset = (path / "image_preset.json").exists()
    has_processor = (path / "process_images.py").exists()

    status, stage, next_action = classify_post(
        flow_path.exists(),
        flow_text,
        flow_status,
        len(slide_paths),
        sourced_count,
        concept_count,
        has_preset,
        has_processor,
    )

    return PostRecord(
        account=account_path.name,
        account_path=account_path,
        name=path.name,
        workspace=path,
        workspace_type=workspace_type,
        flow_path=flow_path if flow_path.exists() else None,
        slide_paths=slide_paths,
        sourced_count=sourced_count,
        concept_count=concept_count,
        has_preset=has_preset,
        has_processor=has_processor,
        flow_status=flow_status,
        status=status,
        stage=stage,
        next_action=next_action,
    )


def classify_post(
    has_flow: bool,
    flow_text: str,
    flow_status: str,
    slide_count: int,
    sourced_count: int,
    concept_count: int,
    has_preset: bool,
    has_processor: bool,
) -> tuple[str, str, str]:
    lower_flow = flow_text.lower()
    lower_status = flow_status.lower()
    has_pending_assets = any(marker in lower_flow for marker in PENDING_FLOW_MARKERS)
    is_draft = "draft" in lower_status or lower_status.startswith("wip")

    if has_flow and slide_count:
        if is_draft:
            return (
                "In Progress",
                "Rendered draft",
                "Approve final copy/assets, update flow status, then rerun tracker",
            )
        if has_pending_assets:
            return (
                "In Progress",
                "Rendered, assets still marked pending",
                "Source/map final images or remove pending markers, then rerun tracker",
            )
        return ("Done", "Ready to post", "Post from ready-to-post pack")

    if has_flow:
        if sourced_count and has_processor:
            return ("In Progress", "Images sourced", "Run the post process_images.py")
        if sourced_count:
            return ("In Progress", "Images sourced", "Create process_images.py, then render")
        if has_preset:
            return ("In Progress", "Flow approved", "Run image sourcing, then Workflow C")
        return ("In Progress", "Flow approved", "Map/source images, then render")

    if concept_count:
        return ("In Progress", "Copy review", "Approve copy, then write final flow.md")

    if sourced_count:
        return ("In Progress", "Images collected, no flow", "Draft/approve copy and map images")

    return ("Started", "Post folder created", "Continue Workflow B")


def discover_account_posts(account_path: Path) -> list[PostRecord]:
    records: list[PostRecord] = []
    seen: set[str] = set()
    flat_ready_packs: list[Path] = []

    for child in sorted(account_path.iterdir(), key=lambda item: item.name.lower()):
        if not child.is_dir():
            continue
        if child.name in NON_POST_DIRS or child.name.startswith("."):
            continue
        if is_post_candidate(child):
            record = inspect_post(account_path, child, "legacy workspace")
            records.append(record)
            seen.add(canonical_name(child.name))

    preferred_posts = account_path / "posts"
    if preferred_posts.exists():
        for child in sorted(preferred_posts.iterdir(), key=lambda item: item.name.lower()):
            if not child.is_dir() or child.name.startswith("."):
                continue
            if is_flat_ready_pack(child):
                flat_ready_packs.append(child)
                continue
            if is_post_candidate(child):
                record = inspect_post(account_path, child, "post workspace")
                records.append(record)
                seen.add(canonical_name(child.name))

    for child in flat_ready_packs:
        key = canonical_name(child.name)
        if key in seen:
            continue
        records.append(inspect_post(account_path, child, "flat ready pack"))
        seen.add(key)

    return sorted(records, key=lambda record: (record.status != "Done", record.name.lower()))


def refresh_ready_pack(record: PostRecord) -> None:
    if record.status != "Done" or record.flow_path is None or not record.slide_paths:
        return

    pack_dir = record.account_path / "ready-to-post" / record.name
    pack_dir.mkdir(parents=True, exist_ok=True)

    flow_dest = pack_dir / "flow.md"
    if flow_dest.exists():
        flow_dest.unlink()
    for old_slide in sorted_slide_paths(pack_dir):
        old_slide.unlink()

    shutil.copy2(record.flow_path, flow_dest)
    for slide_path in record.slide_paths:
        shutil.copy2(slide_path, pack_dir / slide_path.name)

    record.ready_pack = pack_dir


def render_root_dashboard(records: list[PostRecord], account_paths: list[Path]) -> str:
    lines = [
        "# Post Status Dashboard",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "Use this as the quick view for every account and post. In-progress work stays in the source workspace; finished posting packs are copied to each account's `ready-to-post/` folder.",
        "",
        "## Funnel",
        "",
        "| Stage | Where it lives | What it means |",
        "| --- | --- | --- |",
        "| Concept / copy review | `accounts/{account}/posts/{post}/concept/` or legacy post folder | Idea, VOC, angle, or draft copy exists, but final `flow.md` is not ready. |",
        "| Flow approved | post workspace `flow.md` | Copy is ready, but images or rendering are not complete. |",
        "| Images sourced | post workspace `sourced/` | Raw images exist and need mapping/rendering. |",
        "| Rendered draft | post workspace `processed/` | PNGs exist, but the flow still marks draft or pending assets. |",
        "| Ready to post | `accounts/{account}/ready-to-post/{post}/` | Folder contains only `flow.md` and final `slide_*.png` files. |",
        "",
        "## Global Table",
        "",
    ]
    lines.extend(render_records_table(records, ROOT, include_account=True))
    lines.append("")
    lines.append("## Account Dashboards")
    lines.append("")
    for account_path in account_paths:
        lines.append(f"- {md_link(account_path.name, account_path / 'post-status.md', ROOT)}")
    return "\n".join(lines) + "\n"


def render_account_dashboard(account_path: Path, records: list[PostRecord]) -> str:
    lines = [
        f"# {account_path.name} Post Status",
        "",
        f"Generated: {date.today().isoformat()}",
        "",
        "## Account Funnel",
        "",
        "- Work in `posts/{post-slug}/` for new posts, or the legacy post folder when one already exists.",
        "- Store finished publish packs in `ready-to-post/{post-slug}/`.",
        "- Each publish pack contains only `flow.md` and `slide_*.png` files so posting assets are easy to find.",
        "- Rerun `python tools/post-tracker/update_post_status.py` from the workspace root after a post changes stage.",
        "",
        "## Posts",
        "",
    ]
    lines.extend(render_records_table(records, account_path, include_account=False))
    return "\n".join(lines) + "\n"


def render_ready_index(account_path: Path, records: list[PostRecord]) -> str:
    ready_records = [record for record in records if record.ready_pack is not None]
    lines = [
        f"# {account_path.name} Ready To Post",
        "",
        "Each post folder here is a clean publishing pack. Individual post folders should contain only `flow.md` and final `slide_*.png` files.",
        "",
    ]
    if not ready_records:
        lines.append("No finished posts are ready yet.")
        return "\n".join(lines) + "\n"

    lines.extend(
        [
            "| Post | Slides | Folder | Flow |",
            "| --- | ---: | --- | --- |",
        ]
    )
    for record in ready_records:
        lines.append(
            "| "
            + " | ".join(
                [
                    md_escape(record.name),
                    str(len(record.slide_paths)),
                    md_link(record.ready_pack.name, record.ready_pack, account_path / "ready-to-post"),
                    md_link("flow", record.ready_pack / "flow.md", account_path / "ready-to-post"),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def render_records_table(records: list[PostRecord], base: Path, include_account: bool) -> list[str]:
    if not records:
        return ["No post workspaces found yet."]

    headers = ["Post", "Status", "Stage", "Slides", "Next action", "Workspace", "Ready pack", "Flow"]
    if include_account:
        headers.insert(0, "Account")

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]

    for record in records:
        ready_pack = md_link(record.ready_pack.name, record.ready_pack, base) if record.ready_pack else "-"
        flow_target = None
        if record.ready_pack:
            flow_target = record.ready_pack / "flow.md"
        elif record.flow_path:
            flow_target = record.flow_path
        flow_link = md_link("flow", flow_target, base) if flow_target else "-"
        workspace_label = record.workspace.name
        if record.workspace_type == "post workspace":
            workspace_label = f"posts/{record.workspace.name}"

        row = [
            md_escape(record.name),
            record.status,
            record.stage,
            str(len(record.slide_paths)) if record.slide_paths else "-",
            record.next_action,
            md_link(workspace_label, record.workspace, base),
            ready_pack,
            flow_link,
        ]
        if include_account:
            row.insert(0, md_link(record.account, record.account_path / "post-status.md", base))
        lines.append("| " + " | ".join(md_escape(cell) if not cell.startswith("[") else cell for cell in row) + " |")

    return lines


def main() -> None:
    if not ACCOUNTS_DIR.exists():
        raise SystemExit(f"Missing accounts directory: {ACCOUNTS_DIR}")

    all_records: list[PostRecord] = []
    account_records: dict[Path, list[PostRecord]] = {}

    account_paths = [
        path
        for path in sorted(ACCOUNTS_DIR.iterdir(), key=lambda item: item.name.lower())
        if path.is_dir() and not path.name.startswith(".")
    ]

    for account_path in account_paths:
        records = discover_account_posts(account_path)
        for record in records:
            refresh_ready_pack(record)
        account_records[account_path] = records
        all_records.extend(records)

    for account_path, records in account_records.items():
        ready_dir = account_path / "ready-to-post"
        ready_dir.mkdir(parents=True, exist_ok=True)
        write_text(account_path / "post-status.md", render_account_dashboard(account_path, records))
        write_text(ready_dir / "README.md", render_ready_index(account_path, records))

    write_text(ROOT / "POST_STATUS.md", render_root_dashboard(all_records, account_paths))

    print(f"Updated {ROOT / 'POST_STATUS.md'}")
    print(f"Updated {len(account_records)} account dashboards")


if __name__ == "__main__":
    main()
