# Element run 3: one thin board, the groove, Hall beside TMR

Calculated, not measured (2D axisymmetric model, homogenised rope, placeholder steel and rope curves, large model box);
part figures as read on the makers' data sheets. Head for the 52 mm rope, groove 20 mm wide at the mid-plane, N52 and
N48SH magnets with the rope near 1.97 T. Lift-off is from the rope surface. Nothing here is selected; the outside
expert and the owner decide. Terms: [terms.md](terms.md); figure sources: [source.md](source.md).

**In plain words.**
1. On one thin board across the rope, the radial field lies in the board and the axial field goes through it, so an
   in-plane part reads the radial element and a through-the-package part reads the axial element, both lying flat;
   that is the pairing the working prototype already carries (TMR2185 radial, TMR2584 axial).
2. The radial element sits on the mid-plane, where its own field is near zero; its largest signal is 9.5 mT at 3 mm
   (about 10.7 mT with 0.5 mm off the mid-plane), while 32–42 mT of standing axial field passes through it across its axis (45–52 mT without a groove).
3. The axial element at the groove's zero sits in a field of about ±5 mT from rope, temperature and nearby steel, and
   needs about −16 to +7 mT of range once build tolerances and a 10 % loss are added; without a groove it needs
   −21 to −14 mT.
4. The groove makes every element error smaller in % of metal by about 3.8 times (0.77 against 0.20 mT per 1 % of
   metal at 16 mm), and it puts the axial element near the magnet's temperature null (0.4 % of metal at −40 °C against
   11 % without a groove).
5. For the axial element the Z-axis TMR parts draw 1.1–3.3 mA; the TMR2584's offset moves 0.1 mT over −40 to +50 °C
   (plus 0.2 mT hysteresis: 0.4 % of metal) if its offset figure is a total, but 9 mT if it is per kelvin (12 %); its
   sheet does not say which.
6. The 3.3 V Hall parts have the range and a noise density on the sheet (about 0.016 mT peak to peak in 0–125 Hz,
   derived), but their zero drifts
   0.55–1.0 mT over temperature (0.7–1.3 % of metal with the groove) and they draw 2–8 mA each; the one low-drift Hall
   read (0.08 mT) needs 5 V and 11 mA, and its noise is about 0.26 mT p-p on an assumed gain (`tradeoff.md` §5).
7. No three-axis part read serves both elements of a position: one package sits at one radius; the Hall ones have
   0.11–0.16 mT peak to peak of noise in the board plane, as large as the weakest broken-wire signal (0.11 mT), and the
   three-axis TMR part is specified to ±20 mT against 26–36 mT through it at 5 mm.
8. On spokes the two elements of a position sit 4 mm apart along the rope in the record's layout, and the large axial
   field lies in the radial part's film plane; on the board they share one spot and that field goes through the film.

**The cases for the outside expert, side by side** (nothing picked; per half: 8 radial + 8 axial elements).

| Case | Parts that fit on the sheets | What it gains | What it loses | What the prototype must show to decide | The one number that would rule it out |
|---|---|---|---|---|---|
| **A** TMR radial + Z-axis TMR axial, one board | radial: TMR2185, CT100, TLI55910, TMR2084S (in-plane); axial: TMR2584, TMR2583 (through the package) | the prototype's own pairing; bridges suit a ratiometric converter; about 9–30 mA per half for all 16 (0.03–0.10 W at 3.3 V); TMR2584 offset 0.1 mT + hysteresis 0.2 mT if its figure is a total | axial range specified only to ±20 mT (TMR2584 saturates at ±30 mT): fits the groove (−16 … +7 mT), not the no-groove head (−21 mT); no noise and no long-term drift on the Z-axis TMR sheets; the TMR2584 offset unit is unclear | the axial channel's zero against temperature in the head (−20 … +45 °C at least), and its gain with a small known field at the working point | axial offset change over −40 … +50 °C above 0.77 mT (1 % of metal at the groove's zero) |
| **B** TMR radial + Hall axial, one board | radial as A; axial: DRV5055 A1/Z1, TMAG5253 BA1, A1304 (3.3 V, ratiometric); MLX91377 (5 V, analog); HAL 2455 (PWM) and TLE4998 (SENT) only with another read-out | range and no saturation; noise density on the sheet (0.016–0.017 mT p-p in 0–125 Hz, d); lifetime drift on the sheet; the A1304's ±37.5 mT fits even the no-groove head | zero drift 0.55–1.0 mT over temperature on the 3.3 V parts (0.7–1.3 % of metal with the groove, 2.7–5 % without), so a per-part temperature table is needed to come under 1 %; 16–62 mA for 8 axial parts (0.05–0.2 W); the 0.08 mT part needs 5 V and 88 mA for 8 (0.44 W) and its noise is about 0.26 mT p-p (d, assumed gain) | the Hall zero against temperature, per part, and what remains after a per-part table | residual zero drift after the per-part table above 0.77 mT over −40 … +50 °C |
| **C** one multi-axis part per position | none on the sheets read: TMAG5170, TMAG3001 (digital Hall), TMR2301 (analog 3-axis TMR, 4 × 4 × 2.5 mm) | one part, no pairing of two packages | one radius for both elements (5 mm and 16 mm are 11 mm apart); Hall parts: in-plane noise 0.11–0.16 mT p-p (d) against a 0.11 mT weakest wire, digital outputs do not suit the converters; TMR2301: ±20 mT against 26–36 mT through it at 5 mm | not worth a prototype test on these sheets | Hall: in-plane noise 0.16 mT p-p against the 0.113 mT inner-wire signal at 5 mm; TMR2301: 36 mT against its ±20 mT |
| **S** the same on spokes (the specification's layout, not confirmed) | in-plane TMR for both: radial TMR2185 / CT100; axial TMR2084S (±40 mT), TMR2083S (±50), TMR2151S (±100), TLI55910 (±35) | in-plane parts read both directions flat; wider-range in-plane TMR exists for the axial element (fits without a groove too) | the two elements of a position 4 mm apart along the rope (record) or 3° apart round it (back to back); 31–51 mT of axial field in the radial part's film plane, across its axis (effect disputed in the board round); 18 boards and 16 connectors per head (board round) | the radial part's gain with 30–50 mT in its film plane across its axis | a radial gain change above 10 % with 50 mT across its axis in the film plane |

![Figure E3](fig_e3_board.png)

*Figure E3 ([svg](fig_e3_board.svg)). One half seen along the rope, a section through the mid-plane, and the spoke for
comparison. Drawn to the model's dimensions; board thickness and package sizes assumed.*

![Figure E2](fig_e2_resolved.png)

*Figure E2 ([interactive](fig_e2_resolved.html), [slide](fig_e2_resolved_slide.png)). Axial element: the loss of metal
one element's drift or noise is equal to, against the level per 1 %. The left dotted line is the head without a groove
at 16 mm, the right one the groove with the zero at 16 mm. The TMR2584 line is its best case (offset figure read as a total); read
per kelvin it is 12 % with the groove and 46 % without, off the scale. MLX91377 (0.10 % / 0.40 %) is not drawn.*

Also: Figure E1 for the radial element ([interactive](fig_e1_radial.html), [png](fig_e1_radial.png)) and for the axial
element ([interactive](fig_e1_axial.html), [png](fig_e1_axial.png)).

---

## Dense part

### 1. What each element sees

Head for the 52 mm rope, mid-plane, large box; N52 18.1 mm with the groove for the zero at 13 / 16 / 19 mm (3.58 mm
for 16 mm; rope 1.97 T); N48SH 19.1 mm with the groove for 16 mm (3.92 mm; 1.97 T) beside it. Files:
`../../3d/tradeoff/results/summary.json` and `lines.json` (on file, middle rope curve), `results/fields.json`
(solved here: 38 standing or level solves, all converged in 10–11 Newton steps, 164–252 k nodes). Temperature acts
on the magnet only (register α(Br) −0.12 %/K; the rope and yoke curves are not temperature-dependent in the model);
+50 °C is above the 45 °C service ruling for the magnet and is shown because the brief's range asks for it.
**Radial element** (groove for the zero at 16 mm; N52 / N48SH; mT):

| Lift-off | Along its axis (B_r): standing on the mid-plane | B_r per mm off the mid-plane | Across, through the board (B_z): standing | its spread (min … max) | Across, round the rope | No groove: B_z (cold, −40 °C) | Short ring, peak ΔB_r | One outer-strand wire (3D) | One inner-rope wire (3D) |
|---|---|---|---|---|---|---|---|---|---|
| 3 mm | 0 (read-out ≤ 0.08) | 2.5 / 2.4 | −36.6 / −36.4 | −42.3 … −32.2 / −42.3 … −31.9 | 0 (2D) | −45.0 (−50.9) / −45.9 (−52.2) | 9.51 / 9.47 | 1.95 / 2.36 / 2.46 | 0.158 / 0.346 / 0.464 |
| 5 mm | 0 (≤ 0.04) | 2.9 / 2.9 | −30.7 / −30.5 | −36.2 … −26.3 / −36.3 … −26.1 | 0 | −40.0 (−45.4) / −41.1 (−46.8) | 5.07 / 5.05 | 1.17 / 1.35 / 1.36 | 0.113 / 0.231 / 0.301 |
| 8 mm | 0 (≤ 0.05) | 2.7 / 2.7 | −23.4 / −23.4 | −28.8 … −19.2 / −28.9 … −19.0 | 0 | −34.2 (−38.8) / −35.6 (−40.5) | 2.68 / 2.67 | not on file (about 0.6–0.7, d) | not on file (about 0.06–0.16, d) |

Wire columns: one broken wire, worst position and angle, zero-peak, at 3D rope induction 1.881 / 1.989 / 2.093 T
(`../../3d/falsify/c_third_dimension.md` §2; old box r 300 mm, groove for 16 mm, stranded rope). 8 mm: the 5 mm value ×
the short ring's 8/5 ratio (0.53), derived, not solved. Spread: rope curve low / high, magnet at −40 / +50 °C, magnets
1 % weaker, steel near the head (shell at 10 / 30 mm, tube at r 100 mm, second head at 300 mm). The largest single
terms at 3 mm: low rope curve −5.7, magnet at −40 °C −4.8, mild-steel shell 10 mm outside −2.5 … −2.9, second head
+2.9 … +3.1 mT. Strand ripple (3D, stranded, `../../3d/verification.md`): B_r on the mid-plane not resolved above the
read-out floor (0.06–0.17 mT p-p); B_r 4 mm off the plane 0.32–0.49 mT p-p at 3 mm; B_z at 3 mm 0.15–0.20 mT p-p
(across the radial element's axis).
**Axial element** (each at the zero of its own groove; N52, and N48SH at 16 mm; mT):

| Position (groove) | Along its axis (B_z): standing at the position | its spread (min … max) | of which rope curve low / high | magnet −40 / +50 °C | steel near the head | Across (B_r): on the mid-plane / per mm off it | Round the rope | Level per 1 % (at the zero) | Short ring ΔB_z | One wire (3D, 16 mm only): outer / inner |
|---|---|---|---|---|---|---|---|---|---|---|
| 13 mm (4.34 mm), N52 | +0.45 (zero 12.83 mm) | −5.8 … +5.3 | −6.3 / +4.9 | −0.94 / +0.26 | not solved | 0 / 3.3 | 0 (2D) | −0.881 | −1.60 | — |
| 16 mm (3.58 mm), N52 | +0.09 | −5.3 … +4.5 | −5.4 / +4.4 | −0.31 / +0.05 | −5.2 (shell 10 mm) … +4.4 (second head 300 mm) | 0 / 2.9 | 0 | −0.774 | −1.04 | 0.140–0.158 / 0.031–0.064 |
| 19 mm (2.77 mm), N52 | −0.07 | −3.8 … +3.4 | −3.7 / +3.4 | +0.06 / −0.05 | not solved | 0 / 2.9 | 0 | −0.522 | −0.62 | — |
| 16 mm (3.92 mm), N48SH | +0.09 | −5.8 … +4.7 | −5.6 / +4.6 | −0.35 / +0.05 | −5.9 … +4.6 | 0 / 3.1 | 0 | −0.802 | −1.07 | — |
| no groove, at 16 mm, N52 / N48SH | −16.1 / −17.9 (zero 23.4 / 24.4 mm) | −18.3 … −14.9 / −20.4 … −16.7 | −1.4 / +1.2; −1.5 / +1.2 | −2.2 / +0.85; −2.5 / +1.0 | not solved (g_large_box Table 2, model magnet: −0.34 … +0.81) | 0 / 2.0 | 0 | −0.201 / −0.217 | −0.96 (N52 × 1.0) | 0.14–0.17 (3D-D, no groove) |

What the axial element must hold along its axis (groove for 16 mm, N52): the spread −5.3 … +4.5 mT; build
tolerances (groove depth ±0.1 mm moves the zero ±0.41 mm, element ±0.5 mm: ±0.91 mm × 2.9 mT/mm = ±2.6 mT); a 10 %
loss passing (10 × −0.774 = −7.7 mT): **−15.6 … +7.1 mT**; a 20 % loss: −23.4 mT. Without a groove at 16 mm: −16.1 mT
standing, −18.3 … −14.9 spread, ±1.0 mT build (2.0 mT/mm × 0.5 mm), −2.0 mT for 10 %: **−21.3 … −13.9 mT**; the cold
case alone sits at −18.3 mT. With the zero trimmed in place at installation (as the measurement-chain note proposes), the rope
curve, the build and the steel present then drop out of the groove case: −8.0 … +0.1 mT for a 10 % loss, plus any
steel that moves near the head afterwards (up to about ±5 mT, `g_large_box.md` Table 2).

What the magnet's temperature does to the axial reading, uncorrected (magnet only, from the spread solves): with the
groove −0.31 mT at −40 °C and +0.05 mT at +50 °C, read as +0.40 % and −0.06 % of metal; without a groove −2.21 / +0.85
mT, read as +11.0 % and −4.2 %. The groove's zero sits near the magnet null (magnets 1 % weaker: +0.019 mT at the zero,
+0.284 mT without a groove).

Bandwidth: 0–125 Hz for both channels (spec §7: 1 mm pitch at 15 m/min); the loss-of-metal reading is a standing
(DC) value compared against a base trace taken months earlier.
### 2. The geometry on one thin board

**Where things sit** (head for the 52 mm rope as modelled, `t_net.case`; Figure E3). Rope surface r 26 mm; pole
bore r 30 mm; magnet rings r 32–51.1 mm (N48SH 19.1 mm; N52 18.1 mm: r 32–50.1 mm) at z 50–90 mm on each side; yoke
inner face between the magnets r 51.1 mm (50.1 mm), 25.1 mm (24.1 mm) lift-off. The board lies on the mid-plane, half
way between the magnet faces, which are 100 mm apart: a board of 0.8–1.6 mm plus parts of 0.4–1.5 mm takes a few mm
of that 100 mm and is not limited by it. What limits the board is radial: inner edge against the rope, outer edge
against the yoke face.

| Item | Radius (mm) | Lift-off (mm) | Pitch between the 16 positions (mm, 2π r ÷ 16) |
|---|---|---|---|
| Rope surface (nominal) / at +4 % | 26.0 / 27.0 | 0 / 1.0 | — |
| Radial element at 3 mm (the specification's floor, not a position) | 29.0 | 3 | 11.4 |
| Pole bore | 30.0 | 4 | — |
| Radial element at 5 mm | 31.0 | 5 | 12.2 |
| Radial element at 8 mm | 34.0 | 8 | 13.4 |
| Axial element, zero at 13 / 16 / 19 mm | 39.0 / 42.0 / 45.0 | 13 / 16 / 19 | 15.3 / 16.5 / 17.7 |
| Yoke face, N48SH 19.1 mm / N52 18.1 mm | 51.1 / 50.1 | 25.1 / 24.1 | 20.1 / 19.7 |

- A radial element at 3 mm lies inside the pole bore (r 29 < 30): the board's inner edge then reaches into the free
  bore between the magnets, and the liner there must be smaller than the pole bore (the same conflict
  `../../3d/p52/design.md` §4 records for spokes). At 5 mm (r 31) the element is 1 mm outside the pole bore.
- 8 positions per half at 22.5°, the split mid-way between two positions (11.25° from it), as in the 3D split model
  (`../../3d/falsify/c_third_dimension.md` §1: the split moves the zero by under 0.1 mm, the same at every angle).
- The radial element and the axial element of one position lie on one radius line, 8–16 mm apart radially (5 → 13
  … 8 → 19 mm), at the same angle and on the same mid-plane: they read the same spot of rope at the same moment.
- A half-ring board from about r 30 to r 49.5 mm is 19.5 mm wide radially. Room per position at the radial element:
  12.2 mm of arc at r 31 (5 mm) for the part, its decoupling and its traces.

**Which way each package must sense when it lies flat on the board.** The board's normal points along the rope. The
radial field lies in the board, along the radius; the axial field goes through the board.
- Radial element: a part that senses **in its package plane** (in-plane TMR bridges such as TMR2185, CT100,
  TMR215x), turned so its sensing axis points along the radius. The large standing field (axial, 31–51 mT) then goes
  through the package, perpendicular to the film. A Hall part that senses through its package would read the axial
  field here, not the radial one.
- Axial element: a part that senses **through its package** (Z-axis TMR such as TMR2584; common linear Hall parts
  such as DRV5055, TMAG5253, A1304). The standing field along its axis is near zero at the groove's zero; the field
  across it (radial) is 0 on the mid-plane and 2.5–3.5 mT per mm off it.
- So the prototype's pairing (in-plane TMR2185 radial, Z-axis TMR2584 axial, register) is the pairing this board
  asks for: "mounted in different planes" can be read as two kinds of package, one sensing in its plane and one
  through it, both lying flat.

**If a part only senses the other way** (options with their cost; nothing chosen):

| Option | What it is | Cost in assembly | What it costs the reading |
|---|---|---|---|
| Part flat, other kind of part | in-plane part for radial, through-package part for axial (as above) | none beyond a two-part bill of materials | none; the pairing has to exist on the sheets (section 3) |
| Daughter piece | a small board soldered at right angles to the half-ring, carrying the part | one extra board and two solder rows per position, 16 per head; angle set by a solder joint | tilt: 1° puts 1.7 % of the field across the axis into the reading (0.5–0.9 mT at the radial element, 31–51 mT across) |
| Part on its edge | a leaded or castellated part stood upright | hand or jig assembly; angle held by the leads | as the daughter piece; lead length adds lift-off |
| Flex tail | a flexible tail of the board folded to 90° with the part on it | fold and fix 16 tails; stiffener under each part | fold angle sets the tilt; tails move with temperature |
| 3-axis part | one package reads both directions | none | the package sits at one radius: radial and axial cannot both be at their best lift-off (5 and 16 mm are 11 mm apart) |

**The board and the parts against the gap.** Along the rope there is no squeeze (100 mm between magnet faces). The
squeeze is radial at the radial element: rope at +4 % (1 mm), rope movement 2–3 mm, liner, clearance, die depth
in the package. The record has two stacks for 5 mm (`../sws_sensor_placement.md` §1): liner 1.5 + recess 2.5 + die
1.0, or movement 3 + guard 1 + die 0.7 = 4.7. On the board the die depth is measured in the board's plane, from
the package edge facing the rope to the die (for a leadless part about half the body; not on most sheets), plus the
board-edge keep-out (board maker's figure, not on file). The parts' height (0.4–1.5 mm) is along the rope and does
not add lift-off.

**Protecting the radial elements.** On the prototype the elements had no protection and broke because they sat too
close to the rope. A liner or sleeve between rope and board:
- Non-magnetic, non-conducting (a polymer such as PEEK or a filled polymer, as named in the housing study; or a
  ceramic): costs only its thickness in lift-off. From the on-file 2D signals: near 3–5 mm the short-ring signal falls
  about 27 % per mm, near 5–8 mm about 19 % per mm (9.51 / 5.07 / 2.68 mT at 3 / 5 / 8 mm); the 3D wire signals fall
  23 % per mm (outer-strand wire) and 15 % per mm (inner-rope wire) between 3 and 5 mm. Calculated.
- Non-magnetic, conducting (stainless 316L, aluminium): the same thickness cost, plus eddy currents when the field
  through it changes, i.e. when a fault passes. General physics, not computed here: a thin conducting sleeve passes
  a changing field with a time constant of about μ0 σ t L / 2 (t thickness, L the size of the field pattern, a few mm
  for a short fault up to the sleeve radius). For 1 mm of 316L (σ about 1.35 MS/m) this is under 25 µs, a corner
  above 6 kHz: no loss in 0–125 Hz. For 1 mm of aluminium (σ about 25 MS/m) it is 0.1–0.5 ms, a corner of 0.3–1.5 kHz:
  up to about 7 % of amplitude and a phase lag at 125 Hz, less at lower frequency. Copper or brass would cost more.
  Cold-worked 316 can become slightly magnetic (board round, from memory, not checked); a magnetic liner would move
  the standing field and the zero.
- The 3 mm floor is where the signal is largest and where the parts broke; each mm of protection moves the element
  out by that mm.

**Spokes, for the fair comparison** (the specification's layout, not confirmed; nothing further is built on it).
On a spoke (a board in the plane through the rope's axis) both fields lie in the board: in-plane parts read both
the radial and the axial field flat on it. The record puts the radial element at z = ±4 mm (it reads B_r there,
`../../3d/p52/design.md` §4) and the axial element at z = 0, so the two elements of a position are 4 mm apart along
the rope. Placed back to back at z = 0 instead, they are a board thickness apart round the rope (1.6 mm is 3.0° at
r 31 mm). Against a 10–20 mm local fault: 4 mm is 20–40 % of its length, so the two channels see the fault 4 mm of
rope apart (4 samples at 1 mm pitch, 16 ms at 15 m/min); combining them needs that shift, and a fault shorter than
the shift is seen by one channel while the other sees the rope next to it. On the thin board the two elements of a
position are on the same mid-plane within about a package height (under 1.5 mm). On a spoke the axial field (31–51
mT at the radial element) lies in the film plane across the radial part's axis, the case the board round names as
the one whose effect on an in-plane TMR part is disputed; on the board it goes through the film.

### 3. The parts, as the sheets state them

Builds on `../../3d/tradeoff/tradeoff.md` §5 and `../sws_sensor_candidates.md` §2.2 (not repeated: TMR2151S/2152S,
TMR2083S, DRV5055 A3/A4, TMAG5253 BA4, MLX90251, SS495A, AMR parts). Read for this note by a sheet-reading subagent
with general queries (part numbers only); deciding lines as the sheet prints them. "n/s": not on the sheet; "n/r": not
read; "(d)": derived here. 10 G = 1 mT; 1 Oe ≈ 0.1 mT in air.

**Radial element: parts that sense in the package plane** (lie flat, axis along the radius).

| Part | Sensing direction (sheet's words, short) | Linear range; saturation; absolute maximum | Sensitivity | Noise | Zero offset; offset drift | Sensitivity drift | Hysteresis | Across its axis | Output; supply; current | Package; temperature | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TMR2185 | in the package plane (figure) | ±20 mT specified; ±100 mT saturation; 400 mT | 3.4 mV/V/mT | n/s | ±10 mV/V; drift n/s | −770 ppm/K | 0.03 mT typ | n/s | bridge; 0.5–7 V; 43 kΩ, 77 µA at 3.3 V (d) | SOP8 or LGA4L 2.0 × 1.5 × 0.73 mm; −40…125 °C | on the prototype |
| CT100 | field "into the pin 1 / pin 6 side", along the package | ±20 mT at ±0.5 %; ±50 mT operating; ±200 mT | 4.5 mV/V/mT | 700 nV/√Hz at 10 Hz, 1 V: 0.16 µT/√Hz, 0.012 mT p-p in 0–125 Hz (d) | ±5 mV/V; ±4.0 µV/V/K max (0.9 µT/K, d) | −250 typ, −350 max ppm/K | 0.05 % at ±20 mT | n/s | bridge; 1.0–5.5 V; 0.3 mW at 3 V | SOT23-6, DFN6 1.5 × 1.5 × 0.45 mm; −40…150 °C by option | n/s |
| TLI55910-A6E | "sensing element plane … from pin 5 to pin 2" | ±35 mT on the in-plane magnitude √(Bx² + By²); 75 mT | 4.8 mV/V/mT typ | 5 µV rms typ over 100 kHz (35 max over 1 MHz); density n/s | ±10 mV/V; ±4 µV/V/K (0.8 µT/K, d) | −700 ppm/K typ | ±0.5 % of full scale | n/s; effect of a field through the package not stated | bridge; 1–5.5 V; 0.7 mA at 5 V (8.2 kΩ; about 0.4 mA at 3.3 V, d) | PG-SOT23-6; −40…125 °C | n/s |
| TMR2084S | "parallel to the sensor's sensitive direction" (figure: along the long axis) | ±40 mT; ±100 mT; 400 mT | 6 mV/V/mT | n/s | ±10 mV/V; 0.008 mV/V/K (1.3 µT/K, d) | −1000 ppm/K | 0.2 mT | n/s | bridge; 0.5–7 V; 100 kΩ | SOT23-5; −40…125 °C | n/s |

**Axial element: parts that sense through the package** (lie flat on the board, axis along the rope).

| Part | Sensing direction (sheet's words, short) | Linear range | Sensitivity | Noise | Zero offset; drift over temperature; over life | Sensitivity drift | Hysteresis | Across its axis | Output; supply; current | Package; temperature | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TMR2584 | perpendicular to the chip surface | ±20 mT specified; ±30 mT saturation; 400 mT max | 5 mV/V/mT | n/s | ±10 mV/V (±2 mT, d); "0.5 mV max" over −40…125 °C, unit as printed (total or per K); life n/s | −290 ppm/K | ≤ 0.2 mT | n/s | bridge; 1–7 V; 3 kΩ typ, 1.1 mA at 3.3 V (d) | SOT23-5 2.95 × 1.65 mm, TO94, SSIP4; −40…125 °C | on the prototype |
| TMR2583 | "Perpendicular to the package top-marking surface" | ±20 mT fit; ±100 mT saturation; 400 mT | −1.5 mV/V/mT | n/s | ±10 mV/V; "0.002" with unit printed "mV" (read as mV/V/K: 1.3 µT/K, d); life n/s | −950 ppm/K | 0.2 mT | n/s | bridge; 1–7 V; 1 kΩ, 3.3 mA at 3.3 V (d) | TO94, SSIP4, SOT23-5; −40…125 °C | n/s |
| DRV5055 A1 / Z1 | "perpendicular to the top of the package" | ±21 mT at 5 V (3.3 V figure n/r this pass) | 60 mV/mT at 3.3 V | 215 nT/√Hz at 3.3 V; 0.016 mT p-p in 0–125 Hz (d) | ±60 mV at 3.3 V (±1 mT, d); ±1 % × VCC over −40…125 °C, a band (±0.55 mT, d); life < 0.5 % typ, 1 % max after 1000 h (read as % in this run; recorded as unit unreadable in `tradeoff.md` §5) | +0.12 %/K (A), 0 (Z) | n/s | n/s | ratiometric, single-ended; 3–3.63 V; 2 mA typ | SOT-23, TO-92; −40…125 °C | active (sheet's addendum, on file) |
| TMAG5253 BA1 | "perpendicular to the top of the package" | ±20 mT | 60 mV/mT at 3.3 V | 220 nT/√Hz; 0.016 mT p-p (d) | ±50 mV over −40…125 °C (±0.83 mT, d), ±30 mV over 0…85 °C (±0.5 mT, d); life 10 mV (0.17 mT, d) | +0.12 %/K typ | n/s | n/s | ratiometric; 1.65–3.6 V, enable pin; 2.6 mA typ | X2SON-4 1.4 × 1.1 × 0.4 mm; −40…125 °C | active (on file) |
| A1304-T | branded face (Hall, perpendicular) | ±37.5 mT typ | 40 mV/mT | 0.23 µT/√Hz; 0.017 mT p-p (d) | ±25 mV; ±40 mV typ 25 → 85 °C (±1 mT, d); life: sensitivity ±3 % typ | +0.12 %/K typ | n/s | n/s | ratiometric; 3–3.6 V; 7.7 mA typ | SOT23-W; **−40…85 °C** | n/s |
| MLX91377 (Bz version) | "perpendicular to the IC (i.e. Bz)" | span ±10 / 25 / 40 / 80 mT, programmed | programmed | 2.5 mV rms at ±40 mT span, band n/s | 3.9 LSB12 over the full range at ±40 mT span (about 0.08 mT, d) | ±1.5 % | thermal ±0.5 % of sensitivity | n/s | analog or SENT; 5 V; 11 mA | TSSOP-16, two dies; −40…160 °C | status not confirmed |
| HAL 2455 | "perpendicular to the branded side" | 6–200 mT programmable | programmed | 0.05 % of full scale rms typ | ±0.4 mT unadjusted; ±5 µT/K max (0.45 mT over 90 K, d) | ±1–1.5 % | n/s | n/s | **PWM**; 4.5–5.5 V; 7 mA | TO92UT, SOIC8 | third-party copy of the sheet |
| TLE4998S8 | out of plane (figure) | ±50 / 100 / 200 mT | programmed | ≤ 2 LSB12 rms | ±0.4 mT band incl. lifetime; ±5 µT/K max | ±2 % | 20 µT | n/s | **SENT**; 4.5–5.5 V; 6 mA | PG-TDSO-8; −40…125 °C | n/s |
| A1324 / 5 / 6 | perpendicular to the branded surface | n/s (output clamps) | 50 / 31 / 25 mV/mT | 0.13 µT/√Hz | ±10 G over the range (±1 mT) | −5…+8.5 % over the range | package ±2 % | n/s | ratiometric; **4.5–5.5 V**; 6.9 mA | SOT23-W, SIP; −40…150 °C | n/s |

**Three-axis parts** (one package for both elements of a position).

| Part | Range per axis | Noise per axis | Offset drift | Output; current | Note |
|---|---|---|---|---|---|
| TMAG5170A1 | ±25 / 50 / 100 mT | at 32× averaging, ±50 mT: X/Y 24 µT rms (0.16 mT p-p, d), Z 11 µT rms (0.073 mT p-p, d) | X/Y ±5.0 µT/K max (25…125 °C); Z ±1.5 µT/K; life ±50 µT | SPI; 3.4 mA | digital |
| TMAG3001A1 | ±37 / 75 mT | X/Y 16 µT rms (0.11 mT p-p, d), Z 9 µT rms, most averaging | ±1 typ, ±9.6 max µT/K | I2C; 2.1 mA | DSBGA-6, 0.83 × 1.32 mm |
| TMR2301 | ±20 mT fit, ±50 mT saturation, each axis | 100 nT/√Hz at 1 Hz (0.007 mT p-p in 0–125 Hz if white, d) | n/s | three analog bridges; 0.2 mA at 1 V | LGA 4 × 4 × 2.5 mm |
| MLX90395, ALS31313, TLE493D-P3I8, TLV493D-A2BW | 50–160 mT | 75–450 µT rms, or 1 G rms | 0.075–1.6 mT | digital | noise far above the budget; MLX90395 code not for new designs; TLV493D a target sheet to 85 °C |

Not kept as candidates and why (from the same reading): NVE AA/AB series are omnipolar (the output does not change
sign with the field); TMR2102 / TMR2104 range ±3–8 mT; DRV5056 is unipolar; A1366 −5/−10 last-time-buy, A1369
discontinued; A1377 is 5 V through-hole; no in-plane linear Hall single-axis part was found (TI, Melexis IMC variants
not found).

### 4. Each part against what the element sees

Radial element (needs along its axis 9.5 mT of short-fault signal at 3 mm plus 1.2 mT for 0.5 mm off the mid-plane,
about 10.7 mT; 11.6 mT of signal at a rope of 2.03 T, `tradeoff.md` table; across, through the package, 32–42 mT with the groove, up to 51–52 mT without; weakest signal the
inner-rope wire, 0.113 mT zero-peak at 5 mm and 1.88 T; acceptance as `c_third_dimension.md`: zero-peak ≥ 2 × noise
p-p):

| Part | In range along its axis | Across its axis (32–52 mT through the package) | Weakest wire over noise (0–125 Hz) | 8 parts per half |
|---|---|---|---|---|
| TMR2185 | meets (±20 mT) | not on the sheet (400 mT absolute maximum, no direction) | not on the sheet | 0.6 mA, 2 mW |
| CT100 | meets (±20 mT linear) | not on the sheet (200 mT absolute maximum) | meets: 0.113 ÷ (2 × 0.012) = 4.9 | 0.8 mA, 3 mW |
| TLI55910-A6E | meets (±35 mT) | not on the sheet; its 75 mT maximum is stated on the in-plane magnitude only | not on the sheet as a density | 3.2 mA, 11 mW |
| TMR2084S | meets (±40 mT) | not on the sheet | not on the sheet | 0.3 mA, 1 mW |

Axial element (`results/parts.json`; range needed: groove untrimmed −15.6 … +7.1 mT, trimmed in place −8.0 … +0.1 mT,
no groove −21.3 … −13.9 mT; across its axis 0 on the mid-plane and about 3 mT per mm off it, far below any stated
limit; level per 1 %: 0.774 mT with the groove, 0.201 mT without; smallest loss = (offset change over −40 … +50 °C +
hysteresis) ÷ level, one element, no temperature correction; the bands stated over −40 … 125 °C are used as they
stand, an upper bound):

| Part | In range: groove / trimmed / no groove | Noise p-p 0–125 Hz | Smallest loss from noise: groove / no groove | Offset change + hysteresis used | Smallest loss from drift: groove / no groove | Converter fit (simultaneous delta-sigma, element supply as reference) | 8 parts per half |
|---|---|---|---|---|---|---|---|
| TMR2584, offset as a total | meets / meets / does not meet (±20 mT specified) | not on the sheet | not on the sheet | 0.10 + 0.20 mT | 0.39 % / 1.5 % | bridge: meets | 8.8 mA, 29 mW |
| TMR2584, offset per kelvin | as above | not on the sheet | not on the sheet | 9.0 + 0.20 mT | 11.9 % / 46 % | bridge: meets | as above |
| TMR2583 | meets / meets / does not meet | not on the sheet | not on the sheet | 0.12 + 0.20 mT (unit read as per volt per kelvin) | 0.41 % / 1.6 % | bridge: meets | 26 mA, 87 mW |
| DRV5055 A1 / Z1 | meets / meets / does not meet (±21 mT, 5 V figure) | 0.016 mT (d) | 0.02 % / 0.08 % | 0.55 mT | 0.71 % / 2.7 % | single-ended around half supply: needs the negative input at half the element supply | 16 mA, 53 mW |
| TMAG5253 BA1 | meets / meets / does not meet | 0.016 mT (d) | 0.02 % / 0.08 % | 0.83 mT (0.5 over 0…85 °C) | 1.07 % / 4.1 % | as DRV5055 | 21 mA, 69 mW |
| A1304-T | meets / meets / meets (±37.5 mT) | 0.017 mT (d) | 0.02 % / 0.08 % | 1.0 mT (25 → 85 °C only) | 1.3 % / 5.0 % | as DRV5055; part rated to 85 °C only | 62 mA, 0.20 W |
| MLX91377, ±40 mT span | meets / meets / meets | not on the sheet as a density | not on the sheet | 0.08 mT | 0.10 % / 0.40 % | analog at 5 V: needs 5 V in the head | 88 mA, 0.44 W at 5 V |
| HAL 2455 | meets (programmed) | — | — | 0.45 mT | 0.58 % / 2.2 % | PWM: does not meet | 56 mA, 0.28 W at 5 V |
| TLE4998S8 | meets | — | — | 0.47 mT | 0.61 % / 2.3 % | SENT: does not meet | 48 mA, 0.24 W at 5 V |
| TMAG5170A1, Z | meets | 0.073 mT (d) | 0.09 % / 0.36 % | 0.135 mT | 0.17 % / 0.67 % | SPI: does not meet | 27 mA, 90 mW |
| TMAG3001A1, Z | meets | 0.059 mT (d) | 0.08 % / 0.30 % | 0.86 mT | 1.1 % / 4.3 % | I2C: does not meet | 17 mA, 55 mW |

Against the record's 0.2–0.4 W per half (register "Total per half", which also holds the converters, the
microcontroller and the line driver): the radial elements take 1–11 mW; the axial elements 29–87 mW as bridges,
53–203 mW as 3.3 V Hall parts, 0.24–0.44 W as 5 V parts. Sixteen elements summed divide noise and independent offsets
by about 4, not the common temperature drift (`../../3d/falsify/d_measurement_chain.md` §5). A per-part temperature
table (the temperature channel is on the board) removes most of a repeatable drift; how much is left is not on any
sheet.

### 5. Hall against TMR for the axial element: the deciding numbers

| | Z-axis TMR (TMR2584 / TMR2583) | 3.3 V linear Hall (DRV5055 A1/Z1, TMAG5253 BA1, A1304) |
|---|---|---|
| Range against need (groove −15.6 … +7.1 mT; no groove −21.3 mT) | ±20 mT specified, ±30 / ±100 mT saturation: groove only | ±20–37.5 mT, no saturation stated ("unlimited" maximum field on the TI sheets): groove; A1304 also no groove |
| Zero drift, −40 … +50 °C, in % of metal at the groove's zero | 0.4 % (TMR2584 if a total; 12 % if per kelvin); TMR2583 0.4 % on one reading of a truncated unit | 0.7–1.3 % |
| Noise | not on the sheets | 0.016–0.017 mT p-p from the sheets' density (d; 0.02 % of metal) |
| Drift over life | not on the sheets | stated: 0.17 mT (TMAG5253); DRV5055 < 0.5 %, unit read differently in two runs |
| Current, 8 per half | 9–26 mA | 16–62 mA |
| Package | SOT23-5 | SOT-23, X2SON-4 (0.4 mm high), SOT23-W |

### 6. Hall in plain words (for the owner)

A Hall element is a small semiconductor plate carrying a current; a field through the plate pushes the current
sideways and gives a voltage in proportion to the field. A TMR element is a stack of thin magnetic films whose
resistance changes as the field turns one film. Here: a common Hall part senses through its package, so lying flat
on the board it reads the axial field, as the TMR2584 does. It stays straight over a wide range (±20 to ±176 mT on
the sheets) and no saturation is stated on the sheets; the TMR parts here are specified only to ±20 mT through the package.
Noise is about the same where the sheets state it. Two costs: its zero moves 0.5–1 mT over temperature, about 1 % of
metal at the groove's zero, so each part needs its own temperature table; and it draws 2–8 mA, against about 1 mA.

### 7. Source table (sheets read for this note; PDFs read, not copied)

| Part | Sheet | Revision | Address |
|---|---|---|---|
| TMR2185, TMR2584 | MultiDimension data sheets | v2.1.2, v2.1 | copies supplied with the prototype (`../sws_sensor_candidates.md` §2.2); the TMR2584 web page did not open |
| TMR2083S, TMR2084S, TMR2583, TMR2301 | MultiDimension TMR Linear Magnetic Sensor / Z Axis TMR Linear Magnetic Sensor / 3 axis TMR linear sensor | v1.0.1 / v1.0.1 / v1.0.1 / V1.0a | copies read for `../sws_sensor_candidates.md`; maker https://www.dowaytech.com/en/ (address of each copy not re-confirmed) |
| TMR2102, TMR2104 | MultiDimension | V1.0a, V2.0 | https://www.farnell.com/datasheets/3121447.pdf; https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/5341/TMR2104.pdf |
| CT100 | Allegro XtremeSense TMR linear | CT100-DS Rev. 8 | https://www.allegromicro.com/-/media/files/datasheets/ct100-datasheet.pdf |
| TLI55910-A6E-E0001 | Infineon XENSIV linear TMR | Rev. 1.00, 2025-02-21 | https://www.infineon.com/assets/row/public/documents/24/49/infineon-tli55910-a6e-e0001-datasheet-en.pdf |
| DRV5055 | TI | SBAS640C (rev. June 2026) | https://www.ti.com/lit/ds/symlink/drv5055.pdf |
| DRV5056 | TI | SBAS644C | https://www.ti.com/lit/ds/symlink/drv5056.pdf |
| TMAG5253 | TI | SBASAI5E | https://www.ti.com/lit/ds/symlink/tmag5253.pdf |
| TMAG5170 | TI | SBASAF4 | https://www.ti.com/lit/ds/symlink/tmag5170.pdf |
| TMAG3001 | TI | SLYS053C | https://www.ti.com/lit/ds/symlink/tmag3001.pdf |
| A1304 | Allegro | A1304-DS Rev. 4 | https://www.allegromicro.com/-/media/files/datasheets/a1304-datasheet.pdf |
| A1324/5/6 | Allegro | A1324-DS Rev. 9 | https://www.allegromicro.com/-/media/files/datasheets/a1324-5-6-datasheet.pdf |
| A1366, A1369, A1377 | Allegro | A1366-DS Rev. 7, A1369-DS Rev. 10, A1377-DS Rev. 3 | https://www.allegromicro.com/-/media/files/datasheets/a1366-datasheet.pdf (and a1369-, a1377-) |
| ALS31300, ALS31313 | Allegro | Rev. 14, Rev. 9 | https://www.allegromicro.com/-/media/files/datasheets/als31313-datasheet.pdf (and als31300-) |
| MLX91377 | Melexis | Revision 001 | https://www.melexis.com/-/media/files/documents/datasheets/mlx91377-datasheet-melexis.pdf |
| MLX90393, MLX90395 | Melexis | Rev. 012, Rev. 6.0 | https://www.melexis.com/-/media/files/documents/datasheets/mlx90393-datasheet-melexis.pdf (and mlx90395-) |
| HAL 2455 | TDK-Micronas | DSH000173_003EN, 2021 | third-party copy https://cdn.eicom.ru/media/PDF/8103416.pdf |
| TLE4998S8 | Infineon | Rev. 1.1 | https://www.infineon.com/assets/row/public/documents/24/49/infineon-tle4998s8d-datasheet-en.pdf |
| TLE493D-P3I8, TLV493D-A2BW | Infineon | Rev. 1.2; target 1.0 | https://www.infineon.com/assets/row/public/documents/30/49/infineon-tle493d-p3i8-datasheet-en.pdf; …/24/49/infineon-tlv493d-a2bw-datasheet-en.pdf |
| NVE AA/AB | NVE analog catalog | to July 2025 | https://www.nve.com/Downloads/analog_catalog.pdf |

Prices and stock: not read in this run (order of magnitude in `../../3d/tradeoff/tradeoff.md` §5 for two Hall parts).

### 8. What the sheets do not say

- What a field **across** the sensing axis does to any part, at 30–52 mT (no TMR or Hall sheet read gives a figure;
  the TMR sheets give only an absolute maximum without direction, the TLI55910 a limit on the in-plane magnitude).
- Noise of any Z-axis TMR part and of the wide-range in-plane TMR parts (stated only for CT100 and TMR2301).
- Whether the TMR2584's "0.5 mV max" offset coefficient is a total or per kelvin; the TMR2583's unit is truncated.
- Long-term offset drift of any TMR bridge (stated on the Hall sheets only).
- A zero shift after the part has sat in a strong field (the head opened beside the magnets); minor-loop hysteresis on
  a near-zero background.
- Where the die sits in the package (depth from the edge facing the rope; tilt).
- Price and availability of the newly read parts.

### 9. Not done

No new 3D run (the wire signals are the 3D values on file, old box); no solve at 8 mm for one wire; steel near the head
only for the 16 mm groove; temperature acts on the magnet only; build tolerances taken from
`d_measurement_chain.md` §3 (old box) as ±0.1 mm depth and ±0.5 mm element; the converter's input range and
reference input not read (part not on file); any measurement.

### 10. Questions, in order

**For the owner.**
1. On the prototype board: the board thickness, and on which face and at what height above it the two parts' dies
   sit? (It sets whether both elements share the mid-plane.)
2. For protecting the radial elements: is a polymer liner acceptable, or must it be metal? And is 5 mm, rather than
   the 3 mm floor, the lift-off to plan for?
3. Is 5 V available on the board in the head? (Three of the lower-drift Hall parts need it.)
4. May the axial channel's zero be trimmed in place at installation (one reading with the head closed on the rope)?
5. Can the prototype head be run over temperature (at least −20 to +45 °C), to read the TMR2584 channel's zero drift?

**For the outside expert.**
1. The TMR2584's offset coefficient "0.5 mV max" over −40 to 125 °C: a total or per kelvin? And what long-term offset
   drift does a Z-axis TMR bridge show?
2. An in-plane TMR bridge with 30–50 mT through its film (the board) against the same field in the film plane across
   its axis (spokes): what happens to gain, zero and hysteresis?
3. For a 3.3 V ratiometric Hall part: how much of the 0.5–1 mT zero drift does a per-part temperature table remove,
   and is a 3.3 V analog Hall part with under 0.1 mT drift over −40 to +50 °C known?
4. A single-ended ratiometric Hall output into a simultaneous 24-bit delta-sigma converter whose reference is the
   element supply: is the negative input at half supply sound, and what does it cost in noise?
5. Protecting the radial elements at 3–5 mm from the rope: a polymer liner, or a thin stainless sleeve; what
   thickness does a rope that moves 2–3 mm need?
