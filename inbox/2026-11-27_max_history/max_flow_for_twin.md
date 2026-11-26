# The MAx flow for the digital twin: what was said, started and delivered

Question: the twin drawn and run in the MAx flow view (top view, sub views, protocols as boxes at lower zoom,
connection diagrams, the zoom chart with demo data, wiring the twin into the flow). Sources: secretary logs,
START.md, inbox/2026-11-23_dt_plan.md, agent-notes (u10, u13, u14, bunt), read-only look at main (Prosjekter-u05).

## In date order

| Date | Said / asked / promised / started / delivered | Source |
|---|---|---|
| 23 Oct | Owner: the twin is paused and is designed inside MAx (dynamic model from control lab, PLC code in PLCSIM Advanced). | log 23 Oct |
| 29–30 Oct | Delivered: U10 (design only) — one chart format for MAx and the twin (ADR 0007), twin/DESIGN.md, a `twin.platform_load` tool contract; wrapping it "waits until the twin is built". | log 29 Oct; u10 notes |
| 31 Oct | Owner asked: Studio with a module choice (agentic / twin), shared chart kernel, twin first, value lines and line thickness by the line language. Delivered U13; all twin lines one thickness, chart ran off the edge. | log 31 Oct |
| 1 Nov | Owner gave the working layout L1 shiplift → L2 base stations → L3 winch → L4 2 SWS → L5 2 halves → L6 channels. Delivered: SWS shiplift chart with nested zoom to channels, chart 0.2 draft (PROPOSED), scale card ~250 SWS (owner's estimate), MQTT base station → iba, fibre, control room and HIL room; 3D view; Ctrl+wheel zoom. | log 1 Nov; u13, u14 notes |
| 2 Nov | Owner: semantic zoom missing. Delivered same day: one canvas, frames open in place, 3D as a toggle (f72a0ca). Builder: "Next: Functional/Network switch (needs network grouping data)". Studio merged to main 91897db. | log 2 Nov; u14 notes |
| 3 Nov | Owner's priority: SWS first, then MAx flow / agentic; "twin can wait a while". | log 3 Nov |
| 4 Nov | Owner's root rule: one level, zoom shows the inside, what you see is what runs, no hidden inputs — "same rule for the twin". Chart 0.2 to accept all of 0.1; the message envelope recorded in twin/DESIGN.md (done). | log 4 Nov; twin/DESIGN.md l.26 |
| 4–6 Nov | Asked: chart 0.2 (D4), adopt or not. Last on a waiting list 6 Nov. No answer recorded. | logs 4–6 Nov |
| 20 Nov | Owner: the MAx principle view (system, zoom level by level to one half) is "a nice view"; wants one page with all SWS. Delivered: presentation round (U118) and the twin replay page (U120), both on branches, not merged. Neither uses the MAx chart. | log 20 Nov |
| 23 Nov | Owner: signalling is handled in MAx; the earlier zoom view (shiplift → 3 main stations → 51/3 winches → 2 SWS) may be the better structure; one version had far too many winches. Kai's sweep and plan: zoom chart is demo data, no twin code behind it, scale card "~125 winches"; plan step 4 "the structure is the MAx zoom; the chart's counts are corrected at the same time". Each step needs his go. | log 23 Nov; dt_plan.md |
| 25 Nov | DT facts page (U127, unmerged) lists as waiting: "chart scale card to 102 SWS / 51 winches / 3 stations and the test asserting the old card"; open for him: "draw all 51 winches in the chart or fewer". | log 25 Nov l.55–58 |
| 25 Nov | Started on his go: full-scale plant in the simulator (U132), with a fault interface for a trainer screen. Built in the simulator only; the chart was not touched. | log 25 Nov |
| 26 Nov | Owner: all of the twin runs out of or through the MAx flow; the SWS flow has the top "all" view and the sub views; protocols are boxes in the flow line diagram at the lower zoom. Kai: agreed in concept; "wiring the twin into it is a task". Plant corrected to two sides (U137, unmerged); its notes list the chart's generator among the places still at the old size. | log 26 Nov; bunt notes |

## What exists today, and where

- **Studio with the chart kernel, semantic zoom and 3D view** — on main, `Prosjekter-u05/max/studio/` (zoom:
  `studio/modules/sws/szoom.js`); launch `python -m max_core.cli studio --demo`.
- **The SWS shiplift chart** — `max/flow/examples-0.2-draft/sws-shiplift.chart.json` and its generator
  `make_sws_shiplift.py`. Placeholder layout 2 base stations × 3 winches × 2 SWS × 2 halves; scale card still
  `SWS_TOTAL_EST = 250` (~125 winches). Protocols appear as line attributes (MQTT, S7 UDP, drive data), not as
  boxes. Last change 20 Nov (converter count only).
- **Design:** ADR 0007 and twin/DESIGN.md on main; ADR 0008 (core, modules, rule packs) on branch
  u10-twin-design only, PROPOSED.
- **The engine** runs MAx agent charts only (default loop, architect-writer-judge, PLC improve). No twin chart
  can be run; `twin.platform_load` is a contract only.
- **The twin itself** is the simulator in `max/sws/line_beta/` (full-scale plant, temperature, reduction; one
  side on main, two sides on u137). It has a plant hierarchy (side → station → ropes) but no link to the chart.
- **Replay page** (u120) and **screen designs** (u118): branches, not merged, not linked to the chart.

## Started and never reported back

- **Functional / Network switch** in the zoom view: named as the next step on 2 Nov; never built, never reported
  as dropped.
- **Chart counts to the real plant** (plan step 4, 23 Nov): the simulator got the real plant (25–26 Nov); the
  chart's counts were never corrected. The correction is listed as waiting in the 25 Nov facts page (unmerged)
  and he was told on 26 Nov that the chart is demo data and wiring is a task; no log says plainly that U132/U137
  left the chart out.
- **Milestone M4 "Model drives Studio"** (target Fri 4 Dec, proposed 1 Nov): status not reported since the
  5 Nov todo review.
- **U14 / U15 questions** (bad-upstream look, scene scope, reference lift drawing; ADR 0009, chart ports, hoist
  numbering): asked 1 Nov, no answer found; only the scope point came back, as "draw all 51 winches or fewer"
  (25 Nov, still open).
- **Chart 0.2 decision**: asked 1–6 Nov, not re-asked after 6 Nov.

## Never started

- Wiring the twin (simulator) into the MAx chart, so the chart shows live or replayed twin values.
- Protocols drawn as boxes at the lower zoom level (RS-485 to the root box, MQTT or iba to the logger).
- The top "all" view and sub views built from the twin's own plant file (two sides, 6 stations, 102 winches,
  204 SWS, 408 halves).
- A twin chart the engine can run, and the `twin.platform_load` wrapper.
- Connection diagrams per level drawn in the flow (the levelled data-flow drawings of 20 Nov, u116, are SVG
  drawings outside the chart).

The plain answer to "not heard back": after 2 Nov the flow view for the twin was paused by the 3 Nov priority
(SWS first) and no unit has touched it since; the twin was built as a simulator beside the chart, not in it.
