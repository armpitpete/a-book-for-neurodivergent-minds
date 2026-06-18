from pathlib import Path
import re

from export_strip_frontmatter import OUTPUT_DIR as CLEAN_MARKDOWN_DIR
from export_strip_frontmatter import export_clean_markdown


REPO_ROOT = Path(__file__).resolve().parents[1]
COMBINED_OUTPUT_PATH = (
    REPO_ROOT / "build" / "export" / "A_Book_for_Neurodivergent_Minds_clean.md"
)


def natural_sort_key(path: Path) -> list[object]:
    """Sort paths in a way that keeps numbered book files in reading order."""
    relative_path = path.relative_to(CLEAN_MARKDOWN_DIR).as_posix().lower()
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", relative_path)]


def find_clean_markdown_files() -> list[Path]:
    if not CLEAN_MARKDOWN_DIR.exists():
        raise SystemExit(f"Clean Markdown folder not found: {CLEAN_MARKDOWN_DIR}")

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
