# U04 orchestrator — Capstan

## 2026-11-02 — started
- Unit / branch: U04 / u04-orchestrator (C:/Users/stian/Prosjekter-u04/max), from u12-cli-providers 6dce2a4
- Name: Capstan
- Plan: loop per orchestrator docstring, role prompts, stub rule seam, `max run`, scripted-provider test matching AgentLive, one live_cli run.

— Capstan

## 2026-11-02 — built, in QC
- Loop, RuleGate seam (R4 stubbed), spawn, hours, run.end, 8 prompts + spawned template, `max run --docs`.
- Deterministic test matches AgentLive kinds + rule transitions, ends needs_human on R6. Suite 213 passed / 5 skipped.
- Live: 2 runs on the subscriptions, both ended `blocked` after 3 revisions: the critic keeps finding real red
  regressions, so R3 never clears. Decision for Stian in the report. No more live runs.
- boundary.py (U1) touched minimally. qc-falsifier running. Not committed yet.

— Capstan

## 2026-11-02 — committed
- Unit / branch: U04 / u04-orchestrator (C:/Users/stian/Prosjekter-u04/max), from u12-cli-providers 6dce2a4
- Commit: 429cac0 — U4 orchestrator loop: run loop, rule seam, spawn, role prompts, max run
- Tests: 217 passed, 5 skipped. Scripted run matches AgentLive (kinds, rule transitions, R6 pending).
- Live: 2 runs, both `blocked` after 3 revisions (critic keeps raising real red regressions; R3 never clears).
- qc-falsifier: pass 1 one blocking (failed tool call usable as a source), fixed; pass 2 no blocking.
- Ready for Kai's check: yes (live done-when not met; see report "Decisions needed")
- Needs Stian: when critic findings stop blocking (R3); hours.model definition.
- Not pushed, not merged. Stopping.

— Capstan

## 2026-11-02 — restarted: R3 decision (via Kai)
- Merging u03-rule-engine (6cdb5c0) into u04; R3 on U3's real checker; critic findings -> proposed register rows -> needs_human.

— Capstan

## 2026-11-03 ~00:30 — committed (R3 rework)
- Unit / branch: U04 / u04-orchestrator (C:/Users/stian/Prosjekter-u04/max)
- Commits: 8685e92 + b1d51b2 (merges of u03-rule-engine 6cdb5c0, 23ff6de), b00471f — R3 per Stian's decision
- Tests: 369 passed, 5 skipped (Studio browser tests flaked under load earlier; green on rerun)
- Live run (one): R3 passed on v1 on the DEMO register, 5 proposed rows, Codex review BLOCKING -> ended `blocked` at R5. Did not reach R6.
- qc-falsifier: 6 passes; last no blocking.
- Ready for Kai's check: yes
- Needs Stian: what a blocking review should do (end blocked / one revision / needs_human).
- Over the 2 h timebox. Not pushed, not merged. Stopping.

— Capstan

## 2026-11-03 — restarted: review severity (via Kai)
- minor -> one writer revision + re-review (still blocking -> major); major -> needs_human; critical -> blocked. No live runs.

— Capstan

## 2026-11-03 — committed (review severity)
- Commit: dba9c1e — retry ladder (writer; orchestrator tweak; then Stian), layered policy defaults<module<user, floor
- Tests: 405 passed, 5 skipped. No live runs, zero quota.
- qc-falsifier: 4 passes; last no blocking.
- Outside U4: prompts/reviewer.md (U2's reviewer prompt; severity per finding). New: agents/review_policy.yaml, agents/policies/README.md. studio/ untouched.
- For Sheet (U5): blocked reason now "Independent review not passed: <severity>"; major ends orchestrator done "Waiting for your judgement on the review".
- Ready for Kai's check: yes. Not pushed, not merged. Stopping.

— Capstan
