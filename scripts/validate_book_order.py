from __future__ import annotations

import re
from pathlib import Path

BLOCKED_TERMS = (
    "archive_old_modules",
    "NOTE",
    "REVIEW",
    "CHECK",
    "BRIEF",
    "TEMPLATE",
    "LOCAL_TOOL_INVENTORY",
    "TOOL_SPINE",
)

REQUIRED_MAIN_CHAPTERS = range(1, 36)
MAIN_CHAPTER_RE = re.compile(r"^manuscript/main_book/(\d{2})_.*\.md$")


def load_manifest_lines(manifest_path: Path) -> list[tuple[int, str]]:
    """Return non-comment, non-blank manifest lines with source line numbers."""
    entries: list[tuple[int, str]] = []

    for line_number, raw_line in enumerate(
        manifest_path.read_text(encoding="utf-8").splitlines(),
        start=1,
    ):
        entry = raw_line.strip()
        if not entry or entry.startswith("#"):
            continue
        entries.append((line_number, entry))

    return entries


def find_blocked_entries(entries: list[tuple[int, str]]) -> list[str]:
    problems: list[str] = []

    for line_number, entry in entries:
        matches = [term for term in BLOCKED_TERMS if term in entry]
        if matches:
            problems.append(
                f"line {line_number}: {entry} contains blocked term(s): "
                + ", ".join(matches)
            )

    return problems


def find_missing_main_chapters(entries: list[tuple[int, str]]) -> list[str]:
    present_chapters: set[int] = set()

    for _, entry in entries:
        match = MAIN_CHAPTER_RE.match(entry)
        if not match:
            continue

        chapter_number = int(match.group(1))
        if chapter_number in REQUIRED_MAIN_CHAPTERS:
            present_chapters.add(chapter_number)

    return [
        f"{chapter_number:02d}"
        for chapter_number in REQUIRED_MAIN_CHAPTERS
        if chapter_number not in present_chapters
    ]


def validate_book_order(manifest_path: Path) -> list[str]:
    if not manifest_path.exists():
        return [f"missing manifest: {manifest_path}"]

    entries = load_manifest_lines(manifest_path)
    errors = find_blocked_entries(entries)

    missing_chapters = find_missing_main_chapters(entries)
    if missing_chapters:
        errors.append("missing main chapter(s): " + ", ".join(missing_chapters))

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    manifest_path = repo_root / "book-order.txt"

    errors = validate_book_order(manifest_path)

    if errors:
        print("Book order manifest validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Book order manifest valid: no blocked working/archive terms found; "
        "main chapters 01-35 are present."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
