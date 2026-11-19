Session name: Tackle (U15 test model: hoist chain, rope, platform). Every entry ends with — Tackle.

# U15 test model — notes to Kai

## 2026-11-01 — started
- Unit / branch: U15 / u15-test-model (C:/Users/stian/Prosjekter-u15/max), from 43d62c2
- Plan: ADR (stack choice, PROPOSED) → twin/model/ v0 (hoist chain + rigid/flexible platform) → verification tests → run scenario → qc-falsifier → commit.
- Needs Stian: nothing yet.
— Tackle

## 2026-11-01 — milestone: v0 runs, tests green (uncommitted)
- ADR 0009 (0006 = U12, 0008 = U10 draft): Python first, FMI 2.0 wrapper later — PROPOSED.
- twin/model/: params.demo.yaml (all DEMO, sourced), rigid + flexible platform, hoist chain, 50 ms do_step, FMI stub.
- 15 verification tests pass (statics, off-centre hand calc, indeterminacy, energy, speed loop tau, rope frequency). Full suite 110 passed.
- Next: README + report, then qc-falsifier, then commit.
— Tackle

## 2026-11-01 — milestone: report written, qc-falsifier running
- tasks/reports/U15.md, twin/model/README.md done. Spawning qc-falsifier on the uncommitted diff.
— Tackle

## 2026-11-01 — committed
- Unit / branch: U15 / u15-test-model (C:/Users/stian/Prosjekter-u15/max)
- Commit: daa269a — U15 test model v0: hoist chain + rigid/flexible platform, first principles
- QC: pass 1 no blocking; pass 2 (fix delta) one blocking = wrong EI limit text (from QC's own pass 1). Fixed with QC's measured numbers + boundary test; not re-QC'd a third time.
- Ready for Kai's check: yes. Not pushed, not merged.
- Needs Stian: ADR 0009 decision; new signal ports in the SWS chart; hoist order/grouping (Q8).
— Tackle
