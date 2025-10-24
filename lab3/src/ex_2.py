import matplotlib.pyplot as plt
import numpy as np

# 2. a)
index = 420
time = np.linspace(0, 1, 800)
signal = np.cos(8*np.pi*time)
complex = signal*np.exp(-2j*np.pi*time)

Ox = [time, complex.real]
Oy = [signal, complex.imag]
points = [(time[index], signal[index]), (complex.real[index], complex.imag[index])]
titles = ['Semnal sinusoidal', 'Semnal in plan Complex']
lables = [('Time', 'Amplitude'), ('Real', 'Imaginary')]
colors = ['olivedrab', 'mediumslateblue']

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig.suptitle('Reprezentarea unui semnal in planul complex')

for i in range(0, 2):
    # vectorul amplitudinii
    if i == 1:
        axs[i].plot([0, points[i][0]], [0, points[i][1]], 'red')
        axs[i].scatter(points[i][0], points[i][1], 50, 'red')
    else:
        axs[i].stem(points[i][0], points[i][1], 'red')
    
    axs[i].plot(Ox[i], Oy[i], colors[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(lables[i][0])
    axs[i].set_ylabel(lables[i][1])
    axs[i].grid()
 
plt.tight_layout()
plt.savefig('./img/Ex_2_a.pdf', format='pdf')

# 2. b)
w_values = [1, 2, 4, 7]
complex = [signal*np.exp(-2j*np.pi*time*w) for w in w_values]

Ox = [elem.real for elem in complex]
Oy = [elem.imag for elem in complex]

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs = axs.ravel()
fig.suptitle('Reprezentarea transformatei Fourier in planul complex')

for i in range(0, 4):
    axs[i].plot(Ox[i], Oy[i], 'mediumvioletred')
    axs[i].set_title(rf'$\omega = {w_values[i]}$')
    axs[i].set_xlabel(lables[1][0])
    axs[i].set_ylabel(lables[1][1])
    axs[i].grid()
 
plt.tight_layout()
plt.savefig('./img/Ex_2_b.pdf', format='pdf')

# 2. c)
complex_dist = [np.sqrt(nr.real**2 + nr.imag**2) for nr in complex]

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs = axs.ravel()
fig.suptitle('Reprezentarea transformatei Fourier in planul complex')

for i in range(0, 4):
    axs[i].scatter(Ox[i], Oy[i], c=complex_dist[i], cmap='viridis', s=10)
    axs[i].set_title(rf'$\omega = {w_values[i]}$')
    axs[i].set_xlabel(lables[1][0])
    axs[i].set_ylabel(lables[1][1])
    axs[i].grid()
 
plt.tight_layout()
plt.savefig('./img/Ex_2_c.pdf', format='pdf')