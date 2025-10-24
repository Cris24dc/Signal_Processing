import matplotlib.pyplot as plt
import numpy as np

# 3.
time = np.linspace(0, 2, 800)
signal = 1/2*np.cos(8*np.pi*time + np.pi/2) + np.sin(6*np.pi*time) + np.sin(20*np.pi*time)

N = len(signal)
fourier_matrix = np.ones((N, N), dtype=complex)
for row in range(N):
    for col in range(N):
        fourier_matrix[row][col] = np.exp(-2j*np.pi*row*col/N)

# Modulul componentelor
X = np.dot(signal, fourier_matrix)
T = time[1] - time[0]
fs = 1 / T
freq = np.arange(N) * fs / N
half = N // 2
freq = freq[:half]
X = np.abs(X[:half]) / N

Ox = [time, freq]
Oy = [signal, X]

titles = ['Semnal sinusoidal', 'Modulul']
lables = [('Time', 'Amplitude'), ('Frequency', rf'$|X(\omega)|$')]
colors = ['olivedrab', 'mediumslateblue']

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle('Modulul transformatei Fourier')

for i in range(0, 2):
    if i == 0:
        axs[i].plot(Ox[i], Oy[i], colors[i])
    else:
        axs[i].stem(Ox[i], Oy[i], colors[i])
        axs[1].set_xlim(0, 20)
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(lables[i][0])
    axs[i].set_ylabel(lables[i][1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_3.pdf', format='pdf')