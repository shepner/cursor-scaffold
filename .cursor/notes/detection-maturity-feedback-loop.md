# Detection maturity: scripted detection + manual review feedback loop

## Principle

Automated detection (regex, pattern matching) is the fast/cheap first pass that catches known patterns. But it's inherently fragile with arbitrary input. The solution is not to make regex perfect upfront — it's to combine it with manual review in a **positive feedback loop**:

1. Scripted detection catches known patterns (fast, cheap)
2. Logs contain enough detail for a reviewer to diagnose mismatches
3. Manual review catches what scripts missed
4. Scripts are updated with new patterns + test cases
5. Repeat → operational maturity improves over time

Each iteration makes the scripts better. Manual review catches fewer novel issues because the scripts absorb them. This is the concrete mechanism for moving from ad-hoc to continuously improving (Maturity framework progression).

## Rules for the agent

1. **Regex first**: fast/cheap first pass for all known patterns.
2. **Don't try to make regex perfect upfront**: novel patterns will be missed. That's expected.
3. **Log for reviewability**: when detection fails, ensure logs contain enough extracted detail for diagnosis.
4. **Close the loop**: when a mismatch is found, update scripts + add test case + commit.
5. **Measure the trend**: fewer misclassifications over time = feedback loop is working.

See the hub's `.cursor/notes/detection-maturity-feedback-loop.md` for the full version with framework connections.
