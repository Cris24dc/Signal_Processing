import matplotlib.pyplot as plt
import numpy as np

# 5.
def Rectangular(N):
    return np.ones(N)


def Hanning(N):
    n = np.arange(N)
    return 0.5 * (1-np.cos(2*np.pi*n/N))


Nw = 200

time = np.linspace(0, 0.1, Nw, endpoint=False)
sign = np.sin(200*np.pi*time)

rect = sign * Rectangular(Nw)
hann = sign * Hanning(Nw)

Ox = [time] * 3
Oy = [sign, rect, hann]

labels = ('Time', 'Amplitude')
titles = ['Semnal original', 'Fereastra dreptunghiulara', 'Fereastra Hanning']

fig, axs = plt.subplots(3, 1, figsize=(10, 10))
axs = axs.ravel()
fig.suptitle('Sinusoida trecuta prin ferestre')

for i in range(0, 3):
    axs[i].plot(Ox[i], Oy[i], 'olivedrab')
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(labels[0])
    axs[i].set_ylabel(labels[1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_5.pdf', format='pdf')
