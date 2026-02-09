# cursor-scaffold — design note

**Source-of-truth + tooling for Cursor project bootstrapping (packs are opt-in; projects stay clean).**

## Why this exists

A “global rules repo” tends to degrade:

- too many always-on rules → noise and conflicts
- complex rule DSLs → hard to maintain, low leverage
- manual copying → friction, so the system languishes

cursor-scaffold keeps the value (central curation) while fixing the execution model:

- keep packs as **source material** (`.cursor/packs/`)
- install only what a project needs into `.cursor/rules/`
- default installs are **disabled-by-default** (`alwaysApply: false`)

## Minimal workflow

1. Bootstrap a project with `.cursor/` + `AGENTS.md`
2. Install 1–3 packs relevant to that repo
3. Enable rules only when they demonstrably help

