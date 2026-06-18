# Chapters 2–3 Check Note

## Status

Chapters 2 and 3 were checked against the opening flow:

- Chapter 1: immediate bad-day entry point.
- Chapter 2: hidden effort and cost.
- Chapter 3: load, mismatch, and missing support.
- Chapter 4: overload as a specific state.

## Result

The sequence works.

Chapter 2 passes and was normalized to:

```yaml
status: draft_v0.2
standalone_status: checked
```

Chapter 3 also passes conceptually, but the frontmatter-only update was blocked by the connector safety layer during the write attempt.

No chapter body rewrite was needed.

## Chapter 2

Chapter 2 works as the bridge between Chapter 1 and Chapter 3.

It explains that hidden effort counts and that visible success is not the same as low effort.

It prepares the reader for Chapter 3 by making the cost visible before Chapter 3 reframes the problem as load/mismatch/support rather than personal failure.

## Chapter 3

Chapter 3 works as the broad reframing chapter.

It gives the core idea that the reader is not broken and may be carrying too much, too often, with too little support.

It prepares cleanly for Chapter 4, which then explains overload in more detail.

## Remaining action

Retry Chapter 3 frontmatter normalization later, possibly through a local checkout or a smaller/saner Git workflow if the connector blocks the full-file update again.

Do not rewrite the body unless a specific readability problem is found.
