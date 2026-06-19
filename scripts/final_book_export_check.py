from __future__ import annotations

from pathlib import Path

from export_combined_clean_markdown import COMBINED_OUTPUT_PATH
from export_combined_clean_markdown import combine_clean_markdown
from validate_book_order import validate_book_order


REPO_ROOT = Path(__file__).resolve().parents[1]
BOOK_ORDER_MANIFEST = REPO_ROOT / "book-order.txt"


def run_book_order_validation() -> None:
    errors = validate_book_order(BOOK_ORDER_MANIFEST)

    if errors:
        raise RuntimeError(
            "book-order.txt validation failed:\n- " + "\n- ".join(errors)
        )

    print("OK: book-order.txt passed validation.")


def run_combined_export() -> None:
    try:
        combine_clean_markdown()
    except SystemExit as error:
        raise RuntimeError(str(error)) from error

    print("OK: combined clean Markdown export ran.")


def check_combined_output() -> None:
    if not COMBINED_OUTPUT_PATH.exists():
        raise RuntimeError(f"combined output file was not created: {COMBINED_OUTPUT_PATH}")

    text = COMBINED_OUTPUT_PATH.read_text(encoding="utf-8-sig")

    if not text.strip():
        raise RuntimeError(f"combined output file is empty: {COMBINED_OUTPUT_PATH}")

    if text.startswith("---"):
        raise RuntimeError(
            "combined output starts with YAML frontmatter; expected clean Markdown"
        )

    print(f"OK: combined output exists and has no YAML frontmatter: {COMBINED_OUTPUT_PATH}")


def main() -> int:
    try:
        run_book_order_validation()
        run_combined_export()
        check_combined_output()
    except Exception as error:
        print("FAIL: final book export check failed.")
        print(f"- {error}")
        return 1

    print("PASS: final book export check completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
