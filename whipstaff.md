# whipstaff — U136 notes to Kai (join the simulator branches)

- Worktree C:/Users/stian/Prosjekter-u136, branch u136-dt-joined from b5478a7 (main tip verified from u05).
  Venv inside max/sws/line_beta/.venv (Python312 base, requirements.txt), ignored, not committed.
- Merges, --no-ff, history kept: u132-dt-full-scale (c1a8f33), u133-dt-temperature (aaeeb95),
  u135-reduction-brief incl. u134 (905d246). No conflicts in any merge; git auto-merged README.md, settings.toml,
  pipeline.py. Checked afterwards: every marked block (U132/U133/U134) whole, one each per shared file.
- README: one section "The three additions and their switches" at the end, marked U136 (1c3e57f). Nothing else.
- Suites run alone on copies (git archive of each tip into the scratchpad), same venv, same machine, full suite
  incl. slow: b5478a7 76+1F, u132 94+1F, u133 92+1F, u134 89+1F, u135 89+1F. F = the known 27.28 mm position
  proof in every tree. Joined: 123+1F (124 = 77 base + 18 twin + 16 thermal + 13 reduction), same F only.
- Scans: idscan b5478a7..HEAD 0 (17 572 added lines); scan_tree on my added lines and commit messages 0.
- Not done: no falsifier (the brief did not ask for one); combined check is a scratch script, not a test.
- Byte check: `run_beta.py --out <dir>` (defaults: mqtt, 2 lifts) on b5478a7 and on the joined tip; SHA-256 of all
  27 output files: 22 identical incl. every raw_*.bin and index file. The 5 others (report.json, per_second.json,
  session.json, fig_b3.html/png) differ the same way between two runs of b5478a7 itself: out path, wall time,
  speed-up, store_Bps per wall-sampled second (mqtt delivery timing).
- Item 3 (scratchpad combined.py, not committed): plant_first, 2 ropes, thermal summer_worst uncovered,
  reduction data detector + rest hold + dead band at_rest x3 + delta_rice, 20 m travel at 5 m/min, inproc.
  Works together: 27 680 produced = 22 101 at logger + 5 579 held at rest + 0 lost; 19 296 run frames bit for bit
  as the same twin with reduction off; bytes 34.27 MB -> 16.97 MB; two temperatures per frame (upper != lower in
  15 682 of 22 101). With 6 drops (5 in runs, 1 at rest, on two halves) and a 60 s network stop:
  injected 6 = box 6 = logger 6, backfilled 2 402, identity holds, 5 run frames missing, rest bit for bit.
  The README command line was run as written: 30.1 sim min in 230 s, lost 0/0/0.

— whipstaff
