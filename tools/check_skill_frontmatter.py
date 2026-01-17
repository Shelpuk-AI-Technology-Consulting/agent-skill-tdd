#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Frontmatter:
    name: str
    description: str


class FrontmatterError(ValueError):
    pass


def _extract_frontmatter_block(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("SKILL.md must start with a YAML frontmatter block ('---' on first line).")

    end_index = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_index = i
            break

    if end_index is None:
        raise FrontmatterError("YAML frontmatter block must be closed with a second '---' line.")

    return "\n".join(lines[1:end_index])


def parse_minimal_frontmatter(text: str) -> Frontmatter:
    block = _extract_frontmatter_block(text)
    name: str | None = None
    description: str | None = None

    for raw_line in block.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith(("'", '"')) and value.endswith(("'", '"')) and len(value) >= 2:
            value = value[1:-1]
        if key == "name" and name is None:
            name = value
        if key == "description" and description is None:
            description = value

    if not name:
        raise FrontmatterError("Missing required frontmatter field: name")
    if not description:
        raise FrontmatterError("Missing required frontmatter field: description")

    return Frontmatter(name=name, description=description)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Validate minimal Agent Skills frontmatter for SKILL.md files.")
    parser.add_argument("skill_dir", help="Path to a skill directory containing SKILL.md (e.g., skills/tdd).")
    args = parser.parse_args(argv)

    skill_dir = Path(args.skill_dir)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        print(f"ERROR: Missing {skill_md}", file=sys.stderr)
        return 2

    text = skill_md.read_text(encoding="utf-8")
    try:
        fm = parse_minimal_frontmatter(text)
    except FrontmatterError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    expected_name = skill_dir.name
    if fm.name != expected_name:
        print(f"ERROR: frontmatter name '{fm.name}' must match directory name '{expected_name}'", file=sys.stderr)
        return 2

    if "\n" in fm.description or "\r" in fm.description:
        print("ERROR: frontmatter description must be a single line", file=sys.stderr)
        return 2

    # Codex currently constrains description length to 500 characters. Enforce this
    # to maximize cross-client compatibility.
    if len(fm.description) > 500:
        print("ERROR: frontmatter description must be <= 500 characters", file=sys.stderr)
        return 2

    print(f"OK: {skill_md} (name={fm.name!r})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
