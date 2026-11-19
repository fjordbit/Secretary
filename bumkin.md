# bumkin - U101 section B notes

- Worktree C:/Users/stian/Prosjekter-u101b, branch u101b-falsify from c19d94c (verified = u100-h52-sweep tip).
- Tip 3f2589a. Added only max/sws/3d/falsify/b_* (note b_tolerances.md, three scripts, JSON). No merge, push, export.
- About 470 solves, two workers, ~3.8 s each; ran 22:47-23:29.
- Base reproduced: zero 16.07 mm, magnets -1 % +0.45 %, rope 1.924 T (as h52_groove).
- Main result: F1 not broken (zero 0.36-0.45 mm per 0.1 mm depth; steel bracket moves the depth +-0.3 mm).
  F2 offset holds (+0.39...+0.53 %), but at the modelled magnet the level scales 2.5-3.2 % per 1 % of magnet:
  -20...+45 C changes the level -7.7...+18 % (N40SH), -4.7...+7.9 % (N52). F4 null 1.969 T, steel bracket
  1.962-1.976 T, weak ring 1.968 T: not broken.
- Checks: build.py --check fails only on stale report.html (1 problem). pytest: no venv found with both markdown
  and jsonschema; with Prosjekter/max/.venv the test_sws* set is 185/186 (only test_sws_report fails); full suite
  there 72 failed / 637 passed, environment (studio, jsonschema), not this change. Could not reproduce "180 of 181".
- idscan 0 (13 entries); scan_tree 0 (10 files).
