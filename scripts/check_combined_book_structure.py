from __future__ import annotations

import re
from pathlib import Path

from export_combined_clean_markdown import COMBINED_OUTPUT_PATH


BLOCKED_WORKING_TERMS = (
    "archive_old_modules",
    "LOCAL_TOOL_INVENTORY",
    "TOOL_SPINE",
    "_NOTE",
    "_REVIEW",
    "_CHECK",
    "_BRIEF",
    "_PLAN",
    "_MAP",
    "_AUDIT",
    "TEMPLATE",
)

HEADING_RE = re.compile(r"^(#{1,3})\s+(.+?)\s*$", re.MULTILINE)


def load_combined_book() -> str:
    if not COMBINED_OUTPUT_PATH.exists():
        raise RuntimeError(f"combined book file is missing: {COMBINED_OUTPUT_PATH}")

    text = COMBINED_OUTPUT_PATH.read_text(encoding="utf-8-sig")

    if not text.strip():
        raise RuntimeError(f"combined book file is empty: {COMBINED_OUTPUT_PATH}")

    return text


def find_headings(text: str) -> list[tuple[int, str, str]]:
    headings: list[tuple[int, str, str]] = []

    for match in HEADING_RE.finditer(text):
        marker = match.group(1)
        title = match.group(2).strip()
        headings.append((match.start(), marker, title))

    return headings


def print_heading_summary(headings: list[tuple[int, str, str]]) -> None:
    if not headings:
        raise RuntimeError("no Markdown headings found in combined book")

    print("Headings found:")
    for _, marker, title in headings[:80]:
        print(f"- {marker} {title}")

    if len(headings) > 80:
        print(f"... {len(headings) - 80} more headings not shown")


def check_tool_supplement_position(headings: list[tuple[int, str, str]]) -> None:
    supplement_positions = [
        position
        for position, _, title in headings
        if "tool supplement" in title.lower()
    ]

    if not supplement_positions:
        raise RuntimeError("Tool Supplement heading was not found")

    first_supplement_position = min(supplement_positions)

    earlier_headings = [
        title
        for position, _, title in headings
        if position < first_supplement_position
    ]

    if not earlier_headings:
        raise RuntimeError("Tool Supplement appears before the main book headings")

    print("OK: Tool Supplement appears after earlier book headings.")


def check_blocked_terms(text: str) -> None:
    found_terms = [term for term in BLOCKED_WORKING_TERMS if term in text]

    if found_terms:
        raise RuntimeError(
            "blocked working/archive term(s) found in combined book: "
            + ", ".join(found_terms)
        )

    print("OK: no blocked working/archive terms found in combined book.")


def main() -> int:
    try:
        text = load_combined_book()
        headings = find_headings(text)
        print_heading_summary(headings)
        check_tool_supplement_position(headings)
        check_blocked_terms(text)
    except Exception as error:
        print("FAIL: combined book structure check failed.")
        print(f"- {error}")
        return 1

    print("PASS: combined book structure check completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
