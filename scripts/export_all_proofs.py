from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"

PDF_ENGINE_MISSING_MARKERS = (
    "Pandoc could not create a PDF because a PDF engine is probably missing",
    "PDF engine is probably missing",
    "a PDF engine such as MiKTeX, TeX Live, or wkhtmltopdf may be missing",
    "command exited with code 47",
)


@dataclass(frozen=True)
class ProofStep:
    name: str
    script_name: str
    optional_pdf_engine: bool = False


PROOF_STEPS = (
    ProofStep("Final book export check", "final_book_export_check.py"),
    ProofStep("Combined book structure check", "check_combined_book_structure.py"),
    ProofStep("H1 top-level order check", "check_h1_top_level_order.py"),
    ProofStep("DOCX proof export", "export_clean_docx.py"),
    ProofStep("EPUB proof export", "export_clean_epub.py"),
    ProofStep("PDF proof export", "export_clean_pdf.py", optional_pdf_engine=True),
)


def is_missing_pdf_engine(output: str) -> bool:
    return any(marker in output for marker in PDF_ENGINE_MISSING_MARKERS)


def print_captured_output(result: subprocess.CompletedProcess[str]) -> None:
    if result.stdout:
        print(result.stdout.rstrip())

    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)


def run_step(step: ProofStep) -> bool:
    script_path = SCRIPTS_DIR / step.script_name

    if not script_path.exists():
        print(f"FAIL: {step.name} script is missing: {script_path}")
        return False

    print(f"\n=== {step.name} ===")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )

    print_captured_output(result)

    if result.returncode == 0:
        print(f"OK: {step.name} passed.")
        return True

    combined_output = f"{result.stdout}\n{result.stderr}"

    if step.optional_pdf_engine and is_missing_pdf_engine(combined_output):
        print("WARN: PDF proof export skipped because the PDF engine is missing.")
        print("WARN: Install MiKTeX, TeX Live, or another Pandoc PDF engine to enable PDF proof export.")
        return True

    print(f"FAIL: {step.name} failed with exit code {result.returncode}.")
    return False


def main() -> int:
    failed_steps: list[str] = []

    print("Running all proof exports and checks...")

    for step in PROOF_STEPS:
        if not run_step(step):
            failed_steps.append(step.name)

    if failed_steps:
        print("\nFAIL: all proof exports runner found failure(s):")
        for step_name in failed_steps:
            print(f"- {step_name}")
        return 1

    print("\nPASS: all proof exports runner completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
