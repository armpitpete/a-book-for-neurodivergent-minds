# Tool Module Inventory Note

## Status

Partial connector-based inventory.

This is not a full folder listing.

The connector can fetch exact known paths, but it cannot reliably list the whole `manuscript/tool_supplement/modules/` folder in this workflow.

## Confirmed existing module files

These files were confirmed by exact path:

| Tool | Confirmed path | Status line found | Notes |
|---:|---|---|---|
| 8 | `manuscript/tool_supplement/modules/08_Noise_Budget.md` | Expanded draft v0.1 | Existing anchor tool. Keep number. |
| 11 | `manuscript/tool_supplement/modules/11_The_Misread_Map.md` | Expanded draft v0.2 — plain intent/impact wording added | Existing anchor tool. Keep number. |
| 12 | `manuscript/tool_supplement/modules/12_The_Quiet_Handover.md` | Expanded draft v0.1 | Existing anchor tool. Keep number. |

## Confirmed anchor roles

### Tool 8 — Noise Budget

Confirmed title:

```md
# Noise Budget
```

Confirmed use:

Use when the reader feels overloaded but cannot tell why.

Main line:

> What has already filled the shelf?

This matches the proposed supplement sequence.

### Tool 11 — The Misread Map

Confirmed title:

```md
# The Misread Map
```

Confirmed use:

Use when someone misreads tone, face, words, silence, speed, or reaction.

Main line:

> What did I mean, what did they experience, and what was assumed?

This matches the proposed supplement sequence.

### Tool 12 — The Quiet Handover

Confirmed title:

```md
# The Quiet Handover
```

Confirmed use:

Use when the reader needs to pass important information to someone but has limited speech, energy, time, or processing capacity.

Main line:

> I cannot explain fully. This is the important part: ____.

This matches the proposed supplement sequence.

## Paths probed but not found

These proposed paths did not resolve through exact connector fetch:

- `manuscript/tool_supplement/modules/01_The_One_Pressure_Check.md`
- `manuscript/tool_supplement/modules/02_The_Good_Enough_Line.md`
- `manuscript/tool_supplement/modules/03_The_Next_Safe_Step.md`
- `manuscript/tool_supplement/modules/04_The_Capacity_Check.md`
- `manuscript/tool_supplement/modules/05_The_Body_Floor_Check.md`
- `manuscript/tool_supplement/modules/06_The_Choice_Shrinker.md`
- `manuscript/tool_supplement/modules/07_The_Support_Ask.md`
- `manuscript/tool_supplement/modules/09_The_Transition_Bridge.md`
- `manuscript/tool_supplement/modules/10_The_Boundary_Exit_Card.md`

This does not prove these tools do not exist.

It only proves they do not exist at those exact proposed paths.

A local checkout is still needed for a complete inventory.

## Current conclusion

The proposed supplement plan should keep these anchors locked unless a local inventory proves otherwise:

- Tool 8 — Noise Budget
- Tool 11 — The Misread Map
- Tool 12 — The Quiet Handover

The missing/unconfirmed tools should be treated as planned modules until the folder is inspected locally.

## Next local command

From the repo folder, run:

```powershell
Get-ChildItem "manuscript\tool_supplement\modules" -File | Sort-Object Name | Select-Object Name
```

For a fuller inventory:

```powershell
Get-ChildItem "manuscript\tool_supplement\modules" -Filter "*.md" | Sort-Object Name | ForEach-Object {
  $first = Get-Content $_.FullName -TotalCount 8
  [PSCustomObject]@{
    File = $_.Name
    Heading = ($first | Where-Object { $_ -match '^# ' } | Select-Object -First 1)
    Status = ($first | Where-Object { $_ -match 'draft|Status|Expanded' } | Select-Object -First 1)
  }
} | Format-Table -AutoSize
```

## Next project action

After the local inventory, compare the real module files against `TOOL_SUPPLEMENT_SEQUENCE_PLAN.md`.

Then decide whether to:

1. keep the proposed 12-tool sequence,
2. rename existing files to match it,
3. create missing module files, or
4. revise the sequence around stronger existing modules.
