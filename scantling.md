# scantling — U96 builder notes

- Started U96 (yoke cut-out sweep). Starting state verified: u95-axial-liftoff tip = 5f5bbc5. Worktree C:/Users/stian/Prosjekter-u96, branch u96-yoke-cutout from 5f5bbc5.
- H40 yoke thickness 8.511 mm: coarse d = 5 for I/O; d = 10, 15 exceed it (= T). Coarse = ref + I×5 + O×5 + T×5.
- Script sws/3d/demo/yoke_cutout.py; defect_sweep.full_model gets an optional `cutout` band (default None = unchanged). Earlier record (sws_yoke_window.py, geometry_study §2) cut family T (r_yi..r_yo), 52 mm rope, shared head, judged on fault signal at 3 mm and at equal induction.
- Test: ref reproduces U95 (−41.93 / −14.79 / −9.72 / −2.00 / +0.52). T w20 flips B_z positive (+7 at 3 mm, +135 at 20 mm); short ×0.25; rope 1.94 → 1.70 T. Same-mesh no-cut-out scatter ~0.02 mT standing.
- Inside-band defined as smallest lift-off where |B_z| ≤ lim plus intervals (curves not monotone with a cut-out).
- Coarse done (905 s). Ref = U95. Every cut-out changes the answer, far beyond mesh scatter (same-mesh no-cut-out: ≤0.32 mT standing, ≤0.004 mT short peak). I/O grooves (d5) bring B_z through zero at 7.5–11.5 mm and it grows positive to +32..66 mT at 20 mm: the ±20 band is a window, not "from X on". O w20 d5: inside ±20 from 3 mm, short peak −10.7 mT there vs ref −1.43 at 13 mm; rope induction −3.8 %. Bridge steel over a groove at 2.0–2.16 T (saturated). T: B_z flips sign near the rope; short ×0.55..0.2; rope −6..−14 %. Long-loss level about doubles with grooves (−2.0 → −4.6 at 3 mm).
- Fine pass started 16:04: O w14–20 × d3–7, I w30–40 × d5–7, T w2,3,4,6,8.
- Fine done. On "largest short ΔB_z at smallest lift-off with |B_z| ≤ 20": O w18 d5 −10.91 mT at 3 mm (rope −3.6 %), O w20 d5 −10.74, T w3 −9.90, I w30 d5 −9.28 at 3.5 mm. All at the band's edge. At equal B_z at 3 mm the families are within ~10 %.
- H52 (yoke 12 mm): ref reproduces U95; O w20 d5 / I w30 d5 do little (7 mm steel left); O w20 d8 and T w3 bring 3–3.5 mm inside. The steel left over the cut is what counts.
- Commit 4a95195. Checks: 8/9 --check (build.py: report.html stale; rebuilt+diffed = only the U95 and U96 register rows; restored, not committed), pytest 180/181 (test_sws_report, same cause), idscan 0 (13 entries, 22818 lines), scan_tree 0 (added files + added lines). Falsifier running.
- Falsifier pass 1: FAIL, 2 blocking (ranking under the criterion skipped O w30 d5 and O w14–16 d5; rope-induction change missing beside several comparisons) + 8 minor (0.7 not 0.6 %; level range −3.3; zero crossings were step values; scatter 0.005; scatter wording and the d 3 exception; map showed interpolated values; 45 not 46; cold-reader glosses). All taken. No second pass (nothing blocking left).
- Tip e84b603. Rechecked: 8/9 --check (build.py, register rows only), pytest 180/181 (same), idscan 0, scan_tree 0.
- Owed: equal-induction run (magnet re-sized); part-circumference window (3D); the mixed lift-off × cut-out unit; report.html rebuild at merge; prototype's real cut-out.

— scantling
