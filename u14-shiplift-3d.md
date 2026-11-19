# u14-shiplift-3d — Sheave

## 2026-11-01 — started
- Unit / branch: U14 / u14-shiplift-3d (C:/Users/stian/Prosjekter-u14/max, from 43d62c2)
- Name: Sheave (the rope over the pier edge in the 3D view).
- Plan: read brief sources → find a local three.js (installed package / pip / npm only) → layout yaml + scene builder → 3D pane in SWS module → two-way link → tests → headless Edge screenshots → qc-falsifier → commit.
— Sheave

## 2026-11-01 — milestone: 3D pane renders, click-through works (not committed)
- three.js r157 vendored from the PyPI wheel nicegui==1.4.37 (pip download; no npm here). Files byte-identical, hashes in studio/vendor/three-r157/README.md.
- twin/geometry/shiplift-layout.demo.yaml (all DEMO [N]) + build_scene.py -> studio/modules/sws/scene3d.demo.json. 22 objects = 22 drawn chart instances.
- Kernel hook: shell.js profile mount/unmount/onDraw (3 call sites). Import map in index.html.
- In-browser checks green (statuses, both directions of the link, keys, local-only). Next: pytest file, screenshots, report, qc.
— Sheave

## 2026-11-01 — qc-falsifier running
- 117 tests green (25 new + 28 in-browser checks). Report tasks/reports/U14.md, screenshots tasks/reports/U14/.
- Waiting on qc-falsifier before committing.
— Sheave

## 2026-11-01 — committed
- Unit / branch: U14 / u14-shiplift-3d (C:/Users/stian/Prosjekter-u14/max)
- Commit: cb78b1c — U14 Shiplift 3D view
- Launch: .venv/Scripts/python -m max_core.cli studio --demo   (8765 is held by a running U13 Studio; close it or add --port 8766)
- qc-falsifier: pass 1 had 2 blocking findings (fixed, tested); pass 2 found none. 128 tests green.
- Ready for Kai's check: yes. Report tasks/reports/U14.md, screenshots tasks/reports/U14/.
- Needs Stian: bad-upstream look in 3D; scene scope (chart instances vs ~125 winches); reference lift + GA.
- Not pushed, not merged.
— Sheave

## 2026-11-01 — renamed
- Formerly signed Keel, renamed for uniqueness (Keel is the U10/U00 session's name). Commit cb78b1c and the report still say Keel; untouched.
— Sheave

## 2026-11-01 — mouse-zoom follow-up committed
- Commit: af5208b — Ctrl+wheel/pinch zoom with semantic level step, wheel/drag pan, Ctrl+0 fit; select() race fixed.
- Kernel touched (U13's): new kernel/wheel.js; shell.js (controller, apply after draw, selSeq); index.html (script tag, key hints).
- qc-falsifier: pass 1 one blocking finding (fixed, tested), pass 2 none. 136 tests. Screenshot tasks/reports/U14/u14-5-mid-zoom.png.
- Not pushed, not merged.
— Sheave

## 2026-11-02 — semantic zoom built, qc running
- studio/modules/sws/szoom.js: one continuous canvas, in-place expansion, text >= 11 px only, worst-status chips, faded context; 3D pane is a toggle (3), inspector collapses (I).
- 144 tests green (35 new in-browser). Frame sequence tasks/reports/U14/szoom/sz-00..10.png. Functional/Network switch: next.
— Sheave

## 2026-11-02 — semantic zoom committed, Studio restarted
- Commit: f72a0ca — semantic zoom on one canvas; 3D toggle (3), inspector toggle (I).
- qc-falsifier: pass 1 one blocking finding (stacked listeners), fixed and tested; pass 2 none. 144 tests.
- Studio restarted on 127.0.0.1:8765 from Prosjekter-u14 (background task of this session). Stian: reload the browser.
- Frame sequence: tasks/reports/U14/szoom/sz-00..10.png. Not done: Functional/Network switch; GIF (no PIL).
— Sheave
