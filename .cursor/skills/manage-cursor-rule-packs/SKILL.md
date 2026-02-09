---
name: manage-cursor-rule-packs
description: cursor-scaffold workflow: manage curated Cursor rule packs and install them into projects, without a huge always-on rule set.
---

# cursor-scaffold: manage Cursor rule packs

This repo keeps a curated pack library under `.cursor/packs/` and installs selected packs into target repos.

## Principles

- **Keep packs small and sharp**: high signal, low noise.
- **Prefer opt-in**: install with `alwaysApply: false` unless explicitly enabled.
- **Treat packs as source material**: projects receive copies under their own `.cursor/rules/`.

## Install packs into an existing repo

From `cursor-scaffold/`:

```bash
python3 .cursor/helpers/install_cursor_packs.py \
  --target "/path/to/repo" \
  --packs core git security
```

Enable on install (optional):

```bash
python3 .cursor/helpers/install_cursor_packs.py \
  --target "/path/to/repo" \
  --packs core git \
  --enable core
```

## Bootstrap a repo and install packs

```bash
python3 .cursor/helpers/bootstrap-project.py /path/to/repo \
  --install-packs core git security \
  --apply
```

