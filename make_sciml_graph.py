import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np

# label: input data size [B], latency lower bound [s], mean latency [s], latency upper bound [s]
input_dict = {'LHC L1T':             [32, 100e-9, 1e-6, 10e-6],
              'LHC on Det.':         [48, 10e-9, 30e-9, 100e-9],
              'Accel. Control':      [3e3, 10e-3, 20e-3, 66e-3],
              'MLPerf Tiny (IC)':    [3e3, 1e-3, 10e-3, 100e-3],
              'MLPerf Mobile (NLP)': [1e3, 40e-3, 60e-3, 100e-3],
               }
labels = input_dict.keys()
input_data_size = np.array([input_dict[key][0] for key in labels])
xlo = np.array([input_dict[key][1] for key in labels])
x = np.array([input_dict[key][2] for key in labels])
xhi = np.array([input_dict[key][3] for key in labels])

y = input_data_size/x
ylo = input_data_size/xlo
yhi = input_data_size/xhi

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd', '#8c564b', '#e377c2', '#17becf', '#7f7f7f', '#bcbd22', '#d62728']

plt.style.use([hep.style.ROOT, hep.style.firamath])
#hep.set_style("CMS")
#hep.set_style({"font.sans-serif":'Comic Sans MS'})

f, ax = plt.subplots()
for xi, yi, xloi, xhii, yloi, yhii, l, c in zip(x, y, xlo, xhi, ylo, yhi, labels, colors):
    ax.errorbar([xi], [yi],
                yerr=[[yi-yloi],[yhii-yi]],
                xerr=[[xi-xloi],[xhii-xi]],
                label=l, marker='o', capsize=6,
                markersize=10, color=c)
    if 'Mobile' in l:
        ax.text(xi/10, yi/4, l, color=c)
    elif 'Accel' in l:
        ax.text(xi*2, yi/3, l, color=c)
    else:
        ax.text(xi*2, yi*2, l, color=c)

ymin = 1e2
ymax = 1e11
xmin = 1e-9
xmax = 1e5


ax.loglog()
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.set_xlabel('Reference latency [s]')
ax.set_ylabel('Streaming data rate [B/s]')

plt.tight_layout()
plt.savefig('sciml_graph.pdf')
plt.savefig('sciml_graph.png')
