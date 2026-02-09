# Cursor helpers (cursor-scaffold)

Runnable scripts for applying cursor-scaffold to projects.

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

