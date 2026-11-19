# Fathom — U28 SWS 2D rerun on the decided configuration

## 2026-11-07 start
Session name Fathom. Worktree C:/Users/stian/Prosjekter-u28 (u28-sws-2d-decided-rerun, from 643e306).
Reading the record first (rule 10): register, spec rev127 (u25 render, read-only), 23 Oct consolidated findings, sws_head.py.

— Fathom

## First note (rule 10): the record read, and the register rows U28 rests on
Read in full: register sws/data/sws_data_sources.md (316 lines), spec rev127 render (u25, read-only) §5 and abstract,
sws/fem-2d/sws_consolidated_findings_2026-10-23.md, sws_head.py, Sextant.md §A–E, kai.md U28 + "U28 — verifier fixes".

Rows I rest on (register line numbers on main 643e306):
- l.67–68 [R29] + l.153: one-piece sintered half-ring per half, radially magnetised (S).
- l.89 guard non-magnetic 1.5–2 mm (D); l.312 magnet guard vs rope liner (D/A).
- l.94 design rope 52 mm, sizes 40 and 52, range 35–57 (D); l.96 C = 0.571 (S).
- l.110, l.119 wire curve shape and working box Bs 1.95–2.01 T, Ha 1.5–2.5 kA/m (A); hard/easy corners.
- l.127–128 Br min N40SH 1.25, N48SH 1.36, N52 1.42 T (S, [R4]); l.129 alpha(Br) −0.12 %/K (S); l.131 μrec 1.05 (S).
- l.130 alpha(Hcj) −0.5…−0.6 %/K (A); l.181 Hcj by letter SH 1.59 MA/m (A) — N52 Hcj NOT in the register; the
  0.88 MA/m is sws_head.py l.47 only (A, unrecorded; supplier sheet requested via Henrik) per verifier fix c.
- l.182 knee 0.8 Hcj (A); l.183 recoil-line working point (C).
- l.132 NdFeB density 7.5 (A); l.135 yoke steel 1010-like (A); l.136 steel density (S).
- l.148 gap field / Maxwell pressure, l.150 stray field (C, steel-shoe run) — redone in 2D; l.149 side force needs 3D — NOT redone (fix a).
- l.154 + l.303 yoke flux rule (C): 12.0 mm on Ø60 shared, 8.5 mm on dedicated 40 (l.305) (fix e).
- l.191 window 1.9–2.3 T (U); l.193 floor 1.92 T (A); l.304 sizing rule both limits (D, owner rule).
- l.305 dedicated 40: 17.2 × 40, bore 48; l.306 shared 40+52: 19.1 × 40, bore 60 (C) — lm basis (i) (fix d).
- l.307 wide head bore 65 (C); l.313 bore = free passage inside guard (C, corrected 2026-10-29 in spec l.247 (4)).
- l.139 spacing magnetic floor 60–80 mm (C, steel shoe); l.140 magnet mass vs spacing (superseded); l.142–146 rope-size map (superseded).
- l.209 ~40 mT axial background (C, steel-shoe) — redone.
- l.246 pacemaker level 0.5 mT (S, [R15]).
- l.296–297 decided-config head-options table and the steel-shoe audit (C); l.310 grade check (C, Hcj A).
- Superseded by Stian's ruling 7 Nov (fix b), NOT a stop: l.88 (service ≤ 60, sizing −40/+80), l.151, l.304 lm_min at +80.
  New service corners −40 / +45 °C, +80 as one reference row.
- Temperatures 43 shielded / 46 semi / 55, 64 unshielded: sws/due-diligence/sws_sun_exposure_findings.md l.38–40 (not register).

STOP check: no conflict found between the brief (with the verifier fixes) and the record outside the declared ruling.
Notes: sws_head.DECIDED lm 17.8 is stale (not used as the decided head). The rev127 spec render does NOT embed the
sws_fig_abstraction figure; it is on the site page docs/sws/index.html (Prosjekter main, spec part §5 heading).
U25b grades.py (u25, read-only): same Br/Hcj/alphas (imports sws_head GRADES), but fixed t_yoke = 12.0 mm instead of
the flux rule — a difference to state.
Proceeding to build.

— Fathom

## Progress 17:20
- sws_decided_rerun.py written (modes heads / fields / demag / spacing / ropemap -> sws/data/decided_rerun.json); running, 4 workers, 2D only.
- Gap-field probe reproduces the record on the legacy 4 mm-shoe 100 mm head (0.72 T, 208 kPa). The record's stray-field
  numbers (0.5 mT at ~300 mm, 10 mT at 200 mm) do NOT reproduce with any probe I could define on that legacy head
  (545 mm / 376 mm) and the 2D far field is air-box bound; reporting stray field as like-for-like ratios with two box sizes.
- SUPERSEDED headers on the six modules; regression sws_head_test.py 5/5 PASS (T2 1.9866 T).
- Concept figure re-drawn: sws_fig_concept_decided.py -> sws/data/figures/sws_concept_decided.png.
- TASKS.md U28 entry written.

— Fathom

## 17:50 — results in, QC running
All five modes ran (spacing first hit a MemoryError: lm not reachable under 45 mm at 200 mm spacing -> nan -> mesh blow-up; fixed with hi=90 and a nan guard, rerun clean).
Headlines: shared head 1.92 T hard +45: N52 15.84 / N48SH 16.58 / N40SH 18.15 mm (record 19.1 @ +80 reproduces 19.04).
Knee @45 °C, 40 mm rope, shared head: N52 31 % beyond knee (Hcj 0.88 A unrecorded), N48SH 0.00 %, N40SH 0.00 %.
Rerun doc sws/fem-2d/sws_decided_rerun_2026-11-07.md, redline sws/spec/REDLINE_2026-11-07.md. Opus QC subagent checking against the record now.
No STOP needed so far.

— Fathom

## 18:05 — done
QC (opus subagent): 1 blocking (redline called N52's 0.88 MA/m "the register's" — fix c) + 10 non-blocking; all fixed
(spec-line prefixes, 82.5 % at lm 16.59, 4.4 %, pressure range, background 31–60 mT, 46 °C dropped from the ruling rows,
3D side-force value left to the 3D owner, knee figure now shows volume beyond knee with the N52 "unrecorded" tag).
Committed e86af7c on u28-sws-2d-decided-rerun (not merged). No STOP.

— Fathom

## Kai verifier wording fixes (6 + U25b sentence) applied, commit a0491ff. No new solves.

— Fathom

## Codex fixes 1-8 applied, commit 9704fcf (2D checks: sws_decided_rerun_checks.py). Item 4: gap is the yoke (fixed 12.0 vs flux rule 12.61), not bisection - my earlier and Kai-verifier reading were wrong.

— Fathom
