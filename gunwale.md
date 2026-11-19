# Gunwale — U25b (P52 redo: magnet one piece per half)

Started 2026-11-07. Brief: last section of kai.md. Worktree C:/Users/stian/Prosjekter-u25, branch u25-sws-p52-prototype.

## Notes
- max/CLAUDE.md on this branch has rules 1-7 only; rule 10 (build to a cited design) is on main. Following main's rule 10.
- [R29] read (sws_data_sources.md l.67, table row l.153); consolidated findings §1 l.12 agrees. No contradiction found.
  Note for supplier list: the [R29] row asks max one-piece size "at Ø 68–92 × 40 mm"; P52 half-ring is Ø64/105 × 40, bigger.
- head.py: n_seg/bond/seg_angle/seam_centres removed; arc_angle = 178.209°, magnet_cuts = split set-back only. 808.2 g per half-ring, 3.233 kg total.
- Tests: 5 passed (new: one piece per half; STEP has 4 magnet solids).
- Old seams json git-rm'd. build.py --only p52 started (seams re-solve + fault --fresh + summary), sequential, nothing else running.
- Item-6 docs fixed: README, THEORY S1, verification 349/375/592, reconciliation 13, design_inputs 3, params.yaml note; model3d docstring.
- Split set-back re-solve (90° sector, box 300, level 1): closed 431 265 / set-back 776 317 unknowns, 59 / 94 s, 7 Newton each.
  dB_rope −1.794 mT (−0.0920 %) for 0.995 % magnet removed (3D-B rule predicts −0.0915 %). Halves force −663.6 … −669.9 N.
  Hard +80 N40SH lm 20.5: 1.9294 − 0.0018 = 1.9276 T. Easy −40: 2.0352 T.
- ADDENDUM from Kai (Stian's rulings 7 Nov): service corners −40/+45 °C; +80 only as "spec qualification margin" row;
  N52 and N48SH side by side (+N40SH row); knee check at +45/+60 on 40 and 52 mm ropes; no grade recommendation.
  Conflict to report: brief item 3 says "recommend lm"; addendum says never pick. lm depends on the grade -> options only.
- Added head.GRADES / magnet_law / case(grade=), run_p52 --grade, p52/grades.py (2D size + demag/ceiling).
- 2D sizing (floor only, no margin): N40SH 18.17 (+45) / 19.04 (+80); N48SH 16.64 / 17.41; N52 15.93 / 16.65 — reproduces the register row at +80.
- 3D queue logs/p52_grades_queue.sh started after the build (one solve at a time).
- 3D grade queue done (15 cases). Sizing at hard +45 (1.92 + 2.2 mT): N52 16.72 (2.52 kg), N48SH 17.45 (2.65), N40SH 19.02 (2.95).
- 2D knee: N52 40 mm rope 22 % beyond knee at +45, 63.5 % at +60; crosses +62 (52 mm) / +28 (40 mm) / −27 °C (empty head). N48SH/N40SH none below +80.
- Second addendum: fig_envelope.png done (p52/fig_envelope.py, results/p52/envelope.json).
- Final build --only p52 at 17:23: p52_seams failed "Could not allocate localheap": another session's Python
  multiprocessing job (parent PID 39300, system python, ~23 GB, started 17:16) was running. Not mine; did not re-run
  heavy steps alongside it. Earlier full --only p52 at 16:42-16:55 was clean (seams + fault reproduced). Light steps re-run clean.
- Tests 11 passed; docs/sws/build.py --check ok; grep "segment" sws/3d/p52 empty.
- QC falsifier: no blocking findings; 10 non-blocking, 7 fixed (offset −1.40, 2.0351 one method, cross-grade offsets stated, force comparator, 2.3 mT/% source, stale U25.md lines, old QC marked void for segment items).
- Committed 9748537 on u25-sws-p52-prototype (not merged). Done.

— Gunwale
- Kai's verifier fixes applied, QC no blocking. Committed ab635a4. Deviation: alpha(Hcj) and the knee are in the register (l.130, l.182, A), so they are tagged as register values; only N52 Hcj 0.88 got the "unrecorded" tag.

— Gunwale
- Codex review: 9 items fixed, QC blocking item (+0.5 mm overclaim) fixed before commit. Committed 44ce9cd.

— Gunwale
