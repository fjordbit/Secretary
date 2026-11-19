# Yardarm — U88 notes (17 Nov)

U88 builder (Opus): export increment for U87 (84af27a..1cc9661, max/ subtree, first-parent) grafted on 1680bc1,
Pages snapshot in publish/SWS on 367549c, link proof on nine pages. Method as futtock.md / gybe.md. No identifier
values, no personal names.

- 03:07 (machine clock) started; timebox 1 h.
- Start verified: Prosjekter-u05 main 1cc9661 = D:/git/prosjekter.git main; ls-remote fjordbit/max main 1680bc1 =
  export clone tip; publish/SWS 367549c = ls-remote origin and maxflow. first-parent 84af27a..1cc9661 = 1 (U87
  merge); increment touches only max/.
- Export: work/ refs/mono/main17; tools/replay17.py (= replay16, new range/base) -> replay17 61067f3, "exact".
  fast-export --reference-excluded-parents refs/exp/out16..replay17 (in17.raw.stream); ref renamed with
  tools/rename17.py (command lines only, 1 renamed, 0 in data; output == raw with the one replacement);
  rewrite_names: 32 commands / 5 blobs / 0 messages (rw17.log); fast-import -> export main e6e2c14 (parent 1680bc1,
  FF), worktree reset, clean. verify_diff vs 1cc9661:max: same 6 strategy paths (5 OK, 1 pptx only-in-original).
  refs/exp/out17 = e6e2c14 in work/.
- Answers' front matter (6 answers; round.json, models.yaml the same fields): kind, round, backend, model,
  model_used, label, status, started/finished, seconds, dry_run, input_sha256, input_bytes, workdir and command
  (paths start at "~": temp work dirs and CLI paths; cursor command also carries the workspace path from "~" and the
  one-line instruction), sent/not_sent (file names, bytes); models.yaml a comment line and the three model rows. No
  user name, no expanded machine path, no account/org id, no key fragment. Nothing changed.
- Scans (u05 venv): tiptree17 896 files, 660 whole-word, per-file table identical to tip16. addscan17: 28 paths
  (21 A, 7 M, 0 D). Whole blobs report.html 86, sws_data_sources.md 23, TASKS.md 7 = old known hits. Added lines 2
  (owner-name entry) on re-rendered report.html lines; removed side the same 2. Round folder (README, both briefs,
  sent/, six answers, round.json, models.yaml, summary, rig_top_page), procedures/rig_sheet pages + builders,
  register row, message: 0. Substring advisory: no new. Pattern grep (user paths, key/account shapes, pdf,
  secretary/max-private) on added lines: 0. No pdf file. idscan 1680bc1..e6e2c14: 0.
- Tests in testtree17 (u41 venv): nine --check exit 0; ten SWS test files (p52 skipped) 181 passed.
- Snapshot on 367549c: 6 M, 21 A, 0 D; sws/ tree = export tip sws/ (55ecb64). unlink16: index 6, report 1, easy 2,
  procedures 2, rig_sheet 1 (as before); 0 new. Switch: eight entries on eight menu pages, current once, targets
  exist; rig_sheet has no switch, not on the menu.
- New links (procedures #st-proto "one-page top sheet"; rig sheet first page "rig_top_page.md"): both
  https://github.com/MAx-Flow/SWS-Documentation/blob/main/sws/procedures/rounds/2026-11-17-test-sheet/rig_top_page.md
  — GitHub file view of the Pages repo; target committed in the snapshot (and in the export tip at the same path).
  The new .md files carry no links of their own.
- Links tools/links17.py (= links16), export-v3/links17.txt (relative/own-repo/external, broken): index 384/0/0,
  report 497/63/39, easy 62/0/0, hardware 42/303/0, software 19/310/0, housing 79/156/0, procedures 115/20/0,
  sensor 53/94/2, rig_sheet 23/5/0; broken 0 on all nine; re-run on git archive of the commit: 0 broken.
- External: 38 distinct, same set as U86; 0 new, no HEAD sent.
- Visible text procedures / rig_sheet (visible17.txt): 0 on every pattern. Print (headless Edge, snapshot copy, A4):
  rig_sheet17.pdf 5 pages.
- index.zip rebuilt (snapshot report.html + old mp4, byte-checked), untracked; old at index.zip.before-u88.
  pubtree17 (+_titles, _unzipped) 563 files, 397 hits, per-file table identical to pub16; _titles 0. Snapshot
  increment: 2 owner-name hits added on re-rendered report.html, removed 2; advisory no new. Commit 7054acf (tree
  e9afcef = scanned staged tree); idscan 367549c..7054acf 0. git status: only index.zip untracked.
- Push commands (Kai's):
  git -C C:/Users/stian/export-v3/export push https://github.com/fjordbit/max.git main:main
  git -C C:/Users/stian/publish/SWS push origin main
  git -C C:/Users/stian/publish/SWS push maxflow main
- 03:14 done. Nothing pushed. Local main untouched.

— Yardarm
