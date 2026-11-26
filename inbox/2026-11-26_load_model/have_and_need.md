# Load on each rope during a lift: what we have and what we need

Kai, 26 Nov 2026. Not part of the SWS. Prepared so a model round can go out when the mechanical inputs are in.
Nothing here is sent anywhere.

## What Stian asked for

- A load value on each rope for each lift, simulated top-down, simplified but from first principles (for
  example a rigid platform), so nothing in it is wrong, only simplified.
- Later the real values come from the control lab simulator, or from the PLC / logger station in normal
  operation, over the correct protocols.
- Two things the control lab wants to see: **cut one line and see the result**, and **the load curve**: how
  the load is spread over the winches.
- Idea: one round with the newest Sol and one with Fable (API key) on how they would simulate it.

## The simplest correct model (Kai's sketch, to be challenged by the round)

- The platform is a rigid body with three movements: up/down, tilt along, tilt across.
- Each winch holds it through a spring: stiffness k = (number of rope falls) × E × A ÷ (free rope length).
  The free length changes with platform height, so k changes during the lift.
- The ship's weight comes down on the platform as a line of loads along the keel blocks.
- Solve the three movements so the forces and moments balance; the load on each winch follows.
- Cut one line: take that spring out and solve again. The neighbours take the load. A dynamic factor for the
  moment of the break is a separate, stated assumption.
- One step more real, when we have the numbers: the platform as a beam (or beams) on springs, not rigid. It
  needs the bending stiffness of the platform.

## What we have

| Item | Value | From |
|---|---|---|
| Winches | 102: two sides of 51, positions 1A–51A and 1B–51B; 6 stations of 17 | layout drawing; ruling 26 Nov |
| Length along the platform | 6 spans of 46.0 m marked along each winch row | layout drawing (Kai's reading) |
| Distance across | 42.3 m from the platform centre line to the station floor line; 31.3 m marked twice at the end | layout drawing (Kai's reading, to confirm what they measure) |
| Rope | 52 mm; 250 m of travel; 3.2 m/min normal, 5 m/min maximum | rulings 19–20 Nov |
| Reeving | several falls between an upper and a lower sheave block; about six sheaves seen | CAD pictures (Kai's reading, not counted exactly) |
| Drum | one layer of rope at most | Stian, 23 Nov |
| Bending cycles | counted in the PLC, written to the same server | ruling 20 Nov |

## What we need (mechanical inputs)

1. Number of rope falls per winch, and where the load cell sits (dead end, sheave pin, winch frame).
2. Rated load per winch and the lifting capacity of the whole platform.
3. Platform: weight, length, width, and whether it is one stiff piece or sections joined by hinges.
4. If not rigid: bending stiffness along and across (or the main beam sections).
5. Lift height, and the free rope length at the bottom and at the top.
6. Rope: metallic area and E-modulus (rope construction data, already asked for in issue 1).
7. Typical ships: weight, length, and the load along the keel (a docking plan or a typical block load curve).
8. How the winches are controlled together: level control, load sharing, limits and what trips.
9. What "cut a line" means in the control lab: one rope breaks, or one winch stops, or a signal is lost.
10. What the control lab simulator already computes, and in which form it can hand over the loads.
11. Load cell range, resolution and rate, and the protocol from the PLC or logger station.

## Can the round go out now?

- A round on the **method** could go out today: the model can be asked for with the numbers above as
  placeholders. It would give the structure and the list of inputs, not real loads.
- A round that gives **loads we can trust** needs items 1 to 7.
- The drawings and pictures do not leave the machine. A brief for outside models is written blind: no names,
  no site, numbers only, scanned before it goes.
- A Fable run on the API key gets a cost limit set before it starts.
