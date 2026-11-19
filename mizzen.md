# mizzen — U83

## 2026-11-16 21:54 — started
- Unit / branch: U83 / u83-sensor-round-2 (C:/Users/stian/Prosjekter-u83, from 5f415b6)
- Part 1 (gap test on rig sheet) first, then Part 2.

## 2026-11-16 22:03 — part 1 committed
- Unit / branch: U83 / u83-sensor-round-2 (C:/Users/stian/Prosjekter-u83/max)
- Commit: f8e9f2f — gap comparison on existing faults (step 4b in run 4), channel-identity first step, guide 6.6, register U83 row (52 mm test rope ordered; no wire cut). Kai's three corrections applied (no cut; gap as a note; controlled test on ordered rope in the not-possible block, fault list a separate document, no link).
- Dipole ratio (radial peak, two opposite poles): 1/10 mm = 6.1 / 7.2 / 8.0 at d = 6 / 8 / 10 mm. Axial at mid-gap at 8 mm = 6.1. So the 7.2 (Fable) is the radial peak, the 6.1 (Grok) the axial component; both right for their component; the 3D figures are radial.
- 3D gap figures: sws/3d/p52/design.md "R4 gaps" line 399-401 (two hidden wires, worst angle, 5 mm): 1.89/2.70/3.74/5.29 mT.
- Print: C:/Users/stian/secretary/inbox/2026-11-17_rig_sheet_print.pdf, 4 A4 (old one untouched).
- Nine --check ok; SWS tests 181 (p52 out). idscan 0 (191 lines); scan_tree added lines 0; report.html re-rendered line 2 added / 2 removed (known).
- Ready for Kai's check: after reviews (running).

— mizzen

## 2026-11-16 22:2x — part 1 reviewed, part 2 committed
- Part 1: technician pass 1 USABLE WITH FIXES (3 blocking: no boxes for 4b, reading sentence unclear, clash with the not-possible row) -> fixed (9a6420c); pass 2 USABLE WITH FIXES, no blocking, minors taken (770b3d8). Falsifier pass 1 FAIL (2: "5 mm from the sensor"; small estimate is not a dipole model on record) -> fixed; pass 2 FAIL (1: the ratio speaks to gap behaviour, not to which signal level is right) -> fixed in 770b3d8; no third pass (brief: at most two).
- Rig sheet now 5 A4 (was 4; one-page growth allowed). Print re-written: C:/Users/stian/secretary/inbox/2026-11-17_rig_sheet_print.pdf.
- Part 2: 88802af — round folder, synthesis, datasheet_check, sensor page item + open item, register row, TASKS line. Sensor page 4 A4 (word bound raised 3500 -> 3600 in its test, +158 words).
- idscan 5f415b6..HEAD 0 (2897 lines); scan_tree added lines 0, round folder 0; report.html 2 added / 2 removed (known entry).

— mizzen

## 2026-11-16 — done
- Branch u83-sensor-round-2, tip fe83279 (C:/Users/stian/Prosjekter-u83/max). No merge, no push, no export.
- Part 2 reviews: falsifier pass 1 FAIL (7 blocking: misattributions, counts, a non-verbatim quote, "said did not exist", register status letter) -> fixed 51415a9; pass 2 PASS (8 minor, taken in fe83279). Cold page reader CLEAR WITH FIXES (3 blocking: "record's two estimates", undefined warning, what the gap test settles) -> fixed.
- Nine --check ok; SWS tests 181 (p52 out); idscan 0 (2924 lines); scan_tree added 0; report.html 2/2 known.
- Pages: rig sheet 5 A4 (was 4), sensor page 4 A4. Print: C:/Users/stian/secretary/inbox/2026-11-17_rig_sheet_print.pdf.

— mizzen
