"""Build a zipped release bundle from generated export files."""

from __future__ import annotations

import os
import zipfile
from pathlib import Path


EXPORT_DIR = Path("build/export")
RELEASE_DIR = Path("build/release")
PROJECT_SLUG = "a-book-for-neurodivergent-minds"


def get_version() -> str:
    return os.environ.get("GITHUB_REF_NAME") or os.environ.get("RELEASE_VERSION") or "local"


def build_zip(zip_path: Path, source_dir: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source_dir))


def main() -> int:
    if not EXPORT_DIR.exists():
        print(f"FAIL: export directory missing: {EXPORT_DIR}")
        print("Run scripts/export_all_proofs.py before building a release bundle.")
        return 1

    RELEASE_DIR.mkdir(parents=True, exist_ok=True)

    version = get_version()
    zip_path = RELEASE_DIR / f"{PROJECT_SLUG}-{version}.zip"

    build_zip(zip_path, EXPORT_DIR)

    print(f"Release bundle written: {zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
