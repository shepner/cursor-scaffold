#!/usr/bin/env python3
"""
cursor-scaffold: install curated Cursor rule packs into another repository.

Why this exists:
- Cursor *executes* rules from a repo's `.cursor/rules/`.
- A central library is still valuable, but it's best treated as **source material**:
  copy a small selection into each target repo, rather than making a huge always-on set.

This helper copies `.mdc` files from `.cursor/packs/<pack>/` into `<target>/.cursor/rules/`.

Defaults:
- installed rules are set to `alwaysApply: false` to avoid immediate noise

Options:
- `--enable <pack>` flips `alwaysApply: true` for all rules installed from that pack
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]  # .../.cursor/helpers/ -> repo root
PACKS_DIR = REPO_ROOT / ".cursor" / "packs"


@dataclass(frozen=True)
class CopyPlan:
    src: Path
    dst: Path
    enable: bool


def _iter_pack_files(pack: str) -> list[Path]:
    pack_dir = PACKS_DIR / pack
    if not pack_dir.exists() or not pack_dir.is_dir():
        raise SystemExit(f"Pack not found: {pack!r} (expected directory {pack_dir})")
    return sorted([p for p in pack_dir.rglob("*.mdc") if p.is_file()])


def _set_always_apply(content: str, value: bool) -> str:
    """
    Set alwaysApply in the first YAML frontmatter block.
    If not present, insert it near the top of the YAML block.
    """
    m = re.search(r"\A---\n([\s\S]*?)\n---\n", content)
    v = "true" if value else "false"
    if not m:
        return f"---\nalwaysApply: {v}\n---\n\n" + content

    yaml_body = m.group(1)
    if re.search(r"(?m)^\s*alwaysApply\s*:", yaml_body):
        yaml_body2 = re.sub(r"(?m)^\s*alwaysApply\s*:\s*.*$", f"alwaysApply: {v}", yaml_body, count=1)
    else:
        yaml_body2 = f"alwaysApply: {v}\n" + yaml_body

    return content[: m.start(1)] + yaml_body2 + content[m.end(1) :]


def _build_plans(target: Path, packs: Iterable[str], enable_packs: set[str]) -> list[CopyPlan]:
    plans: list[CopyPlan] = []
    target_rules_dir = target / ".cursor" / "rules"

    for pack in packs:
        for src in _iter_pack_files(pack):
            # Prefix with pack name to avoid collisions across packs.
            dst_name = f"{pack}-{src.name}"
            plans.append(CopyPlan(src=src, dst=target_rules_dir / dst_name, enable=pack in enable_packs))

    return plans


def _copy_one(plan: CopyPlan, dry_run: bool) -> None:
    plan.dst.parent.mkdir(parents=True, exist_ok=True)

    if dry_run:
        print(f"[dry-run] copy {plan.src} -> {plan.dst} (alwaysApply={'true' if plan.enable else 'false'})")
        return

    content = plan.src.read_text(encoding="utf-8")
    content2 = _set_always_apply(content, plan.enable)
    plan.dst.write_text(content2, encoding="utf-8")
    shutil.copystat(plan.src, plan.dst, follow_symlinks=True)
    print(f"copied {plan.src.name} -> {plan.dst} (alwaysApply={'true' if plan.enable else 'false'})")


def main() -> int:
    ap = argparse.ArgumentParser(description="cursor-scaffold: install Cursor rule packs into a target repo.")
    ap.add_argument("--target", required=True, help="Target repo directory to receive .cursor/rules/")
    ap.add_argument("--packs", nargs="+", required=True, help="Pack(s) to install (directories under .cursor/packs/)")
    ap.add_argument(
        "--enable",
        nargs="*",
        default=[],
        help="Pack(s) to set alwaysApply:true on install (default: none; installs as alwaysApply:false)",
    )
    ap.add_argument("--dry-run", action="store_true", help="Print actions without writing files")
    args = ap.parse_args()

    target = Path(os.path.expanduser(args.target)).resolve()
    if not target.exists() or not target.is_dir():
        raise SystemExit(f"Target not found or not a directory: {target}")

    packs = list(dict.fromkeys(args.packs))  # de-dupe, preserve order
    enable_packs = set(args.enable or [])

    plans = _build_plans(target=target, packs=packs, enable_packs=enable_packs)
    if not plans:
        print("No files to install (empty packs?)")
        return 0

    for plan in plans:
        _copy_one(plan, dry_run=bool(args.dry_run))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

