# PROPOSAL — a section "MAx platform and way of working" for the Progress plan page

Status: proposed text only, for the owner to read. Nothing here is on the page or in the repository.
Style follows the page's record (topic, when, what, result) and plan (task, state).
Items marked **[S]** describe how the work with AI is done; see part (c) before any of them is used.

## (a) Done, in plain words

| Topic | When | What | Result |
|---|---|---|---|
| Platform core | 22 Oct | The platform's starting structure brought onto the development machine | older duplicate folders moved to the archive |
| Platform core | 29 Oct | Foundation: one way to call every model supplier, and a fixed run log | a new supplier is one file and one line |
| Platform core | 2 Nov | Trial backend on existing subscriptions, with the data boundary probed | no file read outside the exchange folder; names masked and put back [S] |
| Platform core | 2 Nov | Rule engine: the first rules as plain programmed checks | failure-mode and network inputs are demonstration data for now |
| Platform core | 3 Nov | Run loop with review findings sorted by severity and a retry ladder | every outcome reaches a person |
| Platform core | 3 Nov | Start guide for colleagues in three levels, tried from a fresh copy | three install problems found and fixed |
| Platform core | 3 Nov | A check before every run: suppliers reachable and signed in, documents and rules in place | the run cannot start while a lamp is red or amber |
| Platform core | 4 Nov | Flow driver: the drawn chart is what runs | a recorded run replays on its own chart, 100 of 100 events |
| Platform core | 7 Nov | Review policy as one setting on the chart, per flow | no hidden policy file left |
| Platform core | 7 Nov | Front-door documents brought up to date; placeholder checks shown openly | shown in the pre-run check and in the flow view |
| Platform core | 9 Nov | The design brief passed on to the reviewer and the judge in the writer flow | checked in every later run of that flow |
| Flow view | 31 Oct | Flow view with a shared drawing kernel and a choice of module (agent work or twin) | both modules draw |
| Flow view | 1 Nov | Shiplift chart with zoom from the whole plant down to the channels, and a simple 3D view linked to it | demonstration values; scale still an early estimate |
| Flow view | 2 Nov | Zoom on one canvas: each level opens in place | text never under 11 px; 19 channels readable at the level of one half |
| Flow view | 3 Nov | Live view of a run on the flow view | a recorded run can be watched again |
| Flow view | 4 Nov | Card for each agent in the zoom: supplier, model, settings, rules, tools | read only |
| Flow view | 7 Nov | Automatic line layout | no line through a block (105 → 0 on the default flow); crossings 85 → 30 |
| Digital twin, first design | 30 Oct | One chart format for the platform and the twin; design index for the twin | design only, no twin program at that time |
| Digital twin, first design | 1 Nov | Simple shiplift test model from first principles | energy residual 0.001 %; nine hand calculations agree |
| Digital twin, first design | 1 Nov | Delivery milestones for the platform and the twin put forward | first one (flow view demonstration) built; chart format and demonstration script still open |
| Tests and runs | 4 Nov | Two function tests of the default flow, end to end | both stopped for a person as designed, after 2 min 22 s and 2 min 33 s |
| Tests and runs | 7 Nov | A run of the flow on the real record, to check the state of the SWS | stopped for a person; five points beyond the other checks |
| Tests and runs | 9 Nov | The writer flow used to check two team pages | a missing connection in the flow found and closed |
| Way of working | 22–30 Oct | Working rules: look before creating, check before every save to the history, read before asking, every work session names itself | in the platform's rule file [S] |
| Way of working | 29 Oct | One working copy per task; a notes channel between work sessions | in use since [S] |
| Way of working | 3 Nov | Builds checked against their design before release, not only against their tests | in use since [S] |
| Way of working | 7 Nov | "Read the record, build to it, prove it": every task description and every report checked by a second reader | in the platform's rule file [S] |
| Way of working | 9–10 Nov | Start file for restarts; a cold reader before any page goes out | in use since [S] |
| Way of working | 16 Nov | The method packaged as a small shared repository for colleagues | one brief to several reviewers; method files; tests [S] |
| Outside reviews | 8 Nov | Review rounds: one brief to several outside models, names masked and the bundle scanned before it leaves | masked answers kept in the project, unmasked copies kept private [S] |
| Outside reviews | 8 Nov | Which model suits which kind of task, and short instructions per model | proposed levels written down [S] |
| Outside reviews | 10–20 Nov | Briefs for outside rounds written blind: requirements only, no parts, no names | every brief scanned before sending [S] |
| Outside reviews | 25 Nov | Limits on outside programs working on raw data tested | where they did not hold, the outside model wrote scripts and they were run here [S] |
| Release and backup | 25 Oct – 9 Nov | Release route: names replaced by placeholders, a scan, then a forward-only push to the private repository | history cleaned of names on 4 Nov [S] |
| Other work | 9 Sep | Five-project portfolio written: vessel database, agentic proof of concept on bilge support arms, platform and data governance, knowledge base, controls and virtual twin | strategy paper and briefs |
| Other work | 8 Sep, 2–7 Nov | Bilge support arms as the first engineering case for the flow | sizing rules found already encoded in the design models; flow proposed for after the SWS paper |
| Other work | 16–18 Nov | Ship database: first design and a review reply to its product owner. **Owner to rule: keep between the owner and the colleague continuing it, or show.** | handed over to a colleague to continue, under the owner's supervision |
| Release and backup | 3 Nov, 19 Nov | Backups: every work line copied to a private backup line that does not build | in use since |

## (b) Open tasks, loose (no forced dates)

The SWS work for the current customer comes before all of this, and has priority until its parts are ordered
(order gate 15 Dec). The interface (API) work is closed until next year. (Both lines as given in the request
for this section; neither is in the logs: the record has "SWS first" and the order date 15 Dec.) The work below is still there and
waits behind both; next steps are loose.

Where the other work stands:
- Bilge support arms: the case is described; the flow for it waits for ready models and the design team's input.
  Next: the flow after the SWS paper.
- Ship database: first design and review reply done; continued by a colleague under the owner's supervision.
  Next: the colleague's first skeleton. (Owner to rule whether this line is shown.)
- Further plan for the flow: the SWS paper and a recap of the SWS documents through the flow; documentation at
  three reading levels; a review round run inside the flow; later the spare-parts / warranty case and code cases.

Open tasks for the platform:

- Document flow with a reading level as a setting (paper, plain).
- Third function test of the flow, recorded as video.
- The SWS paper through the flow; a recap run of all SWS documents through the flow.
- The twin in the flow view: chart counts to the real plant (two sides), communication protocols as boxes at
  the lower zoom, top view and sub views built from the twin's own plant file, twin values shown on the chart.
- Network view switch in the zoom.
- Open design points: chart format version 0.2; core, modules and rule packs; test-model stack; placeholder
  names at the data boundary; whether the reviewer sees the sources.
- Small fixes: a refused setting caught before the run; start a run from a ready-made answer; one failing test.
- A third outside supplier in the flow; a default model per agent type in a side menu.
- A spending limit on paid runs; a separate confined account for outside programs on this machine.
- Clean-up of older published content (names in older reports, one image).
- One home for the repositories; hosting on site with phone access.
- Request for company-paid model accounts, after a demonstration.

## (c) Sensitive: owner to rule

Each item below describes how the work with AI is done. Proposed neutral line beside it, for use if the item is
kept off the page.

| Item in (a) | Why it may be private | Proposed neutral line |
|---|---|---|
| Trial backend, data boundary probed (2 Nov) | names the use of subscriptions and how the boundary is tested | "Trial backend in place; the data boundary is tested." |
| Working rules (22–30 Oct) | the rule set itself | "Working rules for the platform written down." |
| One working copy per task; notes channel (29 Oct) | how parallel work sessions are run | "Parallel work kept apart." |
| Builds checked against their design (3 Nov) | the check method | "Every build is checked before release." |
| "Read the record, build to it, prove it" (7 Nov) | the rule text and the second-reader check | "Work is checked against the record." |
| Start file; cold reader (9–10 Nov) | the hand-over and reading checks | "Pages are read for clarity before they go out." |
| Method packaged for colleagues (16 Nov) | the method as a product | "A small shared tool for colleagues." |
| Review rounds with masking and scan (8 Nov) | the protocol for outside models | "Outside reviews held; no names leave the company." |
| Model suitability and instructions (8 Nov) | which model for which task, and the prompts | "Review set-up prepared." |
| Blind briefs (10–20 Nov) | how briefs are written | "Outside reviews get requirements only." |
| Limits on outside programs, scripts run here (25 Nov) | the confinement protocol | "Raw data stays on this machine." |
| Release route with placeholders and scan (25 Oct – 9 Nov) | the publishing checks | "Releases are scanned for names before they go out." |

Separate from the list above (not about the method): the ship database line in (a) and (b) is marked
**owner to rule: keep between the owner and the colleague continuing it, or show**. Neutral line if shown:
"Ship database: first design done; work continues."

Count: 12 sensitive items, plus the ship database line for a separate ruling.
