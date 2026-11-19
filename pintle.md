# Pintle — U41 format switch (9 Nov)

I am Pintle, building U41 (one link, two formats) from Kai's brief in kai.md.
Worktree C:/Users/stian/Prosjekter-u41 on branch u41-format-switch from 2c94172.

Record this rests on (rule 10): this is a presentation change to the SWS pages; no spec
row or data-register row is touched. Record read: U39 report (tasks/reports/U39.md) and
the U41 brief. No numbers, anchors, link targets or figures change.

— Pintle

## 9 Nov, build done, verifier running
- FORMATS + formats_nav() in build.py; SHORT_LINE replaced; short page calls B.formats_nav. Both pages rebuilt.
- Checks ok, 7 tests pass. HTML diff: +5 style lines, +1 header line each; long page -1 (old note).
- Project venv lacks `markdown`: built in a worktree-local .venv (git-ignored) with markdown==3.7 (CI pin).
- Short-page number test: format labels exempted (label "4 printed pages" is a name, not a sourced number).

— Pintle

## 9 Nov, done
Commit 9b0764f on u41-format-switch (not merged, not pushed). qc-falsifier: no blocking findings; N2 (exemption
scope) fixed, report corrected (N3, N4). Needs Stian: landing page; the typed "4" in the short-page label.

— Pintle
