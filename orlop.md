# orlop — U101 section C (the third dimension), falsify F1, F2, F6

Worktree C:/Users/stian/Prosjekter-u101c, branch u101c-falsify from c19d94c (verified = tip of u100-h52-sweep).
Tip 1d52b57. Files only under max/sws/3d/falsify/; note c_third_dimension.md. No merge, push or export.

## Runs (never more than two solver processes of mine)
- c_split_3d.py: 90° sector, H52/52, hard, +25 °C, k 1, groove 20 × 5.36 mm, box 300 × 700; split slab its own
  solid, so closed / magnet-only / both share one mesh per gap (1, 0.5, 0.2 mm). 9 solves, all converged.
  A first attempt at level 0.7 (313 k elements) was stopped as too slow beside the other sections.
- c_wire_k.py: run_3dd.py driven in-process (magnet × k, groove via head_mod, extra band at 16 mm), half-space,
  L_h 15, level 1.5, faults 1king and deep_wire; k 0.87 / 1.48 / 2.35 (3D 1.881 / 1.989 / 2.093 T) and k 1 groove
  on / off. 15 solves, all converged.

## Results
- 3D closed head reproduces the 2D zero: 15.98 against 16.07 mm; slope 3.08 against 2.99 mT/mm.
- Split up to 1 mm: zero −0.08 mm (magnet + yoke cut) / +0.06 mm (magnet only), uniform over φ to 0.007 mm;
  offset +0.25 / −0.19 mT at 16 mm = −0.45 / +0.34 % of metal per mm; linear in g.
- One outer-strand wire, 5 mm: 1.17 / 1.35 / 1.36 mT → 5.9 / 6.7 / 6.8 × (S ÷ 2 × 0.10 mT p-p).
- One inner-rope wire below the jacket, 5 mm: 0.113 / 0.231 / 0.301 mT → 0.56 / 1.16 / 1.51 ×; margin 1 near 1.96 T.
- Groove at fixed magnet: rope −0.021 T, outer wire −3 %, inner-rope wire −17 %.
- Axial element at 16 mm, one outer wire: 0.14–0.16 mT, groove on or off.

## Checks
- build.py --check: 1 problem, stale report.html only. pytest (no single venv has all deps; ran Prosjekter/max venv
  with u05 site-packages on PYTHONPATH): sws tests 185 passed / 1 failed (stale report); whole suite 772 passed,
  2 failed (stale report + test_review_round models-file backends {claude,codex,cursor} vs +xai, in-repo at c19d94c,
  not touched). Brief's "180 of 181" count differs from 186 here.
- idscan c19d94c..HEAD 0; scan_tree on falsify/ 0.

— orlop
