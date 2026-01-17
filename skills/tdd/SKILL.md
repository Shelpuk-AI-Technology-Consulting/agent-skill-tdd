---
name: tdd
description: Use for every coding task. Enforce strict TDD workflow: activate Serena, investigate first, clarify+confirm requirements, write REQUIREMENTS.md (As Is/To Be/Requirements+AC/Testing Plan/Implementation Plan), verify APIs via web search, then implement in tiny test-verified steps.
metadata:
  short-description: Always-on TDD workflow + requirements discipline.
---

## Working Agreement

This skill is intentionally **always-on** for coding tasks. Follow it exactly unless the user explicitly opts out.

### Non-negotiables

1. **Serena first**: Start by activating the Serena project (if the Serena tools exist in the environment). If activation fails for reasons outside your control, continue without Serena and say why.
2. **Investigate before changing anything**: Understand the current state (application state, execution results, user input, logs) before proposing edits.
3. **No requirement changes without confirmation**: If requirements are unclear, ask clarifying questions. Before you change/add/interpret requirements, get explicit confirmation.
4. **Write `REQUIREMENTS.md` before implementation**:
   - If `REQUIREMENTS.md` exists, ask for confirmation before overwriting and keep a backup copy when overwriting.
   - Use the mandated structure (below).
5. **Use up-to-date docs**: When you rely on an API/package/technology detail, use Kindly Web Search (if available) to confirm signatures, version behavior, breaking changes, and deprecations.
6. **Smallest possible steps (TDD)**: Implement one small change at a time and test each change (unit → integration → smoke as appropriate) before proceeding.

## `REQUIREMENTS.md` Structure (Mandated)

Write/overwrite `REQUIREMENTS.md` in the target repository root with:

1. **As Is**: current behavior/state (what exists today).
2. **To Be**: desired behavior/state after the change.
3. **Requirements**: functional requirements (numbered).
4. **Acceptance Criteria**: for every functional requirement, add explicit acceptance criteria.
5. **Testing Plan**: test strategy + cases (TDD best practices).
6. **Implementation Plan**: the smallest sequential code changes; for each change, include how you’ll test it.

## Workflow (Step-by-step)

### 1) Investigate

- Inspect the repository structure, relevant code paths, current behavior, and existing tests.
- Run the smallest commands needed to confirm the current state (build/test, smoke, reproducer), when applicable.
- Summarize findings briefly.

### 2) Clarify + confirm requirements

- Ask clarifying questions where anything is ambiguous (scope, UX, edge cases, compatibility, performance).
- Propose the requirements in concrete, testable language.
- Ask for explicit confirmation before finalizing requirements or changing them.

### 3) Create/overwrite `REQUIREMENTS.md`

- Write `REQUIREMENTS.md` using the mandated structure.
- Ensure every functional requirement has acceptance criteria.
- Add a Testing Plan and an Implementation Plan with the smallest steps.

### 4) Validate assumptions

- Use Kindly Web Search to verify any API or dependency assumptions.
- Update `REQUIREMENTS.md` if assumptions change (and re-confirm requirements when needed).

### 5) Optional review (PAL MCP)

- When available and useful, ask `moonshotai/kimi-k2-thinking` (via PAL MCP) to review `REQUIREMENTS.md` and later the code for corner cases, failure modes, and inconsistencies.
- Consider feedback critically; apply only what improves correctness/scope-fit.

### 6) Implement with TDD

- Follow the Implementation Plan in order.
- After each step: run the smallest relevant tests first; expand to broader tests when confidence is needed.
- Keep diffs minimal and focused; avoid unrelated refactors.

## Serena memories (when supported)

When Serena memory tools are available, store important information as short memories:

- `project_overview.md`: what the repo is, key architectural facts.
- `suggested_commands.md`: build/test/lint/smoke commands.
- `style_and_conventions.md`: coding conventions, patterns, gotchas.
- `bugs.md`: notable bugs + fixes (date, cause, prevention) when applicable.

