# Cursor helpers (cursor-scaffold)

Runnable scripts for applying cursor-scaffold to projects.

## New machine and importing projects

- **Bootstrap a new computer**: see [.cursor/notes/bootstrap-new-machine.md](../notes/bootstrap-new-machine.md) for full setup (clone hub + cursor-scaffold, layout, open workspace).
- **Import an existing project** into the hub structure: see [.cursor/notes/importing-projects.md](../notes/importing-projects.md). Then run `bootstrap-project.py` (or use `prepare-project-for-hub.sh` below) on the project path.

## prepare-project-for-hub.sh

Convenience wrapper to prepare one project for the hub: runs bootstrap and prints next steps.

```bash
./.cursor/helpers/prepare-project-for-hub.sh /path/to/project --apply
./.cursor/helpers/prepare-project-for-hub.sh /path/to/project --install-packs core git --apply
```

Without `--apply`, shows a dry run. All extra args are passed to `bootstrap-project.py`.

## bootstrap-project.py

Bootstrap a project directory so Cursor can “document and learn” consistently:

- ensures a local git repo exists (even without a remote)
- creates `AGENTS.md` if missing
- creates `.cursor/` skeleton and `self-document-workflows` rule if missing
- can optionally install cursor-scaffold rule packs into the target repo

Run (dry-run by default):

```bash
python3 .cursor/helpers/bootstrap-project.py /path/to/project
python3 .cursor/helpers/bootstrap-project.py /path/to/project --apply
```

Optional packs:

```bash
python3 .cursor/helpers/bootstrap-project.py /path/to/project \
  --install-packs core git security
python3 .cursor/helpers/bootstrap-project.py /path/to/project \
  --install-packs core git \
  --enable-packs core \
  --apply
```

## install_cursor_packs.py

Install curated cursor-scaffold packs from `.cursor/packs/` into a target repo’s `.cursor/rules/`.

```bash
python3 .cursor/helpers/install_cursor_packs.py \
  --target "/path/to/repo" \
  --packs core git security
```

