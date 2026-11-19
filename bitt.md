# Bitt (U45) — notes to Kai

I am Bitt (U45: the architect's brief reaches the reviewer and the judge). Brief: kai.md "## U45".
Worktree C:/Users/stian/Prosjekter-u45, branch u45-brief-to-judge from 0ef5b68; work in max/.

Record this rests on (rule 10):
- docs/design/flow-driver.md §11.2: the judge's inputs are listed as a closed list
  ("inputs task, current, previous (delay), review"); round 8 (C7) adds `task` to reviewer and
  judge and says "What each block receives per round is otherwise unchanged". This is the
  closed list the brief means; the owner's 9 Nov ruling changes it (recorded as a dated paragraph).
- §2.1 prompt rendering (inputs in port order, null omitted; v0 never held), §3 ready rule (a)-(c)
  (a non-trigger input with a default never joins a correlated set), §4.3 the judge, §8 Judge row,
  §9 prompts live under max_core/agents/prompts/.
- ADR 0011 (docs/decisions/0011-the-engine-runs-the-chart.md): silent on per-block inputs; no
  schema-version rule for a wire change. Status stays ACCEPTED; chart schema stays 0.2-draft.
- Default loop has no architect block: untouched.

— Bitt

## Progress (9 Nov)
- A: dated U45 paragraph added to flow-driver.md §11.2 (owner's ruling recorded; ADR 0011 silent, unchanged).
- B: brief input (default null, held, not a trigger) + 2 data edges on wire `brief`, both chart copies;
  judge.md / reviewer.md told about the brief; check_u21 Judge probe keeps task+current by name.
- C: 3 new tests in test_flows_m3.py; suite 591 pass / 1 pre-existing fail (test_review_round xai, same on
  base); flow check, check_u21, preflight (stubs), Studio arrange all ok; ruff no new findings.
- qc-falsifier running.

— Bitt

## Done (9 Nov)
Commit 03571af on u45-brief-to-judge (no merge, no push). qc-falsifier: no blocking; non-blocking held-brief
wording and sign-off assertion fixed. Report: max/tasks/reports/U45.md. Needs Stian: seeding; severity of the
judge's "no brief" finding.

— Bitt
