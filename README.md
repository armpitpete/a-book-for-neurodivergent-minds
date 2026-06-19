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
- DOCX proof export
- EPUB proof export
- PDF proof export, if a PDF engine is available

Expected outputs are written under:

```text
build/export/
```

These generated proof files are outputs. Do not commit them.

### Proof check commands

After pulling `main`, run these commands from the repo root:

    python scripts/check_no_tracked_export_outputs.py
    python scripts/export_all_proofs.py

The first command checks that generated export files under `build/export/` are not tracked by Git.

The second command runs the full proof/export workflow.

A missing PDF engine warning is acceptable for now.

Generated files under `build/export/` must not be committed.

### Final proof checklist

Before using the exported book files:

- run `python scripts/check_no_tracked_export_outputs.py`
- run `python scripts/export_all_proofs.py`
- check the DOCX opens correctly
- check the EPUB opens correctly
- check the PDF if a PDF engine is installed
- do not commit files under `build/export/`
- if the proof looks wrong, fix the source manuscript files, not the generated export files

### PDF note

DOCX and EPUB proofs should export normally when Pandoc is available.

PDF export also needs a Pandoc PDF engine, such as MiKTeX or TeX Live. If the PDF engine is missing, the runner should warn and continue. That warning is acceptable for now.
