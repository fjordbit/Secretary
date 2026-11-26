# SWS: history of work done (22 Oct – 26 Nov 2026)

Sources: secretary log/*.md, START.md, todo.md, inbox/2026-11-23_dt_plan.md, max/sws/README.md (U7 status only).
Dates are log dates. "Merged" = on local main (D: and backup); GitHub/Pages only where a push is named.
First SWS mention in the secretary logs: **22 Oct 2026** (earlier SWS work was done on another computer; see section 4).
All figures are calculated unless marked measured.

## 1. Completed work

### Specification and requirements

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 22 Oct | INPUT spec copied into max/sws/spec; sensor positions settled | 16 positions (spec rev115 §6) | log 22 Oct |
| 23 Oct | Spec rev123/124 replaced rev115 (delta b) | rev115 moved to old/ | Prosjekter 26b156b; log 23 Oct |
| 30 Oct | Spec rev127 redacted and rendered on the report page | 23/23 tables, 7/7 + 10 figures, 16/16 plots | republish 600c1aa; log 29 Oct |
| 7 Nov | Audit of all 3D work against spec rev127 + register (Fable, read-only) | Reference defect redefined (0.62 % vs < 0.5 %); P40 inheritances; +80 °C used throughout | agent-notes/Sextant.md; log 7 Nov |
| 7 Nov | Redline of the spec from the 2D rerun (U28) | 24 rows for the owner | sws/spec/REDLINE_2026-11-07.md; log 7 Nov |
| 8 Nov | Register rows applied, spec rev128 built (U31) | 15 rows applied, 17 superseded; DECIDED lm 19.1 mm | main 130203f; log 8 Nov |
| 8 Nov | Spec rev129 banners (U34) | banners only, register unchanged | main 8d28f5f; log 8 Nov |
| 8 Nov | Spec rev130 temperature envelope (U36) | operating −40/+50 °C; ±80 °C marked historical; redline rows 32–40 | main 4e13ccf; log 8 Nov |
| 10 Nov | Register "Rulings of 2026-11-10" (U56) | B_rope reading; working area as the deliverable; LD/LMA names | main db05b45; log 10 Nov |
| 11 Nov | Rulings into register and housing page (U66) | never submerged; IP66/IP67 | main 4241003; log 11 Nov |
| 18 Nov | LD/LMA wording corrected everywhere (U93) | 21 places, discard rules, redline rows 7–12 | main 062b8bd; log 18 Nov |
| 20 Nov | Live parts table (U114) | 28 parts, 153 rows: 15 ruled, 19 open | max/sws/parts_table/; main 5a8dcc6; log 20 Nov |
| 20 Nov | Two converters per half in all live documents (U119) | spec rev131 rendered; price/link figures recomputed | main b5478a7; log 20 Nov |
| 25 Nov | DT fixed facts and disagreement list (U127) | 47 facts; 34 disagreements (25 out of date, 9 open) | branch u127-dt-facts 591e1ab (not merged); log 25 Nov |

### Magnetic circuit and FEM (2D, 3D)

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 22–23 Oct | 3D defined as real magnetostatic FEM; solvers chosen | NGSolve main, GetDP cross-check (ADR 0003) | log 22–23 Oct |
| 23 Oct | Corrected 2D code (ferromagnetic-ring bug) applied | regression gate 5/5 | Prosjekter 26b156b; log 23 Oct |
| 25–26 Oct | U7 Stage 1: in-house 2D vs FEMM vs GetDP | B_rope agrees ≤ 3.3e-4 T in 18 cases; accepted 26 Oct | 7f26813; sws/README.md; log 26 Oct |
| 26–29 Oct | U8 3D: 3D-A and closures | bond line, demagnetisation, off-centre rope, force between halves | branch u08-sws-3d 86ea9ea; log 29 Oct |
| 3 Nov | U17 Bz radius and P40 notch (Fable) | groove 10×2 mm: B_rope −0.2 %; Bz(36.5 mm) = −11 mT | u17 602c6b3; log 3 Nov |
| 3 Nov | U16 3D-C stranded rope + 3D-D broken wires | 2 hidden outer wires B_r 4.40 / 2.66 mT at 3 / 5 mm; margins 20 / 12 | u16 50475e3; log 3 Nov |
| 4 Nov | U19 stranded section under the poles | B_rope ≈ 1.915 T at hard +80 °C (floor 1.92 not held) | u19 bdb1581; log 4 Nov |
| 4 Nov | U19 solver stall fixed + stage 4 | eps_reg 1e-4; easy −40 °C ≈ 2.023 T | u19 023da1f; log 4 Nov |
| 7 Nov | U25 P52 prototype head (withdrawn same day: segmented magnets) | 20.5 mm magnet → 1.927 T | u25 55844ed; log 7 Nov |
| 7 Nov | U25b P52 redone with one-piece magnets | lm for 1.92 T: N52 16.72 / N48SH 17.45 / N40SH 19.02 mm; halves −664…−670 N | u25 44ce9cd; log 7 Nov |
| 7 Nov | U28 2D rerun on the decided configuration at +45 °C | lm N52 15.84 / N48SH 16.58 / N40SH 18.15 mm; 0.5 mT at ~490–520 mm | u28 9704fcf; log 7 Nov |
| 7 Nov | U29 merge, nine figures, STEP files | STEP at 16.73 / 17.45 / 19.02 / 19.1 / 20.5 mm; P40 vs ours figure | main ff20112; log 7 Nov |
| 8 Nov | U32 3D main set + appendix | B_rope 1.9222 T at 3D lm; steel mean 1.906 T; fault margins 20.1–20.3 / 12.2–12.3 | main 38974e6; log 8 Nov |
| 8–9 Nov | U35 appendix fold-in (7 runs) | −40 °C easy reads 13–30 % above +45 °C hard | main 34ef91a; log 8 Nov |
| 18 Nov | U92 long loss (300 mm) | per 1 % lost: rope flux −0.93 %, axial TMR +0.4–0.5 % | main 062b8bd; log 18 Nov |
| 18 Nov | U95 axial lift-off, 40 mm head | standing Bz −41.9 mT at 3 mm; inside ±20 mT from 13 mm | main 1bd304c; log 18 Nov |
| 18 Nov | U96 yoke cut-out sweep, 45 cases, 2D | outer groove w18 d5: Bz inside ±20 mT at 3 mm | main 1bd304c; log 18 Nov |
| 18 Nov | U97 groove physics | zero at 10/13/16 mm needs 4.5/3.7/3.1 mm groove (H40, small box) | main 1bd304c; log 18 Nov |
| 18 Nov | U98 working point | LMA drift null near 1.90 T; short-fault signal +60 % from 1.90 to 2.10 T | main 1bd304c; log 18 Nov |
| 19 Nov | U100 52 mm head fine sweep (small box, later corrected) | groove 6.1/5.4/4.6 mm for zero at 13/16/19 mm | main 1bd304c; log 19 Nov |
| 19 Nov | U101 A–F team falsification run (six builders) | box size broke groove depths; inner-wire margin ~1 at 2.0 T | sws/3d/falsify/; main 1bd304c; log 19 Nov |
| 19 Nov | U102 re-run in a large model box | H52 groove 4.98/4.25/3.53 mm; steel within 0.5 m shifts reading 1–8 % of metal | main 1bd304c; log 19 Nov |
| 19 Nov | U103 40 mm prototype head as drawn | standing-field zero at 16.67 mm lift-off (15.9–17.8) | main 1bd304c; log 19 Nov |
| 19 Nov | U106 groove plots redrawn, large box | 72 solves; level at 16 mm −0.675 / −0.768 / −0.806 mT per 1 % | main 5a8dcc6; log 19 Nov |
| 19 Nov | U107 groove trade-off map | 540 solves; zero at 16 mm holds up to ~2.04 T; groove costs 9 % radial | main 5a8dcc6; log 19 Nov |
| 20 Nov | U115 40 mm head on 38–40 mm rope | 378 solves; rope 1.865–2.067 T; groove N52 2.54 mm | main 5a8dcc6; log 20 Nov |

### Magnet grade and temperature

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 7 Nov | Knee screening per grade (U25b) | N52 knee at +62 °C on 52 mm, +28 °C on 40 mm, −27 °C empty head | sws/3d/p52/fig_envelope.png; log 7 Nov |
| 7 Nov | Empty-head knee in 2D (U28) | N52 82–100 % past knee at 45–80 °C; needs Hcj20 ≈ 1.19 MA/m | u28 9704fcf; log 7 Nov |
| 8 Nov | Knee-history re-solve (U34, second method after verifier fail) | N52 empty +45 °C −29/−28 mT; loss < 1 mT at Hcj ≥ 1.14/1.12 | main 8d28f5f; log 8 Nov |
| 8 Nov | Sun model on the decided head (U34) | shielded 43.1–43.4 / 48.6–48.9 °C | main 8d28f5f; log 8 Nov |
| 8 Nov | 2D excursion table (U36) | N52 (Hcj 0.88) empty loses 29–60 mT at +45…+80 °C; N48SH 0 | main 4e13ccf; log 8 Nov |
| 19 Nov | Demagnetisation and forces with real thicker magnet (U101 F) | N52 empty head 57–88 % past knee; N48SH fine | sws/3d/falsify/f_magnet_mech.md; log 19 Nov |
| 25 Nov | Temperature in the DT (U133) | magnets above 45 °C only worst summer uncovered (5.6 h) | main 67866d8; log 25 Nov |

### Sensing elements and converters (PCB architecture)

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 10 Nov | Link and read-out note (U60) | ADS131M08 sheet checked: external reference yes; 24 ch at 500/s needs 1 Mbit/s | sws/hw-selection/sws_link_and_readout.md; log 10 Nov |
| 10 Nov | Multiplexed case checked on data sheets (U61) | ≤ 362–407 samples/s per bridge on three chips | main 4a50a29; log 10 Nov |
| 11 Nov | Price against complexity (U64, U67) | converters per half A 15, B 21, C 22, D 22–40 USD | sws/figures/decided/price_glance.png; log 11 Nov |
| 12 Nov | Sensor candidates against data sheets (U71) | no part passes cleanly; linear range 94–141 mT needed | main d98e70d; log 12 Nov |
| 12 Nov | Prototype parts read (TMR2185, TMR2584) | specified ±20 mT; saturate ±100 / ±30 mT | inbox data sheets; log 12 Nov |
| 12 Nov | Literature sweep (U72) | 14 makers, 17 papers; no GMR/TMR/AMR in any product | main d9b602d; log 12 Nov |
| 12 Nov | Sensor round folded in, parts checked (U73) | DRV5055A4 (±176 mT) and TMAG5253 reach 150 mT | main d9b602d; log 12 Nov |
| 12 Nov | Sensor placement page (U74) | six placements A–F, three combinations, nothing selected | docs/sws/sensor.html; log 12 Nov |
| 16 Nov | "What the sensor measures" chapter (U76) | record 0.39 mT vs own 3D 1.27 / 2.69 mT break signal | main f806c68; log 16 Nov |
| 16–17 Nov | Second sensor round data-sheet check (U83) | DRV5055A2 ±44 mT at 3.3 V; rig sheet gap/identity steps | merged 17 Nov; log 16 Nov |
| 18 Nov | Board arrangement marked "not settled" (U91) | spokes not confirmed; thin board across the rope | START 18 Nov 16:15; log 18 Nov |
| 19 Nov | Element run 3 on one thin board (U111) | axial at 16 mm 0.77 mT per 1 %; groove cuts −40 °C error 11 % → 0.4 % | main 5a8dcc6; log 19 Nov |
| 19 Nov | Semi-blind element round compared (U113) | in-plane radial + through-package axial on one board (3 of 3) | main 5a8dcc6; log 19 Nov |
| 20 Nov | Element round rerun with newest models, five answers (U122, U123) | axial 3 Hall : 2 TMR; radial at 5 mm 5 of 5 | branch u122-rerun-rounds eb0e658 (not merged); log 20 Nov |

### Potting / encapsulation

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 11 Nov | Housing and sealing page, four cases (U65) | example epoxy Tg 49 °C inside service range | docs/sws/housing.html; log 11 Nov |
| 11 Nov | Sealant round checked on data sheets (U68) | Stycast 2850FT Tg 40 °C (RT cure), 55 °C after 4 h at 65 °C | main 8f97214; log 11 Nov |
| 19 Nov | Scotchcast resins note (U105) | 2123 soft re-enterable gel, 24 h at 21 °C; no −40 °C figure | sws/hw-selection/sws_potting_scotchcast.md; main 1735f4b; log 19 Nov |

### Data line, half firmware (C), root box, logger

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 10 Nov | Software page with half/root-box pseudocode (U61) | pseudocode walked twice, 9 blocking fixed | docs/sws/software.html; log 10 Nov |
| 19 Nov | Data path, three blind answers + traffic (U108) | 250/s per channel; 102 heads 25.2 Mbit/s serial | sws/data-path/; main 5a8dcc6; log 19 Nov |
| 19 Nov | Transmitter line study (U109) | frame 1 229 B per 100 ms = 123.5 kbit/s per half (27 % of 460.8k) | sws/transmitter/; main 5a8dcc6; log 19 Nov |
| 19 Nov | Half core in C11 (U112) + clamp at full scale | frames byte-identical to Python; 35 ns per result set | sws/line_beta/c_half/; main 5a8dcc6; log 19 Nov |
| 20 Nov | Principle drawings + levelled data flow (U116, GPT Sol) | 6 + 11 drawings; buffer cap holds 22.6 h, not 24 h | branch u116-line-drawings e0dd47a (not merged); log 20 Nov |
| 25 Nov | Firmware update and root-box connection note (U126) | two-slot fall-back; 32 kB image 13.6 s; ring 0 SWS lost per fault | branch u126 6c85176 (not merged); log 25 Nov |
| 25 Nov | Root box reduction (U134) | movement found in 1.1 s, 0 misses in 36 starts; 218 → 30.5–42.5 GB/day | main 67866d8; log 25 Nov |
| 25 Nov | Reduction brief for Henrik, detector on real recording (U135) | 20 of 20 passes, 0 false starts in 106 min | inbox/2026-11-25_reduction_brief/; main 67866d8; log 25 Nov |

### Digital twin and simulator

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 29 Oct–1 Nov | Twin design unit (U10) and SWS shiplift chart in Studio (U13/U14) | design only, no twin code; zoom shiplift → half → channels | u10 / main 91897db; log 29 Oct, 1 Nov |
| 19 Nov | Data line as a running beta (U110, Python) | 67× real time; 6 of 7 proofs pass; position 27.3 mm vs 10 mm fails | sws/line_beta/; main 5a8dcc6; log 19 Nov |
| 20 Nov | Twin replay page (U120) | 12 scenarios, 6.7 MB, 0 console errors | branch u120-twin-page 4c7f039 (not merged); log 20 Nov |
| 23 Nov | DT documentation sweep and 8-step plan | simulator is one head; signal by formula | inbox/2026-11-23_dt_plan.md; log 23 Nov |
| 25 Nov | Full-scale plant (U132) | 51 ropes / 102 SWS / 204 halves; one pass 59 min, 12.4 GB | main 67866d8; log 25 Nov |
| 25–26 Nov | Simulator branches joined (U136: U132+U133+U134+U135) | 125 tests pass + 1 known failure | main 67866d8; log 25 Nov |

### HMI / presentation design

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 18–19 Nov | Interactive plot layout (U99) then plot standard (U104) | research + presentation types; 38 tests | fjordbit/agentic 573e59b; log 18–19 Nov |
| 20 Nov | HMI round 1: four models, four HTML designs (U118) | 12 decisions listed; Grok slot rerun on 4.7 | branch u118-hmi-round c1629d4 (not merged); log 20 Nov |
| 20 Nov | HMI round 2: Opus on OpenBridge (U118) | palette only; findings latch; 9 decisions | max/sws/hmi/round_2/; log 20 Nov |

### Prototype rig measurement and its analysis

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 12 Nov | Procedures page + data list for the 40 mm test (U70) | 12 stages as placeholders; 16-row data list | docs/sws/procedures.html; log 12 Nov |
| 16 Nov | Rig sheet + AI helper guide (U77) | 4 A4; rope fixed, head moves | docs/sws/rig_sheet.html; main 5f415b6; log 16 Nov |
| 16 Nov | 52 mm test-rope fault list (U84) | 21 faults (32 breaks), ~22.1 m | branch u84-test-rope 4c8511c (not merged); log 16 Nov |
| 17 Nov | Rig sheet read from the runs; test-sheet round in repo (U85, U87) | live/dead/not-fitted column; rig sheet 5 A4 | main 84af27a, 1cc9661; log 16 Nov (17 Nov entries) |
| 18–20 Nov | Prototype test at the rig (Stian on site) | owner facts: thin board in two halves; TMR2185 radial, TMR2584 axial | log 18 Nov |
| 19 Nov | Prototype yoke drawing received and read | yoke 105 mm, Ø102, groove 10 × 2 mm | inbox/2026-11-19_prototype_yoke_drawing.png; log 19 Nov |
| 25 Nov | Opus analysis of the recording (U124, measured) | 30 files at 100/s; ripple 0.644 s; strong field shifts zero up to 11 mT | branch u124 8c9b948 (not merged); log 25 Nov |
| 25 Nov | Codex analysis by script loop (U131) | 8 of 15 figures agree; parser bug found | branch u128 181b99c (not merged); log 25 Nov |
| 25 Nov | Fable 5.2 analysis on API key (U130) | 15 of 20 agree; cost 82.19 USD; three analyses agree | branch u130 9ed9bf5 (not merged); log 25 Nov |

### Reviews by outside models (model rounds)

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 7 Nov | Codex reviews of U25b/U28 + MAx run on the record | both FIX; Codex right on the 15.84 vs 15.93 mm gap | log 7 Nov |
| 8 Nov | Peer read of the whole SWS (U30, Fable) | 75 input fields, 11 knowledge bases | docs/paper/peer_read_2026-11-08.md; log 8 Nov |
| 8 Nov | Grok external review of the masked pack | 10 findings: 9 confirmed, 1 partly | docs/paper/reviews/2026-11-08/grok-external.md; log 8 Nov |
| 8–9 Nov | Nine-model review round + synthesis | 20 findings, 7 contradictions, scorecard | docs/paper/reviews/2026-11-08/SYNTHESIS.md; log 8 Nov |
| 10 Nov | Electronics round 1 (blind, five models) | 5 of 5: two simultaneous 8-ch 24-bit converters per half | sws/hw-selection/rounds/2026-11-10/; log 10 Nov |
| 10 Nov | Electronics round 2 (challenge, cases A–D) | case A first 3 of 5; multiplexed case D last for four | same folder; log 10 Nov |
| 11 Nov | Sealant round (five models) | 4 of 5: gasket-sealed shell + soft silicone gel | C:/Users/stian/sealant_round_2026-11-11/; log 11 Nov |
| 12 Nov | Sensor round 1 (three models) | 3 of 3 chose silicon Hall | sws/hw-selection/rounds/2026-11-12-sensor/; log 12 Nov |
| 16 Nov | Sensor round 2 (two steps) | all end on placement B with DRV5055A4 axial | C:/Users/stian/sensor_round_2026-11-16/; log 16 Nov |
| 17 Nov | Test-sheet round (two steps) | only a hand probe gives the standing field in mT | sws/procedures/rounds/2026-11-17-test-sheet/; log 16 Nov |
| 17 Nov | Release-mechanism and halves-force rounds | solid bar net ~500 N closed; real rope may be near zero | sws/housing/rounds/; log 17 Nov |
| 18 Nov | Groove physics round (Grok, Codex; Sol checks) | working point not derivable without real B–H curves | C:/Users/stian/groove_round_2026-11-18/; log 18 Nov |
| 18 Nov | Board-arrangement round (three models, two steps) | six answers | C:/Users/stian/board_round_2026-11-18/; log 18 Nov |
| 19 Nov | Data-line round (Opus, Grok 4.5, Codex 5.3) | 250/s, raw 24-bit frame per 100 ms, one line per half | sws/transmitter/; log 19 Nov |
| 19 Nov | Semi-blind element round (Opus, Grok, Codex) | see U113 | sws/hw-selection/element_round_1/; log 19 Nov |
| 20 Nov | Reruns with newest Grok (4.7); Fable 5.2 + Sol added | axial Hall/TMR split flipped, then 3 : 2 Hall | branch u122 eb0e658; log 20 Nov |

### Pages / documentation

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 26 Oct | SWS spec site delivery checked | stale docs/ rejected; rebuilt by U7 | log 26 Oct |
| 29–30 Oct | SWS published to private repos + Pages | 220 files; 59 links repointed | fjordbit/SWS, MAx-Flow/SWS-Documentation c1920f4; log 29 Oct |
| 4 Nov | Names removed from GitHub history | placeholders; 70 commits rewritten | fjordbit/max 7a70832; log 4 Nov |
| 9 Nov | Identifier sweep, export v3, short page (U37–U40) | short page 4 A4 | Pages f545164; log 9 Nov |
| 9 Nov | Format switch, short landing, easy read (U41, U42, U46) | easy read 3 A4; three formats | Pages d8c54c9; log 9 Nov |
| 9 Nov | Standard-on-file wording (U48, U49) | register notes; analogy | Pages 2093ebc; log 9 Nov |
| 10 Nov | Pages about the task, not the owner (U50–U55) | "owner" 24 → 1–2; easy read in four parts | Pages ed8274c; log 10 Nov |
| 10 Nov | Working-area plot + LD/LMA (U56, U57) | lower edge of working area stated | Pages 40f186a; log 10 Nov |
| 10–11 Nov | Hardware and software pages (U58–U63) | 0 broken links on five pages | Pages 832e98f; log 11 Nov |
| 11 Nov | Housing page, price plot, sealant (U64–U69) | six pages live | Pages 2dc95f3; log 11 Nov |
| 12 Nov | Procedures and sensor pages (U70–U75) | eight pages live | Pages f51035e; log 12 Nov |
| 16–18 Nov | Releases U79, U86, U88, U90, U94 | nine pages; two-part demo video v2 (42.8 s) | Pages 1a58533 → 67c6e1f; logs 16–18 Nov |
| 20 Nov | Results page + parts page, release (U117, U121) | results 8 A4; eleven pages, 0 broken links | GitHub dd24591, Pages f74c6a4; log 20 Nov |

### Standards (EN 12927, ISO 4309) reading

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 9 Nov | EN 12927:2019 ch. 14 extract | Annex B (1.9–2.3 T) informative; test piece 0.5 % of metallic area | max-private/standards/EN12927-2019_ch14_extract.md; log 9 Nov |
| 9 Nov | EN 12927 clause map | 57 of 68 pages read | max-private/standards/EN12927-2019_clause_map.md; log 9 Nov |
| 12 Nov | EN 12927 check cycles from literature sweep (U72) | function check 3 years; performance test ≤ 12 months | sws_sensor_literature.md; log 12 Nov |
| 18 Nov | ISO 4309:2017 and crane rope standards extract | discard LMA 10 % over 30d; LD 6 % over 6d | inbox/2026-11-18_crane_rope_standards_extract.md; todo |

### Tasks issued to colleagues (GitHub issues)

| Dates | What was done | Result (key figures) | Where it lives |
|---|---|---|---|
| 3 Nov | Reply to the head designer's questions (drafted, Stian sent) | notch 10×2, R 36.5, N42 asked to confirm | inbox/drafts/2026-11-03_henrik_reply.md; log 3 Nov |
| 3 Nov | Issue #1 to Ramin: rope construction data | 7 items; open | fjordbit/max#1; log 3 Nov |
| 3 Nov | Issue #2: prototype noise floor | assigned to the head designer 19 Nov; open | fjordbit/max#2; log 3, 19 Nov |
| 8 Nov | Magnet-spec mail to the head designer (Stian sent) | sent 8 Nov | inbox/drafts/sent/; log 9 Nov |
| 19 Nov | Issue #3: prototype groove dimensions | drawing received same day | fjordbit/max#3; log 19 Nov |
| 19 Nov | Issue #4: magnet supplier data N52/N48SH | open | fjordbit/max#4; log 19 Nov |
| 19 Nov | Comment on #1; rope-maker enquiry drafted to Stian | 52 mm reference rope, L4 added (10 % over 1 560 mm) | inbox/drafts/2026-11-19_rope_maker_*; log 19 Nov |
| 25 Nov | Issue #5: platform steel geometry for a 3D run | posted, assigned | fjordbit/max#5; log 25 Nov |

## 2. Rulings by the owner

- 22 Oct — 3D is a real magnetostatic FEM; 16 sensor positions.
- 23 Oct — 3D models all three result-10 heads, dedicated 40 first.
- 26 Oct — Stage 1 accepted; "Independent FEM comparison" register row kept.
- 30 Oct — Twin is design only for now; climate sites kept as allowed-private cases.
- 2 Nov — SWS has no fibre: RS-485 duplex over CAT cable.
- 3 Nov — Br (radial) = local faults, Bz (axial) = loss of metallic area.
- 3 Nov — Keep 0.11 mT p-p noise budget until a floor is measured.
- 3 Nov — SWS before MAx flow; stranded section under the poles before the prototype head.
- 4 Nov — U19 solver setting eps_reg 1e-4 becomes the record; stage 4 finished.
- 7 Nov — Magnet half-rings are one sintered piece; no steel shoe.
- 7 Nov — Max 45 °C in service; N52 given at no cost; run N52 and N48SH; agents do not select.
- 7 Nov — Rule 10: read the record, build to it, prove it.
- 8 Nov — Acceptance follows EN 12927 as minimum (40 mm one wire, 52 mm two wires as translated).
- 8 Nov — Report shows 40 mm, 52 mm and shared head with all grades; management chooses.
- 8 Nov — Masking policy: company and suppliers may be named outside; personal and customer names never.
- 9 Nov — Envelope −40 / +50 °C for service, storage and transport; no more FE runs until supplier data.
- 9 Nov — Landing page = dense short page; easy read a separate third page.
- 10 Nov — Pages describe the task, not the owner.
- 10 Nov — B_rope is the reading, B_wire shown beside it.
- 10 Nov — Deliverable is a working area of magnet and yoke sizes; nomenclature LD / LMA per EN 12927.
- 10 Nov — No multiplexers if avoidable; 2 × 8-channel 24-bit per half; digital temperature fine.
- 11 Nov — Multiplexed case named "the in-house choice"; head never submerged; IP66 and IP67.
- 12 Nov — Easy read is the basic format; sensor placement on the board may change; sensor gets its own page.
- 18 Nov — Spokes never confirmed; one thin board across the rope; LD and LMA are two measurements.
- 18 Nov — Company discard rule 10 % LMA; answers as low / middle / high ranges.
- 18 Nov — Sensor search: one PCB and TMR first; Hall only if no TMR fits.
- 19 Nov — Grade N52 or N48SH by price; both always shown.
- 19 Nov — End plates non-magnetic stainless, specified by the project.
- 19 Nov — Two converters per half (spec's three out of date).
- 19 Nov — Beta in Python first, half in C later; half clamps at full scale.
- 19 Nov — 52 mm rope speed 3.2 m/min normal; simulator max 5 m/min; 100 m cable case must hold.
- 19 Nov — D: is not a backup; backup branches on fjordbit/SWS.
- 20 Nov — Names: SWS, head, half, sensing element, channel, root box.
- 20 Nov — Rope position from end proximity sensors (250 m on 52 mm); never an open question.
- 20 Nov — Board thickness and all dimensions are the project's to set.
- 20 Nov — Ten 40 mm heads first, six at a yard by end of March; change only what 52 mm needs.
- 20 Nov — Need more channels: reduce sensing elements, do not add a converter.
- 20 Nov — Bending cycles come from the PLC to the same server.
- 20 Nov — Concern shown orange; findings latch; worst value may drop on dismissal; no time-window statistics.
- 23 Nov — State is "Concern"; DT HMI design, not "mock-up"; DT scope SWS only; trainer HMI separate.
- 25 Nov — Root box does simple reduction (dead band, lossless compression, send around movement), all settable.
- 25 Nov — Two temperature sensors per half; encoder available on the 52 mm installation.

## 3. Open / not done / late

- 20 Nov (due), 23 Nov, 25 Nov — Board (PCB) package for the outside expert: not started; new date not set.
- 6 Nov — P52 yoke + magnet prototype due ≈ 21 Nov: no log says delivered; P52 calls still open in todo.
- 8 Nov, 20 Nov — Spec Word master rev128–rev131 not updated by hand.
- 10 Nov — Spec §7 "internal reference only" wrong per data sheet; 12 Nov §7 "AMR wider range" wrong.
- 17 Nov — Spec rev130 l.218 / l.506 "snap together" / "attract"; side force 0.12 kN/mm row not fixed.
- 9 Nov — Register l.361 / rev130 storage lines still "owner to set" after the −40/+50 ruling.
- 9 Nov — Register l.331/332, l.348, l.192 wording; EN 12927 ch. 14 rows not in register.
- 3 Nov, 19 Nov — Rope construction data from Ramin (#1) open; needed before the last complete run.
- 19 Nov — Magnet supplier data / N52 Hcj (#4) open; gates further FE runs.
- 3 Nov, 19 Nov — Prototype noise floor (#2) open.
- 19 Nov — Issue #3 partly answered: steel grade, other cut-out, sensor radii still missing.
- 25 Nov — Platform steel 3D run waits on geometry (#5).
- 8 Nov — R5 (Ø48 head 3D model) not decided.
- 16 Nov — FMECA, FAT, HAT/SAT, installation, recalibration: not started.
- 16 Nov — Break signal 0.39 mT (record) vs 1.27 / 2.69 mT (own 3D) unreconciled.
- 16 Nov — Temperature range rethink (−40…+80 °C) to be discussed; no change made.
- 19 Nov, 20 Nov — Position-from-ripple proof fails (27.3 mm vs 10 mm); pass figure not set.
- 20 Nov — Hall or TMR for the axial sensing element: open, hinges on strong-field prototype test.
- 20 Nov — Data-path note figures lack their arithmetic (fix when branch is touched).
- 23 Nov — Owed: results page "all three" → five; 8 README links in fig_b1–b4; two parts-table rows.
- 25 Nov — Unmerged: u116, u118, u120, u122, u124, u126, u127, u128, u130, u84; second push round waits.
- 25 Nov — Next DT steps not started: root box in C++, main HMI v3 + trainer HMI, fit twin to measured data.
- 25 Nov — Open on data: axial step after strong magnet (3.2 vs 6 mV/V), 134 vs 136 ripple cycles.
- 25 Nov — 9 DT disagreements and 8 firmware/connection questions for the owner.
- 19 Nov — Clamp status bit not added (health word bits clash).
- 5 Nov (todo) — Scientific paper through the MAx flow: not run.

## 4. Could not establish

- Start of SWS: work before 22 Oct was on another computer; logs only cite spec first issue 7 Oct and supplier mail 9 Oct.
- No secretary logs for 13–15, 21–22 and 24 Nov; any SWS work on those days is not recorded here.
- U8 3D-A / 3D-B key figures are not stated in the logs.
- Times on 18–19 Nov log headings were estimates (corrected in the log); dates are reliable, hours are not.
- Temperature basis shifted: +80 °C → 45 °C (7 Nov) → −40/+50 (9 Nov) → owner leaning back to −40/+80 (16 Nov, not decided).
- Magnet grade: "N52 is out" (8 Nov) read as numbers out, not grade; 19 Nov ruling = by price, both shown.
- Groove depths: small-box figures (18–19 Nov) superseded by large box (19 Nov); some notes still carry old numbers.
- Liner: Kai said Nitronic 60 (20 Nov), builder showed that is the magnet guard; liner on record is polymer.
- Whether the rope-maker enquiry and the 12 Nov prototype-sensor draft to the head designer were sent.
- SWS count: ~250 (1 Nov estimate) vs 102 (19 Nov) vs 108 across two installations (25 Nov disagreement).
- Whether U84 (test-rope list) and U99 (plot layout) count as done: both left unmerged (U99 superseded).
