# catspaw — U111 element run 3 (builder notes for Kai)

- Worktree C:/Users/stian/Prosjekter-u111, branch u111-element-run from b568641 (verified = tip of u107-tradeoff-map).
- Adds only max/sws/hw-selection/element_run_3/ (note, 5 scripts, terms, source, 4 JSON, figures E1a/E1b/E2/E3).
- Base points: N52 x 0.95 (18.1 mm) lines 13/16/19 and N48SH x 1.00 line 16 from tradeoff summary.json (middle curve,
  large box, rope ~1.97 T). Solved here (e_fields.py): 38 standing/level solves, all converged (10-11 Newton steps,
  164-252 k nodes): rope curve low/high, magnet at -40/+50 C (alpha -0.12 %/K, magnet only), 4 surroundings
  (16 mm only), no groove (level, magnets -1 %, spreads). Logs in the scratchpad (local paths), not in the repo.
- Wire signals are the 3D values of c_third_dimension (old box); 8 mm wire values derived by the ring's 8/5 ratio.
- Sheets read by a subagent (general queries, part numbers only); several MultiDimension sheets are earlier local
  copies without a re-confirmed address; TMR2584 web page 403. TMR2583 offset unit truncated on its sheet.
- Key numbers: radial at 5 mm: along ~0 (2.9 mT/mm off-plane), across -30.7 (-36.2..-26.3) mT, ring 5.07 mT, inner
  wire 0.113 mT; axial at 16 mm: B_z +0.09, spread -5.3..+4.5, level -0.774 mT/%, needs -15.6..+7.1 mT (groove),
  -21.3..-13.9 (no groove). Magnet temp at zero: 0.4 % vs 11 % of metal without groove.
- figkit vline marks get no slide label (module gap, not changed): x-axis label of the E2 slide carries it.
- Checks: build.py --check 1 problem (report.html stale, as base); pytest tests/test_sws_* 185/186 (report, as base).
  The u05 venv lacks `markdown`; checks run with the solver venv.
- Falsifier (fresh subagent, files only): 0 blocking; 15 minor. Fixed: drift vs hysteresis wording, 11 -> 9.5 mT
  (10.7 with off-plane), derived noise marked (d), three-axis TMR fails on range not noise, 26-36 mT, DRV5055 lifetime
  unit flagged as read differently in two runs, MLX91377 noise 0.26 mT p-p carried, "cannot saturate" softened,
  1.1-3.3 mA, aluminium ~7 %, +0.019 mT, E2 TMR2584 line named "best case" with per-K value in hover, E3 title.
  Not fixed: E2 vline legend entries look alike (module gap); slide label DRV5055 near the edge; roles "owner" /
  "outside expert" kept (the brief's own words). No second pass.
- Commit 213e36c on u111-element-run. idscan b568641..HEAD 0; scan_tree 0. No merge, push or export.
