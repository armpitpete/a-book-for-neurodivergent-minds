from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from export_combined_clean_markdown import COMBINED_OUTPUT_PATH


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPORT_READY_MARKDOWN_PATH = (
    REPO_ROOT
    / "build"
    / "export"
    / "A_Book_for_Neurodivergent_Minds_export_ready.md"
)

H1_PATTERN = re.compile(r"^# (?!#)(.+?)\s*(?:\{#[^}]+\})?\s*$")


@dataclass(frozen=True)
class ChapterHeading:
    number: int
    title: str
    anchor: str


def is_fence_marker(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def extract_chapters(lines: list[str]) -> list[ChapterHeading]:
    chapters: list[ChapterHeading] = []
    in_fence = False

    for line in lines:
        if is_fence_marker(line):
            in_fence = not in_fence

        if in_fence:
            continue

        match = H1_PATTERN.match(line)
        if not match:
            continue

        title = match.group(1).strip()
        number = len(chapters) + 1
        chapters.append(
            ChapterHeading(
                number=number,
                title=title,
                anchor=f"chapter-{number:02d}",
            )
        )

    return chapters


def page_break_lines() -> list[str]:
    return [
        "",
        "```{=openxml}",
        '<w:p xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:r><w:br w:type="page"/></w:r></w:p>',
        "```",
        "",
        "\\newpage",
        "",
    ]


def build_contents_lines(chapters: list[ChapterHeading]) -> list[str]:
    lines = [
        "# Contents {#contents}",
        "",
    ]

    for chapter in chapters:
        lines.append(f"- [{chapter.title}](#{chapter.anchor})")

    lines.extend(page_break_lines())

    return lines


def add_contents_and_page_breaks(text: str) -> str:
    lines = text.splitlines()
    chapters = extract_chapters(lines)

    if not chapters:
        raise RuntimeError("no H1 chapter headings found in combined Markdown")

    output_lines = build_contents_lines(chapters)
    chapter_index = 0
    in_fence = False

    for line in lines:
        if is_fence_marker(line):
            in_fence = not in_fence
            output_lines.append(line)
            continue

        match = None if in_fence else H1_PATTERN.match(line)

        if match:
            chapter = chapters[chapter_index]

            if chapter_index > 0:
                output_lines.extend(page_break_lines())

            output_lines.append(f"# {chapter.title} {{#{chapter.anchor}}}")
            chapter_index += 1
            continue

        output_lines.append(line)

    return "\n".join(output_lines).rstrip() + "\n"


def build_export_ready_markdown() -> Path:
    if not COMBINED_OUTPUT_PATH.exists():
        raise RuntimeError(f"combined Markdown file is missing: {COMBINED_OUTPUT_PATH}")

    source_text = COMBINED_OUTPUT_PATH.read_text(encoding="utf-8-sig")

    if not source_text.strip():
        raise RuntimeError(f"combined Markdown file is empty: {COMBINED_OUTPUT_PATH}")

    EXPORT_READY_MARKDOWN_PATH.parent.mkdir(parents=True, exist_ok=True)
    EXPORT_READY_MARKDOWN_PATH.write_text(
        add_contents_and_page_breaks(source_text),
        encoding="utf-8",
    )

    print(
        "PASS: export-ready Markdown with contents and page breaks written to: "
        f"{EXPORT_READY_MARKDOWN_PATH}"
    )

    return EXPORT_READY_MARKDOWN_PATH
