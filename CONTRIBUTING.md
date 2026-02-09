# Contributing

Thanks for taking a look.

## Scope

This repo is a **source-of-truth** for:

- small, opt-in Cursor rule packs under `.cursor/packs/`
- helpers under `.cursor/helpers/` that bootstrap a repo or install packs

## Guidelines

- Keep packs **small** and **opt-in** (prefer `alwaysApply: false` unless there’s a strong reason).
- Avoid repo-specific or user-specific references (paths, emails, internal URLs).
- Do not add secrets (tokens, API keys, private keys, `.env` files).
- Keep rules and docs concise and copy/paste-friendly.

## Making changes

- Add or update packs in `.cursor/packs/<pack-name>/`
- Update docs in `README.md` (repo-level) and `.cursor/packs/README.md` (pack index)
- If you add a helper, document it in `.cursor/helpers/README.md`

