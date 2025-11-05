import matplotlib.pyplot as plt
import numpy as np

# 2.
# freq
f1 = 1
f2 = 9
f3 = 13
fs = 5

# time
t = np.linspace(0, 1, 800)
samples = np.linspace(0, 1, fs)

# signals
signal1 = np.sin(f1*2*np.pi*t)
signal2 = np.sin(f2*2*np.pi*t)
signal3 = np.sin(f3*2*np.pi*t)
signal1_samples = np.sin(f1*2*np.pi*samples)[:-1]
samples = samples[:-1]

# plots
Ox = [(t, samples)] * 4
Oy = [(signal1, signal1_samples), (signal1, signal1_samples), (signal2, signal1_samples), (signal3, signal1_samples)]
titles = ['Signal 1', 'Signal 1', 'Signal 2', 'Signal 3']
labels = [('Time', 'Amplitude')] * 4
colors = ['darksalmon', 'olivedrab', 'mediumseagreen', 'mediumslateblue']

fig, axs = plt.subplots(4, 1, figsize=(10, 10))
fig.suptitle('Aliasing Effect')
for i in range(0, 4):
    axs[i].plot(Ox[i][0], Oy[i][0], colors[i])
    if i > 0:
        axs[i].scatter(Ox[i][1], Oy[i][1], c='gold', s=50)
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(labels[i][0])
    axs[i].set_ylabel(labels[i][1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_2.pdf', format='pdf')
