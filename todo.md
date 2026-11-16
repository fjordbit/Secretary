# Open items

Standing list. The daily files in `log/` record what happened; this is what has
not happened yet. Reviewed with the daily entry.

Last reviewed: 2026-11-05 (pruned: U13/U14/U15 merged, ADR 0006 written, the spec
docx is out of max/sws/, September's in-person window is long closed).

---

## Decisions waiting on Stian

- [x] **Rule 10 — Stian yes, 7 Nov.** Applied with the Grok patch after U23 merges. (As proposed in
      `docs/design/process-rule-design-conformance.md`? Grok applied it in the clone; the page
      says Stian applies it. Yes → it rides with the Grok patch below.
- [x] U27 Fairlead points 1–3 + rule 10 merged to main 8d7ac15 (7 Nov).
- [x] **GitHub: "rewrite" or "accept"?** v2 cleaned history ready in D:/git/max-export-v2.git
      (project code found on GitHub since 4 Nov). rewrite = Stian force-pushes once, managers
      re-clone. accept = Kai fast-forwards main (e73673b). Commands in log 7 Nov.
- [ ] Invalid MAX_RULE_STUBS: stop the run in preflight (new §6 row) or keep driver refusal? (Bollard)

- [x] **Review policy on the chart** — Stian yes, 6 Nov. The severity → outcome
      table (major → revise or needs_human) moves from `review_policy.yaml` onto the
      ladder block, per flow; the floor (critical → stop) stays a rule. Agree → Tiller
      design round + small build.
- [x] **Four `params.model` fields** before the two new flows run live. Kai's proposed
      table 7 Nov (after Stian: Codex writes): architect + judge = Fable (claude-fable-5-1),
      writer + improver = Codex (CLI default model; writer block provider → codex). **Yes, Stian
      7 Nov.** Grok as an option once its provider exists; per-login overrides via U24.
- [x] **API key expiring 13 Nov** (mail): verify in console.anthropic.com, not via the link.
      Nothing on this machine uses it. New key when API mode is tried.
- [x] Yoke + magnet: direct unit (Stian, 7 Nov). → U25 below.
- [ ] **Owner's calls left by U22:** placeholder minting (Boundary, after the AI
      policy); reviewer sees the sources (chart edge); chart 0.2 (D4).
- [x] ffmpeg installed 5 Nov; every good run gets an mp4.

## SWS after U31 (8 Nov)

- [x] **Grok pack upload** — C:/Users/stian/grok_pack_2026-11-08.zip (387 files, 24.3 MB, 0 identifier hits).
      Stian checks it, decides on site pointers + company name, uploads himself. Brief inside:
      docs/paper/grok_brief_2026-11-08.md.
- [ ] **rev128 → live Word master** (sws/spec/…rev128_2026-11-08.docx is a python-docx edit of rev127; Stian's
      document is the master). Row 24 (18 strands wording) waits for the rope maker.
- [ ] EN 12927 §14: B_rope or B_wire (Stian reads). Acceptance rule 40 mm one wire / 52 mm two wires vs
      the spec's "< 0.5 %" (52 mm pair = 0.62–0.64 % on the model): how the spec words it.
- [x] Go for 3D runs R1–R8 (≈8.6 h solve; main-text set ≈1.5 h; run order shared Ø60 / 52 mm / N52 / +45 °C).
- [ ] N52 supplier Hcj sheet (via the head designer).
- [x] **Review round run 8 Nov, nine answers + synthesis on main.** Next round after fixes (tier-0 judge contract text, Codex gets code, DeepSeek preamble + literature brief).
- [x] **Rotate the Claude API key** (pasted in chat 8 Nov; set the new one via the env-var dialog).
- [x] **Review round (U33 on main):** Stian: Cursor login (`agent login`), pin model names; set ANTHROPIC_API_KEY
      (user env var); say go → `python tools/review_round.py` (dry-run first). Fable every round? MAx review
      chart = U24's reviewer half, later.
- [ ] rewrite_names.py: add rules for site names, first names, user path (Davit's second pass was pack-only).

## Confirm or drop — asked since 11 Sep, never reported back

- [x] Spare-parts / after-sales conversation (questions at
      `Prosjekter/systems-integration/01_Spare_Parts_API_Questions.md`). Now also a
      candidate flow scenario, so the input matters again.
- [x] Mail to Ramin, `inbox/drafts/2026-09-09_ramin_platform_questions.md` — sent?
- [x] AI policy review — document never arrived. Still gates placeholder minting (ADR 0004).
- [ ] Strategy paper rev5 (section 5 rewording, placeholders, canonical HTML variant,
      customer name in the example prompt). Nothing since 9 Sep.

## MAx — next

- [x] U23 on_major merged to main ce08340 (7 Nov morning). Live run 3 can go after U27.
- [x] H(ii) softer (Stian, 7 Nov): major/critical count regardless of the flag; minor waived
      on a non-blocking review. Cleat building it on the branch.
- [ ] **U24**: level
      parameter on the document flow (paper / plain). Goal: both run by Monday 9 Nov.

- [ ] **Scenarios to run the flow on, for output we need** (Stian, 5 Nov):
      1. SWS scientific paper — Fable lays out, Codex writes; iterations until all
         models are satisfied; output format (HTML / LaTeX) a setting on the writer.
         Inputs exist: U7/U8/U16/U17/U19 reports, draft abstract in U16.md. First run.
      2. Documentation at three levels — full docs / paper / abstracts only — one flow,
         level as a parameter; the "slider" documentation page. Same flow as 1.
      3. Spare-parts and warranty API — design from inputs plus noisy text; needs the
         spare-parts conversation above.
      4. Bilge arms — part of Stian's agentic plan; models to be made ready first.
      5. Same document-creator flow for MAx-Flow — later, not ready.
      6. PLC cases (Stian, 7 Nov): document PLC source code, evaluate PLC code, TIA
         Openness items. Later; each case is also test data for MAx.
- [ ] **Grok as suggestioneer** (approved, 7 Nov; Stian's default in that role): xAI via the openai provider + base URL,
      `XAI_API_KEY`; a suggestion block in the flow. After Monday.
- [ ] **Studio side menu "Agents"** (Stian, 7 Nov): one default model per agent type —
      Architect, Coder, Reviewer, Judge, Wild card (Grok, its modes) — set from the menu during
      the running-in, per login profile. Builds on U24's layering.
- [x] U26 Studio auto-arrange merged to main 40b0a1f (7 Nov).
- [ ] U26 follow-ups (Stian, small): per-level saved position OK? shared track stretches?
      flat 0.1 charts routed too? A saved position can still cross a block: fix before E8 drag. Today: columns by longest path, one
      barycentre pass, ports in declaration order, feedback lines drawn straight back.
      Proposed small unit: layer sweeps, port order by partner, long and feedback
      lines routed round the columns.
- [ ] **Live run 3** once the review policy is decided; with mp4.
- [x] Henrik's GitHub invite (pending); Ramin's rope data (#1);
      MAX_CLAUDE_CLI_MODEL machine-wide; GitHub Actions on the 4 Nov export unchecked.
- [ ] **Mail to Syncrolift: prepaid API accounts** (Anthropic + OpenAI). Send after the
      demo on the visit; draft to `inbox/drafts/` before.
- [ ] **One home for the repos** (fjordbit/max, fjordbit/SWS, MAx-Flow/SWS-Documentation,
      D:/git/prosjekter.git, publish/SWS) → MAx-Flow org, one scan → push. Not urgent.
- [ ] **Own local agent / learned Boundary** (Stian, 7 Nov): the deterministic checks stay
      local and programmatic; later a local model (maybe open-source, maybe not AI) trained on
      logged faults from released runs becomes a MAx helper and organiser. Precondition: keep
      every released run's `runs/<id>/log.jsonl` + the review findings as training data.
      Idea only; no unit.
- [ ] **Hosting** (later): MAx on the tower, reached from the phone. No plan yet.

## SWS

- [x] U25 P52 prototype built 7 Nov (Capstan, 55844ed). Mail to Henrik drafted
      (inbox/drafts/2026-11-07_henrik_p52.md). Merge onto the SWS line after Stian's four calls.
- [ ] **P52 calls (Stian):** 20.5 mm magnet? no steel shoulder? B_rope vs B_wire? notch purpose?
- [ ] P52 not yet done: hard wire −40 °C, rope off centre, fault with split gap, second mesh
      level, 40 mm rope. One more session once the head designer answers. Deadline ≈ 21 Nov. Kai drafts the mail to the head designer after.

- [ ] **Paper through the flow** = scenario 1 above.
- [ ] Spec: 5 interactive charts in the live Claude Doc (rev 127) dropped by the docx export.
- [ ] 4 broken references in `sws/data/sws_data_sources.md` (URLs in
      C:/Users/stian/agent-notes/u07-work.md). Stian or the spec owner picks replacements.
- [ ] Henrik's three drafts and Ramin's rope draft stay in `inbox/drafts/` until answers
      come; may need resending (Stian, 5 Nov).

## Logging → Maintenance

Notes at `Prosjekter/logging-maintenance/`. Settle in this order; the first question
governs the rest.

- [ ] Fastest event we must not miss (10 Hz may miss a snatch load).
- [ ] How data reaches SQL today (WinCC Tag Logging or other).
- [ ] Tags per hoist, PowerTag / archive-tag licences held.
- [ ] Retention: months or decades.
- [ ] Measure the filter ratio on one real docking at 100 Hz.
- [ ] EG Maintenance ingestion interface (likely EG MainManager); address-standardisation
      document; overload data in the PLCs; "Tosibox on steroids" (likely IXON Cloud).

## Delivery milestones — Stian's own plan (proposed 1 Nov, status 5 Nov)

| # | Deliverable | Status |
|---|---|---|
| M1 | Studio demo build (U13 + U14 merged, one launch command) | Done, except chart 0.2 undecided and no demo script |
| M2 | Demo visit + API mail | Open, week of 16 Nov |
| M3 | Test model v0 (U15, ADR 0009) | Done |
| M4 | Model drives Studio | Open, Fri 4 Dec |
| M5 | A real `max run` animates in Studio | Done 4 Nov (live runs 1 and 2) |
| M6 | SWS design frozen (U8 done, U9 hardware, spec frozen) | Open, Fri 18 Dec |
| M7 | Reference lift in the twin | January |
| M8 | Logging → maintenance | January |

## Later — raised, not scheduled

- [ ] Mail and calendar access for Kai; the 08:00 entry needs a scheduled job.
- [ ] Revision viewer (`Prosjekter/agentic/06_Revision_Tracking_Spec.md`); steel price feed.

## Decided, so it stops being asked

- Drafts and notes are in English.

## SWS after the 7 Nov audit (Sextant.md)
- [ ] Stian: reference-defect headline — keep 0.62 % "hidden pair" or quote the spec's single-wire margin 9.6 / 5.7?
- [ ] Stian: fix the spec leftovers in the live doc (Sextant.md §B; l.474 "segmented magnet blocks" first)
- [ ] Stian: P40 inheritances — sensor R 36.5, yoke notch: keep, or back to spec? Say once that P40 is not the spec head
- [x] U25b lands: one-piece, −40/+45, N52 and N48SH side by side; then re-do Henrik draft
- [ ] Later unit: the reference defect per spec (two inner wires, EN spacing) solved in 3D; +45 °C rerun of U16/U19 numbers
- [ ] Legacy t_shoe=8 modules: retire or mark (no 3D result rests on them)

## SWS after Stian's evening reply (7 Nov)
- [x] U29 landed on main ff20112 (7 Nov 20:30). Next: identifier scan + masked Grok bundle after Stian's calls; GitHub export after the rewrite/accept call.
- Stian's calls still open: grade (leaning N52), thickness basis, B_rope vs B_wire, headline fault; apply redline + 15 register rows.
- After U29: Stian runs external Grok review (masking!); then paper draft with MAx input fields (U24); then management version.
- Henrik draft rewrite with one-piece numbers (after U29 lands).

## SWS after U36 (8 Nov, night)
- [ ] Stian: storage / transport maximum (°C) → rev130 "+[owner value]" lines (l.233, 367, 428, 429) and a U36 addendum
- [ ] Stian: +50 °C operating vs the 45 °C magnet ruling — both stand, or +50 replaces 45
- [ ] Stian: rev128/129/130 into the Word master
- [ ] Stian: register l.331/l.332 (+80 reference, method statement) keep / reword / retire
- [ ] Stian: 52 mm rope wire diameters and inner construction from the rope maker (2.2 mm wires → pair 0.48 %)
- [ ] Stian: build R5 (Ø48 head, 40 mm stranded rope, new 3D model) or not
- [x] Kai: rotate the API key after the next review round; next round runs with the key loaded in-process

- [ ] Later: SWS pages on www.max-flow.no/sws behind Cloudflare Access (26 Oct hosting decision); public would need the mask pass first (Stian, 9 Nov 03:5x)

## MAx after U42 (9 Nov)
- [ ] Chart gap found by the U42 judge run: in max-architect-writer-judge the judge and reviewer never receive the
      architect's brief; `max run` cannot take ready-made architect/writer output. Small MAx unit? (Thwart, 9 Nov)
- [ ] U45 follow-ups (Bitt, 9 Nov): (1) `max run --seed <block>.<port>=<file.json>` so a run can start from a ready-made
      architect/writer answer (U42 needed an outside harness) — build? (2) severity of the judge's "no brief received"
      finding: fixed minor, or judge's call? Kai recommends: a missing brief is a wiring fault → stop in preflight/
      flowcheck, not a severity. (3) pre-existing: test_review_round expects an `xai` backend (fails on main).
- [ ] Landing-page fix bundle (Stian reading, 9 Nov evening): "(see What is open)" → link to the heading; more notes
      as they come; then one fix unit + export (incl. U45) + Pages refresh.
- [ ] U46 follow-ups (Thimble, 9 Nov): (1) ~~landing~~ decided: dense stays (Stian, 9 Nov 19:4x); (2) the owner's late
      storage statement (8 Nov evening) into register l.361 so pages can link it — the judge flagged the missing
      source twice; (3) `max run --seed` (same as U45 item 1).
- [x] Publish root docs/index.html (publish/SWS) names only "SWS report"; add the easy read there, or rename the
      link, next snapshot (Cringle, 9 Nov).

## SWS after U48 (9 Nov, midnight)
- [x] Stian: B_rope or B_wire (clause map: Annex B informative; does not say local / metallic area / nominal area)
- [ ] Stian: register l.348 says both "not on file" and "on file 9 Nov"; l.192 value column ("inner", "< 0.5 % LMA")
      vs 14.3.5.2's wording — reword in a small unit?
- [ ] Ch.14 requirements not in the register: 3-year flux check (14.2.1), ≥ 1 sample/mm (14.2.3), max 5 m/s (14.3.3),
      no testing near end fixings (14.1). Rows in the next spec unit? (map: max-private/standards/EN12927-2019_clause_map.md)
- [x] River analogy replaced by Stian's tyre-under-water picture (U50, 10 Nov); was: keep or change. His own (9 Nov, midnight): smoke blown into a
      fox's den, showing at the other holes — "equally good and would require no link"; he still thinks we can do
      better. The two outside links are optional; drop them if he says so.

## SWS after U50 (10 Nov)
- [x] Stian reads the pages as pushed 10 Nov 03:0x (both in plain text; easy read in four parts with figures + video)
- [x] (done, U52) Short page still reads as a record (cold reader): status letters unexplained, "register l.NNN, D" in every
      sentence, file names in captions/footers, "management chooses" × 7. Same treatment as the easy read — one unit?
      (It is the dense page Stian likes; his call how far.)
- [ ] Easy read leftovers (cold reader): "(options note l.48)" style cites in text; glossary defines B_rope / B_wire /
      Hcj but the body never uses them; "three heads" vs "the 52 mm head is the shared head"; five unclear sentences
      (list in log/2026-11-10.md source: cold-reader hand-back)
- [ ] Standing: cold-reader check before every page push (memory pages-about-the-task-not-stian)
- [x] (done, U54) Easy read, next pass (Stian, 10 Nov ~02:00): same content as the technical pages, short and light, for a reader
      with little or no knowledge; process rules not forced on it beyond safety, sanity, correctness. Proposed unit:
      rewrite in that voice, links only where they help, correctness checked against the short page as a whole
      (falsifier + cold reader) instead of an anchor per sentence; test for per-sentence links relaxed. His go first.
- [ ] Register row for "models not refined further until the supplier's figures are in" (on both pages since 10 Nov
      on his word; ruling of 8 Nov) — next spec unit

## Tomorrow (Stian, 10 Nov ~02:3x)
- [x] **HW design: the card itself, the sensors, PCB parts and all.** The SWS pages stay as pushed tonight until the
      rest of the data is in (supplier figures, wire sizes, the reading of the standard).

## SWS after 10 Nov evening
- [x] B_rope / B_wire: **B_rope, with B_wire beside it and the explanation** (Stian, 10 Nov). Closes the open lines above.
- [ ] Next spec unit: register l.191 / l.333 + pages from "pending" to the B_rope reading; with the rows already
      waiting (supplier-first, storage statement, ch.14 rows).
- [ ] Stian: magnet thickness at the minimum (1.92 T worst case) or mid-window between lm_min and lm_max? Nothing
      selected yet.
- [ ] Nomenclature: LD + LMA (EN 12927) with "LF" named once as the ASTM / literature term — or keep LF? Our text
      uses LF 24 x, LD 0.
- [ ] HW: head designer chose a multiplexed ADC (ADS114S08 / ADS124S08 as Kai reads his typed numbers) — confirm part
      number and count per half with him; spec §7 still recommends 3 × ADS131M08; check per-channel sample rate
      against 1 sample/mm at 15 m/min (Stian pasted his message 10 Nov).

## HW / SW after 10 Nov night (pages local only, main 4a50a29)
- [x] Stian reads hardware.html + software.html locally; says how the head designer's case is attributed
- [x] Go to push both pages (new export needed; U59's held export is the older page)
- [ ] Spec §7 "internal reference only" (ADS131M08) is contradicted by the datasheet → Word master
- [ ] Worked example two chips vs the spec's three; 24 channels need 1 Mbit/s
- [ ] Is 1 ms between halves tight enough for the neighbour pairs across the split?
- [ ] Reader's remaining reasons: case B datasheet check, M08 datasheet noise, aliasing for the simultaneous cases,
      definition of "after processing" in the 0.10 mT limit — one more round, or to the expert as is
- [ ] Old content on GitHub / Pages: owner's first name in older reports (scan_tree 660 / 397); customer-name hit in a
      U13 image — keep or clean
- [x] Rotate the Anthropic API key (rejected 10 Nov: not scoped to a workspace)
- [ ] The outside electronics expert: who, when, what he gets (the two pages + the rounds folder)

## Procedures and life cycle (Stian, 12 Nov)
- [x] U70 merged local 5defd84 (not on GitHub; Stian checks first): seventh page, placeholders (FMECA, prototype test, FAT, HAT, SAT, installation, recalibration) + the
      data list for the 40 mm prototype test. Then the runs in order — sensor run first.
- [ ] **Wed 18 – Fri 20 Nov (Stian: "I think"): test, 40 mm rope, first prototype.** Rig, who records — not known to Kai.
- [ ] Recalibration: look at it with the sensor run (spec §8 is the original text).
- [x] Sensor (12 Nov): U71 merged; U72 (literature) + U73 (model round folded in) on branches, wait for go.
      Finding: no TMR bridge is specified at the axial background; makers use Hall or coils; all three models
      chose Hall; the old prototype's TMR2185 / TMR2584 are specified to ±20 mT. → Henrik / the expert.
- [ ] Stian: sensor page of its own? out-of-plane mounting allowed? is 1 mW per sensor a limit? 2× rule = half span?
- [ ] Spec Word master: §7 l.341 "AMR … wider range" is wrong (sheets: ±0.5–1 mT).

## Status 16 Nov (overrides the 12 Nov section above where they differ)
- [x] U70–U74 on GitHub 12 Nov: fjordbit/max 71288f8, Pages f51035e (eight pages; sensor page is its own page).
- [x] U76 running (16 Nov): chapter "What the sensor measures" on the sensor page + the maintenance statement
      into the register. Merge waits for Stian's go.
- [x] **Prototype test Wed 18 – Fri 20 Nov: test procedure / rig sheet NOT started** (was due Tue 17 Nov).
- [ ] Maintenance (Stian, 16 Nov): head unshielded for hours, perhaps a day → temperature warning near the
      demagnetisation temperature; stainless shield against sun. Record: "never in direct sun" / ≤ 45 °C fully
      covered; sun study unshielded light grey 61 °C; no warning in the spec. Threshold and shield: not decided.
- [ ] Runs not started: FMECA, FAT, HAT / SAT, installation, recalibration.
- [ ] Draft to the head designer (prototype sensor parts, inbox/drafts/2026-11-12) — sent?
- [ ] Placement of the sensor: discussed on site this week (Stian).
- [ ] This week also: demo visit + API mail (no demo script, mail not drafted); P52 deadline ≈ 21 Nov.


## Review 16 Nov evening — closed by fact (20 lines ticked above)
- GitHub history: the grafted fast-forward export has been the method since 9 Nov (= "accept").
- API key: variable removed 16 Nov; ONE item left → delete the old key in the console (pasted in chat 8 Nov);
  a new key, when wanted, goes in max-private/anthropic_key.txt (workspace-scoped), never in chat.
- [x] Delete the old API key in console.anthropic.com (Stian) — done 16 Nov.
- Windows is the default boot; TeamViewer live and tested (Stian, 16 Nov). Open: auto-start of Kai at boot.
- [ ] Stian's fonts look unclear after the update / boot change (he looks into it).

## Stian's answers 16 Nov evening
- Closed: Grok pack (removed; Grok is tested through the rounds), mail to Ramin (done), spare-parts conversation
  (happened), AI policy review (dropped for now).
- [x] **Key test today before Stian leaves:** (done 16 Nov, 3 of 3 + synthesis) Fable 5.2 on the API key + Grok + Sol. Prepared:
      C:/Users/stian/key_test_2026-11-16/ (models.yaml, run_with_key.sh); dry run on the login 3 of 3 ok. WAITS for
      the new key in max-private/anthropic_key.txt (workspace-scoped).
- [ ] **MAx-Flow: the spare-parts / warranty API — the first coding task.** Stian has a list of API commands from
      the conversation; get the list from him, then brief it (scenario 3 in the MAx list above).
- [ ] Draft to the head designer on the prototype sensor parts (12 Nov): Stian thinks sent, not sure — open.
- [ ] Strategy paper rev5: Stian unsure — parked, ask again later.
- [ ] **TRAVEL EXPENSES + AI BILLS — this week, at least half a day. Wed 18 Nov morning or evening.** Stian
      gathers the data; a subagent sorts it. Start with the AI bills. KAI REMINDS HIM (Tue evening, Wed morning).
- Stian travels Tue 17 Nov. Demo visit / API mail: no new date given.
- [ ] **Claude Code sign-in ends between 17 and 20 Nov** (warning 16 Nov; auth status said 20 Nov 01:54). Stian runs
      `claude auth login` before he travels, or it can stop mid-week. Needs a browser (works over TeamViewer).
- [ ] U80 Vessel Library (reply draft + first design) and U81 Oracle integration (API map + estimate skeleton)
      running 16 Nov evening; results to Stian, he decides the next step (first coding task: Vessel Library).

- [ ] Next week: temperature range — Stian's thought of 16 Nov (back to −40…+80 °C, 20 cycles at 70 °C, drop N52-as-wanted; N52M/N52H as options). Discuss before any change; see log 16 Nov.

- [ ] When the 52 mm test rope is specified: design its fault list (same fault at 1 mm and 10 mm gap, depths, wire counts, metal loss over a length, positions) — Stian 16 Nov; rope to be ordered with the breakages built in.

- [ ] Next week: in-place sensor check — test loop per sensor on the new board (Stian 17 Nov: sized to one broken wire / under the 5 % rule) vs a reference rope length; decide whether it goes into the design input.
