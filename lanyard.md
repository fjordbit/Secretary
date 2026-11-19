# Lanyard — U34 builder (close the outside review's 2D and record findings)

## 2026-11-08 16:40 — start; record rows I rest on

Worktree C:/Users/stian/Prosjekter-u34 (repo root; max/ inside, as the other worktrees), branch
u34-review-closeout from main 922d8b3. Brief: kai.md l.1230 + addendum l.1308 (addendum wins).

Record (rule 10) = spec rev128 render + register `sws/data/sws_data_sources.md`. Rows I rest on:
- REG l.127–129 Br min per grade, alpha(Br) −0.12 %/K (S, [R4]); l.130 alpha(Hcj) −0.5…−0.6 %/K (A);
  l.131 recoil permeability 1.05 (S); l.181 Hcj by grade letter SH 1.59 MA/m (A); l.182 knee ~0.8 Hcj (A).
- REG l.191 window U (B_rope or B_wire open); l.193 floor 1.92 T (A); l.316 B_rope / B_wire definition (C).
- REG l.100 / l.215 wire diameters not held / 2.5 mm A; l.96 C = 0.571 (S).
- REG l.247 sun-model body 30 kg (A); l.315 three-tools statement (D, files pending); l.318 3D tolerance (A).
- REG l.329–335 envelope / service range −40…≈45 °C (D, shielded mapping A) / +80 reference / method / sizing rule /
  thickness per head and grade / record lm; l.340–341 N52 status and Hcj 0.88 MA/m (A); l.346 head mass; l.347
  acceptance fault per size (D, conflict open); l.348–350 report scope, paper scope, run order.
- SPEC128 render l.11, l.155, l.175, l.233, l.237–255, l.369–376.
Not in the record, used as A and labelled: the post-knee intrinsic-curve shape and the recoil-from-point-reached rule
(part A), Hcj20 1.05 MA/m as an intermediate sweep point.

— Lanyard

## 2026-11-08 — A–F built, verifier running

A: two-pass knee history in sws_head.py + sws_knee_history.py (json, figure, rerun md section). N52 at 0.88: empty +45 °C
leaves 1.11 / 1.36 T; 40 mm +45 costs 14–18 mT; < 1 mT needs Hcj20 ≳ 0.95 (40 mm) / ≳ 1.16 (empty +45). N48SH 0.0.
B: Q5 rebuilt, 27 rows. C/D/E/F applied per brief + addendum; rev129 render differs from rev128 in rows 28–31 + log row.
Register untouched (row proposed under Needs Stian). Checks green. qc-falsifier verifying before commit.

— Lanyard

## 2026-11-08 — committed cdd3595 on u34-review-closeout (no merge, no push)

qc-falsifier PASS WITH FIXES, six fixes applied. Scratch venv deleted. Report tasks/reports/U34.md.

— Lanyard

## 2026-11-08 — A re-solved after verifier-U34 FAIL; committed on the branch

First A overshot (locked-in cut from virgin H). Quasi-static fixed point now; N52 0.88 empty +45 °C −29 / −28 mT
(lm 15.84 / 16.73), 40 mm +45 −2.6 / −1.7; < 1 mT needs Hcj20 ≳ 0.91 (40 mm) / ≳ 1.14 (empty +45). qc-falsifier
(load-stepping) agrees to 0.01 mT.

— Lanyard
