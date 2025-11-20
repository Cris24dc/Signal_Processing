import matplotlib.pyplot as plt
import numpy as np

# 2. a)
N = 100
time = np.linspace(0, 100, N)
signal = np.random.rand(N)
Ox = [time]
Oy = [signal]

for i in range(3):
    signal = np.convolve(signal, signal)
    Oy.append(signal)

    time = np.linspace(0, 100, len(signal))
    Ox.append(time)

labels = ('Time', 'Amplitude')
titles = ['Semnal random', 'Convolutia 1', 'Convolutia 2', 'Convolutia 3']

fig, axs = plt.subplots(4, 1, figsize=(10, 10))
axs = axs.ravel()
fig.suptitle('Semnal random, alaturi de 3 iteratii de convolutie')

for i in range(0, 4):
    axs[i].plot(Ox[i], Oy[i], 'olivedrab')
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(labels[0])
    axs[i].set_ylabel(labels[1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_2_a.pdf', format='pdf')

# 2. b)
N = 100
time = np.linspace(0, 100, N)
signal = np.zeros(N)
signal[30:70] = 1
Ox = [time]
Oy = [signal]

for i in range(3):
    signal = np.convolve(signal, signal)
    Oy.append(signal)

    time = np.linspace(0, 100, len(signal))
    Ox.append(time)

labels = ('Time', 'Amplitude')
titles = ['Semnal rectangular', 'Convolutia 1', 'Convolutia 2', 'Convolutia 3']

fig, axs = plt.subplots(4, 1, figsize=(10, 10))
axs = axs.ravel()
fig.suptitle('Semnal rectangular, alaturi de 3 iteratii de convolutie')

for i in range(0, 4):
    axs[i].plot(Ox[i], Oy[i], 'olivedrab')
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(labels[0])
    axs[i].set_ylabel(labels[1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_2_b.pdf', format='pdf')
