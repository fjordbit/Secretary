# Painter — U35 builder (fold in the U32 appendix queue results), 8 Nov 2026

Brief: kai.md "## U35" (l.1338–1383). Worktree C:/Users/stian/Prosjekter-u32/max, branch u35-appendix-foldin from main (d5db50c).

## Note 1 — record rows I rest on (register sws/data/sws_data_sources.md, read-only)
- l.96 Metallic area factor C 0.571 (S) — the B_rope denominator C·d² = 1544 mm².
- l.192 Sensitivity test (U); l.347–348 Acceptance fault per rope size (D rule / U wire-count reading; open 0.62 % > 0.5 % conflict).
- l.221 / l.292 noise rows; the result json use 0.11 mT p-p (spec rev127 §7 l.314), margin = S / (2 N_pp).
- l.316 Rope-induction definition in the model (B_rope = flux / A_metallic).
- l.330 Service temperature range −40 / ≈45 °C (D): R3 is the −40 °C easy service corner.
- l.333 Sizing rule (D), EN 12927 §14 B_rope vs B_wire open (l.191 U).
- l.340–342 knee margin (C), N52 status (C/A), Hcj N52 (A): N52 label on every N52 number.
- l.350 3D run order (not a design selection) (D); l.349 Report scope (D).
- sws/3d/rope_construction.yaml: inner_rope.fill "closes_C" status U; d_wire 2.5 A.
No grade, thickness or head is selected. lm values 16.73 / 17.45 / 19.02 are run points (U25b, design.md §2).
Register rows l.329–333 are being remade by U36 tonight; I cite only l.330 (service range) and touch nothing.

## Note 2 — 8 Nov, build done, before the verifier
- Branch u35-appendix-foldin from main d5db50c; seven json added.
- u32_summary.py: case gets variant / corner / construction fields (old keys unchanged, checked against HEAD json).
- Found: make_u32_figures.fig_faults merged cases by case_id, so the CF/CFDW files (same case id as N48SH +45 hard, L_h 25) would have overwritten the N48SH bars. Excluded by variant.
- New p52/u35_appendix.py -> u35_appendix.json; figure u35_appendix_3d.png.
- design.md §8, README row, peer read C.10, Q2 dated line, TASKS U35 block.
- Departure from brief: Q2 line does not say "R1–R8 complete": R5 is not started (U32 report l.55). Said what is solved.
- Test: only failure is index.html stale (expected; U36 rebuilds).

## Note 3 — committed
- qc-falsifier: no blocking findings; two non-blocking fixed (C.10 heading, 2D citation). Committed on u35-appendix-foldin; no merge, no push.
