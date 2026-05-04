# Learn from mistakes

When the agent (or user) identifies a mistake, the agent should:

1. **What went wrong** — State the incorrect action/assumption explicitly.
2. **Why it went wrong** — One-sentence root cause (missed rule, wrong context, wrong tool).
3. **Codify** — Add or update a rule, note, AGENTS.md bullet, or skill so the same mistake never recurs.

**Trust but verify** — The pack rule also asks you to confirm factual claims against primary evidence (files, logs, APIs, CI), not only human or tool assertions, before relying on them.

This is available as a rule in the **agent-behavior** pack: `learn-from-mistakes.mdc`. Install with:

```bash
python3 .cursor/helpers/install_cursor_packs.py --target /path/to/repo --packs agent-behavior
```

Use `--enable agent-behavior` if you want this rule to apply always in that repo. In knowledge-hub the rule is always-on; in scaffold it is opt-in via the pack.

## Relation to other workflows

- **document-and-improve-workflows**: General "document this" / "take notes and improve" — user- or completion-triggered. Learn-from-mistakes is **error- or correction-triggered** and always includes root-cause analysis.
- **continual-learning** (transcript mining): Extracts preferences/facts from past chats into AGENTS.md. Learn-from-mistakes is **in-session**: as soon as a mistake is identified, codify it so the current and future sessions don't repeat it.
