# gripe — U103 (the 40 mm prototype head as drawn)

Worktree C:/Users/stian/Prosjekter-u103, branch u103-prototype-head from 1ded20a (verified = tip of u102-large-box).
Adds only max/sws/3d/falsify/h_*. Start 11:40, timebox 120 min (stop 13:40).

Log
- One base solve 17 s, 181 k nodes: zero at 16.67 mm lift-off (r 36.67), B_z at 16.5 mm −0.92 mT, rope 1.97 T.
- Side finding: bz_radius_2d.py (earlier prototype model) has the 1 mm step the other way round (seat dia 88 at the
  magnets, bore 86 between) and magnets R24–R44; the brief's drawing gives 86 at the magnets, 88 between, R24–43.
- Running cuts, brackets, level (mean z_d), box (1200 / 4800) in sequence, 2 workers.
- All 69 solves converged (~15 min). Zero 16.67 mm (r 36.67), bracket 15.91–17.82, steel end plates 22.76.
  Box 1200/2400/4800: 16.87/16.67/16.65. Level −0.442 mT/1 % at 16.5 (mean −0.440).
- Commit d137964. Checks: build.py --check 8/9 (report.html stale only, as base), test_sws* 185/186 (same),
  idscan 0 (13 entries, 8346 lines), scan_tree 0 on the added files (a git-ignored .pyc under falsify/ hits on the
  path; not committed). Falsifier running.
- Falsifier: 1 blocking (easy-read sentence 3 too close to a "which cut helped" verdict, missing "in the model"),
  9 minor (probe-reading caveat, one rounding +76→+75, node range, two claims firmer than numbers, cold-reader
  terms, one results table, magnetisation status). ~120 numbers checked against JSON, all match. All fixed;
  no second pass needed. Tip 02a9486; idscan 0, scan_tree 0 rechecked.
