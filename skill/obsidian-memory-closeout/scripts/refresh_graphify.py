#!/usr/bin/env python3
"""Refresh Graphify outputs for a curated Markdown vault when graphify is installed."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys


def run(cmd: list[str], cwd: str) -> int:
    print("+ " + " ".join(cmd))
    completed = subprocess.run(cmd, cwd=cwd, text=True)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("vault", help="Obsidian vault or memory repo path")
    parser.add_argument("--html", action="store_true", help="Generate graph.html as well as graph.json/report")
    args = parser.parse_args()

    if not shutil.which("graphify"):
        print("graphify not found; skipping derived index refresh", file=sys.stderr)
        return 2

    code = run(["graphify", "update", ".", "--no-cluster", "--force"], args.vault)
    if code:
        return code

    cluster_cmd = ["graphify", "cluster-only", "."]
    if not args.html:
        cluster_cmd.append("--no-viz")
    return run(cluster_cmd, args.vault)


if __name__ == "__main__":
    sys.exit(main())
