# jib — U131 (prototype recording, Codex through a script loop in the round tool)

Started 25 Nov. Main tip b5478a7 verified (Prosjekter-u05). Worktree C:/Users/stian/Prosjekter-u128 on
u128-prototype-data-codex at b5478a7, clean, no commits: verified. Data copy: 31 files, md5 identical to the
original. Probe files (out/p1.txt, out/probe_inside.txt, probe/) removed.

Model: gpt-5.3-codex-xhigh (Cursor `agent models`: newest Codex 5.3, "Extra High"; -fast excluded).
Round tool as it stands; --work-base C:/mrw131 (keeps the user folder name out of the workspace path),
--out <work folder>/loop/rounds. Limits: tool defaults, 200 KB per file, 400 KB total.

Round 1 brief scanned (scan_tree 0), notes.txt scanned 0. Round 1 sent: 14 676 bytes, 489 s, answer
81 KB; first line quotes the brief's last line word for word (whole input received). Three scripts, all
read: no network/subprocess/shell/eval/deletion; reads data arg, writes output arg only. Fix recorded:
np.trapz -> np.trapezoid in scripts 2 and 3 (removed in numpy 2.5.5; renamed function, no logic change).
The venv needs subst R: (its pyvenv.cfg points to R:\pybase): R: mapped to the work folder, to be removed
at the end. V: belongs to the other builder: not touched.

Scripts ran 4 s / 11 s / 2 s, exit 0, outputs 399 279 bytes (model was asked for <= 250 KB). Its own parser
drops every record stamped on a whole second (1 %): left as is (its logic), no hint given.
Round 2: 398 497 bytes; optional files dropped (2); the tool's 400 000-byte total left out
steady_channel_means.csv (named in the input). Model quoted the brief's last line AND the last line of the
last file: whole input read. No further scripts asked, no failures -> no round 3 (brief: round 3 only then).

Check (15 figures from raw, own scripts in analysis_b/check/): 8 agree, 1 arithmetic only (day drift rests on
steady3), 6 differ: missing records (parser), tones +1 % (same cause), ripple vs speed (its 1 s smoothing),
steady3 event count (3, not 1/2) and after-levels, steady4 sums (unscaled). Not checked: repeatability,
run9/10 position error, steady4 per mm.

Commit 181b99c on u128-prototype-data-codex (49 files, analysis_b/); idscan 0, scan_tree 0 (briefs, round
inputs, answers, repo folder). No merge, push, export.
Front matter of the answers carries workdir "C:\mrw131\..." (temp folder, no user name) and the tool's usual
"~\AppData\..." command path, as 38 earlier committed answers do: kept, flagged to Kai.
Left behind: C:\mrw131 empty (removal blocked by the harness); R: removed; work folder loop/ (briefs, rounds,
outputs); Cursor's own state in ~/.cursor; check cache in the session scratchpad. No API key read.

— jib
