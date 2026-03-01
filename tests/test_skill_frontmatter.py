import unittest
import re
from pathlib import Path

from tools.check_skill_frontmatter import parse_minimal_frontmatter


class TestSkillFrontmatter(unittest.TestCase):
    @staticmethod
    def _read_skill_text() -> str:
        return Path("skills/tdd/SKILL.md").read_text(encoding="utf-8")

    def test_tdd_skill_frontmatter_is_valid(self) -> None:
        text = self._read_skill_text()
        fm = parse_minimal_frontmatter(text)
        self.assertEqual(fm.name, "tdd")
        self.assertTrue(fm.description.strip())
        self.assertLessEqual(len(fm.description), 500)
        self.assertIn("every coding task", fm.description)

    def test_tdd_skill_requires_per_task_requirements_folder(self) -> None:
        text = self._read_skill_text()
        self.assertIn(".requirements/", text)
        self.assertIn("<datetime>_<feature_name>", text)
        self.assertIn(".requirements/<datetime>_<feature_name>/REQUIREMENTS.md", text)
        self.assertIn("YYYYMMDDTHHMMSSZ", text)
        self.assertIn("update_github_authentication", text)
        self.assertIn("_01", text)
        self.assertIn("REQUIREMENTS.md", text)
        self.assertIsNotNone(re.search(r"\d{8}T\d{6}Z", text))

    def test_tdd_skill_does_not_instruct_overwriting_root_requirements(self) -> None:
        text = self._read_skill_text()
        self.assertIsNone(re.search(r"(?i)write\s+/REQUIREMENTS\.md\b", text))
        self.assertIsNone(
            re.search(r"(?i)write/?overwrite\s+`?REQUIREMENTS\.md`?\s+in\s+the\s+target\s+repository\s+root", text)
        )
        self.assertIsNone(re.search(r"(?i)backup copy when overwriting", text))

    def test_tdd_skill_contains_workflow_activity_diagram(self) -> None:
        text = self._read_skill_text()
        self.assertIn("## Workflow Activity Diagram (PlantUML)", text)
        match = re.search(r"```plantuml\s*(@startuml.*?@enduml)\s*```", text, re.DOTALL)
        self.assertIsNotNone(match)
        diagram = match.group(1)
        self.assertIn("@startuml", diagram)
        self.assertIn("@enduml", diagram)
        self.assertIn("start", diagram)
        self.assertIn("stop", diagram)
        self.assertIn("if", diagram)
        self.assertIn("repeat", diagram)
        self.assertIn("while", diagram)
        self.assertIn("Serena", diagram)
        self.assertIn("Investigate", diagram)
        self.assertIn("REQUIREMENTS.md", diagram)
        self.assertIn("Lad", diagram)
