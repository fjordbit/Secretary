# shroud — U77 (rig sheet for the prototype test, 40 mm rope)

## Start (16 Nov 12:43 machine clock)
- Worktree C:/Users/stian/Prosjekter-u77 on u77-rig-sheet from a3a633a. Brief: kai.md "## U77" (line 3167).
- Rests on: procedures page data list (build_procedures.py, 17 rows, and the sources it cites); spec rev130 §11 (prototype characterisation), §6, §8, §12; register rows on the old prototype's parts and the 12 Nov rulings; sensor page and both sensor notes; sws_sensor_placement.md; the two prototype data sheets (read only).
- Timebox 2 h, ends ~14:43 machine clock.

— shroud

## Progress
- Built docs/sws/build_rig_sheet.py -> rig_sheet.html; link from the prototype stage of the procedures page (one line). Prints 4 A4 (headless Edge to PDF, page objects counted, pages looked at).
- Technician: USABLE WITH FIXES (4 blocking: no per-channel table in run 1, empty-head contradiction, no fallback without a defect, no recipient field) -> all fixed, minors mostly taken.
- Falsifier pass 1: FAIL (1 blocking: rows 1-2 claimed filled in full) -> fields added, rows 1, 2, 4 named "filled only in part"; minors M1-M14 taken. Pass 2 running.
- Nine --check ok; SWS tests 173 (151 + 22 new; p52 out).

— shroud

## Done
- Branch u77-rig-sheet, tip 2155c44 (C:/Users/stian/Prosjekter-u77/max). No merge, no push, no export.
- Falsifier pass 2 PASS (5 minor, 3 taken). Sheet 4 A4. Nine --check ok; SWS tests 173 (p52 out). idscan a3a633a..HEAD 0 (900 added lines); scan_tree 0 on the 7 changed files.

— shroud

## Round 2 done
- main f806c68 merged (TASKS.md conflict: both entries kept). Tip 4015134 on u77-rig-sheet. No merge to main, no push, no export.
- Moving head throughout; register "Rulings of 2026-11-16 (U77)"; shaded not-possible block (6 entries); 8 IF-THE-RIG-ALLOWS marks; still 4 A4.
- Guide sws/procedures/prototype_test_ai_guide.md, 463 lines, linked from sheet and prototype stage.
- Technician USABLE WITH FIXES (minors taken); AI-helper test 16 guess points (offset contradiction the real one) fixed; falsifier pass 1 FAIL ("carriage" not on record), pass 2 PASS (3 minor, taken).
- Nine --check ok; SWS tests 180 (p52 out). idscan f806c68..HEAD 0 (1570 lines, 1 long skipped); scan_tree added 2 / removed 2, both on the re-rendered report.html line (same entry), 0 elsewhere.

— shroud
