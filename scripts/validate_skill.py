from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = {
    "SKILL.md",
    "README.md",
    "LICENSE",
    ".gitignore",
    ".gitattributes",
    "references/decisoes-metodologicas.md",
    "references/ecossistema.md",
    "references/fluxos-hermes.md",
    "references/ontologia-e-chains.md",
    "references/sintaxe-e-validacao.md",
    "docs/PROTOCOLO_DE_MANUTENCAO.md",
    "docs/PROMPT_CRON_DIARIO.md",
    "CHANGELOG_MANUTENCAO.md",
    "tests/fixtures/README.md",
    "tests/fixtures/corpus-sintetico-minimo.md",
    "tests/cenarios/01-descoberta-da-skill.md",
    "tests/cenarios/02-template-sem-unidade-de-analise.md",
    "tests/cenarios/03-portao-t-template-integral.md",
    "tests/cenarios/04-portao-o-ontologia.md",
    "tests/cenarios/05-portao-a-piloto-de-anotacao.md",
    "tests/test_maintenance.py",
}
FORBIDDEN_CHARACTERS = {
    chr(0x2013): "U+2013",
    chr(0x2014): "U+2014",
    chr(59): "U+003B",
}
STYLE_TERMS = {
    "abrangente",
    "crucial",
    "disruptivo",
    "valioso",
    "essencial",
    "inspirador",
    "significativo",
    "transformador",
    "revelador",
    "imperativo",
    "fundamental",
    "insight",
    "sinergia",
    "experiência",
    "potencial",
    "aliado",
    "mosaico",
    "multifacetado",
}


def text_files() -> list[Path]:
    text_suffixes = {".md", ".py", ".yml", ".yaml"}
    text_names = {"LICENSE", ".gitignore", ".gitattributes"}
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
        and (path.suffix.lower() in text_suffixes or path.name in text_names)
    )


def validate_frontmatter(text: str) -> list[str]:
    errors: list[str] = []
    match = re.match(r"^---\n(.*?)\n---\n(.+)$", text, re.DOTALL)
    if not match:
        return ["SKILL.md tem frontmatter ou corpo inválido"]

    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if field:
            metadata[field.group(1)] = field.group(2).strip().strip('"\'')

    required = {
        "name",
        "version",
        "description",
        "author",
        "license",
        "platforms",
        "metadata",
    }
    for field in sorted(required - metadata.keys()):
        errors.append(f"frontmatter sem {field}")

    name = metadata.get("name", "")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append("name deve usar letras minúsculas, números e hífen")

    description = metadata.get("description", "")
    if not description.startswith("Use "):
        errors.append("description deve começar com Use")
    if len(description) > 60:
        errors.append("description ultrapassa 60 caracteres")

    if len(text) > 100_000:
        errors.append("SKILL.md ultrapassa 100000 caracteres")

    references = re.findall(r"`(references/[^`]+\.md)`", text)
    for reference in sorted(set(references)):
        if not (ROOT / reference).is_file():
            errors.append(f"referência ausente, {reference}")

    return errors


def main() -> int:
    errors: list[str] = []

    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).is_file():
            errors.append(f"arquivo ausente, {relative}")

    for path in text_files():
        relative = path.relative_to(ROOT).as_posix()
        data = path.read_bytes()
        if data.startswith(bytes([0xEF, 0xBB, 0xBF])):
            errors.append(f"BOM UTF-8 em {relative}")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as error:
            errors.append(f"UTF-8 inválido em {relative}, {error}")
            continue

        if "\r\n" in text:
            errors.append(f"quebra CRLF em {relative}")

        for character, label in FORBIDDEN_CHARACTERS.items():
            for line_number, line in enumerate(text.splitlines(), 1):
                if character in line:
                    errors.append(
                        f"caractere proibido {label} em {relative}:{line_number}"
                    )

        if path.suffix.lower() == ".md":
            lowered = text.lower()
            for term in sorted(STYLE_TERMS):
                for line_number, line in enumerate(lowered.splitlines(), 1):
                    if term in line:
                        errors.append(
                            f"termo de estilo {term!r} em {relative}:{line_number}"
                        )

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill_text = skill_path.read_text(encoding="utf-8")
        errors.extend(validate_frontmatter(skill_text))

    if errors:
        print("VALIDATION_FAILED")
        for error in errors:
            print(error)
        return 1

    print("VALIDATION_OK")
    print(f"files={len(text_files())}")
    print(f"skill_chars={len((ROOT / 'SKILL.md').read_text(encoding='utf-8'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
