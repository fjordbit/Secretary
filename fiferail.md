# Fiferail — U127 (digital twin fact page and disagreements list)

- Worktree C:/Users/stian/Prosjekter-u127, branch u127-dt-facts from b5478a7 (main tip verified from Prosjekter-u05).
- Added only max/sws/twin/dt_facts.md (F01–F47) and dt_disagreements.md (D01–D34: 25 (a), 9 (b)). No existing file changed.
- Found: "3 x converters" already gone from the chart script (U119); residue is the per-half "excitation" channel.
  Main's architecture.html already reads 16 channels; the u10 branch copy still 24. Buffer 4 096 MB = 21.8 h by the
  code's own count (22.6 h measured, 23.0 h line_calc). 125/s does not fit a 100 ms frame (settings.py raises).
- parts.yaml I01's conflict line names transmitter_line.md l.115 as out of date; it is not (listed as D34).
- States/screens/bending cycles: no project file on main; cited as outside (secretary log 20 and 23 Nov).
- Scans before commit: idscan (b5478a7, intent-to-add) 0; scan_tree 0.
- Falsifier (fresh Opus subagent, files only): 0 blocking, 7 should-fix, 11 minor; arithmetic and quotes all exact.
  All fixed: F13 counted as ruled; D26 (buffer) and D07 (base station = main station?) moved to (b), no value
  picked; D34 to (a) with its fix; F23 several values; F16 check bytes; 11 lines marked two values; paths, D13 full
  text, D20 whole sentence, F36 arithmetic; signatures removed from the pages. No second pass.
- Commit 591e1ab on u127-dt-facts (2 files, 312 lines added). idscan b5478a7..HEAD 0, scan_tree 0. No merge/push/export.

— Fiferail
