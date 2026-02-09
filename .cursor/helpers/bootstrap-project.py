#!/usr/bin/env python3
"""
cursor-scaffold: bootstrap a project directory so Cursor can "document and learn".

Ensures:
- git is initialized (even without a remote)
- AGENTS.md exists
- .cursor/ structure exists
- .cursor/rules/self-document-workflows.mdc exists
- .cursor subfolders are tracked (README placeholders)
- .cursor is not ignored by gitignore

Optionally:
- install cursor-scaffold rule packs into the target repo (`.cursor/rules/`)

Default behavior is DRY RUN. Use --apply to make changes.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


SELF_DOCUMENT_RULE = """\
# Self-documenting workflows

This project uses Cursor to continually document and improve its own workflows.
All Cursor-for-Cursor artifacts live under `.cursor/` (rules, skills, notes, helpers).

## When to document or improve

- After a non-trivial or repeatable workflow, add/update a rule/skill/helper.
- When you notice gaps or repeated friction, codify it.

## What to create or update

- Rules: `.cursor/rules/*.mdc`
- Skills: `.cursor/skills/<name>/SKILL.md`
- Notes: `.cursor/notes/`
- Helpers: `.cursor/helpers/`
"""

CURSOR_DIR_README = """\
# Cursor artifacts

This directory is for Cursor-for-Cursor artifacts (rules, helpers, notes, skills).
"""

CURSOR_SUBDIR_README = """\
This directory contains Cursor-for-Cursor artifacts for this project.
"""

GITIGNORE_UNIGNORE_CURSOR_BLOCK = """\

# Cursor (tracked)
!.cursor/
!.cursor/**
"""

INSTALL_PACKS_HELP = """\

## Optional: install cursor-scaffold rule packs

This repo contains curated rule packs under `.cursor/packs/` (source material).
This helper can install selected packs into the target repo via:

  python3 .cursor/helpers/install_cursor_packs.py --target <repo> --packs core git

By default, installed pack rules are set to `alwaysApply: false` to avoid noise.
Use `--enable-packs` to flip `alwaysApply: true` for installed packs.
"""


def agents_md_template(project_name: str) -> str:
    return f"""\
# Cursor agent in this project

This is the **{project_name}** project. Cursor is expected to **document and improve its own workflows** here.

## How the agent should work

- Keep Cursor-for-Cursor artifacts under `.cursor/` (rules, skills, notes, helpers).
- After non-trivial or repeatable workflows, add a rule/skill/helper so future sessions improve.

## Current artifacts

- Rule: `.cursor/rules/self-document-workflows.mdc`
"""


@dataclass(frozen=True)
class Action:
    description: str
    path: Path | None = None
    command: list[str] | None = None
    write_text: str | None = None


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=str(cwd), check=True)


def has_git(project_dir: Path) -> bool:
    return (project_dir / ".git").exists()


def git_check_ignore(project_dir: Path, relpath: str) -> bool:
    # return True if ignored
    r = subprocess.run(
        ["git", "check-ignore", "-q", relpath],
        cwd=str(project_dir),
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return r.returncode == 0


def ensure_gitignore_allows_cursor(actions: list[Action], project_dir: Path) -> None:
    if not has_git(project_dir):
        return
    if not git_check_ignore(project_dir, ".cursor"):
        return

    gitignore = project_dir / ".gitignore"
    existing = gitignore.read_text(encoding="utf-8") if gitignore.exists() else ""
    if "!.cursor/" in existing:
        return
    actions.append(
        Action(
            description="Update .gitignore to track .cursor/",
            path=gitignore,
            write_text=existing + GITIGNORE_UNIGNORE_CURSOR_BLOCK,
        )
    )


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="cursor-scaffold: bootstrap a project for Cursor learning.")
    ap.add_argument("project_dir", help="Path to the project directory")
    ap.add_argument("--apply", action="store_true", help="Apply changes (default: dry run)")
    ap.add_argument(
        "--install-packs",
        nargs="*",
        default=[],
        help="Install cursor-scaffold Cursor rule pack(s) into the project (.cursor/rules/). Example: --install-packs core git",
    )
    ap.add_argument(
        "--enable-packs",
        nargs="*",
        default=[],
        help="Pack(s) to set alwaysApply:true for when installing. Example: --enable-packs core",
    )
    args = ap.parse_args(argv)

    project_dir = Path(args.project_dir).expanduser().resolve()
    if not project_dir.exists() or not project_dir.is_dir():
        raise SystemExit(f"project_dir does not exist or is not a directory: {project_dir}")

    project_name = project_dir.name
    cursor_dir = project_dir / ".cursor"
    cursor_rules = cursor_dir / "rules"
    cursor_helpers = cursor_dir / "helpers"
    cursor_notes = cursor_dir / "notes"
    cursor_skills = cursor_dir / "skills"

    actions: list[Action] = []

    # git init (if needed)
    if not (project_dir / ".git").exists():
        actions.append(Action(description="Initialize git repo", command=["git", "init"]))

    # Create .cursor skeleton
    for p in (cursor_rules, cursor_helpers, cursor_notes, cursor_skills):
        if not p.exists():
            actions.append(Action(description=f"Create directory {p.relative_to(project_dir)}", path=p))

    # Ensure .cursor itself is documented/tracked (so empty dirs are kept in git)
    cursor_readme = cursor_dir / "README.md"
    if not cursor_readme.exists():
        actions.append(Action(description="Create .cursor/README.md", path=cursor_readme, write_text=CURSOR_DIR_README))

    for p in (cursor_helpers, cursor_notes, cursor_skills):
        readme = p / "README.md"
        if not readme.exists():
            actions.append(
                Action(
                    description=f"Create {readme.relative_to(project_dir)}",
                    path=readme,
                    write_text=CURSOR_SUBDIR_README,
                )
            )

    # self-document rule
    rule_path = cursor_rules / "self-document-workflows.mdc"
    if not rule_path.exists():
        actions.append(Action(description="Create self-documenting workflows rule", path=rule_path, write_text=SELF_DOCUMENT_RULE))

    # AGENTS.md
    agents_path = project_dir / "AGENTS.md"
    if not agents_path.exists():
        actions.append(Action(description="Create AGENTS.md", path=agents_path, write_text=agents_md_template(project_name)))

    # If the repo ignores .cursor, unignore it (required for learning)
    ensure_gitignore_allows_cursor(actions, project_dir)

    # Optional: install packs
    install_packs = [p for p in (args.install_packs or []) if p.strip()]
    enable_packs = [p for p in (args.enable_packs or []) if p.strip()]
    if install_packs:
        install_script = Path(__file__).with_name("install_cursor_packs.py")
        if not install_script.exists():
            raise SystemExit(
                "install_cursor_packs.py not found next to bootstrap-project.py. "
                "Expected: .cursor/helpers/install_cursor_packs.py"
            )

        cmd = [
            sys.executable,
            str(install_script),
            "--target",
            str(project_dir),
            "--packs",
            *install_packs,
        ]
        if enable_packs:
            cmd += ["--enable", *enable_packs]

        actions.append(Action(description=f"Install Cursor rule packs: {', '.join(install_packs)}", command=cmd))

    # Print plan
    print(f"Project: {project_dir}")
    print("Mode:", "APPLY" if args.apply else "DRY RUN")
    if not actions:
        print("Nothing to do.")
        return 0

    for a in actions:
        if a.command:
            print("-", a.description, ":", " ".join(a.command))
        elif a.path:
            print("-", a.description)

    if not args.apply:
        if install_packs:
            print(INSTALL_PACKS_HELP)
        print("\nRe-run with --apply to make changes.")
        return 0

    # Apply
    for a in actions:
        if a.command:
            run(a.command, cwd=project_dir)
        elif a.path:
            # Directories: write_text is None. Files: write_text is not None.
            if a.write_text is None:
                a.path.mkdir(parents=True, exist_ok=True)
            else:
                a.path.parent.mkdir(parents=True, exist_ok=True)
                a.path.write_text(a.write_text, encoding="utf-8")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}", file=sys.stderr)
        returncode = e.returncode or 1
        raise SystemExit(returncode)

