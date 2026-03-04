# Log-driven diagnosis

## Principle

When detecting errors or diagnosing failures in automated pipelines, the primary method is **reviewing high-quality, detailed logs against the reported outcome**.

### Mid-level: verify outcome against evidence

- Logs must have a **high signal-to-noise ratio**: structured, timestamped, relevant context.
- When an outcome is reported, **read the actual logs** and verify whether the evidence supports that conclusion.
- If evidence contradicts the outcome, the detection logic is wrong — fix it, don't suppress evidence.

### Senior-level: read between the lines

- What logs *don't* say tells you what *didn't* happen.
- Missing events, timing gaps, unexpected ordering, and absent-but-expected output are all signals.
- When explicit content doesn't explain the failure, ask: what *should* be here but isn't?

## How this applies to the agent

1. **Don't trust labels** — read the actual output/logs first.
2. **Check evidence quality** — if logs lack diagnostic detail, add events/context before chasing the symptom.
3. **Look for what's missing** — absence of expected events is a finding.
4. **Improve signal-to-noise** — log what helps diagnosis, skip what dilutes it.

See the hub's `.cursor/notes/log-driven-diagnosis.md` for the full version with concrete examples.
