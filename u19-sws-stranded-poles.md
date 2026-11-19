# u19-sws-stranded-poles — notes to Kai (Fathom)

## 2026-11-03 21:20 — started
- Unit / branch: U19 (SWS 3D-C2: stranded 52 mm section under the poles) / u19-sws-stranded-poles, from u16-sws-fault-detection 50475e3
- Worktree: C:/Users/stian/Prosjekter-u19. FEM env: C:/Users/stian/Prosjekter/max/.venv used read-only (as U16 did); nothing in Prosjekter touched.
- Timebox: 4 h wall-clock, to ~01:20. Late-night run; will stop and report at the box.
- Plan: section-length study (≥3 lengths) for B_rope / background / ripple, then the 2-hidden-wire headline on the longest section, two mesh levels.

— Fathom

## 2026-11-03 22:05 — progress
- Found: intact straight-lay stranded rope in a closed head is mirror-symmetric about every strand centre and valley, so a 10° sector is exact for 3D-C2. Added `sector` to rope3d.py (default 180 = U16 path). Cost at L_h 140: 0.48 M unknowns vs ~8 M half-space.
- Cross-check, L_h 25, level 1.5: sector B_rope 1.92748 T vs U16 half-space 1.92752 T; 3 mm background −39.143 vs −39.154 mT. Read-out noise on B_r(z=0) drops 0.059 → 0.014 mT.
- Running: L_h 25/60/100/140/180 at levels 1.5 and 1.0. First sign: L_h 60 gives 1.9398 T, above homogeneous — section effect not monotonic. Waiting for the long ones.
- Headline (stage 2) will use a 60° sector (fault imaged at ±120°, masked in read-out), validated against U16 half-space at L_h 25 first.

— Fathom

## 2026-11-03 21:40 — progress (clock correction: the "22:05" entry above was really ~21:30)
- 3D-C2 section study (10° sector, level 1.5): B_rope (flux def.) 1.9275 (L_h 25) → 1.9398 (60) → 1.9392 (100); homogeneous 1.9370. 140/180 and level 1.0 still running.
- 60° sector for the fault: tried and rejected. The fault has a global part (~0.2 mT at every angle), so the ±120° images bias the headline +4–7 %. Stage 2 runs on the half-space (U16 model): L_h 60 running now (4 M unknowns), L_h 100 next.

— Fathom

## 2026-11-03 22:06 — progress
- Lost ~25 min: three FEM jobs at 12 threads each on 12 physical cores stalled NGSolve (spin contention). Now ≤ 12 threads total.
- 3D-C2, level 1.5, B_rope (flux def.): L_h 25 1.92748 / 60 1.93980 / 100 1.93925 / 140 1.93882 / 180 1.93899 T; homogeneous 1.93697. 140→180: +1.7e-4 T. Running: 250/320, level 1.0 repeat, boxes 600×800 and 1200×1600 (for the floor at an unbounded domain).
- Headline on the half-space at L_h 100, level 1.5 (6.2 M unknowns) started; level 1.8 after it. Estimate ~1.5 h + ~1.2 h — tight inside the box; will report what finishes.

— Fathom

## 2026-11-03 22:40 — progress, one finding that changes the question
- Any two FEM jobs at once stall here (even 8+4 threads). Now strictly one job at a time.
- Half-space at L_h 100 cannot assemble: 6.2 M unknowns → NGSolve "bad array new length" (index overflow). Coarser levels don't help (strands are curvature-limited, 5.8–6.0 M). Headline will run at L_h 60 (4.0 M), the longest that fits.
- Box matters more than section length: at L_h 180, box 300×400 stranded 1.93899 / homogeneous 1.93697 T; box 600×800 stranded 1.92308 / homogeneous 1.92413 T. The stranded-minus-homogeneous sign flips with box size. Running the 1200×1600 box and the L_h series at 600×800 before the floor statement.

— Fathom

## 2026-11-03 23:00 — stage 1 result, in QC
- Finding: the 1.92 T floor does NOT hold on the stranded rope at a realistic domain. B_rope (3D-A flux def.), L_h 180: 1.939 T at the 3D box 300×400, 1.923 at 600×800, 1.917 at 1200×1600; extrapolated ~1.914–1.915 T (≈0.3 % short). The stranded-minus-homogeneous offset flips sign with box size, so U16's small-box comparison does not carry.
- Side finding: the 3D sensor background (U08/U16, box 300×400) reads ~12 % high in magnitude against the 1200×1600 box.
- Section length converged at 300×400 and 600×800 (140→180 mm: ≤ 1.7e-4 T). Not shown at 1200×1600.
- qc-falsifier (on fable) running on stage 1; headline run (half-space L_h 60) solving.

— Fathom

## 2026-11-03 23:10 — committed stage 1
- Unit / branch: U19 / u19-sws-stranded-poles (C:/Users/stian/Prosjekter-u19)
- Commit: 1b9f0ae — 3D-C2 section length + domain size; floor does not hold on the stranded rope (1.917 T at 1200×1600, ~1.915 extrapolated). docs/sws/index.html rebuilt, --check ok.
- QC (fable): no blocking findings; 7 non-blocking fixed.
- Stage 2 change of plan: the half-space at L_h 60 (4 M unknowns) would need ~3 h (no Newton step after 13 min). Using the 60° sector instead with a ratio correction: headline(L_h 100) ≈ U16 half-space L_h 25 × [s60 L_h 100 / s60 L_h 25], same mesh level, levels 1.5 and 1.8. Labelled as derived, not a direct half-space solve.
- Ready for Kai's check: stage 1 yes.

— Fathom

## 2026-11-03 23:45 — stage 2 at risk
- 60° sector at L_h 100 (1.8 M unknowns) stalled in Newton at step 4 (line-search step 1/1024), as the long-section runs at L_h 250 and box 2400 did. Pattern: the longer the stranded section, the worse the Newton/CG behaviour. Stopped.
- Last try inside the box: 60° sector at L_h 60 (stranded 10 mm under the poles; its B_rope is within 9e-4 T of the converged section at 300×400). If it does not converge by ~00:35 I stop and report stage 2 as not done.

— Fathom

## 2026-11-04 00:08 — stage 2 done (derived), in QC
- Headline (2 hidden flank wires) re-checked by a ratio method on the 60° sector: section L_h 25→60 +1–2.6 %, box 300→1200 −2–4 %; net −1 to −2 % vs U16: B_r 4.33 / 2.63 mT (3 / 5 mm), B_z 6.14 mT, R 36.5 0.95 mT; margins 19.7 / 11.9. Verdict unchanged.
- Not done: direct half-space on a pole-covering section (6 M index limit / ~3 h), two-level mesh check at L_h 60 (level 1.8 stalled), stage 4 (soft wire −40 °C).
- U19.md written; U16.md "Not to forward yet" amended (rope induction settled; backgrounds at 300×400 box still not forwardable, read 12–16 % high).
- QC (fable) on stages 2–3 running; then commit.

— Fathom

## 2026-11-04 00:13 — committed stages 2–3
- Commits: 1b9f0ae (3D-C2), fe2afc1 (3D-D2 + U19.md + U16 amendment). Not pushed, not merged. docs index rebuilt, --check ok.
- Ready for Kai's check: yes. QC (fable) no blocking findings on both.
- Trying stage 4 (easy wire, −40 °C) in the 10° sector — cheap; will stop by ~00:50 whatever the state.

— Fathom

## 2026-11-04 00:21 — stopping
- Stage 4 (easy wire, −40 °C) stopped: L_h 25 solved (stranded 2.0339 / homogeneous 2.0405 T at box 300×400, not committed), L_h 140 stalled in Newton (line-search steps 1/1024). Listed under remaining in U19.md.
- Final: commits 1b9f0ae, fe2afc1 on u19-sws-stranded-poles. Worktree clean, no FEM job left running. ~3 h wall-clock.
- Needs Stian: hours.human [FILL]; two decisions in U19.md (floor shortfall ~0.3 % on the stranded rope; move 3D runs to a 1200×1600 box).

— Fathom
