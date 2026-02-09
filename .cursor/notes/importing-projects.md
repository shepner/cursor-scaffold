# Importing projects into the knowledge-hub structure

How to bring an existing project (already on this machine or cloned from elsewhere) into the hub’s methodology so Cursor can index it and follow project conventions.

## Where projects live

In the typical layout, projects sit inside **container** roots that are already in the workspace:

- **Personal projects**: e.g. `~/local/personal/projects/MyApp` or `~/local/personal/MyApp`
- **Work projects**: e.g. `~/local/work/projects/ClientX` or `~/local/work/ClientX`

Because the workspace has a root for `personal` and `work`, Cursor **already indexes everything under those folders**. You do **not** need to add each project as its own workspace root unless you want a dedicated workspace (e.g. “Hub + this one project”) or a custom sidebar name.

So “importing” means:

1. **Place** the project under the right container (personal or work).
2. **Bootstrap** it so it has `AGENTS.md`, `.cursor/`, and git (if missing).
3. **Optionally** add it as a workspace root or create a scoped workspace that includes it.

## Step 1: Place the project

**Option A — Move or copy into the container**

```bash
# Example: move existing repo into personal projects
mv ~/old-location/MyApp ~/local/personal/projects/MyApp
```

**Option B — Clone into the container**

```bash
mkdir -p ~/local/personal/projects
cd ~/local/personal/projects
git clone <repo-url> MyApp
```

**Option C — Leave in place and add as root**

If you prefer not to move the repo, you can add its current path as a **workspace root** in the hub’s `knowledge-hub.code-workspace`. Then Cursor will index it when that workspace is open. Prefer Option A or B if you want a single “personal” or “work” root that contains many projects.

## Step 2: Bootstrap the project

Every project in the hub should be **Cursor-bootstrapped**: git (initialized), `AGENTS.md`, and `.cursor/` with at least the self-document-workflows rule. Use cursor-scaffold’s helper from the **cursor-scaffold** repo (or from the hub, if the hub has a copy of the helper):

```bash
# From cursor-scaffold repo
python3 /path/to/cursor-scaffold/.cursor/helpers/bootstrap-project.py \
  /path/to/your/project \
  --apply
```

Example:

```bash
python3 ~/local/cursor-scaffold/.cursor/helpers/bootstrap-project.py \
  ~/local/personal/projects/MyApp \
  --apply
```

Optional: install rule packs at bootstrap time:

```bash
python3 ~/local/cursor-scaffold/.cursor/helpers/bootstrap-project.py \
  ~/local/personal/projects/MyApp \
  --install-packs core git \
  --apply
```

If the project already has `.cursor/` or `AGENTS.md`, the bootstrap script skips overwriting them; it only adds what’s missing (e.g. git init, `.cursor/rules/self-document-workflows.mdc`, un-ignore `.cursor` in `.gitignore`).

## Step 3: Optionally add as a workspace root

You only need this if you want the project to appear as its **own root** in the hub workspace (e.g. a named folder in the sidebar) or if the project lives **outside** the personal/work trees.

1. Open `knowledge-hub.code-workspace` (or the scoped workspace under `_workspaces/` you use).
2. Add a folder entry, e.g.:
   ```json
   {"name": "MyApp", "path": "../personal/projects/MyApp"}
   ```
   Use a path **relative to the workspace file’s directory** (usually the hub root).
3. Update the hub’s `AGENTS.md` workspace roots table so the new root is documented.

**Avoid duplication**: If the project is already under `personal` or `work`, it’s already indexed. Adding it again as a separate root will index it twice; prefer not adding a second root unless you have a good reason (e.g. a dedicated “Hub + MyApp” workspace).

## Step 4: Optional — focused workspace for one project

For focused work you can use a **scoped workspace** that includes only the hub and one project:

1. Copy an existing scoped workspace from `knowledge-hub/_workspaces/` (e.g. `knowledge-hub.personal.code-workspace`) to a new file, e.g. `knowledge-hub.myapp.code-workspace`.
2. Add a folder entry for the project (path relative to the workspace file).
3. Open that workspace in Cursor when you want “hub + this project” only.

## Summary

| Goal | Action |
|------|--------|
| Project under personal/work, indexed with everything else | Place repo in container → run bootstrap-project.py |
| Project as its own named root in the hub | Place repo → bootstrap → add folder to workspace JSON + AGENTS.md |
| Focused “hub + one project” window | Create scoped workspace that includes hub + project root |

After importing, use **install_cursor_packs.py** anytime to add or refresh rule packs in that project (see [manage-cursor-rule-packs](../skills/manage-cursor-rule-packs/SKILL.md)).
