import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import math

# label: data rate lower bound [B/s], data rate upper bound [B/s], latency lower bound [s], latency upper bound [s]
input_dict = {
    "Jet Classification": [32 * 40e6, 32 * 40e6, 100e-9, 10e-6],
    "Sensor Data Compression": [48 * 40e6, 48 * 40e6, 10e-9, 100e-9],
    "Beam Control": [3e3 * 15, 3e3 * 15, 100e-6, 5e-3],
    "MLPerf Tiny (IC)": [3e3 / 100e-3, 3e3 / 1e-3, 1e-3, 100e-3],
    "MLPerf Mobile (NLP)": [1e3 / 100e-3, 1e3 / 40e-3, 40e-3, 100e-3],
}
labels = input_dict.keys()
ylo = np.array([input_dict[key][0] for key in labels])
yhi = np.array([input_dict[key][1] for key in labels])
xlo = np.array([input_dict[key][2] for key in labels])
xhi = np.array([input_dict[key][3] for key in labels])

colors = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#17becf",
    "#7f7f7f",
    "#bcbd22",
    "#d62728",
]

plt.style.use([hep.style.ROOT, hep.style.firamath])

ymin = 1e2
ymax = 1e11
xmin = 1e-9
xmax = 1e5


f, ax = plt.subplots()
# FastML contour
ax.text(2e-9, 2e10, "FastML Science", color="gray", style="italic", weight="bold")
box_y = np.array([3e3 * 15, 3e3 * 15, ymax, ymax])
box_x = np.array([xmin, 5e-3, 5e-3, xmin])
ax.fill(box_x, box_y, "gray", alpha=0.2)

for xloi, xhii, yloi, yhii, l, c in zip(xlo, xhi, ylo, yhi, labels, colors):
    yi = math.sqrt(yloi * yhii)
    xi = math.sqrt(xloi * xhii)
    ax.errorbar(
        [xi],
        [yi],
        yerr=[[yi - yloi], [yhii - yi]],
        xerr=[[xi - xloi], [xhii - xi]],
        label=l,
        marker="",
        capsize=6,
        markersize=10,
        color=c,
    )
    if "Mobile" in l:
        ax.text(xi / 10, yi / 4, l, color=c)
    elif "Beam" in l:
        ax.text(xi / 4e5, yi * 2, l, color=c)
    elif "Jet" in l:
        ax.text(xi * 10, yi / 4, l, color=c)
    else:
        ax.text(xi * 2, yi * 2, l, color=c)

ax.loglog()
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
ax.set_xlabel("Reference latency [s]")
ax.set_ylabel("Streaming data rate [B/s]")

plt.tight_layout()
plt.savefig("sciml_graph.pdf")
plt.savefig("sciml_graph.png")
