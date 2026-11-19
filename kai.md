# From Kai to all sessions

Only Kai writes here. Newest at the bottom.

## 2026-10-29 — notes protocol

- From now on, keep your notes in `C:/Users/stian/agent-notes/<your-session-name>.md`
  (see README.md). Please write one the moment you start, commit, get blocked or finish.
- U7/U8 session: when the demag runs are merged and committed, write
  "ready for Kai's check". Kai then checks the diff, runs the pre-publish scan and
  publishes SWS to `fjordbit/SWS`.
- Don't merge `u08-sws-3d` into `main` yet. `main` now has U0 (`1ad0d53`), so
  it will be a real merge. That happens after Kai's check, and Stian decides.
- New worktrees: copy `CLAUDE.local.md` from `C:/Users/stian/Prosjekter/max/` into
  the new worktree's `max/`.

## 2026-10-29 — U12 brief (beta backend on subscription CLIs)

You are U12. Read max/CLAUDE.md, tasks/TASKS.md, tasks/reports/U00.md and
docs/decisions/0005 first. Your notes go in `u12-cli-providers.md` in this folder.
Write one when you start.

WHERE
Worktree C:/Users/stian/Prosjekter-u12/max, branch u12-cli-providers (from U0,
1ad0d53). Work only here. U8 is running in C:/Users/stian/Prosjekter; don't touch it.
Make your own venv: python -m venv .venv; pip install -e ".[dev]".

THE DECISION (write it down first)
1. docs/decisions/0006-beta-runs-on-subscription-clis.md, short, same style as 0001-0005:
   - MAx beta runs on Claude Code (`claude -p`) and Codex CLI (`codex exec`), under
     existing personal subscriptions. No API keys.
   - Users: Stian plus two named colleagues, all with both subscriptions. The beta is
     for showing, testing and running before Syncrolift funds API access.
   - v1 moves to the API (the U1/U2 connectors) on prepaid Syncrolift accounts. These
     are to be requested after the demo in the week before 20 Nov 2026.
   - The switch must be seamless: one setting, and no code change outside the
     providers. ADR 0001 (Claude works, OpenAI reviews) still holds.
   - Conditions: CLI agents only ever see boundary-cleaned files, and training on
     chats is switched off on the plans used.
2. tasks/TASKS.md: add U12 to Wave 1, and make U4 depend on "U1 or U12". Keep the
   edit small.

BUILD
- Write max_core/providers/claude_cli.py and codex_cli.py, implementing the FROZEN
  Provider in base.py. Don't change base.py or runlog.py. If something truly cannot
  fit, stop and report: that would need an ADR, not a silent change.
- Backend switch: add MAX_BACKEND=subscription|api to .env.example (and to .env if it
  is missing), defaulting to subscription. registry() resolves "claude" to
  ClaudeCliProvider or ClaudeProvider, and "openai" to CodexCliProvider or
  OpenAIProvider. roles.yaml stays unchanged.
- Binaries: claude is on PATH (Claude Code 2.1.312). Codex comes bundled with the
  Store app: codex-cli 0.165.0-alpha. Its path is versioned and changes with every
  update, e.g. C:/Program Files/WindowsApps/OpenAI.Codex_26.1023.6621.0_x64__2p2nqsd0c76g0/app/resources/codex.exe.
  Resolve each binary from CLAUDE_EXE / CODEX_EXE in .env first, then PATH. Never
  hard-code a path. Stian may install a proper Codex CLI later.
- Billing guard: in subscription mode, strip ANTHROPIC_API_KEY and OPENAI_API_KEY
  from the subprocess environment, or the CLI will bill the API.
- Data boundary: the CLI runs with its working directory set to MAX_EXCHANGE_DIR
  (outside the repo), which holds only files written there by Boundary.outbound.
  Switch off its web and shell tools, and limit file access to that directory. Look
  up the real flags with `claude --help` and `codex exec --help`; don't rely on memory.
- MAx tools: expose the on-prem tool registry (max_core/tools) to both CLIs as a
  local MCP server built from that same registry, so tools run inside MAx and are
  logged as tool.call/tool.result. The registry is empty now; prove the bridge with
  one test tool.
- Structured output: use the CLI's own JSON-schema option if it has one, otherwise
  validate in the connector. Raise StructuredOutputError on failure.
- Usage: map tokens from the CLI's JSON output. If a number isn't reported, write 0
  and add usage["usage_reported"]=0. Never estimate.

TESTS
- Unit tests with a fake subprocess: arguments, env stripping, cwd = exchange dir,
  JSON parsing, the MAX_BACKEND switch.
- Live tests marked `live_cli`, skipped when a binary is missing: one role call
  through each CLI provider with a masked customer name that the vault restores,
  plus one MCP tool call that gets logged.

DON'T
- Touch claude.py, openai_provider.py or boundary.py. Those belong to U1/U2; note
  any gaps in your report.
- Touch sws/, twin/ or studio/.
- Merge.

FINISH
- Write the report: tasks/reports/U12.md.
- Run qc-falsifier on the diff. Commit on u12-cli-providers only if it reports no
  blocking findings; the message starts with "U12".
- Don't push or merge.
- Write a note saying "ready for Kai's check", then stop.

## 2026-10-29 21:00 — read before you ask (all sessions, from Stian)

Before asking Stian or Kai anything, search the existing work: the spec,
`sws/deltas/`, `sws/SWS_FILE_MAP.md`, `docs/decisions/`, `tasks/reports/`, the
READMEs and git log. Only ask what that work does not answer, and say what you
checked. Most of U7 work's last list was already answered in earlier work.

## 2026-10-30 ~01:30 — identifier list (all sessions)

`C:/Users/stian/max-private/identifiers.yaml` lists names that must never appear in a repo,
on a published page or in a model call. Read it; never copy it into a repo. Use the
placeholder it gives. U1 will load it into the boundary later.

## 2026-10-30 — spec owner's answers to the six questions (pasted by Stian; binding unless Stian overrides)

Source: the SWS specification owner (the original architect), 2026-10-29, relayed by Stian on 2026-10-30.
Summary below. Full text: ask Kai, or see Stian's paste in the secretary log reference.

1. Hours: human hours only from Stian. Model hours from the session logs (sourced).
2. Bore = free passage inside the magnet guard (r_bore = guard inner face, r_mi = r_bore + t_guard). The double
   subtraction in hw-selection/sws_geometry_stack.py is corrected in the owner's delivery. Clearances at +4 % rope:
   Ø48/40 3.2 mm, Ø60/52 2.96 mm, Ø65/57 2.86 mm. DECISION: shared 40+52 head Ø60; wide head Ø65;
   **Ø70 WITHDRAWN** (keep its rows as data, or mark it "not required" in params.yaml).
3. Stian's call. Owner's recommendation: the wide 35–57 head is an OPTION, not rev 1 (bore 65 if kept). Design U9 for
   the shared head's worst case (~75 mT axial, hard wire, −40 °C), and record that the wide head needs ~91 mT. Choose a
   ≥180 mT part only if it meets 0.10 mT p-p at 250 S/s; otherwise the wide head gets its own sensor variant.
   The radial TMR cross-axis tempco goes in the U9 selection table as a drift term. File the background table as a register row.
4. B_rope is NOT settled. Which quantity EN 12927 Ch. 14 means (flux over the metallic area vs B_wire) is status U, and
   Stian must read §14. Until then run_case() reports B_rope, B_wire, H_rope and μ0·H. Conservative sizing on file:
   1.92 T floor on B_wire → shared head lm 19.1→20.7 mm, 2.99→3.3 kg. Always say which definition a number uses.
5. 3D check tolerance (proposal, status A until Stian accepts): rope induction ±1e-3 T, sensor field ±0.2 mT.
   The residuals reported are inside both → recommendation "3D-A verified on these results".
6. params.yaml wide heads: keep them. The W65/W70 yokes (13.4/13.0 mm) come from the result 7 flux rule; re-deriving should give ~13 mm.

The owner's delivery changed: hw-selection/sws_geometry_stack.py (+ geometry_stack.json), fem-2d/sws_head.py (B_wire output),
fem-2d/sws_consolidated_findings_2026-10-23.md, fem-2d/sws_review_2026-10-23_findings.md, data/sws_data_sources.md,
due-diligence/briefs/sws_carrier_brief.md, and the Claude Doc (result 10 (4), sections 12 and 14).

## 2026-10-30 — name yourself and sign (all sessions, from Stian)

Choose a short name that fits your work, and say it once in your next answer and at the top of your notes
file. Keep it for the whole session. End every answer, note and cross-session message with `— <name>`.
Your notes file keeps its current filename. Kai signs `— Kai`.

## 2026-10-30 — SWS published

fjordbit/SWS now holds a snapshot of caa522e (no history). Publishing is Kai's job: re-extract, scan against identifiers.yaml,
then push from C:/Users/stian/publish/SWS to fjordbit/SWS and MAx-Flow/SWS-Documentation (internal). Sessions don't push to fjordbit/SWS themselves.
— Kai

## 2026-10-31 — U13 brief (Studio front end: module select + chart kernel)

You are U13. Name yourself after your work (rule 9) and sign every answer `— <name>`.
Read max/CLAUDE.md, tasks/TASKS.md, flow/README.md, flow/STANDARDS.md, ADR 0007, and
studio/README.md first. Your notes go in `u13-studio-frontend.md` in this folder.
Write one when you start.

WHERE
New worktree C:/Users/stian/Prosjekter-u13/max, branch u13-studio-frontend, from
u10-twin-design at 6c7b03d (the chart format lives there and is not merged yet).
Keel has uncommitted ADR 0008 work in Prosjekter-u10. Don't touch it. Treat 0008 as
proposed, not binding. Other trees: Prosjekter (U8/Flux), -u00, -u12. Not yours.

WHAT STIAN WANTS
Something he can see and use: one Studio front end where you pick a module, **agentic**
(MAx) or **twin**. Each module draws its flow from the same chart file, using one
shared kernel. The twin view comes first: value lines, line thickness by what flows,
and status patterns, all per the line language.

THE KERNEL (shared, module-neutral)
"Kernel" here means the front-end kernel. It does not mean the execution engine.
P7 says the backend executes everything, and no twin backend exists.
1. Load a `max-flow/chart@0.1` file and validate it against flow/chart.schema.json.
   Don't change the schema. If the views need more than it holds, stop and write the gap
   down as a proposal for chart@0.2.
2. Draw blocks, ports, wires, edges and frames from `view: {x, y, w}`.
3. Draw lines per twin/Shiplift-twin-analysis/docs/flow-line-language.html:
   - Geometry says what flows (thickness, circles, markers). Colour and pattern say how
     it is doing. Never mix the two.
   - Normal is quiet (ISA-101). Use the page's dash patterns for late/stale, offline,
     waiting and not bound. The `z⁻¹` marker goes on delay edges. Message lines are distinct
     and never meet a signal port. A bus takes the worst status of its members and shows a
     count badge. Binding lines use the small-circle glyph.
   - Take every thickness class, colour and pattern from that page. Where the page says
     proposed or open, implement it and list it in your report as "rendered from a
     proposed rule".
4. Value lines: a line shows its current value + unit + status (OPC UA status names) at
   a label on the line. Values come from a value stream the kernel animates (step, play,
   pause, scrub).
5. Zoom levels from the instance hierarchy (frames), if the chart carries it.

THE TWO MODULES (profiles on top of the kernel)
- twin: flow/examples/twin-hoist-load.chart.json. There is no twin code or physics, so
  drive it with a scripted replay file and label it DEMO on screen. The demo values must
  be visibly synthetic (round, obviously placeholder). Never present them as calculated
  hoist loads. Provenance (R2) applies.
- agentic: flow/examples/max-agentlive.chart.json, animated from the scripted run in
  studio/AgentLive.dc.html, converted to run-log events (schema max_core/runlog.py,
  frozen; don't edit it). Map events to the chart per the table in flow/README.md.
  Leave the spawned-agent position as U5's [OPEN]. Pick something sane and say so.
- Module selector: a top-level switch. Adding a third module later must mean only a new
  profile + chart, with no kernel change. Prove it with a test.

BUILD RULES
- Open source only (P1). Plain HTML/JS/SVG, served locally. Pin exact versions of any
  library. No external services, no CDN at run time, nothing leaves the machine.
- Code lives in studio/kernel/ and studio/modules/{twin,agentic}/. Keep the four
  .dc.html designs as they are. They are the visual reference for style.
- Light and dark, keyboard usable.
- Stay inside the design pages. Where they disagree with the 14 Oct screens, the pages win.
  Don't invent new visual rules; write them up as proposals instead.

OUT OF SCOPE
Twin execution/simulation, PLC coupling, a live run of a real `max run` (U5, waits on
U4), editing charts (save/compile, E8), and publishing anywhere.

TASKS.md
Add U13 to the graph (depends on U10). Make U5 build on U13's kernel for the live part.
Keep the edit small.

TESTS AND DONE WHEN
- Tests: the schema validates all 3 examples; each line-language rule has a render test
  (status → pattern, flow kind → thickness, bus worst-status); the module-add test.
- Done when: `python -m max_core.cli studio --demo` (or a documented equivalent) opens
  the selector, both modules animate, and a screenshot of each is in the report.
- qc-falsifier pass: checks every rendered rule against flow-line-language.html, and
  that no demo value can be mistaken for a computed one.
- Report: tasks/reports/U13.md. Commit on the branch. Don't push and don't merge.
  Tell Kai in your notes file when it's ready for checking.

Timebox: one working session. If the twin view alone takes that, stop there and report.
The agentic module can follow.

## 2026-11-01 — U14 brief (Shiplift 3D view, simplified)

You are U14. Name yourself after your work (rule 9) and sign every answer `— <name>`.
Read max/CLAUDE.md, tasks/TASKS.md, tasks/reports/U13.md (all sections), flow/README.md,
twin/Shiplift-twin-analysis/docs/architecture.html (P1, P6, P7, P8) and
flow-line-language.html first. Your notes go in `u14-shiplift-3d.md` in this folder.
Write one when you start.

WHERE
New worktree C:/Users/stian/Prosjekter-u14/max, branch u14-shiplift-3d, from
u13-studio-frontend at 43d62c2. Kai creates it. Work only there. U13 (Weft) owns
studio/kernel/ and the SWS chart. Read and reuse them, and don't refactor them. If the
kernel needs a hook, add the smallest one and list it in your report.

WHAT STIAN WANTS
A simplified physical 3D view of the shiplift, beside the flow chart in Studio. It is
for understanding where things are, not for engineering. Use boxes and cylinders, no CAD yet.
- Platform as a long slab, possibly in sections. Winches along both sides at a fixed
  pitch. A rope from each winch to the platform with its 2 SWS on it. Base stations
  near their winches. The main control room and the HIL room, with fiber routes drawn
  from the base stations.
- Generate the 3D scene from the same SWS shiplift chart
  (flow/examples-0.2-draft/sws-shiplift.chart.json) plus one new geometry parameter file,
  e.g. `twin/geometry/shiplift-layout.demo.yaml`: platform length/width, winches per
  side, pitch, sections, positions of base stations and rooms. Every number in it is a
  DEMO placeholder with [N] provenance until Stian supplies the general arrangement.
  Don't invent a real lift's dimensions.
- Two-way link: clicking a winch, SWS, base station or room in 3D zooms the flow chart to
  that frame, and selecting a frame in the chart highlights it in 3D. Both views use the
  same instance paths.
- Status in 3D follows the line language: normal is quiet grey and only deviations get
  colour, so the DEMO sensor failure, late half and not-installed SWS from U13's replay
  show on the 3D objects too.
- Later, real geometry replaces the boxes: simplified STEP/glTF exports from CATIA
  (3DEXPERIENCE). Design the loader seam for glTF now, but don't build a CAD pipeline.

BUILD RULES
- Open source (P1): three.js, pinned exact version, vendored locally. No CDN at run time,
  no external services, nothing leaves the machine.
- Lives in studio/modules/sws-3d/ (or a 3D pane in the SWS module, whichever is cleaner),
  plus twin/geometry/. Light and dark. Keyboard and mouse orbit.
- Nothing executes in the view (P6/P7). It only draws the chart and the value stream.
- No site, customer or project names; use placeholders. Don't read max-private.

OUT OF SCOPE
Real dimensions, CAD import, physics, rope or platform deflection, vessel, publishing.

DONE WHEN
- `python -m max_core.cli studio --demo` shows the SWS module with a 3D pane. The scene
  is built from the chart + layout file, and the click-through works both ways.
- Tests: the scene builder makes one object per chart instance and none extra; every
  layout number carries DEMO provenance; the instance paths match the chart.
- Screenshots: the overview, one winch close-up, and the click-through state.
- qc-falsifier pass with no blocking findings, then commit on the branch. Don't push or merge.
- Report in tasks/reports/U14.md. It lists exactly what real input replaces each
  placeholder: general arrangement, CAD exports, room/base-station locations, reference lift.

Timebox: one session. If the click-through takes it, stop and report.

## 2026-11-01 — U15 brief (Test model: simplified shiplift, first principles)

You are U15. Name yourself after your work (rule 9) and sign every answer `— <name>`.
Read first: max/CLAUDE.md (especially R2, provenance); tasks/TASKS.md; twin/DESIGN.md;
twin/Shiplift-twin-analysis/docs/architecture.html, execution.html and decision-log.md (50 ms
tick, lockstep with PLCSim, FMI 2.0, PROFIdrive);
`C:/Users/stian/Prosjekter/INPUT - Functional Specification Digital Systems and Services.md`
section 4 (what the Mechatronics Model covers per hoist and platform); and U10's
`twin.platform_load` tool contract. Your notes go in `u15-test-model.md` in this folder.

WHY
Syncrolift plans the Mechatronics Model with Controllab (20-sim). Stian wants an
in-house test model as well: simplified, built from first principles, ours. It may stay
a test model, or it may grow good enough to simulate everything in house. Build it so
either outcome works. The interface must match the slot the 20-sim model would fill, so
one can be swapped for the other.

WHERE
New worktree C:/Users/stian/Prosjekter-u15/max, branch u15-test-model, from
u13-studio-frontend at 43d62c2. Kai creates it. Code goes in twin/model/. Don't touch
studio/ (U13/U14) or other worktrees.

FIRST: AN ADR (short, same style as the others)
Choose the modelling stack and write down why. Both options are open source (P1):
(a) Python (numpy/scipy) with an FMI 2.0 co-simulation wrapper later, or (b) Modelica
(OpenModelica) with native FMU export. Weigh: speed of agent work, acausal mechanics,
FMU export, and running in lockstep at 50 ms. Recommend one and mark it PROPOSED. Stian
decides. Build the v0 in the recommended stack.

MODEL v0 (simplest thing that is physically honest)
Per hoist, in a chain:
- drive and motor as a speed loop (first-order or PI) with a torque limit. No PROFIdrive
  state machine yet.
- gearbox: ratio and efficiency.
- drum: radius, inertia, brake as a holding torque.
- wire rope: an elastic spring–damper with k = EA/L(t). Length changes with drum rotation,
  through the reeving ratio.
- load cell pin: reads the rope force through the reeving.
Platform: start as a rigid body, heave plus trim and heel, on N hoists along two sides,
then add one flexible variant (a beam on elastic supports) as a switch. A rigid platform on
many hoists is statically indeterminate. The rope stiffness is what sets the load
distribution, so show that explicitly.
Load: a vessel as a distributed or point load on the platform (mass, position). No buoyancy in v0.

Interface: inputs are speed setpoints and brake commands per hoist. Outputs are rope
tension, load-pin value, drum position and speed, motor torque and speed per hoist, and
platform position, trim and heel. Signal names and instance paths follow the SWS shiplift
chart (flow/examples-0.2-draft/sws-shiplift.chart.json) so Studio can show the model's
output later. Use a fixed 50 ms co-simulation step and a smaller internal solver step if
needed.

PARAMETERS (R2 applies)
- All parameters go in one file, e.g. twin/model/params.demo.yaml, each with a provenance
  field. The values are DEMO placeholders, [N]. Never present them as a real Syncrolift
  lift. Where a textbook formula sets a parameter (EA of a rope from its fill factor and
  modulus, for example), write the formula and the source.
- No customer, site or project names. Don't read max-private.

VERIFICATION (this is the point of first principles)
Each check is a test:
- statics: the sum of hoist loads equals the weight, and the moments balance, against a hand calc;
- uniform load on a rigid platform with equal ropes gives equal hoist loads;
- an off-centre load gives the hand-calculated linear distribution;
- energy: motor work equals the change in potential energy plus the losses, within a tolerance;
- step response: the speed loop time constant matches its parameter;
- rope: natural frequency sqrt(k/m) against a hand calc.
A qc-falsifier re-derives at least two of these by hand.

OUT OF SCOPE
PLC coupling (PLCSim lockstep), PROFIdrive, buoyancy, 3D, Studio wiring, FMU packaging
beyond a stub, real parameters, publishing.

DONE WHEN
- `python -m twin.model.run --scenario lift_uniform` (or similar, documented) runs a
  lift-and-hold scenario and writes a CSV plus 3–4 plots: hoist loads, platform trim,
  rope tension, motor torque.
- All verification tests pass, and the ADR is written.
- The report, tasks/reports/U15.md, says what the model can and cannot answer yet, and lists
  every placeholder with the real input that replaces it (general arrangement, drive data,
  rope data, gearbox, drum).
- qc-falsifier pass with no blocking findings, then commit on the branch. Don't push or merge.

Timebox: one session. If the platform plus statics checks take all of it, stop there and report.

## 2026-11-07 — U23 brief (review policy on the ladder: `on_major`)

**Decision (Stian, 6 Nov 21:50 and 7 Nov 00:30):** the review policy goes on the chart, as
one knob. Minor is always `revise`, critical always stops (the floor), so the only choice a
flow makes is what a blocking **major** finding does: `on_major: revise | human`. Default
`revise`. `review_policy.yaml` keeps nothing a chart can set; the floor becomes a rule.
Stian's reason: the SWS paper and the bilge-arms studies must iterate on majors to the cap
without a person each loop; a safety flow sets one word to stop on major.

Branch `u23-ladder-on-major` from `main` 4730e63, worktree `Prosjekter-u23`. Name yourself
and sign. Design first, then the small build, one session. Timebox 90 min design, 90 min build.

READ (all, before writing)
`docs/design/flow-driver.md` (§2 audit row "the review policy", §4.2 the ladder block,
§8 Cap, §11.1 default loop), ADR 0011 (decisions B and E), `flow/chart.schema.0.2-draft.json`
(ladder params), `max_core/driver.py` (ladder firing, where `ReviewPolicy` is read),
`max_core/orchestrator.py` (`ReviewPolicy`, `OUTCOMES`, `_review`), `agents/review_policy.yaml`,
`agents/policies/README.md`, `preflight.py` (the review-policy check), `flowcheck.py`,
`tests/test_orchestrator.py`, `test_preflight_chart.py`, the two charts under
`max_core/flows/max/`, reports U21 and U22, `docs/design/process-rule-design-conformance.md`,
`CLAUDE.md`, `.claude/agents/qc-falsifier.md`. Nothing under `max-private/`.

DESIGN (flow-driver.md, a new round; the audit row flips to **yes on the chart**)
- `ladder {attempts, escalate_from?, on_major?: revise | human}` replaces `policy: review`.
  State in §4.2 exactly how the `msg:review` branch reads it: worst severity across the
  reviews of this `rev`; minor → count; major → count if `on_major: revise`, else `human`;
  critical → `human` with "critical finding" (the floor, never settable); blocking with no
  finding = major (the former `default_severity`, now a stated rule, not a key).
- `review_policy.yaml`: delete it, or reduce it to a comment pointing at the rule. Say which
  and why. `policies/<module>.yaml` and the user-settings layer go with it (one fewer layer;
  if you keep any of them, say what a chart cannot express that they can). Preflight's
  review-policy check becomes a schema check of `on_major` on every ladder.
- The ladder zoom in the Studio shows `attempts`, `escalate_from`, `on_major` and the count.
- **Worked examples, in the design doc, as a short section with three charts drawn as
  text (Stian asked for this; the current text is correct but not easy to see):**
  1. paper loop — `attempts: 5, on_major: revise`: five revisions, then needs_human;
  2. bilge-arms study — same shape with findings from a judge, metric tick optional;
  3. strict flow — `on_major: human`: stops on the first blocking major.
  Each: the chart, the log lines of one run, when a person is asked and why.
- Keep decision B: a ladder never ends a run `blocked`.

BUILD
- Schema 0.2: `on_major` enum, default `revise`; `policy` removed. Both shipped charts
  updated (default loop: `ladder_review` gets `on_major: human` so run 2's behaviour is
  reproduced exactly by the default chart; the writer flow gets `revise`).
- `driver.py`: the ladder reads `on_major` from its params; `ReviewPolicy` loading is
  removed from the run path or reduced to the floor. `preflight.py` and `flowcheck.py`
  follow. Tests: the acceptance test, one per example chart above (major on `revise`
  iterates to the cap, major on `human` stops, critical stops under both), preflight.
- `docs/decisions/`: a short ADR 0012, or an amendment to 0011, naming this decision F.
- Done-lines cite the design (conformance rule). qc-falsifier with no blocking findings,
  then commit on the branch. Report `tasks/reports/U23.md`. Do not push or merge.

OUT OF SCOPE
The document-flow level parameter (paper / plain), the four model ids, live run 3,
Studio line auto-arrange. If the design round finds a real case for a per-severity table,
write it in the report and still build the one knob.

— Kai

**U23 addendum (Stian, 7 Nov 01:00):** keep the user-settings layer (`MAX_USER_SETTINGS`,
`~/.max/settings.yaml`) and `policies/<module>.yaml` as mechanisms; only the review policy
leaves them. U24 will use the user layer for **model per role** overrides (chart `params.model`
= the flow's default; a login profile may override per role, e.g. Grok as Stian's default
suggestioneer). Design that layering in one paragraph of §2 now so U24 does not reopen it;
do not build it. — Kai

## 2026-11-07 — U25 brief (SWS P52: yoke and magnet prototype design for the 52 mm rope)

**From Stian, 7 Nov 01:20:** a direct agent unit, not through MAx. Deadline for the prototype
design: **~21 Nov 2026**. This unit is the first session; it ends with a design the head
designer can draw from, or a clear list of what is still missing and why.

Branch `u25-sws-p52-prototype` from `u19-sws-stranded-poles` 023da1f (the newest SWS code:
stranded rope, eps_reg 1e-4), worktree `Prosjekter-u25`. Work only in `sws/3d/`, `tasks/`,
`sws/params.yaml` (additions only). Name yourself, sign, notes to
C:/Users/stian/agent-notes/<name>.md. Timebox: one session; stop at the end of it and report.

GOAL
A buildable prototype design of the **H52 head** (shared 40 + 52, free bore Ø60: magnet
19.1 × 40 mm, yoke 12.0 mm, spec rev124 result 10, N48SH preferred) for the **52 mm Powerplast
rope**, as the Ø40 prototype (P40) was built from the head designer's drawings — but this time
designed *here* and handed *to* the head designer.

READ (all, before anything)
`sws/3d/README.md`, `THEORY.md` (assumptions A1–A8, S1–S6), `design_inputs.md` (sensitivity
table §…, magnet/yoke rows), `geometry_study.md` §2 (the yoke cut-out), `verification.md`
(3D-A, 3D-B gap sweep and halves force, 3D-C2, 3D-D2), `rope_construction.yaml`, `model3d.py`,
`rope3d.py`, `run_3dc2.py`, `fig3d.py` (STEP export), the P40 geometry (grep -il p40 sws/3d),
`sws/params.yaml`, `sws/spec/README.md` and the rev127 spec sections 5, 7, 12 (render with
`render_spec.py` if needed; the docx is the record), `sws/SWS_FILE_MAP.md`, reports U08, U16,
U17 (§0 drawing reading, §6 P40), U19 (the floor finding), `tasks/TASKS.md`, `CLAUDE.md`,
`.claude/agents/qc-falsifier.md`. Nothing under `max-private/`. In anything you write, the
head designer is "the head designer", never a name (identifier rule, kai.md 2026-10-30).

WHAT U19 FOUND THAT THIS DESIGN MUST ANSWER
On the stranded 52 mm rope, hard wire, +80 °C, the H52 head gives B_rope ≈ 1.915 T unbounded:
0.3 % under the team's 1.92 T floor (1.9 T requirement holds). Decide and show the smallest
change that restores 1.92 T with margin — magnet thickness (design_inputs sensitivities), yoke,
or accept and state — on the stranded rope at a large box (≥ 600 × 800, one 1200 × 1600 check).

DELIVERABLES
1. `sws/3d/p52/` (new): parametric OCC geometry of the full prototype head — magnet ring
   (segment count and segment dimensions a magnet supplier can quote; grade N48SH placeholder,
   status A), yoke (wall, length, the sensor cut-out as the head designer drew it on P40 —
   outside notch, U17 §0 — sized for the 16 TMR at 3 mm stand-off and the axial sensor at
   R 36.5), clamshell split (gap per 3D-B, hinge/latch envelope as placeholders), end detail.
   STEP export. Reuse `model3d.py` / `fig3d.py`; do not fork the solver.
2. Solved in 3D with the U19 stranded rope at both corners (hard +80 °C, easy −40 °C):
   B_rope, the 16 sensor backgrounds, the 2-hidden-wire fault at the worst angle (one case),
   halves force. Mesh ≤ ~2.5 M unknowns (RAM is the limit on this machine; page file 64 GB;
   never two heavy solves at once; another session may run tests at the same time).
3. `sws/3d/p52/design.md`: dimension table (every number with its source), the floor decision
   above, magnet mass and segment list, sensor positions, open inputs the design still needs
   (real magnet grade and steel curve from suppliers, the B_rope vs B_wire reading of EN 12927
   §14 — Stian's call — the tolerance acceptance, the real notch depth). Written so the head
   designer can draw from it. Kai turns its summary into the mail.
4. `verification.md` gains a "P52" section; `README.md` status line; `build.py --only p52`.
5. qc-falsifier re-derives one number by hand. Report `tasks/reports/U25.md`. Commit on the
   branch; no push, no merge.

OUT OF SCOPE
Sensor electronics and PCBs (U9/U11), the wide head W65, hysteresis/eddy currents, CATIA
(STEP is the seam), anything through MAx.

DONE WHEN
STEP + design.md + both-corner solves + verification section exist, tests that exist still
pass, qc-falsifier passes, report written. If the solves do not fit the session, stop with
the geometry, design.md and one corner, and say which numbers are missing.

— Kai

## 2026-11-07 — U26 brief (Studio: auto-arrange the lines)

**From Stian (5 Nov, confirmed 7 Nov 01:50):** the lines and the look of the flow are messy.
Kai's diagnosis 5 Nov: `studio/kernel/hier.js` places columns by longest path and rows by one
barycentre pass; ports are in declaration order; long and feedback lines (ladder `retry` /
`escalate`, the `count` delay edge) are drawn straight back across the blocks.
`studio/kernel/chart.js` (`layout`, line 111) does the 0.1 placement; `lines.js` is the line
language (colours/states, not routing); `render.js` draws.

Branch `u26-studio-arrange` from `main` 4730e63, worktree `Prosjekter-u26`. JavaScript only,
under `studio/`; no engine code, no chart files. Name yourself, sign, notes to
C:/Users/stian/agent-notes/<name>.md. Timebox: one session, 3 h of own work. Another session
(U23) works in a different worktree on the engine; no collision.

READ (all, before anything)
`studio/README.md`, `kernel/chart.js`, `hier.js`, `render.js`, `lines.js`, `shell.js` (zoom,
drag, saved `view`), `tests/kernel.test.js`, `tests/szoom.test.html`, `tests/harness.html`,
`docs/design/flow-driver.md` §4.2 (the ladder's outputs and the `count` delay edge) and
§11.1 (the default loop, the chart whose look Stian sees), both charts in
`max_core/flows/max/`, `flow/examples-0.2-draft/sws-shiplift`, `studio/make_demo_run.py`,
`CLAUDE.md`, `.claude/agents/qc-falsifier.md`. `flow-graph-principle.html` is locked: a block
is a block, an edge is an edge, a `delay` edge is drawn as one (keep its mark).

DO — one function, `arrange(level)`, used by both `chart.js` and `hier.js`; saved `view`
positions still win (a user's drag is never undone).
1. Layers: longest path from the sources, as now, then **two to four sweeps** (down and up)
   of barycentre ordering within each layer, not one pass. Delay/feedback edges are ignored
   for layering (they close cycles); data edges decide.
2. Ports: order a block's input and output ports by the layer row of their partner, so
   lines leave and arrive without crossing on the block face. Declaration order only as the
   tie-break.
3. Lines: orthogonal or smooth-curve routing with a gutter between columns; a line spanning
   more than one column runs in the gutter, not through blocks. **Feedback and delay edges
   (`retry`, `escalate`, `count`) go around**: below (or above) the row band, into the
   target's input side, with the delay mark kept. No line crosses a block.
4. Nothing moves on replay: the player (`stream.js`) only recolours; layout is computed once
   per level and on explicit "arrange" (a control in `shell.js`, next to zoom), so a
   re-arrange is the user's act, not a surprise.
5. Tests (`tests/kernel.test.js` or a new `arrange.test.html`): on the default loop and the
   writer flow — zero line–block intersections; crossings count not higher than today's
   (measure and record today's number first); feedback edges never pass through the row
   band between their endpoints; a saved `view` is respected; idempotent (arrange twice =
   once). Browser tests run as today (`harness.html`).
6. Before/after screenshots of both charts in `tasks/reports/U26.md` (png under
   `studio/tests/snapshots/` or where README says).

OUT OF SCOPE
Block sizes and icons, the 3D pane, the SWS twin chart beyond "it still renders", the line
language, any engine file. If a full router does not fit the session, ship 1 + 2 + the
feedback-around rule and say so.

DONE WHEN
Both charts render with no line through a block and feedback lines around the band, tests
above pass, existing Studio tests still pass, qc-falsifier passes, report written, commit on
the branch; no push, no merge.

— Kai

## 2026-11-07 02:15 — U23 design input sent to session Cleat (record of the message)

Decide in §4.2 whether the ladder reads finding severities regardless of the reviewer's
`blocking` flag. Observation (verified later on the run-1 tape, line 84): the reviewer returned
two major findings with blocking=false and the ladder wrote `pass`. Kai's recommendation at
the time: read the worst severity across all findings of this `rev` whether or not the review
is marked blocking; minor → count; major → `on_major`; critical → human; blocking=true with
no finding = major. Flag as a decision for Stian. — Kai

**02:50, after Cleat's report:** built as H(ii), PROPOSED. Cost noted by Cleat: a run then
releases only on a review with no findings at all. Kai now recommends the softer form to
Stian: minor findings on a non-blocking review are waived; major and critical count
regardless of the flag. Stian decides. — Kai

## 2026-11-07 morning — Stian's rulings on U23 (record; ADR 0012 cites this)

Stian, 7 Nov 2026, in one line: "yes softer, start U25 and U26, yes rule 10".
- H(ii) **softer form**: major and critical findings count whatever the reviewer's `blocking`
  flag says; a minor finding on a non-blocking review is waived; a minor on a blocking review
  counts; blocking with no finding = major. Reason: a run must be able to release on a review
  that only has nits.
- Decision letter H stands (F taken in ADR 0011). `plc-code-improve` keeps `on_major: revise`.
- Rule 10 (design conformance) goes into the repo's CLAUDE.md, applied with Fairlead's
  (Grok's) points 1–3 after U23 merges.
— Kai

---
## U25b — P52 redo: the magnet is ONE PIECE per half (Kai, 2026-11-07 morning)

CORRECTION OF THE U25 BRIEF. My U25 brief said "magnet ring (segment count and segment dimensions a magnet
supplier can quote)" and "magnet mass and segment list". That was wrong, and it is my error, not Capstan's.
The SWS magnet half-rings are ONE PIECE of sintered, radially magnetised NdFeB each. Source of record:
`sws/data/sws_data_sources.md` [R29] (supplier mail 2026-10-09, status S) and its table row "Magnet half-ring
construction"; spec rev127 section 5 design-input table "One-piece sintered NdFeB half-rings"; the 23 Oct
consolidated findings §1 (`sws/fem-2d/sws_consolidated_findings_2026-10-23.md`). Stian has stopped work on this
twice. Nothing in the head is segmented; there is no steel pole shoe; the 2 mm guard is non-magnetic.
The only cut in the magnet is the A/B split plane.

DO, on the existing branch u25-sws-p52-prototype (worktree C:/Users/stian/Prosjekter-u25, NGSolve in
C:/Users/stian/Prosjekter/max/.venv, read-only; never two heavy solves at once):
1. `sws/3d/p52/head.py`: remove segmentation (n_seg, bond lines, segment rows, segment STEP parts). One magnet
   arc per half per pole, 180° less the split set-back. Keep the set-back and the yoke steel-to-steel split.
2. Re-solve the 90° sector "seams" case with the split set-back only (no bond lines) and the halves force.
   Results replace `results/p52/seams_*.json`; the segmented json files are deleted, not kept.
3. Re-decide lm. The "parallel-oriented segments −2.6 mT" risk no longer exists; the bond-line tolerance term
   goes. State the smallest thickness that meets the margin wanted, and recommend. Keep 20.5 if the stack still
   wants it; say why either way.
4. `design.md`: §1 "three changes" → two; §2 table and margin stack; §3 rewritten as "Magnet half-rings, mass,
   quote list" (one piece per half, R32.0–52.5 × 40 mm × ~180° less set-back, mass, magnetisation, the supplier
   questions that remain: achievable Br/Hcj and max one-piece size per [R29]); dimension table rows;
   §5 "Segments and split set-back" → "Split set-back". Every mention of segment/segmented/bond line gone.
   Cite [R29] where the one-piece construction is stated.
5. `tasks/reports/U25.md`: add a dated "Correction (U25b)" section on top; fix the body; question 1 to Stian
   becomes "lm 20.5 or the smaller value" without the orientation clause. `tests/test_sws_p52.py` updated.
6. 3D doc leftovers that invite the wrong assumption — fix them: `sws/3d/README.md` line ~77 ("segmentation
   … open" → only the gap width is open; magnets one piece [R29]); `sws/3d/THEORY.md` S1 row ("no magnet
   segmentation" and "Still out: … segmentation" → delete; the spec's 5–10 % budget is for the split only);
   `sws/3d/verification.md` ~349, ~592 and the 1238–1260 "Segments and split set-back" block (rename, note
   the segmented run is void); `sws/3d/reconciliation.md` row 13 ("segmentation still open" → not a feature;
   one piece per half [R29]); `sws/3d/design_inputs.md` item 3 ("one-piece … still open supplier questions" →
   one-piece is settled [R29]; Br/Hcj sheet still open). Do NOT edit anything under `sws/spec/` — the spec is
   Stian's live document; list its two leftover lines (result 3 "possibly segmented blocks"; open-items
   checklist "segmented magnet blocks") in your report for Stian to fix in the source.
7. QC: grep -rniE "segment" sws/3d/p52 must return nothing; the test passes; `build.py --only p52` clean.
   Done-lines cite the design per rule 10. Commit on the branch. Write notes to
   C:/Users/stian/agent-notes/<your-name>.md (pick a nautical name not in that folder; sign every message).
   Report to Kai: new B_rope at both corners, lm recommendation, mass, halves force, files changed, the two
   spec lines for Stian.

---
## U28 — SWS 2D rerun on the decided configuration, one pass (Kai, 2026-11-07)

WHY. Stian stopped P52 on 7 Nov: the magnets were modelled as 24 segments. The record says one sintered
piece per half-ring (data register [R29], status S). Earlier, an 8 mm soft-steel pole shoe stayed in the
2D models for the same wrong reason. Sextant's read-only audit (C:/Users/stian/agent-notes/Sextant.md,
§C and §B) lists which numbers in the specification and register still rest on the shoe model, and
which sentences still invite the wrong assumption. Stian's rulings 7 Nov: the head is fully covered under
equipment, never above 45 °C in service (sun study: shielded 43 °C); the +80 °C corner predates the
temperature simulations and stays only as a qualification reference; N52 is the grade given at no
extra cost (the 40 mm head has it); every analysis shows N52 and N48SH side by side, N40SH for
continuity; nobody selects a grade — Stian does. "I hate doing double work": redo everything in one pass.

RULE 10 (max/CLAUDE.md, rewritten today) applies: read `sws/data/sws_data_sources.md` FIRST, then spec
rev127 (render at C:/Users/stian/Prosjekter-u25/max/sws/spec/rendered/…rev127.md, read-only there), then
`sws/fem-2d/sws_consolidated_findings_2026-10-23.md` and `sws_head.py`. Your first note lists the register
rows you rest on. An assumption on an S or D input, or a conflict between this brief and the register,
is a STOP: report it to Kai before building. Where the record is silent, present options; never select.

DO, in worktree C:/Users/stian/Prosjekter-u28 (branch u28-sws-2d-decided-rerun, from main 643e306),
python from C:/Users/stian/Prosjekter/max/.venv (read-only venv). 2D only; no 3D solves (U25b owns the
machine's heavy solves). Do not edit anything under sws/spec/ except the new redline file below.
1. Rerun on `sws_head.py` (decided configuration: one-piece radially magnetised half-rings, 2 mm
   non-magnetic guard, no shoe, 40 mm magnets, 100 mm spacing, 12 mm yoke rule) every number Sextant §C
   says still rests on a t_shoe = 8 module: spec result 1 table, result 6 forces and stray field, result 7
   mass table, result 9 universal-head map, the spacing-floor trend (l.173), register row "~40 mT
   background" (l.209). Corners: −40 °C and +45 °C as the service corners; +80 °C as one reference row.
   Grades: N52 (Br min 1.42 T, [R4]), N48SH (1.36), N40SH (1.25) side by side. Demagnetisation (knee)
   check per grade at 45, 60 and 80 °C with the register's Hcj and alpha (status A; say so) on the 52 mm
   rope and the 40 mm rope in the shared head — this re-examines the register row that excluded N52.
2. Deliverable: `sws/fem-2d/sws_decided_rerun_2026-11-07.md` — a before/after table per spec result
   (old shoe value | decided value at +80 | at +45 | per grade | source script and json), figures under
   `sws/data/figures/`, data json under `sws/data/`. Proposed replacement rows for the register, written as
   rows (not applied). Every number with its source; nothing assumed without a tag.
3. Legacy modules: `sws_axi_head.py`, `_lite`, `_wire`, `_guard`, `sws_fig_abstraction.py`,
   `sws_femm_axi.py` get a two-line header "SUPERSEDED 2026-11-07: steel-shoe geometry, kept for
   reproduction of the pre-23-Oct sweeps only; the decided model is sws_head.py". Regression test T2
   must still pass. The concept figure from `sws_fig_abstraction.py` on the site: re-draw it from the
   decided configuration (one-piece half-rings, guard, no shoe) and say which page uses it.
4. `sws/spec/REDLINE_2026-11-07.md`: the leftover sentences from Sextant §B, one row each: spec line |
   current text | proposed text | reason. Stian applies it in the live document. Include "segmented magnet
   blocks" (l.474), the shoe wording, 17.8 vs 19.1, the 200 mm head, l.232, "N52 excluded" (now: open,
   pending supplier Hcj), "+80 costs 0.01 T", and the temperature basis (fully covered head, 45 °C).
5. Read U25b's `sws/3d/p52/grades.py` on the u25 worktree if it exists (read-only) so the 2D and 3D grade
   tables use the same Br/Hcj inputs; note any difference.
6. QC per rule 10: a separate subagent checks the report against the register before you hand back.
   Tests pass; commit on the branch; `tasks/TASKS.md` entry U28 with "Done when" citing the record
   (spec rev127 §5 results 5–10 and the register). Notes to C:/Users/stian/agent-notes/<name>.md, nautical
   name not in that folder, sign every message. Report to Kai under 40 lines: the before/after headline
   numbers, the knee result per grade at 45 °C, files, commit, anything that needed a stop.

NOT in U28 (queued after U25b, needs Stian's call on the reference defect): the 3D rerun of U16/U19
floors and fault margins at −40/+45 on the stranded rope.

### U28 — verifier fixes (Kai, 2026-11-07, applied before start; these override the text above where they differ)
a. Result 6 in 2D is gap field, Maxwell pressure and stray field only (register l.148, l.150). The side
   force per mm of eccentricity "needs 3D" (register l.149) and is NOT redone here; say so in the table.
b. Stian's ruling of 7 Nov (fully covered head, 45 °C service corner) SUPERSEDES register rows l.88
   (service ≤ 60 °C, sizing at −40/+80), l.151 and l.304 (lm_min at +80) pending the redline. That is not a
   conflict for the STOP rule; it is the ruling the redline will write in. Everything else in the record
   stands and the STOP rule applies to it.
c. N52 Hcj is UNRECORDED: the register has only the SH/H letter minima (l.181). The 0.88 MA/m lives only
   in sws_head.py l.47 (status A). Use it tagged "A, sws_head.py, unrecorded; supplier sheet requested via
   Henrik", never as "the register's". Same tag on alpha(Hcj).
d. Magnet thickness basis: show BOTH — (i) the record's lm (19.1 × 40 for the shared head, 17.2 for the
   dedicated 40, register l.306/l.305, sized at +80) evaluated at +45, and (ii) lm_min re-sized at +45 per
   grade. Stian selects. Result 1 table: primary criterion the decided rule, 1.92 T at the hard-wire corner
   (register l.304); keep the old 2.00 T at 25 °C row only as the "before" column.
e. Yoke: the flux rule (register l.154, l.303), which gives 12.0 mm on the Ø60 shared head and 8.5 mm on
   the dedicated 40 (l.305). Not "12 mm" on every head.
f. 43 °C shielded / 46 semi / 55 and 64 unshielded come from sws/due-diligence/sws_sun_exposure_findings.md
   l.38–40, not from the register. Cite the file. "24 segments" in WHY is narrative, not record.
Also: sws_head.DECIDED (17.8 × 40) is stale (Sextant §B); do not use it as the decided head; use the
register's lm per head. TASKS.md has no U28 entry yet: you write it.

## U29 — merge U25b and U28 to main, rebuild the page, figures over numbers (Kai, 7 Nov evening)

Stian, 7 Nov 20:xx: "merge both branches and rebuild the webpage, and please show me in figures not
numbers, if there are more than a few, figures tell much more for the human eye than numbers."
Later: external Grok review, first paper draft with MAx, then a management version. First the SWS
state must be safe to hand to peer review.

Record (rule 10, read first): spec rev127 render `sws/spec/rendered/…rev127.md`, data register
`sws/data/sws_data_sources.md` ([R29] one-piece half-rings l.67/l.153; [R4] Br; l.130 alpha(Hcj);
l.182 knee 0.8 Hcj), and the two unit documents: `sws/3d/p52/design.md` (U25b) and
`sws/fem-2d/sws_decided_rerun_2026-11-07.md` (U28, with `sws/spec/REDLINE_2026-11-07.md` and the
proposed register rows §11). Rulings 7 Nov: head fully covered, service −40/+45 °C, +80 °C reference
only; N52, N48SH, N40SH side by side; NO grade, thickness or head is selected by any agent. Stian said
"the magnet is N52, we can however choose what we want": that is a leaning, not a ruling. Present all
three; N52 open pending the supplier Hcj sheet. Do not edit `sws/spec/*` or the register (Stian applies
the redline and rows himself).

Worktree: `C:/Users/stian/Prosjekter-u29/max`, branch `u29-merge-page` from main (643e306).

1. Merge `u28-sws-2d-decided-rerun` (fast-forward from 643e306) then `u25-sws-p52-prototype`
   (merge-base 26b156b; main has moved 230 files since; `git merge-tree` shows CONFLICT in
   `.gitignore` and `pyproject.toml`, no other overlap). Resolve those two by keeping both sides'
   entries, show the resolution in the report; anything else resolved by hand goes in the report too.
   U28 already carries a two-line header on six modules (`sws_axi_head.py`, `_lite`, `_wire`,
   `_guard`, `sws_fig_abstraction.py`, `sws_femm_axi.py`): "SUPERSEDED 2026-11-07: steel-shoe
   geometry, kept for reproduction of the pre-23-Oct sweeps only; the decided model is sws_head.py".
   Put that same wording on `sws_shoe_sweep.py`, `sws_guard_sweep.py`, `sws_final_config.py`,
   `sws_guard_config_table.py`, `sws_rope_size_map.py`, `sws_temp60.py` (all sws/fem-2d), and a top
   note of the same kind on `sws/fem-2d/sws_consolidated_findings_2026-10-23.md` (l.75 "N52
   excluded" is superseded by the rerun: N52 open at +45 °C pending the supplier Hcj),
   `sws_axi_findings.md`, `sws_guard_findings.md`, `sws_review_2026-10-23_findings.md` (fem-2d),
   `sws/fem-2d/MANIFEST.md` (arrives with the U25 merge) and
   `sws/due-diligence/briefs/sws_carrier_brief.md`. Historical deltas stay as they are. Do not
   delete files.
2. Figures. Stian reads figures, not tables. Load the `dataviz` skill before plotting (one palette,
   readable at A4 print, light background, labelled axes, grade colours consistent across all figures).
   Make under `sws/figures/decided/` (matplotlib, scripts committed, png committed):
   a. `thickness_by_grade.png` — magnet thickness per grade: 3D at +45 °C with the 2.2 mT margin
      (16.73 / 17.45 / 19.02 mm), 2D no margin (15.84 / 16.58 / 18.15), record 19.1 mm and the drawn
      20.5 mm N40SH baseline as reference lines; caption states every bar is conditional on the
      B_rope reading of EN 12927 §14 (open).
   b. `knee_exposure.png` — volume beyond the knee vs temperature, −40…+80 °C, three grades, three panels
      (52 mm rope, 40 mm rope, empty head), 1 % criterion line, shaded service band −40/+45 and the
      sun-study bands (shielded 43, semi 46, unshielded 55/64 °C from
      `sws/due-diligence/sws_sun_exposure_findings.md` l.38–40). Data: `sws/3d/results/p52/envelope.json` rows[] (9 = 3 grades × 52 mm / 40 mm / empty;
      keys T_C −40…+80 in 5 K steps, frac_beyond_knee, T_cross_C) is the sweep; U28's
      `sws/data/decided_rerun.json` demag.rows[] (t_c 45/60/80) and checks.empty.rows[] are points to
      overlay on it; if the two units differ (22 % vs 31 % at 45 °C, 40 mm
      rope) show both and say why in the caption: both are 2D screenings; the gap is the thickness
      (3D sizes 16.72 mm on the stranded rope with +2.2 mT, 2D sizes 15.84 mm with no margin; rerun
      l.274–278). The yoke rule accounts only for the 0.09 mm between the two 2D sizings (l.269–273).
      Add the dedicated 40 mm head (bore 48, N52 14.86 mm: 11 % beyond at 45 °C, rerun l.237) as a
      fourth trace or panel if the data allows; the empty-head trace is marked "direction expected,
      implementation not independently verified" (design.md l.84).
   c. `n52_hcj_threshold.png` — what the supplier's N52 Hcj at 20 °C must be for ≤ 1 % beyond the knee
      at 45 °C: 0.88 assumed (A, sws_head.py / 23 Oct consolidated findings, not in the register),
      ≈ 0.96 needed with the 40 mm rope, ≈ 1.19 empty head (screening estimate, U28 l.48, l.211–215).
      Reference ticks for the letter classes as sws_head.py carries them (H 1.35, SH 1.59 MA/m) and,
      labelled "catalogue convention, not in the record", M ≈ 1.11.
   d. `head_concept.png` — reuse/extend `sws_concept_decided.png`: one-piece half-rings [R29], 2 mm
      guard, no shoe, yoke, A/B split with 0.5 mm set-back, three thickness options drawn to scale.
   e. `b_rope_margin.png` — B_rope for each grade and thickness at −40/+45/+60/+80 °C against the
      1.92 T floor and 2.30 T ceiling: 2D full set in `decided_rerun.json` heads.rows[]
      (head/grade/basis/lm/wire/t_c/B_rope); 3D points in `sws/3d/results/p52/summary.json`
      grades.rows[] (B_hard45_at_lm, B_easy_m40_at_hi, B_hard80_at_lm) and cases[].B_rope_unbounded.
   f. `mass_vs_spacing.png` and `rope_size_map.png`: U28 already has `sws/data/figures/
      sws_decided_spacing.png` and `sws_decided_rope_size.png`; reuse, restyle only if cheap.
      `fig_envelope.png` lives at `sws/3d/p52/`; `sws_concept_decided.png` in `sws/data/figures/`.
   g. `record_status.png` — one page: what is updated (branches merged, design docs, rerun, figures,
      tests) vs not (live spec: 24-row redline waiting; register: 15 rows waiting; STEP at 20.5
      N40SH until selection; supplier Hcj sheet; B_rope vs B_wire call). Simple traffic-light table as
      a figure.
   Every figure: caption in a `sws/figures/decided/README.md` with the source file and commit.
3. STEP: `python sws/3d/p52/head.py --lm 16.73 --out sws/3d/out/p52` (and 17.45, 19.02; geometry is
   grade-independent, head.py l.248–274; OCC solid write, needs netgen.occ from
   `C:/Users/stian/Prosjekter/max/.venv`, no FE solve, no memory issue) in addition to the existing
   20.5 and 19.1 files. Output is gitignored; list files and sizes in the report.
4. Page: `docs/sws/build.py` — add `sws/3d/p52/design.md`, `sws/fem-2d/sws_decided_rerun_2026-11-07.md`,
   `sws/spec/REDLINE_2026-11-07.md` and the new figure README as PARTS near the top; rewrite ABSTRACT /
   KEY / FINDINGS to the 7 Nov state (one-piece magnets, −40/+45 service with +80 reference, three
   grades side by side, N52 open on Hcj, thicknesses conditional on B_rope vs B_wire, head fully
   covered); embed the new figures above the old ones; label the old shoe figures
   (`shoe_sweep.png`, `sws_fig_abstraction.png`, `guard_sweep.png`, `sws_head_sizes.png`) "legacy,
   steel-shoe model, superseded 7 Nov" where they appear; the spec render stays as is but the redline
   sits right after it with a one-line pointer. `python docs/sws/build.py --check` must pass. Do not
   regenerate the mp4.
5. Tests: `tests/test_sws_p52.py`, `tests/test_sws_report.py`, `sws/fem-2d/sws_head_test.py` green.
   `grep -rn "segment" sws/3d/p52 sws/fem-2d/sws_decided_rerun*` returns only wire-defect segments
   or [R29] one-piece statements.
6. Report `tasks/reports/U29.md`: what was merged, every file marked superseded, the figure list with
   sources, STEP files, page diff summary, tests, and "Needs Stian": grade; thickness basis (record
   19.1 / 3D +45 / 2D +45); B_rope vs B_wire; apply redline + rows; headline fault. TASKS.md entry U29
   with Design line citing design.md + rerun md and the rule-10 Done line. First note in
   `C:/Users/stian/agent-notes/<your-name>.md` lists the register rows you rest on (rule 10). Pick a
   nautical name not already used in that folder (taken: Bight, Buoy, Sextant, Bollard, Bosun,
   Capstan, Cleat, Fathom, Gimbal, Gunwale, Hawser, Keelson, Windlass). TASKS.md entry lines are
   `- **Design:**` and `- **Done when:**` as in U27 (l.162–163). If the `dataviz` skill is not listed
   in your session, follow its intent: one palette, grade colours fixed across figures, light
   background, labelled axes, readable printed on A4.
7. QC: `qc-falsifier` subagent on conformance to the record (not only the tests) before every commit.
   Then stop at the branch, do NOT merge to main or push; Kai runs the Fable check and tells Stian.

Timebox: 3 hours. If any step needs a selection (grade, thickness) stop and write the options; never
select. — Kai

(Brief checked by verifier-brief29, 7 Nov evening; all five corrections applied. — Kai)

### U29 addendum (Kai, 7 Nov late): Henrik's P40 against our 40 mm head; notch re-run

Stian: "all the sizes of Henrik's first design and cad drawings have been delivered so we know where
he ended at 40 mm rope, so we need to plot these together also to see where his lay and where our
40 mm is in sizes. And then we need to explain the difference. Also with the new magnets is it smart
to run a test with the circular cut-out that gave him better results."

Record for P40 (Henrik's Ø40 prototype), all from `tasks/reports/U17.md` §0 on branch
u17-bz-radius-henrik (worktree C:/Users/stian/Prosjekter-u17/max; drawings
C:/Users/stian/Prosjekter/new/henrik_2026-11-03/ sd00039125 YOKE, sd00037347 RING MAGNET):
yoke Ø102/Ø86 × 105 mm S235JR 0.89 kg (per half or whole: drawing silent), magnet seats Ø88 × 20,
1 mm steel shoulder at r 43, no guard; magnets R24–R44 × 20 mm (20 radial × 20 axial), N42, radial,
half ring, 0.37 kg each, 4 pieces = 1.48 kg (derived); pole gap 65 mm; outside groove 10 × 2 mm at
mid-length (DETAIL A); Br 1.28 T N42 [UNVERIFIED]; U17 computed B_rope 1.9936 T without and 1.9893 T
with the groove (U17.md l.47–48), 1.938–2.039 over the register corners. No register row records P40.
Our dedicated 40 mm head (U28 rerun l.63–65, l.222–226, l.175): bore 48, 2 mm guard, 40 mm axial,
100 mm spacing; lm_min(+45) N52 14.86 / N48SH 15.40 / N40SH 16.53 mm; magnet 1.87 / 1.96 / 2.14 kg;
yoke 8.5–8.9 mm, 3.59 kg; magnetics 5.7–5.9 kg.

8. Figure h `p40_vs_ours_40mm.png`: two cross-sections to the same scale (P40 as drawn; our dedicated
   40 at the three lm_min(+45), one-piece half-rings, guard, no shoulder) and a bar panel: magnet mass,
   yoke mass, pole spacing, axial magnet length, radial thickness, B_rope (U17's P40 values vs ours at
   +45). Caption explains the difference, each cause from the record: 40 vs 20 mm axial magnets, 100
   vs 65 mm pole spacing (spec's choice for the sensor-plane field), 2 mm guard vs 1 mm steel
   shoulder (shoulder costs 3.5–4.1 mT, design.md l.129), grade N42 vs the three. Tag P40 values as
   drawing-derived (A) and Br N42 [UNVERIFIED]. Per-half magnet mass shown too (Stian expects ≈ 0.3–0.5
   kg per half).
9. Notch: U17 already ran Henrik's real groove on the one-piece P40 (−0.2 % B_rope, signals within
   ±0.7 %, no gain; U17.md l.45–61) — nothing there is invalidated. The only notch number from the
   segmented runs is P52's "notch cost 0.19 mT, U25 unchanged" (design.md l.107–128). Re-run that one
   delta on the one-piece P52 (2D on sws_head.py if 3D is too heavy; say which) and state it in
   design.md and the report. Do not start a new notch campaign; Henrik's own measured with/without
   comparison is still requested (issue #2 draft).
10. Explanation section: in the report and on the page, one short section "Where Henrik's P40 lies
    against our 40 mm head and why" with figure h. No selection; "optimal sizes" means the three
    lm_min(+45) rows with their yoke walls, stated as conditional on B_rope vs B_wire.
— Kai

## U30 — SWS complete peer read, and the paper's input fields and knowledge bases (Kai, 8 Nov 00:xx)

Stian, 8 Nov just after midnight: "it is time for the SWS review complete first peer to read as total,
and suggest input fields and knowledge bases for the agents to create the paper, and then we will peer
to peer the paper with Grok, GPT highest, Fable and any other models I have available in Cursor. Then
we will have a material of suggestions for MAx."

Reviewer: Fable, on this machine only (nothing leaves). Read-only on the SWS state; writes one document.
Worktree C:/Users/stian/Prosjekter-u30/max, branch u30-sws-peer-read from main ff20112.

Read as a total, in this order, the way a peer reviewer with the code would: the page
`docs/sws/index.html` (or its sources via `docs/sws/build.py` PARTS), the record (spec render
`sws/spec/rendered/…rev127.md`, redline `sws/spec/REDLINE_2026-11-07.md`, register
`sws/data/sws_data_sources.md` with U28's proposed rows in `sws/fem-2d/sws_decided_rerun_2026-11-07.md`
§11), the two unit documents (`sws/3d/p52/design.md`, the rerun md), the figures
`sws/figures/decided/` with README, the models (`sws/fem-2d/sws_head.py`, `sws_decided_rerun*.py`,
`sws/3d/p52/head.py`, `run_p52.py`, `sws/3d/rope3d.py`, stage files), result json
(`sws/3d/results/p52/*.json`, `sws/data/decided_rerun.json`), the due-diligence folder (sun study,
stage 1), the unit reports `tasks/reports/U07/U08/U16/U19/U25/U29.md` (U17 has no report: its record
is `C:/Users/stian/agent-notes/u17-bz-radius-henrik.md` and commit e3bfbd1 on that branch, worktree
C:/Users/stian/Prosjekter-u17/max with `tasks/reports/U17.md` there; U28's document is the rerun md,
TASKS.md l.165), and the rulings in `C:/Users/stian/secretary/log/2026-11-07.md`: head fully covered
(l.168), ≤ 45 °C service (l.139), +80 °C corner predates the temperature simulations and is reference
only (l.139–140; TASKS.md l.174), N52 given at no cost (l.140), N52 and N48SH side by side so Stian
selects, "if one, N52" as his open preference not a selection (l.141), the third grade N40SH from
l.174/285, no selection by agents (l.141–142, l.179), one-piece magnets [R29] (l.123–127; register
l.67, l.153).

Deliverable: `docs/paper/peer_read_2026-11-08.md`, four parts, under 400 lines, every claim cited
file:line:
A. Peer review of the whole: what is established (with the evidence chain), what is asserted without
   evidence, inconsistencies between documents (numbers, statuses, wording), what a reviewer would
   reject or ask for, and where the one-piece correction or the 45 °C ruling has not yet reached. Rank
   by what would stop a paper. Include the B_rope vs B_wire question and the N52 Hcj dependence as
   the two largest open inputs, if you agree; say if you do not.
B. Paper outline for a peer-reviewed engineering paper (target journal type: NDT / wire-rope
   inspection; length target for Stian to trim later): sections, which figure goes where, which
   results are claims and which are preliminary, what must be stated as open. The paper must carry:
   fully covered head, real temperature basis, all three grades (N52, N48SH, N40SH) side by side, where demagnetisation shows
   first, supplier sheet as open input, the P40 comparison, the fault-detection results (U16/U19)
   with the stranded-rope floor.
C. Input fields for the MAx paper flow (the document-flow unit U24 is not yet written; the engine
   runs a chart, see docs/decisions/0011 and `flow/chart.schema.json`, draft 0.2 beside it): for each
   field its name, type, source file, status (S/D/C/M/A/U, register l.7–11), and who fills it (record /
   Stian / supplier). Group: geometry, materials, temperatures, floors and ceilings, rope and wire
   definitions, fault cases, figures, open calls. This is what the writer agent is allowed to use
   and nothing else (rule 10).
D. Knowledge bases: named folders or file sets the writer and reviewer agents read, each with scope,
   what it must NOT contain (superseded shoe work unless marked, identifiers), and its freshness
   rule (rebuilt page before each run). Include the external standards and supplier data as KBs with
   their status (EN 12927 §14: reading open; supplier N52/N48SH sheet: requested).
Then a short "For Stian" list: decisions needed before the paper starts, max 6 items, one line each.

Also produce `docs/paper/review_pack_manifest.txt`: the exact file list for the later masked bundle
to the outside reviewers (page, figures, code, json, reports, rendered spec md, no docx/pdf), one
path per line, so Kai can build the bundle from it.

Rules: rule 10 (read the record, no assumptions, no selection; a departure goes under "For Stian").
No edits outside docs/paper/. QC: a qc-falsifier subagent checks the document's citations against
the files before the commit. Commit on the branch; do not merge or push. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (taken: Bight, Buoy, Sextant, Bollard, Bosun, Capstan,
Cleat, Fathom, Gimbal, Gunwale, Hawser, Keelson, Windlass, Halyard, Compass, Quill, Fairlead).
Timebox 2.5 hours. — Kai
(Brief checked by verifier-brief30; three path fixes, status letters, rulings cited by line. — Kai)

## U31 — apply the rulings, answer Stian's five questions, build the Grok pack (Kai, 8 Nov 01:xx)

Stian, 8 Nov ~01:15, on the U30 peer read: "for 40mm it is one wire, for 52mm it is 2 wires, that is the
rule"; "The initial settings of temperature of -40 to +80 should be there, then the analytical test of
temperature leads us to the temperature that we can use grade N52"; "40mm 52mm and for both, with the
2-3 different magnet types and yokes should all be in the report, and the final evaluation should give
room for management to choose, but we should of course lead them where the numbers show us safest";
"You fix these items first then push"; "There need not be stated anything else than optimizing a TMR
sensor for detection according to [the rulebase]. Why force it?"; "For the 3D part we can select the
one we feel most likely, and we can even run for the others in the appendix. Are we able to do it now
or are we still waiting for RAM for the final runs of the 3D?"; "we go with more than one, the others in
the appendix. The task is to find the optimal area for our wire ropes in our working conditions. It is
not forced ±80"; "Put these questions to the team and show me all results, including your own. Then
give me a brief for Grok with the accounts ready in a note from the agentic team."

Builder: Opus. Worktree C:/Users/stian/Prosjekter-u31/max, branch u31-rulings-and-pack from main
b58faf2. Read first: rule 10 (max/CLAUDE.md l.60–71), the peer read `docs/paper/peer_read_2026-11-08.md`
(its "For Stian" list A.2 is what this unit closes), the redline `sws/spec/REDLINE_2026-11-07.md`, the
rerun §11 `sws/fem-2d/sws_decided_rerun_2026-11-07.md` l.279–297, the register
`sws/data/sws_data_sources.md` (status letters l.7–11), the 7 Nov rulings
`C:/Users/stian/secretary/log/2026-11-07.md` l.139–143 and l.168–169, and this brief.

### Part A — apply what is now ruled (the record first, then everything else)

A1. Register. Apply the 15 rows of rerun §11 to `sws/data/sws_data_sources.md` the way the register
    already marks superseded rows (keep the old row, mark it superseded with date and pointer; the new
    row cites its source). Adjust the temperature wording to Stian's 8 Nov framing: the −40 / +80 °C
    envelope of spec rev127 stays in the register as the *initial sizing basis* (status D, spec); the
    knee screening and the sun study lead to the service case; the service ruling is ≤ 45 °C, head
    fully covered (D, Stian 7 Nov, log l.139/l.168); +80 °C stays as a qualification reference row. Add
    rows for the 8 Nov rulings, status D, source "Stian, 2026-11-08 (kai.md U31)":
    (i)  Acceptance fault per rope size: 40 mm rope one broken wire; 52 mm rope two broken wires. Put
         beside it, as the register's own note: spec rev127 render l.52, l.262, l.425, l.429 read
         EN 12927 §14 as two inner wires below 0.5 % section loss at every rope size and carry no
         per-size rule; U16 l.15/l.57 gives 0.62 % for two hidden wires and l.106–107 0.32 % for one
         hidden wire on the 52 mm rope. Record the conflict; do not resolve it (Part B Q4 asks).
    (ii) Report scope: 40 mm head, 52 mm head and the shared head, each with N52 / N48SH / N40SH and
         its yoke, all in the report; the final evaluation presents the options and leads to the
         safest by the numbers; management chooses.
    (iii) Temperature method for the paper: start from the −40 / +80 °C envelope, show the
         demagnetisation screening, check the actual temperatures (sun study, covered head), state
         the service case; carry more than one candidate, the others in the appendix. "Not forced ±80."
    (iv) 3D main case: for the full 3D runs the team selects the most likely case for the main text
         and runs the others for the appendix as time allows (Stian, 8 Nov). This is a choice of which
         case to run first, not the design selection, which stays with management.
A2. Spec. Apply the 24 redline rows to the specification as **rev128**. Preferred: edit the rev127
    .docx (`sws/spec/SWS_HW_Design_Input_Specification_rev127_2026-10-30.docx`) with python-docx into
    `…rev128_2026-11-08.docx`, paragraph by paragraph, keep the tables intact, re-render with
    `sws/spec/render_spec.py` and diff the rev128 render against the rev127 render: only the redline
    rows, a revision-history line and the new rows (below) may differ. If a row cannot be placed
    cleanly in the docx, apply it in the rendered Markdown rev128 instead and list it under "Needs
    Stian" so he does it in Word. If the docx route breaks tables or images, stop that route, deliver
    rev128 as Markdown only, and say so in one line. Wording changes to the redline before applying:
    rows 2, 18, 19 — keep the −40 / +80 °C envelope as the initial sizing basis of the analysis and
    state the ≤ 45 °C service case as what the temperature study leads to (A1 iii), not as a
    replacement. Add rows 25–27 to the redline file for the 8 Nov rulings (A1 i–iii; row 25 is the
    acceptance-per-size rule, with the < 0.5 % conflict stated in the "Reason" column). Then mark the
    redline file and rerun §11 heading "APPLIED 2026-11-08 in rev128 / register", keep both files.
    Never type a personal name or a drawing number into the spec or the register
    (`C:/Users/stian/max-private/identifiers.yaml` is the list; do not open, copy or print it; the
    existing text uses roles).
A3. U17 onto main. Merge branch `u17-bz-radius-henrik` (one commit 602c6b3 on base 6ec64cd, 10 added
    files incl. `tasks/reports/U17.md`, `sws/3d/figures/bz_radius_sweep_P40.png`) into the unit
    branch. Expect no conflicts (additions only); if there are, report, do not force. Add the U17 line
    to `tasks/TASKS.md` if missing. Check that `tasks/reports/U17.md` carries no personal name (the
    branch name does; that is fine, it is not in the bundle).
A4. `sws/fem-2d/sws_head.py` DECIDED = 17.8 is stale (peer read item 7). Set it to the record's
    19.1 with a comment citing spec rev128 result 10 and the register row "Record lm", or mark the
    constant superseded if the test gate depends on it. Run `sws_head_test.py`.
A5. Rebuild: `python docs/sws/build.py --check` (NGSolve venv `C:/Users/stian/Prosjekter/max/.venv`
    has markdown), `tests/test_sws_report.py`. The page must show rev128 and the applied rows.

### Part B — Stian's five questions, answered from the record (`docs/paper/questions_2026-11-08.md`)

Each answer: the record's numbers with file:line, then "the team's view" labelled as a view. Short.
Q1. B_rope vs B_wire. Stian asks why force the reading: can the paper state only that it optimises a
    TMR head for detection per the rulebase (EN 12927 §14 + the spec) and show both readings? Give the
    thickness and mass per grade and head at +45 °C under the steel-mean reading (3D offset ~15–17 mT,
    `sws/3d/p52/design.md` §6, U25b) beside the B_rope sizing; say which candidates, if any, fall under
    1.92 T at 45 °C under the steel-mean reading at the 3D-sized thickness; say whether the 3D-run
    numbers already exist for this or need a run (Q2).
Q2. 3D "final runs" and RAM. Facts: this machine has 62 GB RAM and a 64 GB page file (set 28 Oct,
    U08 l.42–44); the heaviest 3D solve so far, the fault half-space at 2.09 M unknowns, ran in 345 +
    318 s with one heavy solve at a time (U25 l.88–96). List every 3D run still outstanding for the
    report (fault cases U16/U19 on the one-piece P52 at −40 / +45 °C; the dedicated Ø48 head in 3D at
    +45 °C for each grade; N52 and N48SH fault signal in 3D; anything else the peer read names) with
    unknowns, wall time and the total in hours. State the team's pick of the most likely main-text
    case with its reasons (A1 iv authorises this pick), and which runs go to the appendix. Answer the
    question in one line first: can they run now, yes or no.
Q3. Paper structure as Stian puts it: envelope −40 / +80 → demagnetisation screening → actual
    temperatures → service case → more than one candidate, others in the appendix; main text short.
    Does the team agree; what in the record is missing to write it that way; rough page count main
    text vs appendix against the peer read's outline (part B of the peer read).
Q4. Acceptance fault. Stian's rule: 40 mm one wire, 52 mm two wires; he asks whether the spec says so.
    Report what the spec and the register say (A1 i); compute section loss for one and two wires on
    the 40 mm rope and the 52 mm rope with the register's wire diameters and constructions (which
    wires: outer-strand inner wire as U16, and the inner-rope wire); say whether Stian's rule stays
    under 0.5 % on each rope; say which U16/U19 rows become the acceptance case for each rope and
    what the margins then are at 3 / 5 mm. Do not change the rule; it is his.
Q5. Safest by the numbers today. For each head (dedicated 40, shared 40 + 52, bore 65 if relevant) and
    grade: floor margin at 45 °C (both readings), knee exposure at 45 °C and at the +80 reference,
    mass, open inputs that could move it. One figure (bars or a dot plot, `sws/figures/decided/`
    style, matplotlib, no names) and one short table. End with "the team's view: … leads to …",
    labelled as a view. No selection.

### Part C — the Grok pack (for Stian to upload; nothing leaves this machine from the unit)

C1. Update `docs/paper/review_pack_manifest.txt`: add rev128 render, the applied register, U17 report
    and figure, questions md, the Grok brief; drop nothing else. No docx, no pdf, nothing from
    `secretary/` or `agent-notes/`.
C2. Build the masked bundle outside the repo: `C:/Users/stian/grok_pack_2026-11-08/` with the files
    at their repo paths, run through `C:/Users/stian/max-private/tools/rewrite_names.py <src> <dst>`
    (two positional paths; it reads identifiers.yaml itself; never open or print that file), then
    scan the result for every identifier (use the tool's scan mode if it has one, else grep the
    masked tree against the roles the tool writes) — the bundle ships only at 0 hits. Zip it:
    `C:/Users/stian/grok_pack_2026-11-08.zip`. Report the size and file count.
C3. Write `docs/paper/grok_brief_2026-11-08.md` (goes into the pack, masked): the reviewer's role
    (thorough peer reviewer with the code, NDT / wire-rope magnetics), what the pack holds and the
    reading order (page `docs/sws/index.html` first, then record, unit documents, code, json), what
    is settled and what is open (from the peer read A.1 and A.2, and Part B), the five questions, and
    the output we want: ranked findings with file:line, what would stop a paper, errors in the
    physics or the FE, suggested input fields and knowledge bases for a writer agent, in Markdown.
    Add the "note from the agentic team": one page, the account of the work — units U07–U30 in one
    line each with what each established, the rulings and their dates (no names: "the owner"), the
    status letters, and the honest list of what is assumption. Sign the note "— the MAx team" and the
    brief "— Kai".

### Rules and delivery

Rule 10 throughout: the record is spec + register; A1/A2 *apply rulings Stian has given* (cite him and
the date in every changed row); nothing else in the record changes; a number the record lacks is A and
says so; no selection anywhere except the A1 iv run order, which is labelled as such. A verifier
subagent (qc-falsifier) checks Part A against the redline and rerun §11 row by row, Part B against the
files it cites, and the pack for identifiers before the commit. Report `tasks/reports/U31.md`: what
changed, row counts, the diff summary rev127 → rev128, the five answers in five lines, pack size,
"Needs Stian" (max 6). Commit on the branch; do not merge or push (Kai merges, pushes to D:, and Fable-
checks before anything goes to GitHub). Notes in `C:/Users/stian/agent-notes/<nautical name>.md` (taken:
Bight, Buoy, Sextant, Bollard, Bosun, Capstan, Cleat, Fathom, Gimbal, Gunwale, Hawser, Keelson,
Windlass, Halyard, Binnacle, Compass, Quill, Fairlead). Timebox 4 hours; if A2's docx route eats more
than 1 hour, fall back to Markdown rev128. — Kai

### U31 addendum — verifier-brief31 corrections (Kai, 8 Nov 01:4x). These override the text above.

- Names. The register writes "owner" and never a name. In every row, document and figure U31 writes:
  source "owner ruling, 2026-11-08" (and "owner ruling, 2026-11-07" for the 7 Nov rows); when applying
  rerun §11 and redline rows 5, 16, 23, replace the names they carry with "the owner" / "the head
  designer". `tasks/reports/U17.md` carries the head designer's first name 11 times: replace with "the
  head designer" in the unit branch as part of A3 (the commit message of 602c6b3 stays as history).
- A2. python-docx is not installed anywhere on this machine and the NGSolve venv is read-only. Try once:
  a scratch venv in the worktree (`python -m venv .venv-docx; pip install python-docx`), 10 minutes
  at most. If it fails, deliver rev128 as Markdown
  (`sws/spec/rendered/SWS_HW_Design_Input_Specification_rev128.md`, built from the rev127 render) and
  put "apply rev128 to the Word file" under Needs Stian. The redline header "For Stian to apply in the
  live document" is overridden by the owner's 8 Nov "you fix these items first": say so in the header.
  Apply the envelope reframing to redline rows 1 and 23 as well as 2, 18, 19.
- A3. U17 branch: 8 files added, 2 modified (`sws/3d/README.md`, `sws/3d/build.py`); merge-tree is
  clean.
- A4. Cite rev127 render l.241 (result 10) and the applied register row "Record lm". `DECIDED` takes
  17.8 from `HeadConfig`'s default lm (sws_head.py l.85, l.144); set `DECIDED = HeadConfig(lm=19.1)` or
  the default, with the citation. `sws_head_test.py` passes lm explicitly and does not depend on it;
  `sws_guard_config_table.py` (superseded) and sws_head.py l.258 do use it; check they still run.
- Q1. The 3D offset is "about 17 mT": `sws/3d/p52/design.md` l.132, l.238, l.278; the unit report is
  `tasks/reports/U25.md` (there is no U25b report).
- Q2. Heaviest 3D solve so far: 2.66 M unknowns (3D-A finest level, U08 l.44); the 2.09 M fault
  half-space (U25 l.95) is the heaviest fault solve. RAM is 61.7 GB measured on 8 Nov, not from the
  record; say so.
- Q4. The register holds no wire diameters (register l.100 "not held"; l.101 wires per strand 7–19 is
  A). Use U16's modelled strand (18 × 1+6, U16 l.10, status A) and label every section-loss figure A.
  Cite spec l.68 and register l.192 (sensitivity test, status U, "verify wording"). U16's margin rows
  are at +80 °C (U16 l.14); say so.
- C2. `rewrite_names.py` rewrites a **git fast-export stream**: `python -I rewrite_names.py <in.stream>
  <out.stream>`; its rules are hard-coded and it has no rule for the owner's first name and no scan
  mode. Route: commit the unit's work on the branch, `git fast-export <branch> > in.stream`, rewrite,
  `git fast-import` into a scratch repo under the scratchpad (not under any Prosjekter tree), check out,
  and copy the manifest's files from there into `C:/Users/stian/grok_pack_2026-11-08/`. Scan: write a
  short script in the scratchpad that reads `C:/Users/stian/max-private/identifiers.yaml` and prints
  **only** a count of hits per file, never a value, and run it with `python -I` over the pack; the
  pack ships only at 0 hits for every entry, including the owner's first name — which is why every
  U31 document uses roles. Do not print, copy or quote the yaml anywhere, including the notes.
— Kai

## U32 — 3D main-text runs now, appendix runs queued; acceptance ruling into the register (Kai, 8 Nov morning)

Stian, 8 Nov morning: "We use the standard. [The head designer] told me that it came to one strand in the
outer area hidden [one hidden wire of an outer strand at 40 mm], but for 52 mm the rules turn it into 2
wires. For LF? for LMA I am not sure, but we follow the rules as the minimum. If we are better, great;
worse, redesign." Earlier (01:xx): "For the 3D part we can select the one we feel most likely, and we can
even run for the others in the appendix"; "are we able to do it now?" — U31 Q2 answered yes.

Builder: Opus. Worktree C:/Users/stian/Prosjekter-u32/max, branch u32-3d-main-runs from main 130203f.
Read first: rule 10 (max/CLAUDE.md l.60–71); `docs/paper/questions_2026-11-08.md` Q2 (the run list
R1–R8, the main-text set, the authorised run order: shared Ø60 head, 52 mm rope, N52, +45 °C) and Q4;
`tasks/reports/U31.md`; `sws/3d/p52/design.md`; `sws/3d/README.md` (how runs are queued and logged,
one heavy solve at a time, logs git-ignored); the register `sws/data/sws_data_sources.md` rows added
8 Nov (l.329–350) and l.192 (sensitivity test, U, "verify wording").

A. Register, one row changed and one added, status as the convention (l.7–11), source "owner ruling,
   2026-11-08 (morning)", roles not names:
   - Replace the 8 Nov row (i) (acceptance fault per rope size) with: "Acceptance follows EN 12927 §14 as
     the minimum. Reading given to the owner by the head designer: 40 mm rope — one hidden wire of an
     outer strand; 52 mm rope — two wires. LF / LMA split: open. Design better than the minimum: fine;
     worse: redesign." Status U (said to come from [R5] via the head designer; the standard's text is
     not on file — the register has [R5] by title and [R10] as a secondary summary). Keep the note that
     U16's model gives 0.62–0.64 % for the 52 mm pair and the spec's "< 0.5 %" wording (rev128), as the
     open conflict to verify against the standard's text.
   - Check whether any file on this machine holds the standard's §14 wording (search Prosjekter*,
     Downloads, the due-diligence folder for "12927", "Chapter 14", "artificial"). You may read the
     public [R10] page (register l.36) read-only to see whether it states wire counts by rope diameter;
     cite what it says with status U. Do not send anything anywhere. If the text is not on file, write
     "Needs Stian: the standard's §14 pages" in the report.
B. 3D runs. Run the main-text set from Q2 now, in the authorised order, on the NGSolve venv
   (`C:/Users/stian/Prosjekter/max/.venv`, read-only), one heavy solve at a time, with the existing queue
   and logging conventions. Then queue the appendix runs (the rest of R1–R8) and let them run while you
   write; report what finished inside the timebox and leave the queue running with a note on how to
   read its logs. Results into the existing `sws/3d/results/` layout with json per run; update
   `sws/3d/p52/design.md` (a dated section, numbers with status C, no selection), one figure per result
   group in `sws/figures/decided/` style (figures over numbers; no names), and `docs/sws/build.py` if the
   page shows them. Every number from these runs is C; compare against the 2D values from U28 and the
   3D-sized thicknesses from U25 and state the differences. If a run cannot start (RAM, mesh, solver
   ceiling 6.2 M), say so with the log line; do not shrink the case silently.
C. Verifier subagent on the register row and on the result numbers (recompute two by re-reading json),
   then `tests/test_sws_report.py` and `python docs/sws/build.py --check`. Report `tasks/reports/U32.md`:
   runs done / running / not started with unknowns and wall time, the numbers in one table, what moved
   against 2D, Needs Stian (max 4). Commit on the branch; no merge, no push. Notes in
   `C:/Users/stian/agent-notes/<nautical name>.md` (taken: Bight, Buoy, Sextant, Bollard, Bosun, Capstan,
   Cleat, Fathom, Gimbal, Gunwale, Hawser, Keelson, Windlass, Halyard, Binnacle, Davit, Compass, Quill,
   Fairlead). Timebox 5 hours of your time; the queue may run longer. — Kai

## U33 — the peer-to-peer review round, ready to run on one command (Kai, 8 Nov morning)

Stian, 8 Nov: "you make ready the peer to peer with all agents on your end? set an Opus / Fable to set
up the CLI for Cursor? And we get the Key for Claude now also?" Line-up (02:15): outside round through
the Cursor CLI (GPT highest, Grok latest, Claude, others on the plan); our own local team, one of each:
Opus (and one lower model for interest), Codex, Fable sparingly. Policy (8 Nov): company, Siemens/TIA
Portal/WinCC Unified and sub-suppliers may be named; personal names and customer names never — dummy
names out, replaced back in MAx at output.

Builder: Opus. Worktree C:/Users/stian/Prosjekter-u33/max, branch u33-review-round from main 130203f.
Read first: `docs/paper/grok_brief_2026-11-08.md`, `docs/paper/review_pack_manifest.txt`,
`tasks/reports/U31.md` (pack and masking sections), `C:/Users/stian/agent-notes/davit.md` (masking
pass), the count-only scan scripts in the scratchpad
`C:/Users/stian/AppData/Local/Temp/claude/2a40536beb49695d/c8a54a63-c1a2-4311-8bd6-5f70b32ad736/scratchpad/packcheck/scripts/`
and `…/scratchpad/u31/`, `C:/Users/stian/max-private/tools/rewrite_names.py` (git-stream tool, keep it),
`docs/decisions/0011*` and `flow/chart.schema.json` (so the runner's output can later feed U24's
reviewer half; do not build the chart).

A. Masking tools in `C:/Users/stian/max-private/tools/` (never in the repo): `mask_tree.py <src> <dst>`
   (files → masked files, by a map), `unmask_text.py <in> <out>` (a reviewer's answer → real names
   back), `scan_tree.py <dir>` (count-only, per file and total, never prints a value). The map
   `C:/Users/stian/max-private/mask_map.yaml`: start it with the categories the policy names — personal
   names (first and full), customer names and customer sites, the user path — and leave the company and
   supplier names unmasked. You may read `identifiers.yaml` through a script only to build the map's
   personal/customer entries; never print, copy or quote its values, in notes or report. Dummy names:
   neutral and stable (e.g. "the head designer", "Customer A", "Site A"), so unmasking is a reverse lookup.
B. Runner `tools/review_round.py` in the repo (no secrets in it; keys from the environment only):
   inputs: a pack folder (default C:/Users/stian/grok_pack_2026-11-08/), a brief file, a models list in
   `tools/review_models.yaml`; for each model: send brief + the pack's `docs/paper/*.md`, the register,
   the rev128 render and the figures README (not the whole 24 MB; the html is too big for a prompt — say
   so and list what is sent), collect the answer, unmask it, write
   `docs/paper/reviews/<date>/<backend>-<model>.md` with a header (model, backend, time, what was sent).
   Backends: (1) Claude Code CLI headless (`claude -p`, `--model`), using the current login, or the API
   when `ANTHROPIC_API_KEY` is set; (2) Codex CLI at
   `C:/Users/stian/AppData/Local/OpenAI/Codex/bin/a159911ff70742e9/codex.exe` (`codex exec`, check its
   headless flags with --help); (3) Cursor CLI `agent -p --model <m>`: install with
   `irm https://cursor.com/install -useb | iex` in PowerShell if the network allows (a public installer,
   no internal data goes out); `agent login` is interactive and is the owner's step — do not attempt it;
   (4) Grok: through Cursor (`--model grok…`) or the xAI API if `XAI_API_KEY` exists; (5) a lower Claude
   model (sonnet or haiku) as the "one lower for interest". A `--dry-run` sends a ten-line dummy document
   (no internal content, written by you) and proves each backend end to end where a login exists; where
   it does not, report "not logged in / no key" per backend. **The real pack is never sent in this
   unit.** The owner runs the real round after saying go.
C. Deliver: `tasks/reports/U33.md` with the owner's three steps (Cursor login, the Claude key as a user
   environment variable, the one command for the real round), which backends passed the dry run, the
   masking map's categories (counts, no values), and Needs Stian (max 4). Verifier subagent: the tools
   never print a value; the runner never writes a key or a real name to the repo; the dry run touched no
   internal file. Commit on the branch; no merge, no push. Notes in
   `C:/Users/stian/agent-notes/<nautical name>.md` (taken list as U32 plus the U32 builder's name — check
   the folder). Timebox 3 hours. — Kai

### U32 / U33 addendum — verifier-brief32-33 corrections (Kai, 8 Nov). These override the text above.

U32:
- Queue convention: not in README. It is `verification.md` l.1279–1280, one solve at a time via
  `logs/p52_grades_queue.sh`, which is git-ignored and exists only in
  C:/Users/stian/Prosjekter-u25/max/sws/3d/logs/ — copy it into your worktree's `sws/3d/logs/` as the
  starting point (read it first; it calls run_p52.py with `|| exit 1`).
- Faults: `run_3dd.py --head P52` has no grade argument and would solve N40SH (l.118–133, l.149);
  `head.case` takes `grade=` (head.py l.176). Add the one-line pass-through (`--grade`) before R2, test
  it on a coarse level, and note it in the report.
- Run points (not chosen thicknesses, label them so): the Q2 pick is "the shared Ø60 head on the 52 mm
  rope, N52, +45 °C service corner, hard wire, at its 3D-sized lm 16.73 mm" (Q2 l.77–79). For the
  B_wire-sized point in R1 use the 2D BW column from Q1 l.32 (17.29 / 18.09 / 19.83 mm, C by script),
  report the B_wire the 3D run reaches, and bracket to 1.92 T only if the appendix time allows.
- Comparisons: the 2D values are `sws/fem-2d/sws_decided_rerun_2026-11-07.md` and register l.334–335
  (there is no U28 report); the 3D-sized thicknesses are U25b's, `sws/3d/verification.md` l.1274–1284
  and `design.md` §2. Results: `sws/3d/results/` (3dd_*.json) and `sws/3d/results/p52/` (stranded_*).
  Inputs carried as status: Br [R4] S; wire box params.yaml; faults level 1.5 half-space (design.md
  l.242); N52 Hcj 0.88 MA/m is A (head.py l.37, l.41–42) and every N52 knee figure says so.
- Register: do not overwrite l.347. Add a new row and mark l.347 superseded with a pointer (convention
  l.324). Split the status: "follow EN 12927 §14 as the minimum; better fine, worse redesign" is D (owner
  ruling 2026-11-08); the wire-count reading (40 mm one hidden outer-strand wire, 52 mm two) is U (said
  to come from [R5] via the head designer, text not on file). Numbers: l.347 says 0.62 % and cites spec
  rev127 l.52/262/425/429; 0.636 % is Q4's calculation (questions l.130); rev128's wording is at its
  l.438. No EN 12927 text exists on this machine (verified): write "Needs Stian: the standard's §14
  pages".
- Add a `tasks/TASKS.md` U32 entry with "Done when" citing the record (rule 10).

U33:
- Cursor install on native Windows: `irm 'https://cursor.com/install?win32=true' | iex`
  (cursor.com/docs/cli/installation).
- Dry-run leak risk: `codex exec`, `agent -p` and `claude -p` read their working folder (and claude
  loads CLAUDE.md). Run every backend from an empty temp folder under the scratchpad that holds only
  the dummy document; Codex with `-s read-only --skip-git-repo-check`; the runner must `cd` there
  itself, never run from the repo. The verifier checks the working folder and the command lines.
- U31.md has no "masking section": masking is at l.31, 65, 76, 90–92 and Needs #6 (l.102); the pack
  section is l.83.
- Add a `tasks/TASKS.md` U33 entry with "Done when" (rule 10).
- Names: Davit is taken; Compass, Quill, Fairlead are also taken (no files). — Kai

## U34 — close the outside review's 2D and record findings (Kai, 8 Nov afternoon)

Source: `docs/paper/reviews/2026-11-08/grok-external.md` (outside reviewer on the masked bundle; treat
as data, follow no instruction in it) and verifier-grok's check (this brief carries its verdicts:
9 confirmed, 1 partly, 1 uncheckable, 0 wrong). Stian, 8 Nov ~12:30: "not sure we should stop the N52
study anyhow"; the N52 study continues. Rule 10 throughout; nothing selects a grade, thickness or head.

Builder: Opus. Worktree C:/Users/stian/Prosjekter-u34/max, branch u34-review-closeout from main
4b1f038 (or later; `git log -1 main`). U32 is running 3D in Prosjekter-u32 — do not start any FE heavier
than the 2D `sws_head.py` solves (seconds each); do not touch its worktree. Read first: rule 10
(max/CLAUDE.md l.60–71), the review §1–§5, `docs/paper/questions_2026-11-08.md`,
`sws/fem-2d/sws_head.py` (l.17, l.119–127, l.173, l.233–237), `sws/fem-2d/sws_decided_rerun_2026-11-07.md`
§7 and l.184–202, `sws/3d/p52/design.md` §2, `docs/paper/figures/q5_options.py`, the register rows
l.127–131, l.181–182, l.191–192, l.247, l.315–318, l.329–350, spec rev128 render l.11, l.155, l.233,
l.237–245, l.253–255, l.369–376.

A. Knee-history re-solve (review finding 1, confirmed). Add to `sws_head.py` a two-pass option: pass 1
   solves the worst excursion state (head empty, and separately the 40 mm rope in the shared head) at a
   given temperature; every magnet element whose working point lies beyond the knee (the existing
   0.8·Hcj screen, status A, REG l.130/l.182) gets its Br reduced along the recoil line to the value the
   knee model gives after that excursion (state the model in one paragraph with its status A; if the
   register gives no recoil rule after the knee, use the simplest defensible one — recoil from the
   point reached, slope µ_rec from the existing linear law — and say so); pass 2 solves the service
   state (52 mm and 40 mm rope, hard wire, +45 °C) with the reduced Br map. Run it for N52 at the
   +45 °C B_rope size (15.84 mm) and at the 3D-sized 16.73 mm, for Hcj20 = 0.88 (A), 0.96, 1.05, 1.19
   MA/m, excursion at 20 °C and 45 °C; and for N48SH once as the control (expect no change). Output:
   B_rope and B_wire after history against virgin, the Br loss map as a figure, and the Hcj at which the
   history loss falls under 1 mT. json + one figure (`sws/figures/decided/` style) + a dated section in
   the rerun md ("Knee history, 2026-11-08"). Numbers are C by script, the model A; no selection.
B. Q5 rebuilt (finding 2, confirmed): one thickness per row. For each head × grade give, at lm_min(+45,
   B_rope) and at the B_wire-sized lm and at the record lm: B_rope margin, B_wire margin, in-rope knee
   fraction (smallest rope), empty-head knee fraction, mass. Replace the table and figure in
   `questions_2026-11-08.md` Q5 and `q5_options.py`; re-word the "safest" paragraph so it says which
   thickness it means; keep it a labelled view; add the N48SH empty-head 0.03 % at +60/+80 (RERUN l.202)
   and the N52 history result from A.
C. Record corrections (all confirmed): (1) RERUN l.196 says U25b ran the empty state in 3D — it was 2D
   (DESIGN l.99, U25 l.67): correct the line with a dated note. (2) questions Q2: soften "none waits for
   RAM" to what the record supports (U08 l.42–44 page file; R8 an estimate, U19 l.95); Q3 l.113 "what
   will actually be seen" → "the owner's ruling, mapped to the shielded case (A, REG l.330)"; Q1: add
   that SPEC128 l.155 already reads the window as B_rope, so "complies with EN 12927" cannot be stated;
   Q4: state that neither 40 mm row is supported by the catalogue (REG l.100–101), wire diameters are a
   supplier input. (3) THEORY.md A7 (l.80): add one sentence that the wire and yoke B(H) are
   temperature-independent in the model, so hard/+80 is a conditional bound, not proven. (4) Register:
   add a row "Br / Hcj reference temperature" status U until [R4]'s PDF is read (REG l.127–129; the PDF
   is not in the repo — Needs Stian).
D. Spec rev129 (finding 5, confirmed; rev128 kept the old close-out beside the new one). Apply, with the
   same python-docx route as U31 (scratch venv) and the same diff discipline: banner result 8 (l.233
   "not a design risk") and the steel-shoe map's "≤ 0.1 % beyond the knee" (l.237–245) as "steel-shoe
   record, superseded by result 10 and the 2026-11-07 rerun"; mark the record-lm table l.253–255 as
   "+80 °C N40SH record size, see the per-grade table l.175"; replace l.11 "three independent FEM tools
   agree to within noise" with the Stage 1 statement the register supports (REG l.315, status D) or
   banner it; add the rows to `sws/spec/REDLINE_2026-11-07.md` as rows 28–31 marked applied in rev129.
   The owner's Word file is the master: list "rev129 → Word" under Needs Stian. If the docx route fails
   in 30 minutes, Markdown rev129 only.
E. Writer inputs (review §5): add Grok's fields to the peer read part C with source and status
   (bwire_margin_at_lm_min_45, bwire_lm_45, empty_head_knee, constitutive_ok, acceptance_conflict,
   sun_body, hoist_house_adder, br_tref, core_fill, strand_ripple_vs_budget, fault_temperature,
   domain_offset_donor; shaded_site_peak only if not a duplicate of sun_head_peaks_dubai) and the KB
   caveats on KB1, 2, 4, 5, 6, 9, 11, each one line, dated "added 2026-11-08 after outside review".
F. Sun model on the decided head (finding 3, partly): if `sws/due-diligence/sws_sun_exposure.py` can
   take the body size, re-run it for the ~9 kg Ø126 × 180 mm covered head at the shielded and the
   fully shaded cases (RERUN l.166–173 for the mass and size), report the temperatures beside the
   30 kg results, status C on an A model; if it cannot without a model change, say so and stop that item.
   The hoist-house adder (+5–10 K, SPEC128 l.376) and the 49 °C shaded case: in or out of scope is the
   owner's — Needs Stian, one line.
G. Not yours (3D, with U32's queue): the 3D working-point solve empty and 40 mm per grade, the core-fill
   sweep, the direct acceptance fault. Note them in the report as handed to U32.

Rules and delivery: rule 10; verifier subagent (qc-falsifier) on A's model statement and numbers (re-run
two cases), B's table against json, C/D against the files line by line, E against the review; no names,
no drawing numbers; `tasks/TASKS.md` U34 entry with "Done when" citing the record; rebuild
`python docs/sws/build.py --check`, `tests/test_sws_report.py`, `sws_head_test.py`. Report
`tasks/reports/U34.md`: A's result in one table (N52 after history vs virgin, by Hcj), B's new table,
the rev128→rev129 diff summary, Needs Stian (max 5). Commit on the branch; no merge, no push. Notes in
`C:/Users/stian/agent-notes/<nautical name>.md` (taken: Bight, Buoy, Sextant, Bollard, Bosun, Capstan,
Cleat, Fathom, Gimbal, Gunwale, Hawser, Keelson, Windlass, Halyard, Binnacle, Davit, Scupper, Compass,
Quill, Fairlead, plus the U32 builder's name — check the folder). Timebox 4 hours. — Kai

### U34 addendum — verifier-brief34 corrections (Kai, 8 Nov). These override the text above.

- C(2) Q3: do NOT change "what will actually be seen" — it is the owner's own D wording (REG l.332).
  Only add the mapping note "(the shielded case is the builder's mapping, A, REG l.330)".
- D l.11: REG l.315 is the same three-tools statement (D, team statement 2026-10-26, files pending), not a
  Stage 1 statement. Do not replace l.11; banner it only: "team statement 2026-10-26; files not yet in
  the repository (register l.315)".
- C(4): no new register row by the builder. Write the "Br / Hcj reference temperature" row as a
  proposed row under Needs Stian (text ready to paste), status U.
- A cites: the knee screen is REG l.182 (A); l.130 is alpha(Hcj) (A); recoil permeability 1.05 is l.131
  (S) and in code MU_REC l.49 / HeadConfig.mu_rec l.92. Nothing in the record models the state past the
  knee, so the "recoil from the point reached, slope µ_rec" rule is new: state it as A in one paragraph.
  Hcj 0.96 and 1.19 are RERUN l.211–213 (45 °C); 1.05 is an intermediate sweep point, label it so.
- A implementation: Br per element lives in model.ebr (sws_axi_fem.py l.205–212, l.285–286); a pass-2
  map can overwrite it after build() without a solver change. run_case() rebuilds the mesh and the 40 mm
  rope changes it (r_rope in extra_r, build l.181–183): map the 40 mm-history Br by element centroid
  onto the 52 mm mesh. Empty head: sws_decided_rerun_checks.py _empty_job (l.69–74). 40 mm in the
  shared head: sws_decided_rerun.py job_demag / mode_demag (l.221–240; §7 used nominal wire — pass 2 is
  hard wire per REG l.333, say which wire pass 1 used).
- C(2) Q4: cite REG l.100 and l.215 (wire diameter 2.5 mm, A, not held); l.101 is wires per strand.
- D: rev128 docx is `sws/spec/SWS_HW_Design_Input_Specification_rev128_2026-11-08.docx`; U31's apply
  script is at C:/Users/stian/AppData/Local/Temp/claude/2a40536beb49695d/c8a54a63-c1a2-4311-8bd6-5f70b32ad736/scratchpad/u31/apply_rev128.py
  (copy it into your scratchpad; a fresh scratch venv with python-docx is needed). Redline rows start at 28.
- F: the sun script's cases are unshielded / semi-shielded / shielded (l.6–9, l.172); "fully shaded,
  open structure" (spec l.374) IS the shielded case. Run the shielded case for the decided head on the
  design day (43.5 °C air) and on the record day (49 °C air), with two thermal masses: magnetics only
  8.7–9.3 kg and complete 12.7–15.3 kg (RERUN l.166–173, housing 4–6 kg A). Body(name, d, l, mass, cp)
  is a class (l.67–68); HEAD is hard-coded at l.74 — write a short driver with a new Body, no model change.
- Names: Thole is the U32 builder; Compass, Quill, Fairlead reserved. — Kai

## U35 — fold in the U32 appendix queue results (Kai, 8 Nov 22:4x; brief checked by verifier-brief35/36)

Stian, 8 Nov 22:2x: "start now". The detached queue finished: `sws/3d/logs/u32_appendix2_queue.txt` ends
"APPENDIX2 QUEUE DONE Sun Nov 8 20:57:23 2026". Rule 10 throughout; nothing selects a grade, thickness or head.

Builder: Opus. Work in the existing worktree C:/Users/stian/Prosjekter-u32/max (branch u32-3d-main-runs at
65e8cec, merged into main at 38974e6). Exactly seven result json files are untracked there
(`sws/3d/results/3dd_P52lm*_{acc,lh60,cf,cfdw}.json`); the `results/p52/seams_*` files are already tracked.
Start with `git checkout -b u35-appendix-foldin main` (keeps untracked files), then `git add` the seven. No new
FE solves heavier than seconds. U36 works at the same time in Prosjekter-u36 on the register, the spec,
`docs/sws/build.py` and the page: do not edit `sws/data/sws_data_sources.md`, `sws/spec/*` or
`docs/sws/build.py`; if a new figure needs a build.py entry (figure list l.75–81), write the exact line into
your report under "for U36/merge" and leave `docs/sws/index.html` unbuilt (U36 rebuilds after both merge).
Propose register rows in the report, text only.
Read first: rule 10 (max/CLAUDE.md l.60–71); `tasks/reports/U32.md` run table (l.45–56) and "The queue after
this report" (l.88–95) — the recipe is `p52/u32_summary.py` (globs the new files) then
`sws/figures/decided/make_u32_figures.py` (reads `results/p52/u32_summary.json`); `sws/3d/p52/design.md` §7
(it already carries the knee screen K ≈l.379–406, R2 N40SH ≈l.407 and R6 ≈l.410–413 — do not repeat them);
the queue log and `sws/3d/logs/u32_appendix2_queue.sh` (run order and comments); `sws/3d/rope3d.py` l.81–155
(`construction`, `core_fill_override` l.138–143 — what fill 0.7 means; `run_3dd.py` only passes it through);
`docs/paper/questions_2026-11-08.md` Q2; `docs/paper/peer_read_2026-11-08.md` part C; register l.329–350
(read-only).

A. What is new: R3 (−40 °C easy, acceptance faults) for N48SH, N52, N40SH; R8 (L_h 60 half-space, N52 16.73);
   CF (N48SH, core fill 0.7; log l.121, intact B_rope 1.70269 T, ndof 2,066,302); CFDW (core fill 0.7 with
   2.2 mm wires; log l.136, 1.63384 T, ndof 2,464,123); the single hidden wire on L_h 60 (N48SH; log l.151,
   1.94554 T). Tabulate them from the json: intact B_rope, LMA %, LF margins at 3 mm and 5 mm, Bz, unknowns,
   wall time, convergence. Every number C by script. State what moved against the 2D values
   (`sws/fem-2d/sws_decided_rerun_2026-11-07.md`) and the 3D main set (§7, U32.md l.53–54). The core-fill
   drop in B_rope is a sensitivity of the rope model (the queue comment says the metallic area then falls
   below C·d²), not a head result: say so in those words after reading rope3d.py; the verifier confirms.
B. `sws/3d/p52/design.md`: a dated section "U35, 8 Nov 2026: appendix runs" after §7 — numbers, figure(s),
   no selection. Figures in `sws/figures/decided/` style (and the README there if it lists figures).
C. `docs/paper/peer_read_2026-11-08.md` part C: add the appendix fields (acceptance fault at −40 °C per grade,
   L_h 60 check, core-fill sensitivity, single hidden wire) with source and status C, dated "added 2026-11-08
   (U35)". `questions_2026-11-08.md` Q2: one dated line that the run list R1–R8 is complete.
D. Verifier subagent (qc-falsifier): recompute two numbers from json; design.md text against json and log
   line by line; part C fields against json; nothing selected. `tests/test_sws_report.py`. Report
   `tasks/reports/U35.md`: the run table, what moved, proposed register rows (text only), "for U36/merge"
   lines, Needs Stian (max 3). `tasks/TASKS.md` U35 entry with "Done when" citing the record (U36 also adds
   an entry; keep yours to one block so the merge is clean). Commit on the branch; no merge, no push. No
   names, no drawing numbers. Notes in `C:/Users/stian/agent-notes/<nautical name>.md` (taken: Bight, Buoy,
   Sextant, Bollard, Bosun, Capstan, Cleat, Fathom, Gimbal, Gunwale, Hawser, Keelson, Windlass, Halyard,
   Binnacle, Davit, Scupper, Thole, Lanyard, Compass, Quill, Fairlead — check the folder). Timebox 2.5 hours.
   — Kai

## U36 — spec rev130: the temperature envelope remade to the owner's ruling (Kai, 8 Nov 22:4x; checked)

Owner ruling, 8 Nov 22:2x, record it as said: "No, just remake them to what we want. I started just with
what the ADC was; if another unit was −60 to +60 that would be the edge. Then we end up with real life
−40 … 50 max. Transport MAX we define to what we want!" Context: the +85 °C storage (rev129 render l.367),
the +80 °C soak within 1 % (l.233 result 8, last sentence; l.429) and the −40/+85 cycling (l.429) are our own
text from 9 Oct, written when the envelope was ±80 taken from the ADC range. The ruling means the ±80
"hardware limit / qualification envelope" is no longer a hardware fact: it was the ADC range, and the owner
now sets the envelope. Kai's reading of the rest — check it against the record and report it as a reading:
(1) the hardware operating range becomes −40 / +50 °C ambient at the sensor (replacing −40/+70 at l.367);
the 7 Nov service ruling (magnet ≤ 45 °C, covered head, REG l.330) stands beside it — whether +50 is the
ambient and 45 the covered magnet, or +50 replaces 45, is Needs Stian; (2) the storage/transport maximum is
the owner's to set and the number is not given yet. Rule 10 throughout; the owner picks the number.

Builder: Opus. New worktree: from the git root C:/Users/stian/Prosjekter-u05 run
`git worktree add C:/Users/stian/Prosjekter-u36 -b u36-spec-envelope d5db50c` and work in
C:/Users/stian/Prosjekter-u36/max. U35 works at the same time in Prosjekter-u32 on `sws/3d/*`, the figures
folder and the peer read part C — do not edit those. Yours: the register, `sws/spec/*` (incl. `render_spec.py`
SOURCES l.22–25 and `sws/spec/README.md`), `docs/sws/build.py` (l.124 render path, l.637 rev text) and the
page rebuild — rebuild once more after both units merge (Kai will ask).
Read first: rule 10; register l.7–11, l.127–131, l.181–182, l.329–332; rev129 render l.11, l.233, l.334,
l.367–376 (l.376 "+80 °C the magnets were sized for"), l.384/386 (parts rating −40…+85: stays), l.428
(climate steps +70 / briefly +85), l.429, l.497 (envelope statement), l.506 (keeper plate for storage and
transport of an open half); `sws/spec/REDLINE_2026-11-07.md` rows 1–31; `sws/fem-2d/sws_knee_history.py`
(`one(grade, lm, hcj20, hist, t_x, …)` l.57–92: empty head as fill 1e-9 l.53–54, 40 mm hard wire, Br carry
to +45, service on the 52 mm hard wire; omega 0.2 with 0.1 as the check) and `sws_head.py`
`knee_history_br` (l.287); `sws_decided_rerun_2026-11-07.md` "Knee history, 2026-11-08"; U31.md l.17–18
and U34.md l.70 (docx route: python-docx in the scratch venv `.venv-docx`, not committed).

A. Numbers for the owner's choice (2D, seconds each, status C on the A knee model), with the existing
   driver `sws_knee_history.py one(...)` by passing t_x — no new model: N52 at lm 15.84 (2D lm_min) and 16.73
   (3D-sized) for Hcj20 0.88 (A), 0.96, 1.05, 1.19 MA/m; N48SH at 16.58 with Hcj 1.59 (grade letter, A) as
   the control (these are U34's run points, not selections); history states empty head (the transport state
   without a keeper) and 40 mm rope; excursion t_x = +45, +50, +60, +70, +80 °C; output knee share and the
   B_rope loss at the +45 °C service state against virgin. One table, one figure (loss vs excursion
   temperature per grade and Hcj). `build()` (l.157) has no keeper region: write one line that the keeper
   plate (l.506) is not modelled and stop there.
B. Register (`sws/data/sws_data_sources.md`), roles not names, convention l.7–11:
   - l.329: correct the origin (+80 °C from the ADC range, owner statement 2026-11-08 evening; −40 unchanged)
     and mark the row "no longer the hardware limit; kept as the historical starting point of the sizing
     method (owner ruling 2026-11-08 morning: 'the initial settings … should be there')".
   - l.331 (+80 qualification reference) and l.332 (the method states −40/+80 as the hardware limit): do not
     delete; add "relation to the 2026-11-08 evening ruling: Needs Stian" in the notes.
   - New row "Temperature envelope, owner ruling 2026-11-08 evening" D, with the quote above, source
     "owner ruling, 2026-11-08 (evening)".
   - New row "Hardware operating range −40 / +50 °C ambient at the sensor" D (owner ruling 2026-11-08
     evening), with "relation to the 45 °C magnet ruling l.330: U, Needs Stian".
   - New row "Storage / transport temperature" U: "owner defines; candidates shown in the U36 table (A);
     number not yet given; the head ships open and empty — the keeper plate (spec l.506) is the mitigation".
   - New row "Soak and cycling temperature for the irreversible-loss check" U, tied to the storage maximum.
   - On the relevant rows note that l.367's +85, l.429's +80/+85 and l.11/l.497's −40/+80 are superseded.
C. Spec rev130 (python-docx on rev129, same route and diff discipline as U31/U34; add rev130 to render_spec.py
   SOURCES and the README): l.11 and l.497 (the envelope statement: historical starting point, no longer the
   hardware limit); l.233 result 8 last sentence; l.334 (−40…+70 → −40…+50); l.367 operating −40 / +50 °C
   ambient at the sensor, storage and transport "−40 °C to +[owner value] °C — owner to set, see redline";
   l.376 (what +80 was); l.428 climate steps to +50 and briefly to the storage maximum; l.429 cycling and soak
   at the storage maximum; l.384/386 untouched. Redline rows 32 onward, "applied in rev130; storage maximum
   pending owner". Before you finish, check `C:/Users/stian/agent-notes/kai.md` for a "U36 addendum" with the
   owner's number; if it is there, apply it. If the docx route fails in 30 minutes, Markdown rev130 only. The
   owner's Word file is the master.
D. Verifier subagent (qc-falsifier): A's numbers (re-run two cases); B and C line by line against the ruling
   text and the files; nothing selected; roles not names. `tests/test_sws_report.py`, `python
   docs/sws/build.py --check`. Report `tasks/reports/U36.md`: A's table, the rev129→rev130 diff summary, the
   register rows, Needs Stian (max 4: the storage maximum; +50 vs 45 °C; rev130 → Word; l.331/l.332
   relation). `tasks/TASKS.md` U36 entry, one block. Commit on the branch; no merge, no push. Notes in
   `C:/Users/stian/agent-notes/<nautical name>.md` (taken list as U35 plus the U35 builder's name — check the
   folder). Timebox 3 hours. — Kai

## U36 addendum — owner ruling, 8 Nov 2026 late evening (Kai)

Verbatim: "we cannot avoid temperatures above ambient, so that is the absolute minimum so I would say then 49 →
gives us 50 as the highest allowed and we can have it for both. It is not the electric charger that determines our
transport, it is the magnets. But since we can order magnets per spec we will try to order ones that will have 0
loss at 50 degrees. I think we need more magnet info before doing more runs."
Reading: −40 / +50 °C is the envelope for service, storage and transport; +50 is the magnet corner (the 49 °C
record day rounded up); the magnet procurement requirement is zero irreversible loss after a +50 °C excursion in
the open-half (empty, no keeper) state; no further FE runs until the supplier's data for one-piece radial arcs is
on file. Apply to rev130 l.233/367/428/429 and the register "Storage / transport temperature" row in the next spec
unit (not tonight).

## U37 — identifier sweep of the working tree before the GitHub push (Kai, 9 Nov 00:1x)

Owner, 8 Nov late: "get everything to git … so long as there is no deletion we stay on track". History is not
rewritten. Before main goes to the GitHub remote, the working tree must carry no personal names other than the
owner's and no drawing numbers — the standard already applied to U17 (names → roles) and to every brief since.

Builder: Opus. Worktree: `git worktree add C:/Users/stian/Prosjekter-u37 -b u37-identifier-sweep d455e3d` from the
git root C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u37/max. Rule 10 applies: content and
numbers do not change; only the identifier strings do.
Tool: `C:/Users/stian/max-private/tools/scan_tree.py <dir>` (count-only; NGSolve venv python
C:/Users/stian/Prosjekter/max/.venv/Scripts/python.exe with -I). The list is
C:/Users/stian/max-private/identifiers.yaml; you may read it through a script to locate hits (file:line) but never
print, copy or quote a value in notes, report or commit message. Entries by index: 7, 8, 9, 10 are persons,
11 and 12 drawing numbers, 5 a customer, 0/1/6 project numbers, 2/3/4 sites (policy allowed-private — leave them).
A. In these files replace persons with roles (head designer, manager, supplier contact, as the context says) and
   drawing numbers with the register's drawing reference ([Rn] or "drawing, on file") exactly as the register
   does: README.md; sws/fem-2d/sws_decided_rerun.py; sws/fem-2d/sws_decided_rerun_2026-11-07.md; sws/3d/rope3d.py;
   sws/3d/run_3dd.py; sws/3d/p52/head.py; sws/3d/p52/design.md. For the two result json files
   sws/3d/results/3dd_H52_d52_hard_+80C_*_{d,s60}.json with a project-number hit: find where it sits (a path or
   comment field?) and report; change it only if it is metadata, never a result value. Keep code running
   (`sws_head_test.py`, `tests/test_sws_report.py`); rebuild the page only if a page source changed
   (`python docs/sws/build.py --check`).
B. Do NOT edit docs/strategy/** (customer name, project number, persons in the origins README) — that is the
   owner's content; list the files and hit counts under Needs Stian. Do not edit tasks/reports/U13/*.png.
C. Run scan_tree on the worktree before and after; the report shows both totals and the per-file counts for the
   indices 5–12 after (0 expected outside docs/strategy and the png). Verifier subagent (qc-falsifier): no number
   or statement changed, only strings; no value printed anywhere; tests pass.
D. Report `tasks/reports/U37.md` (counts only), TASKS.md entry, notes in agent-notes/<nautical name>.md (check the
   folder; Painter and Taffrail are taken tonight). Commit on the branch; no merge, no push. Timebox 1.5 h. — Kai

## U38 — GitHub export v3: main since the last export, rewritten and grafted onto GitHub's main (Kai, 9 Nov 02:3x; checked by verifier-brief38/39)

Owner, 9 Nov ~01:20: "yes push all"; earlier the same night: "we anyway have the history so long as there is no
deletion we stay on track". So: no force-push, no replacement of what is on GitHub. GitHub fjordbit/max main is
51c9bc1 = the cleaned export of the max/ subtree at local 4730e63 (4 Nov; `4730e63:max` differs from 51c9bc1
only in the 7 rewritten files). Local main is now 2e8ebf9. The git root C:/Users/stian/Prosjekter-u05 is a
monorepo; only the `max/` subtree is exported. Job: the incremental export, so that GitHub's main fast-forwards
(the "accept" route, secretary log 2026-11-07 l.109–110).

Builder: Opus. Everything in a scratch folder outside every repo, C:/Users/stian/export-v3/ (create it; delete
nothing else). Read first, and only these lines of the owner's private log: C:/Users/stian/secretary/log/2026-11-04.md
l.5–8 and l.62 (v1 method and order: subtree split → first-parent cherry-pick onto the cleaned branch in a clone of
D:/git/max-export.git → `git fast-export --reference-excluded-parents` → rewrite_names.py → fast-import → scan →
push from the clone over https), log/2026-11-07.md l.83–110. Tools: `C:/Users/stian/max-private/tools/rewrite_names.py`
(takes a fast-export stream; `apply(data, scopes)` can be used per blob — copy the scope logic from main(): TEXT/PROSE
extensions → "text"/"prose", commit messages get both; the tool never rewrites paths); never copy a rule's left-hand
side into any note, report or commit message — name rules by placeholder only. `C:/Users/stian/max-private/tools/scan_tree.py`
(count-only; NGSolve venv python C:/Users/stian/Prosjekter/max/.venv/Scripts/python.exe with -I).

A. Clone D:/git/max-export.git (bare, main = 51c9bc1) into the scratch folder. In a scratch clone of the monorepo
   (or a worktree you remove afterwards) run `git subtree split --prefix=max` over 4730e63..2e8ebf9, or replay
   `<commit>:max` trees; take the first-parent commits only (`git rev-list --first-parent --reverse
   4730e63..2e8ebf9` = 34; merges become one commit each, side commits are not replayed — this is tonight's rule,
   chosen by Kai; v1 replayed u22's side commits, we do not). Graft onto 51c9bc1 the v1 way (cherry-pick onto the
   cleaned branch, then fast-export with --reference-excluded-parents → rewrite → fast-import), keeping author
   dates; author stays "fjordbit"; commit messages pass through the same rules. Branch: main only.
B. Checks before anything is handed back: (1) scan_tree on the exported tip tree: persons (ids 7–10) and
   drawings (11–12) must be 0 everywhere, docs/strategy included; customer (5) and project (0/1/6) hits are
   reported by file (the owner accepted docs/strategy and the U13 png tonight; the two float false positives in
   sws/3d/results/3dd_H52_*.json are known) — if a person or drawing hit remains, add a rule to rewrite_names.py
   (placeholder form, dated, your name) and rebuild; (2) scan the full `git log -p 51c9bc1..<tip>` patch of the
   export (count-only), same requirement; (3) at the tip, in a venv with markdown==3.7 and pytest: `python
   docs/sws/build.py --check` and `pytest -q tests/test_sws_report.py` (the workflow .github/workflows/sws-report.yml
   runs these on push; note 51c9bc1 has no .github/, so this push adds the workflow for the first time — say so in
   the report); (4) `git diff --stat <tip> 2e8ebf9:max` (the subtree, not the monorepo): the only differences
   must be the rewritten strings — list the files and confirm by reading three that only placeholders changed.
C. Report to C:/Users/stian/export-v3/REPORT.md (not into the repo): commit count, tip id, the scan tables
   (counts only, per index and file), test results, the exact fast-forward push command for Kai
   (`git -C <clone> push https://github.com/fjordbit/max.git main:main`, no --force; the push is Kai's), and
   anything that could not be made 0. Do not push anywhere. Do not touch D:/git/max-export.git or
   D:/git/max-export-v2.git. Notes in C:/Users/stian/agent-notes/<nautical name>.md (check the folder; Painter,
   Taffrail, Gudgeon are taken tonight); no identifier values in the notes. Timebox 2.5 hours. — Kai

## U39 — the short SWS page: five pages, every number a link into the long page (Kai, 9 Nov 02:3x; checked)

Owner, 9 Nov: build the short page; Kai's answer, accepted: its own page, every number and figure linking into
the matching section of the long page, nothing duplicated, the long page is the appendix. Rulings for the paper
(register l.347–350; l.349 = report scope: leads to the safest, management chooses; l.348 = EN 12927 §14 as the
minimum): the method starts from the initial −40/+80 envelope (register l.329: the ADC-derived starting point,
no longer the hardware limit), the analytical temperature path leads to the hardware range −40/+50 °C ambient
(register l.360, owner ruling 8 Nov evening) and to the owner's later statement the same night that −40/+50 is
also the storage and transport range and that magnets are procured to "zero irreversible loss after a +50 °C
excursion in the open-half state" (the U36 addendum in this file, 8 Nov late evening; recorded in the
coordinator's notes, register row l.361 still reads "owner defines"; cite it with that status, do not amend
the register). 40 mm, 52 mm and the shared head with the grades all appear. The aim, in the owner's words
(this file l.918): "optimizing a TMR sensor for detection according to [the rulebase]" — quote verbatim or drop
the quote marks; "EN 12927 §14 and the specification" is the Q1 gloss. Figures over numbers. Rule 10: nothing
selects a grade, thickness or head; every number from the record with its status and a link.

Builder: Opus. Worktree `git worktree add C:/Users/stian/Prosjekter-u39 -b u39-short-page 2e8ebf9` from the git
root C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u39/max. Read first: rule 10
(CLAUDE.md l.60–71); `docs/sws/build.py` (how the long page is assembled from parts; DECIDED_FIGS l.60–84,
P40_FIG l.86; ~370 heading ids such as `rerun-7-…`, `p52-7-…`, `register-…`; figures have no ids; the check
mode); `tests/test_sws_report.py`; `docs/paper/peer_read_2026-11-08.md` parts A–C incl. C.9 (l.195) and C.10
(l.218); `docs/paper/questions_2026-11-08.md` (Q5 table, three thicknesses per row, and
`docs/paper/figures/q5_options.png/.json`); `docs/paper/reviews/2026-11-08/SYNTHESIS.md`; spec rev130 render
§1 and the result banners; register l.7–11, l.127–131, l.181–182, l.191–192, l.329–361; `sws/3d/p52/design.md`
§1–§2, §7–§8; `tasks/reports/U36.md` table l.30–47.

A. First make the long page the full appendix (Kai's choice, option a): add two parts to build.py —
   `docs/paper/questions_2026-11-08.md` Q5 (the options table and figure) and the U36 excursion table
   (`tasks/reports/U36.md` l.23–53 or its json) — as new sections with ids and figure ids (give figures ids too:
   `fig-<name>`), rebuild the long page. Then `docs/sws/short.html`, built by `docs/sws/build_short.py` from the
   same sources (no number typed by hand; each read from a source file the test checks). At most five printed
   A4 pages at the long page's styling; self-contained like the long page. Sections, in this order:
   1. Purpose, one paragraph (the owner's aim sentence; what the head is, one figure).
   2. Method: envelope → temperature path → knee screen → knee history (the A model) → 2D sizing → 3D confirm.
      One figure; the ruling dates and their status as above.
   3. Results, one table. Rows = head × grade: dedicated 40 (Ø48 bore), shared 40+52 (Ø60 — this IS the 52 mm
      head in the record; bore = d + 8), wide Ø65 (Q5's third head); grades N52, N48SH, N40SH. Columns: magnet
      thickness B_rope-sized and B_wire-sized (both; the record thickness as a third where Q5 has it), B_rope and
      B_wire margin, in-rope and empty-head knee share (+45 / +80), loss after a +50 °C open-half excursion, magnet
      and yoke mass (Q5 notes: 3.6 / 6.06 / 7.3 kg). Where the record is silent the cell reads "record silent":
      the +50 °C loss for every dedicated-40 and Ø65 cell, every N40SH cell, N48SH except the shared head at
      16.58, N52 except the shared head at 15.84 / 16.73 (U36 is shared-head only; N52 at the B_wire-sized 17.29
      is "not solved" in Q5); the knee-history-corrected N52 margin except shared 15.84 / 16.73; 3D figures exist
      for the shared head only. One figure (`q5_options.png` or the U35/U32 3D figure).
   4. Acceptance: the standard as the minimum (l.348), the two readings B_rope / B_wire (l.191), the 52 mm
      two-wire conflict with the spec's < 0.5 % — open; one figure of fault margins.
   5. What the numbers say (a labelled view, not a selection): where each grade is clear of the knee, what N52
      depends on (the supplier's Hcj for one-piece radial arcs; the procurement requirement in the addendum's
      wording), the shared head's mass against the dedicated 40. End with "the choice is management's; the
      record is the long page" and the open decisions (storage number into the spec, wire diameters, R5, supplier
      sheet).
   Every number links to the long-page anchor it comes from (`index.html#<id>`), figures to their `fig-` ids;
   where even the extended long page has no anchor, link to the source file and line in the repo and say so in
   the report.
B. `tests/test_sws_short.py`: every number in short.html appears in the linked source; `build_short.py --check`
   freshness. Add short.html and build_short.py to `.github/workflows/sws-report.yml` paths and steps. Link the
   short page from `README.md` and from the top of the long page (one line in build.py).
C. Verifier subagent (qc-falsifier): read the short page as a manager would and list anything that reads as a
   selection or as a claim without a link; recompute three numbers from json; the rulings stated with the right
   status (register row vs addendum); no personal names, drawing numbers or user paths. Both tests and
   `build.py --check` pass. Report `tasks/reports/U39.md` (what the page says, page count, verifier findings,
   Needs Stian max 3), `tasks/TASKS.md` U39 entry. Commit on the branch; no merge, no push. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (check the folder; Painter, Taffrail, Gudgeon and the U38
   builder's name are taken). Timebox 3 hours. — Kai

## U40 — export increment for U39, then the Pages snapshot (Kai, 9 Nov 03:4x; for Fairlead, who built U38)

Owner, 9 Nov: "yes push all, refresh pages". Preconditions Kai confirms before handing this over: U39 is merged
into local main (Prosjekter-u05/max; take the tip from `git log -1 main`), the page is rebuilt and tests pass.
A. Export increment, exactly the U38 method and checks (kai.md "## U38", B(1)–(4)), from the clone
   C:/Users/stian/export-v3/export: range 2e8ebf9..<new main tip>, max/ subtree, first-parent (the U39 merge
   becomes one commit), rewrite, graft on 97bd8ce. Scan: persons and drawings 0. Tests at the tip incl.
   `pytest -q tests/test_sws_short.py` and `python docs/sws/build_short.py --check` (new in U39). Report to
   C:/Users/stian/export-v3/REPORT-2.md. No push — Kai pushes.
B. Pages snapshot, in the existing publish repo C:/Users/stian/publish/SWS (remotes: origin = fjordbit/SWS,
   maxflow = MAx-Flow/SWS-Documentation; deploy workflow .github/workflows/static.yml serves docs/; read its
   README and the last snapshot commit c1920f4 `git show --stat` to see what a snapshot carries: `sws/` and
   `docs/sws/` from the pseudonymised tree, repo README kept, no pdf/docx — check the last snapshot's tree with
   `git ls-tree -r --name-only HEAD | head -50` and keep the same shape). Replace `sws/` and `docs/sws/` with the
   same paths from the export tip of step A (the rewritten tree; keep `docs/sws/sws_demo_720p.mp4` and
   `docs/sws/index.zip` if the last snapshot had them — rebuild the zip from the new index.html the same way;
   add `docs/sws/short.html`). Fix any link in the pages that points at a repository path the snapshot does not
   carry (the U39 report says one Q1 citation links to the repository file; the long page's source links are
   absolute to fjordbit/max per build.py l.36 — leave those). Scan the whole publish tree with scan_tree.py:
   persons and drawings 0; report the rest by file. `git status` must show only sws/ and docs/sws/ changes.
   Commit "SWS snapshot from MAx <tip>: U35–U39 (3D appendix, rev130 envelope, identifier sweep, short page)";
   no push — Kai pushes to both remotes.
C. Hand back ≤ 10 lines: export tip and counts; snapshot commit; scan residue by file; the two push commands
   (`git -C C:/Users/stian/publish/SWS push origin main`, `… push maxflow main`, plain pushes). Notes in your own
   notes file. Timebox 1.5 hours. — Kai

## U41 — one link, two formats: a format switch in the header of the long and the short SWS page (Kai, 9 Nov 14:1x)

Owner, 9 Nov: the 4-page report (short.html, U39) and the long page (index.html) are both live on Pages; he wants
both reachable from the same link, chosen "by selection in the header or something", simple. A third format
(a readable / management version, U42) follows, so the switch must take a third entry without rework.
Kai's assumptions, to be overruled by the owner: the link keeps landing on the long page (index.html) as today;
the switch is the first thing in the header of both pages; it is hidden in print.

Builder: Opus. Worktree `git worktree add C:/Users/stian/Prosjekter-u41 -b u41-format-switch 2c94172` from the git
root C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u41/max. Read first: rule 10 (CLAUDE.md
l.60–71); `docs/sws/build.py` header block l.905–930 and SHORT_LINE l.167, its CSS and the `--check` mode (l.781);
`docs/sws/build_short.py` header l.545–560, how it reads the long page (l.28, l.111); `tests/test_sws_report.py`,
`tests/test_sws_short.py`; `.github/workflows/sws-report.yml`; `tasks/reports/U39.md`.

A. One list of formats, defined once (in build.py, imported or read by build_short.py — whichever the scripts
   already allow without a new dependency): (file, label, one-line description), today `index.html` "Full report"
   and `short.html` "Short page (4 printed pages)". Both headers render the same switch from that list: a row of
   links at the top of `<header>`, the current page marked (`aria-current="page"`, visually distinct), the others
   plain links. Same CSS in both pages; `@media print { .formats { display:none } }`. Replace SHORT_LINE in the
   long page with the switch (one place, not two). The short page's lede sentence about the long page stays.
   Nothing else in either page changes: after the rebuild, `git diff --stat` and a diff of index.html and
   short.html against 2c94172 show changes in the header and style blocks only — paste that diff summary in the
   report. No number, link target, anchor or figure changes.
B. `python docs/sws/build.py --check` and `python docs/sws/build_short.py --check` pass; both tests pass; add a
   test (in test_sws_short.py or a new small one) that each page's switch lists every format in the list and
   links to a file that exists, and that exactly one entry is current on each page. The workflow runs both
   builds already (U39) — confirm, do not restructure.
C. Verifier subagent (qc-falsifier): open both pages (a browser screenshot or the rendered HTML read as a user
   would); the switch is visible at the top, switches both ways, hides in print (check the CSS); the diff is
   header-and-style only; no personal names, drawing numbers or user paths added. Report `tasks/reports/U41.md`
   (≤ 1 page: what changed, the diff summary, verifier findings, Needs Stian ≤ 2 — the landing page question is
   one), `tasks/TASKS.md` U41 entry whose "Done when" cites U39's report and this brief. Commit on the branch; no
   merge, no push. Notes in C:/Users/stian/agent-notes/<nautical name>.md (check the folder for taken names;
   sign every answer `— <name>`). Timebox 1.5 hours. — Kai

## U43 — export increment for U41, then the Pages snapshot (Kai, 9 Nov 14:4x)

Owner, 9 Nov: the format switch (U41) is wanted on the live link. Preconditions Kai confirmed: U41 merged into local
main as de0171e (Prosjekter-u05/max), both `--check` ok, 7 tests pass, pushed to D:/git/prosjekter.git. Read this
file's "## U38" B(1)–(4) and "## U40" first: same method, same checks, same shape.
A. Export increment from the clone C:/Users/stian/export-v3/export: range 2c94172..de0171e, max/ subtree,
   first-parent (the U41 merge becomes one commit), rewrite with the same tool and map as U38/U40, graft on
   54afb64 (= GitHub fjordbit/max main; verify with `git ls-remote`). Scan the tip: persons and drawings 0.
   Tests at the tip: `pytest -q tests/test_sws_report.py tests/test_sws_short.py`, `python docs/sws/build.py
   --check`, `python docs/sws/build_short.py --check` (the project venv may lack `markdown`; U41's worktree venv
   C:/Users/stian/Prosjekter-u41/max/.venv has markdown==3.7, the CI version — use it, do not install into the
   project venv). Report to C:/Users/stian/export-v3/REPORT-3.md. No push — Kai pushes.
B. Pages snapshot in C:/Users/stian/publish/SWS (last snapshot f545164; `git show --stat f545164~1` shows what a
   snapshot carries): replace `sws/` and `docs/sws/` with the same paths from the export tip of step A; keep
   `docs/sws/sws_demo_720p.mp4`; rebuild `docs/sws/index.zip` from the new index.html the same way as before;
   keep the rev128–130 docx that f545164 added. Fix any link that points at a repository path the snapshot does
   not carry, as U40 did. Scan the publish tree with scan_tree.py: persons and drawings 0; report the rest by
   file. `git status` must show only sws/ and docs/sws/ changes. Commit "SWS snapshot from MAx de0171e: U41 format
   switch"; no push — Kai pushes to both remotes.
C. Hand back ≤ 10 lines: export tip and counts; snapshot commit; scan residue by file; the push commands. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (check taken names; Pintle built U41). Timebox 1.5 hours. — Kai

## U42 — the short page becomes the landing page and the easy read; readability of the whole from the manager's side (Kai, 9 Nov 15:2x)

Owner, 9 Nov (three answers): the 4-page short and the "easy read" are the same page; the link lands on it; it
points into the main report; "it should contain all management needs and all links"; scope "readability of it
all — up to you". Kai's scope: (1) the short page is rewritten for a manager who has ten minutes, carrying
everything management needs for the decisions in front of them, every number still a link into the main report;
(2) the main report changes only where the design pass says a manager following a link needs orientation
(the summary block; not the parts); (3) the link lands on the short page. Owner's method for this unit, his words:
"one pass with Fable for design work, then Codex write, then we do MAx run as a verification that all is good and
all is kept true and all links work". Rule 10 throughout: nothing selects a grade, thickness or head; every
number from the record with its status and its link; where the record is silent, say so.

Builder: Opus, orchestrating. Worktree `git worktree add C:/Users/stian/Prosjekter-u42 -b u42-easy-read de0171e`
from the git root C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u42/max. Use the venv at
C:/Users/stian/Prosjekter-u41/max/.venv (has markdown==3.7; do not install into the project venv). Read first:
rule 10 (CLAUDE.md l.60–71); `tasks/reports/U39.md` and `U41.md`; `docs/sws/build_short.py` (sections, link()/href()
l.108–118, FORMATS use); `docs/sws/build.py` FORMATS l.167–182 and the summary block (abstract, key numbers,
findings, open); `tests/test_sws_short.py`; `docs/paper/peer_read_2026-11-08.md` C.9–C.10; register
`sws/data/sws_data_sources.md` l.329–361; this file's "## U39" (the rulings and their status) and "## U36 addendum".

A. Design pass on Fable (owner's call for this unit): a subagent on model claude-fable-5-1 writes
   `docs/design/sws-easy-read.md` (≤ 2 pages): who reads (management choosing between heads and grades, and the
   head designer's management), the decisions in front of them (from the record: grade, head, thickness basis,
   storage number, wire diameters, R5, supplier sheet), what each decision needs on the page to be decidable
   without opening the main report, the reading order (purpose → what is decided → what is open → results →
   acceptance → what the numbers say), per section: intent, the facts it must carry, the links it must carry,
   what it must not say (selections, unlinked numbers, status upgrades); the main report's summary block: what a
   manager arriving by link needs there and nothing more; the landing-page mechanics (below); an acceptance
   checklist the verification can run. It reads the current short.html and the record; it does not write prose
   for the page. Rule 10 check by the subagent itself against the register before it hands over.
B. Codex writes: the prose of the short page (the text in build_short.py's section templates) rewritten to the
   design, through the project's Codex provider (`max_core/providers/codex_cli.py`, `codex exec`; the 8 Nov
   empty-folder test passed, see secretary log 8 Nov l.135) or `codex exec` directly from the worktree with the
   design note, the current build_short.py and the rule-10 text as its input. Codex may not change: any
   `link(...)`/`href(...)` call target, any number, FORMATS, the tests. If Codex is unreachable within 20 minutes
   of trying, write the prose yourself and say so in the report — the owner wants to know which model wrote it.
   Landing page (Kai's choice; the design pass may argue against it in its note, then follow the design): the
   short page is built as `docs/sws/index.html` and the main report as `docs/sws/report.html`; the two constants
   (build.py OUT l.35, build_short.py's `index.html#` l.111 and LONG l.28) and FORMATS change, labels "Short page"
   (no page count typed) and "Full report"; README.md l.83, the workflow comment and paths, tests, and build.py's
   publish helper (l.816) follow. Every existing `index.html#<id>` anchor must still resolve on report.html
   (same ids); the report lists what else links to index.html outside docs/sws (grep the repo; tasks/reports and
   agent notes are allowed to go stale, say so).
C. Verification, the owner's "MAx run": try the MAx judge first — `max_core/flows/max/max-architect-writer-judge
   .chart.json` with the design note as the architect's output and the built page as the writer's output, judge on
   Fable; read `docs/design/flow-driver.md` and the chart for how a run is started and what the judge receives.
   Cap 1 hour on getting the run to start. If it runs: its findings go in the report verbatim under "MAx judge".
   If it does not run within the cap: say exactly what is missing (so Kai can brief a MAx unit) and fall back to a
   qc-falsifier subagent on Fable with the design note's acceptance checklist. Either way, deterministic checks
   must pass: `build.py --check`, `build_short.py --check`, all tests, plus a link check that every href in both
   pages resolves (file exists; anchor id present) — add it to the tests if it is not there. Both pages still
   print: the short page ≤ 5 A4 pages.
D. Report `tasks/reports/U42.md` (design summary, who wrote the prose, what changed in the main report's summary
   block, verification route taken and findings, link check counts, Needs Stian ≤ 3), `tasks/TASKS.md` U42
   entry citing the design note and this brief. Commit on the branch; no merge, no push. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (Pintle and Chock are taken today; sign every answer). Timebox
   4 hours; report at 2 hours where you are if B or C is slipping. — Kai

## U44 — export increment for U42, then the Pages snapshot (Kai, 9 Nov 16:1x)

Owner, 9 Nov: the short page is the landing page and the easy read; publish it. Preconditions Kai confirmed: U42
merged into local main as 0ef5b68 (Prosjekter-u05/max), both `--check` ok, 11 tests pass, pushed to D:. Read this
file's "## U38" B(1)–(4), "## U40" and "## U43" first; same method, same checks. The file layout changed in U42:
`docs/sws/index.html` is now the short page, `docs/sws/report.html` the full report (old `short.html` deleted; a
script in index.html forwards old `index.html#<id>` links to report.html); `docs/design/sws-easy-read.md` is new.
A. Export increment from C:/Users/stian/export-v3/export: range de0171e..0ef5b68, max/ subtree, first-parent, rewrite
   with the same tool and map, graft on 66b43f9 (= GitHub fjordbit/max main; verify with `git ls-remote`). Scan tip
   and increment: persons and drawings 0. Tests at the tip with the venv C:/Users/stian/Prosjekter-u41/max/.venv:
   both `--check`, `pytest -q tests/test_sws_report.py tests/test_sws_short.py`. Report to
   C:/Users/stian/export-v3/REPORT-4.md. No push — Kai pushes.
B. Pages snapshot in C:/Users/stian/publish/SWS (last snapshot 4903d86): replace `sws/` and `docs/sws/` with the
   same paths from the export tip; `docs/sws/short.html` goes away, `report.html` arrives; keep the mp4; keep the
   rev124–130 docx; rebuild `docs/sws/index.zip` from the new report.html + mp4 (it is untracked; leave it
   untracked as before). The publish root `docs/index.html` links to `sws/` — that now lands on the short page, as
   wanted; check its link text still fits. Unlink the questions-note links as U40/U43 did. Scan the publish tree:
   persons and drawings 0; report the rest by file. `git status` must show only sws/ and docs/sws/ changes (plus the
   untracked zip). Commit "SWS snapshot from MAx 0ef5b68: U42 short page as landing page, full report → report.html";
   no push — Kai pushes.
C. Hand back ≤ 10 lines as U43 did. Notes in C:/Users/stian/agent-notes/<nautical name>.md (Pintle, Chock, Thwart
   are taken today). Timebox 1.5 hours. — Kai

## U45 — MAx: the architect's brief reaches the reviewer and the judge (Kai, 9 Nov 17:1x)

Owner, 9 Nov: "do the small MAx unit for the chart gap". The gap (U42 report §C, Thwart): in
`max_core/flows/max/max-architect-writer-judge.chart.json` the judge receives only task / current / previous / review
and the reviewer only task / draft, so neither sees `architect.brief`; a judge cannot check a draft against a brief it
never gets. U42 worked around it by pasting the design note into the task. Second observation, not this unit:
`max run` cannot seed a ready-made architect or writer output (U42 needed a harness outside the repo) — list it under
"Needs Stian" with a one-line proposal, do not build it.

Builder: Opus. Worktree `git worktree add C:/Users/stian/Prosjekter-u45 -b u45-brief-to-judge 0ef5b68` from the git
root C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u45/max. Project venv
C:/Users/stian/Prosjekter-u05/max/.venv for the engine tests (it has typer/yaml; the SWS page tests are not this
unit's). Read first: rule 10 (CLAUDE.md l.60–71); the record this rests on: ADR 0011 (`docs/adr/`), the U21 design
`docs/design/flow-driver.md` and whatever page defines block inputs and the agent prompts (find it; `docs/design/`
and `max_core/agents/`); the chart json (blocks `reviewer_codex`, `judge`, their `inputs`; edges l.? `architect.brief
→ writer.brief`); `max_core/flowcheck.py` and `preflight.py` (what a new wire must satisfy); the existing chart tests;
`tasks/reports/U42.md` §C; Thwart's notes C:/Users/stian/agent-notes/thwart.md for the harness runs.

A. Record first. If the design page states the judge's and reviewer's inputs as a closed list, this unit changes
   the design on the owner's ruling of 9 Nov: add a dated paragraph to the design page (what changed, why: U42 run 1
   could not check the checklist without the brief) — the owner has ruled, so this is recording a ruling, not the
   builder amending the record to fit. Cite it in "Done when". If the record is silent, say so and proceed.
B. Build: two data edges `architect.brief → reviewer_codex.brief` and `architect.brief → judge.brief`, the `brief`
   input declared on both blocks, and the reviewer's and judge's agent prompts told what the brief is and what to do
   with it (check the draft against it; findings that cite the brief's own acceptance checklist when it has one).
   The brief must not be optional in a way that silently passes when absent: if `brief` is missing at run time the
   judge's verdict says so. The default-loop chart (`max-default-loop.chart.json`) gets the same edges only if it has
   an architect block; otherwise untouched. flowcheck and preflight pass; Studio renders the two new wires (one
   screenshot or the Studio's own chart check); the chart's schema version and ADR 0011 status are unchanged unless
   the design page says a wire change bumps them.
C. Prove: a test that the chart carries both edges and both inputs; a dry run of the chart through `Driver` with
   stub providers (the pattern the engine tests already use) showing the judge's and reviewer's input dicts contain
   `brief`; the full engine test suite passes; `ruff` clean. Verifier subagent (qc-falsifier): conformance to the
   design page as amended, no other block or edge changed (diff of the json), prompts say nothing that selects or
   overrides the ladder. Report `tasks/reports/U45.md` (≤ 1 page; "Needs Stian" ≤ 2 incl. the seeding proposal),
   `tasks/TASKS.md` U45 entry citing the design page. Commit on the branch; no merge, no push. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (Pintle, Chock, Thwart, Gaff taken today; sign every answer).
   Timebox 2 hours. — Kai

## U46 — the easy read: a third SWS page that explains the whole thing simply, every statement still traceable (Kai, 9 Nov 17:5x)

Owner, 9 Nov evening: the short page (U42) is the dense one and he likes it — "definitely dense enough". The easy
one is missing: "the one for easy readability I do not see; it is also the one that most easily will show if we
actually understand all this, because the simpler you can explain something the higher level you understand it".
So: a third page, `docs/sws/easy.html`, third FORMATS entry "Easy read" (short page stays the landing page; the
owner may move the landing later). Reader: a smart person with no magnetics and ten minutes — a manager's manager,
a new colleague, the rope maker's sales engineer. Test of success (the owner's): after reading, the reader can say
in their own words what the sensor head is, why temperature matters, what the three grades and three heads trade,
what the standard requires and what is unknown about it, what has been decided and by whom, and what is still open
and what closes each. Rule 10 still binds: nothing selects; every factual statement is traceable to the record;
numbers only where a reader needs one, each a link; where the record is silent, say "we do not know yet, because …".
Plain words; an analogy is allowed when it is marked as one and does not claim more than the record. Short
sentences. No status codes in the text (no "D", "U", "C by script") — the status is said in words ("decided by the
owner on 8 Nov", "assumed, not measured") and the link carries the row.

Builder: Opus, orchestrating; same method as U42 (the owner's: Fable designs, Codex writes, MAx judges, the
deterministic checks always). Worktree `git worktree add C:/Users/stian/Prosjekter-u46 -b u46-easy-read 860894c`
from the git root C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u46/max. Venv
C:/Users/stian/Prosjekter-u41/max/.venv for the page builds and SWS tests (markdown==3.7); the project venv for
engine code. Read first: rule 10 (CLAUDE.md l.60–71); `tasks/reports/U42.md`, `U45.md`; `docs/design/sws-easy-read.md`
(U42's design: the decisions and their rows — reuse the facts, not the register); `docs/sws/build_short.py` (the
link()/href()/g() helpers and FORMATS use — import and reuse them, do not copy); `docs/sws/build.py` FORMATS;
`tests/test_sws_short.py`; this file's "## U39" rulings paragraph and "## U36 addendum"; register
`sws/data/sws_data_sources.md` l.7–11, l.181–192, l.329–361; `docs/paper/peer_read_2026-11-08.md` A–B.

A. Design pass on Fable (subagent, model claude-fable-5-1): `docs/design/sws-easy-read-plain.md` (≤ 2 pages): the
   reader; the ten sentences the reader should be able to say afterwards (the owner's test, written out); the
   order (what it is → why it is hard → what we tried → what we found → what is decided → what is open → what
   we do not know); per section: the facts to carry (each with its record source), which numbers a reader needs
   (few), allowed analogies and their limits, what must not be said; a glossary of ≤ 10 words (B_rope, knee,
   Hcj, one-piece half-ring, hard wire, …) each in one plain sentence with its source; the acceptance checklist
   (the ten sentences + rule 10 items + "no status codes in the prose"). The design agent does not write the page.
B. Codex writes the prose (`codex exec` or the project's provider; same constraints as U42: it returns text; the
   builder places it in `docs/sws/build_easy.py`, whose numbers and citations come through the shared helpers, never
   typed). If Codex is unreachable within 20 minutes, the builder writes and the report says so.
   Page: `docs/sws/build_easy.py` → `docs/sws/easy.html`, FORMATS gains ("easy.html", "Easy read", …) in build.py,
   so all three headers show three buttons; same styling family, larger type is fine; ≤ 3 printed A4 pages; one or
   two figures at most (the head concept; the options figure only if the design says a lay reader can read it);
   the glossary at the end. Workflow sws-report.yml: build and check easy.html too. README l.83 row updated.
C. Verification: (1) MAx judge with the brief now wired (U45): same harness route as U42 if `max run` still cannot
   seed — architect fixed to the design note (now reaching reviewer and judge through the `brief` wire, not pasted
   into the task), writer fixed to the built page text, reviewer Codex + judge Fable real; cap 1 hour to get a run
   going; report the judge's and reviewer's verdicts verbatim; note whether the brief arrived in their input (this
   is also U45's first real use — say so in the report). (2) qc-falsifier on Fable with the design's checklist; it
   also reads the page as the intended reader and writes the ten sentences back from the page alone — any it
   cannot write is a finding. (3) Deterministic: `build_easy.py --check`, a `tests/test_sws_easy.py` on the U39
   pattern (every number linked and present at its source; every href resolves; FORMATS complete on all three
   pages; no status-code tokens in easy.html prose), all SWS tests, both other `--check`s still pass.
D. Report `tasks/reports/U46.md` (who wrote the prose; the ten sentences and whether the falsifier could write them
   back; judge/reviewer verdicts; whether the brief arrived; Needs Stian ≤ 3 — landing page easy vs short is one),
   `tasks/TASKS.md` U46 entry citing the design note. Commit on the branch; no merge, no push. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (Pintle, Chock, Thwart, Gaff, Bitt taken today; sign every
   answer). Timebox 4 hours; at 2 hours report where you are if B or C slips. — Kai

## U47 — export increment for U45, U46 and the link fix, then the Pages snapshot (Kai, 9 Nov 19:0x)

Owner wants the easy read live tonight. Preconditions Kai confirmed: local main 5c4297f (Prosjekter-u05/max) =
U45 (engine: brief→judge), U46 (docs/sws/easy.html + build_easy.py, third FORMATS button), Kai's one-line link fix
in build_short.py; all three `--check` ok, 21 SWS tests pass, pushed to D:. Read this file's "## U38" B(1)–(4),
"## U43", "## U44" first; same method, same checks. Export tip on GitHub is f8eb3d5 (verify with `git ls-remote`).
A. Export increment from C:/Users/stian/export-v3/export: range 0ef5b68..5c4297f, max/ subtree, first-parent (two
   merges + one commit → three commits), rewrite with the same tool and map, graft on f8eb3d5. Scan tip and
   increment: persons and drawings 0 (the engine files from U45 are new to the scan — look at them). Tests at the
   tip: the three `--check`s and `pytest -q tests/test_sws_report.py tests/test_sws_short.py tests/test_sws_easy.py`
   with C:/Users/stian/Prosjekter-u41/max/.venv; `pytest -q tests/test_flows_m3.py` with the project venv. Report
   to C:/Users/stian/export-v3/REPORT-5.md. No push — Kai pushes.
B. Pages snapshot in C:/Users/stian/publish/SWS (last 9fc6ae1): replace `sws/` and `docs/sws/` from the export tip
   (`easy.html` and `build_easy.py` arrive); keep mp4 and docx; rebuild index.zip (untracked, as before); unlink
   questions-note links as before in all three pages; scan: persons and drawings 0; `git status` only sws/ and
   docs/sws/. Commit "SWS snapshot from MAx 5c4297f: easy read (third page), link fix"; no push.
C. Hand back ≤ 10 lines as U44 did. Notes in C:/Users/stian/agent-notes/<nautical name>.md (Pintle, Chock,
   Thwart, Gaff, Bitt, Thimble taken today). Timebox 1 hour. — Kai

## U48 — easy read and short page: the standard is on file; new analogy; register notes updated to the text (Kai, 9 Nov 23:3x)

Owner, 9 Nov 23:2x, reading the easy read: (1) "I do not want first lines to state like that" — the "What it is"
paragraph says the standard's band and smallest break are "said to" come from it and "its text is not on file".
That was true for the record until tonight: the owner has now put BS EN 12927:2019 on the machine
(C:/Users/stian/max-private/standards/BS-EN_12927-2019.pdf; copyright — never copy it or long passages into the
repo) and Kai extracted the governing clauses to C:/Users/stian/max-private/standards/EN12927-2019_ch14_extract.md.
Read that extract first. (2) "the analogy, use something else. it is flows after all … if there is a leak … use
smoke or something" — replace the horseshoe-magnet analogy with a flow-and-leak one (the method is literally
"magnetic flux leakage"): the field flows along the rope like water through a pipe; a broken wire is a crack, some
of the flow leaks out there, and the sensors sit where a leak would show. Mark it as an analogy with its limit as
before. (3) Repush tonight.

What the text says (clause numbers and short phrases may be quoted; nothing longer): 14.2.2 NOTE points to Annex B
for the flux density; **Annex B is informative**: B between 1,9 and 2,3 T "in a rope … having a maximum metallic
cross section Amax", over an axial extension of 0,5 × dmax; smallest rope ≥ 0,25 Amax, otherwise prove B ≤ 2,4 T.
**14.3.5.2 (normative)** performance test: reference piece with two wire breaks spaced s = d (≤ 50 mm), each with a
3 mm gap, fault between strand and core of a single-layer rope, "equivalent to 0,5 % of the metallic cross sectional
area of the rope tested"; signal amplitude ≥ 2 × envelope height, two breaks shown as two separated signals;
locked coil and/or stranded rope; verification before first use and at ≤ 12 months. The text speaks of metallic
cross section throughout; whether the project's sizing quantity is B_rope or B_wire is still **the owner's
reading, not yet given** — the page and the register state the text and leave the reading open. Rule 10: this
unit records facts from the text; it does not change any status letter or choose a reading.

Builder: Opus. Worktree `git worktree add C:/Users/stian/Prosjekter-u48 -b u48-standard-on-file 5c4297f` from the
git root C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u48/max; venv
C:/Users/stian/Prosjekter-u41/max/.venv. Read: rule 10; the extract; `docs/design/sws-easy-read-plain.md`;
`docs/sws/build_easy.py`, `build_short.py`; register `sws/data/sws_data_sources.md` l.24, l.35, l.191, l.192, l.348;
`tests/test_sws_easy.py`, `test_sws_short.py`.
A. Register (the record first): rows l.191 and l.192 — replace "not checked against the text" / "verify wording"
   in the notes column with the fact: "text on file (owner, 2026-11-09); Annex B (informative): 1,9–2,3 T in a rope
   characterised by its metallic cross section; the owner's B_rope / B_wire reading pending" and for l.192 "text on
   file (owner, 2026-11-09); 14.3.5.2: two breaks spaced d (≤ 50 mm), 3 mm gaps, fault equivalent to 0,5 % of the
   metallic cross-sectional area, signal ≥ 2 × envelope". Status letters unchanged (U stays until the owner reads
   and rules). Row l.348 notes: add "standard text on file 2026-11-09; the one-wire / two-wire translation is the
   head designer's, the text defines the fault by area (0,5 % of metallic area, two breaks)". Add a dated line under
   the register's change log if it has one. Reference [R5] l.24: add "(held: max-private/standards, not in the
   repository)".
B. Easy read `build_easy.py`: rewrite the "What it is" standard sentences to state the text: the standard sets a
   band for how strongly the rope is magnetised, in an informative annex, and a test with a reference fault equal
   to 0,5 % of the rope's steel area, two breaks a rope-diameter apart; the team has the text since 9 Nov 2026;
   which measure of magnetisation the project uses is the owner's call, still open — each a link to the register
   row. Replace the analogy (above). "What we do not know yet" first item: now "we do not yet know which measure
   of the rope's magnetisation the owner adopts; the standard's words are on file and point to the steel area" —
   plain words, link l.191. Any other "not on file" on the easy page goes the same way. Short page
   `build_short.py`: the Acceptance paragraph ("That reading remains U: the standard's text is not on file") and the
   "Induction has two readings" paragraph, and the open-list "Induction quantity" and "Wire diameters" items —
   same facts, same links; status stays U in the short page's style. Design note: add a dated line that the
   analogy changed on the owner's instruction and why.
C. Prove: all three `--check`; `pytest -q tests/test_sws_report.py tests/test_sws_short.py tests/test_sws_easy.py`;
   the easy page still ≤ 3 A4 and the short ≤ 5 (print check); qc-falsifier (Fable): every new sentence against the
   extract (no claim beyond the text; "informative" said where Annex B is cited; no status letter changed; no
   reading selected; no verbatim passage longer than a short phrase in the repo; no identifiers). Report
   `tasks/reports/U48.md` (≤ ½ page; Needs Stian: his reading of the B quantity — one item), TASKS.md entry.
   Commit on the branch; no merge, no push. Notes in C:/Users/stian/agent-notes/<nautical name>.md (Pintle, Chock,
   Thwart, Gaff, Bitt, Thimble, Cringle taken today). Timebox 1 hour. — Kai

## U49 — export increment for U48, then the Pages snapshot (Kai, 9 Nov 23:5x)

Owner wants U48 live tonight. Preconditions Kai confirmed: local main 6655e8c (Prosjekter-u05/max) = merge of U48
(register notes l.25/191/192/348, easy read and short page wording, river analogy with two outside links on the easy
read); three `--check` ok, 21 SWS tests pass, pushed to D:. Read this file's "## U38" B(1)–(4), "## U43", "## U44",
"## U47" and cringle.md first; same method, same checks. Export tip on GitHub is 6f70bfc (verify with `git ls-remote
https://github.com/fjordbit/max.git main`).
A. Export increment from C:/Users/stian/export-v3/export: range 5c4297f..6655e8c, max/ subtree, first-parent (one
   merge → one commit), rewrite with the same tool and map, graft on 6f70bfc. Scan tip and increment: persons and
   drawings 0. Tests at the tip with C:/Users/stian/Prosjekter-u41/max/.venv: the three `--check`s and `pytest -q
   tests/test_sws_report.py tests/test_sws_short.py tests/test_sws_easy.py`. Report to
   C:/Users/stian/export-v3/REPORT-6.md. No push — Kai pushes.
B. Pages snapshot in C:/Users/stian/publish/SWS (last d8c54c9): replace `sws/` and `docs/sws/` from the export tip;
   keep mp4 and docx; rebuild index.zip (untracked, as before); unlink the questions-note links and the links to
   files not carried, as U47 did, in all three pages; the two new external links on the easy read (asnt.org,
   en.wikipedia.org) stay as they are; scan: persons and drawings 0; `git status` only sws/ and docs/sws/. Commit
   "SWS snapshot from MAx 6655e8c: standard on file, river analogy"; no push.
C. Hand back ≤ 10 lines as U47 did. Notes in C:/Users/stian/agent-notes/<nautical name>.md (Pintle, Chock, Thwart,
   Gaff, Bitt, Thimble, Cringle, Sheave taken today). No identifier values in notes. Timebox 1 hour. — Kai

## U50 — the pages are about the instrument, not about who said what: "the owner" out of the prose (Kai, 10 Nov 00:1x)

Owner, reading the live easy read, 10 Nov: "the owner said.. is this a text about me? or about the task?" and "link to
number, number link to me for instance or owner, not owner 100 times. fix this now, it reads really bad". Count now
(tags stripped): easy.html 24 × "the owner / owner's", index.html (short page) 15. Cause: rule 10 makes every ruling
attributable and the writers put the attribution into the sentences. The attribution belongs in the link.

Rule for this unit (wording only; no number, status letter, register row or selection changes):
1. A decided thing is stated as a fact about the instrument or the project: "The hardware range is −40 to +50 °C."
   The number (or the sentence, via `say`) stays a link to the register row / ruling it rests on; the link's `title`
   (hover text) carries the provenance, e.g. "decided 2026-11-08 (owner ruling), register l.360". `say()` already
   takes a `title` argument; `link`/`g`/`cite`/`reg` in build_short.py — extend with an optional title the same way
   if they lack one. The reader sees the fact; who and when is one hover or one click away.
2. An open thing says it is not yet decided and what closes it: "Not yet decided: which measure of magnetisation the
   project uses." No "the owner's call", "for the owner to define", "the owner rules".
3. Who decides, where a manager needs it (the short page's "What is open" list): one sentence above the list —
   "Unless another name is given, the open decisions are the project owner's" — and then name only the exceptions
   (management, the team, the rope maker, the supplier, the head designer). Target: "owner" appears at most 3 times
   in the visible text of each page (that sentence, and where a sentence truly cannot be said otherwise, e.g. "the
   editor's reading, not the owner's words" may become "the editor's reading, not a ruling").
4. Same treatment for narration of events: "Late that same evening, after the hardware-range ruling, the owner said
   more about storage" → state what holds and its status ("The same range would also cover storage and transport;
   this is stated but not yet a register row"), keep the link.
5. The full report (report.html, build.py) and the register are the record: do not touch their attribution. Only
   build_easy.py and build_short.py (and what they generate) change; report.html changes only if the builders
   regenerate shared header bits.
6. Nothing may become stronger than the record: a U (unverified) or A (assumed) item must still read as open or
   assumed after the rewording; a statement of the owner's that is not a register row must not read as decided.

Builder: Opus. Worktree `git worktree add C:/Users/stian/Prosjekter-u50 -b u50-task-not-owner 6655e8c` from the git
root C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u50/max; venv
C:/Users/stian/Prosjekter-u41/max/.venv. Read: rule 10; `docs/design/sws-easy-read.md` and `sws-easy-read-plain.md`
(add a dated line under each one's changes: attribution moved from prose to link titles on the owner's instruction,
10 Nov; where a design line prescribes "who decides" per item, the dated line supersedes it for the page text);
`docs/sws/build_easy.py`, `build_short.py`; tests `tests/test_sws_easy.py`, `test_sws_short.py` (a test that pins
the old attribution wording is updated to the new rule; add one test per page: visible-text count of "owner" ≤ 3).
Prove: all three `--check`; `pytest -q tests/test_sws_report.py tests/test_sws_short.py tests/test_sws_easy.py`;
print: easy ≤ 3 A4, short ≤ 5 (headless Edge --print-to-pdf, read /Count); qc-falsifier (separate subagent): every
changed sentence against its cited row — nothing stronger than the record (point 6), no status changed, nothing
selected, every removed attribution still reachable through the link/title, no identifiers. Report
`tasks/reports/U50.md` (≤ ½ page, before/after counts, Needs Stian), TASKS.md entry. Commit on the branch; no merge,
no push. Notes in C:/Users/stian/agent-notes/<nautical name>.md (taken: Pintle, Chock, Thwart, Gaff, Bitt, Thimble,
Cringle, Sheave, Bowline). Timebox 45 minutes. — Kai

## U51 — export increment for U50, then the Pages snapshot (Kai, 10 Nov 01:0x)

Same job as "## U49" directly above the U50 brief; read it and bowline.md first, with "## U38" B(1)–(4) and "## U47".
Preconditions Kai confirmed: local main 5972096 = merge of U50 (easy read and short page: attribution and dates in
link titles, tyre analogy, outside links removed; tests updated); three `--check` ok, 25 SWS tests, pushed to D:.
GitHub fjordbit/max main is 79e29a9 (verify with ls-remote).
A. Export from C:/Users/stian/export-v3/export: range 6655e8c..5972096, max/ subtree, first-parent (one merge → one
   commit), same tool and map, graft on 79e29a9. Scan tip and increment: persons and drawings 0 — the link `title`
   attributes are new text copied from register rows: look at them specifically. Three `--check`s and the three SWS
   test files (expect 25) at the tip with the U41 venv. No push.
B. Snapshot in C:/Users/stian/publish/SWS (last 2093ebc): `sws/` and `docs/sws/` from the export tip; keep mp4 and
   docx; rebuild index.zip (untracked); unlink questions-note links and links to files not carried, as before; there
   are no outside links any more (asnt / wikipedia must be gone); scan persons and drawings 0, hover titles
   included; `git status` only sws/ and docs/sws/. Commit "SWS snapshot from MAx 5972096: pages state the
   instrument; tyre analogy"; no push.
C. Hand back ≤ 10 lines as Bowline did, with the push commands. If the harness refuses to write REPORT-7.md, the
   hand-back is the report. Notes in C:/Users/stian/agent-notes/<nautical name>.md (taken today: Sheave, Bowline, Fid;
   gunwale.md exists). No identifier values in notes. Timebox 1 hour. — Kai

## U52 — the short page reads as a text about the instrument too: status letters, line numbers and file names out of the visible text (Kai, 10 Nov 01:2x)

Owner, 10 Nov 01:2x, told that the short page still carries status letters and register line numbers in nearly every
sentence: "remove it then, dont leave it like that". U50 (read "## U50" above with its rules 1–7, and fid.md) did the
attribution; this unit finishes the job on the short page and clears the leftovers on the easy read. A cold reader
(10 Nov) judged the short page "reads as a report of who said what"; its list is the work list below.
Wording and presentation only: no number, status, register row or selection changes; nothing stronger than the record.

Short page (`docs/sws/build_short.py` → index.html). It stays the dense page for a manager, ≤ 5 A4 (now 4):
1. No "( register l.NNN , D)" tags, no "l.NNN", no bare status letters D / C / A / U / S / M, no "[R29]"-style keys,
   no run or unit ids ("Run R5", "U36") in the visible text. The sentence or its number is the link (as `say()` does
   on the easy read; reuse or share that helper); file, line and status letter go into the link's hover title with
   the provenance.
2. Status in words, only where the reader needs it: A → "assumed", U → "not yet verified" or "not yet decided",
   open → "open". Decided and computed facts need no label; "model result" is said once per section, not per number.
   A sentence that was hedged by its letter must still read as hedged (U50 rule 6).
3. "management chooses" once, in the purpose paragraph; "Every number links to its source" once. Remove the
   duplicates the cold reader listed ("The standard is the minimum. EN 12927 §14 is the minimum"; adjacent repeats).
4. Table cells reading "record silent" → "–" with one line under the table: "– : the record has no value."
5. No file names or paths in captions, footers or prose (tasks/reports/…, docs/paper/figures/…, build_short.py,
   test file names). A caption says what the figure shows; the footer keeps one line: model results on assumed
   material data, not measurements.
6. Rewrite for a first reading, same facts: "Ratios are signal over twice the 0.11 mT p-p requirement, an unmeasured
   budget"; "Knee means volume beyond about 0.8 Hcj … an exposure screen, not loss"; "a quasi-static 2D A model"; "the
   A/B split"; "The options note carries the team's labelled view…" (say what it is or cut the sentence); the
   "Sources are the options note (C by script…" paragraph (cut; the links carry it); the "Historical envelope"
   item → "−40 / +80 °C was the original range, set by the ADC range. The hardware limit is now −40 / +50 °C."; the
   "further statement" paragraph → the same one-sentence "Proposed, not yet in the register: …" as on the easy read
   (see build_easy.py on main 5972096); the run-order sentences → "The dedicated head has no 3D model or broken-wire
   runs yet. Running them does not pick a head."
Easy read (`build_easy.py`) leftovers:
7. "(options note l.48)"-style cites in the text → the words are the link (`say`), no file-and-line in visible text;
   the figure caption's path and the footer's script/test names go (as point 5).
8. Glossary: an entry only for a term the body uses, under the name the body uses ("whole-rope reading (B_rope)",
   "steel-only reading (B_wire)"); drop entries the body never uses unless a link needs them.
9. The cold reader's unclear sentences, same facts in plainer words: "A third option is the recorded size."
   "Management records the thickness basis against the sizing rule." "Part 1 of the paper is design by analysis."
   "Their empty-head exposure is confined to tiny corner regions." The long "every N48SH and N40SH row … reads zero,
   from the dedicated head's first … to the wide head's last …" clause → cut to the fact.
   Do NOT resolve "40 mm, 52 mm and shared heads" (three heads) against "the 52 mm head is the shared head": if the
   record says both, leave the wording and report it under Needs Stian.
Both pages: who decides / "owner" counts and the no-date, no-time-of-day rules from U50 stay enforced.

Builder: Opus. Worktree `git worktree add C:/Users/stian/Prosjekter-u52 -b u52-short-page-plain 5972096` from
C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u52/max; venv C:/Users/stian/Prosjekter-u41/max/.venv.
Read rule 10; `docs/design/sws-easy-read.md` (the short page's design: add a dated line that status letters and
line references moved from visible text to hover titles on the owner's instruction, 10 Nov, superseding the design's
per-item status display for the page text) and `sws-easy-read-plain.md`; the two builders; the two test files.
Tests: update what pins the old display; add per page: visible text has no `l\.\d+`, no "register l", no
parenthesised bare status letter, no path-like token (`\w+/\w+\.\w+`), and the hover title of every link still
carries file and line (so nothing became untraceable). Prove: three `--check`; pytest on the three SWS files;
print short ≤ 5 A4 and easy ≤ 3 (headless Edge, /Count); qc-falsifier (separate subagent): every changed sentence
against its row — nothing stronger, every hedge kept in words, nothing selected, no identifiers in text or titles;
then a cold-reader subagent (fresh, no project context, visible text only): "what is this text about; does it read
as an engineer explaining an instrument or as a record of who said what; what is unclear" — fix what it finds on the
short page until its verdict is READS AS TASK or you are out of time, and report its last verdict verbatim.
Report `tasks/reports/U52.md` (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (taken: Sheave, Bowline, Fid, Kedge, Gunwale and all earlier).
Timebox 60 minutes. — Kai

## U53 — export increment for U52, then the Pages snapshot (Kai, 10 Nov 01:5x)

Same job as "## U51" and "## U49" above; read them, kedge.md and bowline.md first, with "## U38" B(1)–(4).
Preconditions Kai confirmed: local main c593422 = merge of U52 (short page and easy read: status letters, line
references and file names moved into hover titles; tests 29); three `--check` ok, pushed to D:. GitHub fjordbit/max
main is 78b9e8c (verify with ls-remote).
A. Export from C:/Users/stian/export-v3/export: range 5972096..c593422, max/ subtree, first-parent (one merge → one
   commit), same tool and map, graft on 78b9e8c. Scan tip and increment: persons and drawings 0, hover `title`
   attributes included (many new ones). Three `--check`s and the three SWS test files (expect 29) at the tip. No push.
B. Snapshot in C:/Users/stian/publish/SWS (last 0e01f10): `sws/` and `docs/sws/` from the export tip; keep mp4 and
   docx; rebuild index.zip (untracked); unlink questions-note links and links to files not carried, as before — and
   after unlinking, the VISIBLE text must still contain no file path, no "l.NNN" and no "not in this snapshot" note
   (such notes go in the hover title only); scan persons and drawings 0, titles included; `git status` only sws/ and
   docs/sws/. Commit "SWS snapshot from MAx c593422: pages in plain text, sources in hover titles"; no push.
C. Hand back ≤ 10 lines as Kedge did, with the push commands. Notes in C:/Users/stian/agent-notes/<nautical name>.md
   (taken today: Sheave, Bowline, Fid, Kedge, Marlin; gunwale.md exists). No identifier values. Timebox 1 hour. — Kai

## U54 — the easy read rewritten to help someone understand: what we have done, what we found, where we are, what is next (Kai, 10 Nov 02:0x)

Owner, 10 Nov ~02:00, after U50/U52: "readable should not lose anything, it should say the same only in short, like
you are talking to someone with little but some knowledge of this, or even none, and keep it light. The technical
can do the heavy lifting; we do not force all these rules in readable other than the safety and sanity and
correctness." And the acceptance: "push it when it reads like it is to help someone understand what we have done,
what we have found, where we are, and what is next."
So the easy read (docs/sws/build_easy.py → easy.html) is rewritten as a piece of explaining, not a linked record.
The short page (index.html) and the full report are the technical pages; they are NOT changed in this unit.

What the page is now:
1. Voice: one engineer telling a curious colleague from another field. "We", active verbs, short sentences, plain
   words, light — no stiffness, no legal hedging on every line. A technical term appears only if the reader needs
   it later, explained once in passing; no glossary section unless three or more terms survive (then ≤ 5 entries).
2. Shape, in this order, with these headings (wording of headings may be tuned, order may not):
   - one opening paragraph: what the instrument is and why it exists (broken wires inside a hoist rope cannot be
     seen; this head finds them), then the tyre-under-water analogy (keep the paragraph from main, it is the
     owner's picture; tune only for flow);
   - What we have done; What we have found; Where we are; What is next.
   "Where we are" carries what is fixed and what is still open, in words a manager can repeat. "What is next" says
   who brings what (the supplier's figures for the magnets, the rope maker's wire sizes, the reading of the
   standard, management's choice of grade / head / thickness, the 3D runs for the smaller head) and the order that
   follows from it — including: the models are not refined further until the supplier's figures are in.
3. Loses nothing: every fact a reader of the short page would carry away is here in some form — the three heads,
   the three grades and how they differ, the two readings of the rope's magnetisation and why it matters, the
   temperature picture (sized at +45 °C covered, hardware −40/+50 °C, storage/transport not yet set, the open empty
   half as the demanding case, keeper plate not modelled), the acceptance picture (the standard as the minimum,
   fault defined by steel area, the two-wire case on the 52 mm rope exceeding the 0.5 % wording on the modelled
   rope), the 3D signal result in one plain sentence with at most two numbers, and every open item. Short does not
   mean dropping a topic; it means one or two sentences per topic. Few numbers: only those a reader needs to
   follow the story; the rest stay on the short page, one link away.
4. Rules that DO bind (safety, sanity, correctness): nothing false and nothing stronger than the record (an
   assumed, unverified or undecided thing still reads as such — said once and plainly, e.g. one early sentence "all
   results here are computer models on assumed material data; nothing has been measured yet", not a hedge per
   line); it is an aim, not a compliance claim; nothing is selected (grade, head, thickness, reading of the
   standard) — the page may say what the numbers favour only where the short page's "What the numbers say" does,
   and as that; no identifiers; "owner" ≤ 2, no dates or time-of-day narration, no status letters, line references,
   file names or unit ids (U50/U52 rules).
5. Rules that do NOT bind here: a source link per sentence, hover provenance per sentence, the "ten sentences" of
   the old design note. Links are a help: each section ends with (or carries inline) a few links into the short
   page / full report where the reader finds the detail ("the numbers are in the table on the short page"). Every
   NUMBER on the page must still be generated from, or checked by the build against, its source (`g()` / `link()`
   or an equivalent check in `--check`), so the page cannot drift from the record.
6. ≤ 3 A4 printed; one figure (the head concept) stays.

Builder: Opus. Worktree `git worktree add C:/Users/stian/Prosjekter-u54 -b u54-easy-read-voice 82b02d7` from
C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u54/max; venv C:/Users/stian/Prosjekter-u41/max/.venv.
Read first: rule 10; the short page as built (docs/sws/index.html visible text, and build_short.py) — it is your
source of facts; the current build_easy.py; `docs/design/sws-easy-read-plain.md` — add a dated §9 line: on the
owner's instruction of 10 Nov the easy read is an explanation in four parts; per-sentence anchoring and the ten
sentences are superseded for this page; correctness is proved against the short page and register as a whole.
Tests (tests/test_sws_easy.py): replace the per-sentence-link requirement with: every number in the visible text
is produced from or matches its source; the four headings exist in order; U50/U52 visible-text rules; a
completeness list (the topics in point 3, as keywords or anchors) is present; internal links resolve.
Prove, in this order: three `--check`; pytest on the three SWS files; print ≤ 3 A4;
(a) qc-falsifier (separate subagent, gets the short page + register as the record): every claim on the easy read
    is true to them, nothing stronger, nothing selected, every topic of point 3 present — list anything lost;
(b) cold reader (separate, fresh subagent, visible text of easy.html only, told nothing about the project): reads
    once, then answers from memory: what have they done, what have they found, where are they, what is next — and
    says whether the page read as someone helping them understand, what was heavy, what they would cut. Compare its
    four answers with the short page: wrong or missing answer = the page failed there; fix and re-run with a NEW
    cold reader (never the same one twice). Stop when a fresh reader answers all four correctly and says it read
    as help, or at the timebox. Report the last reader's four answers and verdict verbatim.
Report `tasks/reports/U54.md` (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (taken today: Sheave, Bowline, Fid, Kedge, Marlin + the U53 builder's;
check the folder). Timebox 75 minutes. — Kai

## U55 — export increment for U54, then the Pages snapshot (Kai, 10 Nov 02:5x)

Same job as "## U53" above; read it, "## U51", "## U49", ratline.md and kedge.md first, with "## U38" B(1)–(4).
State: local main 224704b = merge of U54 (easy read rewritten in four parts, four figures and the demo video;
tests 32); three `--check` ok, pushed to D:. NOTE: U53's export (tip 1bd191b in C:/Users/stian/export-v3/export) and
snapshot (54db766 in publish/SWS) were built but NOT pushed; GitHub fjordbit/max main is still 78b9e8c and the Pages
repos are at 0e01f10. That is expected — the owner wants one push. Build on top of the unpushed work:
A. Export from C:/Users/stian/export-v3/export: range 82b02d7..224704b, max/ subtree, first-parent (one merge → one
   commit), same tool and map, graft on 1bd191b (the local export tip; verify it is an ancestor chain
   78b9e8c → ffc197f → 1bd191b and that ls-remote still returns 78b9e8c, so the final push is a fast-forward of
   three commits). Scan tip and the whole unpushed increment 78b9e8c..tip: persons and drawings 0, hover titles and
   figure captions included. Three `--check`s and the three SWS test files (expect 32) at the tip. No push.
B. Snapshot in C:/Users/stian/publish/SWS on top of 54db766: `sws/` and `docs/sws/` from the export tip; the easy
   read now uses four figures and embeds docs/sws/sws_demo_720p.mp4 — check every image and the video the page
   references resolves in the snapshot (embedded data or a file that is carried); keep mp4 and docx; rebuild
   index.zip (untracked); unlink as Ratline did (tools/unlink8.py), visible text free of paths, "l.NNN" and
   snapshot notes; scan 0; `git status` only sws/ and docs/sws/. Commit "SWS snapshot from MAx 224704b: easy read
   as an explanation, with figures and video"; no push.
C. Hand back ≤ 10 lines with the push commands. Notes in C:/Users/stian/agent-notes/<nautical name>.md (list the
   folder; avoid every existing name). No identifier values. Timebox 1 hour. — Kai

## U56 — the working area stated and plotted; B_rope reading recorded; EN 12927 terms (LD / LMA) (Kai, 10 Nov 19:3x)

Owner, 10 Nov evening, three rulings. Record them in the register first (status D, owner statement 10 Nov 2026),
then carry them to all three pages (full report, short page, easy read). Attribution and dates live in the register
and hover titles, never in page prose (U50/U52 rules stand; "## U50", "## U52", "## U54" above).

1. **Reading of the standard: B_rope, with B_wire shown beside it.** Register l.191 and l.333 (and every "pending /
   open / the owner's call" echo of it: design.md §6, design_inputs.md l.6, pages) → decided: the 1,9–2,3 T of Annex B
   is read as B_rope = all flux through the rope (steel and the air between the wires) divided by the total steel
   area; B_wire = the flux density in the steel alone, 8–17 mT lower on the models, is reported beside it as margin.
   Neither is "one wire": both use the total steel area. Reasons to record as the editor's (Kai's) inference, not
   as the standard's text: 14.2.1 requires a flux check with calibrated equipment, which measures total flux; for
   the solid test piece Annex B allows, the two are equal; Annex B is informative and does not say. Not a
   compliance claim.
2. **We design a working area, not a point.** Owner: "we are designing the working area of magnet and yoke sizes to
   be selected from, and we wanted this as a clear plot. Of course we do not want to be all in one corner, that
   makes any design fault destructive … we should not search for a local minimum only but a minimum 'area', i.e.
   not one spike but where we have the best results even if the materials are slightly outside the values we get
   specified." New register rows (D): (a) the deliverable of the magnetic design is the window of magnet thickness
   (and the yoke that follows from it) between lm_min and lm_max per head and grade, from which a size is selected;
   (b) selection principle: a size inside the window with margin to both limits, chosen where the result is good
   over a region and tolerant of material values off their specified figures — not the minimum, not a single best
   point. Nothing is selected in this unit; the thicknesses quoted so far are the window's lower edge and every
   page must say so wherever it quotes them.
   **The plot** (new, sws/figures/decided/, made by script from sws/data/decided_rerun.json — NO new FE runs, the
   8 Nov ruling stands): per head (three panels or one clear panel for the shared head + small multiples), magnet
   thickness on x, B_rope on y, the worst-corner curve (hard wire, +45 °C, largest rope) and the best-corner curve
   (easy wire, −40 °C, smallest rope) per grade, the 1.92 T and 2.30 T limits, the allowed window shaded, lm_min /
   lm_max marked, the record sizes (17.2 / 19.1 / 20.1) marked, B_wire as a thin companion line where on file.
   A reader must see at a glance: this is the area, here are its edges, here is where the quoted sizes sit. If the
   yoke is not an independent variable on file (flux-rule yoke), say so in the caption and show yoke wall as a
   second axis or a small companion panel; do not invent a sweep. If the data on file cannot draw a part of this,
   draw what it can and list the missing runs in the report (for after the supplier's figures).
   Short page and full report: the plot + two or three sentences. Easy read: the idea in plain words (we map the
   area that works and pick inside it, away from the edges) + the plot or a link to it; stays ≤ 3 A4.
3. **Nomenclature follows EN 12927.** LD = local discontinuity (replaces LF / "local fault/flaw" as the term), LMA =
   loss of metallic cross-sectional area. Register, design notes that feed pages, report, short page, easy read.
   Where the pages list abbreviations / glossary: LD and LMA defined with the standard's words (clause map (c),
   3.12, 3.13, Table 1), and the other names given there once: "LF, local flaw / local fault — the term in ASTM
   E1571 and much of the literature". Add an abbreviations list to a page that has none only if it uses three or
   more abbreviations. Do not rename result keys, file names or figure file names; the spec docx is not touched
   (Word master is the owner's) — list its LF occurrences in the report.

Builder: Opus. `git worktree add C:/Users/stian/Prosjekter-u56 -b u56-working-area 224704b` from
C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u56/max; venv C:/Users/stian/Prosjekter-u41/max/.venv.
Read first: rule 10 (CLAUDE.md l.60–71); sws/data/sws_data_sources.md l.186–195, l.300–340; the rerun note
sws/fem-2d/sws_decided_rerun_2026-11-07.md §heads; sws/figures/decided/README.md + make_decided_figures.py; the three
page builders in docs/sws/; the clause map at C:/Users/stian/max-private/standards/ (read only, never copied into
the repo beyond short paraphrase). Prove, in this order: three `--check`; pytest on the SWS test files (32 now; add
tests: no visible "LF" outside the abbreviations entry, the window figure exists and is referenced on all three
pages, no page says the B reading is open); print easy ≤ 3 A4; qc-falsifier (separate subagent: every changed claim
true to register and json, nothing selected, limits and curves in the plot match the json); cold reader on the easy
read (fresh subagent, visible text only: "what is the working area and why not the minimum?" answered correctly).
Report tasks/reports/U56.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (list the folder; avoid every existing name). No identifier values.
Timebox 90 minutes. — Kai

## U57 — export increment for U56, then the Pages snapshot (Kai, 10 Nov 20:5x)

Same job as "## U55" above; read it, "## U53", "## U51", bulwark.md, ratline.md and kedge.md first, with "## U38"
B(1)–(4). State Kai confirmed: local main db05b45 = merge of U56 (register "Rulings of 2026-11-10": B_rope reading,
working area + selection principle; new figure sws/figures/decided/working_area.png used on all three pages; LD /
LMA terms; tests 37 over the four SWS test files incl. tests/test_sws_u56.py); three `--check` ok; pushed to D:.
GitHub fjordbit/max main is 9f3beec and the export clone's tip is 9f3beec (verify both with ls-remote / log);
publish/SWS is at ed8274c, pushed.
A. Export from C:/Users/stian/export-v3/export: range 224704b..db05b45, max/ subtree, first-parent (one merge → one
   commit), same tool and map, graft on 9f3beec (the push must be a fast-forward of one commit). Scan tip and
   increment: persons and drawings 0, hover titles, alts and figure captions included. Three `--check`s and the four
   SWS test files (expect 37; say so if a test cannot run in the export tree and why) at the tip. No push.
B. Snapshot in C:/Users/stian/publish/SWS on top of ed8274c: `sws/` and `docs/sws/` from the export tip; the new
   working-area figure must resolve on index.html, report.html and easy.html (embedded data or a carried file);
   keep mp4 and docx; rebuild index.zip (untracked); unlink as before (tools/unlink8.py), visible text free of
   paths, "l.NNN" and snapshot notes; scan 0; `git status` only sws/ and docs/sws/. Completeness: every figure,
   table and the video the three pages reference is present and renders; the short page shows LD and LMA explained
   once; no page says the reading of the standard is open. Commit "SWS snapshot from MAx db05b45: the working area,
   the B_rope reading, EN 12927 terms"; no push.
C. Hand back ≤ 10 lines with the push commands. Notes in C:/Users/stian/agent-notes/<nautical name>.md (list the
   folder; avoid every existing name, Clew is taken). No identifier values. Timebox 1 hour. — Kai

## U58 — a fourth page: "Hardware selection" (the electronics), on the top menu (Kai, 10 Nov 21:2x)

Owner, 10 Nov evening: the HW design starts with the acquisition electronics; he wants "some brief ready and added
to the page on a hardware selection top menu". An outside electronics expert will be hired and needs a few cases to
choose from. Nothing is selected by us; the page presents the cases.

What exists (outside the repos, made by Kai tonight): C:/Users/stian/hw_round_2026-11-10/ — brief_round1.md (blind
design task, requirements only), answers/2026-11-10/*.md + round.json (five models: Fable 5.2, GPT 5.6 Sol xhigh
and max, Grok 4.7, Grok 4.6), synthesis_round1.md (Kai), brief_round2.md (challenge: four cases A–D, D = the head
designer's choice). Round 2 is running; its answers will be in answers_round2/2026-11-10/ and Kai will add
synthesis_round2.md. All passed the masking gate (0 hits). In the repo: spec rev130 render §4, §6, §7, §10
(sws/spec/rendered/…rev130.md), sws/hw-selection/ (sync, stand-off, angular studies).

Build:
1. Carry the round material into the repo as the page's sources: `sws/hw-selection/rounds/2026-11-10/` (both
   briefs, the five round-1 answers + round.json, synthesis_round1.md; round 2 when Kai says it is in). Scan 0.
   A README there: what a round is, that answers are model output and every datasheet figure in them is from the
   models' memory, unverified.
2. `docs/sws/build_hardware.py` → `docs/sws/hardware.html`, and one more entry in build.py's formats list so all
   four pages show the switch "Hardware selection" (formats_nav; see the comment at build.py l.177). `--check` as
   the other builders. Tests in tests/test_sws_hardware.py.
3. The page, ≤ 3 A4, in the voice of the short page (U52 rules: no attribution, dates, status letters, line
   numbers or file names in the visible text; sources in hover titles / links; "owner" ≤ 2; no personal names —
   "the head designer" is the role). Sections, in this order:
   - What the electronics in one half must do: the requirements, as a short list (from brief_round1.md, each
     traceable to the spec section it came from: §4 sample rate, §6 16 bridges and neighbour differencing, §7 noise
     0.10 mT, §9 temperature range, §10 RS-422, sync 1 ms). LD and LMA as on the short page.
   - The four cases, A–D, as one table (converters per half, how they sample, inputs for 16 differential bridges,
     where temperature is read, spare channels) and two or three sentences each. Case D is presented in the head
     designer's own reasons (brief_round2.md has them translated), fairly and without comment in that paragraph.
     Note where the spec text stands today (§7 recommends three ADS131M08 per half = case C).
   - What a blind round of five models chose (from synthesis_round1.md and the answers): the agreement, the 3 / 2
     split on the part and the two datasheet questions it turns on, the ideas raised unasked. Say plainly: model
     answers, figures from memory, not checked against datasheets, not a decision.
   - (placeholder to fill when Kai sends round 2) What the challenge round said about each case.
   - What is open and who settles it: the TMR part linear at 110 mT (first prototype measurement); the two
     ADS131M08 datasheet facts; the choice of case — for the outside expert; required LMA accuracy; isolation and
     EMC for the 100 m cable. Nothing is selected.
   Every number on the page is generated from or checked against its source file by the build (as U54 did).
4. Prove: all four `--check`; pytest on the SWS test files (37 + yours); print ≤ 3 A4; qc-falsifier (separate
   subagent: every claim true to the sources, case D fair and complete, nothing selected, nothing presented as
   verified that is not); cold reader (fresh subagent, visible text only: "what are the four cases, which did the
   models prefer and why, what is still open?" answered correctly; reads as about the task).
Builder: Opus. `git worktree add C:/Users/stian/Prosjekter-u58 -b u58-hardware-page db05b45` from
C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u58/max; tests with the U41 venv, figures (if any)
with C:/Users/stian/Prosjekter-u05/max/.venv. Read first: rule 10; "## U52", "## U54", "## U56" above; build.py's
formats_nav; build_short.py for the link / hover helpers. Commit on the branch; no merge, no push, no export.
Hand back when everything except the round-2 section is built and proved; Kai then sends round 2 and you finish.
Report tasks/reports/U58.md, TASKS.md entry. Notes in C:/Users/stian/agent-notes/<nautical name>.md (list the
folder; Clew and Stanchion are taken). No identifier values. Timebox 75 minutes. — Kai

## U59 — export increment for U58, then the Pages snapshot (Kai, 10 Nov 22:3x)

Same job as "## U57" above; read it and stanchion.md first. State Kai confirmed: local main = merge of U58 (fourth
page docs/sws/hardware.html "Hardware selection", built by docs/sws/build_hardware.py; format switch on all four
pages; sources in sws/hw-selection/rounds/2026-11-10/; tests 61 over the five SWS test files incl.
tests/test_sws_hardware.py); four `--check` ok; pushed to D:. GitHub fjordbit/max main and the export clone are at
9d9a329; publish/SWS at 40f186a (verify).
A. Export from C:/Users/stian/export-v3/export: range db05b45..<local main tip>, max/ subtree, first-parent (one
   merge → one commit), graft on 9d9a329, fast-forward of one commit. Scan tip and increment: persons, drawings,
   customer 0, hover titles, alts and captions included — and the model answers under rounds/ (they are model
   output; scan every file). Four `--check`s and the five SWS test files (expect 61). No push.
B. Snapshot in C:/Users/stian/publish/SWS on top of 40f186a: `sws/` and `docs/sws/` from the export tip;
   hardware.html is new: its links must resolve in the snapshot (the rounds folder is carried under sws/; links to
   files not carried are unlinked as before), the switch must show four entries on all four pages and each entry
   must open; publish root docs/index.html: add "Hardware selection" beside the existing entry if that page lists
   the SWS pages (Cringle's note, 9 Nov). Visible text of hardware.html free of paths, "l.NNN" and snapshot
   notes; scan 0; `git status` only sws/ and docs/ ; rebuild index.zip (untracked). Commit "SWS snapshot from MAx
   <tip>: Hardware selection page"; no push.
C. Hand back ≤ 10 lines with the push commands. Notes in C:/Users/stian/agent-notes/<nautical name>.md (avoid every
   existing name; Clew, Stanchion, Grommet are taken). No identifier values. Timebox 1 hour. — Kai

## U60 — the link and the read-out: half ↔ root box, with pseudocode (Kai, 10 Nov 22:5x)

Owner, 10 Nov late evening, after reading both model rounds: "I agree with the bots it seems" — his leaning is the
simultaneous architecture (no multiplexer). That is a leaning, not a selection: the outside expert chooses, and
case D stays a presented case. He asks: "an analysis of the connection, the control box and the rest, with some SW
pseudocode of how to read this." (Control box = the root box of spec §10.)

Deliverable: one design note, `sws/hw-selection/sws_link_and_readout.md` (≤ 6 pages), written for the
simultaneous case (two ADS131M08 per half as the worked example; say in one short section what changes with three
chips, with the ADS131E08, and with the multiplexed case D). Register rows only for what is decided already; new
proposals are marked as proposals. No page change in this unit (hardware.html is under the owner's reading).

Contents:
1. The chain in one diagram (text / mermaid): 16 bridges → 2 converters → MCU → RS-422 → root box (up to four
   halves) → Ethernet; the sync pair; 24 V. What each node does and does not do (the half streams raw samples and
   health, no detection — spec §7, §10).
2. Converter read-out, checked against the datasheet: fetch the TI ADS131M08 datasheet (ti.com, SBAS950) and
   verify — cite section / table for each — the SPI frame (status word, channel words, CRC word, word length),
   DRDY behaviour, the SYNC/RESET pin and how two devices on one clock are aligned, data rates / OSR and the clock
   needed for 500 and 1000 samples/s, the filter's group delay, the reference (is there an external reference
   input, its range), input impedance per gain, the CRC options (communication and register map), packages,
   supply current. These are the facts the two model rounds quoted from memory and disagreed on; state each as
   VERIFIED (with the datasheet location) or NOT VERIFIED. Web access is for public datasheets only: nothing about
   this project goes into a query, a URL or a form.
3. The half's firmware as pseudocode (plain, language-neutral, commented): start-up (configure, read back, self
   test), the acquisition interrupt (DRDY → read both devices → check status and CRC → sample counter), temperature
   read scheduling (digital sensors on I²C, not during the sensitive instant if that matters), sync capture, frame
   assembly, transmit, health word (dead / railed / stuck channel, converter fault, sync lost, supply out of
   window), watchdog.
4. The link: frame layout byte by byte (proposal), bit-rate budget at 460.8 kbit/s and 1 Mbit/s for 16 and 24
   channels at 500 samples/s, framing / resynchronisation after a lost byte, CRC choice and its residual error
   rate, sequence counter, what the root box does on a CRC error or a gap. Compare with spec §10's frame content.
5. Synchronisation of the two halves: the scheme already in the record (sws_sync_findings.md: 1 Hz
   timestamp-and-latch, ≤ 1 ms) against the three schemes the models proposed (10 Hz edge timestamped; continuous
   clock from the root box; 500 Hz strobe); a table of what each needs from the root box and the cable, drift
   between edges, behaviour on loss; say which the record supports and what is open. Do not select.
6. The root box as pseudocode: four receivers, frame check, alignment of two halves to a common time base
   (interpolation), position tagging from the encoder count, buffering one 220 m pass, the first processing steps
   in order (ratiometric / temperature correction, neighbour difference, radial vs axial, axial sum for LMA) as
   function stubs with their inputs and outputs — no detection algorithm invented.
7. Open points and who settles them; what the first prototype must record so that the multiplexed pattern can be
   emulated from a simultaneous recording (the test the model rounds proposed: say what data rate / debug port
   that needs).
Sources: spec rev130 render §4, §6, §7, §8, §10 (sws/spec/rendered/); sws/hw-selection/sws_sync_findings.md and
sws_sync_budget.py; sws/hw-selection/rounds/2026-11-10/ (both rounds; model output, figures from memory — use them
as proposals, never as facts); docs/sws/hardware.html as built. Rule 10: every statement of fact carries its
source (file and line, or datasheet section); a proposal is marked as one; nothing is selected.
Builder: Opus. `git worktree add C:/Users/stian/Prosjekter-u60 -b u60-link-readout ff08f9f` from
C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u60/max. Prove: a qc-falsifier (separate subagent)
checks every VERIFIED item against the fetched datasheet text and every project fact against its cited line; a
second fresh subagent, given only the note, walks the pseudocode once as "the MCU" and once as "the root box" and
lists anything that cannot be executed as written (undefined variable, missing step, race). Report
tasks/reports/U60.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (avoid every existing name; Clew, Stanchion, Grommet taken, and the
U59 builder's). No identifier values, no personal names ("the head designer" only where needed). Timebox 90 min. — Kai

## U61 — "Software analysis and design" as its own page; the hardware page grows and is polished (Kai, 10 Nov 23:5x)

Owner, 10 Nov night, after a quick read of hardware.html ("seems good"): "lets add SW analysis and design as its
own. and then HW selection will grow with the cabling and the controller box etc." And: "do a few runs until we
have the paper brief down to something professional … check it and also publish to D, I will read it in the
morning." He reads both pages in the morning; nothing goes to GitHub or Pages.

Start from U60's branch (the note sws/hw-selection/sws_link_and_readout.md, commit 9b452f9; read jackstay's note and
tasks/reports/U60.md first): `git worktree add C:/Users/stian/Prosjekter-u61 -b u61-software-page 9b452f9` from
C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u61/max; tests with the U41 venv.

1. The note first. Jackstay rewrote §3, §4 and §6 after the pseudocode walk and could not re-walk them. Run a
   fresh walker (separate subagent, the note only: once as the MCU, once as the root box, then the time base end
   to end from sync edge to an aligned sample pair) and fix what it finds. The note stays the source of both pages.
2. Fifth page: `docs/sws/build_software.py` → `docs/sws/software.html`, menu entry "Software analysis and design"
   (formats list in build.py, after "Hardware selection"; all five pages show five entries). Content from the
   note, for a reader who will write or review the firmware: what the software in a half does and does not do;
   reading the converters (frame of ten 24-bit words, status, CRC, DRDY, the reset flag — with the datasheet
   section for each); the half's firmware as pseudocode (start-up, acquisition, temperature schedule, sync
   capture, frame assembly, health word, watchdog); the frame on the link, byte by byte, and what the root box
   does on a CRC error or a gap; the root box as pseudocode (receive, check, time base and alignment of the two
   halves, position tagging, buffering, the first processing steps as stubs); what is proposal and what is
   record; open points. Pseudocode in <pre> blocks, readable in print, not cut mid-block where avoidable.
   ≤ 6 A4. Every design element that is a proposal is marked once per section, not per line.
3. The hardware page grows (build_hardware.py), and stays ≤ 4 A4:
   - a section "Cabling and the root box": the cable per half (24 V, RS-422 data, the spare pair for sync; up to
     100 m; spec §10), the root box's ports and tasks (spec §10), the bit-rate budget from sws_link_budget.py
     (16 and 24 channels at 500 samples/s against 460.8 kbit/s and 1 Mbit/s — 24 channels do not fit the lower
     rate), the sync schemes side by side in one small table (the record's scheme and the three proposed), what
     is open (isolation, EMC standard, who terminates, edge rate and holdover). Nothing selected.
   - the datasheet facts now VERIFIED by U60 replace "the models disagree / from memory" wherever the page says
     so for the ADS131M08: external reference yes (REFIN 1.1–1.3 V), input impedance 330 kΩ at gain 1–4 and ≥ 1 MΩ
     at gain 8–128, leaded TQFP-32 and WQFN-32, CRC on the data output, 500 samples/s from 8.192 MHz at OSR 8192.
     Say what that does to the round-1 reasons for case B (two of three fall away; the loading question remains
     and depends on the bridge resistance) — as a consequence of the datasheet, not as a selection. The open list
     loses the two M08 datasheet items and keeps the multiplexed part's time per input (not fetched, not verified).
     Note for the record that the spec text (§7: "internal reference only") is contradicted by the datasheet;
     the spec is not edited here.
   - polish (the last cold reader's "heavy" list): the honesty statement about model output appears once, at the
     head of the model sections, not in every paragraph; the per-model tables move to the end of their sections or
     into a collapsed <details> that still prints; the requirements block reads as a list, without repeated
     qualifiers.
   - the head designer's case: unchanged in substance (the owner has not decided how it is attributed); role named
     at most twice.
4. A few runs until it reads professionally — at most three rounds, each with FRESH subagents:
   (a) professional reader: an experienced electronics / embedded consultant handed the two pages cold (visible
       text only) and asked: would you put your name under this as a briefing to a client's expert? what is
       unprofessional, vague, repeated, or missing? what would you cut? Fix what is right; say what you declined
       and why.
   (b) qc-falsifier: every claim against its source (datasheet text for VERIFIED items, spec lines, the note, the
       round answers); nothing selected; proposals marked; case D fair.
   Stop when a fresh professional reader says yes without substantive reservations and the falsifier passes, or
   after three rounds; report each round's verdict in one line.
5. Prove at the end: all five `--check`; pytest on all SWS test files (61 + yours: five-entry switch on five
   pages, software page sections in order, numbers on both pages generated from or checked against their source,
   U52 visible-text rules on the new page); print counts (hardware ≤ 4 A4, software ≤ 6 A4); identifier scan 0
   (identifiers.yaml `match:` is a mode, not a regex).
Report tasks/reports/U61.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes
in C:/Users/stian/agent-notes/<nautical name>.md (avoid every existing name; Clew, Stanchion, Grommet, Becket,
Jackstay taken). No identifier values, no personal names. Timebox 2 hours. — Kai

## U62 — an "In short" box at the head of the hardware and software pages (Kai, 11 Nov 13:1x)

Owner, 11 Nov: the hardware page should open with a synopsis that states the conclusions, so that not everyone has
to read the path to them; the same on the software page. He has given the go to publish after this unit (a
separate unit, U63, does the export).

`git worktree add C:/Users/stian/Prosjekter-u62 -b u62-in-short 4a50a29` from C:/Users/stian/Prosjekter-u05; work
in C:/Users/stian/Prosjekter-u62/max; tests with the venv at C:/Users/stian/Prosjekter-u05/max/.venv. Read
forestay's note and tasks/reports/U61.md first.

1. hardware.html (build_hardware.py): a box "In short" directly under the lead, before the first section, five or
   six lines, every number taken from the page's own sections (generated from the same source, not retyped):
   - what is needed: 16 bridge signals per half read at the same instant, temperature beside them;
   - what the blind round chose: five of five two simultaneous 8-channel 24-bit converters per half, no multiplexer
     (three the ADS131E08, two the ADS131M08);
   - how the four cases ranked in the challenge round, one line, and what the datasheet says about the multiplexed
     case (rate per bridge on three and on four chips, offset between neighbouring channels);
   - what gates everything: a TMR sensor linear at 110 mT;
   - what is not decided: nothing is selected; the choice of case is the expert's.
   Wording rule: "the models preferred / ranked", never "we selected / the choice is". The box is what will be
   quoted.
2. software.html (build_software.py): the same box, same style: what the software in a half does and does not do;
   the frame and the rate it needs on the link (24 channels at 500 samples/s need 1 Mbit/s); how the two halves
   are put on one time base; what is proposal and not record; what is open.
3. The multiplexed case is no longer attributed to a person or a role: the two places that say "the head
   designer" become "the in-house choice" (keep "made after a review of the converters, before the blind round and
   without knowledge of it"). Check tests and the rounds README for the same phrase in page-visible text.
4. Page budgets hold: hardware ≤ 4 A4, software ≤ 6 A4 — tighten elsewhere if the box pushes a page over; say what
   you cut.
5. One fresh cold reader (separate subagent, visible text of the two boxes only): does each box stand alone, does
   it claim a selection anywhere, does any number differ from the page body? Fix.
6. Prove: all five `--check`; the six SWS test files (80 + yours: the box exists on both pages, sits before the
   first h2, contains no "selected"/"we chose", its numbers equal the body's); print counts; identifier scan 0 with
   `.venv/Scripts/python.exe -I C:/Users/stian/max-private/tools/scan_tree.py` on the added lines and
   `python -I C:/Users/stian/secretary/tools/idscan.py <repo> 4a50a29..HEAD`.
Report tasks/reports/U62.md (≤ ⅓ page, "the owner", no names), TASKS.md entry. Commit on the branch; no merge, no
push, no export. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not already in that folder). No
identifier values, no personal names. Timebox 45 min. — Kai

## U63 — export increment for U60–U62, then the Pages snapshot, with every link proven (Kai, 11 Nov 13:5x)

Same job as "## U57" and "## U59" above; read them and the notes of the builders who did them (stanchion.md, and
the U59 builder's note) first. The owner has given the go to publish the hardware and software pages; his
condition: **every link on the published pages must work**, so every page and file a link points to is published
with them. Kai pushes after a final check; you do not push.
State: local main = f73fb3e (U60 note + scripts, U61 software page + grown hardware page, U62 "In short" boxes);
D: = f73fb3e. GitHub fjordbit/max main = 9d9a329. Export clone C:/Users/stian/export-v3/export holds one unpushed
commit da77fe4 on 9d9a329 (U59: the first hardware page). publish/SWS holds one unpushed commit c81b11f on 40f186a.
Build on top of both (do not rewrite them); verify these hashes before you start and stop if they differ.
A. Export: the max/ subtree increment from the local commit U59 exported up to f73fb3e, first-parent, grafted on
   da77fe4, fast-forward only. Scan tip and increment (scan_tree with the venv at Prosjekter-u05/max/.venv, and
   `python -I C:/Users/stian/secretary/tools/idscan.py`): persons, drawings, customer 0 on everything added,
   including hover titles, alts, captions, the round answers and the new note. Five `--check`s and the six SWS
   test files touched by U56–U62 (expect 84) with the venv at C:/Users/stian/Prosjekter-u41/max/.venv (it has
   `markdown`; the u05 venv has `yaml` — a test that fails only on a missing module is environment, say which).
B. Snapshot in C:/Users/stian/publish/SWS on top of c81b11f: `sws/` and `docs/sws/` from the export tip. Five
   pages, five-entry switch on each, each entry opens. software.html is new; add it to the publish root
   docs/index.html beside "Hardware selection" if that page lists the SWS pages.
C. Link proof, the point of this unit — write a small script (kept in the scratchpad or your notes folder, not in
   the repo) and print its counts in your hand-back: for all five pages in the snapshot, every `href`/`src`:
   (1) relative → the file exists in the snapshot (and the #anchor exists in the target when it is html);
   (2) absolute to the project's own GitHub repo or Pages site → map the URL to its path in the tree that will
       be at that URL after the push (the snapshot for the Pages/documentation repo, the export tip for the code
       repo; mind branch and blob/tree prefix) and require the file to exist there; a link whose target is not
       carried is either carried now (preferred, if it passes the scan and the masking rules) or unlinked as
       before — list each one you unlinked and why;
   (3) other external (datasheets, standards bodies) → list them; do not fetch more than a HEAD per distinct URL,
       and send nothing about the project.
   Result wanted: (1) and (2) with 0 broken on all five pages. The new pages matter most; report old pages'
   breakage separately if you find any, and fix it by the same rule.
D. Visible text of the two new pages free of local paths, "l.NNN" and snapshot notes; scan 0 on the increment;
   `git status` only sws/ and docs/; rebuild index.zip (untracked). Commit "SWS snapshot from MAx <tip>: software
   page, In short boxes". No push.
E. Hand back ≤ 12 lines: both tips, the link counts per page (relative / own-repo / external; broken 0), what you
   unlinked, scans, tests, the exact push commands for the three remotes. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
   names. Timebox 1 hour. — Kai

## U64 — price against complexity for the four cases (Kai, 11 Nov 14:4x)

Owner, 11 Nov: a price comparison of the converters, and of each case completed to an assembled board; "we had
this price vs complexity graph once, perhaps we do something similar … the more parts, the more complexity, the
cheaper price, but it needs to be told that cheaper price comes at higher complexity. At least where we are before
the challenge to the expert." Housing and potting are NOT this unit (U65, own page).

`git worktree add C:/Users/stian/Prosjekter-u64 -b u64-price-complexity f73fb3e` from C:/Users/stian/Prosjekter-u05;
work in C:/Users/stian/Prosjekter-u64/max; page builds and tests with the venv at
C:/Users/stian/Prosjekter-u41/max/.venv. Read tiller.md, forestay.md and tasks/reports/U61.md, U62.md first. Look
once (15 min at most) for the earlier price-versus-complexity graph in the repo and worktrees (figures, docs,
reports; words like "complexity", "price", "cost"); if found, follow its form; if not, say so.

1. Prices, looked up, not remembered. For each converter in the four cases (ADS131M08, ADS131E08, ADS124S08,
   ADS114S08, in the packages the page names) and for the parts a case drags with it (reference, clock/oscillator,
   input filter parts, digital temperature sensor, RS-422 transceiver, MCU class, regulator): the manufacturer's
   listed 1 ku price and one or two distributors' prices at ~10 pieces (prototype) and ~1000 pieces (400 halves ×
   2–4 chips). Web queries carry part numbers only — nothing about the project, the company, the rope or the
   application. Record for every figure: source URL, date read, quantity break, currency. A price you could not
   read from a page is "not found", never an estimate presented as a price. Stock/lifecycle status (active, NRND)
   where the same page shows it.
2. Per case, per half: (a) converters alone; (b) the acquisition chain's bill of materials as the page describes
   the case — list every line, count and unit price, and mark each line "looked up" or "assumed" (passives and
   PCB are assumed, with the assumption stated); (c) an assembled-board estimate as a RANGE with its assumptions
   (board area and layers, leaded against leadless assembly, test), marked as an estimate for the expert or a
   board house to replace. Both quantities. Generated by a script `sws/hw-selection/sws_price_complexity.py` from
   a data file with the sources — no number typed into the page.
3. Complexity, defined before it is plotted, as countable things, per case: parts in the signal chain; converter
   chips; analog switching stages; things the firmware must do that the other cases do not (slot scheduling,
   settling waits, interpolation to a common instant, per-channel timestamps); timing requirements that carry the
   result (offset between neighbours, alignment at the split); calibration steps; open datasheet questions. Show
   the table; then one index if and only if you state its weights and show that the ordering does not flip under
   two other reasonable weightings (if it flips, plot the counts, not an index).
4. The figure: price per half (x or y, your choice by legibility) against complexity, four points with ranges,
   both quantities distinguishable; caption says in plain words what the owner asked: where a case is cheaper, what
   complexity pays for it, and that this is the state before the expert's challenge. If the data do NOT show
   "cheaper = more complex" (e.g. the converters are a small share of the board and the cases end within each
   other's ranges), say exactly that — do not draw the expected story. Load the house style from the existing
   figures (sws/figures/decided/make_working_area.py).
5. On the hardware page: a section "Price and complexity" after the challenge round, ≤ ½ A4 with the figure and
   the summary table; one line in the "In short" box. The page may go to 5 A4. Nothing selected; wording rule as
   U62. Full tables in a note `sws/hw-selection/sws_price_complexity.md`, linked.
6. One fresh falsifier (separate subagent): every price against its recorded source line, every count against the
   page's case description, the arithmetic, the caption against the data. One fresh cold reader on the section.
7. Prove: five `--check`; the six SWS test files (84 + yours); print counts; identifier scans 0 (scan_tree with
   the u05 venv on added lines; `python -I C:/Users/stian/secretary/tools/idscan.py <repo> f73fb3e..HEAD`).
Report tasks/reports/U64.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes
in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
names ("the owner"). Timebox 2 hours; past it, stop and report. — Kai

## U65 — a sixth page: "Housing and sealing" (the enclosure of a half, potting epoxy for water-tightness) (Kai, 11 Nov 15:2x)

Owner, 11 Nov: "The housing, idea use some specific epoxy to keep it water tight, also should be considered" — its
own page, run after the price comparison. Same purpose as the hardware page: where we are before an outside
expert is asked; a few cases for that expert to choose from; nothing selected.

`git worktree add C:/Users/stian/Prosjekter-u65 -b u65-housing-page ca4df4c` from C:/Users/stian/Prosjekter-u05;
work in C:/Users/stian/Prosjekter-u65/max; page builds and tests with the venv at
C:/Users/stian/Prosjekter-u41/max/.venv. Read outhaul.md, tiller.md, forestay.md first, then the record: the
design input specification render (sws/spec/rendered/…rev130.md — every section that touches enclosure, sealing,
IP class, temperature range, materials near the poles, sensor stand-off, cable entry, wear, service), the data
sources register (sws/data/sws_data_sources.md) and the decided geometry (one-piece half-ring magnets, no shoe,
no segments; N52 and N48SH both carried; max +45 °C in service). What the record says is the frame; where it says
nothing, say "the record does not say".

1. What the housing of one half must do — from the record, each line with its section: keep water out (the IP
   class and what it means in immersion depth and time), the temperature range, carry the sensor boards at their
   stand-off from the rope and the poles, let the heat of the electronics out, bring the cable in, survive the
   rope (wear face, contact, grease, salt water, shipyard environment as the record states it), stay non-magnetic
   where it must, open or not open for service, ten years.
2. The cases, three to five, each described the same way (what it is, what seals it, what it does to the sensors
   and magnets, service, what is unknown): e.g. (a) fully potted in epoxy; (b) potted in a softer compound
   (polyurethane or silicone gel) inside a shell; (c) sealed machined or moulded housing with gasket or O-ring and
   conformal-coated boards, no potting; (d) two-stage: soft coat on the sensor boards, hard epoxy outside;
   (e) overmoulding. Choose the set that is real practice for magnetic sensor heads and submerged electronics —
   look it up (general queries only: material classes, standards, properties; nothing about the project, the
   company, the product or the rope).
3. What matters for THIS head, each as a short paragraph with a source or marked "not sourced": cure shrinkage
   and thermal-expansion mismatch stressing magnetoresistive sensors (offset and sensitivity shift — the round-1
   model answers raise potting stress; cite them as model output); cure exotherm and cure temperature against the
   magnets' maximum temperature and the grade (N52 against N48SH); water uptake of epoxies against polyurethanes
   and silicones, and what moisture does at a bridge output; glass transition against −40…+50 °C; adhesion to
   the cable jacket and the gland as the usual leak path; NdFeB corrosion if water reaches it and what coating
   the record assumes; repair (potted = replaced, not repaired) against 200 heads and 10 years; thermal path for
   the half's power budget; the wear face between sensors and rope and what it does to the stand-off.
   Property figures only from a data sheet or standard you actually read (URL, date); product names only as
   examples of a class, with "not selected".
4. Tests the prototype should run, in order (immersion per the IP class, temperature cycling with the bridges
   logged, sensor offset before and after cure, magnet flux before and after cure) — as a list, marked proposal.
5. What is open, and who settles it. Include: the record's own gaps you found; the interaction with the hardware
   cases (leaded against leadless packages under potting stress; whether the temperature sensor beside each
   bridge survives the same cure).
6. Page: `docs/sws/build_housing.py` → `docs/sws/housing.html`, menu entry "Housing and sealing" after "Software
   analysis and design" (six entries on all six pages; update the tests that count five). Opens with an "In short"
   box as U62. ≤ 4 A4. One comparison table of the cases; a figure only if it earns its place (e.g. a section
   sketch of a half showing what is sealed where — schematic, marked "not to scale, not the design"). Nothing
   selected; "the record says / practice is / the models said", never "we chose". No person, no role.
7. Reviews, fresh subagents: (a) a materials / encapsulation engineer handed the page cold: would you sign this
   as a briefing to a client's expert; what is wrong, vague or missing; (b) a falsifier: every claim against its
   source, every record citation against the spec line. One round of fixes; say what you declined and why.
8. Prove: six `--check`; all SWS page test files (89 + yours); print counts; identifier scans 0 (scan_tree with
   the u05 venv on added lines; `python -I C:/Users/stian/secretary/tools/idscan.py <repo> ca4df4c..HEAD`).
Report tasks/reports/U65.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes
in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
names ("the owner"). Timebox 2 hours; past it, stop and report. — Kai

## U66 — ruling: the head is never submerged; water cast at it in a storm (Kai, 11 Nov)

Owner, 11 Nov, on reading the housing page's gap "whether the head is ever submerged: the record does not say":
the head is never submerged — that is the design intent; a storm may cast water at it; full submersion is not
considered.

`git worktree add C:/Users/stian/Prosjekter-u66 -b u66-not-submerged b28bdcc` from C:/Users/stian/Prosjekter-u05;
work in C:/Users/stian/Prosjekter-u66/max; venv C:/Users/stian/Prosjekter-u41/max/.venv. Read bilge.md first.
1. Record it: sws/data/sws_data_sources.md, a section "Rulings of 2026-11-11" in the form of the 10 Nov section:
   never submerged; exposure is water cast at the head (storm, spray); full submersion is not a design case.
2. housing.html (build_housing.py) and its note: the gap becomes the ruling, wherever it appears (requirements,
   "In short", open list, the cases' comparison where immersion was weighed). State the consequence without
   selecting: the record's IP67 is a temporary-immersion class; the exposure now stated is water projected at the
   enclosure, which IEC 60529 tests under separate second numerals (jets), and a rating for immersion does not by
   itself cover jets unless both are marked — ONLY as far as a source you actually read says so (public summary
   is acceptable, marked as such; the standard text has not been read). Whether the record's class should be
   restated (e.g. a jet class, or a dual marking) is for the owner and the expert — an open point, and a line for
   the specification's master, which is not edited here. The record's "IP68 only if it can stand in water in the
   pit" is answered by the ruling: say so. Prototype tests: the immersion test stays as what the record's class
   requires; add the water-jet test as the one matching the stated exposure, marked proposal.
3. Salt: if the record states sea water or a marine site, the cast water is salt water — say what the record says;
   otherwise "the record does not say".
4. One fresh falsifier on the changed sentences. Prove: six `--check`, SWS tests (107 + yours, skip test_sws_p52
   which needs yaml), page ≤ 4 A4, both identifier scans 0 on b28bdcc..HEAD.
Report tasks/reports/U66.md (a few lines), TASKS.md entry. Commit on the branch; no merge, no push. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). General web queries only, nothing about
the project. No identifier values, no personal names ("the owner"). Timebox 40 min. — Kai

## U67 — the price and complexity figure as one plot that reads at a glance (Kai, 11 Nov)

Owner, 11 Nov: "make one more plot that is easier to read". The four-panel figure from U64
(sws/figures/decided/price_complexity.png) is honest but hard to read: four panels, labels on top of each other.

`git worktree add C:/Users/stian/Prosjekter-u67 -b u67-price-plot b28bdcc` from C:/Users/stian/Prosjekter-u05; work
in C:/Users/stian/Prosjekter-u67/max; venv C:/Users/stian/Prosjekter-u41/max/.venv. Read outhaul.md first. U66 is
running in parallel on the housing page and the data sources register — do not touch those files.
1. One figure, same data file and script (sws_price_complexity.py), no new numbers. Form Kai has in mind — use it
   unless you can show a clearer one: four rows, one per case (A, B, C, D, each with its three-or-four-word
   description, D as "in-house, multiplexed"); on a common USD-per-half axis at ~1000 pieces a horizontal range
   bar for the assembled board (estimate) and a distinct marker for the converters alone (looked up); to the right
   of the axis, aligned with each row, the complexity counts as a small table of numbers (converter chips,
   switching stages, firmware tasks only this case has, timing requirements) — numbers, not a second axis. The
   ~10-piece figures go in the table on the page, not in the plot. Looked-up and estimated must be distinguishable
   without the legend (label them directly). No overlapping text at the page's print width; check the rendered
   png yourself by eye.
2. Caption in plain words, two sentences: what a reader sees (which case is cheapest in parts, which carries the
   most counts, that the assembled ranges overlap because the board figures are estimates), and that this is the
   state before the expert's challenge. No "cheaper comes with more complexity" unless the numbers show it.
3. The new figure replaces the four-panel one on the hardware page; the old one stays in the note
   (sws_price_complexity.md) as the detailed view. Page stays ≤ 5 A4.
4. One fresh cold reader shown ONLY the png and caption: "what does this figure tell you?" — its answer must match
   the data; fix until it does. Prove: `--check` for all builders, SWS tests (skip test_sws_p52, needs yaml), both
   identifier scans 0 on b28bdcc..HEAD.
Report tasks/reports/U67.md (a few lines), TASKS.md entry. Commit on the branch; no merge, no push. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
names. Timebox 40 min. — Kai

## U68 — the sealant round on the housing page: what five models drew, checked against the data sheets (Kai, 11 Nov)

Owner, 11 Nov: "should sealant have its own run?" → yes, started. He had been told of "some special epoxy that did
not get affected by temperature in such a way" (no name). Kai ran a blind round of the same five models as the
electronics round: brief and answers in C:/Users/stian/sealant_round_2026-11-11/ (brief.md, models.yaml,
answers/2026-11-11/*.md, round.json). Kai's first read, to be checked by you, not trusted: four of five drew a
gasket-sealed non-magnetic shell filled with a soft addition-cure silicone gel (three WACKER SilGel 612 first, one
DOWSIL 3-4207 first; shells: 316L, aluminium, PEEK twice); one drew a dry sealed polymer half with parylene-coated
boards and no fill; none chose a hard epoxy; all five read the "special epoxy" as a high-Tg filled low-expansion
epoxy (Stycast 2850FT named by three) or a low-Tg flexible epoxy, and all five said it is not the right material
against the sensors.

`git worktree add C:/Users/stian/Prosjekter-u68 -b u68-sealant-round 4241003` from C:/Users/stian/Prosjekter-u05;
work in C:/Users/stian/Prosjekter-u68/max; page builds/tests venv C:/Users/stian/Prosjekter-u41/max/.venv (figures:
the u05 venv). Read bulkhead.md and bilge.md first.
1. Carry the round into the repo as the electronics round was carried (see sws/hw-selection/rounds/2026-11-10/ and
   its README): `sws/housing/rounds/2026-11-11/` with the brief, the five answers, a README (what was asked, who
   answered, that it is model output), and a synthesis written by you from the answers themselves — per model:
   concept, shell material, what touches the sensors, the magnets, the cable; product first and alternative; cure;
   what it says of the "special epoxy"; its first prototype test; what it asked. Count agreements exactly; quote
   where models differ. Note in the README that the brief's "coastal site, salt water" is the brief's wording; the
   record says marine atmosphere and salt spray.
2. Data sheets, read not remembered, for every product a model named as first choice or alternative, and for the
   epoxy the models took the "special epoxy" to be (general queries: product names and property names only;
   nothing about the project, company, people, product or application). For each figure the models gave: VERIFIED
   (sheet says the same), CORRECTED (sheet says otherwise — give both), NOT ON THE SHEET. At least: cure schedule
   and whether full cure is reached at room temperature; service temperature range; hardness/penetration; thermal
   expansion; water absorption; thermal conductivity; what inhibits cure; adhesion/primer. For the filled epoxy:
   glass transition as a function of cure schedule, expansion, and what cure gives the quoted Tg. Record URL and
   date per figure. A product you cannot find a sheet for is "not found" — and say if a named product seems not to
   exist or to be discontinued.
3. housing.html (build_housing.py): a section "What a blind round of five models drew" after the cases, in the
   form of the hardware page's round section (honesty statement once; per-model table collapsed, prints): the
   count, the reasons in the models' words, the data-sheet verdicts, and a short paragraph "The epoxy that is not
   affected by temperature" — what the models took it to be, what the sheet of that class says, and that the
   owner's source has not been identified, so the page cannot say which product was meant. Map the models'
   concepts onto the page's four cases (which case each answer is). One line in "In short". Nothing selected:
   "the models drew / preferred"; the choice is the outside expert's. Things the models raised that the page lacks
   (gel expansion room in a closed shell, a thinned sensor wall or film window against the 0.3 mm left, magnet
   coating, vapour passing silicone, repair by cutting out gel) go in as model output, each marked sourced or not.
   Page ≤ 4 A4.
4. Fresh subagents, one round: a falsifier (every count and quote against the answers, every figure against its
   sheet line) and a cold materials engineer on the new section. Re-run the falsifier once after fixes — the last
   three units did not, and the owner has been told so each time.
5. Prove: `--check` for all builders; SWS tests (109 + yours; skip test_sws_p52); print counts; identifier scans
   on 4241003..HEAD: idscan 0; scan_tree on added lines — if it reports hits on a re-rendered long line of
   report.html, show that the removed side has the same count (old content) rather than calling it 0.
Report tasks/reports/U68.md (≤ ½ page), TASKS.md entry (append at the end). Commit on the branch; no merge, no
push, no export. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier
values, no personal names ("the owner"). Timebox 2 hours; past it, stop and report. — Kai

## U69 — export increment for U64–U68, then the Pages snapshot, every link proven on six pages (Kai, 11 Nov)

Same job as "## U63" above; read it and scuttle.md first (the method, the link script at
C:/Users/stian/export-v3/tools/links12.py). The owner has given the go to publish; Kai pushes after a final check;
you do not push.
State: local main = 8f97214 (U64 price and complexity, U65 housing page, U66 rulings of 11 Nov, U67 one-plot
figure, U68 sealant round); D: same. GitHub fjordbit/max main = export clone tip = 1e215a2 (it exported local
f73fb3e). publish/SWS = both Pages remotes = 832e98f. Verify before you start; stop if they differ.
A. Export: max/ subtree increment f73fb3e..8f97214, first-parent, grafted on 1e215a2, fast-forward only. Scan tip
   and increment (scan_tree with the u05 venv; idscan): 0 on everything added, including the new rounds folder
   sws/housing/rounds/2026-11-11/, the price data file with its source URLs, hover titles, alts, captions. Where
   scan_tree reports hits on a re-rendered long line of report.html, show the removed side carries the same
   count. `--check` for all builders and the SWS test files (expect 113; skip test_sws_p52) with the u41 venv.
B. Snapshot in C:/Users/stian/publish/SWS on 832e98f: `sws/` and `docs/sws/` from the export tip. Six pages,
   six-entry switch on each, each entry opens; housing.html is new.
C. Link proof on all six pages as in U63: relative and own-repo links 0 broken against the trees that will be
   live; carry or unlink what is not carried and list it. External links: the new pages now have some (data
   sheets, distributor pages) — one HEAD per distinct URL, and THIS time save status per URL to your notes;
   report any 404 by page and link text. Also find the one external link on report.html that returned 404 in
   U63 and report it (do not fix content; list it).
D. Visible text of the three newer pages free of local paths, "l.NNN" and snapshot notes; scan 0 on the
   increment; `git status` only sws/ and docs/; rebuild index.zip (untracked). Commit "SWS snapshot from MAx
   <tip>: housing page, price and complexity". No push.
E. Hand back ≤ 12 lines: both tips, link counts per page (broken 0), what you unlinked, external statuses that
   are not 200/redirect, scans, tests, the three push commands. Notes in C:/Users/stian/agent-notes/<nautical
   name>.md (a name not in that folder). No identifier values, no personal names. Timebox 1 hour. — Kai

## U70 — a seventh page: "Procedures and life cycle" (FMECA, prototype test, FAT, HAT, SAT, installation, recalibration) — placeholders, and the plan for next week's 40 mm prototype test (Kai, 12 Nov)

Owner, 12 Nov: one more page for the procedures — FMECA, FAT, HAT, SAT, installation, recalibration. "Create the
placeholders at least"; the runs that fill them come afterwards, in order; "we want the entire lifecycle of the
sensors handled". Recalibration: something was written originally; it is hard to finish before the sensors are
set, and a sensor run is needed first — note that on the page. Next week there is a test with the 40 mm rope and
the first prototype: what data we want from it goes in the plan. This unit is the frame and that one list; it does
NOT write the procedures.

`git worktree add C:/Users/stian/Prosjekter-u70 -b u70-procedures-page 8f97214` from C:/Users/stian/Prosjekter-u05;
work in C:/Users/stian/Prosjekter-u70/max; page builds and tests with C:/Users/stian/Prosjekter-u41/max/.venv;
scan_tree with the u05 venv. Read bilge.md, gangway.md and U65/U68 above for the page pattern, then the record:
sws/spec/rendered/…rev130.md §8 (calibration pass and noise template — this is the "written originally" text),
§11 (test program: prototype characterisation, FAT, HAT), §12 (open items; the rows on the prototype, calibration
storage, reference rope), §2 (what FAT takes from EN 12927 / ASTM E1571); the register (sws/data/
sws_data_sources.md, incl. the 11 Nov rulings); sws/VERIFICATION_PLAN.md; the hardware, software and housing pages
(their "open" lists and the housing page's proposed prototype tests); whatever the record holds on the 40 mm
prototype head (P40 / first prototype: search sws/, tasks/reports/). Where the record says nothing: "the record
does not say".

1. The life cycle as one ordered list, each stage a section with the same four short parts — what the record
   already says (with section), what is missing, which run fills it, what it waits for: design FMECA →
   prototype characterisation → type / reference-rope work → FAT (factory, per unit) → transport and storage
   → installation → HAT / SAT → commissioning baseline (the frozen template) → operation (calibration pass,
   health, drift) → periodic check and recalibration → repair or replacement of a half → end of life. Adjust the
   list to what the record supports; say what you changed.
2. Terms: the record defines FAT and HAT (how, where); SAT is not in the spec as far as I found — say so and show
   the two readings (HAT = SAT on the installed hoist, or SAT a separate site test after HAT) as an open ruling.
   FMECA: none exists in the record — placeholder with the scope it would need (which items, which failure
   classes the record already names: sensor drift, link loss, a dead channel and the N+1 statement, magnet loss,
   water ingress, mis-registration along the rope) — a list of what is to be analysed, not the analysis.
3. Recalibration placeholder: quote what §8 and §12 say today; list what it depends on that is not set (sensor
   part, drift table, per-unit calibration storage, the reference standard used in the field, interval); state
   that a sensor run comes first. Do not invent an interval or a method.
4. **Next week's test, 40 mm rope, first prototype — the data we want.** A table: quantity, why (which open
   question or which later procedure it feeds, with section), how it is taken, what "good enough" looks like
   if the record gives a figure. Draw from §11 prototype characterisation, §12, the pages' open lists (e.g. DC
   background at the sensor plane and the linear range; noise floor; defect amplitude against depth and angle;
   stand-off; speed; repeatability pass to pass and registration; temperature logged; the split; multiplexer
   behaviour if the prototype has one). Order it: what must be taken first because the rest depends on it. End
   the section with what the record does not tell us about the prototype and the test (which sensors and
   electronics it carries, which defects the rope has, rig and speed, who records) — as questions, ≤ 8.
5. The order of the runs after this unit, as a short numbered list (proposal, marked so), sensor run first where
   the others depend on it.
6. Page: `docs/sws/build_procedures.py` → `docs/sws/procedures.html`, menu entry "Procedures and life cycle"
   last (seven entries on all seven pages; update the tests that count six). "In short" box as U62. ≤ 4 A4.
   Placeholders must read as placeholders: one plain line "Not written yet", not filler. Nothing selected, no
   invented figures; "the record says / not in the record". No person, no role, no dates in prose.
7. Reviews, fresh subagents: (a) a cold reader — a test engineer who will run next week's test: is the data list
   usable, what is missing or unclear; (b) a falsifier: every record citation against the spec line. One round
   of fixes; say what you declined and why.
8. Prove: seven `--check`; all SWS page test files; print counts; identifier scans 0 (scan_tree on added lines;
   `python -I C:/Users/stian/secretary/tools/idscan.py <repo> 8f97214..HEAD`).
Report tasks/reports/U70.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes
in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
names ("the owner"). Sign every message with your name. Timebox 90 minutes; past it, stop and report. — Kai

## U71 — the sensor run: candidate sensor parts against their data sheets, and what the sensor fixes for the life cycle (Kai, 12 Nov)

Owner, 12 Nov: "we need a sensor run" — the sensors are not set, and recalibration (and most of the life-cycle
page) cannot be written before they are. Start it now. Next week (Wed 18 – Fri 20 Nov) the OLD 40 mm prototype —
the one with three multiplexer stages — is tested on a 40 mm rope. Its sensor part number and data sheet are NOT
in the record (asked of the head designer today; do not guess the part). Same purpose as the hardware and housing
pages: where we are before an outside expert is asked; candidates, nothing selected.

`git worktree add C:/Users/stian/Prosjekter-u71 -b u71-sensor-run 5defd84` from C:/Users/stian/Prosjekter-u05; work
in C:/Users/stian/Prosjekter-u71/max; venvs as U70. Read mooring.md, gangway.md, U65/U68/U70 above, then the
record: spec render rev130 §5 result 4 (field at the sensor plane), §6 (sensing architecture, radial and axial
channels, stand-off, redundancy statement), §7 "TMR part selection" table and candidate families, §8, §12; the
register rows on the sensor-plane background and the 0.10 mT limit; the hardware page (its "open" list) and
sws/hw-selection/rounds/2026-11-10/ (what the models said about the TMR part — model output, from memory, none
confident); sws/3d bz_radius work (background against sensor radius; the head designer's question whether a
Hall part with an offset range would suit); the procedures page (docs/sws/build_procedures.py: recalibration and
prototype sections).

1. What the sensor must do, from the record, each line with its section: field to stay linear in (background +
   signal, with the record's figures and their status), smallest signal to resolve, noise allowed, bandwidth at
   15 m/min, temperature range −40…+50 °C, supply, package and footprint on the spoke board, radial and axial
   sensing direction, life. Where the record gives a range or two figures, show both.
2. Candidates, by class and by part, each row from a data sheet you actually opened (URL, date read; no figure
   from memory or from a model answer): linear TMR bridges with wide range; AMR bridges; linear Hall (incl. the
   offset-range idea); anything else that is real practice in rope testers (look it up — general queries only:
   part families, data sheets, MRT practice; nothing about the project, the company or the rope). Per part: linear
   range, sensitivity, noise (as the sheet states it, with bandwidth), offset and its temperature drift,
   sensitivity temperature coefficient, hysteresis, cross-axis sensitivity / what a strong field on the other
   axis does, supply and bridge resistance, package, temperature grade, availability as the distributor shows it.
   "Not on the sheet" where it is not. Check each against 1: passes / fails / cannot be told from the sheet.
3. What the sensor fixes downstream — short, as a table: for each life-cycle stage on the procedures page, which
   sensor property decides it (e.g. drift and hysteresis → the calibration pass and the recalibration interval;
   offset spread → per-unit calibration storage; linear range → the first prototype measurement; noise → the FAT
   criterion). No intervals or methods invented.
4. What next week's test should take BECAUSE the sensor is not set — cross-check against the 16-row data list on
   the procedures page; add or sharpen rows only where the sensor question needs it (e.g. background field per
   channel at the as-built radius, measured with what; clipping check; offset before and after closing the head).
   The prototype's own sensor is unknown: write those rows so they hold for any part.
5. Output: a note sws/hw-selection/sws_sensor_candidates.md (the full table + sources); a section "The sensor"
   on the hardware page (≤ 1 A4 added: requirement, comparison table, what cannot be told from data sheets);
   the recalibration and prototype sections of the procedures page updated to point at it (still "Not written
   yet" where it is). Nothing selected; no person, no role, no dates in prose.
6. Reviews, fresh subagents: (a) a sensor / analog engineer handed the note cold; (b) a falsifier: every figure
   against its data sheet, every record citation against the spec line. Fix; re-run the falsifier once if it
   failed; say what you declined.
7. Prove: seven `--check`; all SWS page test files except p52; counts printed; identifier scans 0 (scan_tree on
   added lines; `python -I C:/Users/stian/secretary/tools/idscan.py <repo> 5defd84..HEAD`).
Report tasks/reports/U71.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes
in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
names. Sign every message with your name. Timebox 2 hours; past it, stop and report. — Kai

## U72 — literature sweep: which sensors other rope testers use; and a third falsifier pass on the sensor note (Kai, 12 Nov)

Owner, 12 Nov: "Which sensors are used by others — do a literature sweep also." And from the owner on the old
40 mm prototype: the head designer's design had four sensing elements in a Wheatstone bridge, and that bridge is
INSIDE the selected part (an integrated full-bridge sensor), not four separate parts. Part number still not on
file. A blind model round on the sensor is running separately (C:/Users/stian/sensor_round_2026-11-12/); it is
not yours and you do not read it — a later unit folds it in.

`git worktree add C:/Users/stian/Prosjekter-u72 -b u72-sensor-literature d98e70d` from C:/Users/stian/Prosjekter-u05;
work in C:/Users/stian/Prosjekter-u72/max; venvs as U71. Read leeboard.md, U71 above, and
sws/hw-selection/sws_sensor_candidates.md whole.

1. **The sweep.** What magnetic rope testers and closely related flux-leakage instruments use as the sensing
   element — for the leakage-flux (broken wire) channel and for the section-loss (LMA) channel separately:
   (a) commercial instruments, from makers' own published material (data sheets, manuals, patents, application
   notes): technology (induction coil, Hall, GMR, TMR, AMR, fluxgate), number and arrangement of sensors, where
   stated the part or part family; (b) the research literature, about the last fifteen years plus the standard
   older references: papers and theses that state the sensor part and the field it works in — part, technology,
   background field or how the background is avoided (sensor position, bias, differential pairs, shielding,
   concentrators), stand-off, reported noise or smallest detected defect; (c) the standards (EN 12927, ASTM E1571,
   ISO 4309 — the EN is on file at C:/Users/stian/max-private/standards/, never copied into the repo; quote
   clause numbers only): do they assume or require a sensor type. General queries only — nothing about the
   project, the company, the product, the rope maker or any person in a query or URL.
   Every row from a source you actually opened (URL or DOI, date read); abstract-only reads marked so; nothing
   from memory. Aim for 15–30 solid rows, not a bibliography. Say what you searched and what you could not open.
2. **What it says for us**, one page at most: how often each technology appears and for which channel; how
   others handle a background of tens of mT (do they put the sensor where it is small? use Hall for that
   reason? use full bridges?); which parts recur, and whether any of them is in the U71 table or should be added
   (read its data sheet and add the row under U71's rules); whether anyone reports hysteresis, drift or
   recalibration experience in service. Integrated full bridge against other arrangements: what the literature
   uses. Mark inference as inference.
3. **Record the owner's statement** about the old prototype (integrated full bridge, four elements in one part;
   three multiplexer stages; part number not on file) in the register under today's rulings, in the same form
   as the 11 Nov rulings, and where the note and pages say the prototype's sensor is unknown, say what is now
   known and what is not.
4. **Third falsifier pass on the U71 note and the hardware page's "The sensor" section** — a fresh subagent:
   every figure against its data sheet (re-open the sheets), every record citation against the spec or register
   line, the two readings of the range rule applied consistently. U71's falsifier failed twice and was not run
   a third time. Fix what it finds; if it fails with blocking findings, fix and run it once more; report the
   verdict of the last pass plainly.
5. Output: sws/hw-selection/sws_sensor_literature.md (the table + sources + section 2); a short paragraph and
   link in the hardware page's "The sensor" section ("what others use"), keeping that page at 6 A4 or less.
   Nothing selected; no person, no role, no dates in prose.
6. Prove: seven `--check`; SWS page test files except p52; counts printed; identifier scans 0 (scan_tree on
   added lines; idscan d98e70d..HEAD).
Report tasks/reports/U72.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes
in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
names. Sign every message with your name. Timebox 2 hours; past it, stop and report. — Kai

## U73 — fold the blind sensor round in: what three models chose, checked against the data sheets; and close the falsifier (Kai, 12 Nov)

The blind sensor round the owner asked for is back: C:/Users/stian/sensor_round_2026-11-12/ (brief.md, models.yaml,
answers/2026-11-12/: Fable, GPT 5.6 Sol extra high, Grok 4.7 high; round.json). Every figure in the answers is
from the models' memory. The round was sent before the prototype's parts were known (its brief says "part number
not known"). Same job as U68 did for the sealant round.

`git worktree add C:/Users/stian/Prosjekter-u73 -b u73-sensor-round c551297` from C:/Users/stian/Prosjekter-u05
(c551297 = U72's tip, not yet on main; build on it). Work in C:/Users/stian/Prosjekter-u73/max; venvs as U71.
Read spinnaker.md, leeboard.md, gangway.md (U68's pattern), U71 and U72 above, both sensor notes whole, then the
three answers.

1. The round into the repo, as sws/housing/rounds/2026-11-11/ is laid out: sws/hw-selection/rounds/
   2026-11-12-sensor/ with brief, models, answers, and a synthesis.md: what each chose per channel and why, where
   the three agree, where they differ, what each says about the range rule, the full bridge, the bias / offset /
   null ideas, power and mounting, calibration over ten years, prototype measurements in order, and their
   questions to us. Model output is quoted as model output. scan_tree on the folder: 0.
2. Every part a model names, against its data sheet actually opened (URL, date; U71's rules): DRV5055 A4 and A2
   (in the table already — check the models' figures against it, incl. supply current, noise density, sensitivity
   temperature coefficient, package options and sensing axis for SOT-23 and TO-92), TMAG5273 (ranges, bit depth,
   noise per axis and averaging, conversion time against 250 S/s, current, I2C addresses, axes), TLE493D-W2B6
   (range, resolution, axes), Allegro A1308/A1309 (3.3 V? range?), TMAG5253 (the low-power analog Hall one model
   mentions — exists? range, enable pin, noise), and the programmable-offset parts named (A1363, HAL 18xy,
   TLE4997: supply voltage only). A table "what the model said / what the sheet says / verdict". Add rows to the
   candidate table for the parts not in it. Where a model's claim is wrong, say so plainly.
3. The two things the choice turns on, worked from sheets and the record, shown as arithmetic with the record's
   figures: (a) power — the record's about 1 mW per sensor against a Hall's supply current at 3.3 V, continuous
   and duty-cycled within a 4 ms sample period (start-up / settling time from the sheet), per half and per head
   against the half's power figure on the hardware page; (b) mounting — a part sensing out of plane on a spoke
   board in the r–z plane: what edge mounting or a leaded upright part does to the stand-off and the 3 × 3 mm
   rule in the record. No design: state what the record's rule says and what the part needs.
4. Three views side by side, short, for the page: what the data sheets allow (U71), what others use (U72), what
   the models chose (this unit), and what the old prototype carries (TMR2185, TMR2584) — where they agree and
   where they do not. Nothing selected; the record's requirement stays as written, with the models' and the
   literature's challenge to the 2× rule and to the full bridge stated as open questions for the outside expert.
5. Life cycle: the in-place checks the models propose (a test coil on each spoke; a reference sensor on the yoke
   to separate magnet ageing from rope wear; a reference rod or test wire at the periodic inspection) and EN
   12927's own cycles from U72 (clause numbers only) into the recalibration and operation placeholders on the
   procedures page, as "proposed, not decided", still "Not written yet".
6. Pages: hardware page stays at 6 A4 or less — if the sensor section cannot hold this, say so in your report and
   propose (do not build) a page of its own; procedures page ≤ 4 A4.
7. Close the falsifier. U71 and U72 ran four passes, every one FAILED, the last not re-run. Fresh subagent on
   both sensor notes, the synthesis and the two page sections: every figure against its sheet — including the
   sheets not re-opened in pass 4 (SS495A, HMC1021, CT100, A1367, AFF756/AFF755B, TMR2151S) and the two prototype
   sheets at C:/Users/stian/secretary/inbox/MDT-Linear-Sensors-*.pdf (read, never copy into the repo); every
   record citation against its line; both readings of the range rule applied to every row. Fix, re-run. Up to
   three passes; stop when one passes with no blocking finding. If the third still fails, say so first in your
   report, with what is left.
8. Prove: seven `--check`; SWS page test files except p52; counts printed; identifier scans 0 (scan_tree on
   added lines and on the new round folder; idscan c551297..HEAD).
Report tasks/reports/U73.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes
in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
names. General web queries only. Sign every message with your name. Timebox 2 hours; past it, stop and report.
— Kai

## U74 — a sensor page of its own, in the easy-read format: where the sensor can sit on the spoke board, with suggestions (Kai, 12 Nov)

Owner, 12 Nov, after U73: (1) "always use the straight forward format easy read as basic" — new pages are
written plainly first; the dense tables stay in the notes behind links. (2) "The sensor placing on the board I
guess we can change, but the radial board is limited by the size of the wire and such and not much else … you
have the complete item how it is thought to be so please help in the suggestions with some more information."
(3) Read what was not read, where it matters. (4) Agreed by the owner: the sensor selection is its own page —
"there is enough things to think about there and it is the most important in some ways". So: the sensor gets its
own page, written as an explanation, and its centre is the placement question U73 left open — a Hall part senses
out of its package plane, the record has the spoke board in the r–z plane with a ≤ 3 × 3 mm in-plane part at its
inner edge. The ruling to record: **the placement of the sensor on the spoke board may change; what limits the
spoke board is the rope (its diameter, its movement) and little else.** Suggestions, not a design; nothing
selected.

`git worktree add C:/Users/stian/Prosjekter-u74 -b u74-sensor-page d9b602d` from C:/Users/stian/Prosjekter-u05; work
in C:/Users/stian/Prosjekter-u74/max; venvs as U71. Read bowsprit.md, spinnaker.md, leeboard.md, U71–U73 above,
the easy read (docs/sws/build_easy.py — its voice is the model) and how it was briefed (U54 above), both sensor
notes and the round synthesis. Then "the complete item as it is thought to be" — gather it before you write:
spec render rev130 §6 (spoke boards in the r–z plane, 8 per half at 22.5°, inner edge at a fixed stand-off, what
the spokes plug into, coverage table), §5 result 5 (guard, clamshell), §7 package row;
sws/hw-selection/sws_geometry_stack.py + geometry_stack.json (guard, liner, recess, die depth, stand-off 5 mm,
r_die and clearance per head and rope); sws_standoff_findings.md (signal against stand-off, about 21 % per mm);
sws_angular_snr.py (signal against angle between spokes); the sws/3d bz_radius work (field against sensor
radius); the housing page (liner, wear face, what is sealed); the hardware page (board description, power).

1. **The space the sensor has**, worked from those sources and shown as numbers a designer can use, per head /
   rope case on record: sensor radius and stand-off; the arc length between neighbouring spokes at the sensor
   radius (2πr/16) and so the room around the rope for a part or a tab; the radial depth between the liner /
   guard and the die; the axial room mid-way between the poles; board thickness if on record; what moves (rope
   movement 2–3 mm, +4 % diameter). Each with its source; "the record does not say" where it does not.
2. **Ways to place the sensor**, four to six, each described the same way — a small sketch, what it is, which
   sensor types it suits (in-plane bridge, out-of-plane Hall in a small package, leaded Hall, 3-axis part, a
   printed or wound coil), where the sensing element ends up (distance from the rope surface → signal kept, by
   the record's signal-against-stand-off law), the room it takes around the rope, how the radial and the axial
   channel are both served, assembly and alignment (tilt → cross-field leakage, with the arithmetic), what
   potting or filling does to it, what is unknown. Candidates to consider; keep the ones that are real practice
   or follow directly from the geometry: (a) as the record has it — in-plane part flat on the spoke at the inner
   edge; (b) a small out-of-plane part on a tab or tongue at the inner edge, turned 90°; (c) a leaded part
   standing upright; (d) a small ring or arc board (rigid or flex) lying tangentially around the rope, carrying
   out-of-plane parts that face the rope for the radial channel, with the spokes or a second part for the axial
   channel; (e) one 3-axis part flat on the spoke; (f) a printed coil on the spoke beside a field sensor. Look
   up how commercial Hall-ring rope testers and MFL heads arrange theirs (U72's sources first; general queries
   only) and say which arrangement each resembles.
   For the radial channel say the plain geometric fact: a part whose sensitive axis is normal to its face
   measures the radial field when its face looks at the rope — and what that means for a board that wraps the
   rope instead of standing on edge.
3. **A comparison at a glance** — one table or one figure: placement against signal kept, room taken, both
   channels yes/no, parts that fit it (from the candidate table, with their verdicts), assembly risk. Then two
   or three combinations worth putting to the head designer and the outside expert, each in three lines, marked
   "suggestion, not selected", with what next week's test on the old prototype can tell about each.
4. **Read what was not read, where it bears on these suggestions**: DRV5055 power-on / start-up time (the
   sheet again, and the maker's application notes if the sheet is silent); TMAG5253 full sheet (enable time,
   noise, package and element position); package drawings for the element position of every part kept in
   section 3; distributor stock and lifecycle for the TI parts and the two prototype parts; the TMR rope paper
   U72 could open only as an abstract, if it can be had. Not needed: parts named only as classes. Say what
   stayed unread.
5. **The page**: `docs/sws/build_sensor.py` → `docs/sws/sensor.html`, menu entry "The sensor" after "Hardware
   selection" (eight entries on all eight pages; tests updated). Easy-read voice throughout: what the sensor has
   to do in plain words; what we found (the four views in a few sentences — data sheets, what others use, what
   the models chose, what the old prototype carries); where the sensor can sit (sections 1–3, sketches);
   calibration through its life in five lines linking the procedures page; what is open and who settles it.
   Short sentences, no status codes, no line numbers in the text; sources behind links; the full tables stay in
   the notes. ≤ 5 A4. Reduce the hardware page's "The sensor" section to a short paragraph and a link (say the
   hardware page's new length). Record the owner's ruling in the register in the form of the 11 Nov rulings. No
   person, no role, no dates in prose.
6. Sketches: schematic, drawn by script (matplotlib, under sws/figures/, the u05 venv), each marked "not to
   scale, not the design"; one figure with the placements side by side beats six separate ones. Look at every
   figure you make before you keep it.
7. Reviews, fresh subagents: (a) a cold reader with no background: can they say back what the sensor must do,
   why the bridge is in question, and what the placement options are; (b) a PCB / sensor-mechanics engineer:
   are the placements buildable, what is wrong or missing; (c) a falsifier: every number against the geometry
   files, the sheets and the record lines. Fix; re-run the falsifier until it passes, at most three passes.
8. Prove: eight `--check`; SWS page test files except p52; counts printed; identifier scans 0 (scan_tree on
   added lines; idscan d9b602d..HEAD).
Report tasks/reports/U74.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export. Notes
in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
names. General web queries only. Sign every message with your name. Timebox 2.5 hours; past it, stop and report.
— Kai

## U75 — export increment for U70–U74, then the Pages snapshot, every link proven on eight pages (Kai, 12 Nov)

Same job as "## U69" and "## U63" above; read them, bobstay.md and scuttle.md first (the method, the link script
at C:/Users/stian/export-v3/tools/links12.py). The owner has given the go to publish, on the condition that all
is checked properly; Kai pushes after a final check; you do not push.
State: local main = a3a633a (U70 procedures page, U71 sensor run, U72 literature sweep, U73 blind sensor round
folded in, U74 the sensor page and placement suggestions); D: same. GitHub fjordbit/max main = export clone tip =
025a0af (it exported local 8f97214). publish/SWS = both Pages remotes = 2dc95f3. Verify before you start; stop if
they differ.
A. Export: max/ subtree increment 8f97214..a3a633a, first-parent, grafted on 025a0af, fast-forward only. Only
   tree content travels: confirm the export clone holds no object from the U74 branch's earlier, squashed
   commits (they are unreferenced in the local store; one of them listed a personal name in a test file). Scan
   tip and increment (scan_tree with the u05 venv; idscan): 0 on everything added, including the new folder
   sws/hw-selection/rounds/2026-11-12-sensor/ (brief, three answers, synthesis), the two sensor notes, the
   placement note / script / json, the figure sws/figures/sensor/, hover titles, alts, captions, the register's
   new rows. Where scan_tree reports hits on a re-rendered long line of report.html, show the removed side
   carries the same count. Also confirm by search that no data-sheet PDF, no standard text and no file from
   secretary/ or max-private/ is in the increment. `--check` for all eight builders and the SWS test files
   (expect 151; skip test_sws_p52) with the u41 venv, run in the export tip.
B. Snapshot in C:/Users/stian/publish/SWS on 2dc95f3: `sws/` and `docs/sws/` from the export tip. Eight pages,
   eight-entry switch on each, each entry opens; procedures.html and sensor.html are new; add them to the
   publish root docs/index.html if that page lists the SWS pages.
C. Link proof on all eight pages as in U63 / U69: relative and own-repo links 0 broken against the trees that
   will be live; carry or unlink what is not carried and list it. External links: one HEAD per distinct URL
   (send nothing about the project), status per URL saved to your notes; report any 404 by page and link text
   (the dead rope-maker link known from U69 is still expected; list it, do not fix content).
D. Visible text of the two new pages free of local paths, "l.NNN", snapshot notes, personal names, roles and
   dates in prose; scan 0 on the increment; `git status` only sws/ and docs/; rebuild index.zip (untracked).
   Commit "SWS snapshot from MAx <tip>: procedures page, sensor page". No push.
E. Hand back ≤ 12 lines: both tips, link counts per page (broken 0), what you unlinked, external statuses that
   are not 200/redirect, scans, tests, the three push commands. Notes in C:/Users/stian/agent-notes/<nautical
   name>.md (a name not in that folder). No identifier values, no personal names; never print the contents of
   max-private/identifiers.yaml. Timebox 1 hour; past it, stop and report. — Kai

## U76 — a chapter "What the sensor measures" on the sensor page; and the owner's maintenance statement into the record (Kai, 16 Nov)

Owner, after reading the sensor page: the page tells about the sensor as a part, but the magnetic effects it
measures have no chapter of their own — they are spread over the full report and the short page. He wants it
**as a chapter on the sensor page**. Easy-read voice (the model is docs/sws/build_easy.py and the sensor page
as it stands); dense detail stays in the notes behind links. Nothing selected, no new simulation runs.

`git worktree add C:/Users/stian/Prosjekter-u76 -b u76-what-the-sensor-measures a3a633a` from
C:/Users/stian/Prosjekter-u05; work in C:/Users/stian/Prosjekter-u76/max; venvs as U74 (page builds and tests:
Prosjekter-u41/max/.venv; figures and scan_tree: Prosjekter-u05/max/.venv). Read the U74 brief above and its
builder's note first, then docs/sws/build_sensor.py.

1. **The chapter**, placed after "What the sensor has to do" and before "What we found" (shorten "What the
   sensor has to do" where the two would repeat). It answers, in this order, in plain words with the numbers
   the record already holds:
   - What is there with no fault: the magnets drive flux along the rope; the rope is close to saturated; some
     field stands in the air around it. What the axial and the radial part of that standing field are at the
     sensor (the background per head / rope on record), and why they differ so much.
   - What a broken wire does: flux leaks out at the gap; the picture of it (the dipole reading the spec uses);
     what the radial channel sees as the break passes (its shape, how long along the rope) and what the axial
     channel sees; how large (the 0.20–0.39 mT on record, and what sets where in that span a break falls — depth
     in the rope, angle between spokes, gap length, if the record says).
   - What lost metal over a length does (wear, corrosion — the LMA reading in the standard's terms, against LD
     for a local break): which channel shows it, as a slow change of the level rather than a blip; what the
     record holds on its size and what it does not.
   - What the rope's own build adds: the strand / lay pattern as a repeating signal, its size against a break
     where on record, and how the template takes it away.
   - What changes the reading that is not the rope's condition: stand-off (the law on record, about 21 % per
     mm), the rope off centre or moving, the angle between spokes, speed (and why a field sensor, unlike a coil,
     reads the same at any speed), temperature (magnet and sensor), the split between the halves.
   - One closing paragraph: so the sensor has to see a small change on top of a large standing field — which
     is what the rest of the page is about.
   Sources to gather before writing: spec render rev130 §5–§7; the short page and the easy read (what they
   already say, so the three do not contradict); sws_standoff_findings.md; sws_angular_snr.py and its results;
   the sws/3d bz_radius work; the 2D / 3D result files the full report cites for background and signal; the
   clause map's terms (clause numbers only, no standard text). Every number with its source behind a link;
   "the record does not say" where it does not — do not fill a gap from general knowledge without marking it
   as such and giving a general source.
2. **Figures**: use what exists first (the report's field and signal figures). Wanted at least: one picture of
   the leak at a break with the two field directions marked, and one of the two channel traces as a break
   passes. If none on record fits, draw a schematic by script (matplotlib, sws/figures/sensor/), marked "not to
   scale", or plot the traces from result files already in the repo (say which). Look at every figure before
   you keep it.
3. **Length**: the sensor page may grow to ≤ 5 A4. Say its new length.
4. **The owner's statement of 16 Nov, into the record** (register, in the form of the 11–12 Nov rulings; no
   name, no role in prose): during maintenance the head stands unshielded for some hours, perhaps a day; the
   temperature sensor should give a warning when the magnet nears its demagnetisation temperature; a
   stainless-steel shield against direct sun on the magnet is suggested, "may already have been considered".
   Set beside it, as findings and not decisions, what the record already holds: the first-application
   statement (head deep under the hoist equipment, never in direct sun), the service ruling (magnet ≤ 45 °C,
   fully covered), the sun study's cases (unshielded light grey, under an open shade, fully shaded; and that
   bare stainless runs warmer than light grey in that study), the magnet head's time constant of hours, and
   whether any warning threshold or temperature alarm exists in the spec (search; say "none found" if so). The
   maintenance case is therefore outside the "fully covered" assumption — say so plainly. Put one short open
   item on the housing page and one line in the operation / maintenance placeholder of the procedures page,
   each linking the register row. No threshold proposed as a decision; if the record's grade data give the
   temperatures at which irreversible loss starts for the two grades at the working point, cite them.
5. Reviews, fresh subagents: (a) a cold reader with no background: can they say back what the sensor sees with
   no fault, at a break, and at lost metal, and what else moves the reading; (b) a falsifier: every number and
   every physical statement in the new chapter and in the register row against the result files, the spec lines
   and the sun study. Fix; re-run the falsifier until it passes, at most three passes.
6. Prove: eight `--check`; SWS page test files except p52 (151 before you start; update tests for the new
   chapter); counts printed; identifier scans 0 (scan_tree on the changed pages and new files; idscan
   a3a633a..HEAD).
Report tasks/reports/U76.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export.
Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no
personal names; never print the contents of max-private/identifiers.yaml. General web queries only (nothing
about the project, the company, the product, the rope maker or persons). Sign every message with your name.
Timebox 2 hours; past it, stop and report.
— Kai

## U77 — the rig sheet for the prototype test: what to record, in what order, with which settings (Kai, 16 Nov)

The test on the old prototype head with the 40 mm rope starts in two days and runs three days. The procedures
page holds a data list (17 rows) for it but no procedure. The owner has said yes to a rig sheet: **something a
person can print, carry to the rig and fill in with a pen**, and a plan for the order of the runs. Easy-read
voice. It is a proposal to the people who run the test, not an instruction to them: they know the rig, we do
not. Another unit (U76) is working at the same time on the sensor page, the register, the housing page and one
line in the operation placeholder of the procedures page — stay out of those; on the procedures page touch
only the prototype-test stage.

`git worktree add C:/Users/stian/Prosjekter-u77 -b u77-rig-sheet a3a633a` from C:/Users/stian/Prosjekter-u05;
work in C:/Users/stian/Prosjekter-u77/max; venvs as U74. Read first: docs/sws/build_procedures.py (the data
list and its sources), the U70 brief and mooring.md, the sensor page and both sensor notes (what the test can
and cannot tell: the background each part must range, whether the in-plane and the Z-axis part clip, whether
a cross field changes their gain), sws_sensor_placement.md, the register's statement on the old prototype's
parts, and the two data sheets of those parts in C:/Users/stian/secretary/inbox (read only; never copied into
the repo). What is NOT known about the old prototype is listed in the register and in U73's note (which part
on which channel, package, count, radius and stand-off, the multiplexer / amplifier / converter parts, bridge
supply, sample rate): the sheet asks for these, it does not assume them.

1. **The sheet**: `docs/sws/build_rig_sheet.py` → `docs/sws/rig_sheet.html`, linked from the prototype-test
   stage of the procedures page (not a ninth menu entry). Prints cleanly on A4 (print CSS, black on white, lines
   and boxes to write in, page breaks where a section ends); at most 4 A4, the first being a one-page overview a
   reader can take in standing up. Sections:
   a. Before the first run — the rig as found, written down once: the unknowns above as fill-in fields; rope
      (diameter measured, construction, length available, known or made defects and where they are, with a
      sketch box); head (stand-off measured at several angles, which half is which, orientation mark);
      temperature; what records the data, file format, sample rate, how position or time is marked; photos to
      take (a tick list).
   b. The runs, in the order that gives the most if the test is cut short — put first what the sensor question
      needs: (1) the standing field with no rope and with the rope at rest, per channel, in raw units and, if a
      handheld gaussmeter is at hand, in mT at the sensor position; (2) noise with the rope at rest; (3) a clean
      length at the nominal speed, repeated; (4) the same over a known defect, both directions; (5) stand-off or
      off-centre steps if the rig allows; (6) speed steps; (7) a temperature note per run. For each run: purpose
      in one line, settings, how many repeats, what to write down, the file name. Say which of the 17 data rows
      each run fills, and which rows no run can fill on this rig.
   c. A run log table to fill in (run number, time, what, settings, file name, remarks), enough rows for three
      days.
   d. What to look at on the spot, so a bad run is caught while the rig stands: is any channel flat at a rail
      (clipping), does the level come back after the rope has passed (hysteresis), does a repeat lie on the
      first.
   e. File naming and where the data goes afterwards — a proposed pattern, no path on anyone's machine.
   Where a setting is the rig owner's to choose, leave a field, with the record's value beside it as "on
   record: …" and its source behind a link. Numbers on the sheet come from the record (speed 15 m/min, 250 S/s
   and 1 sample per mm, stand-off 5 mm, the signal and noise figures, the data sheets' ±20 mT specified range
   and saturation values); mark anything that is your own proposal as a proposal.
2. **Safety line**: one short box — strong magnets and a moving rope; the site's own safety rules govern; the
   sheet adds none. No procedure for handling the magnets is invented here.
3. **What comes back**: a short last section — what the filled sheet and the files let us answer afterwards
   (three to five questions, each tied to runs), so the people at the rig see why each run is asked for.
4. Reviews, fresh subagents: (a) a test technician who has never seen the project: can they run the three days
   from the sheet alone, what would they have to ask; (b) a falsifier: every number against the record and the
   two data sheets; every one of the 17 data rows either filled by a run or named as not fillable. Fix; re-run
   the falsifier until it passes, at most three passes. Look at the printed form yourself (render to PDF or
   screenshots if a headless browser is at hand; say if not) — count the pages.
5. Prove: all `--check` (now nine builders if yours has one); SWS page test files except p52 (151 before you
   start; add tests for the sheet and the link); identifier scans 0 (scan_tree on the new files and the
   procedures page; idscan a3a633a..HEAD).
Report tasks/reports/U77.md (≤ ½ page), TASKS.md entry. Commit on the branch; no merge, no push, no export.
Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no
personal names, no roles, no dates in page prose (date and names are fill-in fields on the sheet); never print
the contents of max-private/identifiers.yaml. General web queries only. Sign every message with your name.
Timebox 2 hours; past it, stop and report.
— Kai

## U78 — the model round as a small repo of its own, easy to start on another machine (Kai, 16 Nov)

The owner's manager wants to run the same workflow we use: one question (a brief) put to several models at
once, each working blind in an empty folder — Claude through Claude Code, the others through the Cursor CLI —
the answers collected side by side, then a synthesis that checks what they claim. Today that is
`tools/review_round.py` inside the project repo, tied to it by imports from `max_core.providers` (`_cli`,
`claude_cli`, `codex_cli`), by the private masking tools, and by default paths. Wanted: **that part only, as a
repo that starts easily on his Windows machine**. He has (or will have) Claude Code and Cursor installed; assume
nothing else beyond what the README tells him to install.

Build it LOCAL ONLY at `C:/Users/stian/model-round` (new folder, `git init`, branch main). No remote, no push,
nothing published — where it goes is the owner's decision, later. Do not change the project repo.

Read first: C:/Users/stian/Prosjekter-u05/max/tools/review_round.py, review_models.yaml, tools/preambles/,
test_review_round.py, max_core/providers/_cli.py, claude_cli.py, codex_cli.py; how a round was really run
(C:/Users/stian/sensor_round_2026-11-12/: brief.md, models.yaml, answers/ with round.json) and how a round was
folded in afterwards (kai.md "## U73" and the synthesis under sws/hw-selection/rounds/2026-11-12-sensor/).

1. **The tool**, standalone: one small package or a single script plus helpers, Python ≥ 3.11, dependencies
   kept to PyYAML (or none). Carry over what makes it safe and keep it true: each backend runs in its own fresh
   empty folder holding only input.md; Claude Code with no tools, no CLAUDE.md, no memory, no session file;
   Cursor in ask mode with the workspace set to that folder; Codex read-only if installed; keys from the
   environment only, never stored or printed. Drop what is ours: the masking step and private tools, the
   project's pack layout, the register / spec file list, default paths into the project. Inputs: a brief
   (markdown), optionally a folder of text files to send with it (size limit stated, what was sent and not sent
   recorded in each answer's header), a models file. Commands kept: `--list` (what would be sent, which
   backends are ready, sends nothing), `--dry-run` (a ten-line dummy text to every backend), the real run,
   `--only`. Output: `rounds/<date>-<name>/answers/*.md` with the header block, `round.json`.
   Fix while you are there: if ANTHROPIC_API_KEY is set but rejected, say so clearly and tell the user how to
   run on the Claude Code login instead (a flag `--claude-login` that ignores the key is better than asking him
   to unset a variable). A backend that is not installed or not logged in is reported, with the one command
   that fixes it, and the round goes on without it.
2. **Models file**: a small default (Claude via Claude Code; two Cursor rows using `pick:` so it works with
   whatever names his account lists; Codex row off by default), with the comments that explain a row. No tier
   study, no notes of ours.
3. **The synthesis step**, as we do it: a prompt file for Claude Code (a slash command or skill in the repo's
   `.claude/` folder — check the current Claude Code docs for the right form) that reads the answers of a round
   and writes `synthesis.md`: where the models agree, where they differ, every claim marked "from memory" or
   unsourced listed for checking, and no claim taken over as fact without a source. Plus a repo CLAUDE.md, short,
   so that he can open Claude Code in the folder and say "run a round on this brief" and be led through
   `--list`, `--dry-run`, the run, the synthesis. State in it what leaves the machine when a round runs (the
   brief and the attached files go to each model's provider) and that he decides that per round.
4. **README**, easy-read voice, one page: what this is in five lines; what you need (Python, Claude Code logged
   in, the Cursor CLI — it is a separate install from the Cursor editor — and `agent login`); the exact Windows
   commands to install and to check each one; first run in four commands; where the answers land; what it costs
   in rough terms (which subscription each backend draws on; no prices invented); what can go wrong and the fix.
   Verify the install commands against the vendors' current documentation (general web lookups are fine here)
   rather than from memory; say what you could not verify.
5. **An example**: `examples/` with one harmless brief of general interest (not ours — e.g. choosing a
   temperature sensor for a hobby weather station) so a first real run sends nothing of anyone's.
6. **Nothing of ours inside**: no project, company, product, customer or person names, no paths from this
   machine, no content from the project. Scan the whole new repo:
   `C:/Users/stian/Prosjekter-u05/max/.venv/Scripts/python.exe -I C:/Users/stian/max-private/tools/scan_tree.py C:/Users/stian/model-round`
   must report 0; also grep it yourself for the user name in paths. Never print the contents of
   max-private/identifiers.yaml.
7. **Prove** on this machine: tests (pytest, backends faked) pass; `--list` and `--dry-run` really run here with
   the Claude Code login and the Cursor CLI (the Anthropic key in this environment is rejected — use your new
   flag); then one real run of the example brief, and the synthesis step on it. Then the cold-start test: a
   fresh subagent that is given only the README and a fresh clone of the repo in a scratch folder (new venv)
   follows it to a dry run and reports every place it had to guess. Fix those.
Commit locally. Hand back ≤ 15 lines: the folder, the tip commit, the file list, what you carried over and what
you dropped, the proof (tests, dry run, real run, cold start), what a new user must install, what you could not
verify. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier
values, no personal names. Sign every message with your name. Timebox 2.5 hours; past it, stop and report.
— Kai

## U79 — export increment for U76 + U77, then the Pages snapshot, every link proven (Kai, 16 Nov)

Same job as "## U75" above; read it, "## U69", "## U63" and gasket.md first (the method; the link scripts under
C:/Users/stian/export-v3/tools/, the newest are the *14.py ones). The owner has said the rig sheet and the
sensor chapter can be released; Kai pushes after a final check; you do not push.
State: local main = 5f415b6 (U76 "What the sensor measures" + the 16 Nov register rows; U77 rig sheet for the
prototype test, the register row "rope fixed, head moves", the AI helper guide); D: same. GitHub fjordbit/max
main = export clone tip = 71288f8 (it exported local a3a633a). publish/SWS = both Pages remotes = f51035e.
Verify before you start; stop if they differ.
A. Export: max/ subtree increment a3a633a..5f415b6, first-parent, grafted on 71288f8, fast-forward only. Scan tip
   and increment (scan_tree with the u05 venv; idscan): 0 on everything added — the new chapter, the figure and
   its script under sws/figures/sensor/, docs/sws/rig_sheet.html and its builder, the new folder
   sws/procedures/ (prototype_test_ai_guide.md), the register rows, hover titles, alts, captions. Where
   scan_tree reports hits on a re-rendered long line of report.html, show the removed side carries the same
   count. Confirm no PDF, no standard text, nothing from secretary/ or max-private/ in the increment. All nine
   `--check` and the SWS test files (expect 180; skip test_sws_p52) with the u41 venv, in a copy of the export
   tip.
B. Snapshot in C:/Users/stian/publish/SWS on f51035e: `sws/` and `docs/sws/` from the export tip. Eight menu
   pages with the eight-entry switch as before; rig_sheet.html is a ninth page that is NOT on the menu — it must
   open from the procedures page's prototype stage, and its own links (back to the procedures page, to the AI
   guide) must work in the snapshot. The AI guide is a .md file: say where its link lands on the Pages site and
   in the code repo, and that the target exists in the tree that will be live.
C. Link proof on all nine pages as in U75: relative and own-repo links 0 broken against the trees that will be
   live; carry or unlink what is not carried and list it. External links: one HEAD per distinct NEW URL only
   (those not already in your predecessors' status list); send nothing about the project.
D. Visible text of the changed and new pages (sensor, rig sheet, procedures, housing) free of local paths,
   "l.NNN", snapshot notes, personal names, roles and dates in prose; the rig sheet prints to 4 A4 from the
   snapshot copy (headless Edge, count pages). Scan 0 on the increment; `git status` only sws/ and docs/;
   rebuild index.zip (untracked). Commit "SWS snapshot from MAx <tip>: what the sensor measures, rig sheet".
   No push.
E. Hand back ≤ 12 lines: both tips, link counts per page (broken 0), what you unlinked, new external statuses
   that are not 200/redirect, scans, tests, the page count, the three push commands. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
   names; never print the contents of max-private/identifiers.yaml. Timebox 1 hour; past it, stop and report.
— Kai

## U80 — Vessel Library: a review reply to the product owner (draft) and a first design (Kai, 16 Nov)

Not SWS. A new line of work, and meant to become the first coding task. The owner's manager (the product
owner for this) sent initial requirements for a "Vessel Library System / Vessel Database" and asked the owner
what is missing or unnecessarily complicated before it goes to development. The owner travels this week and
wants this prepared. Two deliverables: a short reply he can send, and a first design he can read. No code yet.

These documents are internal working documents: real names of colleagues and customers may appear in them where
the sources use them (they live outside max/ and are never exported). Do NOT put any of it under max/.

`git worktree add C:/Users/stian/Prosjekter-u80 -b u80-vessel-library 5f415b6` from C:/Users/stian/Prosjekter-u05.
Read first, all of it:
- the requirements mail: C:/Users/stian/secretary/inbox/GMail/mails_as_text.txt (the second mail, 5 Oct);
- our older brief: agentic/01_Vessel_Database_Project_Brief.md, and agentic/00_Portfolio_Split_and_Project_Briefs.md,
  agentic/07_Questions_For_Ramin.md, agentic/04_Price_Prediction_Concept.md (does the price idea lean on a
  vessel database?);
- what the record says about the company's environment: C:/Users/stian/Prosjekter-u05/INPUT - Functional
  Specification Digital Systems and Services.md (skim for vessels, hosting, users, security), and the
  logging-maintenance/ and systems-integration/ notes for hosting and IT constraints already known.
Compare the mail with the older brief: say where they agree, where the mail is new, where our brief had
something the mail drops.

1. **The reply, as a draft**: `C:/Users/stian/secretary/inbox/drafts/2026-11-16_ramin_vessel_library_reply.md`
   (plain file, not in the repo; the owner sends it himself — never send anything). In the owner's voice: short,
   direct, friendly, English. At most one screen. Shape: yes to starting simple; three to five things that are
   missing and matter for a first version; two or three that are more complicated than they look and how to cut
   them; the two or three decisions needed from him before development starts; a proposed next step. Candidates
   to weigh, keep only those you can argue: where it runs and who logs in (company accounts / single sign-on);
   where the files physically live and their size (CAD files, large PDFs) and backup; who owns the truth for
   project number and customer (an existing system?) so it is linked and not typed twice; duplicate vessels
   (renamed, no IMO number, sister vessels); confidentiality of customer documents and who may see what (three
   roles may not be enough per customer); "configurable properties" (cheap to promise, costly to build well —
   units, types, history); import of what exists today (where is it now: file shares, mail, people's heads?);
   full-text search inside documents (phase 1 or later); the licences of the outside vessel sites named in the
   mail if data were ever copied from them (do not assert — raise it as a question).
   Below the draft, under a line, a short list for the owner only: what you assumed, what you left out and why.
2. **The first design**: `vessel-library/01_First_Design.md` in the worktree (new top-level folder beside
   agentic/). Easy-read voice: plain, short sentences, tables where they help, at most 6 A4. Sections:
   what it is for and who uses it (one paragraph); phase 1 scope as a list of what a user can do — and what is
   deliberately not in; the data model (entities, key fields, relations; how "configurable properties" are
   stored; how change history and archive-not-delete work) with one diagram (mermaid in the markdown is fine);
   two or three architecture options that are honestly different (for example: a small web application with a
   database and file storage we host; building on a platform the company already has, if the record names one;
   a document-library product configured for the purpose) each with cost to build, cost to run, what it needs
   from the company's IT, and risk — then ONE recommendation with its reason, marked as a recommendation, not a
   decision; search (what is indexed in phase 1); security and roles; what would be built first (a walking
   skeleton in one to two weeks: which screens, which data) and a rough size for phase 1 in person-weeks as a
   range with what drives it; how it could be the first task run through the multi-agent flow (what an agent
   needs as input: this design, acceptance tests per feature); open questions with who answers each.
   Do not invent facts about the company's systems: where the record is silent, write "not known" and put it in
   the open questions. General technology facts may come from general web lookups (no company, customer or
   person names in any query).
3. Reviews, fresh subagents: (a) a cold reader who is a naval architect / project engineer and would use the
   tool: is anything they need daily missing, is anything there they would never use; (b) a software architect:
   is the data model sound, are the options honestly compared, is the size estimate defensible. Fix what is
   right; list what you did not take and why.
Commit the design on the branch (the draft is outside the repo). No merge, no push. TASKS.md is not touched (it is
the max project's). Hand back ≤ 15 lines: branch and tip; the reply in five lines; the recommendation and its
size range; the top five open questions; the reviewers' verdicts; what you could not find in the record.
Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name.
Timebox 2 hours; past it, stop and report. — Kai

## U81 — Oracle integration with the maintenance system: what the existing API can do, mapped to the open questions; an estimate skeleton (Kai, 16 Nov)

Not SWS. A customer wants its Oracle system linked with the maintenance management system we deliver. Our
contract manager sent the customer a list of questions after a first meeting (28 Sep) and wrote that our
software designer (the owner) will estimate hours once they are answered; the thread we have holds no answers.
The mail links the maintenance system's API description. Kai's reading: the API already exists (it is the
maintenance product's own, versions 1.0 and 2.0); the work is the link between the customer's Oracle and that
API. Check that reading — say if it is wrong. The owner travels this week; prepare what can be prepared without
the customer's answers.

Internal working document: real customer and colleague names may appear where the sources use them; it lives
outside max/ and is never exported. Nothing is sent to anyone.

`git worktree add C:/Users/stian/Prosjekter-u81 -b u81-oracle-integration 5f415b6` from
C:/Users/stian/Prosjekter-u05. Read first:
- the mail: C:/Users/stian/secretary/inbox/GMail/mails_as_text.txt (the first mail);
- both API descriptions, saved locally: C:/Users/stian/secretary/inbox/GMail/api/maintenance_api_v1_swagger.json
  and maintenance_api_v2_swagger.json (OpenAPI; ~200 and ~330 KB — parse them with a script, do not read raw);
- our earlier notes: systems-integration/01_Spare_Parts_API_Questions.md, logging-maintenance/01–03 (what we
  already know or guessed about the maintenance product and remote access).
HARD LIMITS: do not call the API (no token request, no GET on data endpoints, nothing beyond the two files
already saved). No web query containing the customer's, the company's or any person's name. General lookups
about Oracle integration options (product families, integration middleware, typical REST patterns) are fine.

Deliverable: `systems-integration/02_Oracle_Integration_API_Map_and_Estimate.md` in the worktree. Easy-read
voice, tables, at most 6 A4:
1. In ten lines: what is asked, what exists, what is missing to estimate.
2. **What the API can do**, from the two files, as one table per area (spare parts and stock; stock
   transactions; assets and counter readings; work orders incl. hours, parts, completion; purchase and storage
   orders; suppliers, customers, invoices; projects; rounds and check lists; value lists; anything else):
   operations available (read / create / change), the paging and "changed since" filters that make
   synchronising possible (which endpoints have a last-modified or from-date filter and which do not), external
   reference fields (anything like ExternalRef / external identification that lets two systems share a key),
   and differences between v1 and v2. Counts printed by your script go in an appendix so the tables can be
   checked. Say what the description does NOT tell: authentication details (it declares a token endpoint — what
   grant, what scopes, if stated), rate limits, webhooks or events (is there any push, or is it polling only?),
   error model, whether the dev instance equals what the customer runs.
3. **The contract manager's questions, each with**: why it matters for the estimate; what the API description
   already answers on our side; the two or three likely answers and what each would mean for the design.
4. **Three integration shapes** that are honestly different (for example: the customer pulls from the API with
   their own integration platform and we only support; we build and host a small synchronising service between
   the two; file / batch exchange on a schedule) — for each: who builds what, where it runs, what it needs from
   the customer's IT, failure handling, and a rough hours RANGE with the assumptions that drive it. Mark every
   figure as a first estimate that depends on the answers. One recommendation, marked as such.
5. **The data flows most likely wanted** (from the mail's own examples: work orders, schedules, operating hours
   / counters, spare parts / inventory, costs, completion reports): for each, direction, which system is
   master, which endpoints carry it, what is awkward.
6. A short list: what the owner should ask the maintenance product's supplier (not the customer), and what to
   ask the customer beyond the questions already sent. And a draft, clearly marked DRAFT and placed at
   C:/Users/stian/secretary/inbox/drafts/2026-11-16_sondre_oracle_integration_status.md, of a five-line note the
   owner could send the contract manager: what is prepared, what is still needed from the customer.
7. Review by a fresh subagent acting as an integration architect with ERP experience: are the shapes and hour
   ranges defensible, what is missing. And a falsifier: every statement about the API against the two files
   (endpoint exists, filter exists, field exists). Fix; at most two passes.
Commit the document on the branch. No merge, no push. Hand back ≤ 15 lines: branch and tip; whether Kai's reading
holds; the API in five lines; polling-only or push; the three shapes with their hour ranges; the recommendation;
the questions that move the estimate most; reviewers' verdicts; what the files do not tell.
Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name.
Timebox 2 hours; past it, stop and report. — Kai

## U82 — model-round repo: the way of working around the rounds (sub-agents, briefs, fresh reviewers) (Kai, 16 Nov)

The repo C:/Users/stian/model-round (GitHub: private, pushed at b1325d1) lets a new user run one brief past
several models. The owner wants the method we use around it in the repo too, so that his manager can work the
same way in Claude Code: the main session stays lean and hands work to sub-agents; a builder never checks its
own work; fresh agents review. Generic only — nothing of ours.

Read first: the repo as it stands (README.md, CLAUDE.md, .claude/skills/synthesize-round/SKILL.md), sternpost.md
(the builder who made it), and — as the source of the method, NOT to be copied — a few of Kai's briefs in
C:/Users/stian/agent-notes/kai.md (e.g. "## U74", "## U77", "## U78": their shape — goal, read first,
deliverables, reviews by fresh sub-agents, prove, hard limits, hand-back, timebox). Check the current Claude Code
documentation for the exact form of sub-agent definition files (`.claude/agents/*.md`: frontmatter fields,
tools, model) and of skills, and for how a session delegates to a named sub-agent; do not write the format from
memory.

Add, small and plain (easy-read voice, short sentences):
1. **CLAUDE.md**: a second short part, "How to work on a larger task here", after the part about rounds. The
   rules, each in one or two lines with its reason: the main session plans, briefs and checks — the heavy
   reading and writing goes to sub-agents, so the main session's context does not fill up; every task gets a
   written brief in a file before a builder starts (point to the template); a builder never reviews its own
   work — a fresh sub-agent that has seen nothing does; reviewers get the work, not the builder's conclusion;
   timebox every task and stop and report when it runs out; report plainly what was not verified; do not start
   more agents than the task needs (they cost usage); nothing is sent, published or pushed without the user
   saying so. Keep the whole file under about 80 lines.
2. **Three reviewer sub-agents** in `.claude/agents/`: `cold-reader` (no background; reads the result and says
   back what it understood, lists what it could not follow — the test of whether a text explains itself),
   `falsifier` (takes every number and factual claim and checks it against the sources given; verdict PASS or
   FAIL with the list; never fixes), `domain-reviewer` (takes a role named in the request — e.g. test
   technician, software architect — and says what is wrong, missing or not buildable). Each: a description that
   tells the main session when to use it, read-only tools, a tight instruction, a fixed hand-back format.
3. **A builder sub-agent** `builder` (does one briefed task; works only in the folder or branch the brief names;
   does not merge, push or publish; writes a short hand-back incl. what it could not verify).
4. **`templates/brief.md`**: the brief template with one-line guidance per heading — goal and why; what to read
   first; deliverables (files, length); reviews wanted; how to prove it (tests, counts); hard limits (what not
   to touch, what must not leave the machine); hand-back format and length; timebox. And
   `templates/handback.md` (≤ 15 lines: what was done, where, checks with results, reviewers' verdicts, what is
   open or unverified).
5. **A skill** `/brief-task` (or the form the docs recommend) that asks the user two or three questions, writes a
   brief from the template into `briefs/<date>-<name>.md`, shows it, and only on the user's yes starts the
   builder and afterwards the reviewers. `briefs/` is gitignored like `rounds/`.
6. **README**: one short section "Working with sub-agents (optional)", five to eight lines, pointing to the
   above and making clear a round does not need any of it. One worked example in `examples/` if it fits in a
   page (e.g. "write a one-page comparison of two temperature sensors, then have it falsified") — harmless,
   general.
Leave out: anything about roles for a personal assistant, mail or calendar rules, memory files, identifier
scans, project rules, permission or settings files (the user sets permissions himself; say so in one line).

Prove: the 15 existing tests still pass; the agent and skill files load — start `claude` non-interactively in a
clean clone and show that the sub-agents are listed / can be invoked (the Claude Code login; the API key is not
in the environment — do not look for it); run the worked example once end to end if you wrote one (builder →
falsifier), on the harmless example only; a cold-start read by a fresh sub-agent given only README + CLAUDE.md:
can it say how to brief a task and get it reviewed, where did it guess — fix. Nothing of ours inside:
`C:/Users/stian/Prosjekter-u05/max/.venv/Scripts/python.exe -I C:/Users/stian/max-private/tools/scan_tree.py`
on a clean clone must give 0; grep for user and company names and local paths: 0. Never print
max-private/identifiers.yaml.
Commit locally on main (small commits). Do NOT push — Kai reads it and pushes. Hand back ≤ 12 lines: tip, files
added, the format facts you verified in the docs (with the doc page titles), the proof, what you could not
verify. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your
name. Timebox 1.5 hours. — Kai

## U83 — second sensor round into the repo; the gap test on the rig sheet; a paragraph on the sensor page (Kai, 16 Nov)

On 16 Nov three models (Fable 5.2, Grok 4.7 high, GPT 5.6 Sol extra high) answered a second blind sensor brief in
two steps: a preliminary design each, then a cross-check of all three designs with names removed and a revised
design. Everything is in C:/Users/stian/sensor_round_2026-11-16/ : step1_brief.md, step2_brief.md,
step1_files/, step2_files/, rounds/2026-11-16-step1/, rounds/2026-11-16-step2/, labels_private.txt (which label
is which model), summary.md (Kai's one-page summary — a starting point, not a source; check it against the
answers). The owner read the summary and wants (a) the one new test on the rig sheet in plain words — the
prototype test starts Wed 18 Nov, so this part comes FIRST — and (b) the results in the main documents, as
suggestions, nothing selected.

`git worktree add C:/Users/stian/Prosjekter-u83 -b u83-sensor-round-2 5f415b6` from C:/Users/stian/Prosjekter-u05.
Read first: how U73 put the first round in (sws/hw-selection/rounds/2026-11-12-sensor/ : README, synthesis.md,
datasheet_check.md; notes bowsprit.md), how U77 built the rig sheet and the helper guide (docs/sws/build_rig_sheet.py,
sws/procedures/prototype_test_ai_guide.md; notes shroud.md), and docs/sws/build_sensor.py (the "What we found"
list, the line "What three language models chose"; notes topsail.md). Register: sws/data/sws_data_sources.md.

**Part 1 — the gap test (do first, hand back a first note to Kai when it is committed):**
- Rig sheet: one more step, in the sheet's own style and easy-read words, marked IF THE RIG ALLOWS (crossed out
  with one stroke if no wire may be cut and no test piece with two gaps exists): scan the same broken wire at
  two gap widths, about 1 mm and about 10 mm (tight first, then wider — a cut can only be widened), over the
  break and at the worst angle between two sensors, with the gap measured and written down; compare the two
  peaks. What it tells, in two lines: a ratio near 6–7 points to the record's small estimate (the dipole
  picture), near 3 to the 3D model. State where those two numbers come from: the 3D model's own figures (1.89 mT
  at 1 mm, 5.29 mT at 10 mm → 2.8) are in the record — find and cite them; the dipole ratio (6.1 by one model,
  7.2 by another, at 8 mm) is the models' arithmetic — recompute it yourself with a script, show the formula in
  the helper guide, and give the range you get for the sheet's stand-off. If your figure differs from theirs, yours
  goes on the sheet and the difference in the note. The sheet must still fit its page count or grow by at most
  one page; the block "not possible on this rig" stays as it is.
- Also check the sheet's run order against what all three models agreed (channel identity → probe map → noise
  at rest → repeated passes over a sound length → the defect): say in the hand-back whether "find which part is
  on which channel" is already a step; if not, add it as a first small step (how: package markings, and a small
  known field change — the models disagree on how; give the plainest way and mark it a suggestion).
- The AI helper guide (prototype_test_ai_guide.md): the same step with what to record, how to compute the ratio,
  how to read it, and what can spoil it (stand-off changed between the two scans, the gap not measured, the
  wire ends touching, the head's speed different).
- Print copy: write the new rig sheet as a PDF to C:/Users/stian/secretary/inbox/2026-11-17_rig_sheet_print.pdf the
  same way U77 did (see shroud.md); do not touch the old one.

**Part 2 — the round in the repo:**
- sws/hw-selection/rounds/2026-11-16-sensor/ : README, both briefs, the files sent, the six answers (as given,
  front matter kept as U73 did), a synthesis.md written from the answers themselves in U73's manner (counts,
  per model, what changed between step 1 and step 2, quotes), and a datasheet_check.md: every part figure the
  six answers state, against the maker's sheet (the sheets in C:/Users/stian/secretary/inbox may be read, never
  copied into the repo; a sheet not at hand may be fetched from the maker's site — general queries only, part
  numbers are fine, nothing about the project, company, product or persons). Mark each figure confirmed / wrong
  (with the sheet's value) / not on the sheet. In particular: DRV5055A2 range at 3.3 V, DRV5055 noise, bandwidth
  and supply current, whether it specifies hysteresis, its sensitivity temperature coefficient; TMAG5253 BA2/BA4
  ranges, package, current, enable pin; whether A1304 / A1308 / A1309 run at 3.3 V; TMR2151S cross-axis and
  noise statements. And the models' own arithmetic that matters: the range sums, the noise sums incl. the
  "noise folds in without a filter before the multiplexer" claim — recompute, say what holds.
- The models gave opinions on the magnet grade and a 55 °C interim warning. Record them as the models'
  opinions only. The record's rule stands: both grades are run, nothing is selected, no threshold is set.
- Sensor page (docs/sws/build_sensor.py): under "What we found", one short easy-read paragraph or two list
  lines: what three models agreed on after checking each other (placement B; a Hall part on the axial channel;
  the range rule as a sum; noise budget on the small estimate, range on the large; magnet temperature for the
  warning), what is still disputed, and that the figures are theirs — with links to the synthesis and the
  data-sheet check. In "What is open", add the gap test as the way to settle the signal size. No names, roles
  or dates in page prose; nothing selected; page length may grow by at most half a page.
- Register: a short entry for the round (what it is, where, that it is opinion not data).
- TASKS.md: your unit line as the others have it.

Reviews, fresh subagents (they get the work, not your conclusions): (1) a falsifier — every number and claim you
added to the sheet, the guide, the page and the synthesis, against its source; (2) a cold reader who is a test
technician: given only the new rig-sheet step, can they do it and say what the result means; (3) a cold reader
with no background on the new sensor-page paragraph. Fix; at most two passes; report what failed.
Prove: `--check` on every docs/sws/build*.py (venv C:/Users/stian/Prosjekter-u41/max/.venv); pytest
tests/test_sws_*.py except p52; `python -I C:/Users/stian/secretary/tools/idscan.py . 5f415b6..HEAD` = 0 on added
lines; C:/Users/stian/Prosjekter-u05/max/.venv/Scripts/python.exe -I C:/Users/stian/max-private/tools/scan_tree.py
on what you added = 0 (run it from the worktree's parent; TASKS.md has 7 old hits, report.html the known 2 = 2).
Never print max-private/identifiers.yaml. No data-sheet PDF and no standard text in the repo.
Commit on the branch, part 1 as its own commit(s). No merge, no push, no export. Hand back ≤ 15 lines: tip; the
new step as it reads on the sheet; your dipole ratio against the models'; whether channel identity was already
a step; data-sheet check in five lines (what the models had wrong); reviewers' verdicts; pages of sheet and
sensor page; what you could not verify. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in
that folder). Sign with your name. Timebox 2.5 hours; past it, stop and report. — Kai

## U84 — the 52 mm test rope with built-in faults: a first fault list to order from (Kai, 16 Nov)

The owner says a new test rope in the 52 mm size will be made for testing, and it should be ORDERED with
specified breakages built in, because making faults by hand afterwards took days on the old rope and is hard
to do without disturbing something else. He asked Kai to design that rope's fault list "with other important
info". This is a first proposal to discuss and to send to a rope maker later — nothing is ordered, nothing is
selected, and the document must say so.

`git worktree add C:/Users/stian/Prosjekter-u84 -b u84-test-rope 5f415b6` from C:/Users/stian/Prosjekter-u05.
Another builder (U83) is working on branch u83-sensor-round-2 at the same time: touch ONLY your own new files —
not TASKS.md, not the register, not the rig sheet, not the sensor page, no build scripts. Kai adds the links and
the register line at merge.

Read first (the record decides; find, do not assume):
- what the record says about the 52 mm rope: construction, number of strands and wires, wire diameters, lay
  length, core, steel grade (sws/params.yaml, sws/spec, sws/data/sws_data_sources.md, the full report);
- every fault size the record uses: the broken-wire signal estimates and what they assume (depth 3 mm, 2 mm gap,
  the 2×2×2 mm notch source; the 3D model's one and two hidden wires, its 1 mm and 10 mm gap figures; inner-rope
  wire about 13 mm deep), loss of metallic area, the lay pattern, the detection thresholds and the noise budget;
- the procedures page and the rig sheet (docs/sws/build_procedures.py, build_rig_sheet.py; notes shroud.md) —
  which data rows and later tests need a rope with known faults (FAT, calibration, recalibration);
- the 16 Nov model round: C:/Users/stian/sensor_round_2026-11-16/summary.md and the step 2 answers — what the
  models say a test must settle (the gap ratio; crown against worst angle; matched model and measurement);
- what the standard asks of reference defects: C:/Users/stian/secretary/inbox holds EN 12927 as a PDF — it is
  copyright: cite clause numbers only, quote nothing, never copy it into the repo;
- general practice, by general web lookups only (no project, company, product, customer, rope-maker or person
  names in any query): how reference ropes / calibration ropes for magnetic rope testing are made (ASTM E1571
  and similar: reference wires, simulated broken wires, added-rod and removed-wire standards), what rope makers
  can build in during stranding or closing, and what is usually done afterwards by hand. Mark each source.

Deliverable: `sws/procedures/test_rope_52mm_fault_list.md` (new). Easy-read voice: plain, short sentences,
tables; at most 5 A4. Sections:
1. What the rope is for, in five lines: which open questions it settles and which later tests use it.
2. The questions, one per row: question → the fault(s) that answer it → what is compared. At least: the signal
   size (same fault at about 1 mm and about 10 mm gap, all else alike; and one at the record's 2 mm);
   depth (surface wire, wire in the valley, hidden wire of an outer strand, inner-rope wire); angle (a fault
   under a sensor against between two — by rotating the head or rope, not by more faults: say which);
   one wire against two and more, adjacent and spread; loss of metal over a length in two or three steps and
   lengths; a broken strand if the record wants it; corrosion-like loss only if it can be made in a defined
   way; a long clean length for the template and the noise.
3. The fault list as ONE table to order from: ID, kind, which wire or layer, how many wires, gap width with
   tolerance, length, position along the rope (m from a datum), position round the rope, what must be alike
   to which other fault. And the layout rules with their reasons and numbers from the record: clean length
   between faults (longer than the head's reach: poles 100 mm apart, the signal a few centimetres, the lay
   pattern 30–60 mm — derive a spacing and show the sum), clean lengths at both ends, the datum and markers
   (non-magnetic), total rope length this gives, which end is which. A sketch of the layout (a simple figure in
   the markdown or an ASCII strip) if it helps.
4. What the maker must deliver with the rope: construction data and certificate, as-made measurement of every
   fault (gap, depth, position, photo before the wire is covered), steel grade, how the wire ends are held so
   the gap does not close or open under load, whether the rope will be tested loaded or slack and what the gap
   does then (say what is not known).
5. What may not be possible, and the fallback for each: e.g. a hidden wire with a held gap may not be makeable
   during closing — fallback a short separate test piece, or a surface wire only, or a reference wire laid on a
   clean rope (say plainly what such a substitute does and does not prove).
6. Questions to the rope maker (a list he could send), and questions to the owner (which rope construction is
   final, the length the rig takes, load during test, how many identical ropes).
7. What is assumed, what is not on record.
Where the record is silent write "not on record" — do not invent rope data. No personal names, roles or dates in
the prose.

Reviews, fresh subagents (they get the document, not your conclusions): (1) a falsifier: every number against
the record or the cited source; (2) a domain reviewer as a wire-rope maker's engineer: can this be made, what
would they refuse or ask; (3) a domain reviewer as a magnetic rope testing practitioner: does the list answer the
questions, what is missing, what is wasted; (4) a cold reader with no background: what is the rope for and
what would be ordered. Fix; at most two passes; list what you did not take and why.
Prove: idscan on the range (`python -I C:/Users/stian/secretary/tools/idscan.py . 5f415b6..HEAD`) and scan_tree
on the new file = 0 (see the U83 brief above for the exact commands). Never print max-private/identifiers.yaml.
Commit on the branch. No merge, no push, no export. Hand back ≤ 15 lines: tip; the fault list in six lines (how
many faults, the pairs, total rope length); the spacing sum; what makers can and cannot build in, with sources;
reviewers' verdicts; the top five questions to the maker; what is not on record. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. Timebox 2.5
hours; past it, stop and report. — Kai

## U85 — the in-place test loop as an early note on the sensor page; the rig sheet without a coil (Kai, 17 Nov)

Small and fast: the owner flies in the morning and wants to read it on GitHub Pages. Timebox 1 hour.
`git worktree add C:/Users/stian/Prosjekter-u85 -b u85-test-loop 23b5a19` from C:/Users/stian/Prosjekter-u05
(23b5a19 = local main with U83 merged). Read mizzen.md and topsail.md (how the sensor page and rig sheet are
built and tested), docs/sws/build_sensor.py, docs/sws/build_rig_sheet.py, sws/procedures/prototype_test_ai_guide.md.

Owner's statements of 17 Nov (register them as rulings of this unit, as U76/U77 did; no names or roles):
(a) The prototype rig has no calibration coil. Some of the prototype's channels are probably dead, and it had
    fewer channels than the full count from the start.
(b) For the new sensor board, a proposal to be discussed, not in the design: a small loop beside each sensor
    that can be powered to test and calibrate that sensor in place. Its current can be set to give the signal
    of one broken wire, or a level below the limit for loss of metal. Once the signal of a real fault has been
    recorded (on the test rope with defined faults), the loop can be tuned to reproduce that recorded value —
    the head can then replay a known fault on command. He wants this mentioned EARLY on the sensor page, at
    least as a note with a pointer.

1. **Sensor page.** Early — at the end of "What the sensor has to do" or directly after it, where a reader
   meets it before the findings — a short boxed note or paragraph in the page's easy-read voice, marked as a
   proposal: what the loop is; what it gives (each sensor checked alive and its gain calibrated in place, over
   the years and over temperature; a test signal the size of one broken wire; tuned to a recorded real fault
   so that fault can be replayed); what it does not show (the magnets and the rope's magnetisation — a weaker
   magnet makes a real fault smaller and the loop does not see that; so a reference on the magnet side and a
   test rope are still needed). Pointers: to the page's own calibration section, where "All three models
   propose a test coil…" already stands (make the two agree and not repeat each other), to the placement
   line about a printed conductor under each sensor, and to the first round's synthesis. For the loss-of-metal
   level: use only what the record says about that limit (find it: spec, register, EN 12927 by clause number
   only); if the record gives no figure, write the sentence without a number. Do not state a loop current, turn
   count or field per ampere unless you compute it and mark it as your own estimate with the formula in a
   linked note — it is not needed for this note; leave it out if in doubt. In "What is open": one line —
   whether an in-place check goes into the design, and which kind (loop per sensor, a reference rope length).
   The page may grow by at most a third of a page; adjust its test bound only as far as needed and say so.
2. **Rig sheet.** The first small step "which part on which channel": make the no-coil path the main one,
   because no coil is at hand — read from the runs: live or dead from run 1 (a live channel changes level
   between head off the rope and on it; a dead one does not), position round the rope and radial / axial from
   the pass over a known fault (the nearest channels react most; a radial channel swings one way then the
   other, an axial one makes a single dip — the sensor page's own description, cite it). The coil stays only as
   "if one is at hand". In the channel table add a narrow column "live / dead / not fitted". The later
   "Calibration coil" step keeps its IF THE RIG ALLOWS mark. Page count must stay 5 A4. New print copy:
   C:/Users/stian/secretary/inbox/2026-11-17_rig_sheet_print_v2.pdf (leave the earlier files).
3. **AI helper guide:** the same two changes, in its own words: no coil on this rig; how to tell live, dead and
   not fitted; what to do with a dead channel (note it, carry on; say which angles round the rope are then
   blind).
4. Register rows for (a) and (b); TASKS.md unit line.

Reviews, fresh subagents, one pass each, a second only for a blocking item: a falsifier (every claim added,
against the record and against physics: does the note overstate what a loop proves?); a cold reader with no
background on the sensor-page note (what is proposed, is it in the design, what does it not show); a test
technician on the changed rig-sheet step (can they tell live / dead / not fitted with what is on the rig).
Prove: all nine `--check` (venv C:/Users/stian/Prosjekter-u41/max/.venv), pytest tests/test_sws_*.py except p52,
idscan `python -I C:/Users/stian/secretary/tools/idscan.py . 23b5a19..HEAD` = 0, scan_tree on added lines = 0
(commands as in "## U83" above; report.html known 2 = 2). No names, roles or dates in page prose. Never print
max-private/identifiers.yaml.
Commit on the branch. No merge, no push, no export. Hand back ≤ 10 lines: tip; the note as it reads; where it
sits; the rig-sheet step as it reads; page counts; reviewers' verdicts; checks; what is not verified. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U86 — export increment for U83 + U85, then the Pages snapshot, every link proven (Kai, 17 Nov)

Same job as "## U79" above (and "## U75"); read those, gybe.md and gasket.md first (the method; the link scripts
under C:/Users/stian/export-v3/tools/, use the newest). The owner has asked for the release so he can read on his
phone; Kai pushes after a final check; you do not push.
State: local main = 84af27a (U83: second sensor round under sws/hw-selection/rounds/2026-11-16-sensor/ with
synthesis and datasheet_check, the gap comparison step and channel identity on the rig sheet, a paragraph on the
sensor page; U85: the test-loop note on the sensor page, the rig sheet read from the runs, register rows); D:
same. GitHub fjordbit/max main = export clone tip = 0f7b145 (it exported local 5f415b6). publish/SWS = both Pages
remotes = 1a58533. Verify before you start; stop if they differ.
A. Export: max/ subtree increment 5f415b6..84af27a, first-parent, grafted on 0f7b145, fast-forward only. Scan tip
   and increment (scan_tree with the u05 venv; idscan): 0 on everything added — in particular the whole new round
   folder: both briefs, the files under sent/, the six answers with their front matter (model names are fine;
   check for user names, machine paths beyond "~", account or organisation ids, key fragments — report what the
   front matter carries and unlink or strip nothing yourself: if anything of that kind is there, STOP and
   report), synthesis.md, datasheet_check.md; the changed pages and their builders; the helper guide; the
   register rows; hover titles, alts. report.html re-rendered long line: show removed side = added side.
   Confirm no PDF, no standard text, nothing from secretary/ or max-private/ in the increment. All nine `--check`
   and the SWS test files (expect 181; skip test_sws_p52) with the u41 venv, in a copy of the export tip.
B. Snapshot in C:/Users/stian/publish/SWS on 1a58533: `sws/` and `docs/sws/` from the export tip. Eight menu
   pages with the eight-entry switch as before; rig_sheet.html is the ninth page, not on the menu, opened from
   the procedures page; its own links must work in the snapshot. The sensor page's new links (to the new
   round's synthesis and data-sheet check, to the first round's synthesis, the in-page anchors of the test-loop
   note, the calibration section and the printed-conductor line) must land: say where each lands on the Pages
   site and that the target exists in the tree that will be live.
C. Link proof on all nine pages: relative and own-repo links 0 broken against the trees that will be live;
   carry or unlink what is not carried and list it. External links: one HEAD per distinct NEW URL only; send
   nothing about the project.
D. Visible text of the changed pages (sensor, rig sheet) free of local paths, "l.NNN", snapshot notes, personal
   names, roles and dates in prose; the rig sheet prints to 5 A4 from the snapshot copy (headless Edge, count
   pages); the sensor page 4 A4. Scan 0 on the increment; `git status` only sws/ and docs/; rebuild index.zip
   (untracked). Commit "SWS snapshot from MAx <tip>: second sensor round, test loop note, rig sheet". No push.
E. Hand back ≤ 12 lines: both tips, link counts per page (broken 0), what you unlinked, new external statuses
   that are not 200/redirect, scans, tests, the page counts, what the answers' front matter carries, the three
   push commands. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No
   identifier values, no personal names; never print the contents of max-private/identifiers.yaml. Timebox
   1 hour; past it, stop and report. — Kai

## U87 — the model round on the test sheet into the repo; the top page linked from the rig sheet (Kai, 17 Nov)

Small, mostly added files. The owner wants to read it on his phone on GitHub in the morning. Timebox 45 minutes.
`git worktree add C:/Users/stian/Prosjekter-u87 -b u87-test-round 84af27a` from C:/Users/stian/Prosjekter-u05
(84af27a = local main). Read mizzen.md (how U83 put the sensor round in: folder shape, README, front matter kept,
the sent files) and how the rig sheet links to the AI helper guide (docs/sws/build_rig_sheet.py; shroud.md).

Source: C:/Users/stian/test_round_2026-11-17/ — step1_brief.md, step2_brief.md, step1_files/test_sheet.md,
step2_files/ (the three reviews as X/Y/Z as sent), rounds/2026-11-17-step1/answers/, rounds/2026-11-17-step2/answers/,
labels_private.txt (which label is which model), summary.md and rig_top_page.md (written by a builder from the
answers and checked by a fresh reader; notes ketch.md). Three models: Fable 5.2, Grok 4.7 high, GPT 5.6 Sol extra
high; two steps: independent review, then cross-check with names removed.

1. New folder `sws/procedures/rounds/2026-11-17-test-sheet/` in U83's shape: README.md (what was run, on which
   version of the sheet — the text sent was the sheet at local 84af27a — how to read the folder, that it is the
   models' opinion and nothing in it selects a sensor or changes the sheet), both briefs, sent/ (step 1 and step 2
   files as sent, incl. the label key in the README, not the private file), answers/ (six, front matter kept as
   U83 did — check it carries no user name, expanded machine path, account or organisation id or key fragment;
   if it does, STOP and report), summary.md, rig_top_page.md. Copy summary.md and rig_top_page.md as they are;
   fix only what is wrong against the answers or the sheet, and list every change you make to them. The top page
   speaks of "the head's own channels cannot give this [field in mT]" etc. — leave the content; do not add.
2. One link from the rig sheet, on its first page near "On one page": a single line in the sheet's voice — a
   one-page top sheet from a cross-checked review by three language models, a proposal, with the link to
   rig_top_page.md — and one link from the procedures page's prototype stage beside the existing rig-sheet link.
   Links built the way the AI-guide link is built (so they land in the repo's file view from the Pages site).
   The rig sheet stays 5 A4; no other change to any page. In the rig sheet's block or the round README, no claim
   that the sheet has been changed to follow the round — it has not.
3. Register: one row for the round (what, where, opinion not data). TASKS.md unit line.
4. One fresh subagent as falsifier: summary.md and rig_top_page.md against the six answers and the sheet (run
   numbers and names as on the sheet at this commit; counts "3 of 3 / 2 of 3"; nothing that needs a coil or a
   cut wire presented as a step) — it gets the files, not your conclusions. Fix; one pass, a second only for a
   blocking item.
Prove: all nine `--check` (venv C:/Users/stian/Prosjekter-u41/max/.venv), pytest tests/test_sws_*.py except p52,
idscan `python -I C:/Users/stian/secretary/tools/idscan.py . 84af27a..HEAD` = 0, scan_tree on the new folder and on
added lines = 0 (commands as in "## U83" above; report.html known 2 = 2). No personal names, roles or dates in page
prose. Never print max-private/identifiers.yaml.
Commit on the branch. No merge, no push, no export. Hand back ≤ 8 lines: tip; folder contents; the two links as
they read and where they land; changes made to the two copied files; the falsifier's verdict; checks; what the
front matter carries; what is not verified. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in
that folder). Sign with your name. — Kai

## U88 — export increment for U87, then the Pages snapshot, every link proven (Kai, 17 Nov)

Same job as "## U86" above; read it, "## U79", and futtock.md first (the method, the scripts under
C:/Users/stian/export-v3/tools/). The owner has given the go; Kai pushes after a final check; you do not push.
State: local main = 1cc9661 (U87: the model round on the test sheet under
sws/procedures/rounds/2026-11-17-test-sheet/ — 21 files incl. summary.md and rig_top_page.md; one link line on the
rig sheet's first page and one on the procedures page's prototype stage, both to rig_top_page.md; a register row);
D: same. GitHub fjordbit/max main = export clone tip = 1680bc1 (it exported local 84af27a). publish/SWS = both
Pages remotes = 367549c. Verify before you start; stop if they differ.
A. Export: max/ subtree increment 84af27a..1cc9661, first-parent, grafted on 1680bc1, fast-forward only. Scan tip
   and increment (scan_tree with the u05 venv; idscan): 0 on everything added — the whole new round folder (both
   briefs, sent/, the six answers with front matter: report what it carries; a user name, an expanded machine
   path, an account or organisation id or a key fragment = STOP and report), the two changed pages and their
   builders, the register row. report.html re-rendered long line: removed side = added side. No PDF, no standard
   text, nothing from secretary/ or max-private/. All nine `--check` and the SWS tests (expect 181; skip
   test_sws_p52) with the u41 venv, in a copy of the export tip.
B. Snapshot in C:/Users/stian/publish/SWS on 367549c: `sws/` and `docs/sws/` from the export tip. Eight menu pages
   with the eight-entry switch; rig_sheet.html the ninth, not on the menu. The two new links to rig_top_page.md:
   say where each lands (Pages site → the repo's file view) and that the target exists in the tree that will be
   live on that remote.
C. Link proof on all nine pages: relative and own-repo links 0 broken against the trees that will be live; carry
   or unlink what is not carried and list it. External links: one HEAD per distinct NEW URL only; send nothing
   about the project.
D. Visible text of the two changed pages free of local paths, "l.NNN", snapshot notes, personal names, roles and
   dates in prose; the rig sheet prints to 5 A4 from the snapshot copy (headless Edge). `git status` only sws/ and
   docs/; rebuild index.zip (untracked). Commit "SWS snapshot from MAx <tip>: model round on the test sheet, top
   page". No push.
E. Hand back ≤ 10 lines: both tips, link counts per page (broken 0), what you unlinked, new external statuses not
   200/redirect, scans, tests, page count, what the front matter carries, the three push commands. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
   names; never print max-private/identifiers.yaml. Timebox 1 hour; past it, stop and report. — Kai

## U89 — the open question "do the halves come off the rope by themselves": a note with easy access from the start, and the two model rounds into the repo (Kai, 17 Nov evening)

The owner has asked for this tonight and reads it tomorrow at the rig. Mostly added files. Timebox 75 minutes; past it, stop and report.
`git worktree add C:/Users/stian/Prosjekter-u89 -b u89-halves-note 1cc9661` from C:/Users/stian/Prosjekter-u05
(1cc9661 = local main; verify, stop if it differs). Read boom.md and mizzen.md (how U87 / U83 put a round in: folder
shape, README, front matter kept, sent files, the link built so it lands in the repo's file view from Pages) and
spanker.md (how U85 added a boxed note to a page and moved the word bounds).

Background, plainly. The head is a clamshell of two halves around the rope. The main document says in two places
that the halves "snap together" / "attract when closed" (spec rev130 l.218, l.506; both on the published full
report). The owner's picture, from the mechanical side: the two halves have the same pole at the same end, push
each other apart, and are forced together by the closure; he was told the head would split if released. The 3D
model (sws/3d/verification.md l.399-405, 547-599; sws/3d/p52/design.md l.240-258) has both: per half, closed, rope
centred, 52 mm head: about 370 N push across the split, about 1 030 N pull of each half onto the rope, net
550-700 N holding the head shut; the empty head is not calculated and "may reverse"; the force as the head opens
is not calculated. Two model rounds were run today:
- Release round, C:/Users/stian/release_round_2026-11-17/ (three models, two steps; step 1 was sent with the
  simpler wording "the halves pull towards each other" and the withdrawn 0.4-0.8 kN/mm; step 2 carried the
  correction): step1_brief.md, step2_brief.md, step2_files/ (designs X/Y/Z as sent + brief), rounds/.../answers/
  (six), summary.md (short, checked once, fixes not re-checked), summary_long.md, labels_private.txt.
- Force round, C:/Users/stian/force_round_2026-11-17/ (Grok 4.7 high and GPT 5.6 Sol extra high only, clean, two
  steps, hand estimates — the tool does not let the models run code): step1_brief.md, step2_brief.md,
  step2_files/, rounds/.../answers/ (four), labels_private.txt (X = Sol, Y = Grok). No summary exists yet.
What the force round ends on (verify against the two step 2 answers, do not take it from me): empty head repels,
about 1 kN at closing (2 of 2); on a solid steel bar the closed head stays shut, about 500 N net (2 of 2; Sol's
range runs from 1.10 kN closing to 0.20 kN opening); NOT safe to carry to a real wire rope — steel fill 0.5-0.7
(from memory) can bring the pull down to 250-400 N while the push stays, net near zero or opening (2 of 2); other
holes: half-rings magnetised parallel instead of truly radial (a real pole on the cut, push 0.5-1.5 kN), a
low-coercivity grade knocked down, the 1 030 / 370 split is bookkeeping and only the net is physical, a possible
pi/2 factor in the 1 030 N; "N face to face against N" (about 800-850 N at 1 mm) is about equal to magnet on steel
(about 700-850 N) at 1 mm and the split is the smaller side-by-side case (about 250-350 N).

Do:
1. Two round folders under sws/housing/rounds/ in U87's shape: `2026-11-17-release/` and `2026-11-17-halves-force/`
   (README: what was run, which models, that step 1 of the release round was written before the correction, that
   it is the models' opinion from hand estimates and nothing is selected or decided; both briefs; sent/; answers/
   with front matter kept — check it carries no user name, expanded machine path, account or organisation id or
   key fragment; if it does, STOP and report; summary). Copy the release summary.md and summary_long.md as they
   are; fix only what is wrong against the answers; list every change. Put ONE line on top of the release
   summary: its first point rests on forces for a solid rope that the force round could not confirm for a real
   wire rope — link to the force summary.
2. Write `summary.md` for the force round (easy read, short sentences, at most about 1 A4, for a controls
   engineer on a phone): in five lines; the three reference cases as a small table; what 2 of 2 agree on; where
   they differ; the ways the 3D model can be wrong, with size and whether it flips the sign; the ways the
   hands-on picture is right and where it does not apply; the test that settles it (spring scale: real rope, solid
   bar, empty) with what each outcome means; what the round cannot settle; that these are hand estimates. Every
   figure exact and attributed; nothing of your own engineering.
3. The note, in the easy-read voice, as a boxed note with its own anchor on the page where the head's halves,
   closing or mounting release are described (find it; hardware or housing page — say which and why): "Do the
   halves come off the rope by themselves? Not known." What pushes (same pole side by side at the split), what
   pulls (each half onto the rope), the 3D figures with their limits (solid rope in the model — check in
   sws/3d what "homogeneous rope" means there, whether the metallic fill is in it, and say what you find; closed
   head only; empty head not calculated), what the two models add (real rope is the hole), that the two lines in
   the main document ("snap together", "attract when closed") are too simple and are to be corrected, what
   settles it (the old head opened on the rope this week; a pull test), and what it means for the mounting
   release: do not count on the head splitting by itself and do not count on it holding — the release has to
   push the halves off and hold them clear (the models' proposal, not decided). Links to both summaries. No
   "selected"/"decided". Do NOT edit the spec text itself in this unit; the note names the two lines.
4. Easy access from the start: one line with a link to the note near the top of the start page (index) and of
   the easy-read page, and beside the mount-release line on the procedures page. One line each, no other change.
5. The published top sheet `sws/procedures/rounds/2026-11-17-test-sheet/rig_top_page.md`: add item 8 under (b)
   exactly as in C:/Users/stian/secretary/inbox/2026-11-17_rig_top_page.md (it is marked as added after the
   round, not from the models); the round README there gets one line saying so. The rig sheet stays 5 A4.
6. Register: rows for the two rounds (opinion, not data) and one row for the open question; correct nothing else
   in the register (the old "rope-centring side force 0.4-0.8 kN/mm" row: add nothing, list it in your hand-back
   as owed). TASKS.md unit line.
7. One fresh subagent as falsifier (give it the files, not your conclusions): the force summary and the note
   against the four force answers, the six release answers and the 3D files — counts, figures, signs, nothing
   stated as decided, nothing firmer than the sources ("stays shut" only for the solid bar), cold-reader test of
   the note. Fix; one pass, a second only for a blocking item.
Prove: all nine `--check` (venv C:/Users/stian/Prosjekter-u41/max/.venv), pytest tests/test_sws_*.py except p52
(say the count), idscan `python -I C:/Users/stian/secretary/tools/idscan.py . 1cc9661..HEAD` = 0, scan_tree on the
two new folders and on added lines = 0 (commands as in "## U83" above; report.html known 2 = 2). No personal names,
roles or dates in page prose. Never print max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back ≤ 10 lines: tip; the page and anchor of the note
and the three links as they read; folder contents; changes to copied files; what "homogeneous rope" means in the
3D model; falsifier verdict; checks; front matter; what is not verified; what is owed. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U90 — export increment for U89, then the Pages snapshot, every link proven (Kai, 17 Nov night)

Same job as "## U88" above; read it, "## U86", "## U79", and yardarm.md and futtock.md first (the method, the scripts
under C:/Users/stian/export-v3/tools/). The owner has given the go; Kai pushes after a final check; you do not push.
State: local main = 44a5b0e (U89: a boxed note `#ho-halves` on the housing page — "Do the halves come off the rope
by themselves? Not known."; one link line near the top of index.html and of easy.html and one beside the
mount-release item on procedures.html; two new round folders sws/housing/rounds/2026-11-17-release/ (19 files) and
sws/housing/rounds/2026-11-17-halves-force/ (15 files); item 8 on
sws/procedures/rounds/2026-11-17-test-sheet/rig_top_page.md and a line in that README; register rows; TASKS line);
D: same. GitHub fjordbit/max main = export clone tip = e6e2c14 (it exported local 1cc9661). publish/SWS = both
Pages remotes = 7054acf. Verify before you start; stop if they differ.
A. Export: max/ subtree increment 1cc9661..44a5b0e, first-parent, grafted on e6e2c14, fast-forward only. Scan tip
   and increment (scan_tree with the u05 venv; idscan): 0 on everything added — both new round folders in full
   (briefs, sent/, the ten answers with front matter, models.yaml and round.json if carried: report what they
   carry; a user name, an expanded machine path, an account or organisation id or a key fragment = STOP and
   report), the changed pages and their builders, the register rows. report.html re-rendered long line: removed
   side = added side. No PDF, no standard text, nothing from secretary/ or max-private/. All nine `--check` and
   the SWS tests (expect 181; skip test_sws_p52) with the u41 venv, in a copy of the export tip.
B. Snapshot in C:/Users/stian/publish/SWS on 7054acf: `sws/` and `docs/sws/` from the export tip. Eight menu pages
   with the eight-entry switch; rig_sheet.html the ninth, not on the menu. The new links: from index, easy and
   procedures to housing.html#ho-halves (the anchor must exist in the snapshot page); from the note to the two
   round summaries, to rig_top_page.md and to the 3D files and the specification it cites — say where each lands
   (Pages site → the repo's file view) and that the target exists in the tree that will be live on that remote.
C. Link proof on all nine pages: relative and own-repo links 0 broken against the trees that will be live; carry
   or unlink what is not carried and list it. External links: one HEAD per distinct NEW URL only; send nothing
   about the project.
D. Visible text of the changed pages (housing, index, easy, procedures) free of local paths, "l.NNN", snapshot
   notes, personal names, roles and dates in prose; the rig sheet still prints to 5 A4 from the snapshot copy
   (headless Edge). `git status` only sws/ and docs/; rebuild index.zip (untracked). Commit "SWS snapshot from
   MAx <tip>: open question on the halves, release and force rounds". No push.
E. Hand back ≤ 10 lines: both tips, link counts per page (broken 0), what you unlinked, new external statuses not
   200/redirect, scans, tests, page count, what the front matter carries, the three push commands. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
   names; never print max-private/identifiers.yaml. Timebox 1 hour; past it, stop and report. — Kai

## U91 — the board arrangement: spokes marked "not confirmed", the thin board as the working design on record, the board round into the repo (Kai, 18 Nov)

The owner found today that the main document has carried a spoke-board sensor layout as "chosen layout" since its
first issue, without the choice ever having been put to him. His instruction: make it the first point, rerun, "then
update accordingly all". This unit records it and corrects the documents so no reader takes the spokes as settled.
It does NOT redesign the dependent pages; it lists them. Timebox 90 minutes; past it, stop and report.
`git worktree add C:/Users/stian/Prosjekter-u91 -b u91-board-arrangement 44a5b0e` from C:/Users/stian/Prosjekter-u05
(44a5b0e = local main; verify, stop if it differs). Read trysail.md (U89: how a boxed note with an anchor and links
from the start pages was added, the round folders, word bounds) and boom.md.

Facts on record (owner statements of 18 Nov 2026; in the repo they go in the register and the round README with
the status letter the register uses for owner statements, never as names, roles or dates in page prose):
- The working prototype's sensor board is two halves of one thin plate across the rope (cross-section plane), not
  spokes. The original idea was one thin board with the sensors mounted in different planes.
- On it the in-plane part (TMR2185) is the radial channel and the through-the-package part (TMR2584) the axial
  channel. This closes "which part is on which channel is not on file" as a statement; a photo of the markings is
  still wanted as the record.
- The yoke cut-out on the prototype was made to bring the standing field at the sensor down (more usable range,
  less noise), centred on the board with an equal cut on each side, and was tested in earlier simulations; all
  test data so far is on the 40 mm rope. (The geometry study, sws/3d/geometry_study.md section 2, judged a 20 mm
  cut-out on fault signal only and found no gain at equal induction; whether it was judged on the standing field
  at the sensor, and on the right shape — a smaller notch on the outside of the yoke — is open.)
- Search order for the sensor work: one board and magnetoresistive (TMR) parts first; Hall parts only where no TMR
  part meets the need, and then with the argument and a plain background.
What the record shows: "8-spoke / 16-position sensing array" is in the specification's revision history from the
first issue (2026-10-07); spec rev130 section 6 has a three-row table (ring or half-ring board: "Gives radial
only; axial would need an out-of-plane sensor or a daughter board"; flex strip; spoke PCB: "chosen layout") and the
paragraph "So each half carries eight spoke PCBs…". "Gives radial only" holds only for parts that all sense in the
board plane; with a part that senses through the board (the prototype's Z-axis part, or a Hall part lying flat) the
thin board gives both channels.

The round: C:/Users/stian/board_round_2026-11-18/ — step1_brief.md, step2_brief.md (with the block "A fact learned
after step 1"), step2_files/, rounds/2026-11-18-step1|step2/answers/ (six), labels_private.txt (X = Grok,
Y = Fable, Z = Sol), summary.md (written by a builder, checked once by a fresh reader, fixes applied and not
re-checked). In short (verify, do not take from me): arrangement 1 (two half-ring boards) 3 of 3; arrangement 2
(spokes) puts the calculated 31–107 mT in the film plane across the radial magnetoresistive part, 3 of 3; axial
part type Z-axis magnetoresistive 2 of 3, flat Hall 1 of 3; measure the real field at the elements first, 3 of 3;
all fields are calculated, not measured.

Do:
1. Round folder `sws/hw-selection/rounds/2026-11-18-board/` in U89's shape (README: what was run, the fact added
   before step 2, that it is opinion and nothing is selected; both briefs; sent/; six answers with front matter —
   check for user name, expanded machine path, account or organisation id, key fragment: STOP and report if any;
   summary.md as it is, fixing only what is wrong against the answers and listing every change).
2. A boxed note with its own anchor, easy-read voice, on the sensor page near where the board and the placements
   are described (say where and why): "Which board carries the sensors? Not settled." — what the main document
   has (spokes, written in as chosen from the first issue); what the working prototype has (two halves of one thin
   plate, in-plane part radial, through-the-package part axial); why "gives radial only" is too narrow; what the
   three models ended on and their one physical reason against spokes, with their warning on the radial part and
   that the fields are calculated; that the spoke layout is not confirmed and nothing further is to be built on it
   until the board is settled; what settles it (the field at the sensing elements measured on the prototype; a
   photo of the plate); the yoke cut-out as a linked open point (it decides whether a TMR part fits the axial
   channel); the search order. Links to the round summary. No "selected"/"decided".
3. One line with a link to that note near the top of index.html and easy.html (beside the U89 line), and where
   the hardware page and the housing page first lean on spokes (one short "(board arrangement not settled)" link
   each — find the first mention on each page; no other change to those pages).
4. The placement note sws/hw-selection/sws_sensor_placement.md and the candidates note: at the top, a short
   block: the working prototype is placement F's board (half-ring across the rope) with an in-plane and a
   Z-axis TMR part; placement A (spokes) is the specification's layout and is not confirmed; the part-to-channel
   statement. Do not rewrite the notes.
5. The specification: do NOT issue a new revision. Add a dated redline entry in the repo's redline/delta form
   (see sws/spec/REDLINE_2026-11-07.md and sws/deltas/ for the form) proposing: the table row corrected ("radial
   only with parts that all sense in the board plane; both channels with a part that senses through the board —
   the prototype's arrangement"), "chosen layout" on the spoke row replaced by "written in at the first issue; not
   confirmed", and the paragraph "So each half carries eight spoke PCBs…" marked as depending on that. Also list
   the two "halves attract" lines from U89 in the same redline as still owed.
6. A dependency list as a file in the round folder (or where the repo keeps such lists): every page, note,
   figure, script and register row that assumes spokes (spoke-to-spoke room, tabs, backplane, spoke carrier,
   placement radii, the housing round's eight sensor boards per half, the rig sheet and helper guide's "which part
   on which channel"), each with one line on what would change with the thin board and whether it is magnetics
   (unaffected) or layout (affected). This is the map for the later rewrite; change none of them.
7. Rig sheet and helper guide: where they say the part-to-channel map is not on file, add the statement as "stated,
   to be confirmed by a photo of the markings" and one line: the through-the-package part is specified within
   ±20 mT and saturates near ±30 mT, the calculated standing field along the rope is larger, so axial channels flat
   at a limit with radial channels moving points to range, not dead channels. The rig sheet stays 5 A4. Do NOT
   change rig_top_page.md.
8. Register rows: the owner statements above (each its own row), the round (opinion), the open point on the board
   and on the cut-out. TASKS.md unit line.
9. One fresh subagent as falsifier (files, not your conclusions): the note, the redline and the dependency list
   against the six answers, the specification and the owner statements as written in this brief — nothing firmer
   than the sources, nothing presented as decided, no swapped sensing direction, cold-reader test of the note.
   Fix; one pass, a second only for a blocking item.
Prove: all nine `--check` (venv C:/Users/stian/Prosjekter-u41/max/.venv), pytest tests/test_sws_*.py except p52,
idscan `python -I C:/Users/stian/secretary/tools/idscan.py . 44a5b0e..HEAD` = 0, scan_tree on the new folder and on
added lines = 0 (commands as in "## U83"; report.html known 2 = 2). No personal names, roles or dates in page prose.
Never print max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back ≤ 12 lines: tip; the note's page and anchor and the
link lines as they read; the redline file; the dependency list (count by kind, the five heaviest items); changes
to the copied summary; falsifier verdict; checks; front matter; not verified; owed. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U92 — a long loss of metal through the head: the first LMA calculation, and the demo video in two parts (Kai, 18 Nov)

The owner found that the documents and the demo video call a short fault "LMA". LD (LF) = a short local fault, a
sudden change. LMA = loss of metallic cross-section over a length, read against a reference; it should look like a
step, a level over the length of the loss, and a step back. No long loss has been calculated. This unit calculates
it and remakes the video. U93 runs in parallel and owns all pages and wording; you own `sws/3d/demo/`, new result
files, one new results note and one new video file. Timebox 150 minutes; past it, stop and report what is done.
`git worktree add C:/Users/stian/Prosjekter-u92 -b u92-lma-sweep-video 8f1822e` from C:/Users/stian/Prosjekter-u05
(8f1822e = tip of the unmerged branch u91-board-arrangement; verify, stop if it differs). Read crosstree.md and
boom.md in C:/Users/stian/agent-notes/, and `sws/3d/demo/README.md`, `defect_sweep.py`, `make_video.py`.

Do:
1. `defect_sweep.py`: make fault length, depth, loss and the sweep range command-line parameters. Defaults unchanged;
   prove the default run still gives the old numbers (compare with the existing sweep file if present, else state
   the peak values against the README's −14.8 mT).
2. Cases on the video's case (H40 head, 40 mm rope, hard wire, 25 °C):
   (a) the present groove: 4 mm long, 30 % loss in the outer 2 mm (reference);
   (b) the same loss over 300 mm (about 5.7 % of the metal area by the README; verify);
   (c) a loss of 10 % of the metal area over 300 mm, once as outer-layer loss (wear) and once as uniform loss over
       the whole section (corrosion) — 10 % is the discard level in the crane rope standard's informative annex
       and in the owner's company rule;
   (d) if the box allows it without a new mesh study, one fault of 30 rope diameters (1 200 mm); if not, say why.
   Sweep far enough that the fault fully enters and fully leaves the head.
3. Read-outs at every position, each as absolute value and as change from the intact rope:
   the two sensor channels as now (ΔB_z, ΔB_r at the sensor); and candidate LMA read-outs — flux through the rope
   at the mid-plane, flux through the yoke at the mid-plane, B_z in the air at the sensor radius under a pole and
   at the mid-plane, and the axial-channel signal integrated along the travel. Nothing is selected; these are
   candidates. For each: the level while the fault spans the head, in per cent of the standing value per per cent
   of lost area; how flat the level is; what the two ends look like.
4. Comparators for drift (intact rope, cheap; drop first if the timebox is short, and say so): the same read-outs
   with the magnet remanence 1 % lower, and with the rope diameter 1 % larger. State each as "equals an apparent
   LMA of x %". This is the first line of a drift budget, not the budget.
5. A results note `sws/3d/lma_sweep.md`, easy-read first (short sentences, a table, one figure of the traces for
   (a), (b), (c)), dense detail below. It must say plainly: which read-outs follow a long loss and which only
   show its two ends; that the model is 2D axisymmetric with a homogenised rope, exact only for a ring fault;
   that materials are register placeholders; that which sensor reads LMA is open. Results as JSON in the usual
   results folder. No "selected", "decided", "chosen".
6. Video in two parts, written to `docs/sws/sws_demo_v2_720p.mp4` (do NOT replace, remove or relink the present
   `sws_demo_720p.mp4`; change no HTML page — U93 owns the pages):
   part 1 as now, caption corrected to a short local fault (no "LMA" on it; keep the loss in per cent as the size
   of the fault); part 2 the long loss (b or c, say which and why) travelling through, with the trace panel showing
   the best-following candidate read-out beside the two sensor channels, so the step, the level and the step back
   — or their absence on the sensor channels — are visible. Bottom note: computed, 2D ring fault, placeholder
   materials, the LMA sensor is not settled. Keep the look of the present video. Save three still frames as PNG
   beside the results note for the check. Update `demo/README.md` (what is on screen, source, status).
7. One fresh subagent as falsifier (files, not your conclusions): the note and the video captions against the
   result files — nothing firmer than the numbers, no fault called LMA that is a local fault, units and signs,
   cold-reader test of the easy-read part. Fix; one pass, a second only for a blocking item.
Prove: all nine `--check` (venv C:/Users/stian/Prosjekter-u41/max/.venv; if pyvista / imageio-ffmpeg are missing
there, look in the other Prosjekter-*/max/.venv folders before installing anything, and report what you used),
pytest tests/test_sws_*.py except p52, idscan `python -I C:/Users/stian/secretary/tools/idscan.py . 8f1822e..HEAD`
= 0, scan_tree on added files = 0 (commands as in "## U83"). No personal names, roles or dates in prose. Never
print max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back at most 12 lines: tip; the table of read-outs (level
per per cent of loss, flat or ends only); the drift comparators; the video path, length and which case part 2
shows; the still frames' paths; falsifier verdict; checks; not verified; owed. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U93 — LD and LMA are two measurements: wording corrected, one note, the discard rules (Kai, 18 Nov)

Same finding as U92. This unit corrects the words and records what LMA needs. It calculates nothing; U92 does the
calculation in parallel and owns `sws/3d/demo/`, `sws/3d/lma_sweep.md` and the new video file — do not touch
those. Timebox 120 minutes; past it, stop and report.
`git worktree add C:/Users/stian/Prosjekter-u93 -b u93-ld-lma-wording 8f1822e` from C:/Users/stian/Prosjekter-u05
(8f1822e = tip of the unmerged branch u91-board-arrangement; verify, stop if it differs). Read crosstree.md (U91:
boxed note with anchor, link lines, redline file, register rows, word bounds) and boom.md.

Facts on record (owner statements of 18 Nov 2026; in the repo they go in the register with the status letter used
for owner statements, never as names, roles or dates in page prose):
- LD (local fault, LF in other literature) and LMA are two different measurements. LD: a short discontinuity, only
  the sudden change matters. LMA: loss of metallic cross-section over a length, larger than what LD detects, read
  against a reference run of the rope when new.
- The first run does not catch a rope that is already damaged from the supplier; so an absolute reference
  (calibration of the excitation) may be important for LMA. For LD it matters less.
- For LMA, drift and background noise are extremely important.
- Company rule: discard at any LMA of 10 %. Both rules are to be written: the standard's and the company's.
- Rope data (certificate) is promised but not held; until then work with a low, middle and high case, marked as
  assumed.
- Spokes are not ruled out as such; the objection is that on spokes the two sensors of a position do not sit at
  the same place and so do not read the same spot, which is bad for local faults. (Add this sentence to the U91
  note `sensor.html#s-board` where it fits; change nothing else there.)
From ISO 4309:2017 (not in the repo, copyright: clause numbers and your own words only, no quotation, the PDF is
never copied): 3.13 the first test is the base trace and the datum for later comparison; 3.15 LMA is a percentage
of the nominal metallic area of the new rope; 5.6 a base trace as early as possible, magnetic testing always
together with visual inspection, no instrument requirements (it points to EN 12927 and ASTM E1571); 6.3 the
tester needs the metallic area and the wire diameters; informative Annex C, all rope constructions: local faults
discard at 6 % lost area over 6 rope diameters or 10 % over 30; LMA discard at 10 % over 30 rope diameters. For
52 mm: 312 mm and 1 560 mm; for 40 mm: 240 mm and 1 200 mm. The head is about 180 mm long, so both limits are
sums along the rope longer than the head. Kai checked 3.13, 3.15, 5.6 and Annex C against the pages. Give it a
reference number in the repo's reference list in the form used for EN 12927.

Do:
1. Find every place where "LMA" labels the axial channel's reading of a short fault (known: `sws/3d/verification.md`,
   `sws/3d/p52/design.md`, the figure u32_faults_3d and its caption, the report and the sensor page; the demo
   README's "an LMA-type defect"; grep the whole of `sws/` and `docs/sws/` builders' sources, list all hits with a
   verdict each). Correct to what it is: the axial channel (B_z) reading of the same local fault; the lost area in
   per cent may stay as the size of the fault. If a figure's baked-in title is wrong and regenerating it is cheap,
   regenerate; else correct the caption and list the figure as owed. Leave `sws/3d/demo/` to U92 and list it.
2. A boxed note with its own anchor on the sensor page, easy-read voice: "LD and LMA are two measurements." — what
   each is; what has been calculated (local faults, both channels) and what has not (a long loss; in work, one
   line pointing to `sws/3d/lma_sweep.md` as "calculation in work", no link that would break the link check — say
   how you handled it); what LMA needs that LD does not (a reference: first run and nominal area; an absolute
   scale; a drift and noise budget; a sum over a rope length longer than the head; position along the rope); the
   two discard rules side by side in a small table (standard, company) with the lengths in mm for 40 and 52 mm;
   that the main document leaves the LMA sensor open (spec lines near 271 and 464 in rev130 — verify); that rope
   data is not held and three cases are used. No "selected", "decided", "chosen".
3. Where the demo video is shown on a page (index, easy, report, sensor — verify): one line under it: the fault
   in the video is a short local fault although its caption says LMA; a corrected two-part version is in work;
   link to the note.
4. Link lines near the top of index.html and easy.html beside the U89 and U91 lines: to the new note; and one to
   the rig sheet `rig_sheet.html` (the owner could not find it from the start page).
5. Append to `sws/spec/REDLINE_2026-11-18.md`: the proposed wording for the spec's LD / LMA lines (definitions, the
   open LMA sensor, the discard rules as standard and company rule), proposed and not applied, no new revision.
6. Register rows: each owner statement above its own row; the ISO 4309 reference; open points: the LMA sensor, the
   LMA reference and calibration, the drift budget, what "any" means in the company rule (any single cross-section
   or over a length — not stated; open). TASKS.md unit line.
7. One fresh subagent as falsifier (files, not your conclusions): every corrected place and the note against the
   facts as written in this brief — nothing firmer than the sources, LD and LMA not swapped anywhere, the two
   rules not blended, no quotation from the standard, cold-reader test of the note. Fix; one pass, a second only
   for a blocking item.
Prove: all nine `--check` (venv C:/Users/stian/Prosjekter-u41/max/.venv), pytest tests/test_sws_*.py except p52,
idscan `python -I C:/Users/stian/secretary/tools/idscan.py . 8f1822e..HEAD` = 0, scan_tree on added lines = 0
(commands as in "## U83"; report.html known 2 = 2). The sensor page's printed length: report it (it is 5 A4 after
U91; if the note takes it past 6, move detail behind a link). No personal names, roles or dates in page prose.
Never print max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back at most 12 lines: tip; the list of corrected places
(count, the five most visible); the note's anchor and the link lines as they read; figures owed; redline lines;
register rows; falsifier verdict; checks; not verified; owed. Notes in C:/Users/stian/agent-notes/<nautical
name>.md (a name not in that folder). Sign with your name. — Kai

## U94 — export increment for U91 + U93 + U92, then the Pages snapshot, every link proven (Kai, 18 Nov)

Same job as "## U90" above; read it, "## U88", "## U86", "## U79", and the notes of the builder that ran U90 plus
yardarm.md and futtock.md first (the method, the scripts under C:/Users/stian/export-v3/tools/). The owner has given
the go; Kai pushes after a final check; you do not push.
State: local main = 062b8bd; D: same. It holds, on 44a5b0e: U91 (boxed note `sensor.html#s-board`, link lines on
index, easy, hardware, housing; `sws/spec/REDLINE_2026-11-18.md`; round folder
`sws/hw-selection/rounds/2026-11-18-board/` with `spoke_dependencies.md`; rig sheet and helper guide lines; register
rows), U93 (21 wording corrections in 14 files; boxed note `sensor.html#s-ldlma`; link lines on index and easy to
that note and to `rig_sheet.html`; a line under the video on report and easy; redline rows; register rows; one
regenerated figure), U92 (`sws/3d/lma_sweep.md`, three still PNGs, `sws/3d/results/lma_sweep_*.json`, changed
`sws/3d/demo/` scripts and README, new video `docs/sws/sws_demo_v2_720p.mp4`) and one commit by Kai (pages point to
the v2 video; the first video `docs/sws/sws_demo_720p.mp4` is REMOVED; one sentence in the s-ldlma note; report
rebuilt). GitHub fjordbit/max main = export clone tip = 7f2b3f7 (it exported local 44a5b0e). publish/SWS = both
Pages remotes = 36bc5cb. Verify before you start; stop if they differ.
A. Export: max/ subtree increment 44a5b0e..062b8bd, first-parent, grafted on 7f2b3f7, fast-forward only. Scan tip
   and increment (scan_tree with the u05 venv; idscan): 0 on everything added — the board round folder in full
   (briefs, sent/, six answers with front matter, models.yaml and round.json if carried: report what they carry; a
   user name, an expanded machine path, an account or organisation id or a key fragment = STOP and report), the
   changed pages and builders, the register rows, the lma_sweep JSON and note. report.html re-rendered long lines:
   removed side = added side. No PDF, no standard text (ISO 4309 and EN 12927 appear as clause numbers and own
   words only — grep for long verbatim-looking passages near "ISO 4309" and report), nothing from secretary/ or
   max-private/. The removed first video must be absent from the export tip and the v2 video present. All nine
   `--check` and the SWS tests (expect 181; skip test_sws_p52) with the u41 venv, in a copy of the export tip.
B. Snapshot in C:/Users/stian/publish/SWS on 36bc5cb: `sws/` and `docs/sws/` from the export tip. Eight menu pages
   with the eight-entry switch; rig_sheet.html the ninth, not on the menu. The first video removed from the
   snapshot too, the v2 video present and the two video tags (report, easy) pointing at it; file size of the v2
   video reported. New links: from index and easy to sensor.html#s-board, sensor.html#s-ldlma and rig_sheet.html;
   from hardware and housing to #s-board; from the notes to the round summary, the redline, the dependency list
   and whatever they cite — say where each lands (Pages site → the repo's file view) and that the target and the
   anchor exist in the tree that will be live on that remote.
C. Link proof on all nine pages: relative and own-repo links 0 broken against the trees that will be live; carry
   or unlink what is not carried and list it. External links: one HEAD per distinct NEW URL only; send nothing
   about the project.
D. Visible text of the changed pages (sensor, index, easy, hardware, housing, report's changed parts, rig sheet)
   free of local paths, "l.NNN", snapshot notes, personal names, roles and dates in prose; the rig sheet still
   prints to 5 A4 and the sensor page to 5 A4 from the snapshot copy (headless Edge). `git status` only sws/ and
   docs/; rebuild index.zip (untracked). Commit "SWS snapshot from MAx <tip>: board arrangement not settled, LD
   and LMA as two measurements, first long-loss calculation, two-part video". No push.
E. Hand back at most 10 lines: both tips, link counts per page (broken 0), what you unlinked, new external statuses
   not 200/redirect, scans, tests, page counts, what the front matter carries, the three push commands. Notes in
   C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). No identifier values, no personal
   names; never print max-private/identifiers.yaml. Timebox 1 hour; past it, stop and report. — Kai

## U95 — the axial sensor at different lift-offs: a sweep over radius (and a little along the rope) (Kai, 18 Nov)

The owner's question: in the video both sensors sit at the same lift-off. It is not given that the axial sensor
should sit at the same lift-off as the radial one. He wants to see what the axial sensor reads at different
lift-offs before any board is drawn. A second unit on the yoke cut-out follows this one; do not start it.
Timebox 120 minutes; past it, stop and report what is done.
`git worktree add C:/Users/stian/Prosjekter-u95 -b u95-axial-liftoff 062b8bd` from C:/Users/stian/Prosjekter-u05
(062b8bd = local main; verify, stop if it differs). Read dodger.md (U92: the sweep tool, the read-outs, the venv
with ngsolve and pyvista at C:/Users/stian/Prosjekter/max/.venv, the box limits) and `sws/3d/lma_sweep.md`,
`sws/3d/demo/defect_sweep.py`, and what the repo already has on stand-off (report section on signal against
radial sensor position; the single-wire figures 0.66 / 0.39 / 0.20 / 0.14 mT at 3 / 5 / 8 / 10 mm).

Facts: the working prototype's board is two halves of one thin plate across the rope at the mid-plane; the radial
part is an in-plane TMR part, the axial part a through-the-package TMR part specified to ±20 mT (saturating near
±30 mT, data-sheet values already in the repo's candidates note — verify there, no web lookups). The sensing
element can in principle sit anywhere on that plate between the guard and the yoke. Nothing is selected.

Do:
1. On the video's case (H40 head, 40 mm rope, hard wire, 25 °C), from the intact solution and the U92 sweeps
   (reuse the result files if they hold the field on a grid; re-solve only what is missing): for sensing-element
   lift-off from the rope surface in 1 mm steps from the nearest possible position out to the inner face of the
   yoke, at the mid-plane and at 2 and 5 mm off the mid-plane along the rope:
   (a) the standing field B_z and B_r (intact rope), and where |B_z| is inside ±20 mT and inside ±30 mT; say
       plainly whether B_z changes sign anywhere between rope and yoke and at which radius;
   (b) the short local fault (the 4 mm groove): peak ΔB_z and ΔB_r;
   (c) the long loss (U92 case c, both variants): the level and the end spikes on B_z;
   (d) the U92 drift comparators (magnets 1 % weaker, rope 1 % thicker) on B_z, as apparent LMA;
   (e) two ratios per lift-off: local-fault peak over standing |B_z|, and long-loss level per 1 % over the drift
       per 1 % magnet change.
   Mark which lift-offs are physically blocked (guard, magnet, yoke) from the geometry in the model.
2. The same for the 52 mm head and rope if the sweep tool takes that case without new development (state the case
   used); if not, the intact standing field only, from the existing 52 mm solutions, and say what is owed.
3. A results note `sws/3d/axial_liftoff.md`, easy-read first: one figure with the curves against lift-off (standing
   B_z with the ±20 and ±30 mT bands drawn; fault peak; long-loss level), one table, five plain sentences on what
   the curves show. Then the dense part. It must say: 2D axisymmetric, homogenised rope, ring faults — a ring fault
   falls off more slowly with distance than a single broken wire, so set the repo's single-wire stand-off figures
   beside the ring figures and do not read the ring's fall-off as a wire's; placeholder materials; calculated, not
   measured; the prototype measurement of the real field at the elements is what would settle it. No "selected",
   "decided", "chosen", "optimal". JSON in the usual results folder.
4. Change no HTML page and no existing note's conclusions. TASKS.md unit line; one register row for the result
   (model result, status as the register uses for calculations).
5. One fresh subagent as falsifier (files, not your conclusions): the note against the JSON — signs, units, radius
   against lift-off not mixed up, nothing firmer than the numbers, ring against wire stated, cold-reader test.
   Fix; one pass, a second only for a blocking item.
Prove: all nine `--check` (venv C:/Users/stian/Prosjekter-u41/max/.venv), pytest tests/test_sws_*.py except p52
(181), idscan `python -I C:/Users/stian/secretary/tools/idscan.py . 062b8bd..HEAD` = 0, scan_tree on added files
= 0 (commands as in "## U83"). No personal names, roles or dates in prose. Never print
max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back at most 12 lines: tip; the table (lift-off, standing
B_z, fault peak, long-loss level, drift) at five or six lift-offs; where B_z is inside ±20 mT; sign change yes or
no and where; the 52 mm result or what is owed; the figure path; falsifier verdict; checks; not verified; owed.
Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U96 — the yoke cut-out: a coarse sweep of width and depth, then finer if it changes anything (Kai, 18 Nov)

Owner statements on record (register, U91/U93 rows): the prototype's yoke has a cut-out, made to bring the standing
field at the sensor down (more usable range, less noise), centred on the sensor board with an equal cut on each side
along the rope, tested in earlier simulations. The geometry study (`sws/3d/geometry_study.md` section 2) judged a
20 mm cut-out on fault signal only. U95 (`sws/3d/axial_liftoff.md`, read it and rudder.md first) shows why it
matters: without a cut-out the standing B_z is about −42 mT at 3 mm lift-off and comes inside ±20 mT only from
13 mm, where the short-fault peak is a tenth of its value at 3 mm. The owner's instruction for this unit: start
with a width w and a depth d in steps of about 5 mm, see whether it changes anything, then go finer to find a best
cut-out "if there is one". A third unit will later mix lift-off and cut-out; do not start it.
Timebox 150 minutes; past it, stop and report what is done.
`git worktree add C:/Users/stian/Prosjekter-u96 -b u96-yoke-cutout 5f5bbc5` from C:/Users/stian/Prosjekter-u05
(5f5bbc5 = tip of the unmerged branch u95-axial-liftoff; verify, stop if it differs). Venv with the solver:
C:/Users/stian/Prosjekter/max/.venv. Reuse `sws/3d/demo/axial_liftoff.py` and the sweep tool; read how the
geometry study and `fem-2d/sws_yoke_window.py` drew their cut-out before you draw yours.

The exact size and side of the prototype's cut-out is NOT on file (Kai is asking the owner). So sweep families, and
say which family each earlier study used:
  I  a groove in the INNER face of the yoke (towards the rope), centred on the mid-plane: width w along the rope,
     depth d into the yoke;
  O  the same in the OUTER face;
  T  a cut through the whole yoke thickness (a window; in 2D axisymmetric this is a full ring gap — say plainly
     that a real window covers only part of the circumference and that 2D overstates it).
Do:
1. Coarse, on the H40 head with the 40 mm rope (hard wire, 25 °C): w = 5, 10, 15, 20, 30 mm; d = 5, 10, 15 mm as
   far as the yoke thickness allows (state the thickness), families I and O; family T at the same widths. Plus the
   no-cut-out reference, which must reproduce U95.
2. For every case, against lift-off 3–20 mm at the mid-plane: standing B_z and B_r; the lift-off from which |B_z|
   is inside ±20 mT and inside ±30 mT; the short ring fault's peak ΔB_z and ΔB_r; the long-loss level (10 %,
   one variant is enough for the coarse pass); the magnet −1 % comparator. And per case: the rope induction and the
   flux through the rope (does the cut-out starve the rope?), the highest B in the remaining yoke steel (does it
   saturate?). Do NOT re-tune the magnet to restore the induction in this pass; report the induction change beside
   every signal so nobody compares unequal cases unknowingly, and add one line per family on what "at equal
   induction" would do, if the earlier study's method lets you say it.
3. One merit table, stated as a comparison and not a choice: for each case, the short-fault peak ΔB_z and ΔB_r at
   the smallest lift-off where |B_z| ≤ 20 mT (and the same for ≤ 30 mT), beside the no-cut-out values. This answers
   "does it change anything".
4. If a family changes the answer by more than the mesh scatter (state the scatter): a finer pass around the best
   cases (steps of 1–2 mm in w and d), same read-outs. If nothing changes it, say so plainly and stop there.
5. The 52 mm head: the reference and the two or three most telling cases only, if time allows; else owed.
6. A results note `sws/3d/yoke_cutout.md`, easy-read first: one figure (standing B_z against lift-off for the
   reference and the telling cases, with the ±20 / ±30 mT bands), one small map (w against d, colour = lift-off
   where |B_z| reaches 20 mT, per family), the merit table, five plain sentences. Then the dense part. It must say:
   2D axisymmetric, homogenised rope, ring fault (a ring falls off more slowly with distance than a wire);
   placeholder materials; calculated, not measured; the prototype's real cut-out is not on file; what the earlier
   study concluded and on what criterion, without calling it wrong. No "selected", "decided", "chosen"; "best" only
   with the criterion named beside it. JSON in the usual results folder.
7. Change no HTML page. TASKS.md line; one register row for the result.
8. One fresh subagent as falsifier (files, not your conclusions): the note against the JSON — signs, units, inner
   against outer face not swapped, w against d not swapped, induction change stated beside each comparison,
   nothing firmer than the numbers, cold-reader test. Fix; one pass, a second only for a blocking item.
Prove: `--check` on all nine and pytest tests/test_sws_*.py except p52 (venv C:/Users/stian/Prosjekter-u41/max/.venv;
the report check and one report test are expected to fail only because report.html embeds the register — confirm
that is the only reason by a rebuild you do not commit), idscan
`python -I C:/Users/stian/secretary/tools/idscan.py . 5f5bbc5..HEAD` = 0, scan_tree on added files = 0. No personal
names, roles or dates in prose. Never print max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back at most 12 lines: tip; does a cut-out change anything,
per family, in one sentence each; the merit table's five most telling rows; the induction and yoke saturation
side effects; finer pass yes or no and its result; 52 mm; figure paths; falsifier verdict; checks; not verified;
owed. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U97 — why the yoke groove works, re-read by the owner's criterion, inner against outer, and a screen for other levers (Kai, 18 Nov)

Read scantling.md (U96) and rudder.md (U95), `sws/3d/yoke_cutout.md`, `sws/3d/axial_liftoff.md` first.
`git worktree add C:/Users/stian/Prosjekter-u97 -b u97-groove-physics e84b603` from C:/Users/stian/Prosjekter-u05
(e84b603 = tip of the unmerged u96-yoke-cutout; verify, stop if it differs). Solver venv
C:/Users/stian/Prosjekter/max/.venv. Timebox 150 minutes; past it, stop and report what is done.

Owner statements (18 Nov), to go in the register as owner statements:
 - The prototype's cut-out is a groove in the OUTER circumference of the yoke, ALL THE WAY ROUND, centred where the
   sensors are. So a 2D axisymmetric model is the right model for it; U96's caution that "a real window covers only
   part of the circumference" does not apply to family O (correct that sentence in the note; keep it for T only if
   a window is meant).
 - In the prototype's design work an INNER groove moved the sensing signal "the wrong way"; the outer one worked.
   U96 found inner and outer acting in the same direction. This disagreement is open. Do not explain it away.
 - The aim is NOT to bring the axial sensor close to the rope. The owner wants it as far from the rope as it can be
   while the signal is still good, and NOT at the same radius as the radial sensors (board layout). U96's merit
   criterion ("smallest lift-off inside ±20 mT") was Kai's and is the wrong question. Re-read by the owner's.

Kai's re-read of U96's JSON (check it, do not trust it): the groove depth sets the radius where the standing B_z is
zero — outer groove 3 mm deep: zero near 17 mm lift-off, inside ±20 mT from 9.5 to beyond 20 mm, short-fault peak
there about 0.9 mT; 4 mm: zero near 12 mm, peak 1.8 mT; 5 mm: zero near 8 mm, 2.9 mT; width 14–20 mm hardly matters.
No cut-out: zero only 0.5 mm from the yoke face. The steel over the groove is at 1.9–2.1 T. The long-loss level at
the zero point is several times the no-cut-out level.

Do:
1. THE PHYSICS, shown from the model's own fields, not asserted. Hypothesis to test (try to break it): along a steel
   surface the tangential H is continuous, so the axial field in the air beside the yoke equals mu0·H_z inside the
   yoke steel; a thick yoke is unsaturated (H small, air field near zero, zero crossing at the yoke face); thinned
   steel saturates (H large, direction of the yoke flux, opposite to the rope side), so a zero of B_z appears
   between rope and yoke and moves inward as the steel thins. Test: (a) for no cut-out and four groove depths, H_z
   in the yoke steel at the mid-plane against B_z/mu0 in the air just inside the yoke face — do they agree, to what
   per cent; the same at the rope surface; (b) the radial profile of H_z from rope axis to outside the yoke for
   those cases in one figure; (c) a hand calculation from the B–H curve and the flux through the yoke that predicts
   the zero-crossing radius, set beside the model's; (d) what the hypothesis predicts and the model does not show.
   Say plainly: this is shown in a calculation; a measurement of the field against radius on the prototype (a
   gaussmeter traverse) is what proves it physically, and give the three numbers such a traverse should find.
2. THE OWNER'S CRITERION. For no cut-out and families O and I (T only as a note): against groove depth in 0.5 mm
   steps (width fixed at two values), the zero-crossing lift-off, the ±20 mT interval, and across that interval the
   short-fault peak ΔB_z, ΔB_r, the long-loss level, the magnet −1 % comparator, and the ratio signal / |standing|.
   One figure: lift-off against depth, the ±20 mT band as a shaded region, signal as contours. One table. State
   what a board with the axial element at 10, 13 and 16 mm lift-off would need as groove, and what signal it gets,
   beside the no-cut-out value at the same lift-off (so the reader sees what the groove buys at EQUAL lift-off —
   this may be little; say so if so). How sensitive is the zero radius to groove depth tolerance (mm per 0.1 mm),
   to magnet strength ±3 % and to temperature (−20, +25, +45 °C if the tool takes it)? Both heads if time allows;
   else the 52 mm head owed.
3. INNER AGAINST OUTER. Look for any condition in which an inner groove moves the standing field or the fault signal
   the other way: element inside or near the groove mouth, off the mid-plane, B_r instead of B_z, narrow against
   wide, at equal steel left. Report where they differ and by how much, or that no such condition was found in the
   range tried (state the range). Do not conclude the owner's finding was wrong.
4. OTHER LEVERS, a coarse screen, one or two cases each, same read-outs as point 2, as a table "lever / what it
   does to the zero radius and the signal / side effect on rope induction": yoke thinner over its whole length;
   two grooves either side of the mid-plane; a tapered or rounded groove; a small steel ring or pair of rings near
   the element (a local shield or concentrator); magnet spacing along the rope; the element moved along the rope
   instead of radially. Mark each "changes it / does not / not tried". Nothing is recommended; no "optimal",
   "selected", "chosen"; "best" only with its criterion beside it.
5. Note `sws/3d/groove_physics.md`, easy-read first (five plain sentences, two figures, two tables), dense part
   after; JSON in the results folder. Correct the one sentence in `yoke_cutout.md` named above and add a line there
   that its merit table answers "how close" and that this note answers "how far out". Change no HTML page.
   TASKS.md line; register rows: the three owner statements (as owner statements, no name) and the result.
6. One fresh subagent as falsifier (files, not your conclusions): signs, units, H against B, inner against outer,
   depth against steel left, nothing firmer than the numbers, the open disagreement still stated as open,
   cold-reader test. Fix; a second pass only for a blocking item.
Limits to state: 2D axisymmetric, homogenised rope, ring faults (fall off more slowly than a wire), placeholder
materials — the result depends directly on the yoke steel's B–H curve near saturation, so say which curve and how
far the zero radius moves with a plausible other curve; magnet not re-sized; calculated, not measured.
Prove: `--check` on all nine and pytest tests/test_sws_*.py except p52 (venv C:/Users/stian/Prosjekter-u41/max/.venv;
report check and one report test fail only because report.html embeds the register — confirm by a rebuild you do
not commit), idscan `python -I C:/Users/stian/secretary/tools/idscan.py . e84b603..HEAD` = 0, scan_tree on added
files = 0. No personal names, roles or dates in prose. Never print max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back at most 14 lines: tip; does the H-continuity
explanation hold, with the per-cent agreement; predicted against modelled zero radius; the table for 10 / 13 / 16 mm;
what the groove buys at equal lift-off; tolerance sensitivities; inner against outer; the lever table; B–H
dependence; figure paths; falsifier verdict; checks; not verified; owed. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U98 — where in the 1.9–2.3 T window the rope should work, with the groove in place (Kai, 18 Nov)

Read stemson.md (U97), scantling.md (U96), `sws/3d/groove_physics.md`, `sws/3d/yoke_cutout.md`, `sws/3d/lma_sweep.md`
first. `git worktree add C:/Users/stian/Prosjekter-u98 -b u98-working-point ab4fe6b` from C:/Users/stian/Prosjekter-u05
(ab4fe6b = tip of the unmerged u97-groove-physics; verify, stop if it differs). Solver venv
C:/Users/stian/Prosjekter/max/.venv. Timebox 150 minutes; past it, stop and report what is done.

Owner's position (register it as an owner statement, no name): the rope is meant to work saturated inside
1.9–2.3 T; nothing should be designed close to either limit; if a value had to be named today it would be the
middle, 2.1 T, but the working point should come from simulation and knowledge, not from "the middle".
Facts from U96/U97: on the H40 head the rope is at 1.94 T at the mid-plane without a groove (peak 2.18 T along the
rope) and 1.88–1.92 T with the grooves that put the standing-field zero at 10–16 mm lift-off. The axial element is
for LMA: its merit is the long-loss LEVEL per 1 % lost metal, held flat along the loss, and how little drift is
mistaken for loss. The radial elements take the short faults.

Do:
1. Say first what the 1.9–2.3 T window is in the repo: where it is defined, on what grounds each limit rests (the
   knee of which curve; which quantity — induction in the wire steel or averaged over the rope section), and what
   the homogenised model's "rope induction" corresponds to. If the limits rest on a placeholder curve, say so.
2. Raise the rope's working point in steps, by the means the model has (magnet remanence scale first, as a neutral
   knob; then say what real change would give it — grade N48SH against N52, magnet thickness or length; both grades
   stay in, nothing is selected). Mid-plane rope induction from about 1.85 to 2.30 T in 6–8 steps. At each step,
   re-tune the outer groove depth (w 20 mm) so the standing-field zero sits at 13 mm and at 16 mm lift-off, and read
   at that position:
   (a) long-loss level per 1 % lost metal, and its linearity at 5 / 10 / 20 % lost;
   (b) flatness of the level along a 300 mm loss and the end spikes relative to it;
   (c) what is mistaken for loss: magnets 1 % weaker; rope 1 % thicker; groove depth 0.1 mm off; the element 0.5 mm
       off in radius; each as apparent % of metal;
   (d) the same four for a direct flux reading (rope flux, yoke flux) for comparison;
   (e) the short-fault peak ΔB_r and ΔB_z at the radial element's lift-off (state which lift-off you use and why);
   (f) rope induction at the mid-plane and its peak along the rope, in tesla; the yoke's highest induction away
       from the groove; the groove depth needed and steel left.
   Also one row per step with NO groove, same read-outs at 13 and 16 mm.
3. Dependence on the rope: repeat the middle three steps for the low and high fill cases the repo already uses
   (`sws/3d/rope_construction.yaml` sensitivity) and for a plausible other rope B–H curve (softer and harder knee).
   The question to answer: does the answer to "where in the window" survive not knowing the rope exactly?
4. Present it as curves against rope induction, one figure with four small panels (level per 1 %; linearity error;
   apparent loss from the four disturbances; short-fault peak), with 1.9 and 2.3 T marked. One table. Then state
   what the curves show: is there a region where the LMA reading is least sensitive to the disturbances and still
   linear; does the short-fault signal pull the same way or the other way; what it costs (magnet, yoke steel).
   No recommendation as a decision; no "optimal", "selected", "chosen"; "best" only with the criterion beside it.
   If the curves are flat across the window, say plainly that the model gives no reason to prefer a point.
5. The 52 mm head: the no-groove row and two steps if time allows; else owed.
6. Note `sws/3d/working_point.md`, easy-read first (five plain sentences, the figure, the table), dense part after;
   JSON in the results folder. Change no HTML page. TASKS.md line; register rows for the owner statement and the
   result.
7. One fresh subagent as falsifier (files, not your conclusions): signs, units, rope steel against yoke steel not
   confused, induction in steel against section average, like compared with like (same zero position), nothing
   firmer than the numbers, cold-reader test. Fix; a second pass only for a blocking item.
Limits to state: 2D axisymmetric, homogenised rope, ring faults, placeholder materials (the whole question depends
on the rope's B–H curve near its knee, which is not measured), calculated not measured.
Prove: `--check` on all nine and pytest tests/test_sws_*.py except p52 (venv C:/Users/stian/Prosjekter-u41/max/.venv;
the report check and one report test fail only because report.html embeds the register — confirm by a rebuild you
do not commit), idscan `python -I C:/Users/stian/secretary/tools/idscan.py . ab4fe6b..HEAD` = 0, scan_tree on added
files = 0. No personal names, roles or dates in prose. Never print max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back at most 14 lines: tip; what the window rests on; the
table at four or five induction steps (level per 1 %, linearity, the four disturbances, short-fault peak, groove
depth); whether a least-sensitive region exists and where; whether it survives the rope uncertainty; what it costs;
52 mm; figure path; falsifier verdict; checks; not verified; owed. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U99 — a layout for plots: hover explanations, a note on every curve, interactive where it helps (Kai, 18 Nov)

The owner's request: the plots are many and not all are understood. He wants one layout that every new plot
follows: a general explanation of the plot on hover, an explanation of each curve on hover, and interactive plots
where possible. Old plots are NOT to be redone now; this unit sets the layout and proves it on the newest ones.
`git worktree add C:/Users/stian/Prosjekter-u99 -b u99-plot-layout ab4fe6b` from C:/Users/stian/Prosjekter-u05
(ab4fe6b = tip of the unmerged u97-groove-physics; verify, stop if it differs). Solver venv (matplotlib, numpy)
C:/Users/stian/Prosjekter/max/.venv. Timebox 120 minutes; past it, stop and report what is done.
Read first: `sws/3d/groove_physics.md`, `sws/3d/yoke_cutout.md`, `sws/3d/axial_liftoff.md`, their figure scripts
under `sws/3d/demo/` and their JSON under `sws/3d/results/`; how `docs/sws/build*.py` embed figures; stemson.md.

Do:
1. A small plotting helper in the repo (say where; one module, no new dependency fetched from the web — look at
   what the venv already has; if a bundled library is in the venv and can write a self-contained HTML file, weigh
   it against plain inline SVG with a few lines of own script, and state the file size each gives). The output of
   one plot is ONE self-contained HTML fragment or file: no CDN, no external script, font or style, works offline
   and from the static site, readable on a phone, prints sensibly (the explanations must also exist as plain text
   under the plot, because hover does not exist on paper or on a touch screen: tap must work, and so must a
   keyboard).
2. The layout, written down as a one-page standard `sws/3d/PLOT_LAYOUT.md`, easy-read first:
   - a title that states what is plotted, in plain words;
   - an "about this plot" marker: hover or tap gives three to five plain sentences — what the axes are, what a
     reader should look at, what the plot shows, what it does not show (calculated or measured; which head; limits);
   - every curve: hover or tap on the curve or its legend entry gives what the curve is, in one or two plain
     sentences, and the value under the pointer with its unit; clicking a legend entry hides or shows the curve;
   - shaded bands and marker lines (limits, ranges) explained the same way;
   - terms: no undefined abbreviation in any hover text; symbols such as B_z explained once in the "about" text;
   - colours distinguishable for colour-blind readers and in grey print; light and dark background;
   - a static PNG of the same plot still written beside it, for documents that cannot carry HTML;
   - where the explanation text lives (beside the data, in the figure script or JSON, so text and numbers cannot
     drift apart) and the rule that the text is written for a reader who has not seen the note.
3. Prove it on three existing plots, from their JSON, without changing their numbers: the standing field against
   lift-off with and without a groove (`yoke_cutout.png`), the field profile from rope axis through the yoke
   (`groove_physics_profile.png`), and the lift-off against groove depth map (`groove_physics_map.png`; a map is
   the hard case — hover gives the values at the pointer and what the contour families mean). Write the
   explanations yourself from the notes; nothing firmer than the notes say; calculated, not measured, stated in
   every "about" text. Output under `sws/3d/figures/interactive/`.
4. Do NOT change any existing HTML page, any builder under docs/sws/, or any existing figure. Say in the standard
   how a page builder would embed a fragment later, and what the page tests would need (the sensor page test
   requires every number in visible text to be linked to a source — say how hover text counts under that test, by
   reading the test, and do not change the test).
5. One fresh subagent as cold reader (the three HTML files only, opened as files; it has not seen the notes): can it
   say what each plot shows and what each curve is from the hover texts alone; any term not explained; any text
   firmer than "calculated"; does it work without a mouse. Fix; one pass.
Prove: `--check` on all nine and pytest tests/test_sws_*.py except p52 (venv C:/Users/stian/Prosjekter-u41/max/.venv;
report check and one report test fail only because report.html embeds the register — say so if you add a register
row, else expect the same 8/9 and 180/181 as the base), idscan
`python -I C:/Users/stian/secretary/tools/idscan.py . ab4fe6b..HEAD` = 0, scan_tree on added files = 0. No personal
names, roles or dates in prose. Never print max-private/identifiers.yaml. No web lookups, nothing downloaded.
Commit on the branch. No merge, no push, no export. Hand back at most 10 lines: tip; the technique used and why;
file sizes; the three file paths; what works on touch, keyboard and print; cold-reader verdict; checks; not
verified; owed. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your
name. — Kai

## U100 — the 52 mm head: groove, zero position and working point, the fine sweep (Kai, 18 Nov)

Read coaming.md (U98), stemson.md (U97), `sws/3d/working_point.md`, `sws/3d/groove_physics.md` first.
`git worktree add C:/Users/stian/Prosjekter-u100 -b u100-h52-sweep 88c7a03` from C:/Users/stian/Prosjekter-u05
(88c7a03 = tip of the unmerged u98-working-point; verify, stop if it differs). Solver venv
C:/Users/stian/Prosjekter/max/.venv. Timebox 180 minutes; past it, stop and report what is done.

The owner's aim: the physical principle for the 52 mm head (the design case) with numbers behind it. U98 did three
coarse steps on H52. Three outside models were asked for the mathematics; what they established (for your tests,
not as authority): the simple interpolation for the zero is off by 1–3 mm for a 20 mm groove, so positions must
come from the field solution; their estimates of the H52 outer-groove depth for a zero at 13 / 16 / 19 mm lift-off
were 6.2 / 5.4 / 4.4 mm (central), 6 / 5.3 / 4.6 and 7.4 / 6.8 / 6.0 mm — set the model's values beside these.
Do, all on H52 with the 52 mm rope (hard wire, 25 °C), yoke 12 mm:
1. No groove: standing B_z and B_r against lift-off 3 mm to the yoke face; ±20 / ±30 mT intervals; rope induction
   at the mid-plane and peak along the rope (say again which quantity the model's rope induction is); yoke
   induction; flux in rope and yoke.
2. Outer groove, all the way round, widths 15, 20, 30 mm: depth in 0.5 mm steps from 3 to 10 mm. Zero-crossing
   lift-off, ±20 mT interval, steel left and its induction (mean and maximum, both), rope induction. A map as in
   U97. The depth that puts the zero at 13, 16 and 19 mm, per width, and mm of zero per 0.1 mm of depth.
3. At those three positions (width 20 mm), at the present working point and at mid-plane rope induction 1.90, 1.95,
   2.00, 2.05, 2.10 T (U98's knob; say what real magnet change each step would need — grade N48SH and N52 both
   stay in, and a thicker magnet; nothing is selected): the long-loss level per 1 % (300 mm loss; and say what
   loss length the model box allows on this head), linearity at 5 / 10 / 20 %, flatness along the loss and end
   spikes, and mistaken-for-loss from: magnets 1 % weaker, rope 1 % thicker, groove 0.1 mm deeper, element 0.5 mm
   further out, element 0.5 mm along the rope. The same disturbances for the rope-flux and yoke-flux readings.
   The short ring fault's peak ΔB_r and ΔB_z at 3 and 5 mm lift-off (the radial element's region).
4. A static reading of the flux, as the outside models asked about: what a field sensor reads (i) inside a thin
   non-magnetic slot through the yoke wall at the mid-plane and at z = ±30 mm, slot 1 and 2 mm, and (ii) just
   outside the steel left over the groove, as candidates for a reading that follows the flux. For each: level per
   1 % lost metal, linearity, the same disturbances, the standing field the sensor must stand, and what the slot
   costs the rope induction. This is a screen, two or three cases each; mark what is not tried.
5. The head's response along the rope: for the axial element at the zero (16 mm case) and for the rope-flux
   reading, the response to a short ring loss (1 % of area over 10 mm) against position, i.e. the kernel; then
   check that convolving the kernel with the 300 mm loss reproduces the directly calculated long-loss trace, and
   state the misfit. This tests whether a level trace can be recovered by processing. Do not build the processing.
6. Note `sws/3d/h52_groove.md`, easy-read first (five plain sentences, two figures, two tables), dense part after;
   JSON in the results folder. Present trade-offs; no recommendation as a decision; no "optimal", "selected",
   "chosen"; "best" only with its criterion. Change no HTML page. TASKS.md line; one register row for the result.
7. One fresh subagent as falsifier (files, not your conclusions): signs, units, 52 against 40 mm numbers not mixed,
   depth against steel left, mean against maximum induction, like compared with like, nothing firmer than the
   numbers, cold-reader test. Fix; a second pass only for a blocking item.
Limits to state: 2D axisymmetric, homogenised rope, ring faults, placeholder B–H curves for rope and yoke (U98
showed the place of the magnet null in tesla moves with the rope curve — repeat the 16 mm case with the softer and
harder knee so the reader sees how much), magnet knob against real magnet, calculated not measured.
Prove: `--check` on all nine and pytest tests/test_sws_*.py except p52 (venv C:/Users/stian/Prosjekter-u41/max/.venv;
report check and one report test fail only because report.html embeds the register — confirm by a rebuild you do
not commit), idscan `python -I C:/Users/stian/secretary/tools/idscan.py . 88c7a03..HEAD` = 0, scan_tree on added
files = 0. No personal names, roles or dates in prose; do not name the outside models. Never print
max-private/identifiers.yaml. No web lookups.
Commit on the branch. No merge, no push, no export. Hand back at most 14 lines: tip; groove depth for zero at
13 / 16 / 19 mm per width beside the three outside estimates; the table at 16 mm across the induction steps; where
the magnet null is and how far it moves with the rope curve; the short-fault signal across the steps; the static
flux candidates; the kernel test; what each induction step costs in magnet; figure paths; falsifier verdict;
checks; not verified; owed. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder).
Sign with your name. — Kai

## U101 — team run: six falsifiers try to break the day's findings (Kai, 19 Nov, night; owner's go given)

Six builders run at once, one section each (A–F below). The common part applies to all.

COMMON
The owner's instruction: a team run on all major design settings that tries to FALSIFY the findings. You are not
here to confirm. A finding you could not break after an honest attempt is reported as "not broken by these tests",
with the tests listed; a finding you broke is reported with the numbers; what you could not test is listed.
The findings under attack (calculated, 2D axisymmetric, homogenised rope, placeholder materials — notes
`sws/3d/axial_liftoff.md`, `yoke_cutout.md`, `groove_physics.md`, `working_point.md`, `h52_groove.md`, their JSON in
`sws/3d/results/`, builder notes rudder / scantling / stemson / coaming / martingale in C:/Users/stian/agent-notes/):
 F1 A groove all round the outside of the yoke at the sensors sets the lift-off where the standing axial field is
    zero (H52: 6.1 / 5.4 / 4.6 mm deep for zero at 13 / 16 / 19 mm; 0.37–0.46 mm of zero per 0.1 mm of depth).
 F2 An axial element at that zero reads a long loss 4–6 times larger than without the groove, and a 1 % magnet
    change is mistaken for well under 1 % of metal; the groove does not change the short-fault peak.
 F3 A yoke thin over its whole length does not do the same job; the thick yoke with a local groove stands.
 F4 The LMA reading is least sensitive to the magnet at a rope induction of 1.92–2.07 T (middle 2.00 T) across a
    physical bracket of rope curves; the short-fault signal keeps rising with induction (+68 % from 1.90 to 2.10 T).
 F5 The axial element alone is not a sufficient LMA reading: a rope 1 % thicker reads as about 2 % more metal; the
    level is flat only over the middle of a loss; a level trace needs processing with the head's response (kernel
    test: sum of short rings reproduces the long loss within 5.4 %, 1.7 % after one fitted gain).
 F6 Proposed direction (not decided): where LMA and local faults pull apart, lean towards LMA, because the local
    fault signal has margin.
Rules for every section:
- Worktree: `git worktree add C:/Users/stian/Prosjekter-u101<letter> -b u101<letter>-falsify c19d94c` from
  C:/Users/stian/Prosjekter-u05 (c19d94c = tip of the unmerged u100-h52-sweep; verify, stop if it differs).
  Touch no other worktree. Solver venv C:/Users/stian/Prosjekter/max/.venv (ngsolve, pyvista). Four of the six
  sections solve at the same time on one machine: keep meshes no finer than the test needs, do not start more than
  two solver processes yourself, and expect slow runs.
- ADD files only, under `sws/3d/falsify/` (note `<letter>_<topic>.md`, scripts, small JSON, figures). Change no
  existing file: no page, no builder, no existing note, no register row, no TASKS line. (So the checks stay as the
  base: `--check` 8 of 9 and pytest 180 of 181, both failing only on the stale report.html — confirm that.)
- Note format, easy-read first: a table "finding / test / result (broken, weakened, not broken, not testable) /
  the number"; then five plain sentences; then the dense part. Nothing firmer than the numbers. No "optimal",
  "selected", "chosen", "decided". Calculated is called calculated.
- idscan `python -I C:/Users/stian/secretary/tools/idscan.py . c19d94c..HEAD` = 0; scan_tree on added files = 0
  (`C:/Users/stian/Prosjekter-u05/max/.venv/Scripts/python.exe -I C:/Users/stian/max-private/tools/scan_tree.py <folder>`).
  No personal names, roles or dates in prose. Never print max-private/identifiers.yaml. No web lookups unless your
  section says so; then general terms only, nothing about the project. No external service.
- Commit on your branch. No merge, no push, no export. Timebox 180 minutes; past it, stop and report.
- Hand back at most 12 lines: tip; per finding you attacked: broken / weakened / not broken / not testable, with
  the one number that shows it; the single most serious thing you found; what you could not test; checks.
  Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name.

SECTION A — the numbers themselves (solver). Attack F1 and F2 as numerical artefacts.
 Mesh convergence of the zero position, the long-loss level and the magnet-drift reading (three refinements, the
 groove corners especially); size of the outer air box and its boundary condition; element order; how the B–H
 tables are interpolated and extrapolated above their last point (what does the model assume beyond the table, and
 does the steel over the groove sit beyond it?); the solver tolerance against the 0.005 mT differences the drift
 numbers rest on. Then an independent calculation: the repo has a second 2D code under `fem-2d/` (see
 `sws_yoke_window.py`) — reproduce the H40 no-groove profile and one groove case with it, or with a hand-built
 magnetic circuit if that code cannot take the case, and state the disagreement in mm of zero position and in %.

SECTION B — tolerances and asymmetries (solver). Attack F1, F2 and F4 with a real head, not an ideal one.
 The two magnet rings unequal (one 2, 5 % weaker): the mid-plane is no longer a symmetry plane — where does the
 zero go, what does the axial element read, does the magnet-drift cancelling survive? The groove not centred on
 the sensor plane (0.5, 1, 2 mm); groove depth ±0.1 and ±0.2 mm; the element ±0.5 and ±1 mm in radius and along
 the rope; yoke steel curve soft / hard (the yoke curve is a placeholder: bracket it from the register's sources);
 temperature −20 / +25 / +45 °C with BOTH grades N48SH and N52 (the magnet coefficient and what the tool does with
 it); rope diameter tolerance 0 to +4 % at equal fill and equal metal. Give each as "mistaken for x % of metal" on
 the H52 head with the zero at 16 mm, and say which tolerances the 10 % discard rule can live with and which it
 cannot, as arithmetic only. Say what a one-point field calibration at installation would remove and what it
 would not.

SECTION C — the third dimension (solver; read `sws/3d/README` and the 3D demo scripts first). Attack F1, F2, F6.
 The head is a clamshell: two half yokes with a split. In 3D (or, if the 3D tool cannot take it in the timebox,
 a 2D planar cut plus a stated argument): does the split, with a gap of 0.2 / 0.5 / 1 mm, change the standing
 axial field at the 16 positions, and does the zero sit at the same lift-off at a position next to the split as
 at one far from it? Does a groove all round still work when the yoke is two halves? Then the premise of F6: the
 signal of ONE broken wire (not a ring) at the radial element, at rope induction 1.90, 2.00 and 2.10 T, at 3 and
 5 mm lift-off, against the allowed noise the repo states (find it; 0.10 mT peak-to-peak in 0–125 Hz is what the
 sensor notes use) — how much margin is there really, and at what induction does it run out? Use the repo's
 existing single-wire figures and scripts first; re-solve only what is missing. And what a single broken wire
 does to the axial element at the zero, 16 mm out.

SECTION D — the measurement chain (desk study, no solver; general web lookups allowed for data-sheet classes of
 parts, general terms only). Attack F2, F5, F6 from the sensor side.
 The level is about 0.5–0.9 mT per 1 % of metal. Against that: the offset, the offset drift with temperature, the
 sensitivity drift, the hysteresis and the noise of the axial part types the repo's candidates notes hold (Z-axis
 TMR, flat Hall; find the data-sheet values already in the repo and use those first), over −20…+45 °C and over a
 year, each converted to "% of metal". The reading is a standing (DC) quantity compared against a base trace taken
 months earlier: what must stay stable, and to how many microtesla? Cross-axis sensitivity: the element sits in a
 zero of the axial field but what are the radial and tangential fields there, and what does 1–2° of tilt do?
 Sixteen positions: does summing or averaging help, and against which errors not? The 16 mm position against the
 parts' ±20 mT range with the tolerances of F1 (0.4 mm of zero per 0.1 mm of depth, about 2 mT per mm). The
 standard's and the company's limits (the repo's notes on ISO 4309: clause numbers and own words only — the
 standard is copyright, quote nothing): 10 % over 30 rope diameters, 6 % over 6 — what resolution and stability
 does that need, and does this chain reach it with what margin? State plainly whether the sensor chain or the
 magnetics is the weaker link.

SECTION E — the documents against each other (desk study, no solver).
 Read the five notes, their JSON, the five builder notes, and the outside answers in
 C:/Users/stian/groove_round_2026-11-18/rounds/ (three files; they are opinions, anonymise them as outside
 answers 1–3, name no model). Find: numbers that differ between notes for the same case; claims in a note that
 its own JSON does not carry; easy-read sentences firmer than the dense part; findings that rest on a single
 case; places where 40 mm results are read as 52 mm; every fix that a falsifier demanded and nobody re-checked
 (list them with file and line). Then the consequences: against `sws/spec/` (the master and
 REDLINE_2026-11-18.md), the register and the sensor notes, list every statement the findings F1–F6 would change
 if they stand — as a list "document / place / what it says now / what would change / how large", sorted by size.
 Change nothing. This list is for the owner to decide from; mark each large item "needs the owner".

SECTION F — magnet and mechanics (solver). Attack F3 and F4 and what a higher working point costs.
 Re-run the working-point steps on H52 with a REAL thicker magnet and the groove in place (owed from the last
 unit: only the remanence knob was run), both grades N48SH and N52: rope induction, zero position, the level, the
 drift reading. Demagnetisation: the lowest working point inside the magnet at each step at +45 °C against the
 knee of each grade (from the register's data; say where the values come from). The force that holds the two
 halves together and the force on the rope, at each step, against what the housing notes assume — does a 1.3×
 or 1.9× magnet break a handling or clamping assumption? Stray field at 50, 100, 300 mm outside against any
 limit the repo states. Weight. Then F3 once more from the other side: is there ANY uniformly thinned or stepped
 yoke, or a yoke of another steel, that gives the zero at 16 mm with less magnet than the groove? Report the best
 competitor you can find and by how much it loses or wins.
— Kai

## U102 — re-run the groove numbers in a model box that is large enough, and with real surroundings (Kai, 19 Nov)

Section A of the team run (note `sws/3d/falsify/a_numerics.md`, builder note hawsepipe.md — read both first) broke
the groove depths: every groove note used a model box that sets the field to zero 300 mm from the rope axis. With
the boundary at 1200 or 2400 mm the H52 depths for a zero at 13 / 16 / 19 mm become 5.02 / 4.31 / 3.59 mm instead
of 6.08 / 5.36 / 4.64, and a second solver agrees. The slope per 0.1 mm of depth and the mesh are not in question.
`git worktree add C:/Users/stian/Prosjekter-u102 -b u102-large-box cb19ba7` from C:/Users/stian/Prosjekter-u05
(cb19ba7 = tip of u101a-falsify, which has the larger-box scripts; verify, stop if it differs). Solver venv
C:/Users/stian/Prosjekter/max/.venv. Two other builders may still be solving: at most two solver processes.
Timebox 180 minutes; past it, stop and report what is done.
Rules as in "## U101" COMMON (read it): ADD files only, under `sws/3d/falsify/` (prefix `g_`); change no existing
file; scans 0; no names, roles or dates; no web lookups; commit on the branch; no merge, push or export.

Do, on H52 with the 52 mm rope unless said otherwise:
1. Settle the box first: zero position and long-loss level for one groove case against box radius AND box length
   (600, 1200, 2400, 4800 mm, or an open-boundary treatment if the tool has one — say which); pick the smallest box
   whose last doubling moves the zero less than 0.05 mm and the level less than 0.5 %, or state plainly that the
   zero does not converge with box size and what that means physically (the field reaches far; the surroundings
   matter). Everything below runs in that box. Give the old 300 mm value beside each new value.
2. Redo in that box: no-groove standing field against lift-off and the ±20 / ±30 mT intervals; groove depth for the
   zero at 13 / 16 / 19 mm (width 20 mm) and mm of zero per 0.1 mm; the long-loss level per 1 % with and without
   groove and their ratio; magnets 1 % weaker read as; the lift-off where the magnet reading is null against the
   lift-off of the zero, at the modelled magnet and at rope induction 1.95, 2.00, 2.05 T; the working-point null
   across the low / middle / high rope curves; the short-fault peak at 3 mm with and without groove at equal
   magnet; the kernel test (short rings summed against the long loss). One table "old box / large box / change".
   The same for H40 with the 40 mm rope: depths and the level only.
3. Real surroundings, because the zero now looks sensitive to what is outside the yoke: (a) a steel housing shell
   around the head (take the housing's steel or aluminium and wall from the housing notes; if it is aluminium or
   stainless say so and treat it as air for the static field, then test a mild-steel shell 3 mm thick at 10 and
   30 mm outside the yoke as the adverse case); (b) a large steel plate or beam passing 100, 200 and 500 mm from
   the rope axis (in 2D axisymmetric this is a steel tube at that radius — say that it overstates a one-sided
   object); (c) a second identical head on the same rope 300 and 600 mm along it. For each: movement of the zero,
   change of the level, and what it is mistaken for in % of metal. Say what a one-point calibration after
   installation removes and what changes if the surroundings change afterwards (a vessel, a platform moving).
4. Note `sws/3d/falsify/g_large_box.md`, easy-read first: the table of point 2, five plain sentences, then the
   surroundings table, then the dense part. Say which of the day's notes carry numbers from the 300 mm box (list
   them; change none). Nothing firmer than the numbers; calculated, not measured; no "optimal", "selected",
   "chosen".
5. One fresh subagent as falsifier (files only): old against new not swapped, 40 against 52 mm not mixed, units,
   signs, nothing firmer than the numbers, cold-reader test. Fix; a second pass only for a blocking item.
Hand back at most 12 lines: tip; the box used and whether the zero converges; the old / new table in short; what
changes in the findings F1–F5 (see "## U101"); the surroundings result; falsifier verdict; checks; not verified;
owed. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign with your name. — Kai

## U103 — the 40 mm prototype head as drawn: where is the zero, and what would a gaussmeter read (Kai, 19 Nov)

The owner received a section drawing of the 40 mm prototype head. The model's "H40" is NOT that head (H40: yoke
radius 43.2–51.7 mm, magnets 40 mm long at 50–90 mm from the middle). Read kentledge.md and
`sws/3d/falsify/g_large_box.md` first (large box r 2400 × z ±2400 mm, `g_lib.py`).
`git worktree add C:/Users/stian/Prosjekter-u103 -b u103-prototype-head 1ded20a` from C:/Users/stian/Prosjekter-u05
(1ded20a = tip of u102-large-box; verify, stop if it differs). Solver venv C:/Users/stian/Prosjekter/max/.venv.
At most two solver processes. Timebox 120 minutes; past it, stop and report what is done.
Rules as "## U101" COMMON: ADD files only, under `sws/3d/falsify/`, prefix `h_`; change no existing file; scans 0
(idscan range 1ded20a..HEAD); no names, roles or dates; no web lookups; do not copy the drawing into the repo;
commit on the branch; no merge, push or export. Calculated is called calculated; no "optimal / selected / chosen".

Geometry. DIMENSIONED on the drawing (use as given): yoke 105 mm long (z ±52.5), outside dia 102; one groove
round the outside at the middle, 10 mm wide (z ±5), bottom at dia 98 (2 mm deep); yoke inside dia 88 between the
magnets and dia 86 at the magnets (so the inside is relieved 1 mm between the magnets); radial holes dia 12
through the yoke wall centred 28.5 mm from each yoke end (z ±24), their number round the yoke not known; end
plates outside the yoke, overall length 125 mm (10 mm each), material not known. Rope 40 mm.
READ OFF THE PICTURE BY SCALE (approximate; bracket them): each magnet ring about 20 mm long at the yoke end
(z 32.5–52.5; bracket 18–22), radius about 24 to 43 mm (inner 23–25), drawn as two radial layers; a sleeve in the
bore, inner radius about 22 mm. Magnet grade not known: base N42 at 25 °C, bracket ±5 % remanence. Radially
magnetised, the two rings opposed as in the repo's heads. An axial sensor radius of about 36.5 mm was reported
earlier for this head (not confirmed): mark it in every profile.
Do:
1. Base case as drawn (holes ignored, end plates as air), middle rope curve: standing B_z and B_r on the
   mid-plane against radius from the rope surface to the yoke; the zero of B_z (lift-off and radius); the
   ±20 / ±30 mT intervals; B_z and B_r at 3, 5, 8, 10, 13, 16.5 mm lift-off; rope induction (mid-plane, peak);
   induction in the steel under the groove and in the yoke elsewhere; flux in rope and yoke.
2. What each cut does, one at a time against the base: no outer groove; no inner relief (inside dia 86
   throughout); inner relief only; outer groove 1 / 2 / 3 mm deep and 10 / 20 mm wide. For each: zero position,
   B_z at 16.5 mm lift-off, long-loss level per 1 % at the zero and at 16.5 mm. (The owner knows only that one
   cut-out tested on this head did not help and another helped a lot; say what the model gives, do not say which
   was which.)
3. Brackets on the base: rope curve low / middle / high; magnet length, inner radius, remanence; end plates as
   mild steel; the holes — axisymmetric cannot hold them: give (a) holes ignored and (b) an equivalent ring with
   the same steel removed for 2, 4 and 6 holes, and say it is a stand-in. Result as "zero at x mm, from y to z".
4. For the rig (no rope cutting, head moves, no calibration coil): a short table "what a gaussmeter probe would
   read" — axial and radial field at the mid-plane at five radii a probe could reach, with the rope in and with
   the head empty, with the bracket; and which single reading separates the model from its alternatives best.
5. Note `sws/3d/falsify/h_prototype_head.md`, easy-read first: the dimensions table (dimensioned / read by scale
   / assumed), one table of results, five plain sentences, one figure (B_z against lift-off: as drawn, no
   groove, no relief, with the bracket as a band; sensor radius marked), then the dense part. Plot text short:
   legend and two or three notes, no long caption.
6. One fresh subagent as falsifier (files only): dimensions against this brief, radius against lift-off not
   mixed, signs, units, nothing firmer than the numbers, cold-reader test. Fix; second pass only if blocking.
Hand back at most 12 lines: tip; zero position as drawn with its bracket; B_z at 16.5 mm; what each cut does;
level per 1 %; the gaussmeter table in short; which unknown moves the answer most; falsifier verdict; checks; not
verified. Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). Sign. — Kai

## U104 — a plot standard for the shared agent repository: research type and presentation type (Kai, 19 Nov)

Repository C:/Users/stian/model-round (remote fjordbit/agentic, tip bc6c4cd; verify). Work on a new branch
`plot-standard` there. Commit on the branch; NO push. Read its README.md and CLAUDE.md first.
Source to generalise: the project's first plot layout, branch u99-plot-layout (ab5ee65) in
C:/Users/stian/Prosjekter-u05: `max/sws/3d/plotlayout.py`, `max/sws/3d/PLOT_LAYOUT.md`,
`max/sws/3d/demo/interactive_figures.py` (read with `git show ab5ee65:<path>`). Copy NO project content: no
sensor, rope, company or project words, numbers or figures. The examples use invented general data (the repo's
weather-station example is the tone). scan_tree on the committed tree must be 0
(`C:/Users/stian/Prosjekter-u05/max/.venv/Scripts/python.exe -I C:/Users/stian/max-private/tools/scan_tree.py <folder>`);
never print C:/Users/stian/max-private/identifiers.yaml. No web lookups except library documentation.
The owner's words on the first layout: "very close, perhaps overkill"; the About text and the text underneath
"seemed like it was trying to be long and over elaborate". What is wanted: short and straight; the information
spread over the parts that already carry it (legend, hover on each curve, plot notes); abbreviations explained
once in a terms list and LINKED from the plot, never explained again; more detail behind a link; someone with
some knowledge of the field understands what they are looking at. This is to be the standard for research
figures; and a simpler second type for slides.
Deliver:
1. `docs/PLOT_STANDARD.md`, one page, easy-read: the two types, the rules of each as a short list, one example
   picture of each, and "which type when".
   - Research type: interactive HTML (hover) plus a static PNG twin; title = what is plotted; axis labels with
     units; legend entry of at most six words per curve; hover per curve: ONE sentence saying what the curve is
     and how it was obtained (calculated / measured / assumed); a plot note of at most three sentences; a link
     to the terms list and a link to the source note; no About block, no text under the plot beyond the note;
     calculated and measured visibly different (say how); colour-blind-safe palette, also readable in grey.
   - Presentation type: static, 16:9, one message as the title (a sentence with the finding), at most four
     curves, labels on the curves instead of a legend where possible, large type readable from the back of a
     room, no hover, no note beyond one source line, units on axes.
   Hard limits as numbers (words, sentences, curves, font sizes), so a checker can test them.
2. `plotstandard.py` (one module, small): two functions that take the same data description and produce each
   type; a check function that fails a figure breaking a hard limit. Use the libraries the source uses unless
   there is a reason; keep requirements minimal and add them to the requirements files.
3. `examples/plots/`: one invented data set, both types generated from it, outputs committed (HTML + PNG).
4. Tests for the limits (run with the repo's test command; all existing tests still pass).
5. One short paragraph in README.md pointing to the standard, and one line in the repo's CLAUDE.md: figures
   follow docs/PLOT_STANDARD.md. Nothing else in those two files changes.
6. One fresh subagent as cold reader (given only the standard and the two example outputs): can it say what each
   plot shows, and is anything longer than it needs to be? Cut; second pass only if blocking.
Timebox 90 minutes. Hand back at most 10 lines: tip; files; the hard limits; what the cold reader said; tests;
scan; not verified; full paths of the two example outputs. Notes in C:/Users/stian/agent-notes/<nautical name>.md
(a name not in that folder). Sign with your name. — Kai

## U105 — potting resins of the Scotchcast family against the head's needs (Kai, 19 Nov)

The owner asks: look at 3M Scotchcast 2123 and the other Scotchcast versions; they are not mentioned in the
housing and sealing note. Read first: `max/sws/hw-selection/sws_housing_sealing.md` (form, source table, the
three example compounds EP / PU / GEL, the conflicts section) and `max/docs/sws/housing.html` section "Tests for
the prototype" (text only). The new note follows the form of the first.
`git worktree add C:/Users/stian/Prosjekter-u105 -b u105-scotchcast 062b8bd` from C:/Users/stian/Prosjekter-u05
(062b8bd = main; verify, stop if it differs). ADD one file only: `max/sws/hw-selection/sws_potting_scotchcast.md`.
Change no existing file. Commit on the branch; no merge, push or export. Timebox 75 minutes; past it, stop and
report what is done.
Rules: web lookups with GENERAL queries only (product names and properties; never the company, the project, the
rope or the sensor in a query). Read the maker's data sheets; give a number only if you read it on a sheet, with
the sheet's title, revision/date and address in the source table; "not on the sheet" where it is not. Do not copy
data-sheet PDFs into the repo. A quote of at most one short sentence per source; the rest in own words. No
personal names, roles or dates in the prose. Nothing is "selected / chosen / optimal / recommended": the note
compares. scans 0 before commit: idscan on added lines (range 062b8bd..HEAD) and scan_tree, as the earlier units
did (tools in C:/Users/stian/max-private/tools/; never print identifiers.yaml).
What the head needs (from the record; do not restate beyond a short table): operating −40 / +50 °C; outdoors at
sea, salt, rope lubricant; IP66/IP67; potted around a circuit board with magnetic field sensors whose zero and
sensitivity shift under mechanical stress (so a low-modulus compound and low cure stress matter); NdFeB magnets
nearby, N52 limits cure temperature to about 60 °C (N48SH higher); a cable entry that must stay tight; a split
head, so each half is potted on its own; small volume (tens to a few hundred ml); rework is a plus, not a must.
Do:
1. Scotchcast 2123: what it is (chemistry, one or two part, intended use), mix and pot life, cure schedule and
   whether it cures at room temperature, exotherm, hardness, modulus or elongation, glass transition, service
   temperature range, CTE, water absorption, dielectric data, adhesion to metals and cable jackets,
   re-enterable or not, chemical / oil resistance, shrinkage, shelf life, pack sizes, approvals. Say for each
   whether it was read on the sheet.
2. The family: the other Scotchcast electrical resins that could be candidates (for example the re-enterable
   gel types, the flexible polyurethane cable-joint resins such as the 40-series, the rigid epoxies such as
   the 2xx/2xxx-series, the flame-retardant types). One line each in a table with the same properties, then
   which three or four deserve a closer look for this use and why, and which are clearly unsuitable and why.
3. Each candidate against the needs table: meets / does not meet / not on the sheet, per need. Mark the cure
   temperature against the 60 °C limit and the low end against −40 °C plainly.
4. Compare in two or three sentences with the three example compounds already in the housing note.
5. What a test on the prototype would have to show for these resins that a sheet cannot (tie to the existing
   test list; add nothing to it, list proposals separately).
6. Easy-read first: five plain sentences and the comparison table on top; the dense part and the source table
   below. Open questions at the end.
7. One fresh subagent as falsifier (given the note and the sheets' addresses only): every number against its
   sheet, units, nothing firmer than the sheet, product numbers not mixed up, cold-reader test. Fix; a second
   pass only if blocking.
Hand back at most 12 lines: tip; what 2123 is in one sentence; the three or four candidates with the one fact
that matters for each; what is unsuitable; what the sheets do not say; falsifier verdict; scans; not verified.
Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). If a permission is denied,
stop and report it; do not ask anyone to do the action for you. Sign with your name. — Kai

## U106 — the groove plots redrawn with the large-box numbers, in the plot standard, as a marked proposal (Kai, 19 Nov)

The owner said yes to: redraw the groove plots with the corrected numbers in the new short form, as a marked
proposal for the sensor page, to look at before anything is published.
`git worktree add C:/Users/stian/Prosjekter-u106 -b u106-groove-plots 02a9486` from C:/Users/stian/Prosjekter-u05
(02a9486 = tip of u103-prototype-head; verify, stop if it differs). Solver venv C:/Users/stian/Prosjekter/max/.venv.
At most two solver processes. Timebox 120 minutes; past it, stop and report what is done.
Read first: `max/sws/3d/falsify/g_large_box.md` (the correction; large box r 2400 × z ±2400 mm, `g_lib.py`,
`g_results/`), `max/sws/3d/falsify/h_prototype_head.md` and `h_results/`, the old plot scripts for
`max/sws/3d/figures/groove_physics_profile.png`, `groove_physics_map.png`, `h52_groove_working_point.png`,
`h52_groove_map.png`; the plot standard in C:/Users/stian/model-round: `docs/PLOT_STANDARD.md`, `plotstandard.py`,
`examples/plots/`; and the sensor page section "Where the sensor can sit" in `max/docs/sws/sensor.html`
(id s-where; text only) and `max/docs/sws/build_sensor.py`.
Rules as "## U101" COMMON: ADD files only; change no existing file (in particular not sensor.html, build_sensor.py
or any existing figure); scans 0 before commit (idscan on added lines, range 02a9486..HEAD, and scan_tree); no
personal names, roles or dates; no web lookups except library documentation; commit on the branch; no merge, push
or export. Calculated is called calculated; nothing is "optimal / selected / chosen / decided". Where a magnet
grade matters, both N52 and N48SH are shown. Lift-off is from the rope surface; do not mix it with radius.
Put everything under a new folder `max/sws/3d/groove_plots/`.
Do:
1. Copy `plotstandard.py` from C:/Users/stian/model-round (main, 573e59b) unchanged into the folder, with one
   line in the folder's README saying where it came from. Every figure passes its `check`; if a limit cannot be
   met, cut the figure, do not loosen the check. If the standard cannot draw something needed (a field map),
   say so and make that one figure by hand to the same limits; do not change the module.
2. Data: use the large-box results already in `g_results/` and `h_results/` where they hold what a plot needs;
   re-run in the large box (with `g_lib.py`) only what is missing. No old-box number in any figure. Each figure's
   source note names the result files and the script.
3. Figures, each as research type (HTML with hover + PNG) and, for A and B, also as presentation type (16:9 PNG):
   A. How the groove moves the zero (H52, 52 mm rope): standing axial field against lift-off, without a groove
      and with the groove depths that put the zero at 13, 16 and 19 mm; the ±20 mT range of the axial sensor
      marked.
   B. Groove depth against where the zero falls (H52), 0 to about 6 mm, with the three points 4.98 / 4.25 /
      3.53 mm marked, and the same curve for H40 if the data are there.
   C. What the groove buys: the long-loss level per 1 % against lift-off, with and without the groove.
   D. The prototype head as drawn: axial field against lift-off as drawn, without the outer groove, without
      the inner relief, with the bracket; the reported sensor radius marked as "reported, not confirmed".
   E. One field map of the head with the groove (large box, cropped to the head), if it can be made short and
      clear; otherwise leave it out and say so.
   One terms list (`terms.md`) and one source note per figure or one shared `source.md`, linked from the plots.
4. `proposal_sensor_page.md`, headed "PROPOSAL — not in the specification, not on the pages": the text that
   would go into the section "Where the sensor can sit", easy-read, at most 150 words plus figures A and B with
   one-sentence notes; C, D and E behind a "detail" link. Say what is calculated, what is not measured, and what
   is open (sensor distance not picked; the zero must be adjustable; steel near the head). Give exactly where in
   the section it would sit (after which existing paragraph), without editing the page.
5. A table in the README: figure, files, what it shows in one line, which numbers it carries, where they come
   from.
6. One fresh subagent as falsifier (files only): every number in a figure or the proposal against
   `g_large_box.md` / `h_prototype_head.md` and the result files; no old-box number left; lift-off against
   radius; signs and units; the standard's limits; a cold reader says what each plot shows. Fix; a second pass
   only if blocking.
Hand back at most 12 lines: tip; the figures made, with full paths of the HTML and PNG files; anything re-run;
anything left out and why; the proposal's word count; falsifier verdict; scans; not verified.
Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). If a permission is denied,
stop and report it; do not ask anyone to do the action for you. Sign with your name. — Kai

## U107 — the trade-off map: groove depth against rope induction, axial gain against radial cost; Hall beside TMR for the axial element (Kai, 19 Nov; owner's go given)

The owner asks for plots that show, in one picture, why the groove cannot be made as deep as one likes (it also
costs the radial side), and what happens if the magnets take the rope higher (2.2, 2.3 T): less groove or more.
The owner's method: first a coarse net for approximate values, then a tight net in the area of interest.
Names (use in every new text): SWS = the whole product; head = the part round the rope (magnets, yoke, board);
element = one TMR or Hall chip (axial element, radial element); channel = one signal out (broken-wire channel,
loss-of-metal channel). Do not call an element "sensor".
`git worktree add C:/Users/stian/Prosjekter-u107 -b u107-tradeoff-map 1bd304c` from C:/Users/stian/Prosjekter-u05
(1bd304c = main; verify, stop if it differs). First step on the branch: `git merge u106-groove-plots` (tip
d112319; it only adds the folder `max/sws/3d/groove_plots/` with plotstandard.py and figkit.py; stop if it
conflicts). Solver venv C:/Users/stian/Prosjekter/max/.venv. At most two solver processes. Timebox 180 minutes;
past it, stop and report what is done.
Read first: `max/sws/3d/falsify/g_large_box.md` and `g_lib.py` (large box r 2400 × z ±2400 mm; ALL solves in
this unit use it), `max/sws/3d/h52_groove.md` (the working-point tables; old box, for the method and the
read-outs only), `max/sws/3d/falsify/c_third_dimension.md` and `d_measurement_chain.md` (one broken wire against
rope induction; the inner-wire margin), `f_magnet_mech.md` (real thicker magnets, the empty warm head),
`max/sws/3d/groove_plots/README.md`, `figkit.py`, and C:/Users/stian/agent-notes/stunsail.md and kentledge.md.
Rules as "## U101" COMMON: ADD files only, in a new folder `max/sws/3d/tradeoff/`; change no existing file;
scans 0 before commit (idscan on added lines, range 1bd304c..HEAD, and scan_tree); no personal names, roles or
dates; commit on the branch; no merge to main, no push, no export. Calculated is called calculated; nothing is
"optimal / selected / chosen / decided / recommended"; where a magnet grade matters both N52 and N48SH are
shown. Lift-off is from the rope surface; never mixed with radius. Web lookups only for part 5, general queries
(part families and data sheets; never the company, the project or the rope in a query); data-sheet PDFs are
read, not copied into the repo; a number only if read on a sheet, with the sheet in a source table.
Do (H52 head, 52 mm rope, middle rope curve, 25 °C, groove 20 mm wide, unless said):
1. Coarse net. Two knobs: groove depth 0 to 7 mm (step about 1 mm) × magnet strength from the model magnet up to
   as far as the head can take the rope (remanence scale k and/or real thicker magnets as in f_magnet_mech; aim
   for rope induction at the mid-plane from 1.85 T to 2.30 T; if 2.2 or 2.3 T cannot be reached in this head, say
   at what induction it stops and why: magnet thickness, yoke saturation, room). At each point: rope induction
   (mid-plane, peak); the zero of the standing axial field; standing B_z at 13, 16, 19 mm; the loss-of-metal
   level per 1 % at the zero and at 13 / 16 / 19 mm; magnets 1 % weaker read as; the short-fault signal of the
   radial element (largest |ΔB_r|, the repo's short ring) at 3, 5 and 8 mm lift-off; the standing radial and
   axial field at those lift-offs against the radial element's range; and the inner-wire margin from the
   repo's own method (name the note and method used; if it cannot be carried to this net, say so and give the
   rope induction as its stand-in).
2. Fine net. From the coarse net, mark the area where the zero falls between 13 and 19 mm AND the rope is at or
   above 1.90 T, and refine there (depth step 0.25 mm or finer, induction step 0.02–0.03 T). Report mesh
   scatter; smooth nothing silently.
3. The second view the owner asked for: along lines of constant zero (13, 16, 19 mm), groove depth needed
   against rope induction, with the axial level and the radial short-fault signal on the same lines: does a
   stronger magnet want less groove or more, and what does each side gain or lose. Include N48SH and N52
   thicknesses that give each induction, and mark where N52 in the warm empty head is past its knee if
   f_magnet_mech's method gives it cheaply (else leave it out and say so).
4. Figures, in the plot standard (plotstandard.py + figkit.py from the merged folder; every figure passes
   `check`; hand-drawn maps to the same limits):
   F. The map: groove depth (x) against rope induction (y), lines of constant zero (13 / 16 / 19 mm), shading
      or contours for the axial level, contours for the radial short-fault signal at 3 mm; the area of step 2
      outlined. One picture that carries the trade-off.
   G. At the model magnet: axial level and radial short-fault signal (both as % of their no-groove value)
      against groove depth, with the zero position on a second panel or as marks.
   H. Along constant zero at 16 mm: groove depth, axial level, radial signal against rope induction.
   I. Radial short-fault signal against lift-off 3 / 5 / 8 mm, with and without the groove (the owner asks
      whether 3 mm is too close; the plot shows what moving the radial element out costs).
   F and G also as presentation type. Legends: keep entries short; if figkit allows it without changing
   plotstandard.py, lay the HTML legend out in even columns aligned with the plot area and put "Terms · Source"
   on its own line (do it in figkit or the figure script, and say what you did).
5. Hall beside TMR for the axial element (desk study, data sheets): three or four current linear Hall parts and
   the TMR parts already in the repo's sensor notes (`max/sws/hw-selection/`, read what is there first). Per
   part: sensing direction relative to the package, range, sensitivity, noise (density and over 0.1–100 Hz if
   given), zero offset and its drift with temperature, sensitivity drift, hysteresis, supply and current,
   package, price class. Then, with this unit's numbers: for each part, the smallest long loss it resolves at
   the zero and without a groove (noise and drift over −40…+50 °C against the level per 1 %), and whether it
   stays in range in the standing field at 13 / 16 / 19 mm with and without the groove. Say plainly what a Hall
   element gains (range, no saturation, direction) and loses (noise, drift), and that the board arrangement is
   not confirmed, so the direction argument is given both ways. Compare; pick nothing.
6. Note `tradeoff.md`, easy-read first: six plain sentences, one results table, figures F and G; then the dense
   part, the Hall/TMR table with its source table, and what is not calculated. Old-box numbers from
   h52_groove.md appear only in a marked comparison row, if at all.
7. One fresh subagent as falsifier (files only): every number against the result files; large box everywhere;
   lift-off against radius; signs and units; names (element, not sensor); nothing firmer than the numbers; the
   Hall/TMR numbers against the sheets; a cold reader says what figure F shows. Fix; second pass only if
   blocking.
Hand back at most 14 lines: tip; how far the rope induction could be taken and what stopped it; less or more
groove with stronger magnets (numbers along the 16 mm line); what the groove costs the radial side (numbers);
what moving the radial element from 3 to 5 and 8 mm costs; the Hall/TMR finding in two lines; full paths of
figures F–I (HTML and PNG); falsifier verdict; scans; not verified.
Notes in C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). If a permission is denied,
stop and report it; do not ask anyone to do the action for you. Sign with your name. — Kai

## U108 — blind round on the data path from the converters to the logger; traffic graphs (Kai, 19 Nov; owner's go given)

The owner asked for a blind agent run on the data path "from ADC to logger computer", with what is certain
only, and graphs of the amount of traffic. The blind brief is written and scanned (0 hits):
C:/Users/stian/agent-notes/u108_blind_brief.md. Do NOT change it and do NOT add to it.
`git worktree add C:/Users/stian/Prosjekter-u108 -b u108-data-path 1bd304c` from C:/Users/stian/Prosjekter-u05
(1bd304c = main; verify, stop if it differs). First step on the branch: `git merge u106-groove-plots` (d112319;
adds only `max/sws/3d/groove_plots/` with plotstandard.py and figkit.py; stop on a conflict). Another builder
works in C:/Users/stian/Prosjekter-u107: do not touch it. No solver is needed. Timebox 120 minutes.
Rules as "## U101" COMMON: ADD files only, in a new folder `max/sws/data-path/`; change no existing file; scans
0 before commit (idscan on added lines, range 1bd304c..HEAD, and scan_tree); no personal names, roles or dates;
no customer, site or installation names anywhere (the brief's "installation A / B" are the names to use);
commit on the branch; no merge to main, no push, no export; nothing is "selected / chosen / decided /
recommended" by you. Names: SWS = the whole product; head; half; element; channel; "root box" as the
specification calls the box (say once that the owner also calls it the transmitter).
Do:
1. Start THREE fresh subagents, in parallel, each given ONLY the text of the blind brief (paste it whole; no
   path into the project, no word about this repository, the others, or you). They may use general web
   queries. Save each answer unchanged as `answers/answer_1.md` … `answer_3.md`.
2. Your own check, independent of them, as a small script `traffic.py` (standard library plus what the plot
   helpers need): the traffic arithmetic of the brief's point 3 from first principles, written so each
   assumption is one named constant (bytes per sample, frame header, check, start/stop bits, MQTT and
   TCP/IP/Ethernet overhead, samples per frame). Output `traffic.json` and tables. Where an answer's number
   differs from yours by more than 10 %, find out why and say who is right.
3. What the record already says: read `max/sws/spec/SWS_HW_Design_Input_Specification_rev123_2026-10-23.md`
   sections on sampling, the array, the electronics and interfaces (search RS-422, ADS131M08, root box, 1 Hz,
   15 m/min, 1 mm), `max/sws/fem-2d/sws_sync_findings.md` if present, and the software and hardware notes
   under `max/sws/` that mention the link. Make a table: item / what the specification says (with section) /
   what the owner's newer thought is (from the blind brief) / what the three answers say / agreed or not.
   The blind agents never see this.
4. Figures in the plot standard (plotstandard.py + figkit.py from the merged folder; every figure passes
   `check`; research type HTML + PNG; figure T1 also as presentation type):
   T1. Bit rate on one serial line against samples per second per channel (10 … 1000), for 1, 2 and 4 halves
       on a line, with the 115.2 k, 460.8 k and 1 Mbit/s limits and a named margin marked.
   T2. Rope length between two samples against rope speed (1 … 15 m/min) for 10, 20, 50, 100 and 250 samples
       per second, with the 10–20 mm fault length and the 1 mm pitch of the specification marked.
   T3. Traffic on the head network for installation A and B against sample rate, raw against reduced, with
       100 Mbit/s and 1 Gbit/s marked; and storage per day on a second panel or a second figure.
   T4. Safe cable length against bit rate for RS-422 / RS-485, from the standard's guidance (say which
       document; assumed curve marked as assumed).
5. Note `data_path.md`, easy-read first: eight plain sentences (what all three agree on; where they differ;
   what the sample-rate question comes to; how much traffic there is; whether RS-485 with two heads on a line
   holds; what the temperature part should be; what is most likely to go wrong; what the owner must answer),
   the comparison table of point 3, figures T1 and T2, then the dense part: each answer in ten lines, the
   disagreements as a list for the owner (they are not resolved by you), all assumptions, the questions for
   the owner in order, and what is not known.
6. One fresh subagent as falsifier (files only, not blind): the arithmetic in traffic.py and every number in
   the note against traffic.json and the answers; units (bit against byte, k against M); the figures against
   the tables; names; nothing firmer than the sources; a cold reader says what T1 and T2 show. Fix; second
   pass only if blocking.
Hand back at most 14 lines: tip; what the three agree on; where they differ; the sample-rate finding with
numbers; traffic per half / head / winch / installation A and B at 10 and 250 samples per second; whether two
heads on one RS-485 line hold and at what rate; the temperature-sensor finding; full paths of T1–T4 (HTML and
PNG); the five most important questions for the owner; falsifier verdict; scans; not verified.
Do not hand back while background work of your own is still running. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). If a permission is denied, stop and
report it; do not ask anyone to do the action for you. Sign with your name. — Kai

## U109 — the complete transmitter line: head to box to logger, with curves, logging and disk sizing (Kai, 19 Nov evening; owner's go given)

The owner wants this evening spent on "the complete transmitter line": from the converters in the half to the
main box first, then MQTT from the box to the logger; with curves, with logging, with sizing of the disks. New
facts from the owner today (use them; they are also in the blind brief):
- No speed sensor and no run signal on the first installation: "we do not know what a millimetre is". The
  strand ripple is seen so clearly in the tests that it "could almost be used as an encoder". Speed is known only
  after a full run, from the ramps and the fixed length out and back. The later, large installation can have an
  encoder. Not a safety system now: delay does not matter.
- Rope speed normally about 5 m/min on the 52 mm rope; 15 m/min is an extreme, about double what will ever be
  seen.
- Two 8-channel converters per half (8 radial + 8 axial elements), digital temperature. The specification's
  three converters is out-of-date text.
- "I know we had made some code already but I see no averaging." And: averaging must not make drift invisible.
  He liked that converter noise rises with data rate and asks for curves of it, to find a rate that is high
  enough and no higher.
A blind round runs in parallel on the same question with three outside models (Opus, Grok, Codex). Brief:
C:/Users/stian/data_path_round_2026-11-19/brief.md. Answers land under
C:/Users/stian/data_path_round_2026-11-19/answers/ (one Markdown file per model; may take 30 minutes). Do your
own parts 1–5 first, WITHOUT reading the answers; then read them for part 6. If no answer is there 100 minutes
after you start, go on without and say so. The earlier blind round (three Claude agents) and its traffic
arithmetic are on branch u108-data-path (8c3218c), folder `max/sws/data-path/` — read `data_path.md`,
`traffic.py`, and C:/Users/stian/agent-notes/foresail.md first.
`git worktree add C:/Users/stian/Prosjekter-u109 -b u109-transmitter-line 8c3218c` from
C:/Users/stian/Prosjekter-u05 (8c3218c = tip of u108-data-path; verify, stop if it differs). Another builder
works in C:/Users/stian/Prosjekter-u107: do not touch it. Timebox 180 minutes; past it, stop and report.
Rules as "## U101" COMMON: ADD files only, in a new folder `max/sws/transmitter/`; change no existing file;
scans 0 before commit (idscan on added lines, range 8c3218c..HEAD, and scan_tree); no personal names, roles or
dates; no customer, site or installation names ("installation A / B"); commit on the branch; no merge to main,
no push, no export; nothing is "selected / chosen / decided / optimal / recommended" by you — the owner asked
for "the optimal high enough" rate: give the curve and the range where it holds, and say what decides inside
it. Names: SWS, head, half, element (radial / axial), channel, root box (the owner's "transmitter", say once).
Web lookups: the converter data sheets and public standards only, general queries; a number only if read on
the sheet (say which sheet, revision, table); PDFs are read, not copied into the repo. Calculated, read from a
sheet, assumed and measured are kept apart in every table.
Do:
1. What is on record. Find the code the owner means (firmware, read-out, link or logger code: search the repo,
   start with `max/sws/` and the software page's sources under `max/docs/sws/build_software.py`; also the
   specification sections 7, 8 and 10 and `sws_sync_findings.md`). One table: what exists, where, what it does,
   what it lacks (averaging, framing, time stamps, position). Say plainly if there is no averaging.
2. Noise against data rate. From the data sheets of the two converter candidates (ADS131M08, ADS131E08):
   the table of data rate / oversampling against input-referred noise and effective bits at the gains that fit
   a bridge output (state the assumed bridge sensitivity and supply; take them from the repo's sensor notes
   and say which), converted to field noise in µT at the element. Curve N1: field noise against converter data
   rate, both parts. Then averaging: curve N2: noise after decimation to line rates of 100, 250, 500, 1000
   per second from each converter rate (white-noise rule, and say where 1/f noise of converter and element
   stops it helping). Against the two needs: a broken wire of a fraction of a millitesla, and a level error of
   0.005 mT that is 1 % of a 1 % loss (take the level per 1 % from `max/sws/3d/falsify/g_large_box.md`).
3. Averaging that does not hide drift and does not smear a fault. Frequency content of a 10 and a 20 mm fault,
   of the strand ripple and of the long-loss signal at 1, 5, 7.5 and 15 m/min (figure S1: a band chart). Compare
   plain block averaging, a moving average, and a proper decimation filter (for example cascaded integrator
   comb plus a short compensating filter): pass-band droop on the fault (figure S2: amplitude kept against
   line rate, 10 and 20 mm, at 5 and 7.5 m/min), aliasing of the ripple, and what each does to a slow drift
   (show that a low-pass keeps drift and that any high-pass or offset removal in the half would remove the
   long-loss signal; so none in the half). State the rule that follows, as a rule with its number.
4. Position without an encoder. From the repo's own data if there is any trace with strand ripple (search
   `max/sws/` for recorded or simulated traces; if none, build a simulated one and say so): how well the
   ripple phase gives rope position (figure P1: position error against noise and ripple amplitude), what the
   fixed length and the ramps add, and registration of a run to the first run (the specification's ±4 mm
   scheme, section 8/10). What the half and the box must record for it. What breaks it. What an encoder adds
   on the large installation. Mark everything simulated as simulated.
5. The line itself, as a design draft with alternatives beside it (not selected): frame layout byte by byte;
   serial rate and margin (reuse traffic.py; add the two-converter frame); the 1 Hz edge; the box in blocks
   (receive, check, stamp, buffer, forward, health), buffer size for 1 h and 24 h of lost network; MQTT topics,
   payload and message rate, with one alternative beside it; logging: what is stored, per-run files,
   detecting "moving" from the data when there is no run signal; storage per run / day / year for
   installations A and B for running hours of 1, 4 and 24 per day (figure D1), disk sizing with a stated
   margin and retention cases, and keeping the first run of each rope for its life; what to ask the supplier
   of a commercial process data acquisition system. A block diagram as text or simple SVG if figkit allows.
6. The outside answers (after 1–5): each in ten lines; a table of where the three agree, where they differ,
   and where they differ from your own numbers by more than 10 % (find out who is right, with the arithmetic);
   the disagreements listed for the owner, not resolved by you. Save the three answers unchanged in
   `answers/`, after running scan_tree on them (they are blind; if a hit appears, stop and report).
7. Figures in the plot standard (plotstandard.py + figkit.py in `max/sws/3d/groove_plots/`; every figure
   passes `check`; research type HTML + PNG; N1 and S2 also as presentation type). Legends short.
8. Note `transmitter_line.md`, easy-read first: ten plain sentences, the block diagram, one table "the line in
   numbers" (rates, bytes, bits per second, storage, buffer, disk), figures N1, S2 and D1; then the dense part,
   the comparison with the outside answers, assumptions, the questions for the owner in order, not done.
9. One fresh subagent as falsifier (files only): arithmetic; every data-sheet number against its sheet; units
   (bit/byte, µT/mT, per second/per mm); filters (droop numbers recomputed independently); nothing firmer than
   its source; names; a cold reader says what N1 and S2 show. Fix; second pass only if blocking.
Hand back at most 16 lines: tip; the existing code and what it lacks; the noise curve in three numbers and the
range of converter rate and line rate that holds; the averaging rule; position without encoder: expected
accuracy and what breaks it; the frame and serial load; the box buffer; storage and disk for A and B; what the
three outside models agree and differ on; full paths of the figures; the five most important questions for the
owner; falsifier verdict; scans; not verified.
Do not hand back while background work of your own is still running. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). If a permission is denied, stop and
report it; do not ask anyone to do the action for you. Sign with your name. — Kai

## U110 — the transmitter line as a running beta: simulator, half, line, box, logger (Kai, 19 Nov evening; owner's go given)

The owner wants the line not only as theory: the code and a running simulator, as a beta, part of the SWS
digital twin. His words: "do this task completely as beta"; "if we cannot generate data quick enough we create
tables"; a rope 250 m long, ramp 1 second. Decided by the owner: Python first, the half in C later. Rope speed:
3.2 m/min is the normal case on the 52 mm rope (platform 0.4 m/min × 8), 5 m/min the fast test case; a setting.
The task note the owner has is C:/Users/stian/secretary/inbox/2026-11-19_transmitter_beta_task.md — read it
first; it is the contract for what the beta is and what it must prove. Then read, on the base branch:
`max/sws/transmitter/transmitter_line.md`, `line_calc.py`, `source.md` (the frame, the filter, the rules, the
numbers), `max/sws/data-path/data_path.md`, and C:/Users/stian/agent-notes/luff.md and foresail.md.
There is NO existing code for any part of the line: you start from nothing.
`git worktree add C:/Users/stian/Prosjekter-u110 -b u110-line-beta aa1eae5` from C:/Users/stian/Prosjekter-u05
(aa1eae5 = tip of u109-transmitter-line; verify, stop if it differs). Another builder works in
C:/Users/stian/Prosjekter-u107: do not touch it. Timebox 300 minutes; past it, stop and report what runs.
Rules as "## U101" COMMON: ADD files only, in a new folder `max/sws/line_beta/`; change no existing file; scans
0 before each commit (idscan on added lines, range aa1eae5..HEAD, and scan_tree); no personal names, roles or
dates; no customer, site or installation names; commit on the branch; no merge to main, no push, no export.
Nothing is "selected / chosen / decided / optimal" by you: everything the task note lists as not settled is a
SETTING in one settings file, with the starting value from transmitter_line.md and the alternatives beside it.
Names: SWS, head, half, element (radial / axial), channel, root box (the owner's "transmitter").
Environment: Python from a NEW virtual environment inside the worktree (not committed; `.gitignore` it within
your folder); packages by pip only, few and common (numpy; a plotting library as the plot helpers need; an
MQTT client; pytest). NO system installs, no services, no admin rights, nothing outside localhost, no outside
model or web service. If a pip-installable MQTT broker works, use it; if not, put the transport behind one small
interface, ship a stand-in that runs in-process or over a local socket, keep the MQTT adapter as real code
with its test skipped when no broker is there, and say so plainly. Web lookups: library documentation only.
Build in this order; each stage ends with its tests passing and a commit, so a stop at any point leaves
something that runs:
1. `settings`: one file (rope length 250 m, ramp 1 s, speed 3.2 and 5 m/min, strand pitch, elements 16 per
   half, converter rate, line rate 250 per second, frame every 100 ms, filter type, serial rate, box per winch
   or per head, buffer length, topics, noise, drift, hum). Every piece reads it; nothing is hard-coded.
2. `rope_sim` (the twin's signal source): a rope with strand ripple; faults at known positions (types and
   positions in the style of `sws/procedures/test_rope_52mm_fault_list.md` on branch u84-test-rope,
   `git show 4c8511c:max/sws/procedures/test_rope_52mm_fault_list.md`; scaled to the 250 m rope); stretches
   with loss of metal; element noise, slow drift, temperature, mains hum with harmonics; a motion profile
   (ramp, run, ramp, out and back over the fixed length, with standstill before, between and after). Output:
   what each of the 32 elements of one head reads, as converter counts, in chunks. Signal sizes from the
   repo's own numbers (`max/sws/3d/falsify/g_large_box.md` for the level per 1 %, `d_measurement_chain.md` and
   `c_third_dimension.md` for one broken wire); where the repo has no number, an assumed one, marked assumed.
   Two modes: generated in chunks, and read from tables made beforehand. It must run much faster than real time
   (a 250 m pass is 78 minutes at 3.2 m/min): measure and report the speed-up; if the full converter rate is
   too slow, generate at a lower converter rate or from tables and say what that changes.
3. `half`: converter counts in; the decimation filter (the proper filter and the block average, both, as a
   setting) down to the line rate; the frame every 100 ms exactly as transmitter_line.md lays it out (header,
   counter, time, status, 25 × 16 × 3 bytes, CRC-32C). No high-pass, no offset removal. Written as plain
   functions on integer arrays so that the same logic can be carried to C later; a short note says which
   parts map one to one.
4. `line`: a simulated serial line: the chosen bit rate as a real limit (bytes per second), start/stop bits
   counted, and switches to drop or corrupt frames, break the line, and restart a half.
5. `root_box`: receives two halves (four for a winch with two heads), checks CRC and counters, counts every
   loss, time-stamps, buffers to disk when the network is down, forwards frames unchanged over the transport,
   publishes health. Real code meant to run later on a small industrial computer.
6. `logger`: receives, stores each run as files in an open, documented format (raw frames plus an index),
   detects "moving" from the data alone, rebuilds rope position from the strand ripple, the ramps and the fixed
   length, registers a run to the first run, and writes per-run results.
7. `run_beta`: ONE command starts everything on this PC for one head (and with a switch for 6 and for 102
   heads, the latter from tables or at reduced detail), runs a lift out and back faster than real time, prints
   a live status line (frames per second, bytes per second, lost frames, buffer level, disk used), and at the
   end writes a run report and the plots. Fault tests as one-line switches: drop frames, break a line, stop
   the network for a set time, restart a half.
8. Proof, as automated tests with a pass figure each (provisional figures; say that the owner sets them):
   a 10 mm fault at 5 m/min arrives with at least 95 % of its peak; a slow drift put in is recovered at the
   logger within 2 %; 50 Hz hum and its harmonics put in do not appear as a level change above a stated
   figure; position from the data alone within 10 mm after registration over 250 m out and back (and say what
   it is before registration); no frame is lost silently (injected losses = counted losses); the box rides
   through a network stop of 10 simulated minutes without losing a frame; measured traffic and storage agree
   with line_calc.py within 5 %. A test that fails stays failing and is reported; do not loosen a figure to
   pass.
9. Plots after a run, in the plot standard (plotstandard.py + figkit.py in `max/sws/3d/groove_plots/`; every
   figure passes `check`): B1 a fault as the logger saw it against what the simulator put in; B2 position
   error along the rope; B3 traffic measured against calculated; B4 the drift put in against the drift
   recovered. Research type, HTML + PNG.
10. `README.md`, easy-read first: what it is in five sentences; how to start it (the exact commands, from an
    empty checkout, including making the virtual environment); what you see; the settings table; the proof
    table (test, figure, result); what is simulated and what is real code; what is not done.
11. One fresh subagent as reviewer (files only; it also runs the commands in the README from scratch in a
    second empty folder): does it start as written; do the tests pass; is any figure loosened; any high-pass
    or offset removal hidden in the half or the box; frame layout against transmitter_line.md; names; a cold
    reader says what B1 shows. Fix; second pass only if blocking.
Hand back at most 16 lines: tip; what runs with the one command and the exact command; speed-up against real
time; the proof table (pass or fail with the number); whether MQTT is real or a stand-in and why; measured
traffic and storage against calculated; position accuracy before and after registration; what is simulated
only; full paths of B1–B4 and of the README; reviewer verdict; scans; not done.
Do not hand back while background work of your own is still running. Notes in
C:/Users/stian/agent-notes/<nautical name>.md (a name not in that folder). If a permission is denied, stop and
report it; do not ask anyone to do the action for you. Sign with your name. — Kai
