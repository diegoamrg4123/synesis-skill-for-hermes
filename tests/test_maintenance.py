from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class MaintenanceRepositoryTests(unittest.TestCase):
    def copy_repository(self, temporary_dir: str) -> Path:
        target = Path(temporary_dir) / "repo"
        shutil.copytree(
            ROOT,
            target,
            ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"),
        )
        return target

    def run_validator(self, root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, "scripts/validate_skill.py"],
            cwd=root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )

    def test_gitattributes_crlf_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="synesis-test-") as temporary_dir:
            root = self.copy_repository(temporary_dir)
            path = root / ".gitattributes"
            text = path.read_text(encoding="utf-8")
            path.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))

            result = self.run_validator(root)

            self.assertNotEqual(result.returncode, 0)
            self.assertIn("quebra CRLF em .gitattributes", result.stdout)

    def test_prompt_defines_deterministic_scenario_rotation(self) -> None:
        prompt = (ROOT / "docs/PROMPT_CRON_DIARIO.md").read_text(encoding="utf-8")
        expected = (
            "Segunda-feira, cenário 01",
            "Terça-feira, cenário 02",
            "Quarta-feira, cenário 03",
            "Quinta-feira, cenário 04",
            "Sexta-feira, cenário 05",
            "Sábado e domingo, cenário 01",
        )

        for item in expected:
            with self.subTest(item=item):
                self.assertIn(item, prompt)

    def test_changelog_registers_crlf_correction(self) -> None:
        changelog = (ROOT / "CHANGELOG_MANUTENCAO.md").read_text(encoding="utf-8")

        self.assertIn("## 2026-07-10", changelog)
        self.assertIn("preservação de LF em clones Windows", changelog)

    def test_public_docs_warn_about_the_historical_compiler_baseline(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        ecosystem = (ROOT / "references/ecossistema.md").read_text(encoding="utf-8")
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

        for text in (readme, ecosystem, skill):
            with self.subTest(document=text[:20]):
                self.assertIn("0.9.0", text)
                self.assertIn("0.7.0", text)
                self.assertIn("0.6.0", text)

    def test_graph_integration_uses_the_current_repository_name(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        ecosystem = (ROOT / "references/ecossistema.md").read_text(encoding="utf-8")

        for text in (readme, ecosystem):
            with self.subTest(document=text[:20]):
                self.assertIn("synesis-graph", text)
                self.assertNotIn("synesis2graph", text)

        self.assertIn(
            "https://github.com/synesis-lang/synesis-graph",
            ecosystem,
        )

    def test_workflow_uses_read_only_permissions_and_pinned_actions(self) -> None:
        workflow = (ROOT / ".github/workflows/validate.yml").read_text(
            encoding="utf-8"
        )

        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertNotIn("actions/checkout@v4", workflow)
        self.assertNotIn("actions/setup-python@v5", workflow)
        self.assertRegex(workflow, r"actions/checkout@[0-9a-f]{40}")
        self.assertRegex(workflow, r"actions/setup-python@[0-9a-f]{40}")


if __name__ == "__main__":
    unittest.main()
