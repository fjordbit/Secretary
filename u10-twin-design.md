Session name: Keel (U00 foundation, U10 twin and shared flow core)

## 2026-10-30 — started
- Unit / branch: U10 (redefined, Stian approved) / u10-twin-design (C:/Users/stian/Prosjekter-u10/max, from main 42dcd47)
- Scope: no twin code exists (searched Prosjekter, old/, agentic/, new/, systems-integration/).
  U10 changes from "wrap twin.platform_load" to "twin + shared flow: design defined":
  1. twin/DESIGN.md: decided / open, taken from the decision log, architecture.html and execution.html.
     No new numbers.
  2. Shared chart contract (JSON schema): blocks, ports, wires, edges, frames, per
     flow-graph-principle.html. One MAx agent flow and one twin flow as examples.
  3. Mapping of MAx onto it: roles become agent blocks, handoffs become message edges.
     The run log stays as frozen in ADR 0005.
  4. twin.platform_load as a tool contract only.
- Found: U12 takes ADR 0006 and edits TASKS.md (U12 entry, U4 deps). I will use ADR 0007
  and touch only the U10 entry and the U5 node-positions line.
- Asked Kai: OK on ADR number and TASKS overlap with U12?
- Needs Stian: nothing yet.

## 2026-10-30 — committed
- Unit / branch: U10 / u10-twin-design (C:/Users/stian/Prosjekter-u10/max)
- Commit: 1968e7f — U10 Twin and shared flow: design defined (no twin code yet)
  (twin/DESIGN.md, flow/ chart schema + 3 examples, ADR 0007, TASKS U10 entry + U5 line,
  report tasks/reports/U10.md; 68 tests pass)
- QC: qc-falsifier first pass had 3 blocking findings, all fixed; second pass found none.
  Not pushed, not merged.
- Ready for Kai's check: yes
- Needs Stian:
  1. Approve the CLAUDE.md repo-map row for flow/ (proposed in the report, not applied).
  2. identifiers.yaml was not readable here (permission check). New files use generic
     placeholders; a grep for the names in the twin docs found none.
- Session stopped.

## 2026-10-30 — committed (Kai follow-up)
- Unit / branch: U10 / u10-twin-design (C:/Users/stian/Prosjekter-u10/max)
- Commit: 6c7b03d — placeholders in twin docs; DESIGN.md as a short index
- Ready for Kai's check: yes
- For Kai:
  1. I could not read identifiers.yaml, so I inferred the term (the one name in exactly the 6
     twin files). Please confirm with git grep -i against the list. The project number next to
     it is now [PROJECT NO].
  2. The same name is still in 5 sws/ files (not mine to touch) and in git history
     (1968e7f, older main commits). Decide before any push.
- Session stopped.

## 2026-10-30 — finished
- Kai checked 6c7b03d: right term; sws/ hits fixed on u08 (b3d80a0); history handled by
  publishing snapshots only; DESIGN.md index accepted.
- U10 is done. It stays on u10-twin-design until Stian merges.
- Still with Stian: the CLAUDE.md repo-map row for flow/ (proposed in tasks/reports/U10.md).
- Session stopped.

## 2026-10-30 — reopened: draft ADR 0008 (Stian asked)
- Branch: u10-twin-design. Draft, uncommitted: docs/decisions/0008-firm-core-modules-and-rule-packs.md
- Content: a firm core for every module (principles, chart format, names as deployment data);
  modules bring profiles and rule packs; R2 moves to docbot/techdoc (with sub-modules report,
  spec, calc, test/fat/hat/sat, manual); sales, training and archive are docbot siblings.
- Waiting on Stian: review of the draft; scope of identifiers.yaml (in the ADR's open list).
  QC before any commit.

## 2026-10-30 — name
- Session name is Keel, per Stian's new rule (via Kai). Also covers u00-foundation.md.
— Keel

## 2026-10-30 — waiting on Kai (ADR 0008)
- Stian: wait for Kai and the review, then update the ADR.
- Sent Kai the draft path, the review agent's 7 errors, and the open questions (a)–(f).
- ADR 0008 is still an uncommitted draft. I'll update it after Kai replies, then run QC.
— Keel

## 2026-10-30 — Kai's review received (cross-session message, ~04:04)
- Kai: apply fixes 1–7; withdraw the human-hours [OPEN]; identifiers.yaml section accurate, plus a project
  number and three allowed-private sites (climate cases), not to be named; no Stian answers yet on (a)–(f),
  keep [OPEN] Stian; Kai recommends R2 stays in the firm core with techdoc tightening it; (d) run-time drawing
  is the proposal; (f) [OPEN] for U5. Leave uncommitted until Stian approves.
- Applied: ADR 0008 updated; flow/README.md (core pages, chart@0.2 list, U5 note, run.start); flow/STANDARDS.md
  (new); twin/DESIGN.md (4 rows); U10 report section. 68 tests pass.
- QC pass 1: 3 blocking (ISA-5.1 glyph status, README stating a proposed ADR as binding, ADR 0007 citation
  for off-graph agents/rules), all fixed with the non-blocking ones. QC pass 2 running.
- Note for Kai: the QC subagent opened max-private/identifiers.yaml (counts and keys only, it says no names
  were printed). I did not ask it to; my own read of that file is blocked. Telling Stian too.
— Keel

## 2026-10-30 — ADR 0008 ready for Stian (uncommitted)
- QC pass 2: 2 blocking (README read as in force; reference project number in the ADR), fixed.
  QC pass 3: no blocking findings. Cosmetic rewrap after it. 68 tests pass.
- Files (uncommitted, u10-twin-design): docs/decisions/0008-..., flow/README.md, flow/STANDARDS.md,
  twin/DESIGN.md, tasks/reports/U10.md. Commit only on Stian's approval (message "U10 ...").
- For Kai: the reference project number is still in committed docs/strategy/ on main; your call before any push.
- Ready for Kai's check: yes
- Needs Stian: approve the ADR; R2 in core or techdoc; P6 proposal; identifiers.yaml third value, owner,
  location, sales leads; CLAUDE.md flow/ row.
— Keel

## 2026-10-30 — Stian decided R2; commit authorised after QC
- Stian (in this session): provenance is mandatory in the root; each module selects which catalogue parts it
  inherits, including the source kinds it accepts. Manual override source = manual binding + who and when.
- Cross-module falsification (in this session, with Stian): no number found that cannot carry a source of some
  kind; only unaccountable numbers (model-invented, hand-typed results) fail, and R2 blocks those.
- ADR 0008 §1 split into 1a mandatory core and 1b catalogue. Stian: "commit it when QC passes".
- QC on the split: 1 blocking (techdoc/test needs measured values), fixed; re-QC running.
— Keel
