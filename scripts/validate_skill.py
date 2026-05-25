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
]


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    skill_dir = root / "skill" / SKILL_NAME
    skill_md = skill_dir / "SKILL.md"
    agents_yaml = skill_dir / "agents" / "openai.yaml"

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

    for pattern in PRIVATE_PATH_PATTERNS:
        if pattern.search(text):
            return fail(f"SKILL.md contains private-looking text matching {pattern.pattern}")

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

    for rel in (
        "references/memory-note-schema.md",
        "references/transcript-processing.md",
        "scripts/refresh_graphify.py",
        "scripts/secret_scan.py",
    ):
        if not (skill_dir / rel).is_file():
            return fail(f"missing required file: {rel}")

    print(f"validated {SKILL_NAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
