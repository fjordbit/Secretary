# rudder — U95 builder notes

- Started U95 (axial sensor at different lift-offs). Worktree C:/Users/stian/Prosjekter-u95, branch u95-axial-liftoff from 062b8bd (verified = local main).
- Starting state verified: Prosjekter-u05 HEAD = main = 062b8bd, clean.
- Script sws/3d/demo/axial_liftoff.py (reuses defect_sweep.full_model; probe read-out as defect_sweep.readouts). Re-solves rather than reading the U92 grids: the grids are "for pictures only" and straddle the yoke face; U92 grids used as a cross-check instead (--grid-check). One solve ~2.5 s; H40 full run ~6 min.
- First run: rope +1 % comparator at 1 mm lift-off was garbage (stencil reached into the thicker rope's skin annulus). Fixed stencil d = min(1, (r_mo-r)/2, (r-1.01 r_rope)/2); 3 mm row still reproduces U92 (-41.93 mT, -14.79 mT, levels -1.62/-2.00, magnet drift +0.52 mT).
- Physics: B_z changes sign just in front of the yoke face (lift-off ~22.6-22.8 mm, r ~42.6-42.8; yoke face at 43.2). Plausible: yoke carries the return flux the other way.

— rudder
- Commit a105fbd on u95-axial-liftoff. Checks: 8/9 --check (build.py: report.html stale only because it embeds the register; rebuilt+diffed = only the new register row; restored, not committed, brief says no HTML), pytest 180/181 (test_sws_report, same cause), idscan 0 (12797 lines), scan_tree 0 on added files and lines.
- 52 mm: tool took H52,52,hard,25 unchanged; full (a)-(e) done.
- Falsifier running.

— rudder
- Falsifier pass 1: FAIL, 2 blocking (easy-read named the TMR2584 limits as the axial part's without the register's "stated, photo wanted"; short fault / long loss / ring-vs-wire not defined above the line) + 12 minor (rounding x6, sum 4.0 not 3.9, grid 7 % for wear, 9 vs 10 mm at 5 mm off, -54 mT, drift signs, 23 mm rope cell, causal claim on ring tail, guard is air, unverifiable 25.4). All taken. No second pass (nothing blocking left).
- Tip 5f5bbc5. Rechecked: 8/9 --check (build.py report.html stale, register row only), pytest 180/181 (same), idscan 0 (12817 lines), scan_tree 0.
- Owed: rebuild docs/sws/report.html at merge (register row); the yoke cut-out unit (not started); a broken wire (3D) at large lift-offs; prototype measurement.

— rudder
