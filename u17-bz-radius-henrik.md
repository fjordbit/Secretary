Session name: Compass (U17, Henrik's questions on the SWS head geometry and Bz radius). Every entry ends with — Compass.

# u17-bz-radius-henrik — notes to Kai

## 2026-11-03 — started
- Unit / branch: U17 / u17-bz-radius-henrik, from u08-sws-3d 6ec64cd
- Worktree: C:/Users/stian/Prosjekter-u17 (Prosjekter = Flux, Prosjekter-u16 = Strand: not touched; max/.venv of Prosjekter used read-only)
- Drawings read (vectors measured with PyMuPDF, not by eye): yoke sd00039125 A.1 = Ø40 PROTOTYPE, Ø102/86 × 105, S235JR,
  magnet seats Ø88 × 20 at both ends, notch on the OUTSIDE at mid-length 10.0 wide × 2.0 deep (Ø102 → Ø98), 2×Ø12 radial holes
  at 28.5 from each end (not axisymmetric, not modelled). Ring magnet sd00037347 A.1: R24–R44 × 20, N42, radial. Pole gap 65 mm.
  Agrees with Strand's reading (Kai's message). The old sws_yoke_window.py modelled a full-wall air window on the H52 head — wrong on three counts.
- Plan: 2D axisymmetric model of the drawn Ø40 head (own build function, fem-2d solver), notch vs no notch, one mesh; B along r at z=0;
  Bz sensor radius sweep + Br at its radius; same figure of merit; U17 report; Norwegian reply draft in secretary/inbox/drafts/.
- Timebox ~4 h. 2D only.

— Compass

## 2026-11-03 ~18:00 — analysis done, QC running
- Study ran (2D, ~1 min): results/bz_radius_2d.json (+ refine 0.7 check), 3 figures, tasks/reports/U17.md, Norwegian draft at
  secretary/inbox/drafts/2026-11-03_henrik_reply.md. qc-falsifier (fable) running on the diff; commit follows if no blocking findings.
- Headline (Ø40 head as drawn, notch 10 × 2 mm outside): B_rope 1.994 → 1.989 T (−0.2 %); defect signals at the rope within ±1 % at
  equal induction → geometry_study §2 conclusion holds; r0(Bz=0) 42.5 mm (= yoke bore) → 39.6 mm with the notch, moving 38.5–40.5 mm
  over the temperature/wire box; at R 36.5 the Bz signal is 11× smaller than at 3 mm and the movement term larger (0.8 vs 15 signal/movement).
- Needs Stian: see U17.md §8 (confirm notch/36.5/N42 with Henrik; is Bz an LMA-only channel; Strand's queue). [FILL] hours.human.
— Compass

## 2026-11-03 — committed
- Unit / branch: U17 / u17-bz-radius-henrik (C:/Users/stian/Prosjekter-u17)
- Commit: 602c6b3 — U17 SWS: Henrik's questions (notch, r0, Bz radius sweep, 2D). Not pushed, not merged.
- Ready for Kai's check: yes. qc-falsifier (fable): 4 blocking number findings in U17.md corrected, re-check "no blocking findings"; code/results clean.
- Draft for Henrik (Norwegian): secretary/inbox/drafts/2026-11-03_henrik_reply.md, [DATO] placeholder for Strand's first 3D numbers.
- Handed to Strand (U17.md §6): broken wire vs sensor radius 23/25/30/36.5/39.6 mm on the drawn Ø40 head; eccentricity 0.5 mm at 36.5/39.6; ring LMA defect in 3D at 23/36.5 as the 2D link; r0 in 3D on/off the split plane.
- Needs Stian: U17.md §8 (confirmations from Henrik incl. which rope the prototype ran; is Bz an LMA-only channel; Strand's queue); hours.human [FILL].
— Compass
