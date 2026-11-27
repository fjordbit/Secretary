# Blind brief: network and time base for a rope-monitoring system on a large lifting plant

You are asked for an independent engineering view. You know only what is written here. Do not guess who the
owner, the plant or the site is. Nothing below has been chosen; weigh the options openly. Say what you assume,
and write "I do not know" where that is the truth. Give numbers with their arithmetic. Mark every figure and
claim with its source: a named standard (number, part, year if you know it), a data sheet or product class,
"general practice", or "from memory". Name product classes, not suppliers; name a supplier only where a
feature exists from one supplier alone, and say so.

## What exists (taken as given)

**The plant.** A large lifting plant by the sea: 102 electric winches in two rows of 51. Each row is fed from
three motor control centres (cabinets with the drives and the control system for their winches). Cable runs
from a winch to its motor control centre, and between centres, range from some tens of metres to some hundreds
of metres. Outdoors, wet, salt air, a wide temperature range, large variable-speed winch drives nearby.

**The monitoring system.** Each winch has one steel wire rope. Each rope carries two magnetic monitoring heads;
each head is two halves with their own small board. So: 102 ropes, 204 heads, 408 halves.
- Each half sends its data on its own serial line (RS-422 or RS-485 class, a few hundred kbit/s) to a small box at its
  winch, here called the root box: one root box per winch, four halves per box, 102 root boxes in all. The box
  also supplies the halves with 24 V. The box is a small computer with Ethernet; how many Ethernet ports it has
  and how it is powered are not fixed.
- The halves have no clock time. The root box sends a 1 Hz timing edge to its halves on a separate pair; each
  half latches its sample counter on the edge and sends its sample index and the latched count. The root box
  maps these onto one time base (its own clock) and sends the data on, possibly reduced, to a monitoring logger
  (a server). The residual between halves on one box after this mapping is about 80 µs.
- Data rate on Ethernet before any reduction, from the design so far: about 0.11 Mbit/s per half, so about
  4 × 0.11 = 0.44 Mbit/s per root box and 408 × 0.11 ≈ 45 Mbit/s for the whole plant. A reduction in the box
  (dead band, lossless compression, sending only around rope movement) can lower this; by how much is not known.
- Sampling: 250 values per second per channel, by time (not triggered by position).
- Rope speed through the heads: normally about 3.2 m/min; 5 m/min is the fast case; an older design figure is
  15 m/min. The rope always travels the same fixed length out and back (250 m).
- Purpose: detect broken wires (local signals about 10–20 mm long along the rope) and slow loss of metal (found
  by comparing each run with the first run of the same rope, aligned along the rope to about 1 mm).
- Rope position: the monitoring system works it out afterwards from its own data (the rope strands give a
  steady ripple) and from proximity switches at each end of the travel. This is the base method and must work
  on both plants. The first plant has no encoder. On the large plant the control system has an encoder per
  winch, which the monitoring side could read if a link exists. Where the end switches are wired is not fixed.
- The monitoring system is not a safety system. Delay does not matter.

**The control side.** In the same motor control centre cabinets there is a separate control system (PLCs and
drives on their own network, protocol family not given) and a separate process data logger. The control system
knows each winch's drive speed, reads one load cell per winch (102 in all) and counts the rope's bending
cycles; it writes the bending cycles to the same server as the monitoring data, so that one screen shows both.
The monitoring side must never be able to disturb the control side.

**A first, small plant** comes before the large one: 6 winches, one head each (12 halves, 6 root boxes), and no
link to the control system at all. The owner wants the same design and software on both. On the large plant
the owner wants the load per rope, the lifting speed and the platform position shown and stored together with
the monitoring data, provided the link cannot disturb the control side. That wish is firm; how it is done is
open.

## What is asked

1. **Time source.** One time server for both the monitoring network and the control network, or separate ones;
   where it lives (in the monitoring logger, in the control system, a dedicated unit, or elsewhere) and what its
   reference is; SNTP / NTP against PTP (IEEE 1588, and which profile). First derive the accuracy really needed,
   with the arithmetic, for each of these: (a) two halves on one root box; (b) the two heads on one rope (same
   box); (c) root box to root box; (d) monitoring data to control-side data (speed, load, bending cycles, end
   switches); (e) monitoring data to load and platform position, for a correction of the readings for platform
   position (the steel of the platform passes 1 m to 4 m from a head and changes the reading slowly, as a slow
   effect over the whole lift). Use the rope speeds and the alignment along the rope given above. Then say what the root box does
   when the time source is lost, when it returns, and when its time steps (forwards or backwards).
2. **Keeping monitoring data apart from control data.** Separate fibres and switches, or VLANs on shared fibre
   with managed switches in each cabinet, or another way. Broadcast and multicast storm protection. For each:
   what a single failure takes down (one switch, one fibre, one power supply, one misconfiguration).
3. **Topology for the 102 root boxes.** Star from each box to its motor control centre, chains, rings, or a mix;
   redundancy and what it costs; how the boxes get power (and what that means for the halves' 24 V); how the six
   centres join each other and the logger; fibre against copper for each run length.
4. **Getting position, load, speed and platform position from the control side** without any path back that could disturb it:
   one-way transfer, a gateway, a read-only interface, the shared server, or another way. What protocol, what
   rate, what time stamp, and who owns the interface. Also what the first plant, with no link, must do instead.
5. **Rough cost** in parts and in commissioning hours for the plant of 102 winches, per option, in EUR, as
   ranges by product class. Say what the ranges rest on.
6. **What you would do differently** from the arrangement described, if anything, and why.

## Answer format (keep these headings and their order)

```
## 0. In short          (at most 8 lines; your recommendation per question, one line each)
## 1. Time source       (the accuracy table (a)-(e) with arithmetic; options table; loss / return / step behaviour)
## 2. Separation        (options table: how / single failures / storm protection / pros / cons)
## 3. Topology          (options table; power; fibre and copper; a small text diagram if it helps)
## 4. Control-side data (options table; protocol, rate, time stamp, owner; the first plant without a link)
## 5. Cost              (table: option / parts range / commissioning hours / what the range rests on)
## 6. What I would do differently
## 7. Unsure            (every point you are unsure of, each with what would settle it)
## 8. Sources           (standards with number and part; product classes; "from memory" where so)
## 9. Questions to the owner (most important first, at most 8)
```

Every options table has at least the columns: option / how it works / what one failure takes down / pros /
cons. Define every abbreviation once. Plain words. At most 2 500 words plus tables.
