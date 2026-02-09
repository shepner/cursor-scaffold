# cursor-scaffold: rule packs

These packs are **source material**. Cursor only executes rules located in a repo’s `.cursor/rules/`, so packs must be **installed (copied)** into a target repo.

Install packs:

```bash
python3 .cursor/helpers/install_cursor_packs.py --target "/path/to/repo" --packs core git security
```

Notes:

- Packs are installed **disabled by default** (`alwaysApply: false`) to keep projects clean.
- Use `--enable <pack>` to flip `alwaysApply: true` for installed rules from that pack.

