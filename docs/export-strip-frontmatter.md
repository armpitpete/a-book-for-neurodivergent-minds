# Export rule: strip YAML frontmatter

Reader-facing exports must not show YAML frontmatter.

The manuscript source files can keep frontmatter because it helps with project tracking, status, linked chapters, and later automation.

The reader-facing export must strip the frontmatter block from each Markdown file before creating DOCX, PDF, EPUB, or any other reader copy.

## Rule

Keep one source version.

Do not create duplicate reader-clean files.

Strip frontmatter during export.

## What counts as frontmatter

A YAML frontmatter block is a metadata block at the top of a Markdown file.

It starts with a line containing three hyphens.

It ends at the next line containing three hyphens.

Only strip this block when it appears at the very start of the file.

## Source files

Source files may contain metadata such as tool number, title, status, linked chapters, or source notes.

That metadata is useful for managing the project.

It should not appear in the reader-facing book.

## Export behaviour

During export:

1. Read the Markdown source file.
2. If the file starts with a YAML frontmatter block, remove that block.
3. Keep the visible heading and body text.
4. Combine or export the cleaned content.
5. Do not write cleaned duplicate files back into the manuscript folders.

## Run the clean Markdown export

Run this from the repository root:

    python scripts/export_strip_frontmatter.py

The script writes cleaned Markdown files to:

    build/export/markdown-clean/

The build folder is ignored by Git.

Do not edit the cleaned export copies as manuscript source.

## Good export result

A reader-facing export should begin with the actual reader text.

Example:

# Tool 1 - The One-Pressure Check

## What this tool is for

It should not begin with project metadata.

## Why this rule exists

Frontmatter is useful for managing the book.

Frontmatter is not useful for the reader.

Keeping one source version reduces confusion, prevents duplicated text, and avoids maintaining two versions of the same manuscript.
