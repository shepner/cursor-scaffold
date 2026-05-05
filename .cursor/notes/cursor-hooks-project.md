# Cursor project hooks

To version-control Cursor hooks with a repo:

1. Create **`/.cursor/hooks.json`** with `"version": 1` and a `"hooks"` object (see [Hooks | Cursor Docs](https://cursor.com/docs/hooks)).
2. Put scripts under **`/.cursor/hooks/`** and reference them as **`.cursor/hooks/script.sh`** (paths are relative to the **project root**).
3. Mark scripts executable (`chmod +x`).

User-level hooks instead use **`~/.cursor/hooks.json`** and **`~/.cursor/hooks/`** with paths like `./hooks/script.sh`.

If you use the **knowledge-hub** workspace, see that repo’s `.cursor/notes/cursor-hooks.md` for multi-root behavior and `CURSOR_PROJECT_DIR`.
