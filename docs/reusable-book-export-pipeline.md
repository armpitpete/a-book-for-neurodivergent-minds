# Reusable Book Export Pipeline

This project now has a simple export pattern that can be reused for other Markdown-based book projects.

The purpose is to keep the working manuscript useful for editing while producing clean reader-facing files for review, conversion, and publishing.

## Standard folder pattern

Use this structure for book projects:

```text
manuscript/
scripts/
build/
```

## Source files

Put the editable book files in:

```text
manuscript/
```

The manuscript files may contain YAML frontmatter if it helps with editing, sorting, status tracking, or project management.

Reader-facing exports must not include YAML frontmatter.

## Required scripts

Use these scripts:

```text
scripts/export_strip_frontmatter.py
scripts/export_combined_clean_markdown.py
```

### `export_strip_frontmatter.py`

This script reads Markdown files from `manuscript/`, removes YAML frontmatter from each file, and writes clean copies to:

```text
build/export/markdown-clean/
```

### `export_combined_clean_markdown.py`

This script runs the frontmatter-stripping export first, then combines the cleaned Markdown files into one book-level Markdown file:

```text
build/export/A_Book_for_Neurodivergent_Minds_clean.md
```

For other books, change the final output filename to match the book title.

Examples:

```text
build/export/Blackhope_clean.md
build/export/Behringer_System_55_Guide_clean.md
build/export/Lina_of_Vaelinya_clean.md
```

## Generated files

Generated export files belong under:

```text
build/
```

The `build/` folder must stay ignored by Git.

Do not commit generated exports unless there is a specific release reason.

## Why frontmatter is stripped

YAML frontmatter is useful for managing a manuscript, but it is not reader-facing book content.

Clean exports are better for:

- full-book reading
- DOCX conversion
- PDF conversion
- EPUB conversion
- website publication
- sending the manuscript to another tool

## Current ordering rule

The combined export currently uses sorted file paths with natural number sorting.

This works when files and folders are named clearly, for example:

```text
001-title-page.md
002-introduction.md
010-chapter-01.md
011-chapter-02.md
```

This is good enough for a simple book repo.

## Risk

Filename sorting can still produce the wrong reading order if files are badly named or if draft/planning files live inside `manuscript/`.

Avoid putting notes, discarded drafts, or planning files inside the export path unless they are meant to appear in the book.

## Next upgrade

The safer future version should use an explicit book-order manifest.

Possible file:

```text
book-order.txt
```

Example content:

```text
manuscript/front/title.md
manuscript/front/introduction.md
manuscript/chapters/chapter-01.md
manuscript/chapters/chapter-02.md
manuscript/back/notes.md
```

A manifest would make the export order exact instead of relying on filenames.

## When this pattern is safe to copy

Copy this pattern to another book project when:

- the book is mostly Markdown
- reader-facing exports need to be clean
- the project has many chapter files
- generated outputs should stay out of Git
- the manuscript needs a combined review file

Do not copy it blindly into a project with unusual source folders or mixed file types without checking the folder structure first.

## Good enough rule

A book export is good enough when:

- clean Markdown files are generated
- the combined book file exists
- the combined file does not start with YAML frontmatter
- the reading order is sensible
- `git status` does not show generated `build/` output
