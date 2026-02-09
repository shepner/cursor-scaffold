# Bootstrap a new computer for the knowledge-hub methodology

This note describes how to set up a new machine so you can use the **knowledge hub** (multi-root Cursor workspace, “knowledge about” indexing, project-in-hub workflow) and **cursor-scaffold** (project bootstrapping, rule packs).

## Prerequisites

- **Cursor** installed ([cursor.com](https://cursor.com))
- **Git** installed
- (Optional) Access to your existing knowledge-hub and related repos (e.g. via clone, sync, or fresh setup)

## Target directory layout

The methodology assumes a consistent layout so workspace files can use relative paths. Typical choice (adjust to taste):

```
~/local/                          # or /path/to/workspace-root
├── knowledge-hub/                 # hub repo: workspace file + .cursor/ + AGENTS.md
│   ├── knowledge-hub.code-workspace
│   ├── _workspaces/               # scoped workspace entrypoints
│   └── .cursor/
├── cursor-scaffold/               # this repo: packs + bootstrap/install helpers
├── ObsidianLibrary/
│   └── Personal Library/         # vault (if you use one)
├── email-archive/                 # if you use getmail6/Maildir pipeline
├── personal/                      # container for personal project repos
│   └── projects/                 # or flat list of repos here
└── work/                          # container for work project repos
    └── projects/
```

Not every root is required: start with **knowledge-hub** and **cursor-scaffold**; add vault, email-archive, personal, work as you need them.

## Step 1: Create the parent directory

```bash
mkdir -p ~/local
cd ~/local
```

(Use any path you prefer; substitute it in steps below.)

## Step 2: Clone knowledge-hub and cursor-scaffold

```bash
cd ~/local
git clone <your-knowledge-hub-repo-url> knowledge-hub
git clone <your-cursor-scaffold-repo-url> cursor-scaffold
```

If you don’t have a remote for knowledge-hub yet, you can create the directory and init git; then add the workspace file and hub content (see knowledge-hub’s AGENTS.md and `.cursor/notes/knowledge-hub-architecture.md` for what the hub contains).

## Step 3: Clone or create other roots

- **Vault**: Clone or sync your Obsidian vault into e.g. `~/local/ObsidianLibrary/Personal Library/`.
- **Email archive**: Clone or create `email-archive` (scripts, config, docs); see that repo’s README.
- **Containers**: Create empty containers so the hub workspace can reference them:
  ```bash
  mkdir -p ~/local/personal ~/local/work
  ```
  Add a minimal `AGENTS.md` (and optionally `.gitignore`) if you track them in git. The knowledge-hub’s personal/work roots point at these; projects live inside them (e.g. `personal/projects/MyApp`).

## Step 4: Open the hub in Cursor

Open the **canonical workspace file**:

```bash
cursor ~/local/knowledge-hub/knowledge-hub.code-workspace
```

Or from Cursor: **File → Open Workspace from File…** and choose `knowledge-hub.code-workspace`.

If some roots are missing (e.g. vault not cloned yet), Cursor may show warnings for those folders; you can remove those roots from the workspace JSON until the paths exist, or add them once the dirs are in place.

## Step 5: Verify workspace roots

In the hub repo, `knowledge-hub.code-workspace` lists all roots with relative paths (e.g. `"path": "../cursor-scaffold"`). Ensure each path resolves from the hub directory:

- Hub: `"."`
- cursor-scaffold: `"../cursor-scaffold"`
- Personal Library: `"../ObsidianLibrary/Personal Library"`
- personal: `"../personal"`
- work: `"../work"`
- etc.

Adjust path names to match your layout (see hub’s AGENTS.md workspace roots table).

## Step 6: Use scoped workspaces (optional)

For focused work, use the hub’s scoped workspace files under `knowledge-hub/_workspaces/`, e.g.:

- `knowledge-hub.personal.code-workspace` — hub + vault + email + personal
- `knowledge-hub.work.code-workspace` — hub + work
- `knowledge-hub.scaffold.code-workspace` — hub + cursor-scaffold

Open the one that matches what you’re doing.

## One-time per-machine notes

- **Cursor MCP**: If you use MCP servers (e.g. NAS, APIs), configure them in `~/.cursor/mcp.json`; they apply to every Cursor window.
- **Git**: Set `user.name` and `user.email` if not already set.
- **cursor-scaffold**: No install step; use the repo’s helpers by path, e.g.  
  `python3 ~/local/cursor-scaffold/.cursor/helpers/bootstrap-project.py /path/to/project --apply`

## Summary

1. Create parent dir (e.g. `~/local`).
2. Clone knowledge-hub and cursor-scaffold.
3. Clone or create vault, email-archive, personal, work as needed.
4. Open `knowledge-hub.code-workspace` in Cursor.
5. Optionally use `_workspaces/*.code-workspace` for focused contexts.

After that, use cursor-scaffold to **bootstrap and import projects** (see [importing-projects.md](importing-projects.md)).
