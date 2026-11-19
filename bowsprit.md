# bowsprit — U73 (fold the blind sensor round in; close the falsifier)

## Start (12 Nov)
Worktree C:/Users/stian/Prosjekter-u73 on u73-sensor-round from c551297. Brief: kai.md "## U73".
Record rows rested on: spec rev130 §5 r4, §6, §7, §8, §12; register sensor-plane rows and 0.10 mT limit (as U71 note cites).
Timebox 2 h.

— bowsprit

## Progress (12:45)
- Round carried in: sws/hw-selection/rounds/2026-11-12-sensor/ (brief, models, answers, README, synthesis). scan_tree 0.
- Two sheet readers out (TI; Infineon/Allegro/TDK); the second is back: TLE493D-W2B6 not a 2x2 BGA (TSOP6), A1308/9, A1363, HAL 18xy, TLE4997 all 4.5-5.5 V.
- Procedures: "proposed, not decided" in operation and recalibration. Pages at 6 / 4 A4 before this unit.
— bowsprit

## Progress (12:46)
- Both sheet readers back; datasheet_check.md written; 5 rows + section 5 in the sensor note; hardware section (6 A4 after trimming), procedures proposals (4 A4). Committed f70283c on the branch.
- Seven --check ok; 135 tests pass. Falsifier pass 1 out (two halves: figures vs sheets; counts/record/pages).
— bowsprit

## Progress (13:0x)
- Falsifier pass 1: FAIL (A: 3 blocking, 8 minor; B: 6 blocking, 9 minor). All fixed except "outside expert" in prose (existing pages use it). Hardware back to 6 A4 (mounting folded into the open line). Commits 72ebdf9, 5b301c8.
- Falsifier pass 2 out (both halves).
— bowsprit

## Progress (13:07)
- Falsifier pass 2: FAIL (2A: 1 blocking — TMAG5170 noise inconsistent with the digital-part rule — 5 minor; 2B: 2 blocking — 179 mT / full span missing on the page; reference-rod count — 7 minor). Fixed, commit 2eefe97; hardware 6 A4.
- Pass 3 (last) out.
— bowsprit

## Done (13:2x)
- Branch u73-sensor-round, tip after "U73: report wording" (C:/Users/stian/Prosjekter-u73/max). No merge, no push, no export.
- Falsifier: pass 1 FAIL (9 blocking), pass 2 FAIL (3 blocking), pass 3 PASS both halves (9 minor, 6 taken).
- Seven --check ok; 135 tests (p52 deselected); hardware 6 A4, procedures 4 A4. idscan 0 (1132 added lines, 2 long data lines skipped); scan_tree added 0, removed 0, round folder 0.
— bowsprit
