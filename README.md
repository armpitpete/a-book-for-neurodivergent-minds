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

### PDF note

DOCX and EPUB proofs should export normally when Pandoc is available.

PDF export also needs a Pandoc PDF engine, such as MiKTeX or TeX Live. If the PDF engine is missing, the runner should warn and continue. That warning is acceptable for now.
