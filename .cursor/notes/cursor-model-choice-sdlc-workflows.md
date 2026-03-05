# Cursor model choice: multi-model SDLC workflows

Saved from a slide screenshot (Feb 2026) as a quick reference for choosing models in Cursor by workflow stage.
Source image: `/Users/shepner/.cursor/projects/Users-shepner-local-knowledge-hub/assets/image-c57f5aaa-1a20-4a86-87fd-939d444c6fd4.png`

## Research and plan

- Modes: Ask Mode, Plan Mode
- Models:
  - GPT-5.3 (deep investigations)
  - Opus 4.6
  - Composer 1.5 (interactive planning)
- Note: all models in this flow are shown as having Cursor Semantic Search and Instant Grep.

## Execute with fleets of subagents

### Autonomous, large-scale

- Intent: let the agent handle full task execution, testing, and report back for review
- Placement: Cloud
- Models: GPT-5.3, Gemini 3.1 Pro, Opus 4.6

### Speedy and interactive

- Intent: dev-in-the-loop pair programming
- Placement: Local
- Models: Sonnet 4.6, Composer 1.5, Gemini 3 Flash

### Quick fixes

- Intent: run a quick background fix instead of logging a to-do
- Placement: Cloud
- Models: Composer 1.5, Gemini 3 Flash

## Review, debug, and verify

- Modes/tools shown: Agent Mode, Debug Mode, Cursor Bugbot, Agent Review
- Models: GPT-5.3 Codex, Gemini 3.1 Pro

## Practical selection shortcut

- Start in Ask/Plan with GPT-5.3 for high-ambiguity discovery.
- Use autonomous cloud agents for broad, parallel implementation.
- Shift to local interactive models when iterating quickly with tight feedback loops.
- Finish with GPT-5.3 Codex or Gemini 3.1 Pro for review/debug/verification passes.
