# HMI round 1: how to show 51 ropes, 102 SWS and 204 halves

Four outside models were given the same blind brief ([brief.md](brief.md)) and answered alone. Nothing here is
chosen; the owner chooses. Their answers are in [answers/](answers/), the mock-ups in [mockups/](mockups/).

The Grok slot was rerun with grok-4.7-xhigh, pinned by exact name ([models_grok_rerun.yaml](models_grok_rerun.yaml)),
on the same brief unchanged; the first Grok answer is withdrawn as an out-of-date model.

## In ten sentences

1. Four models answered: Claude Opus, Grok, GPT Codex and GPT Sol; none failed.
2. All four keep local faults (LD) and loss of metal (LMA) apart on every screen, as the brief asked.
3. All four lay the rope out along one position axis, in separate lanes for faults, loss of metal, bending cycles
   and change since the first run.
4. All four keep raw channels off the overview and reach them in three or four clicks: rope, SWS, half, channel.
5. All four keep the existing zoom view as one view among several; none makes it the first page, which is the
   overview of all ropes.
6. They differ most on the overview: Opus and Grok use three fixed columns of 17 ropes, Codex and Sol a grid of
   cards.
7. The Opus and Grok mock-ups show all 51 ropes and both SWS of each at once on a 1366 x 768 screen; Codex and
   Sol are cut at the bottom at that size.
8. Opus, Grok and Sol keep the rope's condition and the monitoring's health as two separate marks; Codex puts
   them on one scale.
9. None of them proposes how fatigue is worked out; Opus leaves it blank, the other three show invented numbers;
   in Grok's mock-up that number does not set the rope's level, in Codex's and Sol's it alone can raise it.
10. Each built plain HTML, CSS and SVG with no library; only Opus named a standard and a font to embed, as options.

## Side by side

| | Claude Opus | Grok (Cursor) | GPT Codex (Cursor) | GPT Sol (Cursor) |
|---|---|---|---|---|
| Model that ran | claude-opus-5-5 | grok-4.7-xhigh | gpt-5.3-codex-high | gpt-5.6-sol-high |
| Role it adds | monitoring technician; a person who signs a discard decision | none: the three roles cover the daily work; a person who only signs a replacement uses the overview and the rope view | maintenance planner / asset manager | inspection authority |
| Views proposed | 7: overview, rope, findings list, SWS and half, channel, system map (the zoom view), log | 5: fleet, rope, place (the zoom view, down to one half), channels, attention (what is not quiet, with a reason) | 6: fleet overview, zoom map, rope detail, SWS pair, half and channel, alarm timeline and audit | 7: fleet overview, installation zoom, rope, run comparison, SWS, half and channels, notifications and health log |
| Overview, per rope | state mark; worst LD (% in 6 d); max LMA; change since first run (points); max bending cycles; fatigue column (empty); SWS A and B marks; days since last run | rope level; equipment state; a mark for SWS A and B; fatigue placeholder; drift (largest LMA rise since the first run, in points, and the count of local faults not on the first run); cycles of the busiest section | state badge; fatigue; drift; cycles; LMA max; SWS-A and SWS-B state | condition; SWS A and B health; fatigue ("experimental"); LD change; LMA change; cycles; age of last run |
| How a concern stands out | shape + colour mark, solid or dotted edge band, the cell that caused it boxed, "needs a look" chips at the top; rows in fixed winch order | word, shape, colour and a coloured edge; fixed places; counts per level at the top; a switch may list concerns first, with Unknown beside the top level | grid sorted by severity, coloured border, text badge (CRIT, WARN, ...) | coloured edge, symbol and word on the card; a filter may make a separate list, sorting never hides ropes |
| Alarm levels | rope: Concern, Watch, Normal, Not known; a "not current" flag; monitor health on its own scale (in service, degraded, out of service, no data) | rope: Quiet, Watch, Inspect, Discard guide, Unknown; equipment on its own scale: Sound, Doubt, No data, Out of service | one scale of 5: Critical, Warning, Advisory, Data quality, Out of service | condition: Normal, Watch, Inspect, Rule reached; data health on its own scale (current, stale, missing, out of service) |
| Colour for normal | none (grey dot) | green | green | green |
| Design language reached for | calm grey with colour only for what is abnormal, after the high-performance HMI idea; names ISA-101.01 (sold by ISA, no open licence); system fonts, IBM Plex optional (SIL OFL 1.1); dark theme for the control room, light for the office | light paper-coloured page, dark text, colour only for state; the browser's own interface font; inline SVG; 8 px spacing steps; no font or kit named | dark neutral cards and badges, fixed-width numbers; no product named | restrained high-contrast panels, light theme in the mock-up, tabular numbers; no product named |
| What it alone proposed | thin the data as min/max per pixel; ask whether to keep the reference run after a head is replaced (Sol lists reference-run replacement as an owner decision); no green, no sound, no flashing; the address in the browser holds the place for work orders | an "attention" view listing what is not quiet in ordinary words; a hollow fault head for a fault not on the first run; asks how long a head may be out of service before the rope shows Unknown | an "Advisory" level below Warning; severity-sorted grid (data retention as an owner decision is shared with Grok and Sol) | a run-comparison view that sets any run against the first or the preceding one; no continuous animation of live values |

## Where they agree

- LD and LMA are two measurements and are never merged into one number or one score.
- The rope view has one shared position axis (all four); the first run is drawn behind the latest (Opus, Grok,
  Sol; not in Codex's mock-up).
- Bending cycles sit in the rope view per section (all four); Opus marks them as coming from the winch control
  system, Grok as coming "from the winch".
- Raw channels are not on the overview (all four; temperatures are named as left off by Opus, Grok and Sol).
  Below the SWS view each half shows its 16 sensing elements, one channel each (8 radial, 8 axial); Opus, Grok
  and Sol show the root box in the path down to the half.
- No screen should look like a trip or a stop, because the SWS is not a safety system (Opus, Grok, Sol say so;
  Codex does not take it up).
- Missing data is never shown as normal (all four; Opus adds: never as zero).
- One SWS out of service: Opus and Grok judge the rope on what the other SWS sees, with the blind head marked on
  its own; Codex keeps the rope visible with lower confidence and no escalation from missing data alone; Sol keeps
  a planned out-of-service head visible without repeated notifications, and for missing data keeps the last valid
  state with its time and marks the current state unknown.
- Plain browser technology with nothing fetched from outside; marks carry a shape and a word as well as a colour.
- Channel traces at the finding's position along the rope (Opus, Grok); time traces (Codex); not specified (Sol).
- The owner must settle what "10 % LMA" means (one cross-section or over a length) and the fatigue method (all
  four); the watch levels (all four); who may act on a finding (Opus, Codex, Sol: acknowledge or dismiss; Grok:
  accept a discard guide and order replacement).

## Where they differ

- **Overview form**: three fixed columns of 17, a table (Opus) or two-line rows (Grok); cards 7 across (Codex),
  cards 9 across (Sol).
- **Order**: fixed winch order so a rope never moves (Opus, Grok, with an optional concerns-first switch in
  Grok); sorted by severity (Codex).
- **One scale or two**: condition and monitoring health kept apart (Opus, Grok, Sol) or on one scale (Codex).
- **Fatigue**: left blank until a method exists (Opus); an invented index with its formula printed, not setting
  the level (Grok); 0–100 without a unit (Codex); a % labelled experimental (Sol).
- **Drift on the overview**: change since the first run in percentage points of LMA (Opus); LMA rise and new
  local faults as two figures (Grok, Sol); one "Drift %" figure whose basis the card does not say (Codex).
- **Normal colour**: grey (Opus) or green (the other three). Theme: dark (Opus, Codex), light (Grok, Sol).
- **The zoom view**: the technician's map only, possibly dropped (Opus); a "place" view from the installation
  down to a half, opened from an SWS name (Grok); an alternate entry (Codex); kept, with condition and data health
  shown apart (Sol).

## What none of them covered

Checked against the owner's list: all SWS at a glance, fatigue, drift from the start, bending cycles from
control-system data, zoom from system to one half.

- **All SWS at a glance**: covered by all four (an A and a B mark per rope).
- **Fatigue**: none proposes a method; all give it a place and name inputs. Opus and Sol give the longest
  lists: Opus bending cycles per section, rope make-up, sheave sizes and reverse bends, loads, LD and LMA findings,
  a chosen model with an owner; Sol an approved formula, bending-cycle history, section position, load assumptions,
  SWS findings, uncertainty and validation.
- **Drift from the start**: covered by all four, in the overview and in the rope view.
- **Bending cycles from control-system data**: covered by all four. On this system the control system calculates
  them and writes them to a server; the SWS writes its data to the same server; the screens read both, so the SWS
  needs no link to the control system. None of the four says how the control system's rope sections are lined up
  with the SWS's own position along the rope (Grok's mock-up uses an invented 10 m section).
- **Zoom from system to one half**: all four keep it as a view in the structure; none shows it in its mock-up
  (the brief asked for the overview and the rope view only).

## The mock-ups

All four files were checked before opening (text search for http, //, fetch, XMLHttpRequest, WebSocket, import,
src=, href=, url( and others; [mockups/mockup_check.json](mockups/mockup_check.json), script
[extract_mockups.py](extract_mockups.py)). The hits were in-page links (`#rope/…`), SVG references (`url(#…)`) and
the CSS word `!important`; no file loads anything from outside. All four are clean and were opened in headless Edge.
Sizes: Opus 27.9 kB, Grok 26.7 kB, Codex 15.1 kB, Sol 13.4 kB, all under 300 kB.

Pictures are at 1366 x 768 (overview, then rope view) and at 2560 x 1440 for the overview. The rope view was
opened by the file's own button or card (a one-line click added to a scratch copy, not to the file kept here) or,
for Opus, by its address `#rope/17`.

### Claude Opus

![Opus overview](mockups/claude-claude-opus-5-5.png)
![Opus rope view](mockups/claude-claude-opus-5-5-rope.png)
Large screen: [2560 x 1440](mockups/claude-claude-opus-5-5-2560.png).

- Works: all 51 ropes and both SWS marks fit at 1366 x 768 without scrolling; the cell that caused a concern is
  boxed; the counts and "needs a look" chips sit at the top; text grows on the large screen.
- Works: the rope view has seven lanes on one axis, including which stretch each SWS sees and an LMA-over-time band
  (one row per run); a side panel puts each figure beside its rule.
- Does not: the type is small at 1366 x 768 for a control room, and the SWS A and B dots are faint; the large
  screen leaves about the lower quarter empty; in the rope view the "scale 0–6 pp" label sits on the 5 pp watch
  line; the LMA-over-time band is low in contrast; watch levels are placeholders.

### Grok

![Grok overview](mockups/cursor-grok-4.7-xhigh.png)
![Grok rope view](mockups/cursor-grok-4.7-xhigh-rope.png)
Large screen: [2560 x 1440](mockups/cursor-grok-4.7-xhigh-2560.png).

- Works: all 51 ropes and the A and B marks fit at 1366 x 768 in three fixed columns; each row carries a rope
  level and a separate equipment word (Sound, Doubt, Out of service, No data); counts per level at the top; a
  caption says fatigue does not set the level, and the code bears that out (a rope with fatigue 82 stays Quiet).
- Works: the rope view has four bands on one 0–250 m axis with end switches, numbered vertical scales, the first
  run in grey behind the selected run, and buttons for four run dates.
- Does not: the text stays about the same size at 2560 x 1440 and the rows spread out; the fatigue placeholder is
  printed as a number on every row even so; the rope level is worked out from the latest run only, so a rope can
  return to Quiet; the 10 m section width is invented.

### GPT Codex

![Codex overview](mockups/cursor-gpt-5.3-codex-high.png)
![Codex rope view](mockups/cursor-gpt-5.3-codex-high-rope.png)
Large screen: [2560 x 1440](mockups/cursor-gpt-5.3-codex-high-2560.png).

- Works: cards with SWS-A and SWS-B state and a text badge; the rope view separates lanes for LMA, bending cycles
  (a heat strip), LD findings and drift; a rope can be picked from a list.
- Does not: at 1366 x 768 the seventh row of cards is cut at the bottom and the last two cards are below the
  fold; at 2560 x 1440 the page stays a fixed narrow width with small text; the grid re-sorts by severity, so a
  rope's place changes; the invented fatigue figure is shown without a placeholder label and alone sets CRIT (85
  or more) or WARN (70 or more); lane labels overlap the plot ("Bending cyc…"); the drift lane, a value per run,
  is drawn on the position axis.

### GPT Sol

![Sol overview](mockups/cursor-gpt-5.6-sol-high.png)
![Sol rope view](mockups/cursor-gpt-5.6-sol-high-rope.png)
Large screen: [2560 x 1440](mockups/cursor-gpt-5.6-sol-high-2560.png).

- Works: condition word and symbol on every card, separate data-health ticks per SWS; the rope view marks the end
  switches, has a coverage line for SWS A and B (health ticks, no positions), and puts LMA and LD trends over
  runs in two separate charts below.
- Does not: at 1366 x 768 the fifth row is cut, the footer text runs over it and the sixth row (R46–R51) is
  below the fold; "Rule reached" is clipped on its card; at 2560 x 1440 the cards are tall with empty middles;
  the invented fatigue figure ("experimental" in the rope view) alone sets Inspect (90 or more) or Watch (75 or
  more); the page shows its own source labels to the user ("BRIEF = input.md", "DEMO").

## The owner's decisions

1. Which roles are served, and whether one of the added roles (monitoring technician, planner, inspection
   authority) is real here.
2. The overview form: table, rows or cards; and fixed winch order or sorted by severity.
3. One alarm scale, or rope condition and monitoring health kept apart.
4. The number of condition levels and their names, and whether normal is green or grey.
5. What "10 % LMA" means: at one cross-section or over a length, and which length.
6. The watch levels below the discard rules.
7. The fatigue method and who owns it; until then, a blank or a placeholder figure.
8. Which "drift" figure goes on the overview (LMA change, LD change, or both).
9. How the control system's rope sections (bending cycles, read from the shared server) line up with the SWS's
   position along the rope.
10. The zoom view's place: daily path, technician's map, or dropped.
11. Who may acknowledge, dismiss a finding, change the reference run or put a head out of service.
12. Dark or light theme, and the large-screen layout.
