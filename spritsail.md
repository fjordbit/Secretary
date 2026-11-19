# spritsail — U110 notes (the transmitter line as a running beta)

- Worktree C:/Users/stian/Prosjekter-u110, branch u110-line-beta from aa1eae5 (verified = tip of
  u109-transmitter-line). Adds only max/sws/line_beta/. Venv inside it (.venv, git-ignored), pip only.
- Kai's mid-run addition (tables replay a recording; disturbances as separate switchable settings; README
  "Fitting the simulator to a recording") done: table format in README, example table 0.5 s made by the
  simulator, test that table replay gives byte-identical frames.
- MQTT: real. amqtt (pip broker) on 127.0.0.1 inside run_beta; paho client. Found: amqtt can drop messages it has
  already PUBACKed if the sender disconnects within ms; the box's client waits 0.5 s after its last ack before a
  deliberate disconnect. Also found and fixed: a paho lock inversion (own lock held across client.publish).
- Bugs found in own code on the way: float32 running sum of ripple phase lost cycles past 2^14 rad (1.3 m error
  on 250 m); median of per-channel phase advance biased by ripple harmonics (5 % scale error); mains tone aliasing
  onto the 50 mm drift grid. All fixed; position now cleans 0.1 s phase blocks distorted by a passing wire.
- Line fault counting: a break that swallows a delimiter costs the next frame only if the box still holds open
  bytes; first version over-counted.
- Losses next to a restart fold into the box's restart-gap count (time-based), not the sequence-gap count.
- Position test (10 mm after registration vs true position) is expected to FAIL with the assumed 1 % pitch wave:
  registration aligns to the first run, so the first run's own error stays (offset of about -8 mm plus +-8 mm).
- Final: proof 7 of 8 pass; position 27.3 mm largest after registration (FAIL, figure 10 mm); constant pitch side
  figure 11.0 mm. Speed-up 67x over the real broker (85x in-process, generator alone 141x). 102 heads over amqtt:
  the broker could not keep up (11 841 of 122 400 reached the logger); in-process all 122 400.
- Reviewer (fresh agent, files only; ran the README from git archive in an empty folder): no blocking; started as
  written, 53 tests pass, numbers matched. Minors fixed: B1 skipped silently on short runs (README now says so),
  B1 note gap hard-coded, --proof ignored --set for the short tests. Not changed: storage +5.3 % with the CSV index
  (stated in README; owner's call), MQTT bytes counted by formula not on the wire, drift case easy (one rate,
  same temperature coefficient), "owner" kept (the brief asks for it), installation A/B labels kept (TL's).
