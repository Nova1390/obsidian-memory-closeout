#!/usr/bin/env python3
"""Package the installable Codex skill as a zip archive."""

from __future__ import annotations

import argparse
import pathlib
import sys
import zipfile


SKILL_NAME = "obsidian-memory-closeout"
REQUIRED_FILES = {
    "SKILL.md",
    "LICENSE.txt",
    "agents/openai.yaml",
    "references/graphify.md",
    "references/memory-note-schema.md",
    "references/transcript-processing.md",
    "references/web-clips.md",
    "scripts/refresh_graphify.py",
    "scripts/secret_scan.py",
}


def iter_package_files(skill_dir: pathlib.Path) -> list[pathlib.Path]:
    files: list[pathlib.Path] = []
    for path in sorted(skill_dir.rglob("*")):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts:
            continue
        files.append(path)
    return files


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--check", action="store_true", help="Validate package contents without keeping the zip")
    args = parser.parse_args()

    root = pathlib.Path(args.root).resolve()
    skill_dir = root / "skill" / SKILL_NAME
    if not skill_dir.is_dir():
        print(f"missing skill directory: {skill_dir}", file=sys.stderr)
        return 1

    rel_files = {str(path.relative_to(skill_dir)) for path in iter_package_files(skill_dir)}
    missing = sorted(REQUIRED_FILES - rel_files)
    if missing:
        for rel in missing:
            print(f"missing required package file: {rel}", file=sys.stderr)
        return 1

    dist_dir = root / "dist"
    dist_dir.mkdir(exist_ok=True)
    archive = dist_dir / f"{SKILL_NAME}.zip"

    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in iter_package_files(skill_dir):
            zf.write(path, pathlib.Path(SKILL_NAME) / path.relative_to(skill_dir))

    if args.check:
        with zipfile.ZipFile(archive) as zf:
            names = set(zf.namelist())
        expected = {str(pathlib.Path(SKILL_NAME) / rel) for rel in REQUIRED_FILES}
        missing_in_zip = sorted(expected - names)
        archive.unlink(missing_ok=True)
        if missing_in_zip:
            for rel in missing_in_zip:
                print(f"missing from zip: {rel}", file=sys.stderr)
            return 1

    print(archive)
    return 0


if __name__ == "__main__":
    sys.exit(main())
