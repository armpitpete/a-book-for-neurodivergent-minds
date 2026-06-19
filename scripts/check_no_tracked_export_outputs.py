"""Fail if generated export outputs are tracked by Git."""

from __future__ import annotations

import subprocess
from pathlib import Path


EXPORT_DIR = "build/export"


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]

    try:
        result = subprocess.run(
            ["git", "ls-files", EXPORT_DIR],
            cwd=repo_root,
            check=False,
            text=True,
            capture_output=True,
        )
    except FileNotFoundError:
        print("FAIL: git is not available on PATH.")
        return 1

    if result.returncode != 0:
        print("FAIL: could not check tracked export outputs.")
        if result.stderr.strip():
            print(result.stderr.strip())
        return result.returncode

    tracked_files = [line for line in result.stdout.splitlines() if line.strip()]

    if tracked_files:
        print(f"FAIL: generated export outputs are tracked under {EXPORT_DIR}:")
        for path in tracked_files:
            print(f"- {path}")
        print("Remove these from Git tracking. Do not delete local proof outputs unless intended.")
        return 1

    print(f"PASS: no generated export outputs are tracked under {EXPORT_DIR}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
