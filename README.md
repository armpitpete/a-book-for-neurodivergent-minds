# a-book-for-neurodivergent-minds

## Proof export workflow

Use the all-in-one proof runner from the repo root:

```powershell
python scripts/export_all_proofs.py
```

This runs the book export checks and proof exports in one command.

It checks:

- `book-order.txt` validation
- combined clean Markdown export
- combined book structure
- H1 top-level order
- export-ready Markdown with Contents and page breaks
- DOCX proof export
- EPUB proof export
- PDF proof export, if a PDF engine is available

Expected outputs are written under:

```text
build/export/
```

These generated proof files are outputs. Do not commit them.

For the full operator checklist, see:

```text
docs/proof-export-manual.md
```

### Proof check commands

After pulling `main`, run these commands from the repo root:

    python scripts/check_no_tracked_export_outputs.py
    python scripts/export_all_proofs.py

The first command checks that generated export files under `build/export/` are not tracked by Git.

The second command runs the full proof/export workflow.

A missing PDF engine warning is acceptable for now.

Generated files under `build/export/` must not be committed.

### Export-ready Markdown

The proof workflow now builds an export-ready Markdown file before creating DOCX, EPUB, and PDF proofs.

This generated helper file adds:

- Contents page
- chapter anchors
- page breaks before top-level chapters and tools
- export metadata used by the proof formats

Expected generated helper file:

```text
build/export/A_Book_for_Neurodivergent_Minds_export_ready.md
```

Do not commit this file.

### Final proof checklist

Before using the exported book files:

- run `python scripts/check_no_tracked_export_outputs.py`
- run `python scripts/export_all_proofs.py`
- check the DOCX opens correctly
- check the EPUB opens correctly
- check the PDF if a PDF engine is installed
- check that Contents appears
- check that chapters and tools start on new pages
- do not commit files under `build/export/`
- if the proof looks wrong, fix the source manuscript files, not the generated export files

### PDF note

DOCX and EPUB proofs should export normally when Pandoc is available.

PDF export also needs a Pandoc PDF engine, such as MiKTeX or TeX Live. If the PDF engine is missing, the runner should warn and continue. That warning is acceptable for now.

### Windows PDF engine note

PDF export needs a Pandoc PDF engine.

On Windows, MiKTeX is a practical choice.

If `pdflatex` is missing, the all-in-one runner should warn and continue.

DOCX and EPUB proofs are still usable without the PDF engine.

This does not block normal proof work.
