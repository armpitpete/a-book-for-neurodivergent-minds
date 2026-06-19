from __future__ import annotations

from pathlib import Path
import re

from export_strip_frontmatter import OUTPUT_DIR as CLEAN_MARKDOWN_DIR
from export_strip_frontmatter import SOURCE_DIR
from export_strip_frontmatter import export_clean_markdown


REPO_ROOT = Path(__file__).resolve().parents[1]
BOOK_ORDER_MANIFEST = REPO_ROOT / "book-order.txt"
COMBINED_OUTPUT_PATH = (
    REPO_ROOT / "build" / "export" / "A_Book_for_Neurodivergent_Minds_clean.md"
)


def natural_sort_key(path: Path) -> list[object]:
    """Sort paths in a way that keeps numbered book files in reading order."""
    relative_path = path.as_posix().lower()
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", relative_path)]


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False

    return True


def read_manifest_order() -> list[Path]:
    if not BOOK_ORDER_MANIFEST.exists():
        return []

    source_root = SOURCE_DIR.resolve()
    ordered_clean_paths: list[Path] = []
    seen_entries: set[str] = set()
    errors: list[str] = []

    for line_number, raw_line in enumerate(
        BOOK_ORDER_MANIFEST.read_text(encoding="utf-8-sig").splitlines(),
        start=1,
    ):
        entry = raw_line.strip()

        if not entry or entry.startswith("#"):
            continue

        if entry in seen_entries:
            errors.append(f"Line {line_number}: duplicate entry: {entry}")
            continue

        seen_entries.add(entry)

        source_path = (REPO_ROOT / entry).resolve()

        if Path(entry).is_absolute():
            errors.append(f"Line {line_number}: use a relative path, not an absolute path: {entry}")
            continue

        if not source_path.exists():
            errors.append(f"Line {line_number}: file not found: {entry}")
            continue

        if not source_path.is_file():
            errors.append(f"Line {line_number}: not a file: {entry}")
            continue

        if source_path.suffix.lower() != ".md":
            errors.append(f"Line {line_number}: not a Markdown file: {entry}")
            continue

        if not is_relative_to(source_path, source_root):
            errors.append(f"Line {line_number}: file is outside manuscript folder: {entry}")
            continue

        clean_relative_path = source_path.relative_to(source_root)
        ordered_clean_paths.append(CLEAN_MARKDOWN_DIR / clean_relative_path)

    if errors:
        raise SystemExit("Book order manifest has problems:\n- " + "\n- ".join(errors))

    if not ordered_clean_paths:
        raise SystemExit(f"Book order manifest is empty: {BOOK_ORDER_MANIFEST}")

    return ordered_clean_paths


def find_clean_markdown_files() -> list[Path]:
    if not CLEAN_MARKDOWN_DIR.exists():
        raise SystemExit(f"Clean Markdown folder not found: {CLEAN_MARKDOWN_DIR}")

    manifest_order = read_manifest_order()

    if manifest_order:
        missing_clean_files = [
            clean_path
            for clean_path in manifest_order
            if not clean_path.exists()
        ]

        if missing_clean_files:
            missing_list = "\n- ".join(str(path) for path in missing_clean_files)
            raise SystemExit(f"Clean exported files missing:\n- {missing_list}")

        print(f"Using book order manifest: {BOOK_ORDER_MANIFEST}")
        return manifest_order

    print("No book order manifest found. Falling back to natural sorted path order.")
    return sorted(CLEAN_MARKDOWN_DIR.rglob("*.md"), key=natural_sort_key)


def combine_clean_markdown() -> None:
    export_clean_markdown()

    markdown_files = find_clean_markdown_files()

    if not markdown_files:
        raise SystemExit(f"No cleaned Markdown files found in: {CLEAN_MARKDOWN_DIR}")

    combined_sections: list[str] = []

    for markdown_path in markdown_files:
        text = markdown_path.read_text(encoding="utf-8-sig").strip()

        if text:
            combined_sections.append(text)

    COMBINED_OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    COMBINED_OUTPUT_PATH.write_text("\n\n".join(combined_sections) + "\n", encoding="utf-8")

    print(f"Combined {len(combined_sections)} Markdown files into {COMBINED_OUTPUT_PATH}")


if __name__ == "__main__":
    combine_clean_markdown()
