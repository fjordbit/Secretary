"""Radial stack, 52 mm rope in the shared Ø60 SWS head: one dimensioned figure.

Every number is from the max repo (read-only); file:line in 2026-11-18_radial_stack_52mm_sources.md.
Run: C:/Users/stian/Prosjekter-u41/max/.venv/Scripts/python.exe 2026-11-18_radial_stack_52mm.py
"""
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge

OUT = Path(__file__).with_suffix(".png")

# --- sizes (mm), see sources list ---
R_ROPE = 26.0          # 52 mm rope
R_ROPE4 = 27.04        # rope new at +4 %
R_FREE = 30.0          # free bore Ø60 = guard inner face
T_GUARD = 2.0          # guard under the magnets
R_SEAT = 32.0          # magnet seat Ø64
LM_DRAWN = 20.5        # drawn baseline
LM_MIN = 15.8          # smallest in the documents (spec decided table, N52)
T_YOKE = 12.0
Z_MAG = (50.0, 90.0)   # magnet at z = 50 ... 90
R_DIE5, R_DIE3 = 31.0, 29.0
R_AXIAL = 36.5
R_CARRIER = (30.0, 52.5)

C = dict(rope="#8a8f98", guard="#6fa8dc", magnet="#e06666", yoke="#5b5b5b", liner="#f6b26b",
         recess="#fff2cc", die="#cc0000", move="#b4d7a8", carrier="#d9d2e9", ink="#1a1a1a", warn="#b45f06")
FS = 17

fig = plt.figure(figsize=(16, 31), dpi=100)
fig.patch.set_facecolor("white")
gs = fig.add_gridspec(4, 2, height_ratios=[7.2, 10.0, 6.2, 7.6], hspace=0.2, wspace=0.12,
                      left=0.06, right=0.98, top=0.958, bottom=0.01)
fig.suptitle("52 mm rope: what sits between the rope and the sensors (sizes in mm)",
             fontsize=27, fontweight="bold", y=0.99)


def dim(ax, x, r0, r1, text, col=C["ink"], tx=None, ty=None, ha="left", fs=FS, lw=2.0):
    """Radial dimension arrow at x from r0 to r1, label at (tx, ty)."""
    ax.annotate("", xy=(x, r1), xytext=(x, r0),
                arrowprops=dict(arrowstyle="<|-|>", color=col, lw=lw, shrinkA=0, shrinkB=0, mutation_scale=16))
    if text:
        ax.text(x + 0.6 if tx is None else tx, (r0 + r1) / 2 if ty is None else ty, text, color=col,
                fontsize=fs, ha=ha, va="center")


# ================= Panel A: half section to scale =================
ax = fig.add_subplot(gs[0, :])
ax.set_title("A. Half section along the rope, to scale (upper half; the head is mirrored at z = 0)",
             fontsize=19, loc="left")
ZL, ZR = -14, 140
ax.set_xlim(ZL, ZR); ax.set_ylim(18, 68); ax.set_aspect("equal")
r_mo = R_SEAT + LM_DRAWN
ax.add_patch(Rectangle((ZL, 18), 106 - ZL, R_ROPE - 18, color=C["rope"], alpha=0.55, lw=0))
ax.add_patch(Rectangle((-50, R_CARRIER[0]), 100, R_CARRIER[1] - R_CARRIER[0], fc=C["carrier"], ec="#7a6aa6",
                       lw=1.2, ls="--", alpha=0.6))
ax.add_patch(Rectangle((Z_MAG[0], R_FREE), 40, T_GUARD, color=C["guard"]))
ax.add_patch(Rectangle((Z_MAG[0], R_SEAT), 40, LM_MIN, color=C["magnet"]))
ax.add_patch(Rectangle((Z_MAG[0], R_SEAT + LM_MIN), 40, LM_DRAWN - LM_MIN, fc=C["magnet"], alpha=0.35,
                       hatch="//", ec="white", lw=0))
ax.add_patch(Rectangle((ZL, r_mo), 90 - ZL, T_YOKE, color=C["yoke"]))
ax.axhline(R_FREE, xmin=0, xmax=(106 - ZL) / (ZR - ZL), color=C["guard"], ls=":", lw=1.6)
ax.plot([ZL, 106], [R_ROPE4] * 2, color="#333", ls="--", lw=1.2)
# sensors
ax.plot([0], [R_DIE5], "o", ms=12, color=C["die"])
ax.plot([0], [R_DIE3], "o", ms=10, mfc="white", mec=C["die"], mew=2)
ax.plot([-4, 4], [R_DIE5, R_DIE5], "s", ms=7, color="#990000")
ax.plot([0], [R_AXIAL], "D", ms=10, color="#7f6000")
ax.axvline(0, color="#999", lw=1, ls="-.")
# labels inside regions
ax.text(40, 21.5, "52 mm rope (radius 26)", fontsize=FS, ha="center", va="center", color="white", fontweight="bold")
ax.text(70, 40, "magnet", fontsize=FS + 1, ha="center", color="white", fontweight="bold")
ax.text(40, r_mo + T_YOKE / 2, "yoke (steel)", fontsize=FS, ha="center", va="center", color="white")
ax.text(30, 45.0, "sensor carrier space\nr 30 to 52.5, |z| < 50", fontsize=FS - 1, ha="center", va="center",
        color="#4b3f72")
ax.text(1.5, R_AXIAL + 1.6, "axial sensor r 36.5\n(\"unverified\" in the document)", fontsize=FS - 3,
        color="#7f6000", va="bottom")
ax.text(1.0, 50.5, "sensor plane z = 0", fontsize=FS - 3, ha="left", va="top", color="#555")
ax.text(58, 29.0, "guard 2", fontsize=FS - 3, ha="center", va="top", color="#1c4587")
# dimensions at the magnet (right of it)
dim(ax, 95, R_SEAT, R_SEAT + LM_DRAWN, "", col=C["magnet"])
ax.text(96.5, 42.5, "magnet thickness\n15.8 to 20.5 by grade\nand document\n(no grade selected)",
        fontsize=FS - 1, color=C["magnet"], va="center")
dim(ax, 95, r_mo, r_mo + T_YOKE, "", col=C["yoke"])
ax.text(96.5, r_mo + 6.5, "yoke wall 12.0 (12.1)", fontsize=FS - 1, color=C["yoke"], va="center")
dim(ax, 112, 18, R_FREE, "", col=C["guard"])
ax.text(113.5, 24.5, "free bore Ø60\n(r 30, guard face)\nmagnet seat Ø64", fontsize=FS - 1,
        color="#1c4587", va="center")
ax.text(12, R_ROPE4 + 0.35, "rope new at +4 %: r 27.04", fontsize=FS - 4, va="bottom", color="#333")
ax.text(ZL + 1, R_FREE + 0.35, "r 30", fontsize=FS - 4, va="bottom", color="#1c4587")
# zoom markers
for zc, lab in ((0, "C"), (70, "B")):
    ax.add_patch(Rectangle((zc - 3, 24), 6, 10, fill=False, ec="black", lw=2))
ax.text(-3.5, 34.4, "zoom C", fontsize=FS - 3, ha="right", va="bottom")
ax.text(66.5, 34.4, "zoom B", fontsize=FS - 3, ha="right", va="bottom")
ax.set_xlabel("z along the rope (mm); magnets at z = 50 to 90, pole spacing 100", fontsize=FS - 2)
ax.set_ylabel("r from rope centre (mm)", fontsize=FS - 2)
ax.tick_params(labelsize=FS - 4)
ax.set_xticks([0, 25, 50, 75, 90]); ax.set_yticks([20, 26, 30, 32, 40, 50, 52.5, 60, 64.5])

# ================= zoom panels =================
def zoom_axes(pos, title):
    a = fig.add_subplot(pos)
    a.set_xlim(0, 20); a.set_ylim(24.5, 33.6)
    a.set_title(title, fontsize=19, loc="left")
    a.set_xticks([]); a.tick_params(labelsize=FS - 3)
    a.set_yticks([25, 26, 27, 28, 29, 30, 31, 32, 33])
    a.set_ylabel("r (mm)", fontsize=FS - 2)
    a.grid(axis="y", color="#ddd", lw=0.8)
    return a


# ---- B: at a magnet / pole ----
b = zoom_axes(gs[1, 0], "B. At a magnet (z = 70)")
b.add_patch(Rectangle((0, 24.5), 6, R_ROPE - 24.5, color=C["rope"], alpha=0.6))
b.add_patch(Rectangle((0, R_FREE), 6, T_GUARD, color=C["guard"]))
b.add_patch(Rectangle((0, R_SEAT), 6, 1.6, color=C["magnet"]))
b.plot([0, 6], [R_ROPE4] * 2, color="#333", ls="--", lw=1.5)
b.text(3, 25.2, "rope", ha="center", fontsize=FS, color="white", fontweight="bold")
b.text(3, 28.0, "open gap\n(air)", ha="center", va="center", fontsize=FS)
b.text(3, 31.0, "guard", ha="center", va="center", fontsize=FS, color="white", fontweight="bold")
b.text(3, 32.8, "magnet", ha="center", va="center", fontsize=FS, color="white", fontweight="bold")
dim(b, 6.6, R_ROPE, R_FREE, "")
b.text(7.1, 29.15, "free gap 4.0 to a\ncentred new 52 mm rope", fontsize=FS - 1, va="center")
dim(b, 6.6, R_ROPE4, R_FREE, "", lw=1.4)
b.text(7.1, 27.5, "2.96 if the rope\nis at +4 %", fontsize=FS - 2, va="center", color="#333")
dim(b, 6.6, R_FREE, R_SEAT, "")
b.text(7.1, 31.05, "guard 2.0, non-magnetic\n(spec, register: 1.5 to 2)", fontsize=FS - 2, va="center")
b.text(7.1, 32.75, "magnet inner face r 32 (Ø64)", fontsize=FS - 2, va="center")
b.text(0.2, 30.15, "free bore Ø60", fontsize=FS - 4, va="bottom", color="#1c4587")
# liner question
b.add_patch(Rectangle((15.2, 28.0), 1.6, 2.0, fc=C["liner"], hatch="xx", ec=C["warn"], lw=1.5))
b.text(19.8, 25.0, "Liner here?\nCurrent documents:\nno liner at the\nmagnet; Ø60 is the\nfree bore.\n"
       "One superseded note:\n\"4 mm gap incl.\n~2 mm wear liner\"\n(orange box).\nDOCUMENTS DIFFER",
       fontsize=FS - 4, color=C["warn"], ha="right", va="bottom", linespacing=1.05)

# ---- C: at the sensor plane ----
c = zoom_axes(gs[1, 1], "C. At the sensor plane (z = 0), between the magnets")
c.set_ylim(22.3, 33.6)
for x0, lab in ((0, "geometry stack"), (10.5, "spec floor stack")):
    c.add_patch(Rectangle((x0, 22.3), 4, R_ROPE - 22.3, color=C["rope"], alpha=0.6))
    c.text(x0 + 2, 25.2, "rope", ha="center", fontsize=FS, color="white", fontweight="bold")
    c.text(x0 + 2, 33.45, lab, ha="center", va="top", fontsize=FS, fontweight="bold")
# geometry stack: liner 1.5 + recess 2.5 + die 1.0
c.add_patch(Rectangle((0, 26.0), 4, 1.5, color=C["liner"]))
c.add_patch(Rectangle((0, 27.5), 4, 2.5, color=C["recess"], ec="#bf9000"))
c.add_patch(Rectangle((0, 30.0), 4, 1.0, color="#cfe2f3", ec="#3d85c6"))
c.plot([2], [31.0], "o", ms=13, color=C["die"])
c.plot([0, 4], [R_ROPE4] * 2, color="#333", ls="--", lw=1.5)
c.text(2, 26.4, "liner", ha="center", va="center", fontsize=FS - 2)
c.text(2, 28.75, "recess", ha="center", va="center", fontsize=FS - 2)
c.text(2, 30.5, "package", ha="center", va="center", fontsize=FS - 3)
dim(c, 4.4, 26.0, 27.5, "1.5", fs=FS - 1)
dim(c, 4.4, 27.5, 30.0, "2.5", fs=FS - 1)
dim(c, 4.4, 30.0, 31.0, "1.0", fs=FS - 1)
dim(c, 6.6, 26.0, 31.0, "5", fs=FS + 1, col=C["die"])
c.text(2, 31.2, "element r 31", fontsize=FS - 3, color=C["die"], va="bottom", ha="center")
# floor stack: movement 3 + guard 1 + die 0.7
x0 = 10.5
c.add_patch(Rectangle((x0, 26.0), 4, 3.0, color=C["move"]))
c.add_patch(Rectangle((x0, 29.0), 4, 1.0, color=C["guard"], alpha=0.7))
c.add_patch(Rectangle((x0, 30.0), 4, 0.7, color="#cfe2f3", ec="#3d85c6"))
c.plot([x0 + 2], [30.7], "o", ms=13, color=C["die"])
c.text(x0 + 2, 27.5, "rope\nmovement", ha="center", va="center", fontsize=FS - 2)
c.text(x0 + 2, 29.5, "guard", ha="center", va="center", fontsize=FS - 2)
dim(c, x0 + 4.4, 26.0, 29.0, "3", fs=FS - 1)
dim(c, x0 + 4.4, 29.0, 30.0, "1", fs=FS - 1)
dim(c, x0 + 4.4, 30.0, 30.7, "0.7", fs=FS - 2)
dim(c, x0 + 6.6, 26.0, 30.7, "4.7", fs=FS + 1, col=C["die"])
for a_ in (c,):
    a_.axhline(R_DIE5, color=C["die"], lw=1, ls=":")
    a_.axhline(R_DIE3, color=C["die"], lw=1, ls=":")
    a_.axhline(R_FREE, color="#1c4587", lw=1.2, ls="--")
c.text(10.3, R_DIE3 + 0.08, "3 mm floor: r 29", fontsize=FS - 4, color=C["die"], ha="right", va="bottom")
c.text(10.3, R_DIE5 + 0.08, "5 mm design: r 31", fontsize=FS - 4, color=C["die"], ha="right", va="bottom")
c.text(10.3, R_FREE + 0.08, "r 30 = free bore\nat the magnets", fontsize=FS - 4, color="#1c4587",
       ha="right", va="bottom")
# stand-off marks: rope surface to element, and rope surface to the first solid surface it can touch
c.text(0.1, 22.5, "stand-off: rope to element 5.0\nrope to first solid surface: 0\n(liner face at the rope surface)",
       fontsize=FS - 3, color="#cc0000", va="bottom", fontweight="bold",
       bbox=dict(fc="white", ec="#cc0000", lw=1))
c.text(10.6, 22.5, "stand-off: rope to element 4.7\nrope to first solid surface: 3\n(guard face, r 29)",
       fontsize=FS - 3, color="#cc0000", va="bottom", fontweight="bold",
       bbox=dict(fc="white", ec="#cc0000", lw=1))
c.text(10.0, 32.1, "DOCUMENTS DIFFER: liner + recess + package (status \"assumed\")\n"
       "vs movement + guard + die depth (spec); no decision on file",
       fontsize=FS - 4, color=C["warn"], ha="center", va="bottom")

# ================= D: end view =================
d = fig.add_subplot(gs[2, 0])
d.set_aspect("equal"); d.set_xlim(-62, 62); d.set_ylim(-60, 60); d.axis("off")
d.set_title("D. End view of the sensor ring (z = 0)", fontsize=19, loc="left")
d.add_patch(Circle((0, 0), R_ROPE, color=C["rope"], alpha=0.6))
d.add_patch(Circle((0, 0), R_DIE5, fill=False, ec=C["die"], ls=":", lw=1.2))
d.add_patch(Circle((0, 0), 52.5, fill=False, ec=C["yoke"], lw=3))
d.plot([-58, 58], [0, 0], color="black", lw=2, ls="--")
d.text(58, 1.5, "split", fontsize=FS - 3, ha="right", va="bottom")
for i in range(16):
    ph = math.radians(11.25 + 22.5 * i)
    d.plot([R_DIE5 * math.cos(ph), 50 * math.cos(ph)], [R_DIE5 * math.sin(ph), 50 * math.sin(ph)],
           color="#3d85c6", lw=3)
    d.plot([R_DIE5 * math.cos(ph)], [R_DIE5 * math.sin(ph)], "o", color=C["die"], ms=7)
d.text(0, -10, "rope", ha="center", va="center", fontsize=FS, color="white", fontweight="bold")

e = fig.add_subplot(gs[2, 1]); e.axis("off")
e.text(0.0, 1.0,
       "End view (D): 16 positions, 22.5° apart,\n"
       "8 per half, first 11.25° from the split,\n"
       "none on the split. Each position is a spoke\n"
       "board carrying one radial and one axial\n"
       "sensor at its inner edge.\n\n"
       "Not in the documents:\n"
       "- what fills the recess (only \"room\" for parts)\n"
       "- the carrier liner bore between the magnets\n"
       "- a liner at the magnets (current documents)\n"
       "- spoke board thickness and axial length\n"
       "- which stand-off stack the carrier follows",
       fontsize=FS - 1, va="top", ha="left", linespacing=1.3, transform=e.transAxes)

# ================= F: what the free gap must swallow =================
f = fig.add_subplot(gs[3, :]); f.axis("off"); f.set_xlim(0, 1); f.set_ylim(0, 1)
f.set_title("E. What the 4.0 mm free gap at the magnets must swallow (52 mm rope, Ø60 free bore)",
            fontsize=19, loc="left")
X = (0.0, 0.38, 0.57, 0.72)
rows = [
    ("Item", "Value", "Gap left", "Where in the documents", True, None),
    ("Free gap, new 52 mm rope, centred", "4.0", "4.0", "p52 design §4; design inputs §1", False, None),
    ("Rope diameter, +0 to +4 % (maker)", "54.08 mm, -1.04", "2.96", "spec open items; register R9", False, None),
    ("   or +5 % (older note, unverified)", "54.6 mm, -1.30", "2.70", "stand-off brief; spec rev history", False, "differ"),
    ("Off-centre, installation target", "0.5", "2.46 / 2.20", "spec §1 precondition", False, None),
    ("   or sideways movement, literature", "2 to 3", "0.96 to -0.30", "register R18; stand-off findings", False, "red"),
    ("Grease, lubricant, dirt", "no allowance", "-", "spec: \"wipeable\", no size given", False, "missing"),
    ("Ice on the rope", "no allowance", "-", "spec open item: scraper, larger gap or heat", False, "missing"),
    ("Protruding broken wire", "no allowance", "-", "spec: loose end at a pole touches guard", False, "missing"),
    ("Liner wear", "not in the documents", "-", "no liner at the magnets in current documents", False, "missing"),
]
y = 0.95
for it, val, left, src, head, flag in rows:
    col = {"red": "#cc0000", "missing": C["warn"], "differ": C["warn"]}.get(flag, C["ink"])
    w = "bold" if head else "normal"
    f.text(X[0], y, it, fontsize=FS - 1, fontweight=w, va="top")
    f.text(X[1], y, val, fontsize=FS - 1, fontweight=w, va="top", color=col if flag in ("missing",) else C["ink"])
    f.text(X[2], y, left, fontsize=FS - 1, fontweight="bold" if not head else w, va="top", color=col)
    f.text(X[3], y, src, fontsize=FS - 4, va="top", color="#444", fontweight=w)
    y -= 0.083
f.text(0.0, y - 0.01,
       "Worst case in the documents: rope at +4 to +5 % and 3 mm movement leaves -0.04 to -0.30 mm: the rope touches the guard.\n"
       "With the 0.5 mm centring target it leaves 2.2 to 2.5 mm, with nothing set aside for grease, ice, wire ends or wear.\n"
       "Gap left after the off-centre rows is counted at +4 % / +5 %. Between the magnets (C, geometry stack) the liner face sits at the\n"
       "nominal rope surface: a rope at +4 % already presses 1.04 into the liner. +5 % vs +4 %: DOCUMENTS DIFFER.",
       fontsize=FS - 3, va="top", color="#222", linespacing=1.3)

fig.savefig(OUT, dpi=100)
print(OUT)
