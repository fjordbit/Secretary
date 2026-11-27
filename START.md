# State 27 Nov, 12:26 (Kai) — read this first; older blocks below

**Project main = D: = backup = bced1a9 (27 Nov 13:15: rerun rounds, two sides, steel study, prototype analyses, update note, drawings, HMI round, twin facts, twin page merged; not released). GitHub fjordbit/max = 83d83fd. Pages repos = c0d72f9** (pushed 27 Nov
00:42: Progress plan page without the rulings list, simulator joined work, review brief for Henrik). **The
live site did NOT update:** the deploy job on MAx-Flow/SWS-Documentation is refused, "account's billing is
currently locked" (enterprise trial expired; account deleted in 88 days from 27 Nov). Stian sent the note to
Ramin, who takes the billing over. When fixed: re-run the failed job, check the page, then post the issue to
Ramin about the plan page (go given, held).

**Nothing is running.** Builders back tonight: U140 (rulings out), U141 (MAx history, private:
inbox/2026-11-27_max_history/), U142 (board package draft: inbox/drafts/2026-11-27_board_package/, mailed to
Stian; out to the expert 1 Dec), U143 (release), U144 (steel near the SWS + tilt: branch u138-steel-nearby
4342a71, not merged; numbers not yet traced by Kai).

**Rulings 26-27 Nov:** large installation two sides, 102 winches, 6 stations, design for 2 SWS per rope;
rulings and his AI method are private (never on the site or in the project repo); first names allowed when
not negative, never next to a delay; every study ends with options and a marked proposal; backup history is
not rewritten; vessel library and Oracle integration have their own private repos (fjordbit/vessel-library,
fjordbit/oracle-integration, also D:/git/); RAM 4 x 64 GB OK to order, delivered to his home; one platform
for MAx (my advice, not ruled); the MAx / agentic section stays out of the SWS site until he rules on the 12
sensitive items.

**Waiting on Stian (in order):** 1 go to merge u137-two-sides (f7c72d4) and then u138-steel-nearby; 2 read
and send the board package (1 Dec); 3 forward the steel and movement mail to Henrik and the mechanical
colleague (add question 17: can the head be moved by hand); 4 detail read of the Henrik brief; 5 the 12
sensitive items of the MAx plan section; 6 two-factor on GitHub before 11 Dec; add Ramin to vessel-library
(password step); 7 Bitwarden plan (Teams bought; Families fits the household).
**Next for Kai after the merge go:** movement settings (shift toward the wall, sideways, tilt) and the steel
term in the twin; correct the 75 old-size lines (list in agent-notes/bunt.md); life cycle data run; fit the
twin to the measured data; DT first version target Wed 2 Dec (not forced).
**Browser:** Stian gave Kai a Chrome window on a second virtual desktop (27 Nov) so his work does not put it
to sleep. Mail: check the shared mailbox when awake; advertising to trash; Bitwarden mails kept.
Details: log/2026-11-26.md, log/2026-11-27.md.

---

# State 25 Nov, 20:00 (Kai) — end of the day in the desktop UI; next session in the terminal; read this first

**Posted 25 Nov evening:** the task to Henrik (platform steel geometry) is fjordbit/max issue #5, assigned hmssyncro. U135 (root box brief for Henrik, Opus) was started 20:15; Stian reads the draft after Kai's check.

**Nothing is running.** MERGED 26 Nov 02:50: u136-dt-joined (u132+u133+u134+u135+2 joined tests) is in main. Brief for Henrik: inbox/2026-11-25_reduction_brief/ (Stian reads in detail first; then page + link). Stian brings "the plan" on 26 Nov. Project main = D: = backup = 67866d8 (GitHub fjordbit/max dd24591, Pages f74c6a4, both
from 20 Nov). Nothing from 23–25 Nov is merged. All branches below are on D: and on `backup-<name>`.

| Branch | Tip | What |
|---|---|---|
| u124-prototype-data | 8c9b948 | Opus analysis of Henrik's recording |
| u128-prototype-data-codex | 181b99c | Codex (script loop) analysis |
| u130-prototype-data-fable | 9ed9bf5 | Fable analysis (API key; cost 82 USD) |
| u126-update-and-connection | 6c85176 | firmware update and connection note |
| u127-dt-facts | 591e1ab | DT facts page + 34 disagreements |
| u132-dt-full-scale | 4f341b5 | 51 ropes / 102 SWS / 204 halves, fault interface |
| u133-dt-temperature | dd874bc | two temperature sensors per half, four days |
| u134-rootbox-reduction | 71426a2 | dead band, lossless compression, send around movement |
| u116, u118, u120, u122 | e0dd47a, c1629d4, 4c7f039, eb0e658 | from 20 Nov; u122 now five answers |

**Next for Kai:** join u132 + u133 + u134 (all change `max/sws/line_beta/`; marked blocks, line ranges in the
log of 25 Nov). After that, on Stian's go: root box code in C++, main HMI design v3 and trainer HMI, fit the
twin to the measured data, second push round. Details and the full list: `log/2026-11-25.md`.

**Measured data:** three analyses agree (Grok not needed). Notes in `inbox/2026-11-25_prototype_data/`. Raw
data at `C:/Users/stian/sws-testdata/2026-11-20/`, never in a repository. Open: axial step size after the
strong magnet (3.2 vs 6 mV/V), 134 vs 136 ripple cycles; ask Henrik travel length, speed, rope construction.

**Rulings 20–25 Nov (not yet in the parts table):** state is "Concern", orange, latches; worst value drops when
a finding is dismissed; no time-window statistics; no "6 d" in the header; not "mock-up" but the HMI design of
the DT of the SWS; three screens (main, trainer, customer later); root box does simple reduction, all settable,
also in the twin; two temperature sensors per half; encoder available on 52 mm; any API-key run gets a cost limit;
outside models are not run unconfined on this machine.

**Late:** board (PCB) package for the outside expert (was due before 22 Nov) — ask Stian for a new date.

**Open questions, one at a time:** dead band only at rest (my proposal); MQTT or iba; Watch levels (hmi_round_2);
eight in `inbox/2026-11-25_update_design/update_and_connection.md`; nine in
`inbox/2026-11-25_dt_facts/dt_disagreements.md`; remove probe leftovers; ADC data sheets (he promised them).

# State 23 Nov, 16:10 (Kai) — Stian restarts; read this first

- Nothing is running except possibly a local web server for the replay page (127.0.0.1:8765, started 20 Nov);
  a restart ends it. Do NOT start a builder before Stian says he is back.
- NEXT: Stian brings lab data from the prototype (good low-noise ADC) and the ADC's data sheets. Plan for
  the digital twin (DT) of the SWS: inbox/2026-11-23_dt_plan.md. First step is to LOOK at the data, no
  fitting. Ask where the data file is. Data sheets are read, never copied into the project repo.
- Words: not "mock-up" any more; it is the HMI design for the DT of the SWS. Three screens: our HMI (never
  changed by training), a separate trainer HMI (pick rope, create fault), customer HMI later.
- Rulings 20-23 Nov: state is "Concern", shown in warning orange; findings latch (cleared only by rope
  replacement or finding removed with evidence); worst value drops when a finding is dismissed; no time-window
  statistics; "6 d" (six rope diameters) out of the overview header; two converters per half (reduce sensing
  elements rather than add a converter); names SWS / head / half / sensing element / channel / root box; rope
  position from end sensors, never an open question; bending cycles from the PLC via the shared server; model
  rounds name the newest model exactly.
- Released 20 Nov 12:13: GitHub fjordbit/max dd24591, Pages f74c6a4 (results page, parts table, two
  converters, rev131). Project main = D: = backup = b5478a7.
- Unmerged, on D: and backup-<name>, waiting for his go (second push round): u116-line-drawings e0dd47a
  (remove "Source: input.md" label, fix four text overlaps), u118-hmi-round c1629d4, u120-twin-page 4c7f039
  (+ link from results page), u122-rerun-rounds eb0e658 (sensing-element round now five answers: axial 3 Hall
  : 2 TMR, radial 5 mm 5 of 5). Owed with it: results page says "all three outside answers" (now five);
  8 README links in line_beta/figures/fig_b1-b4.html; parts-table rows (bending cycles from PLC; reduce
  sensing elements principle).
- LATE: board (PCB) package for the outside expert, needed before Sun 22 Nov, not started. Ask Stian for a
  new date. Also owed: test list for Henrik to inbox/drafts/.
- Open with Stian, one at a time: 8 decisions left in inbox/2026-11-20_hmi_round/round_2/hmi_round_2.md
  (next: watch levels or no Watch state); processing in root box or at the logger; stainless guard also in
  front of the sensing elements or polymer liner; root box per winch or per SWS; two-wire polled or
  four-wire RS-485; rerun Codex at highest level or leave; platform steel geometry for the 3D run.
- DT facts found 23 Nov: simulator is one head (all heads share one rope and fault list); signal is a formula
  with FEM-sized amplitudes; MAx zoom chart is demo data and its scale card says "~125 winches"
  (flow/examples-0.2-draft/make_sws_shiplift.py, SWS_TOTAL_EST=250); right: 3 stations x 17 winches, 102 SWS,
  204 halves. Firmware update: spec requires bootloader + remote update via root box; nothing on root box's
  own update, versioning or failed updates; not built.
- Detail: log/2026-11-20.md, log/2026-11-23.md; briefs U114-U123 in agent-notes/kai.md.

# State 20 Nov, 08:55 (Kai) — Stian restarts for an update; read this first

- Nothing is running. All repos clean and pushed (D: and the GitHub backups). Do NOT start a builder before
  Stian says he is back.
- NEXT (Stian's yes given 19 Nov): the board (PCB) package for the outside expert, as a draft in inbox/ for him
  to send; needed before Sun 22 Nov. Build it from u111 (element run 3), u113 (element round compared), the
  corrected groove numbers (large box) and the data line. Ask him one question first: what must be in it.
- Asked, not answered: yes to the four names for the report (SWS, head, element, channel; "sensor" alone not used).
- Project repo: main = D: = backup on fjordbit/SWS = 1735f4b. GitHub fjordbit/max 8beade9, Pages 67c6e1f
  (unchanged). Unmerged, all on D: and as backup-<name>, waiting for his look: u106-groove-plots d112319,
  u107-tradeoff-map b568641, u108-data-path 8c3218c, u109-transmitter-line aa1eae5, u110-line-beta d8a0cf4,
  u112-half-in-c a1ddd29 (on u110), u111-element-run 213e36c, u113-element-round 0384308 (on u111). Merge on his
  go only; then one publish with export, page rebuild and final check.
- Backup rule (19 Nov): D: is not a backup. Every push to D: also goes to fjordbit/SWS backup branches (never its
  main) and the secretary repo to fjordbit/Secretary (remote `backup`); agent-notes to branch `agent-notes` there.
- State of the design (calculated): groove depths from the large box (H52 4.98 / 4.25 / 3.53 mm for zero at
  13 / 16 / 19 mm); one thin board, radial element at 5 mm (all three outside models), axial element Hall or TMR
  open (hinges on the zero after a strong field: a prototype test); two converters per half; 250 values/s per
  channel; half in C gives the same frames as the Python byte for byte. Beta fails one proof: position from
  ripple 27 mm worst against 10 mm.
- Owed: 38 mm rope in the 40 mm head runs; Scotchcast 2123 at -40 °C; legend layout in the plot standard; design
  conclusion page (end plates non-magnetic stainless, groove proposal) as marked proposals on his go; fit the twin
  to the raw TMR data and the Ropesys measurement in the week of 23 Nov; multi-agent setup for Ramin.
- Tools: C compiler at the path in memory c-compiler-on-this-machine; never a bare `python` in Git Bash; clock
  times from `date`. Detail: log/2026-11-19.md, summary of the day at its end; briefs U105-U113 in agent-notes/kai.md.

# State 19 Nov, ~11:40 (Kai) — Stian restarts the machine; read this first

- Nothing is running. Do NOT start a builder before Stian says he is back after the restart.
- Then, in order: (1) ask again: run the prototype geometry from the drawing
  (inbox/2026-11-19_prototype_yoke_drawing.png; yoke 105 long, dia 102 / 88, groove 10 x 2 mm, dia 12 holes;
  the model's H40 is a different head) in the large box (r 2400 x z +-2400 mm, see g_large_box.md on
  u102-large-box) — he has not said yes yet; (2) plot standard for fjordbit/agentic (research type with hover +
  simple presentation type), on a branch, shown before any push; (3) today: set up the multi-agent system for
  Ramin together from fjordbit/agentic README + CLAUDE.md (check that Ramin has access to that repo).
- Posted today on fjordbit/max: issue #3 (prototype groove, head designer), #4 (magnet supplier data, head
  designer), #2 assigned to him, comment on #1 (rope data, Ramin). Mail to Stian 11:36: rope enquiry draft.
- Open question to Stian: longer loss (1 560 mm) and a 10 % loss in the test rope list before he sends it?
- Stian, today: problems 2 and 3 of the team run (temperature, N52 empty head) are handled by magnet type; grade
  by price; show N52 and N48SH together. Rope data from Ramin is needed before the "last" complete run.

# State 19 Nov, ~02:30 (Kai) — team run done; read this first after a restart

- Nothing is running. Team run (U101 A-F) and the large-box re-run (U102) are all back and logged in
  log/2026-11-19.md. Gathered note for Stian: inbox/2026-11-19_team_run_morning_note.md.
- Unmerged, all waiting for Stian's go: u95 5f5bbc5 -> u96 e84b603 -> u97 ab4fe6b -> u98 88c7a03 -> u100 c19d94c;
  u99-plot-layout ab5ee65; u101a cb19ba7, b 3f2589a, c 1d52b57, d 5aa981b, e ad85858, f c1ee951 (each from
  c19d94c); u102-large-box 1ded20a (from cb19ba7). Local main = D: = 062b8bd; GitHub and Pages unchanged.
  Nothing into the spec or pages before his go; then as a marked proposal. report.html rebuild at merge.
- Conclusion now (calculated): principle held (groove sets the zero; holds in 3D and with the split). H52 depths
  for the zero at 13 / 16 / 19 mm = 5.0 / 4.25 / 3.5 mm (old notes: 6.1 / 5.4 / 4.6, small model box); gain 3.8x;
  LMA null about 1.94-1.96 T at 1.06-1.15x magnet; no working point above ~2.0 T. New problems: steel within
  ~0.5 m and a second head change the reading by 1-8 % of metal; temperature changes the scale (-6..+11 % N48SH);
  N52 in a warm empty head demagnetises; zero must be adjustable; inner-wire local-fault margin about 1 at 2.0 T;
  TMR2584 offset temperature figure ambiguous. All 18 Nov groove notes carry small-box numbers; part F too.
- Owed: real-magnet steps (part F) in the large box; one-sided steel in 3D; grade-specific magnet temperature
  coefficients; second check of U102's falsifier fixes; plot layout simplification; PCB package Friday 20 Nov.
- Open questions to Stian (one at a time): prototype groove width and depth; was a rope inside when the head was
  split; gaussmeter at the rig; measured noise from the rig; "axial channels flat at a limit"; private Gmail
  address; what "any" means in the company rule.

# State 18 Nov, ~23:55 (Kai) — Stian signed off; read this first after a restart

- RUNNING: U100, the 52 mm head fine sweep (worktree C:/Users/stian/Prosjekter-u100, branch u100-h52-sweep, from
  88c7a03; brief "## U100" in agent-notes/kai.md; due ~02:00; told to give low / middle / high across a physical
  bracket of the rope wire's magnetic curve). If it died with the power: check the branch and the builder's note in
  agent-notes/, restart from the brief.
- NEXT, Stian's go given (23:50): when U100 is back, start the team run that tries to falsify the findings on all
  major design settings. Log everything in log/ as it happens.
- Unmerged chain, each on the one before: u95-axial-liftoff 5f5bbc5 -> u96-yoke-cutout e84b603 ->
  u97-groove-physics ab4fe6b -> u98-working-point 88c7a03 (-> u100); side branch u99-plot-layout ab5ee65 (from
  ab4fe6b). Local main = D: = 062b8bd; GitHub and Pages unchanged since the afternoon. No merge without Stian's go;
  nothing into the spec or pages before the team run and his go. report.html must be rebuilt at merge.
- Conclusion so far (calculated, not measured): thick yoke + outer groove all round at the sensors; groove depth
  sets where the standing axial field is zero; axial element there (13-19 mm out) = 4-6x LMA level, magnet drift
  nearly cancels; no effect on local faults (radial elements near the rope, unchanged). Axial element alone is not
  enough for LMA (rope diameter / fill look like loss; a level trace along a loss needs processing). Working point:
  LMA wants ~1.9-2.0 T, local faults higher; lean towards LMA (Stian's suggestion, Kai agrees; check single-wire
  margin). Uniformly thin yoke does not work.
- Outside models: C:/Users/stian/groove_round_2026-11-18/ (Grok, Codex; Sol's check in rounds/2026-11-18-step2).
- Figures of the day: inbox/2026-11-18_*.png and three interactive examples *.html.
- Plot layout: simplify (memory: plot-text-short-and-spread). PCB package for Stian's friend: Friday 20 Nov.
- Open questions to Stian (one at a time): prototype groove width and depth; "axial channels flat at a limit" on
  the top sheet; private Gmail address; gaussmeter at the rig; what "any" means in the company rule.

# State 18 Nov, ~16:15 (Kai)

- Released: board arrangement "not settled" (U91), LD and LMA as two measurements + discard rules + link to the rig
  sheet (U93), first long-loss calculation + two-part video (U92). Local main = D: = 062b8bd; GitHub fjordbit/max =
  8beade9; Pages (both remotes) = 67c6e1f. Live pages checked: sensor.html#s-board, #s-ldlma, rig sheet link on the
  start page, v2 video served; the first video is removed.
- Stian's order: LMA threads first, then the sensor part and the PCB package for his friend (a first package, about
  90 min for a builder; not started, waits for his go).
- Findings to carry: rope flux follows a long loss (-0.93 % per 1 % lost), axial TMR does not (small level, ends 7-9
  times larger; 1 % weaker magnets = about 3 % apparent LMA). LMA sensor search = a reading of the flux itself.
  1 200 mm case not run (model box). Company rule: discard at 10 % LMA ("any" not defined). ISO 4309 extract in inbox
  (PDF in InternationalStandards-Cranes-Ropes/, git-ignored, copyright). Rope data: certificate promised; work with
  low / middle / high cases.
- Spokes are not ruled out (Stian): objection is that the two sensors do not read the same spot.
- Owed in the project: two u16 figures with the old legend; no page links the redline file; the sentence Kai wrote in
  the s-ldlma note had no fresh check; later rewrite of the 37 spoke-dependent items; redline rows into the spec.
- Open questions to Stian (one at a time): PCB first package go; "axial channels flat at a limit" line on the top
  sheet; private Gmail address; gaussmeter at the rig; was a rope inside when the head split; half-rings truly
  radially magnetised; photo of the plate with part markings; what "any" means in the company rule.

# State 18 Nov, midday (read this first)

- FIRST POINT OF THE RECAP RUN (Stian, 18 Nov): the board arrangement. The spoke layout was never confirmed by him; his original design is one thin board across the rope with sensors mounted in different planes. Spokes = "not confirmed by the owner"; build nothing more on them.
- Running / just run: model round on the board arrangement, three models, two steps, blind: `C:\Users\stian\board_round_2026-11-18\`. After it: summary (writer + fresh checker), then a builder updates the documents on a branch; merge and push need Stian's go.
- Stian asked "update accordingly all": plan = mark the spoke layout as not confirmed where the documents say "chosen", correct "gives radial only", add the round and its summary, and list what depends on the board. A full redesign of dependent pages waits for his decision after he has read the result.
- Chrome extension connected. fjordbitdev mailbox shared; Kai sends only to Stian's own addresses (private Gmail address still not given). First mail sent 10:29.

# State 18 Nov, late morning (read this first; Stian restarts Kai to connect the Chrome extension)

- Nothing is running. All project work is pushed: local main = D: = 44a5b0e; GitHub fjordbit/max = 7f2b3f7; Pages (both remotes) = 36bc5cb.
- Pages site address: https://miniature-bassoon-zqw7owk.pages.github.io/sws/ (docs/sws/ is served as /sws/). github.com needs its own sign-in in the browser.
- After the restart: Stian connects "Claude in Chrome" (`/chrome`). First test: open housing.html#ho-halves on the Pages site and check that the note and its links are live. Use the extension only on the Pages site and the two repositories.
- New this morning (inbox, not in the project): `2026-11-18_radial_stack_52mm.png` + `_sources.md` (every layer between the 52 mm rope and sensors/magnets; gap budget), `2026-11-18_standoff_signal_52mm.png`, two side views. Numbers in the figure not checked by Kai against the sources.
- Findings to carry: two different splits of the 5 mm stand-off in the documents, no decision; the 4 mm gap at the magnets is 2.96 mm with a +4 % rope and about 0 with 2-3 mm movement; no allowance for grease, ice or a protruding wire; the Ø70 bore was withdrawn for a double-counted guard, not rejected. Old 40 mm head: net holding force only 94 N (577 pull vs 482 push), so it may spring open on the rig even if the 52 mm head would not.
- Stian, 18 Nov: keep the radial stack noted as its own point for the recap run (one agreed stack for the 52 mm head, allowance for grease, ice and the real rope diameter, cost per extra mm in signal and magnet).
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
