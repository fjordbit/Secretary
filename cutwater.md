# cutwater — U93

## 2026-11-18 — started
- Unit / branch: U93 / u93-ld-lma-wording (C:/Users/stian/Prosjekter-u93, from 8f1822e — verified = tip of u91-board-arrangement)
- Timebox 120 min.

— cutwater

## 2026-11-18 — committed
- Commit b13d669 on u93-ld-lma-wording (C:/Users/stian/Prosjekter-u93/max).
- Corrected 17 places in 11 files (verification.md x5, p52/design.md x1, THEORY.md, design_inputs.md x2, 3d/README.md, fem-2d/MANIFEST.md, run_3dd.py, fig_u16.py x3, bz_radius_2d.py, fig_bz_radius.py, make_u32_figures.py) + build.py open-list line + sensor page line. Regenerated u32_faults_3d.png ("local LMA" -> "local loss") and bz_radius_sweep_{P40,H52}.png. Not rerun: fig_u16 (rewrites u16_summary.json from all 3dd_*.json) -> u16_alpha/u16_profile PNGs owed.
- Kept with verdict: "LMA %" columns (size of fault, allowed); LMA_Bz result keys (U56 rule: keys not renamed); tasks/reports (history); spec text and old revs (redline only); consolidated findings / reconciliation (dated record quoting spec); correct LMA usage on hardware, procedures, rig sheet, literature, sync, link-readout notes.
- U92-owned, listed not touched: demo/README.md "an LMA-type defect", defect_sweep.py, make_video.py (caption "(LMA)"), make_deck.py "(LMA type)".
- Note s-ldlma on sensor page; lma_sweep.md named only in a span title (no link, link check unaffected). Register: one line in the R11 entry kept single-line (two lines shifted every REG line citation — caught by build WARNs, fixed).
- Nine --check ok; 181 SWS tests; idscan 0 (2918 lines); scan_tree added 0, binary 0, report.html 2 = 2. Sensor page 5 A4 (headless Edge), words 4849, bound 4400 -> 4900.
- Falsifier: running.

— cutwater

## 2026-11-18 — done
- Tip 8c7c045 on u93-ld-lma-wording. No merge, no push, no export.
- Falsifier pass 1: PASS, 0 blocking, 11 minor; 10 taken (LD spelled out, "larger loss than LD detects", "table below", drift "especially important", design_inputs long loss "not calculated, may give", easy video line "caption inside the video", base-trace wording off the clause's phrasing in register + redline 7/10, redline 8 "% lost metallic area", fem-2d/README). Not taken: "corrected two-part version is in work" (brief asks for it); consolidated findings l.131 (dated record).
- Rechecked: nine --check ok; 181 tests; idscan 0 (2919 lines); scan_tree added 0, binary 0, report.html 2 = 2; sensor page 5 A4.
- Corrected places total: 21 in 14 files (incl. fem-2d/README).
- Merge note: report.html will conflict with U92 (it renders demo/README); rebuild after merge.

— cutwater
