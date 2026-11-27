Subject: SWS: steel near the head and movement of the head. What we found, and what we need from you

Hi,

We have calculated in 3D how steel near the SWS changes its readings, and how much it matters if the head
moves sideways. Below: what we found, what we propose, and a numbered list of what we need from you. Three
pictures with the questions marked are attached, and four result figures.

Everything is calculated, not measured. The sizes are read off the CAD pictures and the steel properties are
placeholders, so the numbers are a first screening. Each effect is given as the percent of rope metal it would
be mistaken for. The fault we design for is 1 % of metal lost. Steel nearby always looks like metal GAINED.
Two numbers a / b are the two magnet grades, N52 / N48SH.

1. WHAT WE FOUND

  Steel wall, 1 x 1 m, 143 mm from the rope centre      2.1 / 2.1 %
  The same wall at 300 mm                               0.55 / 0.55 %
  The same wall at 600 mm                               0.09 / 0.10 %
  Holder plate 300 x 300 mm at 143 mm:
    non-magnetic stainless (relative permeability 1.1)  under 0.01 %
    magnetic stainless (relative permeability 50)       0.59 / 0.58 %
    plain steel                                         0.90 / 0.88 %
  Platform plate 986 mm below the head (service)        0.13 / 0.13 %
  Platform plate at 400 mm                              0.60 / 0.61 %
  Neighbouring rope fall at 200 mm                      0.71 / 0.71 %
  One neighbouring fall on each side                    1.34 / 1.34 %

  - The effect is almost the same on all sixteen positions round the rope. So averaging round the rope does
    not remove it. The good side: the comparison between positions, which finds broken wires, hardly sees it.
  - Steel close by also makes the head about 3 % more sensitive (3.4 / 3.2 % for the wall at 143 mm).

2. HOW WE REMOVE IT

  - Steel that does not move (the beam behind the rope, the holder, the neighbouring falls) gives a fixed
    offset. We take a zero on site, once, and it is gone. The beam about 14 cm away we cannot move, and we do
    not need to: it is fixed.
  - The platform is the only steel that moves during a lift. The system knows where the platform is, so we
    subtract its effect by position. With that correction 10 % wrong, 0.013 % is left at 986 mm.
  - We do not propose a steel shield round the head. It removes most of the effect, but it halves the signal
    for lost metal.
  - Where the layout allows, ferromagnetic steel 300 mm or more from the rope centre is better.

3. STAINLESS STEEL FOR THE HOLDER, ARM AND PLATE (proposal)

  - Austenitic stainless, EN 1.4404 (316L). It stays non-magnetic better than 1.4301 (304) after bending and
    machining, and it resists sea air.
  - Not duplex, not ferritic and not martensitic grades (for example 1.4462, 1.4016, 1.4021): they are
    magnetic and act like plain steel here.
  - Write the limit into the drawing: relative permeability 1.1 or lower, checked on the finished part (a
    simple hand-held permeability indicator does it). Cold forming and welds raise the permeability, so the
    check is on the finished part, not on the plate as bought.
  - Bolts, pins and the spring near the head in A4 (316) as far as strength allows. Tell us which parts must
    be hardened or spring steel, with size and position: we then put them in the model.
  - Where stainless meets the carbon steel of the beam, or aluminium: insulating sleeves and washers, so the
    joint does not corrode.

4. MOVEMENT OF THE HEAD

  - Tilt alone is small: 0.03 % at 5 degrees, 0.15 % at 10 degrees (next to the wall at 143 mm).
  - Sideways movement TOWARDS steel is what matters: about 0.02 % per millimetre at 143 mm, so 20 mm gives
    about 0.45 %. At 300 mm from the steel it is about six times smaller.
  - Movement that is the same in every lift is not a problem: it is in the reference runs. Movement that
    differs from lift to lift is.
  - If needed, we think of a simple angle sensor in the vertical pin of the holder (picture 1, A), or a
    clip-on measurement used only during commissioning to see how much the head really moves. We would rather
    not add parts if the movement is small or the same every time.

5. WHAT WE NEED FROM YOU (numbers as in the pictures where they apply)

  The holder (picture 1)
   1. A: does the arm turn on the vertical pin? Through how many degrees? Is there room for a small angle
      sensor (a potentiometer or a contactless one) on that pin?
   2. B: the spring arm: travel in mm, spring force, and what the spring is there to do.
   3. C: is the block fixed to the head, or can the head turn on the horizontal pin?
   4. D: the planned material of holder, arm, plate, pins, spring and bolts.
   5. E: the 143 mm is from the rope centre to which surface, and what is that part made of?
   6. The distance from the centre of the head up or down to the point it swings about.

  Movement (picture 2)
   7. How many millimetres does the rope move sideways at the head during a lift (arrow 1), and towards or
      away from the beam (arrow 2)? An estimate is fine.
   8. When does it happen: at start and stop, with load, with wind, at certain platform heights?
   9. Is it the same in every lift, or does it differ?
  10. Does the head tilt, and about which axis? Roughly how many degrees?

  Steel around (pictures 2 and 3)
  11. The beam behind the rope: distance from the rope centre, plate thickness, height and width of the face,
      steel grade.
  12. Distance between the rope falls at the height of the SWS (we assumed 200 mm).
  13. The platform: distance below the SWS in the NORMAL top position and in the bottom position (we have
      986 mm for the service position); plate thickness, steel grade, size of the opening for the ropes.
  14. The lower sheave block: how close to the SWS does it come, and its size and material.
  15. Any other steel within 600 mm of the head that the pictures do not show.

  The second proposed position
  16. Where is the second proposed position for the SWS? Please send the same for it: the three pictures with
      dimensions, and points 5 and 11 to 15.

  Format: dimensions written on pictures are enough. A STEP file of the area round the head is better, if it
  is allowed to send one.

This continues the task already on GitHub (issue 5, geometry for the 3D run). Answers can go there or by mail.

Thank you,
Stian
