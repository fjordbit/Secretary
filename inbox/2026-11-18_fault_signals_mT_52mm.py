"""Fault signals in plain mT for the 52 mm rope (calculated, not measured).

Reads the U32 summary (read-only) and writes one PNG to secretary/inbox.
Case: the base of sws/figures/decided/u32_faults_3d.png = P52 one-piece head, N52* lm 16.73 mm (run point),
hard wire, +45 C, half-space L_h 25, box 300, level 1.5, worst angle.
"""
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullLocator

REPO = Path("C:/Users/stian/Prosjekter-u05/max")
SUMMARY = REPO / "sws/3d/results/p52/u32_summary.json"
OUT = Path("C:/Users/stian/secretary/inbox/2026-11-18_fault_signals_mT_52mm.png")

LIMIT = 2 * 0.11          # mT zero-peak; spec rev130 l.327 (0.11 mT p-p at 52 mm) and l.325 (zero-peak >= 2 x p-p)
BG_3MM, BG_365 = -39.22, -26.56   # p52/design.md l.214, l.217 (lm 20.5, +80 C, box 1200)

# top-to-bottom order, plain labels
ROWS = [
    ("deep_wire", "1 wire deep in the rope\n(inner rope, under jacket)"),
    ("1king", "1 hidden wire, outer strand\n(king wire)"),
    ("1bottom", "1 hidden wire, outer strand\n(bottom wire)"),
    ("1crown", "1 visible crown wire"),
    ("2hidden_flank_g1", "2 hidden wires (flank), gap 1 mm"),
    ("2hidden_flank", "2 hidden wires (flank), gap 2 mm\n= acceptance-type case"),
    ("2hidden_flank_g4", "2 hidden wires (flank), gap 4 mm"),
    ("2hidden_flank_g10", "2 hidden wires (flank), gap 10 mm"),
    ("2hidden_king_bottom", "2 hidden wires (king + bottom)"),
    ("lma_corrosion", "3 wires missing over 20 mm"),
    ("cluster6", "6-wire cluster (one strand)"),
    ("inner_strand", "inner-rope strand broken"),
]

SHORT = {"deep_wire": "1 wire deep in the rope", "1king": "1 hidden wire (king)",
         "1bottom": "1 hidden wire (bottom)", "1crown": "1 visible crown wire",
         "2hidden_flank_g1": "2 hidden wires (flank), gap 1 mm", "2hidden_flank": "2 hidden wires (flank), gap 2 mm",
         "2hidden_flank_g4": "2 hidden wires (flank), gap 4 mm", "2hidden_flank_g10": "2 hidden wires (flank), gap 10 mm",
         "2hidden_king_bottom": "2 hidden wires (king + bottom)", "lma_corrosion": "3 wires missing over 20 mm",
         "cluster6": "6-wire cluster (one strand)", "inner_strand": "inner-rope strand broken"}

DARK, LIGHT, RED, INK, GREY = "#1f4e79", "#9cc3e6", "#c0392b", "#222222", "#555555"


def load():
    d = json.loads(SUMMARY.read_text(encoding="utf-8"))
    out = {}
    for c in d["faults"].values():
        if c["case_id"] == "P52lm16.73N52_d52_hard_+45C" and c["Lh"] == 25:
            out.update(c["faults"])
    return out


def bars(ax, vals_a, vals_b, lab_a, lab_b, labels, xmin, xmax, title):
    n = len(labels)
    y = list(range(n))[::-1]
    h = 0.38
    ax.barh([v + h / 2 for v in y], vals_a, h, color=DARK, label=lab_a)
    ax.barh([v - h / 2 for v in y], vals_b, h, color=LIGHT, label=lab_b)
    for yy, a, b in zip(y, vals_a, vals_b):
        ax.text(a * 1.08, yy + h / 2, f"{a:.2f}", va="center", fontsize=17, color=INK, fontweight="bold")
        ax.text(b * 1.08, yy - h / 2, f"{b:.2f}", va="center", fontsize=17, color=GREY)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=17)
    ax.set_xscale("log")
    ax.set_xlim(xmin, xmax)
    ticks = [0.1, 0.22, 0.5, 1, 2, 5, 10, 20]
    ax.xaxis.set_major_locator(FixedLocator([t for t in ticks if xmin <= t <= xmax]))
    ax.xaxis.set_minor_locator(NullLocator())
    ax.set_xticklabels([f"{t:g}" for t in ticks if xmin <= t <= xmax], fontsize=16)
    ax.set_xlabel("mT at the sensor (log scale, numbers printed at each bar)", fontsize=17)
    ax.set_title(title, fontsize=21, loc="left", fontweight="bold", pad=14)
    ax.set_ylim(-0.7, n - 0.3)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="x", color="#dddddd", lw=0.8)
    ax.set_axisbelow(True)


def main():
    f = load()
    keys = [k for k, _ in ROWS]
    lab = [l for _, l in ROWS]

    fig = plt.figure(figsize=(16, 31), dpi=100)
    gs = fig.add_gridspec(3, 1, height_ratios=[1.0, 1.0, 0.62], hspace=0.42,
                          left=0.29, right=0.965, top=0.935, bottom=0.01)
    fig.suptitle("52 mm rope: what each fault gives at the sensor, in mT\n(calculated, not measured)",
                 fontsize=26, fontweight="bold", x=0.5, y=0.99)

    # Panel 1: LD, radial channel
    ax1 = fig.add_subplot(gs[0])
    bars(ax1, [f[k]["Br5_worst"] for k in keys], [f[k]["Br3_worst"] for k in keys],
         "5 mm from the rope (design stand-off)", "3 mm from the rope",
         lab, 0.1, 40,
         "1  Broken wires (LD): radial sensor channel B_r, worst rope angle")
    ax1.axvline(LIMIT, color=RED, lw=2.5)
    ax1.annotate("0.22 mT = pass line: signal must be\nat least 2 x noise (0.11 mT p-p)",
                 xy=(LIMIT, 11.0), xytext=(0.6, 11.0), color=RED, fontsize=15, va="center",
                 arrowprops=dict(arrowstyle="->", color=RED, lw=1.5))
    ax1.legend(fontsize=16, loc="upper left", bbox_to_anchor=(-0.38, -0.075), ncol=2, frameon=False)
    ax1.text(-0.38, -0.135,
             "Case: 52 mm head, N52 run point lm 16.73 mm, hard wire, +45 C (the base case of u32_faults_3d.png).\n"
             "The N48SH and N40SH run points read within about 1 % of these (0.6 % and 0.9 %).\n"
             "N52 values carry the label: magnet past the knee in storage and on the 40 mm rope.",
             transform=ax1.transAxes, fontsize=15, color=GREY, va="top")

    # Panel 2: LMA, axial channel
    ax2 = fig.add_subplot(gs[1])
    lab2 = [f"{SHORT[k]}\n[{f[k]['lma_percent']:.2f} % metal lost]" for k in keys]
    bars(ax2, [f[k]["Bz3_worst"] for k in keys], [f[k]["Bz365_worst"] for k in keys],
         "3 mm from the rope", "axial sensor radius R 36.5 mm",
         lab2, 0.05, 60,
         "2  The SAME broken wires seen by the axial channel B_z (this is NOT an LMA measurement)")
    ax2.axvline(LIMIT, color=RED, lw=2.5, ls="--")
    ax2.annotate("0.22 mT line for scale only: the spec gives\nno mT limit for LMA (it asks +/-0.5 %)",
                 xy=(LIMIT, 11.0), xytext=(0.7, 11.0), color=RED, fontsize=15, va="center",
                 arrowprops=dict(arrowstyle="->", color=RED, lw=1.5))
    ax2.legend(fontsize=16, loc="upper left", bbox_to_anchor=(-0.38, -0.075), ncol=2, frameon=False)
    ax2.text(-0.38, -0.135,
             f"Standing axial field with no fault (much larger than any bar): {BG_3MM:.1f} mT at 3 mm, "
             f"{BG_365:.1f} mT at R 36.5.\n"
             "So the LMA signal of 1 hidden wire is about 8 % of the standing field at 3 mm and 1.6 % at R 36.5.\n"
             "Each bar is ONE sensor. The spec's LMA figure (16 axial sensors summed around the rope)\n"
             "is not calculated.",
             transform=ax2.transAxes, fontsize=15, color=GREY, va="top")

    # Panel 3: long faults
    ax3 = fig.add_subplot(gs[2])
    ax3.axis("off")
    ax3.set_title("3  Long faults: is LMA measured right when the fault\n    is longer than the sensor or the head?",
                  fontsize=21, loc="left", fontweight="bold", x=-0.38)
    txt = (
        "- Longest fault calculated: 20 mm (3 wires missing over 20 mm). The fault model only\n"
        "   allows breaks of 1-20 mm, and its read-out assumes the signature fits in about +/-20 mm.\n"
        "- Faults longer than the pole spacing (100 mm) or the head (180 mm): not calculated.\n"
        "   A long, uniform loss of metal: not calculated.\n"
        "- The specification: the 16 axial channels, summed around the rope, should track the\n"
        "   main flux that drops with metal loss. Whether that is enough, or a dedicated main-flux\n"
        "   sensor (Hall in the pole gap or a search coil) is needed, is open for the prototype.\n"
        "- Discard criteria (EN 12927, ISO 4309) are in % LMA, so a calibrated LMA channel is\n"
        "   required. Planned test: 1 % and 5 % removed-wire steps, read within +/-0.5 %.\n"
        "- So today: short faults are calculated; long-fault LMA is assumed, not shown."
    )
    ax3.text(-0.37, 0.86, txt, transform=ax3.transAxes, fontsize=18, va="top", ha="left", linespacing=1.45,
             bbox=dict(facecolor="#f4f6f8", edgecolor="#bbbbbb", boxstyle="round,pad=0.8"))
    ax3.text(-0.38, 0.06,
             "All values: 3D finite-element model, placeholder materials (status A), not measured.\n"
             "Sources with file:line in 2026-11-18_fault_signals_mT_52mm_sources.md.",
             transform=ax3.transAxes, fontsize=15, color=GREY, va="top")

    fig.savefig(OUT, dpi=100, facecolor="white")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
