# Keelson (U22 builder) -> Kai

Started 2026-11-04 11:19. Worktree C:/Users/stian/Prosjekter-u22/max, branch u22-flow-driver.
Milestone 1 only, timebox 4 h (stop-and-report at 3 h if not green).

## Done
- driver.py: the chart runs (rounds, readiness, joins, delay latches, envelope, stall guard;
  executors io, agent, context, gate, ladder, condition, checkpoint). No sequence elsewhere:
  Orchestrator._run and the role steps deleted, roles.yaml deleted, prompts carry the wording.
- Boundary per (provider, model, account); tool specs and response schema now masked.
- max_core/flows/max/max-default-loop.chart.json (equal to the specimen, test holds it).
- SCHEMAS architect/judge/compliance{verdicts}; ReviewPolicy without attempts/tweak.
- `flow` run-log kind; `max run --flow`; preflight providers from the chart.
- Suite: 476 passed, 5 skipped, 1 xfailed (the acceptance test, strict xfail on C1).

## Blocked: design conflict C1 (needs Stian)
The chart's compliance block has `rules: [R3, R4]`. flow-driver §5: "a rule is carried when a
drawn block whose params.rules names it fires". So R4 is carried in round 1 when compliance
fires, before gate_r3; §11.1 says the specialist carries it. Effect: `R4 checking` lands before
`R3 triggered` (acceptance test red), and gate_r4 checks R4 on every run. With compliance
`rules: [R3]` the transitions match exactly (scratch run, not committed). Not mine to change.

## Other findings for the owner
- C2: only the planner sees the question; writer, critic, compliance, reviewer, orchestrator,
  specialist do not (today all did). Live-run risk.
- C3 (wording): no writer -> critic edge; C4: critic re-check no longer sees earlier rows.
- If ~/.max/settings.yaml has review.attempts or tweak, preflight's policy line goes red now
  (decision E). I did not read that file.

## Decisions I had to make (reading, not departure)
- The `R4 checking "<role> at work"` line is logged only for a rule whose gate is
  `active: when_carried` (§5/§10 name R4 only); other carried rules log nothing.
- Compliance answers R3 always and R4 when a specialist proposal is present (prompt file).
- Gate fail findings: R3 = the open red items; other rules = {rule: reason}.

— Keelson

## Commit 2283e86 (u22-flow-driver, not pushed)
- QC (qc-falsifier) found one blocking item: the §9 test (params.rules == binds_to) fails on
  the chart. Declared as C5, strict xfail. Also C6 (tool-caller summary no longer R2-checked).
- QC non-blocking, open: C1 also makes R4 fail on runs where R3 passes on v1 and no
  specialist was asked (3 escalations, then needs_human); a ladder fed by two review inputs
  takes one per round; --module default chart (§7); SCHEMAS["tweak"] left.
- Suite: 476 passed, 5 skipped, 2 xfailed. .env copied into the worktree (gitignored) for the
  owner's live run. Stopped at milestone 1.

— Keelson

## Round 7 implementation (Kai's brief, 4 Nov)
- Tiller's b26d1b4 resolved C1-C6 + QC opens. Implemented: v0 never held, task first (chart
  edges + prompt files), cumulative rows already in place, compliance prompt names R3 (R4 on
  the specialist section), binds_to/for_role/xfail test deleted, ladder review join, --flow
  default, SCHEMAS["tweak"] deleted.
- Suite 479 passed, 5 skipped, no xfail; test_run_matches_agentlive green; check_u21 all ok;
  chart copies identical. QC pass running before the commit.

— Keelson
- Committed round 7: see git log (u22-flow-driver, not pushed). QC no blocking; open
  non-blocking: a ladder with 2+ review inputs plus tick/stop cannot fire on tick/stop
  while only some reviews have arrived (no saved chart has that shape). Stopped.

— Keelson

## Milestone 2 (Kai's go after live run 1, 4 Nov)
- Built: flowcheck.py + `max flow check`; preflight flow/boundary/model lines; settings map
  in the preflight event; doctor --flow/--refresh. Suite 502 passed, 5 skipped.
- IMPORTANT for the next live run: the boundary line is required. Stian needs MAX_IDENTIFIERS
  (a YAML list file) or `identifiers: none` in ~/.max/settings.yaml, else preflight aborts.
- Live-run notes recorded under "QC open" in U22.md (openai model unknown -> settings map;
  reviewer cannot see sources -> chart edge, owner; majors passed because blocking=false,
  no policy value decides it).
- QC pass running; commit after it.

— Keelson
- Milestone 2 committed (see git log). QC's 4 blocking fixed. Stopped; reporting to Kai.

— Keelson
- 14054c6: identifier list accepts mappings with a non-empty name (Kai's follow-up). Starting M3.
- M3 built (uncommitted): both new flows run scripted end to end; plc.complexity tool;
  architect/judge/plc_improver prompts; two skills. Suite 520 passed. Design conflict C7:
  the two new charts lack `task` on some agent blocks (§2.1 round 7 says every block).
  Both carry [MODEL ID] placeholders: no live run possible until Stian fills them.
  QC running.
- M3 committed (see git log). QC blocking fixed. Stopped; reporting to Kai.
- round 8 follow-up committed: 93e9607. Starting M4 (Studio).
- M4 (Studio) built, uncommitted; suite 527 passed incl. browser tests. QC next.
- M4 committed: 57ef3ce. Stopped; reporting.
- M5 built (uncommitted): WYSIWYG replay, palette, vault lock, bridge masking, accounts, --probes, ladder label, flags from claude_cli. U22.md rewritten complete. QC running.
- M5 committed: 9e66432. Done; reporting to Kai for the Fable check.
- Bosun fixes committed: 5070a01. Stopped.
