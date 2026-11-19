# u16-sws-fault-detection — notes to Kai (Strand)

## 2026-11-03 — started
- Unit / branch: U16 (SWS 3D-C stranded rope, 3D-D broken wires) / u16-sws-fault-detection, from u08-sws-3d 6ec64cd
- Worktree: C:/Users/stian/Prosjekter-u16 (Flux's checkout C:/Users/stian/Prosjekter not touched; its max/.venv used read-only)
- Plan: stranded 52 mm rope in H52 (hard wire, +80 °C floor corner), explicit outer strands, half-space mirror on the
  split plane; 2 hidden broken wires at several angles; verification vs 2D ring defect + dipole estimate + mesh study.
- Rope construction is not held (spec open item): wire count, wire diameter, jacket are [UNVERIFIED] parameters.
- Timebox ~6 h.

— Strand

## 2026-11-03 17:55 — progress
- Henrik's facts applied (Kai's two messages): H52/52 Powerplast stays headline; drawn Ø40 prototype head P40 added
  (rope3d.p40_case, drawings as source; N42 kept as N40SH Br [UNVERIFIED]; notch read as 10 mm groove to Ø98
  [UNVERIFIED, drawing reading]; prototype rope type unknown → scaled Powerplast placeholder [UNVERIFIED]).
- B_z read on a radial profile incl. R = 36.5 mm [UNVERIFIED, not in spec/register]; LF (B_r) and LMA (B_z) reported separately.
- Model: rope3d.py (18 fused 1+6 strands, jacket 1.0, homogenised core closing C), ~2 M unknowns at mesh level 1.5,
  ~5 min per Newton step at 14 threads. Running: H52 intact + headline fault; check 4 ring (2D done, 3D running).
- Not yet read: agent-notes/u17-bz-radius-henrik.md does not exist yet.

— Strand

## 2026-11-03 19:10 — committed
- Unit / branch: U16 / u16-sws-fault-detection (C:/Users/stian/Prosjekter-u16)
- Commit: a8fe24d — 3D-C stranded rope + check 4a ring-defect limit (3D vs 2D within 1.4 %)
- Ready for Kai's check: not yet (3D-D commit follows; P40 runs still to come)
- Note for publishing: rope3d.py carries the Syncrolift drawing numbers of the Ø40 prototype (P40_SOURCE); check
  them against identifiers.yaml before any publish.

— Strand

## 2026-11-03 20:15 — committed, stopping
- Unit / branch: U16 / u16-sws-fault-detection (C:/Users/stian/Prosjekter-u16)
- Commits: a8fe24d (3D-C + check 4a), 8b7966d (3D-D + U16 report). Not pushed, not merged.
- Ready for Kai's check: yes (H52/52). QC falsifier "no blocking findings" on both stages, after fixes.
- Headline: 2 hidden broken wires, B_r worst 4.40 / 2.66 mT at 3 / 5 mm, margin 20 / 12 against 2 × 0.11 mT.
- P40 (Ø40 prototype): built and meshed but the solve is ~20× slower per Newton step than H52 at equal size, cause
  not found (not the notch: the run without notch was just as slow). No P40 numbers to forward to Henrik yet.
- Needs Stian: hours.human [FILL]; decisions in tasks/reports/U16.md; CASAR request needs his go-ahead.
- Before any publish: P40_SOURCE in rope3d.py names Syncrolift drawing numbers; check against identifiers.yaml.

— Strand
