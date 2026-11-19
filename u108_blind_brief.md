# Blind brief: data path from the converters in a rope-monitoring head to a logging computer

You are asked for an independent engineering proposal. You know only what is written here. Do not guess who the
owner is. Say what you assume. Where you use a figure from a standard or a product class, say which and how sure
you are; you may look up public standards and typical data of product classes with general web queries.

## What exists (taken as certain)

- A monitoring head is clamped round a steel wire rope on a winch and reads magnetic field elements while the
  rope runs through it. A head is made of two halves. Each half has its own small electronics board.
- Per half: three 8-channel, 24-bit, simultaneous-sampling delta-sigma converters (ADS131M08 class) read over
  SPI by one microcontroller on the board. 16 of the channels are signals; the rest are spare or measure the
  bridge supply. In addition one or two digital temperature sensors per half (a 1-wire type such as DS18B20 is
  known to the owner; others may be better).
- The existing design input says: sampling should be tied to rope position, about one sample per 1 mm of rope;
  rope speed up to 15 m/min (so up to 250 samples per second per channel); one serial link per half, RS-422,
  4-wire plus 24 V supply in one shielded cable, 460.8 kbit/s or 1 Mbit/s; a "root box" at the other end;
  a 1 Hz timing edge from the root box to each half so that the two halves are aligned to well under 1 ms;
  0.2–0.4 W per half; no redundancy in the first revision.
- The owner's newer thoughts, not decided: a frame every 100 ms, perhaps every 50 ms ("the winch moves
  slowly"); RS-485 instead of RS-422 so that more than one head can share a line; category 7 cable; the root
  box as an industrial mini computer that receives the serial data, perhaps scales it, and sends it on over
  Ethernet (MQTT "or other") to a main logging computer where all processing is done; or instead a remote I/O
  station with a serial card, which the owner suspects is needlessly complex. The owner calls the box "more or
  less the transmitter of 1 to n".
- Installation A (first, a test, a few months away): 6 winches, one head per winch, 6 heads.
- Installation B (later): 51 winches, two heads per winch, 102 heads. Per winch then 64 signal channels of
  24 bits and 4 temperature values.
- The heads get a network of their own: a managed industrial Ethernet switch with two fibre uplinks.
- Logging may be done with a commercial high-speed process data acquisition system that the site already uses
  for other signals.
- The owner wants installation A to use exactly the same design and software as installation B.
- Environment: outdoors at sea, −40 to +50 °C, wet, salt, strong permanent magnets in the head, large electric
  winch drives nearby. Cable length from head to box is not known: treat 5, 30 and 100 m as cases.

## What is asked

1. The data path from the converters to the logging computer, as one proposal with its reasons, and the one or
   two serious alternatives you rejected and why. Cover: what the microcontroller in the half sends and when
   (raw samples or reduced; framing; time or position stamp; error check); the physical link from half to box
   (RS-422 point to point, RS-485 2-wire or 4-wire multidrop, or something else such as single-pair or standard
   Ethernet, CAN FD); how many halves or heads can share one line and at what cost; the box (what it must do and
   what it must not do); the protocol from box to logger; time alignment of the two halves of a head, of the two
   heads on a winch, and of all heads on a site; what happens on a lost frame, a lost link, a restart.
2. Sample rate. The design input (position-tied, up to 250 samples per second) and the owner's newer thought
   (a frame every 100 or 50 ms) differ. Say what each means for finding a fault that is about 10–20 mm long in
   the rope at rope speeds of 1, 5 and 15 m/min, and whether "sample fast in the half, send a frame every
   100 ms" reconciles them.
3. Traffic, with the arithmetic shown, as tables that can be plotted: bytes per frame and bits per second
   - per half, per head, per winch, per box, and for the whole of installation A and B;
   - for sample rates of 10, 20, 50, 100, 250 and 1000 samples per second per channel;
   - raw 24-bit samples against any reduction you propose;
   - on the serial link (with framing and start/stop bits) and on Ethernet (with protocol overhead, for MQTT
     and for one alternative), and the storage per hour and per day at the logger.
   Give the highest sample rate each serial option carries with a margin you name, for 1, 2 and 4 halves on one
   line, at 115.2 k, 460.8 k and 1 Mbit/s, and the cable lengths at which those rates are safe.
4. The temperature sensors: is a 1-wire part a sound choice here (conversion time, bus, noise near the
   converters), and what would you use instead if not.
5. One box per winch, one per group of winches, or none (heads straight onto the network): cost in parts and
   complexity, and what fails together.
6. The five things most likely to go wrong in this data path on a first installation, and the test that shows
   each before installation.
7. A list of what you had to assume, and the questions you would put to the owner, most important first.

Answer in at most 1 500 words plus tables. Plain words; define every abbreviation once. Do not select a
supplier or a product; name product classes. Say "I do not know" where that is the truth.
