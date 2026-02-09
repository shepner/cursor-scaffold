# Legacy `cursor-rules` salvage (into cursor-scaffold)

This note captures what we salvaged from the old `/Users/shepner/local/cursor-rules` rule library and how it was translated into **cursor-scaffold**.

## What we salvaged (principles → packs)

We intentionally **did not copy** the legacy DSL (`<rule>...</rule>`) or the duplicated/empty frontmatter patterns. We extracted only the durable ideas and rewrote them as short, opt-in pack rules (default `alwaysApply: false`).

### Error handling

- **Legacy source**: `cursor-rules/cursor-rules/.cursor/rules/code-error-handling.mdc`
- **cursor-scaffold**: `.cursor/packs/quality/quality-error-handling.mdc`
- **Kept**: specific exceptions, preserve context, cleanup, actionable errors

### Logging

- **Legacy source**: `cursor-rules/cursor-rules/.cursor/rules/code-logging.mdc`
- **cursor-scaffold**: `.cursor/packs/quality/quality-logging.mdc`
- **Kept**: level discipline, context, structure, avoid secrets, avoid noisy hot-loop logs

### Standard library first

- **Legacy source**: `cursor-rules/cursor-rules/.cursor/rules/code-stdlib-first.mdc`
- **cursor-scaffold**: `.cursor/packs/quality/quality-stdlib-first.mdc`
- **Kept**: dependency discipline + justification; removed questionable “always use X instead of Y” recommendations

### Testing standards

- **Legacy source**: `cursor-rules/cursor-rules/.cursor/rules/code-testing.mdc`
- **cursor-scaffold**: `.cursor/packs/testing/testing-basics.mdc`
- **Kept**: AAA, edge cases, determinism, isolation, naming for intent

### Timestamps + durations

- **Legacy source**: `cursor-rules/cursor-rules/.cursor/rules/code-timestamp-handling.mdc`
- **cursor-scaffold**: `.cursor/packs/time/time-timestamps-and-durations.mdc`
- **Kept**: explicit timezone, UTC at rest, ISO 8601 / documented units, validate config durations
- **Dropped**: pandas/BigQuery-specific conversion recipes (too implementation-specific for a general pack)

### Docker optimization/log viewing

- **Legacy sources**:
  - `cursor-rules/cursor-rules/.cursor/rules/docker-optimization.mdc`
  - `cursor-rules/cursor-rules/.cursor/rules/docker-logging.mdc`
- **cursor-scaffold**: `.cursor/packs/docker/docker-basics.mdc`
- **Kept**: multi-stage builds, caching order, minimal layers, `.dockerignore`, non-root, bounded log viewing

## What we did *not* salvage (and why)

- **Rule enforcement / validation DSL** (`cursor-rule-*` rules): over-engineered and not aligned with how Cursor rules are actually effective today.
- **BigQuery/pandas-specific “data types / schema management”**: valuable in a domain repo, but too specific for a general scaffold. Consider adding a dedicated pack later (e.g. `bigquery/`) if you find repeated reuse.
- **Mass `alwaysApply: true`**: this was a core failure mode; cursor-scaffold defaults to opt-in.

