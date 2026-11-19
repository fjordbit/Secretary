# Task note — the transmitter line as a running beta (code and simulator)

Status: a note for Stian to correct. Not a brief yet, nothing started. Written 19 Nov, evening.
The brief is written from this note once (a) Stian has corrected it and (b) the run on the transmitter line
(U109) has said which code already exists.

## What Stian asked for

Not only theory: the code for the line and a running simulator, as a beta, as part of the SWS digital twin.
If data cannot be generated fast enough, use tables.
Given: a rope 250 m long; ramp 1 second; maximum speed 5 m/min (confirmed by Stian). One pass of 250 m then
takes 50 minutes in real time, so the simulator must also run faster than real time.
Corrected by Stian the same evening: on the 52 mm project the platform moves 0.4 m/min and the rope at the drum
8 times that, 3.2 m/min. Rope speed is therefore a setting: 3.2 m/min as the normal case (250 m in 78 minutes),
5 m/min as the fast test case. The rope speed at the first installation (40 mm head) is not on record.

## What we know (from Stian today and the record)

- There is no code for any part of the line in the project today (found by the transmitter-line run): no
  firmware, no box, no logger, no averaging. The beta starts from nothing.
- One SWS = one head = two halves. Per half: 16 elements (8 radial, 8 axial), two 8-channel 24-bit
  converters, digital temperature.
- The half samples fast and sends a packet every 100 ms. About 250 samples per second per channel is the
  starting figure.
- One serial line per half to the box (RS-422 in the specification; a shared RS-485 line is the alternative).
  100 m of cable must hold.
- The box (the transmitter) receives, and passes the packets on over MQTT to one logger computer. All
  processing is in the logger.
- No encoder and no run signal on the first installation. Position comes afterwards from the data: the strand
  ripple, the ramps and the fixed length out and back.
- Not a safety system now; delay does not matter.
- First installation: 6 SWS. Later: 102 SWS, two per winch. Same design and software for both.

## What is not settled (the beta must leave these as settings, not build them in)

- Converter rate, line rate and the averaging filter (the running work gives the curves).
- The packet layout. The serial speed. One line per half or a shared line.
- One box per winch or one per SWS.
- The MQTT topics and payload. The logger: own code, or the commercial logging system.
- Temperature part.

## What we need: five pieces, each runnable alone

1. **The rope and head simulator (the twin's signal source).**
   A rope of 250 m with: the strand ripple; a list of faults at known positions (the test-rope fault list can
   be used); stretches with loss of metal; noise, slow drift, temperature; mains hum. A motion profile: ramp
   up, run, ramp down, out and back over the fixed length. Output: what each of the 32 elements reads at each
   instant, as converter counts. Either calculated live or read from tables made beforehand.
2. **The half.**
   Takes the counts at the converter rate, filters and averages down to the line rate, builds the packet every
   100 ms with counter, time and check. Written so that the same logic can later go into the microcontroller.
3. **The line.**
   A simulated serial line between half and box: limited to the chosen speed, with the possibility to drop or
   corrupt packets, to break the cable and to restart a half.
4. **The box (the transmitter).**
   Real code, meant to run later on the mini computer: receives the two halves (or four), checks, time-stamps,
   buffers when the network is down, publishes over MQTT, reports health.
5. **The logger side.**
   A broker and a logger: stores each run as a file, detects "moving" from the data, rebuilds position from the
   ripple and the fixed length, compares a run with the first run, and shows the traces.

## How it should look when it runs

- One command starts everything on one PC: simulator, two halves, line, box, broker, logger.
- A run is one lift: out and back. It can run in real time or faster than real time.
- A simple live view: the 32 channels, packets per second, bytes per second, lost packets, buffer level, disk
  used.
- After a run: the plots in the plot standard — a fault as the logger saw it against what the simulator put in;
  the position error against the true position; the traffic measured against the traffic calculated.
- Scaling test: 6 SWS, then 102 SWS, on the same PC or with the data from tables; measured traffic and disk
  growth.
- Fault tests as one-line commands: drop packets, break a line, stop the network for an hour, restart a half.

## What it must prove before it is called beta

- A 10 mm fault put in at 7.5 m/min comes out with its shape (amplitude kept above a figure to be set).
- A slow drift put in is still there at the logger (the averaging does not hide it).
- 50 Hz hum put in does not appear as a level change.
- Position from the data alone is within a figure to be set, over 250 m out and back.
- No packet is lost silently: every loss is counted and visible.
- The box rides through a network stop of a set length without losing data.
- Measured traffic and storage agree with the calculation.

## Open questions for Stian (one at a time)

1. (Answered: 5 m/min.)
2. (Answered: Python first, C for the half later.) Was: Python first, or the half in C from the start (as in the
   microcontroller)?
3. Where it lives: as a module of the twin in the project, beside the existing twin and Studio work?
4. Should the logger in the beta be our own code, or should it write a format the commercial logging system
   reads?

## Next step after the beta (Stian, 19 Nov evening)

- In the week of 23 Nov: raw element data from the prototype head (TMR elements), and a measurement of the same
  rope with a calibrated and approved rope tester. The tester gives a processed signal, not the raw one.
- The raw element data is then used to adapt the simulator: converter noise and the other effects seen in the
  real signal are put into the model. The tester's result is the reference for what is in the rope.
- Aim: a digital twin that is as good as current knowledge allows.
- For the beta this means: the simulator must be able to replay a recorded trace in place of the generated one
  (the "tables" mode), and its noise, ripple, drift and hum must be settings that can be fitted to a recording.
