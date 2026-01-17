# agent-skill-tdd

This repository contains an Agent Skill named `tdd` (stored under `skills/tdd/`) to replace repeated per-project `AGENTS.md` boilerplate with a consistent TDD + requirements workflow.

## Install

### Codex (recommended)

Codex discovers skills from `.codex/skills/` (repo-scoped) and `~/.codex/skills/` (user-scoped). To install this skill, copy or symlink `skills/tdd` into one of those locations.

User-scoped (all repos):

- `mkdir -p ~/.codex/skills`
- `ln -s "$(pwd)/skills/tdd" ~/.codex/skills/tdd` (or `cp -R skills/tdd ~/.codex/skills/tdd`)

Repo-scoped (shared in a target repo):

- `mkdir -p <target-repo>/.codex/skills`
- `ln -s "$(pwd)/skills/tdd" <target-repo>/.codex/skills/tdd` (or `cp -R skills/tdd <target-repo>/.codex/skills/tdd`)

Restart Codex after installing skills. To verify in Codex CLI, use `/skills` (or type `$` to select a skill).

### Claude Code

Claude Code discovers skills from `.claude/skills/` (repo-scoped) and `~/.claude/skills/` (user-scoped). To install this skill, copy or symlink `skills/tdd` into one of those locations.

User-scoped (all repos):

- `mkdir -p ~/.claude/skills`
- `ln -s "$(pwd)/skills/tdd" ~/.claude/skills/tdd` (or `cp -R skills/tdd ~/.claude/skills/tdd`)

Repo-scoped (shared in a target repo):

- `mkdir -p <target-repo>/.claude/skills`
- `ln -s "$(pwd)/skills/tdd" <target-repo>/.claude/skills/tdd` (or `cp -R skills/tdd <target-repo>/.claude/skills/tdd`)

Claude Code loads/updates skills automatically when they change. To verify, ask: `What Skills are available?`

## Validate (this repo)

- Skill frontmatter check: `python3 tools/check_skill_frontmatter.py skills/tdd`
- Unit tests: `python3 -m unittest discover -s tests -p 'test*.py'`
