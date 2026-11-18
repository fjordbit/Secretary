"""52 mm rope: radial and axial sensor on one spoke board, placements A and B, to scale (mm).

Numbers from the documents listed in 2026-11-18_spoke_board_52mm_sources.md (file:line there).
Nothing is selected. Sizes not in the documents are labelled on the figure.
Run: C:/Users/stian/Prosjekter-u05/max/.venv/Scripts/python.exe 2026-11-18_spoke_board_52mm.py
"""
import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import patches, transforms
from matplotlib.lines import Line2D

OUT = Path(__file__).with_suffix(".png")

# ---- numbers from the documents (see sources file) ----
R_ROPE = 26.0            # 52 mm rope
LINER = 1.5              # geometry stack, status A
RECESS = 2.5             # geometry stack, status A
R_FACE = R_ROPE + LINER + RECESS   # 30.0: face nearest the rope (stand-off = 4.0 + e)
R_REF = 31.0             # 5 mm reference
PITCH = 22.5
ARC_31 = 12.17           # 2*pi*31/16
# placement A, TMR2185G LGA4L 2.0 x 1.5 x 0.73, element 0.6-0.85 from the edge, 0.16-0.18 below top
LGA_L, LGA_W, LGA_H, LGA_DEPTH = 2.0, 1.5, 0.73, 0.17
A_E = (0.60, 0.85)
# placement B, TMAG5253 X2SON-4 1.40 x 1.10 x 0.4, element 0.115-0.145 below top; cross tab 0.50-0.75 from edge
X2_L, X2_W, X2_H = 1.40, 1.10, 0.40
B_RAD_E = (0.115, 0.145)
B_AX_E = (0.50, 0.75)
# DRV5055 SOT-23 (DBZ): body 2.80-3.04 x 1.20-1.40, height <= 1.12, 2.10-2.64 across the leads
SOT_L, SOT_W, SOT_H = 3.04, 1.40, 1.12

# ---- drawing-only assumptions (labelled on the figure) ----
T_BOARD = 1.6            # board thickness: NOT in the documents
T_TAB = 0.8              # tab thickness: NOT in the documents
TAB_W = 1.8              # radial tab width: documents give only ">= part, 1.10-1.40"
CROSS_TAB_LEN = 2.8      # cross tab size: NOT in the documents
Z_AX_B = 1.2             # z of the cross tab: NOT in the documents

C_ROPE, C_LINER, C_BOARD, C_PART = "#9a9a9a", "#e8d9b5", "#5f9e6e", "#2b2b2b"
C_TAB, C_EL, C_MOD, C_DIFF = "#8cc49a", "#d62728", "#7b3fa0", "#e07b00"
FS = 12

plt.rcParams.update({"font.size": FS, "font.family": "DejaVu Sans"})
fig = plt.figure(figsize=(16, 24), dpi=100)
gs = fig.add_gridspec(4, 2, height_ratios=[0.82, 0.70, 0.34, 0.78], hspace=0.17, wspace=0.07,
                      left=0.045, right=0.985, top=0.915, bottom=0.012)
fig.suptitle("52 mm rope: where the radial and the axial sensor sit on one spoke board\n"
             "(to scale; nothing is selected)", fontsize=22, fontweight="bold", y=0.985)
fig.text(0.5, 0.94, "All sizes in mm. Red dot = sensing element (bar = range in the documents).  "
         "Blue arrow to the rope = senses radial.  Orange ⊙ = senses axial (along the rope).  "
         "Purple dashed = part the three models ended on, position not computed.",
         ha="center", fontsize=12.5, wrap=True)


def rect(ax, x0, y0, w, h, fc, ec="black", lw=1.0, ls="-", alpha=1.0, z=3, tr=None, hatch=None):
    p = patches.Rectangle((x0, y0), w, h, fc=fc, ec=ec, lw=lw, ls=ls, alpha=alpha, zorder=z, hatch=hatch)
    if tr is not None:
        p.set_transform(tr + ax.transData)
    ax.add_patch(p)
    return p


def element(ax, x, y_lo, y_hi, vertical=True):
    """Red dot at mid-range with a bar showing the documented range (along r)."""
    ym = 0.5 * (y_lo + y_hi)
    if vertical:
        ax.plot([x, x], [y_lo, y_hi], color=C_EL, lw=3, zorder=8, solid_capstyle="butt")
    ax.plot(x, ym, "o", color=C_EL, ms=7, zorder=9)


def axial_symbol(ax, x, y):
    ax.plot(x, y, "o", ms=17, mfc="none", mec=C_DIFF, mew=2.2, zorder=10)
    ax.plot(x, y, "o", ms=4, color=C_DIFF, zorder=10)


def radial_arrow(ax, x, y, length=1.6):
    ax.annotate("", xy=(x, y - length), xytext=(x, y), zorder=10,
                arrowprops=dict(arrowstyle="-|>", color="#1f5fbf", lw=2.4, mutation_scale=18))


def ring_background(ax):
    ax.add_patch(patches.Circle((0, 0), R_ROPE, fc=C_ROPE, ec="black", lw=1.2, zorder=1))
    ax.add_patch(patches.Wedge((0, 0), R_ROPE + LINER, 0, 360, width=LINER, fc=C_LINER, ec="#7a6a40", lw=0.8, zorder=1))
    ax.add_patch(patches.Circle((0, 0), R_FACE, fill=False, ec="#555", ls=(0, (4, 3)), lw=1.0, zorder=2))
    ax.add_patch(patches.Circle((0, 0), R_REF, fill=False, ec="#999", ls=":", lw=1.2, zorder=2))


def spoke_A(ax, tr=None, alpha=1.0, detail=True):
    rect(ax, -T_BOARD / 2, R_FACE, T_BOARD, 20, C_BOARD, tr=tr, alpha=alpha)
    # radial part on +x face: 1.5 side (sensing) along r
    rect(ax, T_BOARD / 2, R_FACE, LGA_H, LGA_W, C_PART, tr=tr, alpha=alpha, z=4)
    # axial part on -x face: 2.0 side along r, 1.5 (sensing) along z
    rect(ax, -T_BOARD / 2 - LGA_H, R_FACE, LGA_H, LGA_L, C_PART, tr=tr, alpha=alpha, z=4)


def spoke_B(ax, tr=None, alpha=1.0):
    y_tab = R_FACE + X2_H
    rect(ax, -T_BOARD / 2, y_tab + T_TAB, T_BOARD, 20, C_BOARD, tr=tr, alpha=alpha)
    rect(ax, -TAB_W / 2, y_tab, TAB_W, T_TAB, C_TAB, tr=tr, alpha=alpha, z=4)
    rect(ax, -X2_L / 2, R_FACE, X2_L, X2_H, C_PART, tr=tr, alpha=alpha, z=5)
    # cross tab (in the cross-section plane, at another z) beside the spoke
    rect(ax, T_BOARD / 2, R_FACE, CROSS_TAB_LEN, 3.0, C_TAB, tr=tr, alpha=alpha * 0.85, z=3, hatch="//")
    rect(ax, T_BOARD / 2 + 0.6, R_FACE, X2_L, X2_W, C_PART, tr=tr, alpha=alpha, z=5)


def neighbours(ax, fn):
    for sgn in (+1, -1):
        tr = transforms.Affine2D().rotate_deg_around(0, 0, sgn * PITCH)
        fn(ax, tr=tr, alpha=0.45)
    # centre-to-centre arc at r 31
    ax.add_patch(patches.Arc((0, 0), 2 * R_REF, 2 * R_REF, theta1=90 - PITCH, theta2=90, ec="#1f5fbf", lw=1.6, zorder=6))
    ax.add_patch(patches.Arc((0, 0), 2 * R_REF, 2 * R_REF, theta1=90, theta2=90 + PITCH, ec="#1f5fbf", lw=1.6, zorder=6))
    ax.text(-5.4, 31.75, "12.17 centre to centre\nat r 31.0 (11.39 at r 29)", color="#1f5fbf", fontsize=10.5, ha="center",
            rotation=10, zorder=11, bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))
    ax.text(-10.6, 30.4, "next spoke\n22.5° away", fontsize=10.5, ha="center", color="#333", rotation=22.5, zorder=11)
    ax.text(10.6, 30.4, "next spoke\n22.5° away", fontsize=10.5, ha="center", color="#333", rotation=-22.5, zorder=11)


def common_cs(ax, title):
    ax.set_xlim(-13.5, 13.5)
    ax.set_ylim(22.0, 42.6)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=15, fontweight="bold", loc="left")
    ax.set_xlabel("tangential (mm)      - - r 30.0 face nearest the rope (stand-off 4.0)      ··· r 31.0 = 5 mm reference", fontsize=11)
    ax.set_ylabel("radius from rope centre (mm)")
    ax.grid(True, color="#ddd", lw=0.5, zorder=0)
    ax.text(0, 24.75, "rope, r 26.0 (52 mm)", fontsize=11.5, zorder=11, color="white", fontweight="bold", ha="center")
    ax.text(-4.3, 26.5, "liner 1.5 (assumed, status A)", fontsize=10.5, zorder=11, ha="center", rotation=9)
    ax.text(-5.2, 28.6, "recess 2.5 (assumed)", fontsize=10.5, zorder=11, color="#444", ha="center", rotation=10)


# ================= Panel 1A =================
ax = fig.add_subplot(gs[0, 0])
ring_background(ax)
neighbours(ax, spoke_A)
spoke_A(ax)
xr = T_BOARD / 2 + LGA_H - LGA_DEPTH
element(ax, xr, R_FACE + A_E[0], R_FACE + A_E[1])
radial_arrow(ax, xr + 0.9, R_FACE + 1.9, 1.4)
element(ax, -xr, R_FACE + A_E[0], R_FACE + A_E[1])
axial_symbol(ax, -xr - 0.05, R_FACE + 2.9)
ax.annotate("", xy=(-xr, R_FACE + 0.9), xytext=(-xr - 0.05, R_FACE + 2.55),
            arrowprops=dict(arrowstyle="-", color=C_DIFF, lw=1.2), zorder=9)
common_cs(ax, "1A  Placement A (the record): two in-plane TMR parts\n      flat on the spoke, back to back — looking along the rope")
ax.text(2.3, 35.4, "RADIAL  TMR2185G\n(LGA4L 2.0×1.5×0.73)\nelement r 30.60–30.85\nstand-off 4.60–4.85",
        fontsize=11, color="#1f5fbf", fontweight="bold", zorder=11, bbox=dict(fc="white", ec="#1f5fbf", pad=3))
ax.annotate("", xy=(xr + 0.1, R_FACE + 0.75), xytext=(3.6, 35.3), arrowprops=dict(arrowstyle="->", color="#1f5fbf"), zorder=11)
ax.text(-12.9, 35.4, "AXIAL  TMR2185G,\nturned 90°\nelement r 30.60–30.85\nstand-off 4.60–4.85",
        fontsize=11, color=C_DIFF, fontweight="bold", zorder=11, bbox=dict(fc="white", ec=C_DIFF, pad=3))
ax.annotate("", xy=(-xr - 0.5, R_FACE + 3.1), xytext=(-6.5, 35.3), arrowprops=dict(arrowstyle="->", color=C_DIFF), zorder=11)
ax.text(0, 40.6, "board 1.6: assumed for drawing only\n(thickness not in the documents)",
        fontsize=10, ha="center", zorder=11, bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))
ax.annotate("", xy=(0, 37.2), xytext=(0, 37.6), zorder=11)
ax.text(0, 22.4, "the record names no part; TMR2185G is the leadless\npart the placement note computes for A",
        fontsize=10, ha="center", color="white", zorder=11)

# ================= Panel 1B =================
ax = fig.add_subplot(gs[0, 1])
ring_background(ax)
neighbours(ax, spoke_B)
spoke_B(ax)
element(ax, 0, R_FACE + B_RAD_E[0], R_FACE + B_RAD_E[1])
radial_arrow(ax, -1.25, R_FACE + 1.7, 1.2)
xa = T_BOARD / 2 + 0.6 + X2_L / 2
element(ax, xa, R_FACE + B_AX_E[0], R_FACE + B_AX_E[1])
axial_symbol(ax, xa + 2.2, R_FACE + 0.62)
ax.annotate("", xy=(xa + 0.2, R_FACE + 0.62), xytext=(xa + 1.75, R_FACE + 0.62),
            arrowprops=dict(arrowstyle="-", color=C_DIFF, lw=1.2), zorder=9)
# models' DRV5055 SOT-23, dashed (not computed)
rect(ax, -SOT_L / 2, R_FACE, SOT_L, SOT_H, "none", ec=C_MOD, lw=2.0, ls="--", z=7)
rect(ax, xa - SOT_W / 2, R_FACE, SOT_W, SOT_L, "none", ec=C_MOD, lw=2.0, ls="--", z=7)
common_cs(ax, "1B  Placement B (the three models' choice): small Hall parts\n      on tabs at the spoke's inner edge — looking along the rope")
ax.text(-12.9, 35.0, "RADIAL  TMAG5253\n(X2SON-4 1.40×1.10×0.4)\non a tab across the\nspoke tip, face to rope\n"
        "element r 30.12–30.14\nstand-off 4.12–4.14",
        fontsize=10.5, color="#1f5fbf", fontweight="bold", zorder=11, bbox=dict(fc="white", ec="#1f5fbf", pad=3))
ax.annotate("", xy=(-0.3, R_FACE + 0.15), xytext=(-6.5, 35.0), arrowprops=dict(arrowstyle="->", color="#1f5fbf"), zorder=11)
ax.text(2.6, 34.4, "AXIAL  TMAG5253\non a cross tab (cross-\nsection plane, other z),\nedge to rope\n"
        "element r 30.50–30.75\nstand-off 4.50–4.75",
        fontsize=10.5, color=C_DIFF, fontweight="bold", zorder=11, bbox=dict(fc="white", ec=C_DIFF, pad=3))
ax.annotate("", xy=(xa + 2.2, R_FACE + 1.1), xytext=(5.5, 34.4), arrowprops=dict(arrowstyle="->", color=C_DIFF), zorder=11)
ax.text(-12.9, 42.3, "purple dashed: DRV5055 SOT-23 body (2.80–3.04 × 1.20–1.40, ≤ 1.12 high),\n"
        "the models' parts: radial A2 (2 of 3) / A4 (1 of 3); axial A4 (3 of 3).\n"
        "NOT COMPUTED in the documents: element depth not read, so no dot",
        fontsize=10, color=C_MOD, va="top", ha="left", zorder=11, bbox=dict(fc="white", ec=C_MOD, pad=3))
ax.text(0, 22.4, "tab sizes not in the documents (width ≥ part, 1.10–1.40);\ndrawn 1.8 × 0.8 and 2.8 × 3.0, for drawing only",
        fontsize=10, ha="center", color="white", zorder=11)

# ================= Panel 2: side views =================
def side_common(ax, title):
    ax.set_xlim(-9, 9)
    ax.set_ylim(24.5, 37.3)
    ax.set_aspect("equal")
    ax.set_title(title, fontsize=15, fontweight="bold", loc="left")
    ax.set_xlabel("z along the rope (mm); z = 0 mid-plane, poles at z = ±50 (off the panel)")
    ax.set_ylabel("radius (mm)")
    ax.grid(True, color="#ddd", lw=0.5, zorder=0)
    rect(ax, -20, 0, 40, R_ROPE, C_ROPE, z=1)
    rect(ax, -20, R_ROPE, 40, LINER, C_LINER, ec="#7a6a40", z=1)
    ax.axhline(R_FACE, color="#555", ls=(0, (4, 3)), lw=1.0, zorder=2)
    ax.axhline(R_REF, color="#999", ls=":", lw=1.2, zorder=2)
    ax.axvline(0, color="black", ls="-.", lw=1.2, zorder=6)
    ax.text(-8.8, 24.8, "rope r 26.0", color="white", fontweight="bold", zorder=11)
    ax.text(-8.8, 26.35, "liner 1.5", fontsize=10.5, zorder=11)
    ax.text(0.3, 35.9, "mid-plane z = 0", fontsize=10.5, va="top", zorder=11)


ax = fig.add_subplot(gs[1, 0])
side_common(ax, "2A  Placement A seen from the side (r against z)")
rect(ax, -9, R_FACE, 18, 7, C_BOARD, z=3, alpha=0.9)
ax.text(-8.8, 35.0, "spoke board, face-on;\naxial length: not in the documents", fontsize=10.5, zorder=11,
        bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))
rect(ax, -LGA_L / 2, R_FACE, LGA_L, LGA_W, C_PART, z=5)                     # radial, near face
rect(ax, -LGA_W / 2, R_FACE, LGA_W, LGA_L, "none", ec="white", ls="--", lw=1.6, z=6)  # axial, far face
element(ax, 0, R_FACE + A_E[0], R_FACE + A_E[1])
ax.annotate("", xy=(0.0, 28.4), xytext=(0.0, 29.8), zorder=10,
            arrowprops=dict(arrowstyle="-|>", color="#1f5fbf", lw=2.4, mutation_scale=18))
ax.annotate("", xy=(3.2, 30.72), xytext=(1.3, 30.72), zorder=10,
            arrowprops=dict(arrowstyle="-|>", color=C_DIFF, lw=2.4, mutation_scale=18))
ax.text(3.4, 32.1, "same r and z, one board\nthickness apart (near face\nsolid = radial; far face\ndashed = axial)",
        fontsize=10.5, zorder=11, bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))
# documents differ: design.md positions
for zz in (-4, 4):
    ax.plot(zz, 31.0, "D", ms=10, mfc="none", mec=C_DIFF, mew=2.2, zorder=9)
ax.plot(0, 36.5, "D", ms=10, mfc="none", mec=C_DIFF, mew=2.2, zorder=9, clip_on=False)
ax.text(-8.8, 32.6, "◇ DOCUMENTS DIFFER: the 3D design note reads\nradial at z ±4, r 31.0 and axial at r 36.5\n"
        "[UNVERIFIED]; the placement note puts\nboth at the inner edge (r ≈ 30.6–30.9)",
        fontsize=10, color="#a05000", zorder=11, bbox=dict(fc="white", ec=C_DIFF, pad=2))

ax = fig.add_subplot(gs[1, 1])
side_common(ax, "2B  Placement B seen from the side (r against z)")
y_tab = R_FACE + X2_H
rect(ax, -9, y_tab + T_TAB, 18, 7, C_BOARD, z=3, alpha=0.9)
ax.text(-8.8, 35.0, "spoke board, face-on;\naxial length: not in the documents", fontsize=10.5, zorder=11,
        bbox=dict(fc="white", ec="none", alpha=0.8, pad=1))
rect(ax, -TAB_W / 2, y_tab, TAB_W, T_TAB, C_TAB, z=4)                     # radial tab, edge-on
rect(ax, -X2_L / 2, R_FACE, X2_L, X2_H, C_PART, z=5)
element(ax, 0, R_FACE + B_RAD_E[0], R_FACE + B_RAD_E[1])
ax.annotate("", xy=(-1.6, 28.6), xytext=(-1.6, 30.0), zorder=10,
            arrowprops=dict(arrowstyle="-|>", color="#1f5fbf", lw=2.4, mutation_scale=18))
rect(ax, Z_AX_B, R_FACE, T_TAB, 3.0, C_TAB, z=4, hatch="//")             # cross tab, edge-on
rect(ax, Z_AX_B + T_TAB, R_FACE, X2_H, X2_W, C_PART, z=5)
za = Z_AX_B + T_TAB + X2_H - 0.13
element(ax, za, R_FACE + B_AX_E[0], R_FACE + B_AX_E[1])
ax.annotate("", xy=(za + 2.0, R_FACE + 0.62), xytext=(za + 0.2, R_FACE + 0.62), zorder=10,
            arrowprops=dict(arrowstyle="-|>", color=C_DIFF, lw=2.4, mutation_scale=18))
ax.text(3.6, 32.2, "radial part on the mid-plane;\naxial part on a cross tab\nbeside it. z of the cross tab:\nnot in the documents\n(drawn 1.2–2.0 to illustrate)",
        fontsize=10.5, zorder=11, bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))

# ---- why z matters (note across the row) ----
ax = fig.add_subplot(gs[2, :])
ax.axis("off")
note = (
    "WHY z MATTERS — the field the parts sit in (placement note §1; 2D, shared head on the 52 mm rope, 25 °C, placeholder materials):\n"
    "•  Radial field at r 31.0: 0.23 mT at the mid-plane, 7.53 mT at 4 mm off it — about 1.9 mT per mm off the mid-plane "
    "(straight-line reading, inference).\n"
    "•  Axial background at r 31.0: −36.6 mT; it falls 1.86 mT per mm going outward and is zero at r 50.4 (at the yoke). "
    "15 mm stand-off halves it to −17.6 mT\n    and keeps 17 % of the broken-wire signal (extrapolation).\n"
    "•  So the radial part does best on the mid-plane; the axial background has no slope along z there by symmetry, "
    "so the axial part loses little off it (inference).\n"
    "    The two parts cannot both sit on the mid-plane in B; in A they sit back to back at the same r and z.\n"
    "•  Signal law (radial peak): 0.39 mT at 5 mm, about 21 % less per mm near 5 mm, about 2.4 % per 0.1 mm. "
    "The record has no separate law for the axial channel.\n"
    "•  Stand-off stacks — DOCUMENTS DIFFER: geometry stack liner 1.5 + recess 2.5 + die 1.0 = 5.0 (drawn here); "
    "specification floor stack movement 3 + guard 1 + die 0.7 = 4.7.\n"
    "    The record does not say which the carrier follows. Not in any stand-off above: board-edge keep-out, outline "
    "tolerance, solder fillet (all add to it)."
)
ax.text(0.0, 1.0, note, fontsize=12.2, va="top", ha="left", linespacing=1.45,
        bbox=dict(fc="#f6f6f2", ec="#999", pad=10))

# ================= Panel 3: table =================
ax = fig.add_subplot(gs[3, :])
ax.axis("off")
ax.set_title("3  Per channel and placement: part, element radius, stand-off, signal kept against the 5 mm reference",
             fontsize=15, fontweight="bold", loc="left")
cols = ["Channel", "Placement", "Part named in the documents", "Range (sheet, as corrected)",
        "Element r (mm)", "Stand-off (mm)", "Signal kept vs 5 mm"]
rows = [
    ["Radial", "A (record)", "TMR bridge; record names no part. Computed for A: TMR2185G LGA4L, edge to rope "
     "(also TMR2151S SOT23-5, pin-1 end: r 31.00–31.20, 95–100 %)",
     "TMR2185: specified within ±20 mT only, saturation ±100 mT", "30.60–30.85", "4.60–4.85", "104–110 %"],
    ["Axial", "A (record)", "TMR bridge; record names no part. Drawn: TMR2185G turned 90°",
     "as above; axial background −36.6 mT at r 31 (2D)", "30.60–30.85", "4.60–4.85",
     "104–110 % (law is the radial peak; no axial law)"],
    ["Radial", "B (models)", "DRV5055A2 2 of 3, DRV5055A4 1 of 3 (SOT-23, on a tab) — drawn dashed",
     "A2 ±44 mT at 3.3 V (±42 is the 5 V figure); A4 ±176 mT", "not computed", "not computed", "not computed"],
    ["Radial", "B, computed case", "TMAG5253 X2SON-4 on the tab's rope side, face to rope",
     "BA4 ±160 mT (already net of tolerance)", "30.12–30.14", "4.12–4.14", "124–125 %"],
    ["Axial", "B (models)", "DRV5055A4 3 of 3 (SOT-23, on a cross tab) — drawn dashed",
     "±176 mT at 3.3 V, minimum at 25 °C; models' demand 131–156 mT", "not computed", "not computed", "not computed"],
    ["Axial", "B, computed case", "TMAG5253 X2SON-4 on a cross tab, edge to rope",
     "BA4 ±160 mT", "30.50–30.75", "4.50–4.75", "106–113 %"],
]
widths = [0.065, 0.10, 0.33, 0.20, 0.085, 0.085, 0.135]
wraps = [8, 12, 50, 29, 12, 12, 19]
cell_text = [["\n".join(textwrap.wrap(c, w)) for c, w in zip(r, wraps)] for r in rows]
tab = ax.table(cellText=cell_text, colLabels=["\n".join(textwrap.wrap(c, w)) for c, w in zip(cols, wraps)],
               colWidths=widths, loc="upper left", cellLoc="left", bbox=[0, 0.19, 1, 0.78])
tab.auto_set_font_size(False)
tab.set_fontsize(11.5)
for (r, c), cell in tab.get_celld().items():
    cell.set_edgecolor("#888")
    if r == 0:
        cell.set_facecolor("#e4e4e4")
        cell.set_text_props(fontweight="bold")
    elif "not computed" in rows[r - 1][4]:
        cell.set_facecolor("#f3ecf7")
    elif rows[r - 1][0] == "Radial":
        cell.set_facecolor("#eef3fb")
    else:
        cell.set_facecolor("#fdf3e7")
ax.text(0.0, 0.16,
        "Element r = 26.0 + stand-off; stand-off = 4.0 + depth of the element behind the face nearest the rope (geometry stack).  "
        "Signal kept = signal at that stand-off / signal at 5 mm.\n"
        "Not in the documents: board thickness, spoke axial length, tab sizes, z of the axial part in B, the board-edge keep-out.  "
        "The models' choice is their agreement, not a measurement.\n"
        "Requirements on any part (spec §7): range ≥ 2 × (background + signal) as written (models: a sum instead); "
        "noise 0.11 mT p-p after the template in 0–125 Hz on 52 mm;\n"
        "package ≤ 3 × 3 mm with the die close to the spoke edge; 3.3 V ratiometric; −40…+125 °C; second source or availability statement.",
        fontsize=11, va="top", ha="left", transform=ax.transAxes, linespacing=1.45)

fig.savefig(OUT, dpi=100)
print("wrote", OUT)
