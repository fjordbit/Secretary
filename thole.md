# Thole — U32 (3D main-text runs, appendix queue, acceptance row)

Session Thole (Opus), branch `u32-3d-main-runs` from main 130203f, worktree C:/Users/stian/Prosjekter-u32 (max/ inside).
Brief: kai.md "U32" (l.1092) + "U32 / U33 addendum" (l.1190). Started 8 Nov 14:40.

## 1. Record rows this unit rests on (rule 10)

Register `sws/data/sws_data_sources.md` (REG), spec rev128 render (SPEC128):
- REG l.191 rope induction window 1.9–2.3 T, U (B per steel or per rope area not read).
- REG l.192 sensitivity test, two inner wires < 0.5 % LMA, SNR ≥ 2, U "verify wording".
- REG l.127–128 Br (min) N40SH 1.25 / N48SH 1.36 / N52 1.42 T, [R4] S.
- REG l.316 B_rope = B_wire + 0.008–0.016 T at the floor, C; l.317 conservative B_wire sizing, C.
- REG l.330 service range −40 / ≈ +45 °C, D; l.331 +80 °C reference row, D; l.333 sizing rule, D.
- REG l.334–335 2D thickness per head and grade at +45 °C and record lm, C (the 2D comparison).
- REG l.341 Hcj N52 0.88 MA/m, A (every N52 knee figure says so); l.340 N52 status, C/A.
- REG l.347 acceptance fault per rope size, D (to be superseded, not overwritten; convention l.324).
- REG l.350 3D run order (not a design selection), D: authorises the main-text pick.
- REG [R5] EN 12927:2019 by title only; [R10] secondary summary; [R29] one-piece half-rings, S.
- SPEC128 l.438 reference-rope definition and the per-size acceptance with the recorded conflict.
- Inputs carried, with status: Br [R4] S; wire box params.yaml (register box); faults level 1.5 half-space (design.md l.242).

Not record, used as labelled inputs: U25b 3D-sized lm 16.73 / 17.45 / 19.02 (design.md §2, verification.md l.1274–1284,
status C by script); Q1 2D B_wire column 17.29 / 18.09 / 19.83 mm (questions l.32, C by script, not in the register).
The lm values solved here are run points, not chosen thicknesses.

— Thole

## 2. Progress (8 Nov 15:20)

- Worktree made at Prosjekter-u32 (repo root; max/ inside), matching the other worktrees.
- `--grade` pass-through added to `run_3dd.py` (P52) and to `run_p52.py seams`; coarse test (level 4, N52 16.73, 1king):
  case id P52lm16.73N52, converged, 1.58 M unknowns, 7 min.
- [R10] page: one read-only fetch, HTTP 404. No EN 12927 text on this machine (search Prosjekter*, Downloads, due-diligence).
- Register: l.347 marked superseded; new row below it, status D (rule) / U (wire-count reading).
- Queue running detached: `sws/3d/logs/u32_run_all.sh` → `u32_main_queue.txt`, then `u32_appendix_queue.txt`.
- R1 done (9 min, six cases, 0.64 M unknowns, ~90 s each): 3D-sized lm reproduces U25b to ±0.02 mT on B_rope; steel
  mean there 1.906 T (−14 mT); at the 2D B_wire-sized lm the steel mean is 1.912–1.914 T (6–8 mT short).

— Thole

## 3. Progress (8 Nov 16:20)

- Main-text set done 15:51 (57 min wall: R1 9, R2 N52 28, R4 19 min). Appendix: bracket 5 min, R4 gaps 15 min, R7 4 min done.
- qc-falsifier pass 1: register row PASS, numbers PASS (recomputed R1 N52 16.73 and the headline fault from raw JSON);
  three text fixes applied (16.3 mT rounding, +0.6 % spread, register l.350 → l.351 after the new row), footer of
  design.md moved above §7. Correction to §1 above: the 3D run order row is now l.351 (the new row is l.348).

— Thole

## 4. Coordinator adjustment (8 Nov ~16:25) — confirmed

Confirmed: N52 results labelled "virgin recoil law, knee violated in storage and on the 40 mm rope, Hcj 0.88 MA/m
status A" (json, figure, design.md); N48SH main case (R1 at 17.45 done; R2 N48SH running, moved into the main set);
3D knee screen of the shared head on the 40 mm rope and empty, N52 and N48SH, +45 °C, first in a new appendix part 2
(`demag_3d.py` extended with a "P52:<lm>:<grade>,<rope>" case, a small model change; no reduced-Br re-solve).
Queue: `logs/u32_switch.sh` stops the old chain after "R2 N48SH DONE" and starts `logs/u32_appendix2_queue.sh`.

— Thole

Second coordinator item (8 Nov ~16:25): core-fill sensitivity (fill 0.7; then fill 0.7 + 2.2 mm outer wires, new
`run_3dd.py --d-wire`, pitch scaled with the wire) and the single hidden wire solved directly on the L_h 60 half-space,
both N48SH 17.45, +45 °C, appended at the END of `logs/u32_appendix2_queue.sh` (after R8; they will run tonight if the
queue lives; failures are logged, not fatal).

— Thole

## 5. Hand-back (8 Nov 17:40)

Commit fecd310 on `u32-3d-main-runs` (no merge, no push). Done: R1 + bracket, R2 N52 / N48SH / N40SH, R4 + gaps, R7,
R6, K (3D knee). Queue still running detached: `sws/3d/logs/u32_appendix2_queue.sh` → `u32_appendix2_queue.txt`
(R3 ×3, R8, then core-fill and the single wire on L_h 60). How to read and fold in: tasks/reports/U32.md "The queue
after this report". Nothing written after fecd310 is checked.

— Thole
