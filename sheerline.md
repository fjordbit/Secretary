# sheerline — U107 trade-off map (builder notes for Kai)

- Worktree C:/Users/stian/Prosjekter-u107, branch u107-tradeoff-map from 1bd304c (verified = main); merged
  u106-groove-plots (d112319) first, no conflict.
- Adds only max/sws/3d/tradeoff/. Large box r 2400 x z +-2400, A = 0, middle rope curve, 25 C.
- Magnet knob: real thicker magnet (N52 net; N48SH standing net + 16 mm line), as f_magnet_mech. Knob k not
  used for the net (not a buyable magnet above ~1.14x); wp.json (large box) quoted for comparison only.
- 540 solves, all converged, 2 workers. Logs (local paths) kept in the scratchpad, not in the repo.
- Short-ring dB_r read with the ring fixed at z_d 0 and the read point moved 0-14 mm along the rope; checked
  against moving the ring: -0.7 / +2.5 / +0.9 % at 3 / 5 / 8 mm. Zero plain mesh vs fault mesh 0.004 mm.
- Findings: zero at 16 mm holdable to ~2.04 T (N52 x1.65, 31.5 mm, groove 10.65 mm, 1.3 mm steel). Rope reaches
  2.2 / 2.3 T at N52 ~x2.1 / x2.8 only without a usable zero (26+ mm). Along 16 mm: depth 2.1 -> 9.2 mm for
  1.94 -> 2.03 T (more groove); radial 3 mm 7.9 -> 11.6 mT; level 0.35 -> ~0.95 mT/% flat above 2.0 T.
  Groove for 16 mm at model magnet: radial 3 mm -9 %. Radial 3 -> 5 / 8 mm: -46..49 % / -71..74 %.
- Part 5 sheets gathered by a subagent (general queries); figures re-checked into tradeoff.md section 5.
- Not changed: plotstandard.py, figkit.py (legend columns done in tkit.legend_columns after the fact).
- Checks: build.py --check 1 problem (report.html stale, as base); pytest tests/test_sws_* 185/186 (report).
- Falsifier (fresh subagent, files only): 6 blocking (no-groove magnet read-as sign/value -0.75 -> -1.44 %;
  cal 3 mm moved value 9.71 not 9.83; 22.7 not 22.8; inner-wire margin inductions 2D-step vs 3D not said;
  plain words TMR 0.1-0.9 mT left out the per-K reading; three old-box quotes not marked) - all fixed. Minor
  fixed: level_zero rounding, +18 %, noise wording, bridge current, hatch caption, noise-band reconciliation;
  F redrawn (zero labels, lighter hatch, magnet-thickness rings, slide without radial contours). No second pass.
- Commit b568641 on u107-tradeoff-map (on top of the u106 merge 20c009e). idscan 1bd304c..HEAD 0; scan_tree 0.
