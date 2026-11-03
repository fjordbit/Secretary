# Draft — GitHub issue for Henrik (repo to be decided; posted by Kai on Stian's go)

Title: SWS: prototype noise floor and measurement data

Assignee: Henrik's GitHub user
Labels: sws, input-needed

---

The 3D FEM of the SWS head now gives signal levels for broken wires and loss of
metallic area (`tasks/reports/U16.md`, `U17.md`). Every margin in those reports is
measured against the specification's noise budget, 0.11 mT peak-to-peak, which is a
requirement, not a measurement. Your prototype is the only place a real number exists.

What would replace the assumption:

1. **Noise floor of the prototype electronics**, per channel (radial and axial):
   peak-to-peak and RMS with the rope stationary, and with the rope running at
   inspection speed. Sensor part number, ADC and sampling rate, filter bandwidth,
   and the mT-per-count scale so we can compare in mT.
2. **Raw recordings** behind those numbers, if you have them (CSV or whatever the
   logger writes), with a line on how each was taken.
3. **The prototype test cases:** rope type and construction, speed, the artificial
   faults (how many wires cut, where in the strand, gap), and the signal amplitude
   you saw for each. The notch comparison (with/without) belongs here too.
4. **Head details** not on the drawings: axial sensor radius used (36.5 mm?),
   magnet grade datasheet (N42?), sensor stand-off from the rope.

Upload: add files under `sws/data/prototype/` on a branch, or attach them to this
issue; either works. Mark anything estimated rather than measured.

Why it matters: if the real floor is above 0.11 mT, the smallest faults in
`U16.md` (single hidden wires, inner-rope wires) stop being detectable at 5 mm,
and the hardware selection (U9) has to start from your number, not the spec's.

Thanks,
Stian
