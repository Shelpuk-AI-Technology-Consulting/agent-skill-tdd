# Improve AI-generated code quality by 20%

TDD Skill is a part of the **[Shelpuk AI Technology Consulting](https://shelpuk.com) agentic suite** – a set of tools that together improve the code quality produced by AI coding agents by **15–20%**. [Read more on Claude Code generation quality improvement](https://shelpuk.com/en/blog/how-to-increase-claude-code-generation-quality-by-20-percent/).

Works with **Claude Code**, **Codex**, **Antigravity**, **Cursor**, **Windsurf**, and any agent that supports skills or MCP servers.

| Component | Role |
|---|---|
| **tdd** ← you are here | Enforces TDD, requirements discipline, and peer review for every coding task |
| [Serena](https://github.com/oraios/serena) | Semantic code navigation + persistent project memory |
| [Kindly Web Search](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) | Up-to-date API and package documentation via web search |
| [Lad MCP Server](https://github.com/Shelpuk-AI-Technology-Consulting/lad_mcp_server) | Project-aware AI design and code review |

If you like what we're building, please ⭐ **star this repo** – it's a huge motivation for us to keep going!

## How to use the suite

**1. Install three MCP servers and one skill:**

- [Serena](https://github.com/oraios/serena)
- [Kindly Web Search](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server)
- [Lad MCP Server](https://github.com/Shelpuk-AI-Technology-Consulting/lad_mcp_server)
- [tdd](https://github.com/Shelpuk-AI-Technology-Consulting/agent-skill-tdd)

**2. Use the skill when requesting a feature:**

Prompt your favorite AI coding agent (Claude Code, Codex, Cursor, etc.) as usual. Then just add `Follow $tdd` in the end.

```
> Build [your feature description]. Follow $tdd.
```

# TDD Skill

## Why enforce TDD with a skill?

Picture this: Your AI coding agent just finished a new feature. The code looks clean, the agent is confident – but there's no record of what the feature was supposed to do, the edge cases were never discussed, and when you ask the agent about its design decisions next week, it has no idea what you're referring to. A month later you discover it silently broke an integration that was agreed on in a conversation the agent never saw.

This isn't a bug in the code. It's a bug in the **process**.

### The "No Process" Problem

AI coding agents are stateless by default. Each session starts fresh. Without a structured workflow, even the best models routinely:

- Jump straight to implementation without understanding requirements
- Skip tests or write them after the fact as an afterthought
- Make design decisions without checking current API documentation
- Review their own code and miss "bad token" self-reinforcing mistakes
- Lose all decisions and reasoning the moment the session ends

The result? Technically coherent code that solves the wrong problem – and no paper trail to figure out how you got there.

### What This Skill Does Differently

We built this skill at [Shelpuk AI Technology Consulting](https://shelpuk.com) because we needed our AI coding agents to work the way **disciplined engineers** work: clarify before building, document before coding, test before shipping, and get a second opinion before merging.

✅ **Investigate first, code second** – agents understand the current state before proposing any changes

✅ **Explicit requirements confirmation** – no requirement changes without human sign-off, no silent interpretation

✅ **Per-task requirements history** – each task gets its own `.requirements/<datetime>_<feature_name>/REQUIREMENTS.md` with *As Is / To Be / Requirements / Acceptance Criteria / Testing Plan / Implementation Plan*; nothing is ever overwritten

✅ **Validated assumptions** – agents use [Kindly Web Search](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) to confirm API signatures, breaking changes, and deprecations before implementing

✅ **Design review before code** – architectural proposals go through [Lad MCP Server](https://github.com/Shelpuk-AI-Technology-Consulting/lad_mcp_server) `system_design_review` before a line is written

✅ **Strict TDD in the smallest possible steps** – tests first, implementation second, then Lad `code_review` on every change

✅ **Project memory via Serena** – design decisions, debug findings, and conventions are stored in [Serena](https://github.com/oraios/serena) memories and survive across sessions and team members

If you find this useful, please drop us a star ⭐ – it's huge motivation for us to keep improving it!

## How It Works

The `tdd` skill is a `SKILL.md` file that Codex and Claude Code discover automatically from `~/.codex/skills/tdd/` or `~/.claude/skills/tdd/`. When active, it instructs the agent to follow a 6-step workflow for every coding task:

1. **Activate Serena** – for semantic code navigation and persistent project memory
2. **Investigate** – understand the current state before proposing any changes
3. **Clarify + confirm requirements** – ask questions, propose concrete testable requirements, get explicit confirmation
4. **Write `REQUIREMENTS.md`** – create `.requirements/<YYYYMMDDTHHMMSSZ>_<feature_name>/REQUIREMENTS.md` before any implementation begins
5. **Review design with Lad** – run the requirements and system design through `system_design_review`, iterate until feedback runs dry
6. **Implement with TDD, reviewed by Lad** – write tests first, implement, run tests, run `code_review` on each change, iterate

## Skill Suite

This skill is part of a suite designed to work together:

| Tool | Role |
|---|---|
| [Serena](https://github.com/oraios/serena) | Semantic code navigation + persistent project memory |
| [Kindly Web Search](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) | Up-to-date API/package documentation via web search |
| [Lad MCP Server](https://github.com/Shelpuk-AI-Technology-Consulting/lad_mcp_server) | Project-aware AI code and design review |

## Install

### skill-installer (recommended for Codex)

Use `skill-installer` to pull directly from GitHub without copying or symlinking files manually. This uses the built-in Codex system skill (`skill-installer`) and its helper script.

Primary (recommended, branch-agnostic):

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Shelpuk-AI-Technology-Consulting/agent-skill-tdd --path skills/tdd
```

Alternative (explicit branch/path URL):

```
$skill-installer install https://github.com/Shelpuk-AI-Technology-Consulting/agent-skill-tdd/tree/main/skills/tdd
```

(Replace `main` with another ref if needed.)

> **Troubleshooting:** A bare repo URL (e.g. `https://github.com/Shelpuk-AI-Technology-Consulting/agent-skill-tdd`) fails with `Missing --path for GitHub URL.` Use one of the path-aware forms above.

Restart Codex after installing. Claude Code loads/updates skills automatically when they change.

### Codex (manual)

Codex discovers skills from `.codex/skills/` (repo-scoped) and `~/.codex/skills/` (user-scoped).

User-scoped (applies to all repos):

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/skills/tdd" ~/.codex/skills/tdd
# or: cp -R skills/tdd ~/.codex/skills/tdd
```

Repo-scoped (applies to one target repo):

```bash
mkdir -p <target-repo>/.codex/skills
ln -s "$(pwd)/skills/tdd" <target-repo>/.codex/skills/tdd
# or: cp -R skills/tdd <target-repo>/.codex/skills/tdd
```

Restart Codex. Verify with `/skills` (or type `$` to browse skills).

> **Troubleshooting:** If Codex reports `invalid YAML: mapping values are not allowed in this context`, the frontmatter `description` contains `: ` without quoting. Fix: `description: "…workflow: activate…"`.

### Claude Code (manual)

Claude Code discovers skills from `.claude/skills/` (repo-scoped) and `~/.claude/skills/` (user-scoped).

User-scoped (applies to all repos):

```bash
mkdir -p ~/.claude/skills
ln -s "$(pwd)/skills/tdd" ~/.claude/skills/tdd
# or: cp -R skills/tdd ~/.claude/skills/tdd
```

Repo-scoped (applies to one target repo):

```bash
mkdir -p <target-repo>/.claude/skills
ln -s "$(pwd)/skills/tdd" <target-repo>/.claude/skills/tdd
# or: cp -R skills/tdd <target-repo>/.claude/skills/tdd
```

Claude Code loads/updates skills automatically when they change. Verify by asking: `What Skills are available?`

## Validate (this repo)

```bash
# Frontmatter check
python3 tools/check_skill_frontmatter.py skills/tdd

# Unit tests
python3 -m unittest discover -s tests -p 'test*.py'
```
