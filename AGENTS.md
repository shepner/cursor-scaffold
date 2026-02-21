# Cursor agent in this project

This is the **cursor-scaffold** project: **source-of-truth + tooling for Cursor project bootstrapping (packs are opt-in; projects stay clean)**.

## How the agent should work

- Keep Cursor-for-Cursor artifacts under `.cursor/` (rules, skills, notes, helpers, agents).
- Prefer **small, opt-in packs** over large always-on rule sets.
- Treat packs as **source material**; Cursor only executes rules in a repo’s `.cursor/rules/`.
- **Bootstrap sink**: When adding content (anywhere) that would help bootstrap a new computer or project, add or update the corresponding artifact here (notes, packs, helpers). See [.cursor/notes/bootstrap-artifacts-sink.md](.cursor/notes/bootstrap-artifacts-sink.md). The hub enforces this via the rule **update-scaffold-with-bootstrap**.
- **Subagents**: `.cursor/agents/` (project); for global setup see knowledge-hub’s `.cursor/notes/cursor-subagents.md` and `.cursor/agents/` Define as needed (like helpers). Copy to `~/.cursor/agents/` for use across all projects.

## Triggering improvement

Say "Document this workflow", "Take notes and improve", or "Add a rule for X"; the agent will create or update rules, skills, notes, or helpers in this project’s `.cursor/`. (When the hub is in the workspace, it may use the hub’s **document-and-improve-workflows** skill.)

## Current artifacts

- Packs: `.cursor/packs/` (including **agent-behavior** for multi-ask delegation; core, git, docker, docs, quality, security, testing, time)
- Subagents: `.cursor/agents/` (see README there; templates in knowledge-hub)
- Helpers:
  - `.cursor/helpers/bootstrap-project.py` — bootstrap a project (AGENTS.md, .cursor/, git)
  - `.cursor/helpers/install_cursor_packs.py` — install packs into a target repo
  - `.cursor/helpers/prepare-project-for-hub.sh` — run bootstrap and show hub-import next steps
- Notes:
  - `.cursor/notes/bootstrap-new-machine.md` — set up a new computer (layout, clone hub + scaffold, open workspace)
  - `.cursor/notes/importing-projects.md` — import existing projects into the hub structure (placement, bootstrap, optional workspace roots)
  - `.cursor/notes/external-context-for-projects.md` — pattern for giving projects access to context in another repo (infra, shared docs); summary + optional workspace variant
  - `.cursor/notes/bootstrap-artifacts-sink.md` — scaffold is the place for bootstrap-useful content; when adding such content elsewhere, add it here too (hub rule: update-scaffold-with-bootstrap)
  - `.cursor/notes/creating-project-from-idea.md` — when creating a project from an idea in another root: don't edit that root; keep project self-contained; no cross-project links
  - `.cursor/notes/multi-ask-and-subagent-delegation.md` — recognize multiple independent asks; delegate to subagents when appropriate; summarize afterward (hub has full rule; install `agent-behavior` pack for rule)
  - `.cursor/notes/user-preferences-and-seamless-extension.md` — pattern for operating as seamless extension, learning from user patterns, evolving with needs (hub has instance)
  - `.cursor/notes/project-folded-or-superseded.md` — when a project is retired (tool decision or folded into another); update PROJECTS.md (hub has full note)
- Rule: `.cursor/rules/self-document-workflows.mdc`

