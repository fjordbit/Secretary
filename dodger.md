# dodger — U92

## 2026-11-18 13:58 — started
- Unit / branch: U92 / u92-lma-sweep-video (C:/Users/stian/Prosjekter-u92, from 8f1822e — verified = tip of u91-board-arrangement)
- Timebox 150 min (to about 16:28).
- Venv used: C:/Users/stian/Prosjekter/max/.venv (the only one with ngsolve, scipy, pyvista, imageio-ffmpeg; u41 venv has pytest only, used for --check/pytest). Nothing installed.

— dodger

## 2026-11-18 14:19 — committed
- Commit 6a1d5ba on u92-lma-sweep-video (C:/Users/stian/Prosjekter-u92/max).
- Default defect_sweep run reproduces the old npz (C:/Users/stian/Prosjekter/max/sws/3d/out/) bit for bit (dsig, sig0, dfield max diff 0); peak dBz -14.79 mT.
- Long cases on a +-700 mm box (default +-400 cannot hold 300 mm plus a sweep that leaves the head); box check of standing values done. (d) 1200 mm not run (needs ~+-1500 mm box).
- B_z under a pole is mesh-sensitive without mesh lines at the pole centres (-10.4/-5.5 mT vs ~-3.4 mT); --pole-lines added, used for all LMA runs.
- Video part 2 = case (c) corrosion, candidate = rope flux. v2 720p 42.8 s.
- Checks: 8 of 9 --check ok; build.py --check FAILS (report.html stale) and test_sws_report fails (180/181) — both only because report.html embeds demo/README.md, which the brief told me to update; verified by a rebuild + diff (only the README section changes), report.html restored, not committed (U93 owns pages). idscan 0 (27862 lines); scan_tree on added/modified files 0.
- Falsifier: running.

— dodger

## 2026-11-18 — done
- Tip d19aa6e on u92-lma-sweep-video (C:/Users/stian/Prosjekter-u92/max). No merge, no push, no export.
- Falsifier pass 1: FAIL on 2 blocking -> fixed (JSON unit of the integrated read-out T·m -> mT·m; short drift table now 2.6-3.2 % / 0.5-0.6 % against both 10 % cases). 10 minor, all taken (yoke steps, limits wording, bipolar ends, mT sign, box notation, B_r noise, broken-wire caption, discard-level source in README, (d) "expected", cold-reader terms). Video re-rendered. No second pass.
- Rechecked: 8 of 9 --check ok, build.py fails only on report.html stale (embeds demo/README.md; HTML is U93's); pytest 180/181 (test_sws_report, same cause); idscan 0; scan_tree 0.
- Owed: rebuild docs/sws/report.html at merge (after U93); link the v2 video from a page (U93 / pages).

— dodger
