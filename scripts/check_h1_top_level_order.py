from __future__ import annotations

import re

from export_combined_clean_markdown import COMBINED_OUTPUT_PATH


EXPECTED_H1_COUNT = 48
EXPECTED_TOOL_NUMBERS = range(1, 13)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def load_combined_book() -> str:
    if not COMBINED_OUTPUT_PATH.exists():
        raise RuntimeError(f"combined book file is missing: {COMBINED_OUTPUT_PATH}")

    text = COMBINED_OUTPUT_PATH.read_text(encoding="utf-8-sig")

    if not text.strip():
        raise RuntimeError(f"combined book file is empty: {COMBINED_OUTPUT_PATH}")

    return text


def find_h1_headings(text: str) -> list[tuple[int, str]]:
    return [(match.start(), match.group(1).strip()) for match in H1_RE.finditer(text)]


def print_h1_headings(headings: list[tuple[int, str]]) -> None:
    print("H1 top-level headings:")
    for number, (_, title) in enumerate(headings, start=1):
        print(f"{number:02d} | {title}")


def check_h1_count(headings: list[tuple[int, str]]) -> None:
    if len(headings) != EXPECTED_H1_COUNT:
        raise RuntimeError(
            f"expected {EXPECTED_H1_COUNT} H1 headings, found {len(headings)}"
        )

    print(f"OK: found expected H1 count: {EXPECTED_H1_COUNT}")


def find_heading_position(headings: list[tuple[int, str]], title: str) -> int:
    for position, heading_title in headings:
        if heading_title == title:
            return position

    raise RuntimeError(f"H1 heading not found: {title}")


def check_tool_supplement_contents(headings: list[tuple[int, str]]) -> int:
    position = find_heading_position(headings, "Tool Supplement Contents")
    print("OK: Tool Supplement Contents heading found.")
    return position


def check_all_tool_pages_present(headings: list[tuple[int, str]]) -> list[tuple[int, str]]:
    tool_headings: list[tuple[int, str]] = []
    titles = [title for _, title in headings]

    for tool_number in EXPECTED_TOOL_NUMBERS:
        prefix = f"Tool {tool_number} "
        matches = [
            (position, title)
            for position, title in headings
            if title.startswith(prefix)
        ]

        if not matches:
            raise RuntimeError(f"missing H1 tool page: Tool {tool_number}")

        tool_headings.append(matches[0])

    print("OK: Tool 1-12 H1 pages are present.")
    return tool_headings


def check_tool_pages_after_supplement(
    supplement_position: int,
    tool_headings: list[tuple[int, str]],
) -> None:
    early_tools = [
        title
        for position, title in tool_headings
        if position < supplement_position
    ]

    if early_tools:
        raise RuntimeError(
            "tool page(s) appear before Tool Supplement Contents: "
            + ", ".join(early_tools)
        )

    print("OK: tool pages appear after Tool Supplement Contents.")


def main() -> int:
    try:
        text = load_combined_book()
        headings = find_h1_headings(text)

        print_h1_headings(headings)
        check_h1_count(headings)

        supplement_position = check_tool_supplement_contents(headings)
        tool_headings = check_all_tool_pages_present(headings)
        check_tool_pages_after_supplement(supplement_position, tool_headings)
    except Exception as error:
        print("FAIL: H1 top-level order check failed.")
        print(f"- {error}")
        return 1

    print("PASS: H1 top-level order check completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
