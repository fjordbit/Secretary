# HMI round 2: the round-1 Opus design in the OpenBridge look, with findings that do not forget

One outside model, Claude Opus (claude-opus-5-5, the same model as round 1), was given a blind brief
([brief.md](brief.md)) with its own round-1 answer and mock-up attached ([sent/](sent/)). Nothing here is chosen;
the owner chooses. The answer is in [answers/](answers/), the mock-up and pictures in [mockups/](mockups/).

## In eight sentences

1. Opus kept its round-1 structure and rebuilt the overview and the rope view with OpenBridge's colours, in all
   four of its palettes (day, dusk, night, bright), switchable on the page.
2. Its advice is to use OpenBridge's colours as a palette, but not its components and not its alarm meanings.
3. It marks a rope concern in warning orange, not alarm red, because a concern means "plan an inspection", and the
   page has a switch to show red instead for comparison.
4. In its state logic the finding is what is kept for good: a rope with an active finding stays in Concern until
   every active finding is dismissed with evidence, or the rope is replaced.
5. Acknowledging only removes the "new" tag, losing data never improves a rope's state, and a finding not seen
   again is flagged for review, not cleared.
6. It dropped from the overview every number that serves no decision: change since the first run, peak bending
   cycles and the empty fatigue column; the first two stay on the rope view as context, and fatigue there is an
   empty band labelled "no method yet".
7. The mock-up shows all 51 ropes and both SWS of each at 1366 x 768, uses the colour values from the brief
   exactly, and loads nothing from outside.
8. Open for the owner: orange or red and the word "alarm" or "concern", watch levels, who may dismiss, the
   licence, and how the control system's rope sections line up with SWS position.

## What Opus thinks of OpenBridge here (its words, shortened)

- **Gives:** a published set of palettes, including dark and night ones; alert colours paired with text colours;
  one type family; neutral panels that suit its round-1 rule of calm grey, with colour only for what is
  abnormal; and possibly a look that people used to bridge screens already know (it marks this unchecked).
- **Costs:**
  - The licence: the code is AGPL for each version's first 180 days, then also Apache-2.0, and a commercial
    licence is for project members only. Its ways round this: use versions older than 180 days, become a member,
    or re-create only the look from the tokens, as the mock-up does. It says to ask a lawyer before shipping.
  - The meaning: on a bridge an alarm calls for immediate action and blinks until it is acknowledged. A rope
    concern means "plan an inspection" and the SWS is not a safety system, so red and blinking would overstate
    it and compete with real alarms in the room. It uses warning orange, no blinking and no sound.
  - Four palettes follow a bridge's light from sun to night; a control room with steady light probably needs
    day or dusk only.
  - Upkeep: a hand-made copy of the look must follow OpenBridge's changes by hand.
- **Fit with round 1:** calm grey and no green fit. OpenBridge has one alert ladder; Opus keeps monitoring
  health off it, on its "low integrity" colour, and says it has not read what that colour is defined for.
- **Kept from round 1 regardless:** two separate scales, missing data never drawn as zero, one shared position
  axis, winch order, a word with every mark, no sound and no blinking.
- **Where it disagrees:** OpenBridge is worth it if the same staff use other OpenBridge screens; if not, its
  round-1 palette "serves equally well and raises no licence question".

## The state table (from the answer, shortened)

| Rope state | What puts it there | What takes it out | Who | What is recorded |
|---|---|---|---|---|
| Normal | first run of a new rope; the last active finding dismissed; data returns after Not known | a finding | system | run, time |
| Concern | an active finding at a discard rule | every active finding dismissed, or the rope replaced; not acknowledgement, not data loss, not a lower reading | dismiss: rope engineer or expert; replace: recorded by maintenance, confirmed by the engineer | finding: position, value, run, which SWS; dismissal: reason, evidence, name, role, time; replacement: date, rope serial number, new reference run |
| Not known | no active finding, and both SWS out of service or silent | data returns | out of service is set by the technician | who, why, since when, expected back |
| (Watch) | not active until watch levels are set | as Concern | as Concern | as Concern |

A finding moves through: active and new, then active and acknowledged (anyone on duty; changes no state), then
still active but flagged "for review" if it is not seen in three runs that actually passed its position (the rope
stays Concern; seen again, the flag goes), and dismissed (kept and shown, never deleted). When a rope is replaced, its findings close with the old rope's
identity, read-only, and the new rope starts empty.

On the five proposals in the brief, Opus:
1. accepts, and asks for the person's name in the log as well as the role; reasons from a fixed list that
   matches the owner's two examples; a "head was faulty" dismissal only where the other SWS passed the same
   place and saw nothing; a dismissed finding that comes back at the same place is a new finding, linked to the
   old one;
2. accepts: acknowledging removes "new" and nothing else;
3. accepts with a change: count only runs in which an SWS passed the place; "not seen" is never a reason to
   dismiss on its own: the review either keeps the finding or arranges an approved check; a finding that fades
   may mean a head has lost sensitivity, so the technician sees the flag;
4. changes it: the number of findings recorded and each active finding's worst value never go down, but the
   rope's worst over active findings drops when a finding is dismissed, otherwise a dismissal would mean nothing;
   the latest reading is shown beside the worst value, labelled;
5. accepts and extends it: Not known only ever replaces Normal; a rope with an active finding keeps its state
   through any loss of data.

Not applicable: Opus lists "what starts a new rope identity: replacement only, or re-termination too" as an
owner decision. On these winches a rope is never shortened or re-terminated (the owner's word), so replacement is
the only way; the state table above does not use re-termination.

## Bending cycles and missing sources

The brief gave the owner's data note: the control system calculates the bending cycles and writes them to a
server; the SWS writes its data to the same server; the screens read both. The SWS has no link to the control
system and needs none. Opus keeps each source with its own time stamp: late control-system data is shown as of
its time, in outline, never extrapolated; no data yet (a new rope) is a hatched band "no data", never zero. Until
the alignment is agreed, the mock-up draws the control system's sections 1:1 on SWS position and labels them
"alignment not agreed".

## Round 1 against round 2

Round 1 (one dark palette):

![Round 1 overview](../round_1/mockups/claude-claude-opus-5-5.png)
![Round 1 rope view](../round_1/mockups/claude-claude-opus-5-5-rope.png)

Round 2, day (light) and dusk (dark), overview and the same rope W17:

![Round 2 overview, day](mockups/r2-overview-day.png)
![Round 2 overview, dusk](mockups/r2-overview-dusk.png)
![Round 2 rope view W17, day](mockups/r2-rope17-day.png)
![Round 2 rope view W17, dusk](mockups/r2-rope17-dusk.png)

Also: [night](mockups/r2-overview-night.png), [bright](mockups/r2-overview-bright.png); large screen
[day](mockups/r2-overview-day-2560.png) and [dusk](mockups/r2-overview-dusk-2560.png) at 2560 x 1440; rope
views for [W09, replaced last month](mockups/r2-rope9-day.png), [W22, finding dismissed after a faulty sensing
element was replaced](mockups/r2-rope22-day.png), [W41, finding dismissed after an inspector's separate rope
test and a recalibration](mockups/r2-rope41-day.png) and [W45, finding for review](mockups/r2-rope45-day.png).

Observations, not a ranking:
- What changed: the overview lost three columns (change since first run, bending cycles, fatigue); a second
  summary line shows how many SWS and winches are delivering data; "needs a look" now also lists a rope that
  neither SWS can see; the rope view's findings table gained a status (active, acknowledged, for review,
  dismissed), and a record of events and a "Dismiss a finding" button were added.
- Works: all 51 ropes and both SWS marks fit at 1366 x 768 in every palette; the rope W17 stays Concern with
  its finding acknowledged long ago and SWS B silent; W09 shows its old rope's record closed and a hatched band
  "no data from the winch control system" instead of zero; W22 and W41 show their dismissed findings with
  reason, evidence and role.
- Does not: at 1366 x 768 the overview leaves about the lower third of the screen empty while the type stays
  small; at 2560 x 1440 it fills about two-thirds of the height; in the rope view the right-hand record runs
  below the screen edge, and on W45 and W41 the finding's label runs over the discard-rule label; the night palette's orange text on near-black looks dim in the picture (contrast not measured); the
  rope is drawn to 290 m with SWS stretches 0–250 m and 40–290 m, both invented in round 1.

## Check of its OpenBridge values against what was verified

The mock-up defines its colours per palette on `data-obc-theme`, the attribute OpenBridge uses.

| What | Verified (brief) | In the mock-up |
|---|---|---|
| Panel, sub-panel, backdrop, text, secondary text, outline, highlight: all four palettes | values in brief section 1 | agrees, every value |
| Alarm, warning, caution and their text colours: all four palettes | values in brief section 1 | agrees, every value |
| Alarm and warning inactive backgrounds; low-integrity border | values in brief section 1 | agrees, every value |
| Critical, running, success | defined by OpenBridge | not used, by choice (no green for normal; no magenta) |
| Font "Noto Sans", not loaded | named by OpenBridge | agrees: named first, system sans-serif behind it |
| Type scale in fixed px steps | 11.5 / 16.5 / 23 / 34 / 45.5 px | differs: text scales with screen width, as in round 1, by choice |
| Alert icon shapes | not verified | its own marks, said so on the page |
| Blinking for unacknowledged alerts | timing tokens exist, values not read | differs: no blinking, by choice |
| Concern colour | (meaning not given by OpenBridge for this use) | warning orange; alarm red on a switch |

## The licence

Read in the project's public code repository, file `LICENSE.txt` on its `develop` branch
(https://github.com/Ocean-Industries-Concept-Lab/openbridge-webcomponents/blob/develop/LICENSE.txt): each version
or commit is licensed AGPL-3.0-only, and becomes available also under Apache-2.0 180 days after it was first made
public; before that date a commercial licence is offered to members of the project. **Plainly: for its first
180 days each version is under AGPL only. A closed commercial product built on such a version would need the
commercial licence or would have to meet the AGPL's terms; after 180 days the Apache-2.0 terms are also
available.** That reading is mine, not legal advice; Opus says to ask a lawyer before shipping, and its remark
that AGPL obliges offering the source to users over a network is, in its own words, from memory. The licence text does not say whether the colour tokens, icons or font are
licensed separately; that was not found. The mock-up copies no OpenBridge code; it re-creates the look from the
colour values.

## The owner's decisions that remain

1. Concern in warning orange or alarm red, and whether it is called "alarm" or "concern".
2. Watch levels, or no Watch state at all.
3. Who may dismiss a finding, and whether dismissing a Concern needs a second person.
4. The fixed list of dismissal reasons and the evidence each needs (the owner's two examples as the start).
5. How close two findings must be to count as one, and how many runs before "for review".
6. Licence: whether the colour values may be used as they are, and whether the components would ever be used.
7. Which palettes the control room needs.
8. How the control system's rope sections (bending cycles, read from the shared server) line up with SWS
   position along the rope.
9. How many days before "not current"; the fatigue method and who owns it.
