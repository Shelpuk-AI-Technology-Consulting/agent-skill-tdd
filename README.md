# agent-skill-tdd

This repository contains an Agent Skill named `tdd` (stored under `skills/tdd/`) to replace repeated per-project `AGENTS.md` boilerplate with a consistent TDD + requirements workflow.

## Install

### skill-installer

Use `skill-installer` when you want to install directly from GitHub instead of copying/symlinking files. This uses the built-in Codex system skill (`skill-installer`) and its helper script.

Primary (recommended, branch-agnostic):

- `python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Shelpuk-AI-Technology-Consulting/agent-skill-tdd --path skills/tdd`

Alternative (explicit branch/path URL):

- `$skill-installer install https://github.com/Shelpuk-AI-Technology-Consulting/agent-skill-tdd/tree/main/skills/tdd` (replace `main` with another ref if needed)

Troubleshooting:

- A bare repo URL (for example `https://github.com/Shelpuk-AI-Technology-Consulting/agent-skill-tdd`) fails with `Missing --path for GitHub URL.` because the skill directory is not specified.
- Use one of the path-aware forms above (`--repo ... --path skills/tdd` or `/tree/<ref>/skills/tdd`).

Restart Codex after installing skills. Claude Code loads/updates skills automatically when they change.

### Codex (recommended)

Codex discovers skills from `.codex/skills/` (repo-scoped) and `~/.codex/skills/` (user-scoped). To install this skill, copy or symlink `skills/tdd` into one of those locations.

User-scoped (all repos):

- `mkdir -p ~/.codex/skills`
- `ln -s "$(pwd)/skills/tdd" ~/.codex/skills/tdd` (or `cp -R skills/tdd ~/.codex/skills/tdd`)

Repo-scoped (shared in a target repo):

- `mkdir -p <target-repo>/.codex/skills`
- `ln -s "$(pwd)/skills/tdd" <target-repo>/.codex/skills/tdd` (or `cp -R skills/tdd <target-repo>/.codex/skills/tdd`)

Restart Codex after installing skills. To verify in Codex CLI, use `/skills` (or type `$` to select a skill).

#### Troubleshooting (Codex)

If Codex reports `invalid YAML: mapping values are not allowed in this context` for `SKILL.md`, the YAML frontmatter is not valid. A common cause is an unquoted `description:` value containing `: ` (e.g., `workflow: activate`). Fix by quoting the value:

- `description: "… workflow: activate …"`

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
