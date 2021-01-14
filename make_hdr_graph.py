import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np

def nonlinear(x):
    #return 6*np.log10(x)
    return 6e-5*np.power(np.log10(x),5)
    #return 1e-4*np.power(x,1/2)

labels = ['LHC L1T', 'DUNE', 'IceCube', 'LHC HLT', 'XENON', 'Neuro', 'LIGO']
x = np.array([10e-6, 1e-3, 1, 200e-3, 60, 1e-3, 1e-3]) # latency [s]
y = np.array([100e12, 1e12, 20e6, 5e12,  500e6, 20e6, 32e6]) # throughput [B/s]
#z = np.array([1e6, 50e12, 6e12, 20e15, 50e12]) # buffering [B]
w = np.array([300e15, 30e15, 300e12, 300e15, 2e15, 1e12, 1e12]) # accumulated data volume [B/yr]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
plt.style.use([hep.style.ROOT, hep.style.firamath])
#hep.set_style("CMS")
#hep.set_style({"font.sans-serif":'Comic Sans MS'})

f, ax = plt.subplots()
for xi, yi, wi, l, c in zip(x, y, w, labels, colors):
    ax.plot([xi], [yi], label=l, marker='o', markersize=nonlinear(wi), color=c)
    if 'LHC' in l:
        ax.text(xi*0.1, yi*30, l, color=c)
    elif l=='IceCube':
        ax.text(xi*0.1, yi*5, l, color=c)
    elif l=='XENON':
        ax.text(xi*0.1, yi*10, l, color=c)
    elif l=='DUNE':
        ax.text(xi*0.2, yi*20, l, color=c)
    elif l=='Neuro':
        ax.text(xi*0.01, yi*2, l, color=c)
    elif l=='LIGO':
        ax.text(xi, yi*5, l, color=c)
#plt.legend()
ax.plot([30*1e-2], [1e18], label='1 TB/yr', marker='o', markersize=nonlinear(1e12), color='gray')
ax.plot([4*2e0], [1e18], label='1 PB/yr', marker='o', markersize=nonlinear(1e15), color='gray')
ax.plot([1e3], [1e18], label='1 EB/yr', marker='o', markersize=nonlinear(1e18), color='gray')
ax.text(30*0.23e-2, 0.3e19, '1 TB/yr', color='black',size=18)
ax.text(4*0.40e0, 0.7e19, '1 PB/yr', color='black',size=18)
ax.text(0.23e3, 0.7e18, '1 EB/yr', color='white',size=18)



# FPGA/ASIC contour
ax.text(1e-6, 4e16, 'FPGA/ASIC', color='gray',size=18)
box_y = np.array([1e6, 1e6, 1e17, 1e17])
box_x = np.array([1e-7, 2e-3, 2e-3, 1e-7])
ax.fill(box_x, box_y, 'r', alpha=0.1)

# GPU/CPU contour
ax.text(0.3, 4e15, 'CPU/GPU', color='gray',size=18)
box_y = np.array([1e6, 1e6, 1e16, 1e16])
box_x = np.array([1e-4, 1e5, 1e5, 1e-4])
ax.fill(box_x, box_y, 'b', alpha=0.1)

ax.loglog()
ax.set_xlim(1e-7,1e5)
ax.set_ylim(1e6,1e20)
ax.set_xlabel('Latency requirement [s]')
ax.set_ylabel('Streaming data rate [B/s]')
#hep.cms.label(loc=0)

plt.savefig('hdr_graph.pdf')
plt.savefig('hdr_graph.png')
