# hawsepipe — U101 section A (falsify F1/F2 as numerical artefacts)

Worktree C:/Users/stian/Prosjekter-u101a, branch u101a-falsify, tip cb19ba7 (one commit on c19d94c).
Added only max/sws/3d/falsify/ (a_numerics.md, a_numerics.py, a_getdp.py, a_slope_noise.py, a_summary.py,
a_results/*.json). No merge, push or export. About 80 minutes of the 180.

Result
- BROKEN (F1 depths): the notes' air box (A = 0 at r 300 mm) holds back the field the saturated groove pushes
  outward. r 1200–2400 mm moves the zero for the 5.36 mm groove from 16.05 to 11.8–11.9 mm. Depths for zero at
  13/16/19 mm become 5.02/4.31/3.59 mm (notes 6.08/5.36/4.64). GetDP agrees in both boxes (≤ 0.16 mm).
  Without a groove the box matters little (0.3 mm). The repo's own domain_2d.json had flagged the 300 mm box.
- WEAKENED (F2 ratio): 4.9× → 3.9× at k 1, zero at 16 mm. Level −0.56 → −0.67 mT per 1 %.
- NOT BROKEN: the slope (0.37–0.42 mm per 0.1 mm); magnets 1 % weaker read as well under 1 % (+0.20 %, +0.02–0.30 %
  across 13–19 mm); mesh (3 refinements + corners), tolerance 1e-6…1e-13, B–H variants incl. the physical top and
  the 2.10 T step, stencil, element order 2 (GetDP).
- Side finding: the register steel table implies a falling magnetisation between 2.1 and 2.4 T (unphysical); no
  effect on the results. The "element maximum" over the groove is a corner value that does not converge.
- Consequence not tested here: F4 (magnet null 1.92–2.07 T), the bracket and the kernel test all used the 300 mm box;
  in the larger box the magnet reading at k 1 already crosses zero near the 19 mm position, so F4's null likely moves.
- Checks: build.py --check fails only on the stale report.html; tests/test_sws*.py 185 of 186 (stale report only).
  The full suite in the solver venv has unrelated environment failures (jsonschema missing, studio tests).
  scan_tree 0, idscan 0.
