# Structure Review v0.6

## Verdict

The repository structure now matches the intended project model.

The project is correctly organised as:

- 35-chapter main book
- 12-module tool supplement
- preserved source uploads
- separate working manuscript files
- archive index for old versions
- status and task control files

## What is structurally correct

### Main book

The main book has a 35-chapter table of contents across five parts.

The current imported draft chapters are mapped to the main book:

- Chapter 1 — Start Here When Everything Feels Like Too Much
- Chapter 4 — Overload
- Chapter 5 — Shutdown
- Chapter 6 — Meltdown

### Tool supplement

The supplement has a complete 12-module file spine.

Modules 1 to 6 have imported source material from the tool index.

Modules 7 to 12 are placeholders and need expansion.

### Source safety

Original imported material is preserved under `source_upload/`.

Working files now live under `manuscript/`.

That means future editing should happen in `manuscript/`, not in `source_upload/`.

## Main risk

The repo now contains two kinds of files:

1. real draft material
2. placeholder/scaffold files

Do not treat placeholder files as finished manuscript.

## Real draft material now available

- Chapter 1 source draft
- Chapter 4 source draft
- Chapter 5 source draft
- Chapter 6 source draft
- Tool index source

## Scaffold material now available

- clean working chapter shells
- supplement module placeholders
- chapter map
- tool map
- standalone chapter check
- archive index

## Recommended next action

Begin Chapter 1 cleanup.

Do not create the remaining 31 chapter placeholders yet.

Reason: placeholders for all 35 chapters would make the repo look fuller while adding little real progress.

Better next move:

1. Clean Chapter 1 into a usable working manuscript chapter.
2. Keep it standalone.
3. Make it shorter and easier to scan.
4. Use it as the pattern for later chapters.

## Structure status

v0.6 structure: sound.

Ready for first manuscript cleanup pass.
