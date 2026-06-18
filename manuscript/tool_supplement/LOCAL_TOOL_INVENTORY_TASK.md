# Local Tool Inventory Task

## Status

Local task note.

The GitHub connector confirmed that this path is a directory:

```text
manuscript/tool_supplement/modules
```

But the connector cannot list directory contents in this workflow.

This inventory must be run from a local checkout.

## Goal

Create a trustworthy list of the real tool module files.

Then compare that list against:

```text
manuscript/tool_supplement/TOOL_SUPPLEMENT_SEQUENCE_PLAN.md
```

## Good enough

Good enough means:

- every real tool module filename is listed
- every real tool module heading is listed
- the status line is captured if present
- confirmed Tools 8, 11, and 12 stay anchored unless the local inventory proves a better reason to change them
- no files are renamed yet
- no module bodies are rewritten yet

## Step 1 — Open repo folder

In PowerShell:

```powershell
cd "I:\ORDER\GitHub\a-book-for-neurodivergent-minds"
```

## Step 2 — Confirm folder exists

```powershell
Test-Path "manuscript\tool_supplement\modules"
```

Expected:

```text
True
```

If it says `False`, stop and check repo path.

## Step 3 — Basic module list

```powershell
Get-ChildItem "manuscript\tool_supplement\modules" -File | Sort-Object Name | Select-Object Name
```

Copy the output back into ChatGPT.

## Step 4 — Full heading/status inventory

```powershell
Get-ChildItem "manuscript\tool_supplement\modules" -Filter "*.md" | Sort-Object Name | ForEach-Object {
  $first = Get-Content $_.FullName -TotalCount 12
  [PSCustomObject]@{
    File = $_.Name
    Heading = ($first | Where-Object { $_ -match '^# ' } | Select-Object -First 1)
    Status = ($first | Where-Object { $_ -match 'draft|Status|Expanded|checked|v0\.' } | Select-Object -First 1)
  }
} | Format-Table -AutoSize
```

Copy the output back into ChatGPT.

## Step 5 — Optional exact word count for modules

```powershell
Get-ChildItem "manuscript\tool_supplement\modules" -Filter "*.md" | Sort-Object Name | ForEach-Object {
  $text = Get-Content $_.FullName -Raw
  $count = ([regex]::Matches($text, '\b[\p{L}\p{N}]+(?:[-’''`][\p{L}\p{N}]+)*\b')).Count
  [PSCustomObject]@{
    File = $_.Name
    Words = $count
  }
} | Format-Table -AutoSize
```

## Step 6 — Do not edit yet

After the inventory, do not rename files yet.

First compare the real files against the proposed 12-tool sequence.

## Known confirmed files from connector

These were confirmed by exact connector fetch:

- `08_Noise_Budget.md`
- `11_The_Misread_Map.md`
- `12_The_Quiet_Handover.md`

## Next decision after inventory

After the local inventory, decide one of these:

1. keep the proposed 12-tool sequence and create missing modules,
2. rename existing modules to match the sequence,
3. revise the sequence around stronger existing modules,
4. keep current module names but add a sequence/contents page.
