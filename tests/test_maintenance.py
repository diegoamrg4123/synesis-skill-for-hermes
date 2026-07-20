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


if __name__ == "__main__":
    unittest.main()
