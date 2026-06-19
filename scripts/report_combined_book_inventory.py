from __future__ import annotations

import re
from collections import Counter

from export_combined_clean_markdown import COMBINED_OUTPUT_PATH


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def load_combined_book() -> str:
    if not COMBINED_OUTPUT_PATH.exists():
        raise RuntimeError(f"combined book file is missing: {COMBINED_OUTPUT_PATH}")

    text = COMBINED_OUTPUT_PATH.read_text(encoding="utf-8-sig")

    if not text.strip():
        raise RuntimeError(f"combined book file is empty: {COMBINED_OUTPUT_PATH}")

    return text


def find_headings(text: str) -> list[tuple[int, int, str]]:
    headings: list[tuple[int, int, str]] = []

    for match in HEADING_RE.finditer(text):
        marker = match.group(1)
        title = match.group(2).strip()
        headings.append((len(headings) + 1, len(marker), title))

    return headings


def print_inventory(headings: list[tuple[int, int, str]]) -> None:
    if not headings:
        raise RuntimeError("no Markdown headings found in combined book")

    print("Combined book heading inventory")
    print(f"Source: {COMBINED_OUTPUT_PATH}")
    print("")

    for number, level, title in headings:
        print(f"{number:03d} | H{level} | {title}")

    print("")
    print_summary(headings)


def print_summary(headings: list[tuple[int, int, str]]) -> None:
    counts = Counter(level for _, level, _ in headings)

    print("Summary:")
    print(f"- Total headings: {len(headings)}")

    for level in range(1, 7):
        if counts[level]:
            print(f"- H{level}: {counts[level]}")


def main() -> int:
    try:
        text = load_combined_book()
        headings = find_headings(text)
        print_inventory(headings)
    except Exception as error:
        print("FAIL: combined book inventory report failed.")
        print(f"- {error}")
        return 1

    print("PASS: combined book inventory report completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
