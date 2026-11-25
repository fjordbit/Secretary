# Firmware update of the halves and the root box, and the connection to each root box

Design draft. Options side by side; nothing here is selected. Calculated, not measured. Words: SWS = the whole
product; head = the part on the rope, two halves; half = one of them, with its own board; root box = the box the
halves' lines end in. All figures: [update_calc.py](update_calc.py) → [update_calc.json](update_calc.json); every
constant there is marked REPO (from a note here), BUILT (measured on the PC build of the C half) or ASSUMED.

## In ten plain lines

1. Yes, updates are needed: the record already requires a bootloader with remote update through the root box.
2. Three things change over the years: the half's program, the root box's software, and settings such as the stored zero.
3. Settings and calibration need not be firmware; they can be a small data block, or live at the logger.
4. The half's program is small: the core built here is about 3 kB; a whole image is estimated at 16–64 kB.
5. Sent over the half's own line, 32 kB takes under a second; with a reply per piece it takes about 14 s.
6. Two program slots in the half keep the old program as a fall-back; one slot is cheaper but leaves a half blind if it fails.
7. The table in 2.4 shows what a power cut at each step leaves: the old program, the new one, or the bootloader asking for the image again.
8. For a screen to show the version of all 204 halves and 51 root boxes, the status message would carry each half's version.
9. The brief asks that an update never switches over during a rope run; with no link to the control system, the options are the SWS's own data, a local switch or an operator.
10. One network cable per root box (as on record) loses 2 SWS per cable fault; a chain of boxes uses fewer switch ports but can lose 34.

---

## 1. What needs updating at all

| Part | What can change | Expected how often (ASSUMED, general experience, nothing on record) | Can it be a setting instead? |
|---|---|---|---|
| Half: microcontroller program | bug fixes in read-out, framing, health bits; a new frame format; a new filter | rarely: a few times in the first year, then seldom | Half id, filter id, rate and filter code, decimation and samples per frame are already settings, not code: the C half takes them through `half_config_t` (`../../line_beta/c_half/README.md` l.43–50) and the frame names them in its rate and filter code (`../transmitter_line.md` §5, byte 7) |
| Half: bootloader | almost never; it is the part that must not fail | ideally never in the field | — |
| Half: converter set-up (gains) | gain per converter | when the sensing element type or range changes | Yes: CONFIG_SET, accepted only when the half is stopped (`../../hw-selection/sws_link_and_readout.md` l.266) |
| Half: calibration (stored zero, sensitivity, temperature coefficients) | per channel values | at commissioning and after a part change | Yes. Two places: (a) a data block in the half's flash, travelling with the hardware; (b) at the logger, keyed by the half's identity. The transmitter-line proposal and the beta have the box forward frames unchanged with no scaling (`../transmitter_line.md` l.357, `../../line_beta/linebeta/root_box.py` l.6); the owner's newer thought has the box "perhaps" scale (`parts.yaml` X01). Without scaling in the box or half, the half never needs the values for its own work |
| Root box: software | reception, checks, buffering, forwarding, time, health, firmware distribution (spec rev131 l.415); operating system patches if it runs a general-purpose system | more often than the half; if a general-purpose system, patches every few months | Port-to-half map, topics, buffer size are settings |
| Root box: images it holds for the halves | the halves' images | with each half release | — |

## 2. The half

**On record.** A Cortex-M class microcontroller with hardware SPI, DMA, one UART for RS-422 and hardware CRC;
"Bootloader with remote firmware update via the root box" (spec rev131 l.347). No microcontroller is named
(`../../parts_table/parts.yaml` U01). The command FW_UPDATE goes to the bootloader and "carries its own image CRC,
checked before the switch" (link note l.264, l.268). The line is RS-422, 4-wire, 460.8 kbit/s or 1 Mbit/s (spec
l.412), plus a sync pair (spec l.419); the link note reads the commands from the box as "full duplex" (l.262), that
is a pair each way.

**Image size.** The C half built here with GCC 16.2 (x86-64, `-std=c11`): `size` gives 3 068 bytes of text for
`half_core.o` at `-O2`, 2 600 at `-Os` (the C half's README gives 2 568 at `-Os`; flags differ slightly). This is
the core only, on a PC. No cross compiler is on this machine, so the image for a microcontroller is **estimated**:
core about 3 kB + hardware layer, start-up, command and update receiver. The cases carried through are 16, 32 and
64 kB (ASSUMED).

### 2.1 Memory layout options

| | A. Two image slots with fall-back | B. One slot with a fixed bootloader | C. One slot, fall-back kept in the root box |
|---|---|---|---|
| How | bootloader + slot 1 + slot 2 + config block + state block; new image written to the slot not running; bootloader boots the newer one on trial and goes back if it is not confirmed | bootloader + slot + config + state; the slot is erased and rewritten | as B in the half; the box keeps the old image and sends it back if the new one fails |
| Flash, 32 kB image, 16 kB bootloader | 16 384 + 2 × 32 768 + 8 192 = 90 112 B (fits 128 kB) | 16 384 + 32 768 + 8 192 = 57 344 B (fits 128 kB) | as B |
| Flash, 64 kB image, 16 kB bootloader | 16 384 + 2 × 65 536 + 8 192 = 155 648 B (needs 256 kB) | 16 384 + 65 536 + 8 192 = 90 112 B (fits 128 kB) | as B |
| Flash, 64 kB image, 32 kB bootloader (with a signature check) | 32 768 + 2 × 65 536 + 8 192 = 172 032 B (needs 256 kB) | 32 768 + 65 536 + 8 192 = 106 496 B | as B |
| Half measuring during the download | can be: the old program runs; but see the flash note below | no: the program is erased first | no |
| Failed new image | goes back to the old one by itself | half stays in the bootloader, sends no data, until an image arrives | half sends no data until the box resends the old image |
| Variants | run the image where it lies (two builds, one per slot address) or copy / swap into one run slot (needs a resumable copy, below) | — | — |

The config and state blocks are 4 kB each (ASSUMED; the flash's erase unit sets the real figure, and some parts
have 2 kB pages, others sectors of 16–128 kB, which can make a "4 kB" block a whole sector). The general practice
of the two-slot layout (trial boot, the new image confirms itself, otherwise the bootloader goes back on the next
reset; a state record at the end of a slot) is taken from the design document of a widely used open-source
microcontroller bootloader (MCUboot `docs/design.md`), read for the general method only.

**Flash note.** On many single-bank parts the CPU stalls while flash is erased or written. The half's read-out runs
from an interrupt every converter result (link note §3); a stall longer than the result period loses results,
which the half would flag (health bit 5 MISSED, link note l.313). So "measuring during the download" holds only for a
part with two flash banks (read while write), or with the flash routine and the interrupt both in RAM. Not on record;
it follows from the class, and the part decides.

### 2.2 How the image travels

The downlink pair (root box to half) is separate from the uplink pair (spec l.412 "4-wire"; link note l.262 "full
duplex"), so the half's frames keep
flowing while the image arrives. The link note's commands are "framed as the data frames (COBS, CRC-32C)" and the
result is "acknowledged in the health and aux fields of the next frame" (l.263–264). Chunk (ASSUMED): 256 bytes
payload + 12 bytes header (image id, offset, length) + 4 bytes CRC-32C = 272 bytes; COBS adds 1 + ⌊272 / 254⌋ = 2
bytes and the delimiter 1, so 275 bytes on the wire; 8N1 = 10 bits per byte.

| Image | Chunks | Streamed, 460.8 kbit/s | Streamed, 1 Mbit/s | One reply per chunk in the next 100 ms frame | Reply only in the turning aux slot (24 slots) |
|---|---|---|---|---|---|
| 16 kB | 64 | 64 × 275 × 10 / 460 800 = 0.38 s | 0.18 s | 0.38 + 64 × 0.1 = 6.8 s | 0.38 + 64 × 2.4 = 154 s |
| 32 kB | 128 | 128 × 275 × 10 / 460 800 = 0.76 s | 0.35 s | 0.76 + 128 × 0.1 = 13.6 s | 308 s |
| 64 kB | 256 | 256 × 275 × 10 / 460 800 = 1.53 s | 0.70 s | 1.53 + 256 × 0.1 = 27.1 s | 616 s |

Two ways to send, side by side: (1) **stop and wait**: one chunk, wait for the reply in the next frame; simple,
slow because frames come only ten a second (`../transmitter_line.md` l.74); (2) **stream, then repair**: send all
chunks, the half reports at the end which offsets it is missing (a bitmap), the box resends those; under 2 s for
64 kB at 460.8 kbit/s if the flash can keep up. Flash write and erase time is not counted (it depends on the part).
Measurement paused or not: during the download, see the flash note; during the switch, yes, paused for one restart
(boot count +1, a new segment at the box, link note l.294, l.352).

### 2.3 Check, switch, confirm, fall back

- **Check before switch** (on record: image CRC, link note l.264). Options added: a header in the image with
  hardware id, image length, version and the CRC, so a wrong image for the hardware is refused before the switch;
  the bootloader checks the CRC again on every boot, not only once.
- **Switch**: one write of a "pending" mark in the state block, then a reset.
- **Confirm after first good run**: what "good" means is open. Options: (a) the program confirms itself after it has
  started its converters and sent N frames with no CRC fault and no watchdog reset; (b) the root box confirms it by
  command after it has received, say, 60 s of good frames from that half; (c) confirm only after the first rope run
  registers against the reference run. (a) is fastest; (b) and (c) catch a program that runs but sends nonsense.
- **Fall-back**: option A goes back by itself if an unconfirmed trial boot resets (or after a set number of tries);
  options B and C need the root box to resend.

### 2.4 Power loss at each step

The half takes its 24 V from the root box over the same cable (spec l.349); a root box restart may also cut the
halves' supply (whether its 24 V outputs stay on through a restart is not on record).

| Step | A. Two slots: state after power loss | A. Recovery | B / C. One slot: state after power loss | B / C. Recovery |
|---|---|---|---|---|
| 1. Image arriving | old program, other slot partly written | old program runs; box resends from the start or the missing offsets | slot erased or partly written: no program | bootloader comes up, reports "no valid image", box resends; half blind meanwhile |
| 2. Image complete, CRC checked, not marked | old program; new image complete | box sends the switch again | new image complete, not marked valid | bootloader re-checks CRC on boot, then runs it or asks again |
| 3. Marked pending | new image starts on trial at the next power-up | as a normal trial | — (no separate step) | — |
| 4. Copy or swap into the run slot (copy variant only) | half-copied slot | bootloader resumes the copy from a progress record in the state block; without that record the half can end with no program | — | — |
| 5. Trial run, not yet confirmed | new image, unconfirmed | next boot is a trial again or a fall-back to the old one, by the rule set (2.3) | new image, no old one in the half | if the new one fails: box resends the old image (option C), else the half stays down |
| 6. Confirmed | new image; old kept as fall-back | none needed | new image | none needed |

## 3. The root box

**On record.** "firmware distribution to the halves" is a root box task (spec l.415); one Ethernet port, PoE
powered, one managed, rate-limited switch port per root box (spec l.414). The box's own update is not on record. The
box itself is open: a box with detection and 4 ports (specification) or an industrial mini computer that forwards
(owner's newer thought), `parts.yaml` X01.

**Its own update, options.** (1) Two system partitions with fall-back (the same idea as option A, on a general-purpose
system: write the inactive one, boot it on trial, go back if it does not confirm). (2) Update of the application only
(the receiving and forwarding program, a package or container) on a fixed base system. (3) Whole image by a person on
site (USB or memory card). (4) No field update of the box at all; replace the box. While the box restarts it receives
nothing: the halves either keep sending into an idle port (if the box's 24 V outputs stay on) or are unpowered (if
they drop, 2.4). A half keeps only its two frame buffers (2 × 1 229 bytes, C half README l.110), which at ten frames
a second is 2 × 100 ms = 200 ms of data (derived here), so a box update is a data gap the length of its restart.
That is one reason the brief's "never during a rope run" (5) applies to the box too.

**Order of updating.** If the frame format does not change, either order works. If it does, the box goes first and
must accept both formats: the beta's box (`root_box.py` l.169) drops every frame whose type byte is not the one it
knows and counts it as "wrong half", so a half updated first to a new type would vanish from an old box. Halves
first is possible only when the new half keeps the old frame type.

**Mixed versions.** One half new, one old in a head: the data are still usable if the frame format and the
rate-and-filter code agree; in the transmitter line's frame (type 0x11, `../transmitter_line.md` l.322–326,
the one the beta and the C half build) byte 0 is "type / version" and byte 7 the rate and filter code. The link
note's earlier per-sample frame (type 0x01, l.290) also has "type / version" in byte 0, but byte 7 there is part of
the health word (l.293); the two formats differ. Must the frame carry the software version too? It
already can: aux slot 0 is "firmware id" (link note l.325, set at start-up l.141), u16, one slot per frame in
turn, so it comes round every 24 / 10 = 2.4 s at ten frames a second. What the slot holds is not on record. Options:
(a) a build number (0–65 535); (b) major and minor, 8 bits each; (c) the low 16 bits of the image CRC (two
different images share it with a chance of 1 in 65 536). Spare aux slots exist (14, 16, 19, 22, 23, link note
l.327), so a second slot could carry the other half of a 32-bit id, the bootloader version or the configuration
check sum.

## 4. Version numbering and the status message

Version numbering is not on record. Options: (a) three numbers, major.minor.patch, where major changes with the frame
format; (b) one rising build number; (c) date-based. Kept apart in every option: hardware revision, bootloader
version, program version, frame format (byte 0), configuration check sum.

The status message on record (proposal): `sws/…/<box>/status`, retained, "online, firmware, configuration"
(`../transmitter_line.md` l.371–372). For the screen to show every half it would carry, per box: box software and
system versions, images held for the halves; per half: port, half id, hardware revision, bootloader version,
program version, active slot and whether a fall-back is present, image check sum, configuration check sum, update
state (idle / receiving n % / checked / on trial / confirmed / failed and why). Size (ASSUMED 200 bytes per half,
300 for the box's own part): 4 × 200 + 300 = 1 100 bytes per box; × 51 = 56 100 bytes for the large installation,
negligible. First installation: 12 halves.

## 5. Who may start an update, signing, and never during a rope run

**Who and from where, options.** (a) An operator at the screen of the logger or server, with a named role; the box
takes update commands only from that server's address on its managed port. (b) A service person on site, at the box.
(c) From outside the installation: needs remote access, which is not on record and is a separate question.

**Check sum or signature, options.**

| Option | Protects against | Does not protect against | Cost |
|---|---|---|---|
| Image CRC only (on record) | corruption on the line, a half-written image | a wrong image, a deliberately altered image | none beyond the record |
| CRC + header (hardware id, version, length) | the above + wrong image for the hardware, accidental downgrade | deliberate alteration | a few bytes, a check in the bootloader |
| Signature checked in the root box; halves check CRC + header | an altered image arriving over the network | an altered image put on the box itself | key handling at the release side; verification on the box |
| Signature checked in each half's bootloader | the above, even with a compromised box | a stolen signing key | larger bootloader (ASSUMED 32 kB in place of 16 kB, table 2.1), slower check at boot, key in every half |

**Never during a rope run.** Given: the first installation has no link to the control system; rope position comes
from the proximity sensors at each end of the travel and from the SWS's own data. Ways for the system to know,
options (not exclusive): (1) the SWS's own data: the "moving" detector from the strand-ripple envelope, which
the record places at the logger (`../transmitter_line.md` l.378–380); either the logger tells the box, or (an option
added here) the same detector also runs in the box; with a hold-off (for example no movement for some minutes)
before a switch is allowed; (2) the proximity sensors at the travel ends, if their state reaches the box (how it
would is not on record); (3) a local maintenance switch on the root box, wired to one of its two isolated digital
inputs (a hardware hook on record, spec l.419); (4) an operator confirmation at the screen; (5) the half refuses the
switch unless it is stopped, as it already refuses CONFIG_SET (link note l.266). The download itself could run during
a rope run if the flash allows it (2.1 flash note); only the switch would be held.

## 6. The connection

**On record.** One Ethernet port per root box, PoE powered, one managed, rate-limited switch port per root box
(spec l.414); one root box per hoist, up to four halves (spec l.402); each half on its own line to the box (spec
l.268, l.408). Given in the brief (not from the specification): large installation 3 main stations × 17 winches =
51 winches = 102 SWS = 204 halves; first installation 6 SWS = 12 halves. One box per winch (spec l.402) = 51 boxes,
102 / 51 = 2 SWS per box. Traffic per box: 22.2 Mbit/s (`../transmitter_line.md` l.79, installation B, 250 per
second) / 51 = 0.435 Mbit/s.

| | One cable per root box (on record) | Root boxes chained, one chain per main station | Chain closed into a ring | One box per head |
|---|---|---|---|---|
| Switch ports | 51 | 3 | 6 | 102 |
| Cables to or between boxes | 51 | 3 × 17 = 51 (shorter) | 3 × 18 = 54 | 102 |
| SWS lost per cable fault | 2 | worst 17 boxes × 2 = 34; mean over the 17 links (17 + 1) / 2 = 9 boxes × 2 = 18 | 0 for one fault | 1 |
| Load on the busiest cable | 0.435 Mbit/s | first link 17 × 0.435 = 7.4 Mbit/s | 7.4 Mbit/s on fault | 0.218 Mbit/s |
| Power | PoE from the switch (on record) | PoE does not pass down a chain: local power or PoE pass-through in each box | as chain | PoE, twice the ports |
| Needs in the box | one Ethernet port | two ports and a switch in each box | two ports and a ring-capable managed switch in each box | as on record |

A fault in the central switch takes out everything on it in every option. The 1 Hz edge is per box in every option;
a "sync-out to a second root box" is a hardware hook on record (spec l.419).

**Update traffic against data traffic on the same port.** The port is rate-limited; the limit is not on record.
Images for four halves, 4 × 32 kB = 131 072 bytes = 1.05 Mbit: 1.05 s at 1 Mbit/s, 0.10 s at 10 Mbit/s. A box
system image (ASSUMED 20 / 100 / 500 MB) at 10 Mbit/s: 16 / 80 / 400 s (100 MB × 8 / 10 Mbit/s = 80 s); at
1 Mbit/s ten times that. The data stream per box is 0.435 Mbit/s, so a limit of 1 Mbit/s leaves about half for an
update while data flows. Data flow during a rope run; the downloads may overlap a run in some options of (5), the
switches do not. The halves' images go on
over RS-422, not over Ethernet.

## 7. Scenarios for the simulator (input for a later unit; nothing built here)

| Scenario | Expected end state |
|---|---|
| Good update of one half | new version in aux slot 0 and in the status message; one restart (boot count +1, one new segment); confirmed; old kept (A) |
| Broken image (CRC wrong) | refused before the switch; old program runs (A) or bootloader waits for a resend (B / C); status "failed: check"; no restart in A |
| Power lost mid-download | as table 2.4 step 1; after power returns: old program (A) or bootloader asking (B / C); the box resends and the update completes |
| Power lost in the trial run | as table 2.4 step 5: trial again or fall-back by the rule; never a half with no program in A |
| New image fails to confirm (resets in a loop) | A: back on the old image after the set number of tries, status "failed: not confirmed"; C: box resends the old image |
| One half left on the old version | both halves stream; status shows the two versions; if frame formats differ, the box accepts both or flags the old one |
| Wrong image for the hardware | refused by the header check before the switch; status "failed: hardware id"; old program runs |
| Update asked during a rope run | switch held until stopped (5); download may proceed; status "waiting: rope moving" |
| Root box restarts during distribution | halves lose supply if the 24 V drops (2.4); each half ends in a state of table 2.4; the box resumes |
| A chunk lost on the line | stream-then-repair: the half reports the missing offset, the box resends it; stop-and-wait: the chunk is repeated |

## 8. Open, for the owner

1. Two program slots in each half, or one slot with the fall-back held in the root box?
2. Must a half keep measuring while an image downloads (then a two-bank part), or may it pause?
3. How does the box know the rope is not running: own data, end proximity sensors, a local switch, or an operator?
4. Who may start an update, and from where: the screen, on site only, or also from outside?
5. Check sum and header only, or a signature, and checked where: box only or every half?
6. One network cable per root box as on record, or a chain or ring per main station?
7. What goes in the firmware id slot and how versions are numbered?
8. Does the root box get field updates of its own software, or is it replaced?

## What is not done

The image size for a microcontroller is estimated (no cross compiler; no part named); flash write and erase times
are not counted; the rate limit of the switch port is not on record; nothing was run in the simulator.
