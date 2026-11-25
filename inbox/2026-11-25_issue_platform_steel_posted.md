# Posted 25 Nov as fjordbit/max issue #5, assigned hmssyncro

**Title:** Steel near the SWS during a lift: geometry needed for a 3D run

**Body:**

## Why

Earlier 3D runs showed that steel within about half a metre of the head shifts the standing field, by as much
as 1 to 8 % of metal. During a lift, a large flat steel structure on the platform comes from about 4 m to about
0.4 m from the SWS. Nothing on record describes it. We want to run it in 3D and, if it shows, put it into the
digital twin as a term that follows platform position.

## What is needed

A sketch with numbers is enough. A STEP export or coordinates are better if they exist.

Use this frame: origin at the centre of the SWS, **z** along the rope (up), **x** from the SWS towards the
structure at its closest, **y** to complete it.

1. **The structure that approaches**
   - Shape and size: width (y), height (z), thickness (x). If it is not a plain plate: the outline, and any
     stiffeners or openings within 1 m of the closest point.
   - Material (steel grade, or "structural steel").
   - Closest distance to the SWS centre, and at which platform position that happens.
   - How it moves relative to the SWS: distance against platform position (or against time at normal speed),
     from first approach to closest. Does it pass the SWS, or stop beside it?
   - Which side of the SWS it is on, relative to the cut plane between the two halves.

2. **The drum and other fixed steel**
   - Drum diameter and width, and the distance from the SWS centre to the nearest rope layer on the drum (one
     layer at most).
   - Any sheave, frame, bracket or guard within 1 m of the SWS: position and rough size.

3. **How the SWS sits**
   - Position along the rope between drum and platform (two distances).
   - Orientation of the cut plane (which way the two halves face).
   - Distance between the two SWS on the same rope.

4. **If available**
   - Any existing simulation or measurement of the field or of the structure's position during a lift.

## What comes back

A 3D result: the change at the sensing elements against distance (4 m to 0.4 m), for both magnet grades, and a
note on what it means for the zero. Calculated, not measured.
