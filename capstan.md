# Capstan — U25 (SWS P52 yoke and magnet prototype design)

Name: Capstan. Worktree C:/Users/stian/Prosjekter-u25/max, branch u25-sws-p52-prototype from 023da1f.

## 2026-11-07 — started
- Worktree created, CLAUDE.local.md copied. Reading the READ list now.

— Capstan

## 2026-11-07 — environment
- The brief's venv (Prosjekter-u05/max/.venv) has no netgen/NGSolve. Using C:/Users/stian/Prosjekter/max/.venv
  read-only, as U16/U19 did (NGSolve 6.2.2608). sws modules resolve to the u25 worktree (checked); max_core resolves
  to Prosjekter/max (editable install), so tests run with PYTHONPATH=C:/Users/stian/Prosjekter-u25/max.
- The U17 report is not on this branch; read from Prosjekter-u17 (read-only) for §0/§6.

— Capstan

## 2026-11-07 — plan and assumptions (read list done)
- Plan: p52/head.py (design table + FE case + full-360° OCC solid + STEP), p52/run_p52.py (stranded 10° sector at
  boxes 300/600/1200, L_h 180, both corners; 90° sector homogeneous rope for the segment seams + split set-back
  and the halves force; one half-space fault run via run_3dd --head P52).
- ASSUMPTION (would stop me, so stated): the outside notch is kept exactly as drawn on P40 (10 mm wide x 2 mm deep at
  mid-length); it holds no sensor. The 16 TMR and the axial sensor sit inside the yoke bore between the poles
  (R 29 and R 36.5); "sized for" is read as: the sensor zone (yoke bore between the poles, R 30 ... r_mo - 1) must
  hold them, which it does. QUESTION for the head designer via Stian: what is the outside notch for (clamp band,
  cable, label)? Its depth stays an open input.
- ASSUMPTION: magnet grade sized on the params.yaml N40SH minimum Br 1.25 T (as every result so far); N48SH stays
  the preferred grade (A). A real N48SH minimum Br would only raise B_rope.
- ASSUMPTION: 12 radially oriented arc segments per ring (6 per half, 30° pitch), bond line 0.1 mm, magnet faces
  set back 0.5 mm from the split plane at the bore (magnet-only gap, yoke halves steel-to-steel), all [A].
- ASSUMPTION: 1 mm yoke shoulder between the poles (yoke bore r_mo - 1 there), as the head designer drew on P40.

— Capstan

## 2026-11-07 — first numbers (stranded rope, hard +80 °C, box 300 × 400, L_h 180, 10° sector)
- P52 yoke "plain" (= U19 H52 at a 12.0 mm wall): B_rope 1.939004 T against U19's 1.938991 T. The model reproduces U19.
- Outer notch 10 × 2 mm: −0.19 mT. The P40-style 1 mm steel shoulder between the poles: −4.1 mT (worth ~0.4 mm of
  magnet). DECISION (mine, reversible): the design drops the steel shoulder; the magnets are located axially by a
  non-magnetic spacer. Flag to the head designer.
- Observation (not mine to fix): the magnet volume-mean working point is 0.666 T with the stranded section under the
  poles against 0.692 T homogeneous (same in U19's JSONs). B_rope differs by only 0.1 %. Worth a look by whoever does
  the next demag check.

— Capstan

## 2026-11-07 — floor decision (hard +80 °C, stranded, flux definition)
- Box 1200 × 1600, L_h 180: lm 19.1 / 20.0 / 20.5 / 21.0 mm → 1.91674 / 1.92622 / 1.93137 / 1.93644 T (≈10.3 mT/mm).
- Unbounded (Aitken + 7e-4, U19 method): lm 19.1 → 1.9141 T (U19 H52 1.915); lm 20.5 → 1.9294 T before seams.
- Decision: lm 20.5 mm (smallest 0.5 mm step with ≥ 2.6 mT margin after seams; numbers in design.md §2).
- Seams run crashed on a read-out bug (dict key 'ne' twice), fixed, re-queued after the easy corner and the fault run.

— Capstan

## 2026-11-07 ~04:25 — all solves done, QC running
- Design: lm 20.5 mm; B_rope 1.9269 T unbounded with segments (margin 6.9 mT), easy −40 °C 2.0345 T.
- Seams −2.48 mT (3D-B rule predicts −2.46). Halves attract ~657 N. Fault B_r 3/5 mm 4.50/2.68 mT.
- docs/sws/index.html regenerated (tests/test_sws_report.py requires it current after the README/verification edits).
- Questions for Stian (also in the report): (1) 20.5 or 20.2 mm (depends on the supplier's radial orientation);
  (2) drop the P40 steel shoulder (−4.1 mT)? (3) EN 12927 §14: B_rope or B_wire (B_wire needs ~21.5–22 mm).
- Question for the head designer (via Stian): what is the P40 outer notch for, and its real depth?

— Capstan

## 2026-11-07 ~04:40 — done, ready for Kai's check
- Commit 55844ed on u25-sws-p52-prototype (not pushed, not merged). qc-falsifier: no blocking findings; 9
  non-blocking fixed. Tests: 10 passed. Report tasks/reports/U25.md; design sws/3d/p52/design.md.
- STEP is git-ignored: regenerate with `python p52/head.py` → sws/3d/out/p52/P52_head_lm20.5.step (present now).

— Capstan
