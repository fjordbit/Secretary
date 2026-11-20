# Kingpost — U121 notes (20 Nov)

U121 builder (Opus): export increment 062b8bd..b5478a7 + Pages snapshot. STOPPED before the export on a brief STOP
condition. No identifier values, no personal names.

- 11:56 (machine clock) started.
- Start verified: Prosjekter-u05 main b5478a7 = D:/git/prosjekter.git main; ls-remote fjordbit/max main 8beade9 =
  export clone tip; publish/SWS 67c6e1f = ls-remote origin main and maxflow main (only index.zip untracked).
- Increment: 33 first-parent commits, all under max/; 396 paths (362 A, 34 M, 0 D), 46.5 MB at the tip
  (tools/incr20.py in export-v3). Units match the brief's list; also touched, by U119: flow/examples-0.2-draft
  (2 M, sws-shiplift chart json 0.7 MB), twin/Shiplift-twin-analysis/docs (1 M), sws/figures/decided (2 M);
  by U100: sws/data (1 M). New: spec rev131 .docx (0.9 MB; earlier revs' .docx already in the tree), six .log
  files and run_wire.sh under sws/3d/falsify (U101).
- STOP: one file over 5 MB in the increment: max/docs/sws/report.html (modified), 16,144,829 bytes (was 16,130,841
  at 062b8bd; the same file has been 16 MB on GitHub through every earlier export). Nothing else over 1.5 MB
  (largest added: sws/3d/h40_on_38/results/stand.json 1.49 MB; docs/sws/results.html 1.35 MB).
- Seen before stopping (read-only): no PDF; no compiled binaries, venvs, build folders or caches (line_beta and
  c_half are source: .c/.h/.py/.toml/.ini/.gitignore); 0 expanded user paths on added lines outside docs html;
  the two prototype-head figures (groove_plots/fig_d_prototype.png, falsify/h_prototype_head_bz.png) are
  calculated plots, not drawing images. Front matter, scans, tests, snapshot, links: not done.
- Nothing exported, nothing committed, nothing pushed; local main, export clone and publish/SWS untouched.

— Kingpost
