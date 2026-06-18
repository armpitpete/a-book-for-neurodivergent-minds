# Current Frontmatter Audit — Chapters 1–28

## Status

Audit complete.

This audit checked the current front matter in the live chapter files for Chapters 1–28.

No chapter bodies were rewritten.

## Main finding

The current files show mixed status labels.

Only Chapters 1, 4, and 5 are currently marked with older cleaned/strong labels.

Chapter 6 is marked as safety reviewed, but still needs a later readability check.

Chapters 2, 3, and 7–28 are currently marked `draft_v0.1` and `draft_needs_review` in their front matter.

This means the project status history overstated “checked” for at least part of Chapters 18–28. The chapter files themselves still need either review or status normalization.

## Current frontmatter inventory

| Chapter | File | status | standalone_status | linked_tool | Note |
|---:|---|---|---|---|---|
| 1 | `01_Start_Here_When_Everything_Feels_Like_Too_Much.md` | `cleaned_draft_v0.1` | `strong` | — | early cleaned label |
| 2 | `02_Why_Life_May_Have_Felt_Harder_Than_It_Looked.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 3 | `03_You_Are_Not_Broken_But_You_May_Be_Overloaded.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 4 | `04_Overload.md` | `cleaned_draft_v0.1` | `strong` | `08_Noise_Budget.md` | early cleaned label; linked tool present |
| 5 | `05_Shutdown.md` | `cleaned_draft_v0.1` | `strong` | `12_The_Quiet_Handover.md` | early cleaned label; linked tool present |
| 6 | `06_Meltdown.md` | `safety_reviewed_draft_v0.1` | `good_needs_later_readability_check` | — | safety-reviewed but not fully clean |
| 7 | `07_Burnout.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 8 | `08_The_Cost_of_Masking.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 9 | `09_Sensory_Load.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 10 | `10_Demand_Friction.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 11 | `11_Transitions_Change_and_Being_Thrown_Off.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 12 | `12_Uneven_Skills_Uneven_Days.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 13 | `13_Social_Confusion_and_After_Analysis.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 14 | `14_Rejection_Sensitivity_and_Fear_of_Getting_It_Wrong.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 15 | `15_Food_Body_Basics_and_Keeping_the_Floor_in_Place.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 16 | `16_Environment_Making_Space_Less_Hostile.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 17 | `17_Routines_That_Support_Rather_Than_Trap.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 18 | `18_Planning_Without_Collapse.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 19 | `19_Decisions_Choices_and_Getting_Unstuck.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 20 | `20_Asking_for_Help_Without_Having_to_Perform_Distress.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 21 | `21_Communication_Without_Guesswork.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 22 | `22_Boundaries_Exits_and_Reducing_Damage.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 23 | `23_Repair_Apology_and_Not_Carrying_Everything.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 24 | `24_Friendship_Love_and_Being_Misread.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 25 | `25_Work_School_and_Being_Treated_Fairly.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 26 | `26_Systems_Forms_and_Official_Language.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 27 | `27_Money_Admin_and_Avoiding_Shame_Spirals.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |
| 28 | `28_Health_Appointments_and_Being_Believed.md` | `draft_v0.1` | `draft_needs_review` | — | needs review or normalization |

## Interpretation

The book has a complete 35-chapter inventory, but current file metadata does not yet support marking the whole main book clean.

The safest next step is not a blind status change.

The safest next step is a review/normalization pass in small batches:

1. Chapters 2–3
2. Chapters 7–12
3. Chapters 13–17
4. Chapters 18–23
5. Chapters 24–28
6. Chapter 6 readability check

Each batch should check the actual chapter text briefly before changing `standalone_status` to `checked`.

## Recommended target status scheme

For checked chapters:

```yaml
status: draft_v0.2
standalone_status: checked
```

For Chapter 6 after readability check:

```yaml
status: draft_v0.2
standalone_status: checked
```

For chapters not yet checked:

```yaml
status: draft_v0.1
standalone_status: draft_needs_review
```

## Next action

Start with Chapters 2–3.

Check them against Chapters 1 and 4.

If they work, normalize their front matter only, unless the chapter text needs a small cleanup.

## Do not do

Do not mass-change Chapters 2–28 to `checked` without reading them.

Do not rewrite chapter bodies during normalization unless a specific problem is found.

Do not start the 12-tool supplement sequence until the main book status labels are trustworthy.
