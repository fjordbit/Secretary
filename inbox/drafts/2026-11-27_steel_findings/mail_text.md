Subject: SWS: today's findings on steel near the head. Angle first, then distance

Stian, all of today's steel numbers in one place, angle first as you asked. Six figures attached. Everything is
calculated, not measured; sizes are read off the CAD pictures and the materials are placeholders. Numbers are
N52 / N48SH, as the percent of rope metal the effect would be mistaken for (the reference fault is 1 % of metal
lost). I traced the wall, platform and neighbour numbers from the raw result files myself; the holder, tilt and
shift numbers are the builder's, checked by its reviewer. Kai

1. ANGLE

1a. Tilt of the head alone (the head tips, its centre stays where it is), beam at 143 mm:
    2 degrees    0.005 %
    5 degrees    0.03 %
    10 degrees   0.15 / 0.15 %
    Small. It grows with the square of the angle.

1b. Angle at the pivot pin (the arm turns and carries the head toward the beam). This is the one that matters,
    because the angle becomes a distance: movement = arm length x sin(angle). At 143 mm from the beam the
    reading changes about 0.022 % per mm. THE ARM LENGTH IS NOT KNOWN; three lengths shown:

    Angle     Arm 150 mm          Arm 300 mm          Arm 500 mm
    0.5 deg   1.3 mm   0.03 %     2.6 mm   0.06 %     4.4 mm   0.10 %
    1 deg     2.6 mm   0.06 %     5.2 mm   0.12 %     8.7 mm   0.19 %
    2 deg     5.2 mm   0.12 %     10.5 mm  0.23 %     17.4 mm  0.38 %
    5 deg     13.1 mm  0.29 %     26 mm    0.58 % *   44 mm    0.96 % *
    10 deg    26 mm    0.57 % *   52 mm    1.15 % *   87 mm    1.9 % *
    * beyond the 20 mm that was calculated; straight-line estimate, the real value is somewhat larger.

    So with a 300 mm arm, plus or minus 1 degree is already 0.12 %, and plus or minus 5 degrees is more than
    half the fault we look for. The angle is what to know.

1c. What an angle reading at the pin buys (simulated, beam at 143 mm, arm 500 mm assumed):
    Movement the same in every lift, 20 mm, no angle reading       about 0.001 % left (the reference runs remove it)
    Movement differing between lifts by 4 mm, no angle reading     0.05 % left
    Movement differing between lifts by 9 mm, no angle reading     0.13 % left
    Movement differing between lifts, WITH an angle reading        about 0.02 % left (with the angle known to 0.1 degree)
    Without an angle reading the error passes 0.1 % when the head's position differs by about 7 mm between lifts.
    Beam at 300 mm instead: 37 mm of difference leaves 0.08 % without, 0.004 % with.

1d. Tuning. The angle sensors would not need tuning one by one. In the calibration run the head is moved by
    hand through its travel while the rope stands still, and the system records the SWS reading against the
    raw sensor value. That curve is the correction. Sensor zero, gain and mounting angle are all inside it, so
    nothing is trimmed by hand. What the sensor must be is repeatable: about 0.1 degree over plus or minus 10
    degrees, which is half a percent of its range.

2. DISTANCE

2a. Head moved toward the beam (beam at 143 mm):
    5 mm     0.11 / 0.10 %
    10 mm    0.22 / 0.21 %
    20 mm    0.46 / 0.44 %
    Movement along the beam, not toward it, gives almost nothing.

2b. Steel beam or wall, 1 x 1 m, 20 mm thick, distance from the rope centre:
    143 mm   2.10 / 2.09 %
    300 mm   0.55 / 0.55 %
    600 mm   0.09 / 0.10 %
    Fixed, so it is removed by the zero taken in place. Next to it the head is also 3.4 / 3.2 % more sensitive.

2c. Holder plate 300 x 300 x 15 mm at 143 mm, by material (relative permeability):
    1.1  non-magnetic stainless, annealed      0.00 %
    2    stainless after cold work or welding  0.04 / 0.03 %
    5    the same, worse case                  0.12 / 0.12 %
    50   magnetic stainless                    0.59 / 0.58 %
    plain steel                                0.90 / 0.88 %

2d. Platform plate below the head (the only steel that moves during a lift):
    400 mm    0.60 / 0.61 %
    700 mm    0.27 / 0.28 %
    986 mm    0.13 / 0.13 %   (service position)
    2000 mm   0.01 %
    4000 mm   0.00 %

2e. Neighbouring rope falls:
    one at 200 mm   0.71 %      one each side at 200 mm   1.34 %
    one at 300 mm   0.28 %      one each side at 300 mm   0.54 %
    one at 400 mm   0.14 %      one each side at 400 mm   0.27 %

3. WHAT REMOVES WHAT

    Fixed steel (beam, holder, neighbours)   zero taken in place at the calibration run
    Platform                                 subtracted by platform position; 10 % wrong leaves 0.013 % at 986 mm
    Movement that repeats every lift         the reference runs
    Movement that differs between lifts      an angle reading at the pin, or a guide, or more distance
    Averaging round the rope                 removes nothing: steel shifts all sixteen positions alike
    A steel shield round the head            removes most, but halves the signal for lost metal: not proposed

4. PROPOSAL AS IT STANDS (for you to decide)

    Holder and arm in non-magnetic stainless (EN 1.4404 / 316L), permeability 1.1 or lower checked on the
    finished part. Start without an angle sensor. At the calibration run, clip on a gauge and measure how far
    the head really moves and whether it repeats. Fit an angle reading at the pin, or a guide, only where the
    movement toward steel nearer than 300 mm differs between lifts by more than about 5 mm.

5. NOT KNOWN, AND IT DECIDES THE ANSWER

    The arm length. How far the head really moves and in which direction. Whether it is the same in every lift
    or changes with the load of the vessel. All three are in the questions to Henrik and the mechanical
    colleague. A run on which kind of angle sensor fits (digital, contactless, not disturbed by the magnets,
    needing no trimming) is started.

Kai
