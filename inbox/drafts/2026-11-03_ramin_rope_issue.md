# Draft — GitHub issue on fjordbit/max, for Ramin (posted by Kai on Stian's go)

Title: SWS: rope construction data for the 52 mm Powerplast (FEM input)

Assignee: raminhtmp (once the invitation is accepted)
Labels: sws, input-needed

---

The SWS 3D FEM now models a stranded 52 mm Powerplast rope with broken wires
(`tasks/reports/U16.md` on branch `u16-sws-fault-detection`). The rope
construction in the model is a placeholder, and it is the largest uncertainty in
the results. The manufacturer's data would replace it.

What we need, for the 52 mm Powerplast as used on our lifts:

1. **Construction:** number of outer strands, wires per outer strand and their
   diameters, lay (regular/lang, direction), whether the outer strands are
   compacted, and the inner rope (rotation-resistant core) construction.
2. **Plastic layer:** thickness and extent of the plastic between inner and
   outer rope (and any outer coating).
3. **Metallic cross-section:** steel area in mm² or the fill/C factor, so the
   loss-of-metallic-area percentages are right.
4. **Wire grade** (tensile class), and any magnetic data the supplier has,
   if at all.
5. The supplier's **datasheet or catalogue line** for the rope. If a Paraplast
   variant is in use or considered, the same for that.
6. **Discard criteria** we apply (ISO 4309 / EN 12927): the broken-wire count
   and spacing, if we have them on file.
7. Which rope the **Ø40 prototype head** was tested with (type and
   construction), so the prototype observations can be compared with the model.

Where the placeholders sit: `sws/3d/rope_construction.yaml` and the
`[UNVERIFIED]` section of `tasks/reports/U16.md`.

Current model assumptions, so you can see what is being replaced:
18 outer strands × 7 wires, 2.5 mm wires, straight lay, 1.0 mm jacket,
homogenised inner rope with fill 0.956.

Thanks,
Stian
