import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np

def nonlinear(x):
    #return 6*np.log10(x)
    return 6e-5*np.power(np.log10(x),5)
    #return 1e-4*np.power(x,1/2)

labels = ['LHC L1T', 'DUNE', 'IceCube', 'XENON', 'Neuro', 'LIGO', 'ZTF', 'Netflix 4K UHD', 'Google Cloud', 'LHC HLT']
x = np.array([10e-6, 1e-3, 1, 60, 1e-3, 1e-1, 10, 10, 5, 200e-3,]) # latency [s]
y = np.array([100e12, 1e12, 20e6, 500e6, 20e6, 32e6, 60e6, 2e6, 1e12,  5e12]) # throughput [B/s]
w = np.array([300e18, 30e15, 300e12, 2e15, 1e15, 1e15, 680e12, 60e12, 1e18, 300e15]) # accumulated data volume [B/yr]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd', '#8c564b', '#e377c2', '#17becf', '#7f7f7f', '#bcbd22', '#d62728']

plt.style.use([hep.style.ROOT, hep.style.firamath])
#hep.set_style("CMS")
#hep.set_style({"font.sans-serif":'Comic Sans MS'})


f, ax = plt.subplots()
for xi, yi, wi, l, c in zip(x, y, w, labels, colors):
    ax.plot([xi], [yi], label=l, marker='o', markersize=nonlinear(wi), color=c)
    ax.plot([xi], [yi], label=l, marker='*', markersize=10, color='white')
    if l=='LHC HLT':
        ax.text(xi*0.1, yi*30, l, color=c)
    elif l=='IceCube':
        ax.text(xi*3, yi*0.3, l, color=c)
    elif l=='XENON':
        ax.text(xi*0.1, yi*10, l, color=c)
    elif l=='DUNE':
        ax.text(xi*0.2, yi*0.02, l, color=c)
    elif l=='Neuro':
        ax.text(xi*0.006, yi*2, l, color=c)
    elif l=='LIGO':
        ax.text(xi*0.1, yi*6, l, color=c)
    elif l=='LHC L1T':
        ax.text(xi*0.01, yi*0.0003, l, color=c)
    elif l=='ZTF':
        ax.text(xi*0.08, yi*5, l, color=c)
    elif l=='Netflix 4K UHD':
        ax.text(xi*3, yi*0.5, l, color=c)
    elif l=='Google Cloud':
        ax.text(xi*2, yi*40, l, color=c)
#plt.legend()
ax.plot([300*1e-2], [1e18], label='1 TB/yr', marker='o', markersize=nonlinear(1e12), color='gray')
ax.plot([40*2e0], [1e18], label='1 PB/yr', marker='o', markersize=nonlinear(1e15), color='gray')
ax.plot([10*1e3], [1e18], label='1 EB/yr', marker='o', markersize=nonlinear(1e18), color='gray')
ax.text(300*0.23e-2, 0.3e19, '1 TB/yr', color='black',size=18)
ax.text(40*0.40e0, 0.7e19, '1 PB/yr', color='black',size=18)
ax.text(10*0.23e3, 0.7e18, '1 EB/yr', color='white',size=18)


hep.label._exp_text(text="Institute",exp="A3D3",italic=(True, True),loc=0,pad=0)

ymin = 3e5
ymax = 1e20
xmin = 1e-8
xmax = 1e6

# FPGA/ASIC contour
ax.text(1e-7, 1e19, 'FPGA/ASIC', color='gray',size=18)
box_y = np.array([ymin, ymin, ymax, ymax])
box_x = np.array([xmin, 2e-3, 2e-3, xmin])
ax.fill(box_x, box_y, 'r', alpha=0.1)

# GPU/CPU contour
ax.text(0.3, 4e15, 'CPU/GPU', color='gray',size=18)
box_y = np.array([ymin, ymin, 1e16, 1e16])
box_x = np.array([1e-4, xmax, xmax, 1e-4])
ax.fill(box_x, box_y, 'b', alpha=0.1)

ax.loglog()
ax.set_xlim(xmin,xmax)
ax.set_ylim(ymin,ymax)
ax.set_xlabel('Latency requirement [s]')
ax.set_ylabel('Streaming data rate [B/s]')
#hep.cms.label(loc=0)

plt.tight_layout()
plt.savefig('hdr_graph.pdf')
plt.savefig('hdr_graph.png')
