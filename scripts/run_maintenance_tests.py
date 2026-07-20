from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = (
    "01-descoberta-da-skill.md",
    "02-template-sem-unidade-de-analise.md",
    "03-portao-t-template-integral.md",
    "04-portao-o-ontologia.md",
    "05-portao-a-piloto-de-anotacao.md",
)
FIXTURES = (
    "README.md",
    "corpus-sintetico-minimo.md",
)


def run_step(name: str, command: list[str], env: dict[str, str] | None = None) -> str:
    print(f"ETAPA {name}")
    result = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    output = result.stdout.rstrip()
    if output:
        print(output)
    if result.returncode != 0:
        raise RuntimeError(f"falha na etapa {name}, codigo {result.returncode}")
    print(f"ETAPA_OK {name}")
    return output


def check_repository_files() -> None:
    print("ETAPA arquivos")
    required = (
        ROOT / "docs/PROTOCOLO_DE_MANUTENCAO.md",
        ROOT / "CHANGELOG_MANUTENCAO.md",
        ROOT / "docs/PROMPT_CRON_DIARIO.md",
        ROOT / "tests/fixtures/README.md",
        ROOT / "tests/fixtures/corpus-sintetico-minimo.md",
    )
    required += tuple(ROOT / "tests/cenarios" / scenario for scenario in SCENARIOS)
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise RuntimeError("arquivos ausentes, " + ", ".join(missing))
    print("ETAPA_OK arquivos")


def check_scenario_fixtures() -> None:
    print("ETAPA fixtures")
    fixture_dir = ROOT / "tests/fixtures"
    for fixture in FIXTURES:
        if not (fixture_dir / fixture).is_file():
            raise RuntimeError(f"fixture ausente, tests/fixtures/{fixture}")

    for scenario_name in SCENARIOS:
        path = ROOT / "tests/cenarios" / scenario_name
        text = path.read_text(encoding="utf-8")
        if "tests/fixtures/" not in text and scenario_name != SCENARIOS[0]:
            raise RuntimeError(f"cenario sem fixture, {path.relative_to(ROOT)}")
        references = re.findall(r"`([^`]+)`", text)
        outside = [item for item in references if item.startswith("tests/") and not item.startswith("tests/fixtures/")]
        if outside:
            raise RuntimeError(
                f"cenario referencia corpus fora de tests/fixtures, {path.relative_to(ROOT)}"
            )
    print("ETAPA_OK fixtures")


def check_skill_discovery(hermes_path: str) -> None:
    print("ETAPA descoberta")
    with tempfile.TemporaryDirectory(prefix="synesis-maintenance-") as temporary_dir:
        profile = Path(temporary_dir)
        target = profile / "skills/research/synesis"
        target.parent.mkdir(parents=True)
        shutil.copytree(
            ROOT,
            target,
            ignore=shutil.ignore_patterns(".git", "__pycache__", ".pytest_cache"),
        )
        env = os.environ.copy()
        env["HERMES_HOME"] = str(profile)
        output = run_step("hermes_skills_list", [hermes_path, "skills", "list"], env)
        normalized = output.lower()
        expected = ("synesis", "research", "local", "enabled")
        missing = [term for term in expected if term not in normalized]
        if missing:
            raise RuntimeError("descoberta incompleta, ausente " + ", ".join(missing))
    print("ETAPA_OK descoberta")


def main() -> int:
    hermes_path = shutil.which("hermes")
    if hermes_path is None:
        print("MAINTENANCE_TESTS_FAILED")
        print("executavel hermes nao encontrado no PATH")
        return 1
    try:
        run_step(
            "testes_regressao",
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                "tests",
                "-p",
                "test_maintenance.py",
                "-v",
            ],
        )
        run_step("validacao_skill", [sys.executable, "scripts/validate_skill.py"])
        check_repository_files()
        check_scenario_fixtures()
        check_skill_discovery(hermes_path)
    except RuntimeError as error:
        print("MAINTENANCE_TESTS_FAILED")
        print(error)
        return 1
    print("MAINTENANCE_TESTS_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
