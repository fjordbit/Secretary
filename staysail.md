# staysail — U139, the Progress plan page (builder notes for Kai)

Worktree C:/Users/stian/Prosjekter-u139, branch u139-progress-plan from 67866d8 (checked: main's tip).

## What was built
- max/docs/sws/plan.html: page shell (site CSS from build.py PAGE, menu via formats_nav, light/dark by
  prefers-color-scheme like the other pages), written by build_plan.py (--check as the other builders).
- max/docs/sws/plan.json (49 tasks, 10 controlling dates, 5 rulings/inputs needed, 8 areas) and record.json
  (129 work rows, 43 rulings, 26 open items). The page FETCHES both on load (relative, cache no-cache). Not embedded:
  the release copies docs/sws/ whole (snapshot B step) and the MAx-Flow Pages workflow uploads ./docs as static, so
  .json is served; editing a file then needs no build. From disk (file://) the browser blocks fetch: the page says so.
- max/docs/sws/check_plan_data.py (stdlib): prints ok + counts or problems. The page runs the same checks in JS and
  lists problems in a red box at the top.
- Menu: FORMATS entry 10 "Progress plan" (last). All menu pages rebuilt (diffs = the menu line only), link line on
  index.html and easy.html via build_short/build_easy. tests: test_sws_easy/hardware menu lists + new test_sws_plan.py.
- results.html was stale on main (only line-number shifts in sws/line_beta/README.md citations, L99..106 -> L106..113);
  the rebuild carries them.

## Leads
First briefed as function labels; then Kai relayed the owner's ruling (26 Nov): first names shown as leads,
exactly as the task source has them, only in plan.json `lead`. Done; no `leads`/`lead_names` lists. The label mapping
I had derived (now unused): Stian = Project lead; Henrik = Measurement and head design; Ramin = Project management;
Torbjørn / Mechanical team = Mechanical design; Marius = Rope supplier contact; SWS/MRT team, SWS team, Project = Team.

## Rewrite choices
- Merged 2 history rows told twice: the semi-blind element round (reviews row says "see U113") and the 20 Nov rerun
  with newest models (U122/U123 in both sections); kept under Sensing elements, flagged review_round. 16 review rows.
- Rulings: 42 from the history + 1 (26 Nov: two sides, 102 winches, 6 stations, 204 SWS, 408 halves) = 43.
- Dropped: the AI run cost (82.19 USD), model names and versions, unit numbers, commit ids, paths, issue owners.
  Kept: part prices (converters per half A 15 ... USD) as design content — your call if "no cost figures" meant those.
- Basis per row: calculated / measured / data sheet / blank. "measured" on the three recording analyses and the
  detector on the recording.
- The procedures-page row moved from "Prototype" to area "Test, calibration and installation" (that area had none).
- Tasks 1-20 keep the schedule's wording ("sensor" etc.) except: site/customer names -> "the first installation
  (38 mm rope)" (tasks 13, 15, 18, date 29-31 Mar), "sensors selected" -> "sensing elements settled" (task 8),
  task 25 dependency names -> "the project lead", task 24 "chosen rope" -> "a rope the trainer picks".
- History section 4 ("could not establish") not carried.

## Checks
- 11 --check ok (10 + build_plan); SWS pytest 215 passed, 2 skipped, 1 known failure (test_sws_p52, no yaml).
- Edge headless via local http.server: 0 console lines from the page, light and dark; 49 tasks, 129 rows, 43
  rulings, 26 open rendered; links 10 relative, all exist; 375 px and 1366 px, all open: no horizontal overflow.
  Print (A4, all opened by beforeprint): 18 pages.
- Scans: scan_tree new files except plan.json 0; plan.json 65 whole-word hits, all inside `lead` (plan.json with
  leads blanked = 0; leads alone = 65; group wordings alone = 0). idscan 67866d8..HEAD 13 (entries 9, 10, person),
  all in plan.json: added lines of everything else + commit message scan 0.
- A safety check refused one `rm -f $H/*` in my scratch folder (unneeded; I used a new folder). Nothing deleted.

— Staysail

## Falsifier pass (one fresh reader, files only) and fixes — tip 1878990
- Verdict PASS with fixes; counts exact; ten figures traced identical; no name or site leak; leads first names only.
- Fixed: request 2 row back to the history ("assigned to the head design 19 Nov"); "stage 4" kept; "worst summer"
  (not "day"); "on record" (not "as ruled") for lm 19.1 mm; "Releases of the pages" (no added count); backup ruling
  wording; terms line (LD, LMA, B_rope, Br/Bz, lm, Hcj, knee, hard/easy wire, Hall/TMR/GMR/AMR) and basis meaning
  (blank = counts, standards readings, review answers); filing of review rounds/requests under Specification said;
  how-to adds `updated`, first date = next controlling date, `period`, the check command, ids 21-100, release path;
  footer title with a path removed.
- Not fixed (source wording of the task import or judgement): task 108 "27 mm" / task 102 "0.33 mT"; "issue 4/5" in
  tasks vs "Request" in the record; "Not started" tasks with progress > 0 (2, 9, 12, 31, 33); "was due 22 Nov" vs open
  item "since 20 Nov"; remaining slang ("folded in", "findings latch", "Peer read", "75 input fields, 11 knowledge
  bases"); review rounds not filed by subject.
- After fixes: 11 --check ok; pytest 215/2 skipped/1 known; Edge light+dark 0 console, 375/1366 px no overflow;
  scans as before (plan.json 65 / idscan 13, all in `lead`; everything else 0). Local test servers stopped.

## Release (as U121 did it; Kai's)
Export increment 67866d8-range of local main (after merge) via export-v3 tools (replay/rename/fast-import, FF of
GitHub main), snapshot docs/sws/ + sws/ into publish/SWS, link proof incl. plan.html, then the three pushes:
git -C C:/Users/stian/export-v3/export push https://github.com/fjordbit/max.git main:main;
git -C C:/Users/stian/publish/SWS push origin main; git -C C:/Users/stian/publish/SWS push maxflow main.
Needs attention: the link/visible-text tools see plan.html as a shell (content comes from JSON), so prove its text
on the rendered DOM. A colleague's web-editor commit on fjordbit/max breaks the fast-forward-only export unless it
is brought back into local main first; an edit made straight in the Pages repo is overwritten by the next snapshot.
— Staysail
