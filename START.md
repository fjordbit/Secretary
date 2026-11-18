# State 18 Nov, late morning (read this first; Stian restarts Kai to connect the Chrome extension)

- Nothing is running. All project work is pushed: local main = D: = 44a5b0e; GitHub fjordbit/max = 7f2b3f7; Pages (both remotes) = 36bc5cb.
- Pages site address: https://miniature-bassoon-zqw7owk.pages.github.io/sws/ (docs/sws/ is served as /sws/). github.com needs its own sign-in in the browser.
- After the restart: Stian connects "Claude in Chrome" (`/chrome`). First test: open housing.html#ho-halves on the Pages site and check that the note and its links are live. Use the extension only on the Pages site and the two repositories.
- New this morning (inbox, not in the project): `2026-11-18_radial_stack_52mm.png` + `_sources.md` (every layer between the 52 mm rope and sensors/magnets; gap budget), `2026-11-18_standoff_signal_52mm.png`, two side views. Numbers in the figure not checked by Kai against the sources.
- Findings to carry: two different splits of the 5 mm stand-off in the documents, no decision; the 4 mm gap at the magnets is 2.96 mm with a +4 % rope and about 0 with 2-3 mm movement; no allowance for grease, ice or a protruding wire; the Ø70 bore was withdrawn for a double-counted guard, not rejected. Old 40 mm head: net holding force only 94 N (577 pull vs 482 push), so it may spring open on the rig even if the 52 mm head would not.
- QUESTION NOT ANSWERED (asked three times): shall the radial stack be its own point in the recap run?
- Stian's plan: full run on all SWS documentation in MAx — recap, discussion, then knowledge pack + test set. Kai offered to write the plan for the recap run.
- Other open questions: gaussmeter at the rig?; was a rope inside when the head was seen to split?; half-rings truly radial or magnetised straight through?
- Reminder given this morning: travel expenses + AI bills (Stian runs his own agent for receipts).

# State 17 Nov, ~24:00 (read this first; Stian is at the rig site from 18 Nov)

- Released tonight: local main = D: = 44a5b0e (U89); GitHub fjordbit/max = 7f2b3f7; Pages (both remotes) = 36bc5cb. Live pages not viewed (login).
- New: boxed note `housing.html#ho-halves` "Do the halves come off the rope by themselves? Not known.", linked from the top of index and easy-read and from procedures; round folders `sws/housing/rounds/2026-11-17-release/` and `2026-11-17-halves-force/`; item 8 on the published top sheet.
- Owed in documents: spec rev130 l.218 and l.506 ("snap together", "attract when closed"); register row "rope-centring side force 0.4-0.8 kN/mm" (should be 0.12 kN/mm decentring); about 15 "net only" lines (list in log 17 Nov).
- Open questions to Stian: gaussmeter at the rig?; when the mechanical people saw the head split, was a rope inside?; how are the one-piece half-rings magnetised (truly radial or straight through)?
- Stian's plan for 18 Nov: a full run on all SWS documentation in MAx: recap (what is good, what is missing), discussion, then a knowledge pack + test set as the training piece. Kai offered to write the plan for the recap run.
- Later task noted: multiplexer scan time against vibration frequencies, with data from this week's runs.
- Reminder owed 18 Nov morning: travel expenses + AI bills (Stian runs his own agent for receipts).

# State 17 Nov, ~04:30 (read this first; the "before a reboot" block below is DONE)

- RELEASED: local main = D: = 1cc9661; GitHub fjordbit/max = e6e2c14; Pages (both remotes) = 7054acf. Adds U87: the
  model round on the test sheet (sws/procedures/rounds/2026-11-17-test-sheet/, summary.md, rig_top_page.md) and a
  link to the top page from the rig sheet and the procedures page. Live pages not viewed (login).
- Open with Stian: is a handheld gaussmeter at the rig (or the other certified sensor / an older module)? Reminders:
  expenses + AI bills, Wed 18 Nov morning or evening. Nothing running.

# State 17 Nov, ~03:15 — BEFORE A REBOOT (read this first)

- **Owed right after the reboot (Stian's go given 17 Nov ~03:10: "put it to github for me to read … then push"):**
  put the test round on GitHub so he can read on his phone: C:/Users/stian/test_round_2026-11-17/ (summary.md,
  rig_top_page.md, both briefs, step1_files, six answers) into the project repo as a round folder (mostly added,
  little rewritten), a link to the top page from the rig sheet / procedures page; builder on Opus on a branch →
  Kai check → merge to main + D: → export + snapshot + link proof (as "## U86" in agent-notes/kai.md) → Kai final
  check → push fjordbit/max + both Pages remotes. If any check fails: do not push, tell him.
- Gaussmeter question open ("we will see tomorrow"): he may have another certified sensor (with coils) and an
  older module to pick apart as sources for the standing field.
- Nothing was running when he rebooted (BIOS fan settings).

# State 17 Nov, 02:00 (read this first)

- RELEASED 17 Nov night (Stian's go): local main = D: = 84af27a; GitHub fjordbit/max = 1680bc1; Pages (fjordbit/SWS and
  MAx-Flow/SWS-Documentation) = 367549c. In it: U83 (second sensor round + data-sheet check, gap comparison and
  channel identity on the rig sheet), U85 (test-loop note early on the sensor page, rig sheet read from the runs,
  live/dead/not fitted column). Live pages not viewed (behind login).
- Print copy of the rig sheet for the test: inbox/2026-11-17_rig_sheet_print_v2.pdf (5 A4).
- NOT released, not merged: U84 test rope fault list (branch u84-test-rope, 4c8511c; too long, Kai check not done;
  finding: no source that a maker builds held broken wires in — ask the maker first). U80, U81 as below.
- For next week's talk: temperature range (−40…+80 °C thought), in-place test loop per sensor, test rope order.

# State 16 Nov late evening (read this first)

- Stian travels Tue 17 Nov; prototype test Wed 18 – Fri 20 Nov. Reach: TeamViewer; sleep after 2 h, Wake-on-LAN
  armed (wake from outside not proven); his wife is at home, has the password and can wake / start the machine.
- Sign-in renewed 16 Nov: Syncrolift account, Max 20x, valid to 16 Dec. API key (other, individual account) only in
  max-private/anthropic_key.txt, loaded per run.
- **Reminders owed:** Tue 17 evening and Wed 18 morning — travel expenses + AI bills, half a day Wed morning or
  evening; he gathers the data, a subagent sorts; start with the AI bills.
- Sensor round in two steps done 16 Nov: C:/Users/stian/sensor_round_2026-11-16/summary.md (not in the project
  repo; no data-sheet check yet; nothing selected).
- Back, not merged, waiting for Stian to read: U80 vessel library (branch u80-vessel-library, draft to the CPO in
  inbox/drafts), U81 Oracle integration (branch u81-oracle-integration, draft to the contract manager).
  U82 method files pushed to fjordbit/agentic (bc6c4cd).
- Next week: temperature range discussion (his note 16 Nov, log) — no design change before that.
- Detail: log/2026-11-16.md, todo.md.

# Kai — start here (state as of 10 Nov 2026 23:2x; U48–U57 live, U58–U61 local only)

> **State 16 Nov afternoon (newest, overrides everything below):** ALL PUSHED. Local main **5f415b6** (D: same);
> GitHub fjordbit/max **0f7b145**; both Pages remotes **1a58533**. Since 12 Nov: U76 chapter "What the sensor
> measures" on the sensor page + register rows for the maintenance statement (head unshielded for hours during
> maintenance; temperature warning wanted; no threshold on record); U77 rig sheet for the prototype test
> (docs/sws/rig_sheet.html, 4 A4, not on the menu; ROPE FIXED, HEAD MOVES; block "for the new sensor head: not
> possible on this rig") and the self-contained AI helper guide sws/procedures/prototype_test_ai_guide.md; print
> copy inbox/2026-11-16_rig_sheet_print.pdf. U78: the model round as its own repo, C:/Users/stian/model-round →
> private GitHub fjordbit/agentic (b1325d1), for Stian's manager (Stian gives him access). ANTHROPIC_API_KEY removed
> from the Windows user 16 Nov (it made new sessions start on the key; it belonged to "Stian's Individual Org", the
> login is the Syncrolift account, Max 20x); a new key goes in max-private/anthropic_key.txt, never in chat; two
> subscriptions = one login at a time, /login. Test Wed 18 – Fri 20 Nov; Stian may be out of contact. Open finding:
> break signal 0.39 mT (record) vs 1.27 / 2.69 mT (own 3D), unreconciled. Not started: FMECA, FAT, HAT/SAT,
> installation, recalibration; auto-start of Kai at boot (Stian, later). Log: log/2026-11-16.md.
>
> **State 12 Nov afternoon:** EIGHT pages on local main **a3a633a** (D: same):
> U70 procedures and life cycle, U71–U73 sensor run / literature sweep / blind model round, U74 the sensor page
> (docs/sws/sensor.html, six placements A–F, three suggested combinations, nothing selected). Stian gave the go to
> publish to GitHub "if all is checked properly": U75 (brief in kai.md "## U75") prepares the export on 025a0af and
> the snapshot on 2dc95f3. PUSHED 12 Nov: GitHub fjordbit/max 71288f8, both Pages remotes f51035e. Before that it was
> 025a0af / Pages 2dc95f3. Sensor finding: no magnetoresistive bridge is specified at the axial background; others
> use coils or Hall; old prototype carries TMR2185 + TMR2584 (data sheets in inbox/). Placement discussion: next
> week, on site, with Stian. Prototype test Wed 18 – Fri 20 Nov. Draft to the head designer in inbox/drafts/ (not
> known sent). Next runs, not started: test procedure / rig sheet (by Tue 17 Nov), FMECA, FAT, HAT/SAT,
> installation, recalibration. New pages are written easy-read first (memory). Open list: end of log/2026-11-12.md.
>
> **State 12 Nov morning:** SEVENTH page "Procedures and life cycle" (U70) LOCAL ONLY: local main
> 5defd84, D: same; GitHub still 025a0af, Pages 2dc95f3. Stian checks it, push to GitHub later on his go (export +
> snapshot + link proof on seven pages first). Prototype test, 40 mm rope: Wed 18 – Fri 20 Nov; data list is on the
> page. Next: the runs that fill the placeholders, sensor run first. Merge/push to D: needs his explicit go each time
> (refused by the permission check without it). Open list: log/2026-11-12.md.
>
> **State 11 Nov evening (newest, overrides what is below where they differ):** SIX pages LIVE: short, full,
> easy, hardware (price and complexity, one plot), software, housing and sealing (four cases, sealant round).
> Local main 8f97214 (D: same). GitHub fjordbit/max 025a0af; fjordbit/SWS and MAx-Flow/SWS-Documentation 2dc95f3.
> Rulings 11 Nov: never submerged (storm water); IP66/IP67 both; multiplexed case = "the in-house choice"; magnet
> grade/knee not finally set, not the deciding factor for sealing. Nothing running. Stian reads on paper tonight.
> Venvs: page builds/tests Prosjekter-u41/max/.venv (markdown); scan_tree, figures, review rounds
> Prosjekter-u05/max/.venv (yaml, matplotlib). Rounds: hw_round_2026-11-10/, sealant_round_2026-11-11/.
> Open list: end of log/2026-11-11.md.

Read in this order at the start of a session: this file, `todo.md`, the newest `log/*.md`, then
`C:/Users/stian/agent-notes/kai.md` (my briefs to builders; the last sections are the live units) and any new
builder notes in that folder (nautical names). Rules: `CLAUDE.md` here and the memory directory. Rule 10 in
`C:/Users/stian/Prosjekter-u05/max/CLAUDE.md` l.60–71 binds every brief and report.

## Where the work stands

- **Project repo** `C:/Users/stian/Prosjekter-u05/max`, branch main at **224704b** (U54 merged, 10 Nov 02:5x), pushed to
  the local origin (D:/git/prosjekter.git). GitHub fjordbit/max main is **9f3beec** = the rewritten export of local
  224704b (fast-forward, nothing deleted). Next increment: same method from the clone
  `C:/Users/stian/export-v3/export`, range from 224704b, graft on 9f3beec (brief pattern: kai.md "## U55", "## U53";
  unlink tool export-v3/tools/unlink8.py). Pages: publish/SWS at **ed8274c** (index.html = dense short page, landing;
  report.html = full report; easy.html = easy read), pushed to both remotes 10 Nov 03:0x.
- **Night of 9–10 Nov, after Stian read the live page** ("a biography of me", "a child writing about his father's
  work"): U50 attribution and dates out of the prose into hover titles; U52 status letters, line numbers, file
  names out of the short page's text; U54 easy read rewritten as an explanation (done / found / where we are / what
  is next, figures + video, his tyre-under-water analogy). The rule for readable pages and the cold-reader check:
  memory pages-about-the-task-not-stian. Stian: the pages stay as they are until the rest of the data is in.
  Read log/2026-11-10.md.
- **Next (Stian, for 10 Nov): HW design — the card itself, sensors, PCB parts.** Nothing prepared yet.
- **U56 + U57 live 10 Nov 20:2x:** local main db05b45; GitHub fjordbit/max 9d9a329; Pages 40f186a (working area
  + plot, B_rope reading, LD / LMA). Next increment: range from db05b45, graft on 9d9a329 (brief pattern kai.md
  "## U57"). Known leftovers in log 10 Nov 20:2x (full report still says "open" inside dated documents).
- **HW design started 10 Nov evening:** head designer chose a multiplexed ADC (log 10 Nov 20:1x); spec §7 is behind.
- **Hardware + software pages: LOCAL ONLY (D:), local main 4a50a29** (10 Nov 23:2x). docs/sws/hardware.html ("Hardware
  selection": requirements, four cases A–D, two model rounds, cabling and the root box, both converter families
  checked against their datasheets) and docs/sws/software.html ("Software analysis and design": converter read-out,
  half firmware and root box as pseudocode, frame, time base). Sources: sws/hw-selection/rounds/2026-11-10/,
  sws_link_and_readout.md, sws_link_budget.py, sws_mux_rate.py. GitHub is still 9d9a329, Pages 40f186a. NO push
  until Stian has read and said how the head designer's case is attributed. U59's held export (da77fe4 / c81b11f)
  is the older page — a new export from 9d9a329..4a50a29 is needed (pattern kai.md "## U59").
  Stian's leaning: simultaneous sampling, no multiplexer; the outside expert chooses. Morning list: log 10 Nov, end.
- **Nothing running.** Model rounds: C:/Users/stian/hw_round_2026-11-10/ (briefs, answers, syntheses); run with
  `env -u ANTHROPIC_API_KEY` (the key in the environment is rejected: not scoped to a workspace) from
  Prosjekter-u05/max with its own .venv: `tools/review_round.py --pack <empty dir> --brief … --models … --out …`.
- **A push was refused once by the session's permission check** (10 Nov ~02:2x) when Stian's last word was
  ambiguous; it went through after his explicit "push when done". Get an explicit go for each push round.
- **Identifier scan script** is now kept: `secretary/tools/idscan.py <repo> <range>` (added lines of the range;
  prints entry index and kind, never the name). In identifiers.yaml `match:` is a MODE ("whole-word", "exact
  case"), not a regex — the scratch versions before 10 Nov 22:3x searched for the mode text and so never tested
  10 of the 13 names; the builders' scans (private tools) did. Stricter check for outside bundles and for added
  lines: `Prosjekter-u05/max/.venv/Scripts/python.exe -I max-private/tools/scan_tree.py <dir>` (needs PyYAML).
  Whole-tree scan_tree on the export and publish repos gives 668 / 311 hits from OLD content (a mask-map personal
  name not in identifiers.yaml, e.g. in a 30 Oct snapshot file) — raised with Stian 10 Nov, not yet decided.
- **The standard:** BS EN 12927:2019 at C:/Users/stian/max-private/standards/BS-EN_12927-2019.pdf (copyright: never
  in a repo). Beside it: Kai's ch.14 extract and the **clause map** (EN12927-2019_clause_map.md, 9 Nov: every clause
  that bears on the instrument, corrections to the extract, ambiguities). **B_rope / B_wire: decided 10 Nov — B_rope, B_wire shown beside it** (log 10 Nov 19:1x). The map's finding for that question: Annex B is
  informative and does not say whether B is local, over the metallic area or over the nominal area.
- **Open from U48 (Stian):** register l.348 says both "not on file" and "on file 9 Nov"; l.192 value column ("inner",
  "< 0.5 % LMA") does not match 14.3.5.2's wording; the extract lacks 14.2.1 (3-year flux check), 14.2.3 (≥ 1
  sample/mm), 14.3.3 (max 5 m/s), 14.1 (exclusions) — candidates for requirement rows in the register.
- **Decided 9 Nov:** landing page = the dense short page (index.html); easy read = easy.html, third button; full
  report = report.html. Never merge "short" and "easy" again (memory three-sws-formats-easy-is-the-test).
- **Backup:** full file copy `D:\backup\2026-11-09_0223\` (2.5 GB; holds identifiers.yaml and the transcript with
  the pasted API key — local disk only). All repos committed and on D:/git.

## Rulings from 8 Nov evening not yet fully in the record

- Envelope −40 / +50 °C for service, storage and transport (49 °C record day → 50); the magnets set the
  transport limit; magnets procured to "zero irreversible loss after a +50 °C excursion in the open-half state";
  no further FE runs until the supplier's data for one-piece radial arcs is on file. Recorded as "U36 addendum" in
  kai.md; register l.361 and rev130 l.233/367/428/429 still say "owner to set" → next spec unit (small, docx route).
- Owner's reading accepted by me: "ambient at the sensor" is the editor's reading (marked so in rev130).

## Waiting on Stian (also in todo.md)

Mail to the head designer sent 8 Nov (draft in inbox/drafts/sent/). Create the GitHub issue from
`inbox/drafts/2026-11-08_github-issue_magnet-spec.md` (gh CLI not installed; his login); Word master rev128–130;
register l.331/332 keep or retire; 52 mm wire diameters from the rope maker; R5 (Ø48 3D) yes/no; rotate the
API key (pasted in chat 8 Nov) after the next review round; the "other hardware" tier-0 pass (Fable + GPT 5.6
Sol via tools/review_round.py with the key loaded in-process) once he names the sections.

## How I am started

A fresh session knows only the files: CLAUDE.md, the memory directory, and what I read from here. Resuming the
previous session (`claude -c` in this folder) also restores the conversation transcript. Either way, this file is
the state; keep it current at every handoff and delete the "running" lines once the units are closed.
