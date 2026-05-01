#!/usr/bin/env python3
"""Update hook-memory documents from one post extraction manifest."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
HOOK_INDEX = PROJECT_ROOT / "references" / "hook-ideas" / "index.md"
HOOK_CARDS = PROJECT_ROOT / "references" / "hook-ideas" / "cards"
USAGE_LEDGER = PROJECT_ROOT / "references" / "hook-ideas" / "usage-ledger.md"
POST_INDEX = PROJECT_ROOT / "references" / "social-accounts" / "post-index.md"
TAXONOMY = PROJECT_ROOT / "references" / "social-accounts" / "taxonomy.md"


@dataclass(frozen=True)
class WritePlan:
    path: Path
    content: str


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = [
        "source_id",
        "card_slug",
        "source_label",
        "content_type",
        "original_hook",
        "hook_archetype",
        "transferable_pattern",
        "tags",
        "account_fit",
    ]
    missing = [field for field in required if not data.get(field)]
    if missing:
        raise SystemExit(f"Missing required manifest fields: {', '.join(missing)}")
    return data


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    if isinstance(value, str):
        return [value] if value.strip() else []
    return [str(value)]


def md_list(items: Any) -> str:
    values = as_list(items)
    return "\n".join(f"- {item}" for item in values) if values else "- "


def md_join(items: Any) -> str:
    return ", ".join(as_list(items))


def table_escape(value: Any) -> str:
    text = str(value or "")
    return text.replace("\n", " ").replace("|", "\\|").strip()


def rel(path: Path) -> str:
    return path.relative_to(PROJECT_ROOT).as_posix()


def source_contact_link(source_id: str) -> str:
    return f"[{source_id}](_review/contact-sheets/{source_id}.jpg)"


def render_flow_map(rows: Any) -> str:
    values = rows if isinstance(rows, list) else []
    lines = [
        "| Beat | Source Moment | Job In The Post | Retention Mechanic |",
        "| --- | --- | --- | --- |",
    ]
    if not values:
        lines.append("| 1 |  |  |  |")
        return "\n".join(lines)
    for index, row in enumerate(values, start=1):
        if not isinstance(row, dict):
            continue
        beat = row.get("beat", index)
        lines.append(
            "| "
            + " | ".join(
                [
                    table_escape(beat),
                    table_escape(row.get("source_moment")),
                    table_escape(row.get("job")),
                    table_escape(row.get("retention_mechanic")),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def render_card(data: dict[str, Any]) -> str:
    payload = data.get("idea_payload") or {}
    fit = data.get("account_fit") or {}
    card_title = data.get("title") or data["card_slug"]
    raw_location = data.get("raw_input_location") or f"references/social-accounts/{data['source_id']}"
    status = data.get("status", "candidate for account concept")
    next_use = data.get("next_use", "Use as a reusable hook pattern after adapting it through the target account writing rules.")
    return "\n".join(
        [
            f"# Hook Card: {card_title}",
            "",
            "## Source",
            "",
            f"- Platform: {data.get('platform', '')}",
            f"- Creator/account: {data.get('creator_account', data['source_label'])}",
            f"- URL: {data.get('source_url', '')}",
            f"- Date captured: {data.get('date', date.today().isoformat())}",
            f"- Raw input location: `{raw_location}`",
            f"- Source post ID: `{data['source_id']}`",
            f"- Content type: {data['content_type']}",
            "",
            "## Original Hook",
            "",
            str(data["original_hook"]).strip(),
            "",
            "## Why It Stops The Scroll",
            "",
            md_list(data.get("scroll_stop")),
            "",
            "## Why People Keep Watching Or Swiping",
            "",
            md_list(data.get("retention")),
            "",
            "## Flow Map",
            "",
            render_flow_map(data.get("flow_map")),
            "",
            "## Hook Archetype",
            "",
            f"- Archetype: {data['hook_archetype']}",
            f"- Emotional lever: {data.get('emotional_lever', '')}",
            f"- Curiosity engine: {data.get('curiosity_engine', '')}",
            f"- Proof or credibility device: {data.get('proof_device', '')}",
            "",
            "## Idea Payload",
            "",
            f"- Surface topic: {payload.get('surface_topic', '')}",
            f"- Deeper viewer desire: {payload.get('deeper_viewer_desire', '')}",
            f"- Private pain or identity gap: {payload.get('private_pain_or_identity_gap', '')}",
            f"- Mechanism or explanation: {payload.get('mechanism_or_explanation', '')}",
            f"- Implied fix direction: {payload.get('implied_fix_direction', '')}",
            "",
            "## Transferable Pattern",
            "",
            f"- Reusable pattern: {data['transferable_pattern']}",
            f"- Safe rewrite formula: {data.get('safe_rewrite_formula', '')}",
            f"- Example adapted direction: {data.get('example_adapted_direction', '')}",
            "",
            "## Account Fit",
            "",
            f"- Best-fit account types: {md_join(fit.get('best_fit'))}",
            f"- Poor-fit account types: {md_join(fit.get('poor_fit'))}",
            f"- Claim or proof risks: {fit.get('claim_or_proof_risks', '')}",
            f"- What not to copy: {fit.get('what_not_to_copy', '')}",
            "",
            "## Tags",
            "",
            md_list(data["tags"]),
            "",
            "## Next Use",
            "",
            f"- Suggested use: {next_use}",
            f"- Status: {status}",
            "",
        ]
    )


def upsert_hook_index(content: str, data: dict[str, Any], card_rel: str) -> str:
    row = (
        f"| {data.get('date', date.today().isoformat())} "
        f"| {table_escape(data['source_label'])} "
        f"| {table_escape(data['content_type'])} "
        f"| `{card_rel}` "
        f"| {table_escape(data['hook_archetype'])} "
        f"| {table_escape(data['transferable_pattern'])} "
        f"| {table_escape(md_join(data['tags']))} "
        f"| {table_escape(md_join((data.get('account_fit') or {}).get('best_fit')))} "
        f"| {table_escape(data.get('status', 'Candidate for account concept'))} |"
    )
    lines = content.rstrip().splitlines()
    card_token = f"`{card_rel}`"
    for index, line in enumerate(lines):
        if card_token in line:
            lines[index] = row
            return "\n".join(lines) + "\n"
    lines.append(row)
    return "\n".join(lines) + "\n"


def update_post_index(content: str, data: dict[str, Any], card_rel_from_social: str) -> str:
    source_id = data["source_id"]
    status = data.get("post_index_status", "hook-carded")
    replacement = f"`{status}` ([card]({card_rel_from_social}))"
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if f"`{source_id}`" not in line:
            continue
        cells = line.split("|")
        if len(cells) < 4:
            continue
        cells[-2] = f" {replacement} "
        lines[index] = "|".join(cells)
        return "\n".join(lines) + "\n"
    raise SystemExit(f"Source ID not found in post-index.md: {source_id}")


def update_taxonomy(content: str, data: dict[str, Any]) -> str:
    archetype = data["hook_archetype"]
    source_id = data["source_id"]
    link = source_contact_link(source_id)
    lines = content.splitlines()
    for index, line in enumerate(lines):
        if not line.startswith(f"| `{archetype}` "):
            continue
        if link in line:
            return content
        cells = line.split("|")
        if len(cells) < 7:
            raise SystemExit("taxonomy.md must include a Derived From column before auto-updating.")
        derived = cells[-2].strip()
        cells[-2] = f" {derived}, {link} " if derived else f" {link} "
        lines[index] = "|".join(cells)
        return "\n".join(lines) + "\n"
    raise SystemExit(f"Hook archetype not found in taxonomy.md: {archetype}")


def append_usage_rows(content: str, data: dict[str, Any]) -> str:
    usage = data.get("usage") or []
    if not isinstance(usage, list) or not usage:
        return content
    lines = content.rstrip().splitlines()
    for item in usage:
        if not isinstance(item, dict):
            continue
        row = (
            f"| {table_escape(item.get('date_used', data.get('date', date.today().isoformat())))} "
            f"| {table_escape(data['card_slug'])} "
            f"| hook-card "
            f"| {table_escape(data['transferable_pattern'])} "
            f"| {table_escape(item.get('target_account'))} "
            f"| {table_escape(item.get('target_post'))} "
            f"| {table_escape(item.get('adapted_hook'))} "
            f"| {table_escape(item.get('reuse_mode', 'pattern-only'))} "
            f"| {table_escape(item.get('notes'))} "
            f"| {table_escape(item.get('status', 'planned'))} |"
        )
        if row not in lines:
            lines.append(row)
    return "\n".join(lines) + "\n"


def build_plan(data: dict[str, Any], overwrite: bool) -> list[WritePlan]:
    card_path = HOOK_CARDS / f"{data['card_slug']}.md"
    if card_path.exists() and not overwrite:
        raise SystemExit(f"Hook card already exists. Use --overwrite to replace: {card_path}")
    card_rel = f"cards/{card_path.name}"
    card_rel_from_social = f"../hook-ideas/{card_rel}"

    hook_index_content = HOOK_INDEX.read_text(encoding="utf-8")
    post_index_content = POST_INDEX.read_text(encoding="utf-8")
    taxonomy_content = TAXONOMY.read_text(encoding="utf-8")
    usage_content = USAGE_LEDGER.read_text(encoding="utf-8")

    return [
        WritePlan(card_path, render_card(data)),
        WritePlan(HOOK_INDEX, upsert_hook_index(hook_index_content, data, card_rel)),
        WritePlan(POST_INDEX, update_post_index(post_index_content, data, card_rel_from_social)),
        WritePlan(TAXONOMY, update_taxonomy(taxonomy_content, data)),
        WritePlan(USAGE_LEDGER, append_usage_rows(usage_content, data)),
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update hook-memory docs from an extraction manifest.")
    parser.add_argument("manifest", help="Path to extraction manifest JSON")
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing hook card")
    parser.add_argument("--dry-run", action="store_true", help="Validate and show planned writes without modifying files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = Path(args.manifest).expanduser().resolve()
    data = load_manifest(manifest_path)
    plan = build_plan(data, overwrite=args.overwrite)
    if args.dry_run:
        print("Dry run OK. Planned writes:")
        for item in plan:
            print(f"- {rel(item.path)}")
        return 0
    for item in plan:
        item.path.parent.mkdir(parents=True, exist_ok=True)
        item.path.write_text(item.content, encoding="utf-8")
    print("Updated hook extraction documents:")
    for item in plan:
        print(f"- {rel(item.path)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

