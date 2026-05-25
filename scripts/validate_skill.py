#!/usr/bin/env python3
"""Validate the public skill package without external dependencies."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


SKILL_NAME = "obsidian-memory-closeout"
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
PRIVATE_PATH_PATTERNS = [
    re.compile("/" + "Users" + r"/[^/\s]+"),
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
]
REQUIRED_ROOT_FILES = (
    "README.md",
    "PRIVACY.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "AGENTS.md",
    "LICENSE",
    "docs/GRAPHIFY.md",
    ".github/workflows/validate.yml",
)
REQUIRED_SKILL_FILES = (
    "SKILL.md",
    "LICENSE.txt",
    "agents/openai.yaml",
    "references/graphify.md",
    "references/memory-note-schema.md",
    "references/transcript-processing.md",
    "scripts/refresh_graphify.py",
    "scripts/secret_scan.py",
)


def parse_simple_yaml(text: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def validate_frontmatter_file(path: pathlib.Path, required_keys: tuple[str, ...]) -> str | None:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return f"{path} must start with YAML frontmatter"
    metadata = parse_simple_yaml(match.group("body"))
    for key in required_keys:
        if key not in metadata:
            return f"{path} frontmatter missing {key}"
    return None


def iter_public_text_files(root: pathlib.Path) -> list[pathlib.Path]:
    suffixes = {".md", ".txt", ".yaml", ".yml", ".py", ".sh"}
    skipped = {".git", "dist", "__pycache__"}
    files: list[pathlib.Path] = []
    for path in sorted(root.rglob("*")):
        if any(part in skipped for part in path.parts):
            continue
        if path.is_file() and (path.suffix.lower() in suffixes or path.name in {"LICENSE", ".gitignore"}):
            files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    skill_dir = root / "skill" / SKILL_NAME
    skill_md = skill_dir / "SKILL.md"
    agents_yaml = skill_dir / "agents" / "openai.yaml"

    for rel in REQUIRED_ROOT_FILES:
        if not (root / rel).is_file():
            return fail(f"missing required repository file: {rel}")

    if not skill_md.is_file():
        return fail(f"missing {skill_md}")

    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return fail("SKILL.md must start with YAML frontmatter")

    metadata = parse_simple_yaml(match.group("body"))
    if metadata.get("name") != SKILL_NAME:
        return fail("SKILL.md frontmatter name does not match package name")
    if len(metadata.get("description", "")) < 80:
        return fail("SKILL.md description should be specific enough to trigger reliably")

    frontmatter_keys = set(parse_simple_yaml(match.group("body")).keys())
    if frontmatter_keys != {"name", "description"}:
        return fail("SKILL.md frontmatter should contain only name and description")

    for path in iter_public_text_files(root):
        file_text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in PRIVATE_PATH_PATTERNS:
            if pattern.search(file_text):
                rel = path.relative_to(root)
                return fail(f"{rel} contains private-looking text matching {pattern.pattern}")

    if not agents_yaml.is_file():
        return fail("missing agents/openai.yaml")
    agents_text = agents_yaml.read_text(encoding="utf-8")
    for required in ("display_name:", "short_description:", "default_prompt:"):
        if required not in agents_text:
            return fail(f"agents/openai.yaml missing {required}")

    referenced = re.findall(r"`(references/[^`]+|scripts/[^`]+)`", text)
    for rel in referenced:
        if not (skill_dir / rel).is_file():
            return fail(f"SKILL.md references missing file: {rel}")

    for rel in REQUIRED_SKILL_FILES:
        if not (skill_dir / rel).is_file():
            return fail(f"missing required file: {rel}")

    graphify_docs = (
        root / "README.md",
        root / "docs" / "GRAPHIFY.md",
        skill_dir / "references" / "graphify.md",
    )
    for path in graphify_docs:
        content = path.read_text(encoding="utf-8")
        if "Graphify" not in content or ".graphifyignore" not in content:
            return fail(f"{path.relative_to(root)} should document Graphify and .graphifyignore")

    for example in sorted((root / "examples").glob("*.md")):
        error = validate_frontmatter_file(
            example,
            ("id", "type", "status", "created", "updated", "confidence", "source", "tags"),
        )
        if error:
            return fail(error)

    print(f"validated {SKILL_NAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
