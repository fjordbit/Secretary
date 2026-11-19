# Gudgeon — U37 identifier sweep (9 Nov)

Brief: kai.md "## U37". Worktree C:/Users/stian/Prosjekter-u37, branch u37-identifier-sweep from d455e3d.
Rests on: max/CLAUDE.md rule 10 (content and numbers unchanged); register sws/data/sws_data_sources.md
rows 340-341 ("supplier sheet requested via the head designer"); U17 report wording "the yoke drawing" /
"the ring-magnet drawing". The register has no [Rn] for the P40 drawings, so "drawing, on file" is used.

- Before scan: 758 whole-word hits (742 files). After: 716.
- Persons (index 10) -> "the head designer"; a branch name -> "the U17 branch"; a delivery-folder path ->
  "(drawings, on file)". Drawing numbers (11 yoke, 12 ring magnet) -> "yoke drawing, on file" /
  "ring-magnet drawing, on file". Values located and replaced by script; none printed here.
- Result json (2): the index-6 hit is the digits of a float in a result array (0.<digits>), a coincidence
  of the whole-word boundary at '.'; result value, not metadata -> not changed.
- Page sources changed (p52 design.md, rerun md) -> docs/sws/index.html rebuilt, --check ok.
- Tests: sws_head_test.py 0 failures; tests/test_sws_report.py 2 passed. Full suite: see report.
— Gudgeon
- Committed 94b354f on u37-identifier-sweep; qc-falsifier no blocking findings; after-scan 717 (744 files incl. report). — Gudgeon
