# MAx and the agentic way of working: history of work done (8 Sep – 27 Nov 2026)

Sources: secretary log/*.md (all days from 8 Sep), START.md, todo.md, inbox/2026-11-23_dt_plan.md, agent-notes
(kai.md and builders' notes named per row), memory files, read-only `git log` in Prosjekter-u05 (main) and
C:/Users/stian/model-round. Dates are log dates. "Main" = local main (D:); GitHub only where a push is named.
First date found: **8 Sep 2026** (intake for the agentic-workflow meeting). MAx itself first appears on this
machine **22 Oct 2026** (scaffold arrived; six weeks of work were done on another computer, not recorded here).
SWS work is in `inbox/2026-11-26_plan/sws_history.md`; where a topic is already there it is referred to by heading,
not repeated.

## 1. Completed work

### Strategy and other cases around MAx (before and beside the platform)

| Dates | What was done | Result | Source |
|---|---|---|---|
| 8 Sep | Intake for the agentic-workflow meeting read against the strategy paper | 10 points: gain sits in tenders that never convert; CATIA/VB layer answers assumptions item 1; systems mess is integration, not AI | log 8 Sep |
| 8 Sep | Price-prediction concept written up | per-part regression, five corrections; Prosjekter/agentic/04_Price_Prediction_Concept.md | log 8 Sep |
| 9 Sep | Prosjekter put under version control; D: bare repos as shared remote | initial commit bdf4066, 11 files; `D:\git\secretary.git`, `D:\git\prosjekter.git` | log 9 Sep |
| 9 Sep | Cloud wording for section 5 of the strategy paper | proposed, not applied (05_Section5_Cloud_Rewording.md) | log 9 Sep |
| 10–11 Sep | Logging → maintenance concept, three documents | 100 Hz vs 10 Hz gate; 10 open questions | log 10–11 Sep |
| 9 Sep | Portfolio split into five projects (01 vessel database, 02 agentic POC on bilge support arms, 03 platform and governance, 04 knowledge base, 05 controls / monitoring / virtual twin) | Prosjekter/agentic/00_Portfolio_Split_and_Project_Briefs.md | file dated 9 Sep; git bdf4066 |
| 16 Nov | Oracle ↔ maintenance-system link: API map + estimate (U81) | v1 123 operations, v2 197; shapes A ≈ 100–270 h, C ≈ 240–630 h, B ≈ 400–1,050 h | log 16 Nov; cathead notes |

### Bilge arms (project 02 of the strategy)

| Dates | What was done | Result | Source |
|---|---|---|---|
| 8 Sep | Bilge-arm sizing found already encoded (parameterised CATIA models driven by an existing VB layer) | assumptions item 1 to high confidence; work package 3 shrinks | log 8 Sep |
| 9 Sep | Project 02 brief: agentic POC from enquiry to budgetary offer for bilge support arms | baseline project, process steps P-8004 → P-2006, go/no-go at 9 months | 00_Portfolio_Split_and_Project_Briefs.md |
| 2 Nov | Owner: sales-offer flow (project 02 bilge arms) later; needs the manager | not started | log 2 Nov |
| 5–6 Nov | Bilge arms listed as flow scenario 4; Kai proposed it as MAx's first engineering case after the paper | "models to be made ready first"; no unit | log 5–6 Nov; todo.md |
| 7 Nov | Bilge-arms study used as a worked example of the review ladder (U23 design) | example chart only, no bilge-arm data | kai.md U23 brief; log 7 Nov |

### Ship database (vessel library, project 01 of the strategy)

| Dates | What was done | Result | Source |
|---|---|---|---|
| 9 Sep | Vessel database project brief | Prosjekter/agentic/01_Vessel_Database_Project_Brief.md | file dated 9 Sep |
| 16 Nov | Requirements mail (5 Oct) read; first design + draft review reply (U80, hatch) | small own web app proposed; phase 1 15–28 person-weeks, about 20 likely; first skeleton 1–2 weeks; commit d842901 on u80-vessel-library | log 16 Nov; hatch notes |
| 17–18 Nov | Longer reply drafted (lazarette) and mailed to the owner to forward | sent to the owner only, 18 Nov 10:29 | log 16 Nov (17 Nov entry), 18 Nov |

### MAx platform: foundation, engine and rules

| Dates | What was done | Result | Source |
|---|---|---|---|
| 22 Oct | MAx MVP scaffold placed at Prosjekter/max; old folders checked for duplicates | 2 duplicates moved to old/; QC fixed U9/U11 contradictions, 70c5583 | log 22 Oct |
| 23 Oct | Python and solvers installed (b363dcf); ADR 0004 recorded (code may go to Claude and OpenAI for now) | switch `methods_may_leave` on; no commit id logged for the ADR | log 23 Oct |
| 29 Oct | Platform status checked | Studio: four screens designed, AgentLive scripted only; max_core a skeleton | log 29 Oct |
| 29 Oct | U0 foundation (Provider interface, run log) | 1ad0d53, 44 tests; ADR 0005; merged to main | log 29 Oct |
| 2 Nov | U12 beta backend on subscription CLIs (Tether) | 6dce2a4; 192 passed, 4 live skipped; masked name restored; no reads outside the exchange dir | log 2 Nov |
| 2 Nov | U3 rule engine (Pawl) | 354e84c; 300 tests; FMECA and network inputs are DEMO fixtures | log 2 Nov |
| 2–3 Nov | U4 orchestrator (Capstan), then R3 rework and review severity | 429cac0 → b00471f → dba9c1e; 405 passed / 5 skipped; retry ladder, layered policy | log 2–3 Nov |
| 3 Nov | Merge of U12, U3, U4, U5 to main | main 91897db → f0ecb60 (fast-forward); 426 passed | log 3 Nov |
| 3 Nov | U18 "how to test" guide for the manager (Bight) | docs/TRY_IT.md, 3 tiers; fresh clone found 3 real problems; main eabaa39 | log 3 Nov |
| 3 Nov | U20 preflight and `max doctor` (Buoy) | Play gated on red/amber lamps; ADR 0010 accepted; main 0f312c9; 472 passed / 5 skipped | log 3 Nov |
| 3 Nov | Second Claude account for MAx runs | MAX_CLAUDE_CONFIG_DIR; `max doctor` all green on the company account | log 3 Nov |
| 3–4 Nov | U21 flow-driver design (Tiller, Fable architect), 8 rounds with Opus and Codex reviews | ADR 0011 accepted 4 Nov; decisions A–G recorded; check_u21 43 ok by round 8 | log 3–4 Nov |
| 4 Nov | CLI built-in tools gap found and closed (G) | `--tools ""`; main b852d18 + 9da0287; 474 passed / 5 skipped | log 4 Nov |
| 4 Nov | U22 flow driver, milestones 1–5 (Keelson); final check Bosun | the chart is what runs; WYSIWYG replay of run 1: 100 events resolve; merged main 4730e63, 546 passed / 5 skipped | log 4 Nov |
| 6–7 Nov | U23 review policy on the ladder (Cleat): one knob `on_major` | ADR 0012; review_policy.yaml deleted; merged main ce08340, 572 passed / 5 skipped | log 6–7 Nov |
| 7 Nov | U27 rule 10, front-door docs, stub checkers shown (Bollard) | merged main 8d7ac15; 580 passed / 5 skipped; CLAUDE.md 97 lines | log 7 Nov |
| 9 Nov | U45 the architect's brief reaches reviewer and judge (Bitt) | two data edges; merged main 860894c; 26 flow tests | log 9 Nov |

### Studio, the flow view and the chart (lines, zoom levels, views)

| Dates | What was done | Result | Source |
|---|---|---|---|
| 31 Oct | U13 Studio front end: module select + shared chart kernel (Weft) | adec874; 88 tests; twin lines all one thickness; chart ran off the right edge | log 31 Oct; u13 notes |
| 1 Nov | U13 follow-up: SWS shiplift chart, nested zoom to channels, chart 0.2 draft | 709e544 → d9b80bf → 43d62c2; 92 tests; 11 open points | log 1 Nov; u13 notes |
| 1 Nov | U14 shiplift 3D view (Sheave) | cb78b1c; 128 tests; 3D SWS red on sensor failure | log 1 Nov; u14 notes |
| 1 Nov | Mouse zoom (Ctrl+wheel/pinch) with semantic level steps | af5208b; 136 tests | log 1 Nov; u14 notes |
| 2 Nov | Semantic zoom on one canvas | f72a0ca; no text < 11 px; 19 channels readable at half level; 144 tests | log 2 Nov; u14 notes |
| 2 Nov | Merge of Studio branches (U10, U13, U14, U15) to main (Splice) | main 91897db; 165 tests; smoke test on :8790 | log 2 Nov |
| 3 Nov | U5 Studio live view (Sheet) | 7e178d0; 426 passed / 5 skipped; browser-test flake fixed | log 3 Nov |
| 4 Nov | Agent-zoom mock (Lens, scratch branch) | root map 11 blocks, 18 lines; A4 print fits but too small to read | log 4 Nov; inbox/2026-11-04_agent-zoom-mock/ |
| 4 Nov | Studio draws a run on the chart it ran; read-only agent zoom card (U22 milestone 4) | `/api/flows`; 529 passed / 5 skipped | log 4 Nov |
| 7 Nov | U26 Studio auto-arrange (Hawser) | lines through blocks 105 → 0 and 28 → 0; crossings 85 → 30 and 11 → 6; merged main 40b0a1f | log 7 Nov |

### Digital twin design work of the first weeks

| Dates | What was done | Result | Source |
|---|---|---|---|
| 23 Oct | Twin paused; to be designed inside MAx | dynamic model from control lab, PLC code in PLCSIM Advanced | log 23 Oct |
| 29–30 Oct | U10 twin and shared flow: design only (Keel) | twin/DESIGN.md, chart JSON schema + 3 examples, ADR 0007 (one chart for MAx and twin); 68 tests | log 29 Oct; u10 notes |
| 30 Oct | ADR 0008 "firm core, modules and rule packs" drafted | committed 04286c6 on u10-twin-design only, PROPOSED; never on main | log 29 Oct (30 Oct entries); u10 notes; git |
| 1 Nov | Shiplift layout for the twin example sorted out | L1 shiplift → L2 base stations → L3 winch → L4 2 SWS → L5 2 halves → L6 channels | log 1 Nov |
| 1 Nov | U15 in-house test model, first principles (Tackle) | daa269a; 113 tests; energy residual 0.001 %; ADR 0009 PROPOSED; merged 2 Nov | log 1–2 Nov |
| 1 Nov | Delivery milestones M1–M8 proposed | M1 Studio demo 13 Nov (confirmed 2 Nov); M4 model drives Studio 4 Dec; M7 reference lift January | log 1–2 Nov; todo.md |
| 23 Nov | DT documentation sweep and 8-step plan | zoom chart on demo data only; scale card "~125 winches" | inbox/2026-11-23_dt_plan.md; log 23 Nov |

Later twin work (simulator, replay page, full-scale plant, temperature, reduction): see sws_history.md,
"Digital twin and simulator" and "HMI / presentation design".

### The agentic way of working: builders, falsifiers, final check, notes channel

| Dates | What was done | Result | Source |
|---|---|---|---|
| 22 Oct | Check-before-create and QC subagent before any commit made hard rules | rules 4 and 7 in max/CLAUDE.md | log 22 Oct; memory |
| 25 Oct | Two runs of one unit in the same tree found | Kai's run dropped; "confirm who runs it" | log 25 Oct; memory |
| 29 Oct | Worktree per unit adopted (U0 in Prosjekter-u00) | branch per unit from main | log 29 Oct |
| 29 Oct | Notes channel for sessions | agent-notes/<session>.md; Kai writes kai.md; not in git | log 29 Oct |
| 29 Oct | Rule 8 "Read before asking" | 42dcd47 on main | log 29 Oct |
| 30 Oct | Rule 9: every agent names itself and signs | max/CLAUDE.md, kai.md, CLAUDE.local.md (4 trees) | log 29 Oct (30 Oct entries) |
| 2 Nov | Local dev board without unit numbers (Tally) | 127.0.0.1:8770, read-only | log 2 Nov |
| 3 Nov | Builders on Opus, Fable for the final check before release | first Fable final checks: Tern (U16), Lantern (U18), Sextant (U20) | log 3 Nov; memory |
| 3 Nov | Done-lines cite the design; final check verifies conformance | after U4 was found built as a fixed loop | log 3 Nov; memory |
| 7 Nov | Rule 10 "Read the record, build to it, prove it" | max/CLAUDE.md; verifier subagent on every brief and report | log 7 Nov |
| 7 Nov | Audit of the 3D work against the record (Fable, read-only) | see sws_history.md "Specification and requirements" | log 7 Nov |
| 9 Nov | START.md handoff file | state, running units, rulings pending; fresh session = files only | log 9 Nov; memory |
| 10 Nov | Cold-reader check added before page pushes | "what is this text about?" | log 10 Nov; memory |
| 16 Nov | Method files in the model-round repo (U82) | four sub-agents (builder, cold-reader, falsifier, domain-reviewer), brief and hand-back templates, /brief-task skill; bc6c4cd | log 16 Nov |
| 19 Nov | Six-falsifier team run (U101) | see sws_history.md "Magnetic circuit and FEM" | log 19 Nov |
| 26 Nov | Every study ends with options side by side and a marked proposal | memory written; U138 builder told | log 26 Nov |

### Protocols for outside models: CLIs, Cursor, API key, rounds, blind briefs, masking

| Dates | What was done | Result | Source |
|---|---|---|---|
| 29 Oct | Claude Code and Codex CLI on subscriptions, headless | ChatGPT "Improve the model" off; Codex Cloud repo access declined | log 29 Oct |
| 29 Oct | Codex installed as the Store app | codex-cli 0.165.0-alpha, resolved via CODEX_EXE | log 29 Oct |
| 2 Nov | Boundary probed on both CLIs (U12) | no shell/web; CLAUDE.md/AGENTS.md ignored; Codex still offers apply_patch (read-only sandbox) | log 2 Nov |
| 3 Nov | MAx agent on Fable on the company account | probe with `--model claude-fable-5-1` works | log 3 Nov |
| 4 Nov | Codex could not read files in its Windows sandbox | runs with all files inline instead | log 4 Nov |
| 6–7 Nov | Grok in Cursor on a clean clone of the GitHub repo; independent review of its changes (Gunwale) | 16 files; points 1–3 kept, point 4 dropped; Grok joins as wild card "Fairlead" | log 6–7 Nov |
| 7 Nov | Codex direct reviews (CLI, read-only, masked copies) | both FIX; first attempt hung on stdin | log 7 Nov |
| 8 Nov | Review-round runner and mask tools (U33, Scupper) | tools/review_round.py; mask map: personal 5, customer 1, sites 3, drawings 2, project numbers 3, user path 1 | log 8 Nov |
| 8 Nov | Cursor CLI live | five models pinned; `--sandbox disabled --mode ask` (sandbox macOS/Linux only) | log 8 Nov |
| 8 Nov | Model study and training (preamble) study | three levels; 8 preamble files in tools/preambles/ | log 8 Nov |
| 8 Nov | Claude API key set (pasted in chat) | 106 chars as user env var; credits 200 USD expiring 13 Nov + 100 added | log 8 Nov |
| 8–9 Nov | First nine-model round on the masked pack | see sws_history.md "Reviews by outside models" | log 8 Nov |
| 10 Nov | Key rejected: not scoped to a workspace (HTTP 400) | Fable rows run on the CLI login instead | log 10 Nov |
| 10 Nov – 20 Nov | Blind briefs (requirements only, no parts, no names, scan 0) for every outside round | rounds listed in sws_history.md "Reviews by outside models" | logs 10–20 Nov |
| 16 Nov | Key removed from the environment; new key in a private file, loaded per run | key test 3 of 3: Fable 5.2 54 s, Sol 60 s, Grok 4.7 249 s | log 16 Nov |
| 16 Nov | Model round as its own repo (U78, sternpost) | C:/Users/stian/model-round, 15 tests; pushed to private fjordbit/agentic b1325d1 | log 16 Nov |
| 19 Nov | Plot standard for the shared repo (U104, Sounding) | research + presentation types; 38 tests; branch plot-standard 573e59b, not pushed | log 19 Nov |
| 20 Nov | Old models picked by loose names found | "grok" picked Grok 4.5; rounds rerun with the newest named exactly (U122); models offered listed | log 20 Nov; agent-notes/models_offered_2026-11-20.md |
| 25 Nov | Confinement tested for an outside model on raw data (U125, U128, U129) | Codex app cannot limit reads to the work folder; Cursor enforces none of the limits on Windows | log 25 Nov |
| 25 Nov | Codex through a script loop in the round tool (U131) | 8 of 15 figures agree after the check; parser bug found | log 25 Nov |
| 25 Nov | Fable 5.2 through the API key on its own data copy (U130) | 347 turns, 3.47 h, COST 82.19 USD; no cost limit set in the brief | log 25 Nov |

### Release, export, scan and backup procedure

| Dates | What was done | Result | Source |
|---|---|---|---|
| 25 Oct | max/ pushed to private GitHub fjordbit/max by subtree split | main 87964b8, 5 commits | log 25 Oct |
| 29 Oct | Pre-publish scan and the identifier list | first block: 3 blockers; list started at max-private/identifiers.yaml | log 29 Oct |
| 30 Oct | Publish as a scanned snapshot with no history; completeness added to the check | see sws_history.md "Pages / documentation" | log 29 Oct (30 Oct entries); memory |
| 3 Nov | All design work backed up: 13 branches to D:, 12 heads to GitHub | main 87964b8 → 50470e7 on GitHub; scan 0 real hits | log 3 Nov |
| 4 Nov | Names removed from GitHub history | see sws_history.md "Pages / documentation"; identifiers.yaml 13 entries | log 4 Nov |
| 4 Nov | Export pipeline written down (split → cherry-pick → rewrite names → scan → push) | first incremental export main 7a70832 → 51c9bc1 | log 4 Nov; memory |
| 7 Nov | Export v2 built after an internal project code was found on GitHub | D:/git/max-export-v2.git, 13 blobs rewritten; never pushed | log 7 Nov |
| 9 Nov | Export v3: grafted fast-forward, no deletion | 34 first-parent commits; GitHub 51c9bc1 → 97bd8ce | log 9 Nov |
| 9 Nov | Full copy before reboot | D:\backup\2026-11-09_0223\, 2.5 GB | log 9 Nov |
| 9 Nov | U37 identifier sweep of the tree | 758 → 717 hits; merged 94b354f | log 9 Nov |
| 10 Nov | Kai's own scanner found defective; fixed and kept | 10 of 13 names never tested in three scans; rescan 0; secretary/tools/idscan.py | log 10 Nov |
| 19 Nov | Backup branches on fjordbit/SWS (no build) after "D: is not backup" | main → backup; units → backup-<name> | log 19 Nov; memory |

### Tests and replay runs, including video

| Dates | What was done | Result | Source |
|---|---|---|---|
| 2 Nov | Live runs in U4 (2 runs, ~8 min, 23 calls each) | ended `blocked`: R3 never cleared | log 2 Nov |
| 3 Nov | Live run 20261102-234714: first time the Codex reviewer reached the loop | ended `blocked` (R5 overclaim) | log 3 Nov |
| 3 Nov | Scripted rehearsal in Studio | `studio --rehearse --port 8766` | log 3 Nov |
| 4 Nov | Live run 1 of the default loop, as drawn | `needs_human` after 2 min 22 s; 7 model calls, 1 tool call, 100 events; tape in inbox/2026-11-04_live_run_1/ | log 4 Nov |
| 4 Nov | Live run 2 on main, with the settings map | `needs_human` after 2 min 33 s on a blocking review; 37 settings with sources; tape in inbox/2026-11-04_live_run_2/ | log 4 Nov |
| 5 Nov | ffmpeg 9.0.2 installed (by the owner, winget) | mp4 rule live "from run 3" | log 5 Nov |
| 7 Nov | MAx run on the real record (masked) to verify the SWS state | run 20261107-174251-57e37a ended `needs_human` (FMECA section grew into a verification question) | log 7 Nov |
| 9 Nov | Architect-writer-judge chart run through an outside harness for two pages (U42, U46) | U42 runs 1–3, chart gap found; U46 runs 1–4, brief on the U45 wire in every run | log 9 Nov |
| 18 Nov, 20 Nov | SWS demo video and twin replay page | see sws_history.md "Pages / documentation" and "Digital twin and simulator" | logs 18, 20 Nov |

### Further plan for the MAx flow (as recorded; none of it started)

| Dates | What was planned | State | Source |
|---|---|---|---|
| 23 Oct | Multi-model convergence loop; end goal a web UI where users build their own loops | loop built (flow driver); user-built loops in the browser not built | log 23 Oct, 4 Nov |
| 3 Nov | Next MAx agentic run = the SWS paper | not run | log 3 Nov |
| 5 Nov | Six scenarios: SWS paper; documentation at three levels; spare-parts / warranty API; bilge arms; document creator for MAx-Flow; PLC cases (7 Nov) | none run | log 5–7 Nov; todo.md |
| 6–7 Nov | Document flow with a level parameter (U24); Grok as suggestioneer; side menu "Agents" | never briefed | log 6–7 Nov; todo.md |
| 8 Nov | Review round inside MAx as a review chart (one reviewer block per model, judge on top) | captured | log 8 Nov |
| 16 Nov | Spare-parts / warranty API as first coding task for MAx-Flow | waits for the owner's list of API commands | log 16 Nov |
| 18 Nov | Recap run of all SWS documentation in MAx (four points) | not run | todo.md; START.md |
| 26 Nov | All of the twin through the MAx flow (top view, sub views, protocols as boxes) | see max_flow_for_twin.md | log 26 Nov |

## 2. Rulings by the owner on MAx and the way of working (date order)

- 9 Sep — Never send mail to anyone but him; mail to him is a delivery channel.
- 9 Sep — If he does not answer, he did not see it: few questions, re-asked.
- 22 Oct — Check what exists before creating; QC subagent before any commit.
- 23 Oct — Code may go to Claude and OpenAI for now (ADR 0004).
- 23 Oct — Twin paused; designed inside MAx. MVP direction: multi-model convergence loop; end goal a web UI where users build their own loops.
- 25 Oct — MAx and SWS go to a private GitHub repo on his personal account, knowingly.
- 26 Oct — No public GitHub Pages; Cloudflare Pages + Access.
- 29 Oct — Order U0 → U1/U2/U3 → U4 → U5.
- 29 Oct — Providers for now: Claude Code and Codex CLI on subscriptions, headless; CLI agents only in a boundary-cleaned exchange folder; later an API route paid by the company.
- 29 Oct — Sessions write notes to Kai in agent-notes/; read before you ask.
- 30 Oct — Every agent names itself and signs every answer.
- 30 Oct — The twin is design only for now.
- 30 Oct — Provenance is mandatory in the core (ADR 0008 §1a); modules choose what they inherit.
- 1 Nov — Zoom is the usual mouse zoom (Ctrl+wheel).
- 1 Nov — No external dates; milestones are for his own deliverables.
- 2 Nov — Merge the Studio branches, start U12; a dev board without unit numbers.
- 2 Nov — R3 passes against the DEMO FMECA for now; only RED items block; R4 rate limit only.
- 3 Nov — Review findings by type and severity, all with a human in the loop; minor findings use a retry ladder, settable per module and per user.
- 3 Nov — ADR 0006 approved.
- 3 Nov — Back up all design work.
- 3 Nov — SWS first, then the MAx flow / agentic work; the twin can wait a while.
- 3 Nov — Builders on Opus; Fable for expert answers and the final check before release.
- 3 Nov — The manager is in the repo: it must be tidy.
- 3 Nov — The next MAx run is the SWS paper.
- 3 Nov — "You should not be able to press play if the suppliers are not online" (ADR 0010 accepted).
- 3 Nov — "I want it correct, not hard-coded": design and QC rules enforced; a module can have a saved flow.
- 4 Nov — No names in the cloud.
- 4 Nov — One flow level; zoom shows an agent's internals; what you see is what runs; no hidden inputs; same rule for the twin.
- 4 Nov — Decisions F = 2 (no hidden agents), A = 2 (the chart is what runs), B = needs_human everywhere, D2–D5 yes, E = 2, G = yes.
- 4 Nov — "As simple as it can be but with infinite opportunities to grow"; ADR 0011 accepted.
- 4 Nov — "When we have something good we also do mp4."
- 4 Nov — GitHub export after U22.
- 6 Nov — Review policy goes on the chart; one knob `on_major: revise | human`.
- 7 Nov — Model table: architect + judge Fable, writer + improver Codex; Grok as an option; models not hard-coded.
- 7 Nov — Grok approved as suggestioneer / wild card.
- 7 Nov — H(ii) softer; rule 10 as one rule.
- 7 Nov — Agents follow the document all the way; no selection by the agent.
- 8 Nov — Masking policy: company and suppliers may be named outside; personal and customer names never.
- 8 Nov — Model tiers: tier 0 Fable (only where clearly better: physics, maths, design) and GPT Sol (pre-design) as human stand-ins, priced like a human; tier 1 Opus, Codex, Grok 4.7; tier 2 Gemini, Sonnet, GPT 5.5; DeepSeek, Muse, Kimi off.
- 8 Nov — Chinese models no in general; for SWS one as a literature check.
- 9 Nov — Push all, no deletion: no forced push.
- 9 Nov — The architect's brief reaches reviewer and judge.
- 10 Nov — Pages are about the task, not about him; push "when it reads like it is to help someone understand".
- 16 Nov — API key out of the environment; a new key never in chat.
- 16 Nov — The model round goes to fjordbit/agentic for his manager.
- 16 Nov — The spare-parts / warranty API is the first coding task for MAx-Flow; AI policy dropped for now.
- 19 Nov — D: is not a backup; backup branches on fjordbit/SWS without a build.
- 19 Nov — A plot standard: research type and presentation type.
- 20 Nov — Use the newest model of each family, named exactly.
- 23 Nov — Signalling is handled in MAx; the earlier zoom view (shiplift → main stations → winches → 2 SWS) may be the better structure.
- 25 Nov — Codex on the raw data as far as possible kept separate; Cursor and Grok a later resort; Fable through the API key yes.
- 26 Nov — All of the digital twin runs out of or through the MAx flow: top "all" view, sub views, protocols as boxes at the lower zoom.
- 26 Nov — The plan in layers of interest, like MAx.
- 26 Nov — Studies propose the optimum; management decides.
- 26 Nov — First names allowed when not negative; never last names.
- 27 Nov — The list of rulings is private; model names stay off the site; no forced push on the backup branch (entries dated 27 Nov inside log 26 Nov).

## 3. Open items

- 6 Nov → 9 Nov goal — U24 (document flow with a level parameter, paper / plain; per-login model overrides): never briefed.
- 5–6 Nov — Live run 3 and the first mp4 of a MAx run: never run.
- 3 Nov, 5 Nov — SWS paper through the MAx flow (scenario 1): not run.
- 18 Nov — Recap run of all SWS documentation in MAx (four points listed): not run.
- 4 Nov — Owner's calls left by U22: placeholder minting, reviewer sees the sources, chart 0.2 (D4).
- 31 Oct – 1 Nov — Chart 0.2 draft: adopt or not (asked by U13, U14, U22).
- 1 Nov — U14 questions: bad-upstream look in 3D; draw chart instances only or all winches; reference lift drawing and who sends it.
- 1 Nov — U15 questions: ADR 0009 (Python now, Modelica later); new chart ports vs renaming; hoist numbering.
- 2 Nov — Functional / Network switch in the zoom view: named "next", never built.
- 30 Oct — ADR 0008 (firm core, modules, rule packs): on its branch only, PROPOSED.
- 7 Nov — Invalid MAX_RULE_STUBS: stop the run in preflight or keep driver refusal.
- 7 Nov — U26 follow-ups (per-level saved position, shared track, flat 0.1 charts).
- 9 Nov — `max run --seed`; severity of a missing brief; test_review_round expects an `xai` backend (fails on main).
- 7 Nov — xAI / Grok provider in MAx; Studio side menu "Agents" with a default model per type.
- 3 Nov — MAX_CLAUDE_CLI_MODEL machine-wide (setting() does not read ~/.max/settings.yaml for model keys).
- 8 Nov — MAx review chart (the reviewer half of the paper flow): captured, not built.
- 7 Nov — A "verify" chart without the FMECA rule: captured, not built.
- 29 Oct, 12 Nov, 16 Nov — Demo visit and the mail asking for company-paid API accounts: not drafted.
- 25 Nov — Cost limit on API-key runs: not in the round tool; free runs of an outside model need a separate Windows account or Linux/WSL.
- 10 Nov — Old content on GitHub / Pages: owner's first name in older reports; a customer-name hit in a U13 image.
- 8 Nov — rewrite_names.py: rules for site names, first names, user path.
- 16 Nov — Spare-parts / warranty API task: list of API commands still to come from the owner.
- 19 Nov — Plot standard branch not pushed; U99 plot layout superseded but unmerged.
- 5 Nov (todo) — One home for the repos (MAx-Flow org); hosting on the tower with phone access; max-flow.no behind Access.
- 7 Nov — Own local helper trained on logged faults from released runs: idea only.
- 16 Nov — Auto-start of Kai at boot; calendar and mail access for Kai.
- 29 Oct — Notes channel is "until MAx has its own": MAx has none yet.
- 26 Nov — Wiring the twin into the MAx flow (see max_flow_for_twin.md).
- 16 Nov — Vessel library: u80 design not merged; next step after the reply is the owner's ("first coding task: Vessel Library", todo).
- 2 Nov, 5 Nov — Bilge arms: sales-offer flow needs the manager and ready models; not started.
- 27 Nov (owner, via Kai) — SWS work for the current customer takes precedence over all items above.

## 4. Could not establish

- Work on MAx before 22 Oct (six weeks on another computer): not in these logs; only the scaffold that arrived.
- Whether the strategy-paper meeting (September) was held, and what was decided there: never reported back.
- No secretary logs for 12 Sep – 21 Oct, 24 and 27–28 Oct, 13–15, 21–22 and 24 Nov.
- Whether the demo visit "the week before 20 Nov" (M2) happened.
- Whether Ramin used the model-round repo (fjordbit/agentic) or was given access (owner to add him, 16 Nov).
- The "cost limit on every API-key run" and "outside models not run unconfined" appear as rulings in START.md (25 Nov) but no log line records the owner's words; the 25 Nov log only says Kai set no cost limit and told him.
- "Interface (API) work closed until next year" (in the U141 brief): no log line found.
- U1 (vault), U2 (prompts) and U6 (paper) as units: referred to, never logged as built or merged on their own.
- ADR 0009 status: merged with U15 on 2 Nov as PROPOSED; no ruling found.
- Ship database "delivered and handed to a colleague to continue": the sources show only the first design
  (16 Nov, on a branch, not merged) and the reply drafts (16–18 Nov). No log or note records a delivery or a
  hand-over; the row stops at 18 Nov.
- Sales support in the digital-twin planning: not found. The DT plan (23 Nov), the twin notes and the functional
  spec name no sales use; the only sales items are the bilge-arms "sales-offer flow" (2 Nov) and the strategy
  paper's enquiry-to-offer case (8 Sep). Not written as its own heading for that reason.
- Bilge arms: no work beyond the strategy, the scenario list and one worked example is recorded on this machine.
- Exact MAx test counts after 9 Nov: no engine work logged after U45 (git: last engine change 9 Nov, U119 touched only the chart example's converter counts on 20 Nov).
