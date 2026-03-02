# Scripts-first, LLM-minimal

When working with infrastructure or any repeatable multi-step process, prefer deterministic scripts over ad-hoc LLM-generated commands.

## Why

LLMs are "forgetful" — they improvise commands that may be individually correct but miss established processes, skip steps, or produce inconsistent results across sessions. Scripts are deterministic: if run twice, they produce the same result.

## Pattern

1. **LLM writes scripts** (one-time, reviewed, committed).
2. **Scripts are invoked** — not re-derived as shell commands by the LLM.
3. **Scripts validate preconditions** (services running, directories exist, secrets present).
4. **Scripts are idempotent** where possible (check if work is done, skip safely).

## Anti-patterns

- Multi-step SSH sessions where the LLM types commands one at a time.
- Generating passwords, creating config files, or initializing services via ad-hoc commands.
- Bypassing an established deployment process with "equivalent" commands.

## Oversight

Process violations ("deployment process not followed") are detectable, stoppable errors. If agent roles exist for oversight (QA, SA, Dev Manager), they should catch and halt these immediately — not wait for a human to notice.

Origin: knowledge-hub `.cursor/rules/scripts-first-llm-minimal.mdc`. Install the relevant pack or copy the rule to your project.
