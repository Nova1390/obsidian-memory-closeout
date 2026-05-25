#!/usr/bin/env python3
"""Scan text files for common secret-like patterns before memory commits."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


PATTERNS = {
    "api_key": re.compile(r"(?i)\b(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^'\"\s]{12,}"),
    "private_key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}

SKIP_DIRS = {".git", ".obsidian", "node_modules", ".venv", "venv", "__pycache__", "graphify-out/cache"}
TEXT_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".toml", ".env", ".csv"}


def should_scan(path: pathlib.Path) -> bool:
    parts = set(path.parts)
    if parts & SKIP_DIRS:
        return False
    return path.is_file() and (path.suffix.lower() in TEXT_SUFFIXES or path.name.startswith(".env"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    args = parser.parse_args()

    findings: list[tuple[str, int, str]] = []
    for raw in args.paths:
        root = pathlib.Path(raw)
        candidates = [root] if root.is_file() else root.rglob("*")
        for path in candidates:
            if not should_scan(path):
                continue
            try:
                text = path.read_text(errors="ignore")
            except OSError:
                continue
            for line_no, line in enumerate(text.splitlines(), 1):
                for name, pattern in PATTERNS.items():
                    if pattern.search(line):
                        findings.append((str(path), line_no, name))

    for path, line_no, name in findings:
        print(f"{path}:{line_no}: possible {name}")

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
