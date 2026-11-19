# Element round 1: three outside answers against element run 3

Three outside models (Opus, Grok, Codex) answered a semi-blind brief: one thin board across the rope, no spokes,
the place and the field of each element given, none of our parts named. None of them could open a data sheet;
every part figure in their answers is from memory, and each answer says so. Their figures are checked here against
the makers' sheets and their arithmetic is recomputed. Nothing here is selected; the outside expert and the owner
decide. The answers, unchanged, and ten lines on each: [answers/](answers/summaries.md). Run 3:
[../element_run_3/element_run_3.md](../element_run_3/element_run_3.md). Arithmetic: `r_arith.py`,
`results/arith.json`.

**In plain words.**
1. All three put the radial element at 5 mm from the rope, and all three say no single part can serve both
   elements of a position, because the two want different distances from the rope.
2. All three read the board the same way as run 3: an in-plane part, lying flat, for the radial element and a
   part that senses through its package for the axial element.
3. Two of the three (Opus, Grok) would put a linear Hall part on the axial element, because it has no magnetic
   memory after a strong field; Codex would put a perpendicular-axis TMR part there, for lower noise, if it
   passes a strong-field test.
4. None of the three named a perpendicular-axis TMR part that exists with the number they gave; run 3 already
   has two on their sheets (TMR2584, TMR2583).
5. Grok offers CT100 as a part that senses through the package; its sheet has it sensing in the package plane,
   so it would read the radial field, not the axial one.
6. On the liner, Opus and Codex find eddy currents in thin stainless steel negligible in 0–125 Hz, as run 3 did,
   and the arithmetic agrees (a time constant of about 7 µs for 0.3 mm); Grok's 5–20 % loss is off by more than
   a thousand times.
7. Of the figures that could be checked on a sheet, about 17 of Opus' agree and 2 differ, Grok 15 and 7, Codex 13
   and 6; all three overstated the Hall part's current or noise, and two named Z-axis TMR parts that do not exist.
8. What the round adds to run 3 is mostly risks and tests (a magnetised lead frame, the pinned layer of a TMR part
   after a hot strong field, the divider that sets the Hall part's half-supply reference, cross-axis pick-up of a
   Z-axis TMR part), not better parts.

**Where they agree and differ** (details in section 3; run 3 for comparison).

| Question | Opus | Grok | Codex | Agree? | Run 3 |
|---|---|---|---|---|---|
| Part kind, radial element | in-plane TMR bridge | in-plane TMR; 3-axis Hall if TMR fails a cross-field test | magnetoresistive bridge or 3-axis Hall | yes: in-plane, flat | in-plane TMR (TMR2185, CT100, TLI55910, TMR2084S) |
| Part kind, axial element | linear Hall | linear Hall | perpendicular-axis TMR, if it passes a strong-field test | 2 against 1 | both open (cases A and B) |
| Distance, radial element | 5 mm | 5 mm (8 if wear forces it) | 5 mm | yes | asks the owner whether 5 mm is the plan |
| 23–42 mT through an in-plane TMR part | under 0.1 % of gain; tilt adds 0.8 mT offset | possibly large: gain, zero, saturation, remanence | measurable; damage unlikely | no: from negligible to possibly large | not on any sheet |
| One part for both elements | no | no (only at one radius) | no (one family, two packages) | yes | no |
| Into the converter | bridge direct; Hall against a tracking half-supply divider, gain 1 | the same; gains 1–16 / 1–4 | the same; gains 32–64 axial, 16–32 radial / 8–32 Hall (axial and Hall gains clip, by arithmetic) | wiring yes; gains no | question to the expert |
| Hall current, 8 per half | 6 mA each, 158 mW | 8 mA each, 0.21 W | "mA or sub-mA" | no | 2 mA each (sheet), 53 mW |
| Liner | 0.3 mm annealed stainless | polymer | either, by distance | eddy currents: 2 of 3 (arithmetic sides with them) | eddy currents negligible for 316L |
| Large field | Hall recovers; TMR pinned layer may not | Hall recovers; TMR may need set / reset | Hall recovers; TMR may shift | yes, TMR is the risk | not on the sheets |
| Tests | the same five subjects | the same five | the same five | subjects yes, pass figures no | five owner questions, five expert questions |

**Hall against TMR for the axial element.** Two of the three (Opus, Grok) would put a linear Hall part of the
DRV5055 class on the axial element, because a Hall die has no magnetic memory and its zero then depends only on
temperature, which the board measures; Codex would put a perpendicular-axis TMR part there for its lower noise, but
only if it passes a strong-field test. All three make the choice hang on the same measurement: the zero after the
part has been in a strong field (an empty head, handling). It is not firm: none of the three read a drift figure off
a sheet, their own drift figures for the two kinds overlap, and two of them named TMR parts that do not exist. Run 3's
sheet numbers (TMR2584 0.4 % of metal if its offset figure is a total, 12 % if per kelvin; the 3.3 V Hall parts
0.7–1.3 %) are not moved by any model figure, but re-reading the DRV5055 sheet softens the Hall side: its zero-drift
figure is typical only, with no maximum, and the change over temperature could reach about 1.4 % rather than 0.7 %.

---

## Dense part

### 1. The answers

Saved unchanged in [answers/](answers/), ten plain lines on each in [answers/summaries.md](answers/summaries.md). The
Codex file holds a cut-off first draft followed by a full second answer; both are read; the first names five parts (MLX90393, TLE493D-W2B6,
AAH002, DRV5057, A1362), and its figures are counted with the second's. All three tag every part figure with a confidence (Opus: sure / fairly sure / unsure; Grok: the
same; Codex: "from memory", mostly "unsure").

### 2. Every part named, against its sheet

Marks: **agrees**; **differs** (theirs / sheet); **not found** (part or figure not on the sheet, or the sheet not
read). Sheets read for this note by a sheet-reading subagent with general queries (part numbers only), or taken from
run 3's source table where the part is there (marked R3). 10 G = 1 mT; 10 Oe ≈ 1 mT in air. "(d)": derived here.
The error hunted is the sensing direction: a part that senses in the board plane offered for the axial element
(through the board), or the reverse.

**Radial element (must sense in the package plane).**

| Part (maker) | Named by | Sensing direction | Range | Sensitivity | Noise | Zero drift | Current | Note |
|---|---|---|---|---|---|---|---|---|
| TMR2xxx linear family (MultiDimension), no number | Opus | in plane / sheets of TMR2102-04: "parallel to the package top-marking surface" — **agrees** | "about ±1 to ±50 mT across the market" — not part-specific | — | — | "I do not know" | — | Opus did not know which variant gives ±20 mT; run 3's TMR2185 (±20 mT, in-plane) is one |
| TMR2104 (MultiDimension) | Grok (also 2102 / 2103) | in plane (X) / in plane — **agrees** | ±5–8 mT / ±80 G = ±8 mT linear, ±150 G saturation — **agrees** | 10–30 mV/V/mT / 3.1 mV/V/G = 31 mV/V/mT — **differs** (slightly) | "≪ 0.01 mT rms" / n/s — **not found** | "I do not know" | 1–3 mA at 5 V / 1 kΩ (SOT23-5): 5 mA at 5 V (d); 30 kΩ versions: 0.17 mA at 5 V (d) — **differs** | TMR2102 ±3 mT, TMR2103 ±3 mT linear (sheets v2.1.1) |
| CT100 (Allegro) | Opus (radial), Grok (as axial) | Opus: in plane along a marked axis / sheet R3 and re-read: field "into the pin 1 / pin 6 side", along the package — **agrees** | — (Opus' range is the family's) | — | — | — | — | see the axial table for Grok's entry |
| TLI5590-A6W (Infineon) | Opus | in plane (family A) / "parallel to the package surface" — **agrees**; "made for magnetic encoders" — **agrees** | — / ±5 mT | — | — | — | — | a sine / cosine TMR gradiometer for a magnet strip of 0.5 mm pole pitch, not a field-proportional part; sheet from a third-party copy |
| TMAG5170 (TI) | Opus, Codex | X / Y in plane, Z through / "X and Y … in plane with the package. The Z [field] is perpendicular" — **agrees** (both) | Opus ±25 / 50 / 100 mT; Codex "up to at least ±100" / A1: ±25, 50, 100 mT — **agrees** (both) | — | Opus 50–150 µT rms / X-Y 140 µT, Z 61 µT rms at 1× averaging (24 / 11 µT at 32×) — **agrees** | — | Opus "mA range" for the family — too general to count; Codex "~mA-class" / 3.4 mA active at 5.5 V — **agrees** | package: Opus VSSOP-8 **agrees**; Codex "WSON class" **differs** (VSSOP-8) |
| TLE493D-W2B6 (Infineon) | Opus, Codex | 3D / 3D (figure only) — not found in words | Opus "up to ±160 mT"; Codex "about 100 mT class" / full ±160 min (±200 typ), short ±100 min mT — **agrees** (both) | — | — / 0.1 typ, 0.5 max mT rms | — / Z ±1.6 mT, X-Y ±0.45 mT over −40…125 °C | Codex "low-power modes" / 1–5 mA fast mode, nA power-down — **agrees** | Opus' TSOP-6 **agrees** (PG-TSOP6) |
| ALS31313 (Allegro) | Opus | 3D — **agrees** | ±50 / 100 / 200 mT / ±500 / 1000 / 2000 G — **agrees** | — | — / X-Y 0.1 mT rms (−500 version, d) | — | — / 3.4 mA active | I²C |
| TLV493D-A1B6 (Infineon) | Grok | X / Y in plane, Z through / figure: X, Y in the package plane — **agrees** | ±130 mT / "up to +130 mT" — **agrees** | LSB about 0.1 mT / 98 µT per LSB — **agrees** | 0.01–0.05 mT after filtering / 0.1 mT rms, no filter stated — not comparable | "I do not know" / ±1 mT over −40…125 °C | 3.7 mA / 3.7 mA during conversion — **agrees** | package: WSON **differs** (TSOP-6); sheet from a third-party copy |
| MLX90392 (Melexis) | Grok | 3D — figure not read | "±50 mT settings" / ±5 mT (-010) or ±50 mT (-011 / -013) — **agrees** | — | — / 11 µT rms (-011, 5 ms conversion) | — | "mA" / 1.7 mA average at 100 Hz — **agrees** | Grok's row is "MLX90392 (or MLX90393)", "I²C / SPI": the MLX90392 is I²C only, the MLX90393 has both; 1.8 V supply |
| MLX90393 (Melexis) | Grok, Codex | 3D — figure only | Codex "up to about ±50 mT" / saturation onset 50 mT (standard concentrator) — **agrees** | — | — / plots only — **not found** | — | Codex "mA" / 2.3–3.0 mA converting — **agrees** | Codex' LGA / QFN: QFN-16 **agrees** |
| AA002-02, AA006 (NVE) | Grok | in plane / "in the plane of the package", along its axis — **agrees** | "often a few mT" / AA002 0.15–1.05 mT linear (1.5 saturation), AA006 0.5–3.5 mT; omnipolar — **differs** for AA002 | "high" / 3–5 mV/V/Oe | — / n/s | — | "a few mA" / 5 kΩ bridge: 0.66 mA at 3.3 V (d) — **differs** | omnipolar: the output does not change sign with the field |
| AAH002-02E (NVE) | Codex | in plane / in plane — **agrees** | ±6–10 mT / 0.06–0.3 mT, omnipolar — **differs** | 20–30 / 110–180 mV/V/mT — **differs** | 20–40 nT/√Hz / n/s — **not found** | — | "sub-mA to mA" / 2 kΩ: 1.65 mA at 3.3 V (d) — **agrees** | Codex calls it "TMR / GMR class": GMR |
| AAL family (NVE) | Codex | in plane / in plane — **agrees** | ±20–30 mT / every AAL part 0.15–1.05 mT, omnipolar — **differs** | 5–10 / 30–42 mV/V/mT — **differs** | — / n/s | — | — | |
| MLX91205 (Melexis) | Opus (set aside) | — / "parallel to the chip surface", via concentrator | — / ±10 or ±25 mT | — / 280 or 100 V/T | — / < 125 nT/√Hz | — / ±50 mV over −40…125 °C | 5 V, about 10 mA / 4.5–5.5 V, 11 mA typ — **agrees** | sheet Rev 008 (an old revision), third-party copy; the maker's site refused; one variant listed obsolete by a distributor (not confirmed) |
| HMC1021 (Honeywell) | Opus (set aside) | — | ±0.6 mT / not read — **not found** | | | | | |
| HG (GaAs) / HW (InSb) families (AKM) | Opus | through the package face / not read — **not found** | | | | | | |

**Axial element (must sense through the package).**

| Part (maker) | Named by | Sensing direction | Range | Sensitivity | Noise (0–125 Hz) | Zero drift | Current | Note |
|---|---|---|---|---|---|---|---|---|
| DRV5055 A1 (TI) | Opus, Grok, Codex | through (all three) / "perpendicular to the top of the package" — **agrees** | Opus ±21 mT; Grok ±21–169 mT by grade / 3.3 V: ±22 mT (A1) … ±176 (A4); 5 V: ±21 … ±169 — **agrees** | Opus 60 mV/mT at 3.3 V; Grok 12.5–100 mV/mT / 60 at 3.3 V; 12.5–100 at 5 V — **agrees** | Opus 0.2–2 µT/√Hz → 2–22 µT rms / 215 nT/√Hz → 2.4 µT rms (d) — **agrees**; Grok 10–50 µT rms, Codex 8–30 µT rms — **differs** (3–20 times the sheet) | Grok ±0.1–0.3 mT, Codex 0.8–1.5 mT / ±1 % × VCC in the typical column only, no maximum, over −40…125 °C against its own 25 °C value: ±33 mV = ±0.55 mT (d) — **not comparable** (a typical figure over a wider range cannot refute either); Opus "I do not know" | Opus 6 mA, Grok 6–10 mA / 2 mA typ, 4 max at 3.3 V; 3 / 5 at 5 V — **differs**; Codex "mA or sub-mA" for Hall parts in general — too general to count | Opus' sensitivity drift +0.12 %/K **agrees** (A versions; Z versions 0) |
| DRV5057 (TI) | Codex (first draft) | through / as DRV5055 — **agrees** | — / ±21 mT (A1, 5 V) | — | — / n/s | 0.8–2.0 mT / n/s — **not found** | — / 6 mA typ, 10 max | **PWM output** (2 kHz, open drain): does not feed the converter; Codex compared it with analog parts |
| A1309 (Allegro) | Grok | through / not in words; figures: field toward the branded face — **agrees** (from a figure, as TLV493D) | "few tens of mT" / clamps at about ±22 mT (d) — **agrees** | — / 9 mV/G = 90 mV/mT | — / 1.5 mG/√Hz at 5 V | "I do not know" / −20…+10 mV at 125 °C (SIP) | "mA–tens of mA" / 9 mA typ, 11.5 max — **agrees** | **5 V only** (4.5–5.5 V); not noted by Grok |
| A1324 (Allegro) | Codex | through / perpendicular to the branded surface (R3) — **agrees** | — | — | 8–20 µT rms / 0.13 µT/√Hz → 1.5 µT rms (d) (R3) — **differs** | 0.7–1.2 mT / ±10 G = ±1 mT over the range (R3) — **agrees** | — / 6.9 mA (R3) | **5 V** (4.5–5.5 V, R3); not noted by Codex |
| A1362 (Allegro) | Codex (first draft) | — | — | — | — | "similar class; I do not know" | — / 9.2 mA, 5 V | **discontinued** (stated on its sheet) |
| A1367 (Allegro) | Opus | — | — | — / 0.6–6.4 mV/G programmed | — / 1.4 mG/√Hz | — | 5 V, 8–10 mA / 5 V, 11 typ, 16.25 max mA — **differs** (slightly) | one variant discontinued on its sheet |
| TLE4997 (Infineon) | Opus | — | — | — | — | — | 5 V, 8–10 mA / not read — **not found** | the maker's copy did not open |
| CT100 (Allegro) | Grok, as "perpendicular TMR" | through the board / **in the package plane**, field "into the pin 1 / pin 6 side" — **differs: the hunted error** | "I do not know" | "high" / 0.45 mV/V/G = 4.5 mV/V/mT | "low" / 700 nV/√Hz at 10 Hz, 1 V | "I do not know" | "low mA" / 0.30 mW at 3 V on a 30 kΩ bridge, about 0.1 mA (d) — too general to count | lying flat it reads the radial field; on the axial element it would need a daughter piece or an edge mount (run 3 §2) |
| "TMR4xx / Z" (MultiDimension) | Grok | — | — | — | — | — | — | **part not found**: the maker's list has no TMR4xx linear part; its Z-axis linear parts are TMR2583, TMR2584, TMR2617S-AAC |
| "TMR62xx Z variant" (MultiDimension) | Codex | — | Codex ±20–30 mT | — | 3–10 µT rms | 0.4–0.8 mT | — | **part not found** (no TMR62xx on the list) |
| Z-axis TMR, no number (MultiDimension) | Opus | — | — | — | — | — | — | Opus: "I cannot name a catalogue part with ±20 mT"; one exists (TMR2584, ±20 mT, on the prototype, R3) |
| TMAG5170, MLX90393 (Z axis) | Opus | through / Z "perpendicular to the top of the package" (TMAG5170) — **agrees** | — | — | 50–150 µT rms / Z 61 µT at 1×, 11 µT at 32× (TMAG5170) — **agrees** | — | — | digital (SPI / I²C): bypasses the converters, as Opus says |

**Checkable figures, per model: agrees / differs** (a figure counts where the model gave a value or a direction for
a named part and the sheet states it; "I do not know", family-wide or class-wide figures, package names and the
DRV5055 zero drift (not comparable) are not counted; Codex' count includes its cut-off first draft, which it
replaced, for DRV5057, TLE493D-W2B6 and MLX90393):

| Model | Agrees | Differs | Of which sensing direction | Parts not found (no such part) |
|---|---|---|---|---|
| Opus | 17 | 2 (DRV5055 current; A1367 current, slightly) | 0 | 0 (named no number it was unsure of) |
| Grok | 15 | 7 (CT100 direction; AA002 range and current; TMR2104 current and sensitivity (slightly); DRV5055 noise and current) | 1 (CT100) | 1 (TMR4xx) |
| Codex | 13 | 6 (AAH002 range and sensitivity; AAL range and sensitivity; DRV5055 noise; A1324 noise) | 0 | 1 (TMR62xx); plus, in the first draft, one discontinued part (A1362) and one PWM part listed among "linear Hall" parts compared on analog figures (DRV5057) |

Opus' agrees: direction 6 (TMR21xx, CT100, TLI5590, TMAG5170, ALS31313, DRV5055), range 4 (TMAG5170, TLE493D,
ALS31313, DRV5055), sensitivity 1 and its drift 1 (DRV5055), supply ≥ 3.0 V 1 (DRV5055), noise 3 (TMAG5170 X-Y,
TMAG5170 Z, DRV5055), current 1 (MLX91205). Grok's: direction 5 (TMR2104, AA002, TLV493D, DRV5055, A1309), range 5
(TMR2104, TLV493D, MLX90392, DRV5055, A1309), sensitivity 2 (TLV493D, DRV5055), current 3 (TLV493D, MLX90392,
A1309). Codex': direction 6 (TMAG5170, AAH, AAL, DRV5055, DRV5057, A1324), range 3 (TMAG5170, TLE493D, MLX90393),
zero drift 1 (A1324), current 3 (TMAG5170, MLX90393, AAH). Each count is firm only to about ±2: which figure is
"general" and which "checkable" is a judgement. The counts are of figures, not of parts, and Opus gave fewer numbers
than the others ("I do not know" or a family range in most cells). Read together: Opus said "I do not know" where it
did not know and rarely differed from a sheet; Grok and Codex gave more numbers and more of them differ, and those
that differ are ones that matter here (the Hall part's noise and current, the range of the NVE parts).

**New parts that pass the sheet check on direction and range**, in run 3's row format (run 3 §3; nothing selected):

| Part | Sensing direction (sheet's words, short) | Linear range | Sensitivity | Noise | Zero offset; drift | Output; supply; current | Package; temperature | Status / against run 3 §4 |
|---|---|---|---|---|---|---|---|---|
| MLX91205 (radial) | "parallel to the chip surface" (concentrator) | ±10 (LB) or ±25 mT (HB) | 280 / 100 V/T | < 125 nT/√Hz (0.009 mT p-p in 0–125 Hz, d) | ±20 mV at 25 °C; ±50 mV over −40…125 °C (±0.5 mT HB, d) | ratiometric analog; 4.5–5.5 V; 11 mA typ, 16 max | SOIC8; −40…125 °C | old sheet revision; status not confirmed. The one in-plane analog Hall part run 3 did not find. 8 per half: 88 mA, 0.44 W at 5 V — over the 0.2–0.4 W per half; a concentrator under 31 mT through it: not on the sheet |
| TMR2104 (radial, 5 mm only) | "parallel to the package top-marking surface" | ±8 mT linear, ±15 mT saturation | 3.1 mV/V/G (31 mV/V/mT) | n/s | ±8 mV/V (30 kΩ) or ±10 mV/V (1 kΩ); drift n/s | bridge; 1–7 V; 33 µA at 1 V (30 kΩ) | SOP8, DFN8L, SSIP4, SOT23-5; −40…125 °C | meets at 5 mm (5.1 + 1.5 mT at 0.5 mm off-plane, d), not at 3 mm (10.8 mT); field across the axis n/s |
| A1309 (axial) | branded face (figure) | about ±22 mT before the clamps (d) | 90 mV/mT | 1.5 mG/√Hz = 0.15 µT/√Hz (0.011 mT p-p, d) | QVO 2.5 V ±12 mV; −20…+10 mV at 125 °C (SIP) | ratiometric; 4.5–5.5 V; 9 mA typ | SOT-23W, SIP; −40…150 °C | in range with the groove (−15.6 … +7.1 mT); 5 V and 72 mA for 8 (0.36 W): as A1324 in run 3 |
| A1367 (axial) | — (programmable linear Hall) | programmed | 0.6–6.4 mV/G | 1.4 mG/√Hz | n/r | ratiometric; 4.5–5.5 V; 11 mA typ | SIP-4; −40…150 °C | 5 V, 88 mA for 8 (0.44 W) |
| TMR2617S-AAC (axial) | Z (maker's list) | ±100 mT, programmable (list) | n/r | n/r | n/r | n/r | SOT23-3 | found on the maker's list, named by no model; sheet not read |

Fail the direction or range check here, or do not feed the converters: TMAG5170 (SPI; run 3 §3); TLI5590-A6W (a gradiometer for a magnet strip, ±5 mT); NVE AA / AAH / AAL (omnipolar, ≤ 3.5 mT);
TMR2102 / 2103 (±3 mT); DRV5057 (PWM); A1362 (discontinued); the 3-axis digital parts TLV493D-A1B6, TLE493D-W2B6,
ALS31313, MLX90392 / 90393 (digital buses; in-plane noise 0.1 mT rms on the TLV493D, TLE493D and ALS31313-500 X-Y; MLX90392 1.5–20 µT rms by
version (the ±5 mT version too small in range); MLX90393 noise only in plots; run 3
§3 already sets the 3-axis parts aside for this reason).

### 3. Where the three agree and where they differ

**The technology for the axial element.**
- Opus: an analog ratiometric chopper Hall part of the DRV5055 class; reason: no magnetic memory, so its zero is set
  by temperature alone, which is measured. Would change its mind for a Z-axis TMR part shown to hold hysteresis and
  shift after a strong field at or under 0.03 mT over −16 … +7 mT; it would save about 150 mW and lower the noise.
- Grok: linear Hall (DRV5055, a grade sized for ±20–40 mT) as the default, for range, ratiometric drive and recovery
  after a large field. Would change its mind if Hall drift after temperature correction stays above 0.4 mT over
  −40 … +50 °C, or if power forces well under 2 mA per channel, and the TMR part passes the large-field tests.
- Codex: perpendicular-axis TMR, if it passes strong-field exposure and cross-axis tests; reason: lower
  low-frequency noise for the 0.08 mT run-to-run target. Would change its mind on irreversible offset jumps or a
  heavy re-zero burden after large fields.
- So: two for Hall, one for TMR, and all three make it conditional on the same test (the zero after a strong field).
  Their drift figures for the two technologies overlap and are from memory (Opus: Hall 0.1–0.5 mT, TMR hysteresis
  0.1–0.4 mT; Grok: Hall 0.2, TMR 0.05–0.15; Codex: Hall 0.7–1.5, TMR 0.4–0.8 mT). Firmness: low; it is a judgement
  on magnetic memory against noise, and none of the three read a drift figure off a sheet.

**The distance for the radial element.** All three: 5 mm. Opus: keeps 55–65 % of the 3 mm signal (recomputed on the
middle of each range: short fault 54 %, outer wire 58 %, inner wire 66 %) and leaves room for a liner and the rope's
tolerance. Grok: 5 mm unless wear tests force 8 mm. Codex: 3 mm broke parts, 8 mm leaves 0.06–0.16 mT for an inner
wire. Signal loss per mm, recomputed from the brief's table (geometric): 27 % (short fault), 24 % (outer wire), 19 %
(inner wire) between 3 and 5 mm; 19–21 % between 5 and 8 mm. Opus' "about 20 % per mm" and "−22 / −21 %" sit in
that range.

**23–42 mT through an in-plane TMR part (the radial element).**
- Opus: the free layer's out-of-plane demagnetising field (1–1.6 T, physics from memory) tilts it by 1.1–1.8° at
  31 mT (recomputed), a gain change of 0.02–0.05 % (recomputed); no damage; the real effect is tilt of the die or
  board: 1.5° couples 0.81 mT of the 31 mT into the reading as offset, and the ±5 mT spread moves it by ±0.13 mT
  (recomputed; slow, so it does not hurt pulse detection). Caveat: parts with thick flux concentrators may saturate
  at the edges.
- Grok: "large for many linear MR ranges"; it may cut sensitivity, shift the zero, add non-linearity, saturate or
  leave remanence; qualitative, no number.
- Codex: a measurable zero and span change and more non-linearity; damage unlikely; no number.
- So: all three say it must be measured; Opus and Codex expect no damage, while Grok names saturation and remanence
  "in worst cases" for magnetoresistive parts; they differ on the size (Opus: negligible apart from tilt; Grok:
  possibly large). Run 3 found no sheet that states it.

**One part for both elements.** All three: no. The two elements want 5 mm and 16 mm (11 mm apart on the board), and
the 3-axis Hall parts are too noisy for the inner wire (Opus) or use a digital bus that bypasses the converters
(all three). Codex: one part family could serve both, as two packages. Opus' extrapolation of the outer-wire signal
to 16 mm (0.65 × 0.8⁸ = 0.11 mT) recomputes.

**Connection to the converter.**
- Bridge (TMR): all three, straight into a differential input with the bridge fed from the converter's reference.
  Gains: Opus about 4 (5 mV/V/mT at 2.5 V, ±250 mV for ±20 mT); Grok 1–16, set so 10 mT (radial) or 16 mT (axial)
  fills 50–80 % of full scale; Codex 16–32 (radial) and 32–64 (axial).
- Hall (single-ended, ratiometric): all three, the output against half the supply (a divider or a mid-supply
  input). Gains: Opus 1 (swing −0.96 … +0.42 V for −16 … +7 mT at 60 mV/mT, recomputed); Grok 1–4; Codex 8–32.
- Arithmetic (full scale assumed ±V_ref ÷ gain, V_ref = element supply 2.5–3.3 V; the converter is not named): for
  the axial span of 16 mT, a 60 mV/mT Hall part on a 3.3 V supply allows a gain of at most 3.4 (2.6 if the
  reference were 2.5 V), and a 5 mV/V/mT bridge fed from the reference at most 12.5. Codex' gains (8–32 Hall, 32–64 TMR axial) clip; Grok's top Hall gain of 4 clips slightly; Opus' fit.
- Opus adds: the half-supply divider must track: 10 ppm/K over 90 K at 1.65 V is 1.5 mV, 25 µT at 60 mV/mT
  (recomputed); it asks for ≤ 2 ppm/K. And the Hall part's sensitivity drift (+0.12 %/K) times the standing field:
  0.76 mT on 7 mT, 0.54 mT on 5 mT over 90 K (recomputed); trimming the zero in place shrinks it.
- Power: Opus 8 Hall × 6 mA × 3.3 V = 158 mW, 40–80 % of the budget; Grok 8 × 8 mA = 0.21 W, "may blow" the budget;
  Codex "usually fits; often mA or sub-mA". The DRV5055 sheet at 3.3 V: 2 mA typical, 4 mA maximum: 8 parts take
  53 mW typical, 106 mW at the maximum (d). Opus and Grok overstate it by 3–5 times on the typical figure; the
  5 V Hall parts (A1309 9 mA, A1367 11 mA, A1324 6.9 mA) are where their numbers fit.

**The liner.**
- Opus: 0.3 mm annealed non-magnetic stainless; 0.3–0.5 mm costs 6–10 % of signal by distance, against 20–30 % for 1.0–1.5 mm of
  polymer; eddy currents negligible. Grok: polymer as the wear layer; stainless only if needed, with 5–20 % loss at
  125 Hz. Codex: both cost only by distance (0.5 mm polymer about 12 % of the short-fault peak; 0.2 mm stainless
  about 5 %); eddy loss under 1 %.
- Recomputed (316L, resistivity 0.72–0.74 µΩ·m, textbook; µr = 1): skin depth 38–39 mm at 125 Hz, 43 mm at 100 Hz,
  123–125 mm at 12 Hz. Thin-shell time constant µ0 σ t L ÷ 2 with L = 28 mm: 4.8–4.9 µs for 0.2 mm, 7.1–7.3 µs for
  0.3 mm, 12 µs for 0.5 mm, 25 µs for 1 mm (L = 29 mm); corner 6–33 kHz; amplitude loss at 125 Hz 0.0007–0.02 %.
  Pulses last 0.2–0.4 s at 3 m/min and 0.08–0.16 s at 7.5 m/min (recomputed).
- So Opus' 38 mm / 7 µs and Codex' "tens of mm, under 1 %" agree with the arithmetic; Grok's "about 1 mm" skin depth
  near 100 Hz is about 40 times too small, and its 5–20 % loss is more than a thousand times the computed 0.002 %.
  Codex' distance losses recompute (1.1 mT / 12 %, 0.24 mT / 11 %, 0.026 mT / 8 % for 0.5 mm; 0.44 mT / 5 % for
  0.2 mm).
- The real choice between them is mechanical (cut-through by broken-wire ends against magnetism after cold work);
  Opus and Grok both name magnetism of cold-worked stainless as the thing to check.

**A large field (empty head, handling).**
- Hall: all three, no magnetic memory in the die; recovery automatic. Opus adds: a ferromagnetic lead frame (Alloy 42,
  nickel plating) can magnetise and shift the zero; choose copper lead frames and test. Hall parts with a
  concentrator film keep a small remanence.
- TMR: all three, the free layer's state and the offset can change. Opus: the pinned layer can turn partly and for
  good above a few hundred mT, especially when hot; there is usually no reset strap. Grok and Codex: a set / reset
  pulse where the part has one, else recalibrate.
- So: agreement on the direction of the risk (TMR more than Hall); none gives a threshold from a sheet.

**Their five prototype tests**, side by side (pass figures as each gave them):

| Test | Opus | Grok | Codex |
|---|---|---|---|
| Axial zero over temperature | −40 … +50 °C, bias coil at −16 / 0 / +7 mT, 3 cycles: residual after correction ≤ 0.10 mT, cycle to cycle ≤ 0.04 mT | after correction ≤ 0.4 mT; same-temperature repeat ≤ 0.08 mT | after correction ≤ 0.4 mT; ≤ 0.08 mT at fixed temperature (stretch) |
| Large-field exposure | 500 mT along ±X, ±Y, ±Z: axial zero ≤ 0.04 mT, gain ≤ 0.5 %; radial zero ≤ 0.3 mT, gain ≤ 2 % | ±200–500 mT any axis: Hall zero ≤ 0.05 mT; TMR ≤ 0.1 mT after initialising | ±300 mT, three axes: zero ≤ 0.1 mT after a recovery routine |
| Field across the radial element's axis | −45 mT through the part, sweep ±15 mT along: gain ≤ 2 %, non-linearity ≤ 1 % of full scale, noise ≤ 20 µT rms in 0.5–30 Hz | −42 mT through the board, 2 mT step: gain ≤ 5 %, zero ≤ 0.05 mT after return | ±50 mT through the board: ≤ 0.1 mT (radial), ≤ 0.05 mT (axial) after correction |
| Rope with cut wires | 5 mm, liner fitted, 3 and 7.5 m/min: outer wire SNR ≥ 10 against strand ripple, inner ≥ 3 | 5 mm, outer-wire pulse ≥ 1.2 mT: peak over rms noise ≥ 10 | 3 and 7.5 m/min: outer SNR ≥ 6, inner ≥ 3 |
| Soak, power | 30 days at constant temperature, then 200 cycles and damp heat: axial zero ≤ 0.04 mT per month, total ≤ 0.08 mT; ≤ 0.35 W per half | full half, potted: ≤ 0.4 W per half; no cracked packages | 500 h damp heat: ≤ 0.1 % of metal per month after correction |

SNR: signal-to-noise ratio. All three name the same five subjects; the pass figures differ by up to a factor of
2.5 (axial zero after exposure 0.04 / 0.05 / 0.1 mT) and the gain limits under a cross field by 2.5 (2 % / 5 %).

### 4. Against element run 3

**What the round confirms.**
- The pairing on one thin board: an in-plane part for the radial element and a through-the-package part for the
  axial element, both lying flat (run 3 §2). All three read the board the same way, without being told the parts.
- No single part per position (run 3 case C): the two elements want radii 11 mm apart.
- Digital 3-axis parts bypass the simultaneous converters (run 3 §4, "does not meet" on converter fit).
- A thin stainless liner costs nothing in 0–125 Hz through eddy currents (run 3 §2: 316L corner above 6 kHz for
  1 mm). Opus and Codex agree, the arithmetic agrees (section 3).
- A Hall part's zero is reset by temperature alone; a TMR part can carry a memory of a strong field (run 3 §8 lists
  "a zero shift after a strong field" as not on any sheet). All three agree, none with a sheet figure.
- 5 mm for the radial element (run 3 asks the owner whether 5 mm, not the 3 mm floor, is the plan): all three.

**What the round contradicts, and who is right.**
- The 3.3 V Hall part's current: Opus 6 mA, Grok 6–10 mA against run 3's 2 mA. The DRV5055 sheet (SBAS640C) says
  2 mA typical, 4 mA maximum at 3.3 V: run 3 is right on the typical figure; the maximum (4 mA, 32 mA for 8, 106 mW)
  is not in run 3 and belongs beside it.
- The Hall part's zero drift: Grok ±0.1–0.3 mT and Codex 0.8–1.5 mT against run 3's 0.55 mT. The sheet's ±1 % × VCC
  (±0.55 mT at 3.3 V) is a typical figure over −40…125 °C with no maximum, so it cannot settle which is right over
  −40…+50 °C (see the next point); this stays open (section 5, item 7).
- The Hall part's noise: Grok 10–50 µT rms, Codex 8–30 µT rms against run 3's 215 nT/√Hz (2.4 µT rms in 0–125 Hz,
  d): the sheet sides with run 3.
- CT100 offered for the axial element (Grok): its sheet has it sensing in the package plane, as run 3 used it (on the
  radial element).
- No round answer contradicts a run 3 sheet figure with a sheet figure of its own.

**What the round finds in run 3 that run 3 did not say** (from re-reading the DRV5055 sheet for this note):
- The DRV5055's "±1 % × VCC" drift of the zero over −40…125 °C is printed in the **typical** column, with no maximum,
  and against the part's own 25 °C value. Run 3 used it as a band of ±0.55 mT and took 0.55 mT as the change; the
  change between −40 and +50 °C could be up to 1.1 mT if the zero runs from one edge to the other, and no part is
  guaranteed to stay inside it. Run 3's 0.71 % of metal for this part is then a typical half-band, not a bound.
- The DRV5055 A1's range at 3.3 V is on the sheet: ±22 mT (run 3: "3.3 V figure not read this pass", used ±21 at 5 V).

**What the round adds that run 3 did not have.**
- Risks: a ferromagnetic lead frame (Alloy 42, nickel plating) magnetised by the empty head shifts a Hall part's
  zero (Opus); the TMR pinned layer turning for good after a strong field, worst when hot (Opus); a Z-axis TMR part
  with flux guides picking up 2–10 % of the radial field across it, up to 0.15 mT at 1–1.5 mT off the mid-plane
  (Opus, from memory); the Hall part's sensitivity drift times the standing field (0.76 mT on 7 mT over 90 K for the
  A versions; the Z versions have 0 typical; d); the half-supply divider's tracking (10 ppm/K is 25 µT; d); die or
  board tilt under the field through the radial part (1.5° is 0.81 mT of offset, ±0.13 mT as it varies; d; run 3
  had 1° for a daughter piece only).
- Tests with pass figures (section 3 table), in particular the six-axis exposure at 500 mT with a zero-shift limit
  and a cross field of −45 mT on the radial part with a gain limit; run 3 had the subjects, not the pass figures.
- Parts not in run 3 that pass the direction and range check (section 2, last table): MLX91205, an in-plane analog Hall part (run 3 found none), but
  5 V, 11 mA and an old sheet; TMR2104 for the radial element at 5 mm only; A1309 and A1367 as 5 V Hall parts
  beside run 3's A1324; and TMR2617S-AAC, a programmable Z-axis TMR part on the maker's list that no model named and
  whose sheet was not read.
- Questions for the owner that run 3 did not ask: the strand ripple at 5 and 16 mm (Opus); the worst field at each
  element with the head open (Opus, Grok); whether a digital bus on the half-ring is allowed (Grok, Codex); whether
  a re-zero at every start is allowed (Codex); the potting compound's stiffness (Opus).

### 5. The disagreements, for the owner and the outside expert (not resolved here)

Each with the one measurement or sheet line that would settle it.

1. **Hall or perpendicular-axis TMR for the axial element** (Opus, Grok: Hall; Codex: TMR; run 3: both open as
   cases A and B). Settles it: the prototype's TMR2584 channel and one DRV5055 A1/Z1 beside it, zero read at 20 °C
   before and after a 500 mT exposure on six axes, and over −20 … +45 °C (at least); for each, the residual after a
   per-part temperature table against 0.4 mT (0.5 % of metal) and the shift after exposure against 0.08 mT.
2. **What 23–42 mT through an in-plane TMR part does** (Opus: under 0.1 % of gain, tilt only; Grok: possibly large;
   Codex: measurable). Settles it: TMR2185 and CT100 on a coil, −45 mT through the package, ±15 mT swept along the
   axis: the gain change and the zero shift against no cross field.
3. **Cross-axis pick-up of a Z-axis TMR part** (Opus: 2–10 % with flux guides, could be 0.15 mT; Grok: may bias the
   operating point; Codex: test it; no sheet read states it). Settles it: TMR2584 with 3 mT applied in its package
   plane, reading change along its axis; or a cross-axis line on its sheet (none in run 3's reading).
4. **The liner: polymer or thin stainless** (Opus: 0.3 mm annealed stainless; Grok: polymer; Codex: either, by
   distance). Eddy currents do not decide it (arithmetic above). Settles it: the relative permeability of the
   sleeve as formed (a permeability meter reading under about 1.01 after forming), and a cut-through test with a
   broken wire end against each material at the thickness in question.
5. **Pass figures for the axial zero after a strong field** (0.04 / 0.05 / 0.1 mT). Settles it: the owner's
   accuracy target: 0.1 % run to run is 0.08 mT, so a shift above that is visible as loss of metal unless the zero
   is re-trimmed after every opening of the head.
6. **Whether a part with a magnetic lead frame shifts its zero after the head is opened** (Opus only). Settles it:
   the lead-frame material on the sheet or the maker's package note for each candidate, then the exposure test of
   point 1.
7. **The Hall part's zero drift as a figure** (Grok 0.1–0.3 mT, run 3 0.55 mT, Codex 0.8–1.5 mT; the sheet: ±1 % ×
   VCC typical, no maximum). Settles it: the DRV5055's maker asked for a maximum of the quiescent-voltage drift over
   −40…+50 °C, or five parts measured over that range on the bench.
8. **Gain into the converter** (Opus 1 / Grok 1–4 / Codex 8–32 for the Hall part). Settles it: the converter's sheet
   line for its input range at each gain against the element supply as reference (the converter is not on file).

### 6. Figure

None. The comparison is per part and per model (a category on each axis); the plot standard draws curves over a
numeric axis, and the table in section 2 carries the dozen numbers a figure would show. Run 3's E2 already draws the
sheet values of the axial parts in % of metal.

### 7. Source table (sheets read for this note; PDFs read, not copied)

| Part | Sheet | Revision | Address |
|---|---|---|---|
| DRV5055 | TI DRV5055 Ratiometric Linear Hall-Effect Sensor | SBAS640C (revised June 2026) | https://www.ti.com/lit/ds/symlink/drv5055.pdf |
| DRV5057 | TI DRV5057 Linear Hall Effect Sensor With PWM Output | SBAS646A | https://www.ti.com/lit/ds/symlink/drv5057.pdf |
| TMAG5170 | TI TMAG5170 3D Linear Hall-Effect Sensor With SPI | SBASAF4 | https://www.ti.com/lit/ds/symlink/tmag5170.pdf |
| CT100 | Allegro CT100 1D Linear Sensor | CT100-DS Rev. 8 | https://www.allegromicro.com/-/media/files/datasheets/ct100-datasheet.pdf |
| A1308 / A1309 | Allegro A1308 and A1309 Linear Hall-Effect Sensor ICs | A1308-9-DS Rev. 15 | https://www.allegromicro.com/-/media/files/datasheets/a1308-9-datasheet.pdf |
| A1360 / 1 / 2 | Allegro A1360, A1361, A1362 | A1360-DS Rev. 5 (discontinued) | https://www.allegromicro.com/-/media/files/datasheets/a1360-1-2-datasheet.pdf |
| A1367 | Allegro A1367 | A1367-DS Rev. 14 | https://www.allegromicro.com/-/media/files/datasheets/a1367-datasheet.pdf |
| ALS31313 | Allegro ALS31313 | Rev. 9 | https://www.allegromicro.com/-/media/files/datasheets/als31313-datasheet.pdf |
| AA / AAH / AAL | NVE AA/AB-Series Analog Magnetic Sensors | SB-00-059 Rev H | https://www.nve.com/Downloads/analog_catalog.pdf |
| TMR2102 / 2103 / 2104 | MultiDimension TMR Linear Sensor sheets | v2.1.1 / v2.1.1 / v2.2.2 | https://www.dowaytech.com/en/index.php?c=download&id=2432 (2433, 2434) |
| MultiDimension Z-axis list | maker's product list, TMR Linear Sensors | page read for this note | https://www.dowaytech.com/en/sensor/magnetic_field_sensors.html |
| TLE493D-W2B6 | Infineon Low Power 3D Hall Sensor | Ver. 1.2 | https://www.infineon.com/assets/row/public/documents/24/49/infineon-tle493d-w2b6-datasheet-en.pdf |
| TLV493D-A1B6 | Infineon Low Power 3D Magnetic Sensor | Rev. 1.1 (third-party copy; the maker's page did not open) | https://www.blogs.uni-mainz.de/fb08-physics-halbach-magnets/files/2025/08/Infineon_TLV493D-1.pdf |
| TLI5590-A6W | Infineon TLI5590-A6W | Rev. 01.00 (third-party copy) | https://components101.com/sites/default/files/2024-01/tli5590-a6w%20-%20DataSheet.pdf |
| MLX90393 | Melexis | Revision 012 | https://www.melexis.com/-/media/files/documents/datasheets/mlx90393-datasheet-melexis.pdf |
| MLX90392 | Melexis | Revision 003 | https://www.melexis.com/-/media/files/documents/datasheets/mlx90392-datasheet-melexis.pdf |
| MLX91205 | Melexis | Rev 008 (old revision, third-party copy; the maker's site refused) | https://e2echina.ti.com/cfs-file/__key/telligent-evolution-components-attachments/00-52-01-00-00-04-02-67/MLX91205_5F00_Datasheet.pdf |
| TMR2185, TMR2584, TMR2583, A1324 | as run 3 | as run 3 | `../element_run_3/element_run_3.md` §7 |

Not read: TLE4997 (the maker's copy returned an error, a distributor copy timed out), HMC1021, the AKM HG / HW
Hall elements, the TMR2617S-AAC sheet. Lifecycle read on a sheet only for A1362 (discontinued) and one A1367
variant (discontinued); the rest not confirmed.

### 8. Not verified

- The models' physics claims that no sheet carries: the TMR free-layer tilt model, cross-axis pick-up of Z-axis TMR
  parts with flux guides, lead-frame magnetisation, pinned-layer turning. Recomputed where arithmetic, not checked
  where physics.
- The converter's input range per gain (not on file): the clipping statement in section 3 assumes ±V_ref ÷ gain.
- 316L resistivity is a textbook range (0.72–0.74 µΩ·m), not read on a material sheet.
- Nothing measured.
