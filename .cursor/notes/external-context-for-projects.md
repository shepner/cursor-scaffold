# External context for projects (infra, shared docs, other repos)

Many projects depend on **knowledge that lives elsewhere** — an infra repo, a design system, shared docs, or operational runbooks. Cursor only has "knowledge about" content that’s inside a workspace root it indexes. This note describes a reusable pattern to give projects access to that context in an ongoing way.

## The pattern

1. **Single always-indexed summary**  
   Keep a short overview (topology, key locations, pointers) in a root that’s already in the workspace (e.g. the hub’s `.cursor/notes/` or a small "context" repo). Fill in anything that *doesn’t* live in the external repo. Then any project opened in that workspace gets baseline context without adding the other repo.

2. **Optional full-context workspace**  
   When a project needs *full* depth (configs, scripts, full docs), use a **workspace variant** that adds the external repo as an extra root. Open that variant when working on context-heavy tasks; use the normal workspace when the summary is enough.

3. **Optional sync**  
   If you don’t want the full repo as a root (size, noise), a script can copy or symlink selected files from the external repo into an always-indexed folder. Run after the external repo updates.

## When to use it

- **Infra / network**: Projects need to know how the local network, Proxmox, Docker, or NAS are set up → summary in hub (or similar) + optional workspace that includes the infra repo.
- **Design system / shared UI**: Projects need component or token docs → summary + optional root for the design repo.
- **Runbooks / ops**: Projects need to call APIs or follow procedures documented elsewhere → summary or synced excerpts in an indexed location.

## Implementation checklist (generic)

- [ ] Identify the "external" repo(s) and what’s missing from them (if anything).
- [ ] Add one or more summary docs in an already-indexed root (overview + "not in the repo" items).
- [ ] If full depth is needed sometimes: create a workspace variant that adds the external repo as a root; use it when working on context-dependent projects.
- [ ] Optionally: add a helper that syncs key files from the external repo into the indexed summary area.

## Example: knowledge hub

The knowledge hub implements this for **local network/infra** and the **asyla** project:

- Hub has `.cursor/notes/local-network-knowledge.md` (strategy) and `local-network-overview.md` (summary + "not in asyla" content).
- Workspace `knowledge-hub.personal+infra.code-workspace` adds the asyla repo as a root for sessions that need full infra context.
- See the hub’s note for the concrete setup; this scaffold note is the generic pattern.
