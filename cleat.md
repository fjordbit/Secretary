# Cleat — U23 (review policy on the ladder: `on_major`)

Session name: Cleat. Worktree C:/Users/stian/Prosjekter-u23/max, branch u23-ladder-on-major from main 4730e63.

## 2026-11-07 — started

Worktree created. Reading the brief's READ list before writing anything.

— Cleat

## 2026-11-07 — found while reading (decisions under uncertainty)

1. **Decision letter.** The brief says "naming this decision F". F is already taken (4 Nov:
   no hidden agents; ADR 0011 decisions A–G, flow-driver §14). Two Fs would make "decision F"
   ambiguous in every document. I proceed with **H** (next free letter) in ADR 0012 and §14.
   A rename is a search-and-replace if Stian prefers another letter.
2. **Third chart.** `plc-code-improve` (module plc) also carries `policy: review`; removing
   `policy` from the schema makes it invalid, so it must change too. Under the old default
   table a blocking major there stopped for a person. I set it to `on_major: revise` (the
   default, and what §11.3's walk-through already assumed: "review -> revise -> count"). This
   changes that loop's behaviour on a major; flagged for Stian.
3. **User-settings guard.** The only place that refused a user settings file inside a git
   checkout was `ReviewPolicy.load`. Deleting the class would drop that guard for the file
   that still holds accounts and the identifier path. I keep the guard as a small settings
   layer loader (module name + user file checks, no review keys), per the addendum.
4. **Stale `review:` keys** in a user or module file: not read any more; preflight's `policy`
   line turns amber naming the file, the run goes on (the chart is what decides).

— Cleat

## 2026-11-07 — design and build done, QC next

Design round 9 written (flow-driver.md), ADR 0012 (decision H), build done on
u23-ladder-on-major (not committed yet). Suite green on the U05 venv from the u23 folder.
Running qc-falsifier now.

— Cleat

## 2026-11-07 — Kai's F(ii) input folded in

Built Kai's recommendation as H(ii): the ladder counts every finding whatever the review's
`blocking` flag; blocking with no finding = major; the flag stays on the tape. The option not
chosen (flag as gate) and its one argument (minor nits now always force a revision; release
needs a review with no findings) are in tasks/reports/U23.md. Suite green, 568 passed.

— Cleat

## 2026-11-07 — committed, ready for Kai's check

Commits on u23-ladder-on-major: cb99320 (the unit), plus a report-only follow-up. Not pushed,
not merged. qc-falsifier: no blocking findings (pass 2). Open for Stian: H(ii), plc on_major,
decision letter H. Over the timebox (about 3.5 h against 3 h).

— Cleat

## 2026-11-07 — H(ii) softer form committed

Stian's ruling (relayed by Kai): softer H(ii), letter H, plc keeps revise. Built and committed
on u23-ladder-on-major. 572 passed, 5 skipped. qc-falsifier pass 3: no blocking findings.
For Kai: QC notes the ruling is not yet logged in kai.md; please log it there.

— Cleat
