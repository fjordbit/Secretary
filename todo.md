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
- [ ] **GitHub: "rewrite" or "accept"?** v2 cleaned history ready in D:/git/max-export-v2.git
      (project code found on GitHub since 4 Nov). rewrite = Stian force-pushes once, managers
      re-clone. accept = Kai fast-forwards main (e73673b). Commands in log 7 Nov.
- [ ] Invalid MAX_RULE_STUBS: stop the run in preflight (new §6 row) or keep driver refusal? (Bollard)

- [x] **Review policy on the chart** — Stian yes, 6 Nov. The severity → outcome
      table (major → revise or needs_human) moves from `review_policy.yaml` onto the
      ladder block, per flow; the floor (critical → stop) stays a rule. Agree → Tiller
      design round + small build.
- [ ] **Four `params.model` fields** before the two new flows run live. Kai's proposed
      table 7 Nov (after Stian: Codex writes): architect + judge = Fable (claude-fable-5-1),
      writer + improver = Codex (CLI default model; writer block provider → codex). **Yes, Stian
      7 Nov.** Grok as an option once its provider exists; per-login overrides via U24.
- [ ] **API key expiring 13 Nov** (mail): verify in console.anthropic.com, not via the link.
      Nothing on this machine uses it. New key when API mode is tried.
- [x] Yoke + magnet: direct unit (Stian, 7 Nov). → U25 below.
- [ ] **Owner's calls left by U22:** placeholder minting (Boundary, after the AI
      policy); reviewer sees the sources (chart edge); chart 0.2 (D4).
- [x] ffmpeg installed 5 Nov; every good run gets an mp4.

## Confirm or drop — asked since 11 Sep, never reported back

- [ ] Spare-parts / after-sales conversation (questions at
      `Prosjekter/systems-integration/01_Spare_Parts_API_Questions.md`). Now also a
      candidate flow scenario, so the input matters again.
- [ ] Mail to Ramin, `inbox/drafts/2026-09-09_ramin_platform_questions.md` — sent?
- [ ] AI policy review — document never arrived. Still gates placeholder minting (ADR 0004).
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
- [ ] Henrik's GitHub invite (pending); Ramin's rope data (#1);
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
- [ ] U25b lands: one-piece, −40/+45, N52 and N48SH side by side; then re-do Henrik draft
- [ ] Later unit: the reference defect per spec (two inner wires, EN spacing) solved in 3D; +45 °C rerun of U16/U19 numbers
- [ ] Legacy t_shoe=8 modules: retire or mark (no 3D result rests on them)
