from pathlib import Path
import shutil


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = REPO_ROOT / "manuscript"
OUTPUT_DIR = REPO_ROOT / "build" / "export" / "markdown-clean"


def strip_frontmatter(text: str) -> str:
    if text.startswith("\ufeff"):
        text = text[1:]

    lines = text.splitlines(keepends=True)

    if not lines:
        return text

    if lines[0].strip() != "---":
        return text

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "".join(lines[index + 1:]).lstrip("\r\n")

    return text


def export_clean_markdown() -> None:
    if not SOURCE_DIR.exists():
        raise SystemExit(f"Source folder not found: {SOURCE_DIR}")

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    exported_count = 0

    for source_path in sorted(SOURCE_DIR.rglob("*.md")):
        relative_path = source_path.relative_to(SOURCE_DIR)
        output_path = OUTPUT_DIR / relative_path

        output_path.parent.mkdir(parents=True, exist_ok=True)

        source_text = source_path.read_text(encoding="utf-8-sig")
        clean_text = strip_frontmatter(source_text)

        output_path.write_text(clean_text, encoding="utf-8")
        exported_count += 1

    print(f"Exported {exported_count} cleaned Markdown files to {OUTPUT_DIR}")


if __name__ == "__main__":
    export_clean_markdown()
