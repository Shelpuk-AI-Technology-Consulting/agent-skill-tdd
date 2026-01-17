import unittest
from pathlib import Path

from tools.check_skill_frontmatter import parse_minimal_frontmatter


class TestSkillFrontmatter(unittest.TestCase):
    def test_tdd_skill_frontmatter_is_valid(self) -> None:
        skill_md = Path("skills/tdd/SKILL.md")
        text = skill_md.read_text(encoding="utf-8")
        fm = parse_minimal_frontmatter(text)
        self.assertEqual(fm.name, "tdd")
        self.assertTrue(fm.description.strip())
        self.assertLessEqual(len(fm.description), 500)
        self.assertIn("every coding task", fm.description)
