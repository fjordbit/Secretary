"""Build the layered plan page from the import file. Usage: make_plan_layers.py <backup.json> <out.html>"""
import json, sys, html
d = json.load(open(sys.argv[1], encoding='utf8'))
T = {t['id']: t for t in d['tasks']}
GROUPS = [
    ("Rope and measured data", [1, 3, 27, 34, 110]),
    ("Magnetic circuit and magnets", [2, 5, 6, 26, 102, 103, 104]),
    ("Sensing elements and board", [4, 28, 29, 7, 8, 105, 106]),
    ("Housing, potting and mechanical", [9, 13, 14, 15, 107]),
    ("Data line, root box and controls", [10, 30, 11, 25, 31, 32, 108, 109]),
    ("Digital twin and screens", [21, 22, 23, 24, 19, 111, 112]),
    ("Test, calibration and installation", [12, 33, 16, 17, 18]),
    ("Specification, standards and documentation", [20, 101, 113, 114, 115]),
]
used = [i for _, ids in GROUPS for i in ids]
assert sorted(used) == sorted(T), (set(T) - set(used), [i for i in used if used.count(i) > 1])
DATES = [
    ("27 Nov", "Detailed plan circulated (target, not forced)"),
    ("30 Nov", "Magnetic analysis issued"),
    ("2 Dec", "Digital twin of the SWS, first version (target)"),
    ("4 Dec", "Board architecture with the specialist; potting method"),
    ("14 Dec", "Magnet geometry and grade final; controls rechecked"),
    ("15 Dec", "Orders: magnets (10 heads), control and logging hardware"),
    ("29 Jan", "Mechanical design released"),
    ("10 Mar", "Assembly starts"),
    ("24 Mar", "Readiness decision"),
    ("29-31 Mar", "First installation (six heads)"),
]
NEED = [
    "Board package for the specialist: new date (was due 22 Nov).",
    "Axial sensing element: Hall or TMR, before the board design.",
    "Magnet grade for the order of 15 Dec (N52 and N48SH are shown side by side; neither is selected).",
    "The link and the box at the winch: RS-485 to a root box, own line per half or one shared polled line.",
    "Stored data over the life of a rope: maximum, minimum and proposed size (own run, in preparation).",
]
e = html.escape
# Layer 4: the record of work done, read from the history file (third argument)
HIST_TO_GROUP = {
    "Specification and requirements": 7, "Magnetic circuit and FEM (2D, 3D)": 1, "Magnet grade and temperature": 1,
    "Sensing elements and converters (PCB architecture)": 2, "Potting / encapsulation": 3,
    "Data line, half firmware (C), root box, logger": 4, "Digital twin and simulator": 5,
    "HMI / presentation design": 5, "Prototype rig measurement and its analysis": 0,
    "Reviews by outside models (model rounds)": 7, "Pages / documentation": 7,
    "Standards (EN 12927, ISO 4309) reading": 7, "Tasks issued to colleagues (GitHub issues)": 7,
}
record = {i: [] for i in range(len(GROUPS))}; rulings = []; n_rows = 0
if len(sys.argv) > 3:
    sec = None; part = 0
    for line in open(sys.argv[3], encoding='utf8'):
        line = line.rstrip('\n')
        if line.startswith('## '): part = int(line[3]) if line[3].isdigit() else 0; sec = None
        elif line.startswith('### '): sec = line[4:].strip(); assert sec in HIST_TO_GROUP, sec; record[HIST_TO_GROUP[sec]].append((sec, []))
        elif part == 1 and sec and line.startswith('| ') and not line.startswith('| Dates') and not line.startswith('|---'):
            c = [x.strip() for x in line.strip('|').split('|')]
            record[HIST_TO_GROUP[sec]][-1][1].append(c[:3]); n_rows += 1
        elif part == 2 and line.startswith('- '): rulings.append(line[2:])
def rec_html(gi):
    out = ''
    for name, rows in record[gi]:
        if not rows: continue
        body = ''.join(f"<tr><td class='d'>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in rows)
        out += (f"<details class='task rec'><summary><span class='id'></span>Record: {e(name)}<span class='when'>{len(rows)} pieces of work</span></summary>"
                f"<table class='rec'><tr><th>When</th><th>What was done</th><th>Result</th></tr>{body}</table></details>")
    return out
def fmt(dt):
    y, m, dd = dt.split('-'); return f"{int(dd)} {['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][int(m)-1]}"
def task(t):
    done = t['status'] == 'Completed'
    cls = 'done' if done else ('crit' if t['priority'] == 'Critical' else '')
    mark = 'done' if done else f"{t['progress']} %"
    rows = [("Lead", t['owner']), ("Dates", f"{fmt(t['start'])} to {fmt(t['deadline'])}"), ("State", t['status']),
            ("Priority", t['priority']), ("Depends on", t['dependencies']), ("Risk or what is missing", t['risk'])]
    body = ''.join(f"<tr><th>{e(k)}</th><td>{e(v)}</td></tr>" for k, v in rows if v)
    return (f"<details class='task {cls}'><summary><span class='id'>{t['id']}</span> {e(t['task'])}"
            f"<span class='when'>{fmt(t['deadline'])} · {mark}</span></summary><table>{body}</table></details>")
def group(name, ids, gi=0):
    ts = [T[i] for i in ids]
    open_ = [t for t in ts if t['status'] != 'Completed']; done = [t for t in ts if t['status'] == 'Completed']
    nxt = min((t['deadline'] for t in open_), default=None)
    head = f"{len(open_)} open, {len(done)} done" + (f" · next date {fmt(nxt)}" if nxt else "")
    out = f"<details class='group'><summary><b>{e(name)}</b><span class='when'>{head}</span></summary>"
    if open_: out += "<h4>Open</h4>" + ''.join(task(t) for t in sorted(open_, key=lambda t: t['deadline']))
    if done: out += "<h4>Done</h4>" + ''.join(task(t) for t in done)
    r = rec_html(gi)
    if r: out += "<h4>Layer 4: everything done, piece by piece</h4>" + r
    return out + "</details>"
n_open = sum(1 for t in T.values() if t['status'] != 'Completed'); n_done = len(T) - n_open
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>SWS plan in layers</title><style>
:root{{--bg:#fff;--fg:#1c2530;--mut:#5b6875;--line:#d5dbe1;--card:#f5f7f9;--acc:#0b5cab;--crit:#b3541e;--ok:#2f7d4f}}
@media (prefers-color-scheme:dark){{:root{{--bg:#12171c;--fg:#e4e9ee;--mut:#9aa7b3;--line:#2c3742;--card:#1a2129;--acc:#6fb1f0;--crit:#e39a6b;--ok:#7cc79a}}}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,Segoe UI,Arial,sans-serif;margin:0;padding:24px 16px}}
main{{max-width:980px;margin:auto}} h1{{font-size:1.5rem;margin:0 0 4px}} h2{{font-size:1.1rem;margin:28px 0 8px}} h4{{margin:12px 0 4px;color:var(--mut);font-size:.85rem;text-transform:uppercase;letter-spacing:.04em}}
p.sub{{color:var(--mut);margin:0 0 16px}} .dates{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:8px}}
.dates div{{background:var(--card);border:1px solid var(--line);border-radius:6px;padding:8px 10px}} .dates b{{display:block;color:var(--acc)}}
details.group{{border:1px solid var(--line);border-radius:8px;margin:8px 0;padding:0 12px;background:var(--card)}}
details.group>summary{{padding:12px 0;cursor:pointer;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}}
details.task{{border-top:1px solid var(--line);padding:0 4px}} details.task>summary{{padding:8px 0;cursor:pointer;display:grid;grid-template-columns:2.4em 1fr auto;gap:8px;align-items:start}}
details.task.crit>summary{{border-left:3px solid var(--crit);padding-left:8px}} details.task.done>summary{{color:var(--mut)}} details.task.done .when{{color:var(--ok)}}
.id{{color:var(--mut);min-width:2.2em;display:inline-block}} .when{{color:var(--mut);white-space:nowrap;margin-left:auto;font-variant-numeric:tabular-nums}}
table{{border-collapse:collapse;margin:4px 0 12px 2.6em;font-size:.93rem}} th{{text-align:left;color:var(--mut);font-weight:500;padding:2px 14px 2px 0;vertical-align:top;white-space:nowrap}} td{{padding:2px 0}}
table.rec{{margin-left:0;width:100%}} table.rec td{{padding:3px 12px 3px 0;vertical-align:top;border-top:1px solid var(--line)}} table.rec td.d{{white-space:nowrap;color:var(--mut)}} table.rec th{{padding-bottom:4px}}
ol{{padding-left:1.3em}} footer{{color:var(--mut);font-size:.85rem;margin-top:28px}}
</style></head><body><main>
<h1>SWS plan in layers</h1>
<p class="sub">Draft, 26 Nov 2026. Layer 1: the dates. Layer 2: the eight areas, open one to see its tasks. Layer 3: open a task for lead, dates, dependencies and risk. Layer 4: inside each area, every piece of work done with its result. {n_open} tasks open, {n_done} areas of work done. Dates are targets: correct before fast. A task with a bar on the left is on the critical path.</p>
<h2>Layer 1 — the dates</h2><div class="dates">{''.join(f"<div><b>{e(a)}</b>{e(b)}</div>" for a, b in DATES)}</div>
<h2>Rulings and inputs needed</h2><ol>{''.join(f"<li>{e(x)}</li>" for x in NEED)}</ol>
<h2>Layer 2 to 4 — areas, tasks and the record</h2>{''.join(group(n, ids, gi) for gi, (n, ids) in enumerate(GROUPS))}
<h2>Rulings made so far</h2><details class='group'><summary><b>{len(rulings)} rulings, in date order</b><span class='when'>open to read</span></summary><ul>{''.join(f"<li>{e(x)}</li>" for x in rulings)}</ul></details>
<footer>Layer 4 holds {n_rows} pieces of work done between 22 Oct and 26 Nov 2026, each with its result; all figures are calculated unless marked measured. Work before 22 Oct is not in this record.Large installation: two sides, 102 winches, 6 stations, 204 SWS, 408 halves. Task numbers 1-20 are those of the schedule of 19 Nov; 21-34 are added; 101-115 are work done.</footer>
</main></body></html>"""
open(sys.argv[2], 'w', encoding='utf8').write(page)
print(len(page), 'bytes', n_open, 'open', n_done, 'done')
