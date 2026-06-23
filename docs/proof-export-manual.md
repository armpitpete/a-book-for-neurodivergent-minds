# Proof export manual

This note explains how to make and check proof exports for *A Book for Neurodivergent Minds*.

Use this when preparing DOCX, EPUB, and PDF proof files.

## Main command

From the repository root, run:

```powershell
python scripts/export_all_proofs.py
```

This is the normal proof command.

It runs the proof checks and creates the current proof outputs under:

```text
build/export/
```

Generated files in `build/export/` are proof outputs. Do not commit them.

## Pre-check command

Before exporting, run:

```powershell
python scripts/check_no_tracked_export_outputs.py
```

This confirms that generated export files are not being tracked by Git.

If it fails, stop and fix the tracking problem before making more proof files.

## What the all-in-one runner checks

The proof runner should check:

- `book-order.txt` validation
- combined clean Markdown export
- combined book structure
- H1 top-level order
- DOCX proof export
- EPUB proof export
- PDF proof export if a PDF engine is available

## Export-ready Markdown

The export workflow builds an export-ready Markdown file before creating DOCX, EPUB, and PDF proofs.

The export-ready Markdown file adds:

- a Contents page
- chapter anchors
- page breaks before top-level chapters and tools
- metadata title support for exported formats

Expected generated helper file:

```text
build/export/A_Book_for_Neurodivergent_Minds_export_ready.md
```

This is also a generated output. Do not commit it.

## Expected proof outputs

The proof runner may produce:

- combined clean Markdown
- export-ready Markdown
- DOCX proof
- EPUB proof
- PDF proof, if a PDF engine is installed

All generated proof files belong under:

```text
build/export/
```

Do not edit generated proof files directly.

If the proof looks wrong, fix the source manuscript files or export scripts, then rerun the proof export.

## PDF engine note

DOCX and EPUB require Pandoc.

PDF also requires a Pandoc PDF engine.

On Windows, MiKTeX is a practical PDF engine choice.

If `pdflatex` is missing, the runner may warn and continue. That warning is acceptable for normal proof work as long as DOCX and EPUB export correctly.

Do not treat a missing PDF engine as a manuscript failure.

## Manual DOCX check

Open the DOCX proof and check:

- the file opens without repair warnings
- the Contents page appears near the front
- chapters and tools start on new pages
- headings are in the expected order
- paragraph spacing is readable
- no obvious encoding damage appears
- no source-only notes appear in the proof unless they are meant to be printed

## Manual EPUB check

Open the EPUB proof and check:

- the file opens in an EPUB reader
- the title appears correctly
- the contents/navigation is usable
- chapters appear in the correct order
- text reflows without broken structure
- headings are readable
- no generated build paths appear in reader-facing text

## Manual PDF check

Only run this when a PDF engine is installed.

Open the PDF proof and check:

- the file opens normally
- the Contents page appears
- chapters and tools start on new pages
- page breaks are sensible
- headings are readable
- no text is obviously clipped
- no generated build paths appear in reader-facing text

## Final proof checklist

Before using exported proof files, run:

```powershell
python scripts/check_no_tracked_export_outputs.py
python scripts/export_all_proofs.py
```

Then check:

- DOCX opens correctly
- EPUB opens correctly
- PDF opens correctly if a PDF engine is installed
- Contents page exists
- chapter/page breaks are present
- generated files are not staged for commit
- any error is fixed in source, not by editing generated proof files

## Release workflow note

A proof export is not automatically a release.

Before a release, confirm:

- final proof checklist has passed
- generated outputs are not accidentally tracked
- release workflow has the tools it needs, including Pandoc
- PDF generation is either working or intentionally skipped
- the source manuscript, not the generated files, contains the final text

## Stop rules

Stop and investigate if:

- `book-order.txt` validation fails
- H1 order check fails
- DOCX export fails
- EPUB export fails
- generated files are tracked by Git
- the proof opens with repair warnings
- chapters or tools no longer start on new pages
- Contents is missing or wrong
- source-only notes appear in the reader-facing proof

## Good-enough proof rule

A proof is good enough for review when:

- DOCX opens
- EPUB opens
- Contents is present
- chapters/tools start on new pages
- generated files are not committed
- any missing PDF is only because the local PDF engine is missing

Do not polish generated exports manually.

Fix the source and rerun the export.
