# cursor-scaffold

**Source-of-truth + tooling for Cursor project bootstrapping (packs are opt-in; projects stay clean).**

This repo is the public-safe “scaffolding layer” you can sync across machines:

- curated **rule packs** (small, opt-in)
- helpers to **bootstrap** a project (`AGENTS.md` + `.cursor/` kit)
- helpers to **install packs** into a target repo’s `.cursor/rules/`

## What’s here

- `.cursor/packs/`: curated rule packs (source material)
- `.cursor/helpers/`:
  - `bootstrap-project.py`: create a minimal Cursor-ready project skeleton
  - `install_cursor_packs.py`: copy selected packs into a target repo

## Typical usage

Bootstrap a repo:

```bash
python3 .cursor/helpers/bootstrap-project.py /path/to/repo --apply
```

Install packs into a repo:

```bash
python3 .cursor/helpers/install_cursor_packs.py \
  --target "/path/to/repo" \
  --packs core git security
```

