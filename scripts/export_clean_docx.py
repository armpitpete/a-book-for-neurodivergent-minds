from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from build_export_ready_markdown import build_export_ready_markdown
from export_combined_clean_markdown import COMBINED_OUTPUT_PATH
from final_book_export_check import main as run_final_book_export_check


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCX_OUTPUT_PATH = REPO_ROOT / "build" / "export" / "A_Book_for_Neurodivergent_Minds_clean.docx"


def require_pandoc() -> str:
    pandoc_path = shutil.which("pandoc")

    if not pandoc_path:
        raise RuntimeError(
            "Pandoc is not installed or is not available on PATH. "
            "Install Pandoc, then reopen PowerShell and try again."
        )

    return pandoc_path


def require_combined_markdown() -> None:
    if not COMBINED_OUTPUT_PATH.exists():
        raise RuntimeError(f"combined Markdown file is missing: {COMBINED_OUTPUT_PATH}")

    if not COMBINED_OUTPUT_PATH.read_text(encoding="utf-8-sig").strip():
        raise RuntimeError(f"combined Markdown file is empty: {COMBINED_OUTPUT_PATH}")


def run_preflight() -> None:
    result = run_final_book_export_check()

    if result != 0:
        raise RuntimeError("final book export check failed; DOCX export stopped")

    print("OK: final book export check passed.")


def export_docx() -> None:
    pandoc_path = require_pandoc()
    require_combined_markdown()
    export_ready_path = build_export_ready_markdown()

    DOCX_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    command = [
        pandoc_path,
        str(export_ready_path),
        "-o",
        str(DOCX_OUTPUT_PATH),
        "--metadata",
        "title=A Book for Neurodivergent Minds",
    ]

    subprocess.run(command, check=True)

    if not DOCX_OUTPUT_PATH.exists():
        raise RuntimeError(f"DOCX output was not created: {DOCX_OUTPUT_PATH}")

    print(f"PASS: DOCX proof exported to: {DOCX_OUTPUT_PATH}")


def main() -> int:
    try:
        run_preflight()
        export_docx()
    except subprocess.CalledProcessError as error:
        print("FAIL: Pandoc failed while exporting DOCX.")
        print(f"- command exited with code {error.returncode}")
        return 1
    except Exception as error:
        print("FAIL: DOCX export failed.")
        print(f"- {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
