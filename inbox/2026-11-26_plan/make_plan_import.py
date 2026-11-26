import re, json, sys
src = open(sys.argv[1], encoding='utf8').read()
m = re.search(r'const embedded=(\[.*?\]);const embeddedNote=("(?:[^"\\]|\\.)*");', src, re.S)
tasks = json.loads(m.group(1)); note = json.loads(m.group(2))
assert len(tasks) == 20
def T(i, ws, task, owner, start, end, prog, status, prio, dep, risk):
    return dict(id=i, workstream=ws, task=task, owner=owner, start=start, deadline=end, progress=prog,
                status=status, priority=prio, dependencies=dep, risk=risk)
new = [
 # added, forward
 T(21,"Digital twin","Digital twin of the SWS, first version: large installation (102 winches, 204 SWS), each rope its own faults, main screen fed live, trainer screen","Stian","2026-11-23","2026-12-02",45,"In progress","High","Plant size corrected; twin fitted to measured data","Target date, not forced: correct before fast"),
 T(22,"Digital twin","Correct the plant to two sides (2 x 3 stations x 17 winches) and recompute all totals","Stian","2026-11-26","2026-11-27",20,"In progress","High","Layout drawing","Totals in notes were for one side only"),
 T(23,"Digital twin","Fit the twin to the prototype recording: ripple size, low-frequency noise, level shift with direction of travel","Stian","2026-11-26","2026-11-30",10,"In progress","High","Prototype recording (received)","Prototype is 40 mm with other elements; transfer to 52 mm is an assumption"),
 T(24,"Digital twin","Main screen (design version 3) fed live from the twin; trainer screen to place a fault on a chosen rope","Stian","2026-11-27","2026-12-01",15,"In progress","High","Task 22; presentation rulings","Presentation decisions still open"),
 T(25,"Data line","Root box data reduction: review from the measurement side (brief with pseudocode)","Henrik","2026-11-27","2026-12-04",0,"Not started","Medium","Brief read by Stian first","Dead band at rest may hide slow changes"),
 T(26,"Magnetic circuit","Steel near the SWS: geometry (issue 5), 3D run, term in the twin","Henrik / Stian","2026-11-25","2026-12-11",15,"In progress","High","Geometry; CAD pictures received 26 Nov","Fixed steel 143 mm from the rope; moving steel within 1 m"),
 T(27,"Prototype","Questions on the recording: travel length, speed, rope construction, strong-magnet steps, noisy radial channels","Henrik","2026-11-27","2026-12-04",0,"Not started","High","Three analyses (done)","Zero stays moved after a strong field; cause not separated"),
 T(28,"Sensor hardware","Rule on the axial sensing element: Hall or TMR","Stian","2026-11-27","2026-12-11",40,"In progress","Critical","Task 27; strong-field test","Needed before board design (task 8)"),
 T(29,"PCB","Board package for the specialist","Stian","2026-11-20","2026-12-01",0,"Not started","Critical","Architecture on record","Was due 22 Nov; task 7 depends on it"),
 T(30,"Controls","Propose the link and the box at the winch: RS-485 to a root box (own line per half, or one shared polled line) against RS-422 into a PLC rack as in the minutes","Stian","2026-11-26","2026-12-14",50,"In progress","High","Update and connection note; data line simulator","Minutes and design on record differ"),
 T(31,"Software","Root box logic in C++ (including the data reduction)","Stian","2026-12-03","2026-12-18",5,"Not started","Medium","Digital twin first version",""),
 T(32,"Software","Firmware update and connection design: eight open questions closed","Stian","2026-11-25","2026-12-14",40,"In progress","Medium","Task 30","Nothing on record for a failed update of the root box itself"),
 T(33,"Calibration","Acceptance, factory test and site test procedures; recalibration interval","To name","2027-01-04","2027-03-09",5,"Not started","High","EN 12927 reading (done)","Not started; needed before assembly"),
 T(34,"Rope testing","Second measurement of the same rope with the reference instrument","To name","2026-12-01","2027-01-15",0,"Not started","Medium","Instrument availability","Without it the twin has one measured source only"),
 # done
 T(101,"Done: Specification","Specification revisions 123-131, register of rulings, live parts table (28 parts)","Stian","2026-10-22","2026-11-20",100,"Completed","Medium","","Word master not yet updated by hand"),
 T(102,"Done: Magnetic 2D","In-house 2D checked against two other solvers (18 cases, within 0.33 mT)","Stian","2026-10-23","2026-10-26",100,"Completed","Medium","",""),
 T(103,"Done: Magnetic 3D","3D: stranded rope, broken wires, long loss, yoke groove, falsification run, 40 mm head on 38-40 mm rope (378 solves)","Stian","2026-10-26","2026-11-20",100,"Completed","High","","Real B-H data for the rope still missing"),
 T(104,"Done: Magnets","Magnet grades N52 and N48SH against temperature: knee checks, sun model, both shown side by side","Stian","2026-11-07","2026-11-19",100,"Completed","High","","Supplier data (issue 4) open"),
 T(105,"Done: Electronics","Converter architecture: two simultaneous 8-channel 24-bit converters per half (5 of 5 in a blind round), data sheets checked","Stian","2026-11-10","2026-11-20",100,"Completed","High","",""),
 T(106,"Done: Sensing elements","Sensing element candidates and placement on one thin board; two rounds, five answers","Stian","2026-11-12","2026-11-20",100,"Completed","High","","Axial element still open (task 28)"),
 T(107,"Done: Potting","Housing, sealing and resin options read against data sheets","Stian","2026-11-11","2026-11-19",100,"Completed","Medium","","No trial yet (task 9)"),
 T(108,"Done: Data line","Frame and line study; half core in C; running simulator of half, root box and logger","Stian","2026-11-10","2026-11-19",100,"Completed","High","","Position from ripple: 27 mm against a 10 mm target"),
 T(109,"Done: Data line","Root box data reduction (dead band, lossless compression, sending around movement) and firmware update note","Stian","2026-11-25","2026-11-25",100,"Completed","Medium","","Review pending (task 25)"),
 T(110,"Done: Prototype","Test procedure and rig sheet; prototype recording of 20 Nov analysed three times independently","Stian / Henrik","2026-11-12","2026-11-25",100,"Completed","High","","Questions open (task 27)"),
 T(111,"Done: Digital twin","Simulator of the large installation with each rope its own identity, temperature days and reduction, joined and tested (125 tests)","Stian","2026-10-29","2026-11-26",100,"Completed","High","","Was sized for one side; corrected in task 22"),
 T(112,"Done: Presentation","Screen design, two rounds, four designs; rulings on states and colours","Stian","2026-11-18","2026-11-23",100,"Completed","Medium","",""),
 T(113,"Done: Standards","EN 12927 chapter 14 and ISO 4309 read and mapped to requirements","Stian","2026-11-09","2026-11-18",100,"Completed","Medium","",""),
 T(114,"Done: Reviews","16 review rounds with outside models, each checked against data sheets or recomputed","Stian","2026-11-07","2026-11-20",100,"Completed","Low","",""),
 T(115,"Done: Documentation","Eleven pages for the team in three reading levels; last release 20 Nov","Stian","2026-10-29","2026-11-20",100,"Completed","Low","",""),
]
out = dict(tasks=tasks + new, meetingNote=note + "\nAdded 26 Nov: tasks 21-34 (new) and 101-115 (work done 22 Oct - 26 Nov). Large installation: two sides, 102 winches, 6 stations. Digital twin first version targeted 2 Dec; dates are targets, correct before fast.")
json.dump(out, open(sys.argv[2], 'w', encoding='utf8'), indent=2, ensure_ascii=False)
ids = [t['id'] for t in out['tasks']]
print(len(ids), 'tasks', len(set(ids)), 'unique ids')
