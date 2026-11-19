# u13-studio-frontend — Weft

## 2026-10-31 — started
- Unit / branch: U13 / u13-studio-frontend (C:/Users/stian/Prosjekter-u13/max, from 6c7b03d)
- Name: Weft (the threads that cross the chart: lines).
- Plan: kernel (load + validate chart@0.1, draw, line language, value stream) → twin module (DEMO replay) → selector → agentic if time allows.
- Note: flow/STANDARDS.md, named in the brief, does not exist in this tree (checked Glob + grep). Proceeding without it.
— Weft

## 2026-10-31 — milestone: both modules render (not committed yet)
- Kernel (studio/kernel/), twin + agentic modules, `python -m max_core.cli studio --demo` works.
- 85 tests green (17 new for U13, 43 in-browser checks via local headless Edge).
- Next: TASKS.md, report, qc-falsifier, commit.
— Weft

## 2026-10-31 — qc-falsifier running
- Report written: tasks/reports/U13.md. Screenshots: tasks/reports/U13/*.png.
- Waiting on qc-falsifier before committing.
— Weft

## 2026-10-31 — committed
- Unit / branch: U13 / u13-studio-frontend (C:/Users/stian/Prosjekter-u13/max)
- Commit: adec874 — U13 Studio front end: module select + chart kernel
- Launch: `python -m max_core.cli studio --demo` (from the max folder, with the venv)
- qc-falsifier: pass 1 had 3 blocking issues (fixed, each now tested); pass 2 found none.
- Ready for Kai's check: yes. Report: tasks/reports/U13.md; screenshots in tasks/reports/U13/.
- Needs Stian: message line style (page: Open); whether U10's examples get `view` + `unit`; chart@0.2 hierarchy.
- Not pushed, not merged.
— Weft

## 2026-11-01 — follow-up started (Kai: SWS shiplift chart, deep zoom, fit)
- Plan: draft schema flow/chart.schema.0.2-draft.json (PROPOSED: frame nesting, instance paths, open items,
  udt bus type, s7udp/xplorer protocols); generated SWS shiplift chart in a separate folder so U10's
  0.1 tests stay untouched; kernel reads the draft only when a profile allows it; hierarchical zoom
  with per-level layout fitted to the viewport.
- Sources read (read only): spec rev127 §6, §7, §10; functional spec 3.2.1 and Table 1. Counts there are
  site-specific, so the chart uses [N].
— Weft

## 2026-11-01 — follow-up built, qc running
- SWS shiplift chart (PROPOSED 0.2 draft), nested zoom to channels, every level fitted. 92 tests green.
- Screenshots: tasks/reports/U13/sws-1..5-*.png. Report section "Follow-up 2026-11-01".
— Weft

## 2026-11-01 — follow-up committed
- Commit: 709e544 — U13 follow-up: SWS shiplift chart, nested zoom to channels, fitted levels
- Launch: python -m max_core.cli studio --demo (opens on "Twin: SWS shiplift")
- qc-falsifier: pass 1 had 2 blocking issues (Xplorer values; logger ingests not open), both fixed and tested; pass 2 found none.
- Ready for Kai's check: yes. Not pushed, not merged.
- Needs Stian: chart@0.2 draft yes/no; SWS transport and logger ingests (11 open points in tasks/reports/U13.md).
— Weft

## 2026-11-01 — scale/transport update committed
- Commit: d9b80bf. Scale ~250 SWS (estimate) at the shiplift level; transport halves -> base station -> MQTT -> iba; badges no longer overlap.
- qc-falsifier: no blocking findings. Not pushed.
— Weft

## 2026-11-01 — rooms + fiber committed
- Commit: 43d62c2. Main control room + HIL room at the shiplift level; fiber as a link attribute (fact, no [OPEN]).
- qc-falsifier: no blocking findings. Not pushed.
— Weft
