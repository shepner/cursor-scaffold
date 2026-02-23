# cursor-scaffold as the bootstrap-artifacts sink

**cursor-scaffold** is the place for anything that would be useful for **bootstrapping a new computer** or **bootstrapping/importing a new project**. When you add or improve such content elsewhere (e.g. in the knowledge hub), also add or update the corresponding artifact here so future setups benefit.

## What “bootstrap” covers

- **New computer**: Directory layout, clone order, opening the hub workspace, MCP/config, one-time per-machine steps. See [bootstrap-new-machine.md](bootstrap-new-machine.md).
- **New or imported project**: AGENTS.md, .cursor/ kit, git, optional packs, placement under personal/work. See [importing-projects.md](importing-projects.md) and helpers (e.g. `bootstrap-project.py`, `install_cursor_packs.py`).
- **Reusable patterns**: Any pattern that helps any new machine or project (e.g. external context for projects, rule packs). Add as notes in `.cursor/notes/` or as packs in `.cursor/packs/`.

## Convention (hub rule)

The knowledge hub has a rule **update-scaffold-with-bootstrap**: when adding content that helps bootstrap a machine or project, the agent must also add or update cursor-scaffold. That keeps scaffold the single source of truth for bootstrap and ensures a fresh clone of hub + scaffold has everything needed.

## Where to put things in scaffold

| Kind | Location | Example |
|------|----------|---------|
| New-machine steps / layout | `.cursor/notes/bootstrap-new-machine.md` or new note | MCP, Cursor settings |
| Project import / bootstrap steps | `.cursor/notes/importing-projects.md`, `.cursor/helpers/` | bootstrap-project.py |
| Reusable pattern (any context) | `.cursor/notes/*.md` | external-context-for-projects.md, user-preferences-and-seamless-extension.md, multi-ask-and-subagent-delegation.md, learn-from-mistakes.md |
| Optional project rules | `.cursor/packs/<name>/` | core, git, docker, docs, agent-behavior |
| Scripts for bootstrap or install | `.cursor/helpers/` | install_cursor_packs.py, prepare-project-for-hub.sh |

Always update **AGENTS.md** when you add a new note, pack, or helper.
