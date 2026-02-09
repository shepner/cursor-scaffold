# Cursor agent in this project

This is the **cursor-scaffold** project: **source-of-truth + tooling for Cursor project bootstrapping (packs are opt-in; projects stay clean)**.

## How the agent should work

- Keep Cursor-for-Cursor artifacts under `.cursor/` (rules, skills, notes, helpers).
- Prefer **small, opt-in packs** over large always-on rule sets.
- Treat packs as **source material**; Cursor only executes rules in a repo’s `.cursor/rules/`.

## Current artifacts

- Packs: `.cursor/packs/`
- Helpers:
  - `.cursor/helpers/bootstrap-project.py` — bootstrap a project (AGENTS.md, .cursor/, git)
  - `.cursor/helpers/install_cursor_packs.py` — install packs into a target repo
  - `.cursor/helpers/prepare-project-for-hub.sh` — run bootstrap and show hub-import next steps
- Notes:
  - `.cursor/notes/bootstrap-new-machine.md` — set up a new computer (layout, clone hub + scaffold, open workspace)
  - `.cursor/notes/importing-projects.md` — import existing projects into the hub structure (placement, bootstrap, optional workspace roots)
- Rule: `.cursor/rules/self-document-workflows.mdc`

