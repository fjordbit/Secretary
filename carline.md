# carline — U114 live parts table (builder for Kai)

- Worktree C:/Users/stian/Prosjekter-u114, branch u114-parts-table from 1735f4b (main tip verified 1735f4b).
- Start 10:23; timebox 180 min.
- Sweep split over five read-only helpers: spec + redlines; register + 3d notes; hw-selection/housing/procedures;
  pages; the eight branches. Their rows are checked by render.py --check (quote must sit on the cited line).
- Liner: the record holds two things in the bore. Spec rev130 section 9 table: guard over the magnets Nitronic 60
  (UNS S21800) 1.5-2 mm or 316L annealed after forming; rope-contact liner UHMW-PE / PA6 / PEEK ~2 mm. Both kept.
- Two additions from Kai mid-run: (1) part "Installation facts given by the owner" (I01-I05, ruled, source outside:
  owner's statement); I01 carries a `conflict` line naming data_path.md (u108) and transmitter_line.md (u109) as out
  of date on rope position. (2) Every calculated row has an `arithmetic` field; render.py --check fails without it.
- Names ruled (sensing element etc.) as a `names` block at the top. Terms list: no project-wide list on main; the plot
  standard (u106 plotstandard.py) links each figure set to its own terms.md (groove_plots/terms.md, tradeoff/,
  data-path/, transmitter/, element_run_3/ on the branches). groove_plots/terms.md defines "Head" (magnets in a yoke,
  no board) and uses "sensors"; SWS, half, sensing element, channel, root box are not defined there.
- scan_tree on the folder: 0 after removing the venv path from README.
- Falsifier (fresh, 40 rows, seed 114): 4 blocking (L03 R31->R33; A05 line -0.713 and missing N48SH -0.768 / N52 -0.806;
  H10 "ambient" is an editor's reading, only "-40 ... 50 max" ruled) and 8 non-blocking; all fixed. Not re-run.
- Commit 5419949 on u114-parts-table: 28 parts, 153 rows. idscan 0 (1735f4b..HEAD), scan_tree 0. No merge, push or export.
  (Commit message says 29 parts; the table says 28.)
