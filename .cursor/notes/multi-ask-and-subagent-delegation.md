# Multi-ask detection and subagent delegation

When the user gives **multiple independent, likely unrelated asks** in one message, consider splitting work and delegating to subagents to parallelize and speed things up.

## Pattern

1. **Identify discrete asks** — e.g. "do X, Y, and Z" where each can be done independently.
2. **Match to subagents** — Verifier, debugger, test-runner, cross-root-editor, documenter. Delegate when a subagent's description fits.
3. **Parallel when possible** — Don't serialize independent work.
4. **Summarize afterward** — Always give the user a concise summary of what was delegated, key results, and follow-up.

## When not to delegate

- Single cohesive task
- Dependent tasks (Y needs X's output)
- No matching subagent (do the work in main agent; consider adding a subagent if the pattern repeats)

## How to adopt

- **Install the pack**: `python3 .cursor/helpers/install_cursor_packs.py --target /path/to/repo --packs agent-behavior` (optionally `--enable agent-behavior` for always-on).
- **Knowledge hub**: Has the full rule at `.cursor/rules/multi-ask-and-subagent-delegation.mdc` (always-on). Projects in the hub workspace inherit this behavior.
