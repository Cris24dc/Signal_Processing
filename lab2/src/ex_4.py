import numpy as np
import matplotlib.pyplot as plt

# 4.
time_sign = np.linspace(0, 5, 300)
x_sign1 = np.sin(100*np.pi*time_sign + 50)
x_sign2 = (240*time_sign) % 1
x_sign3 = x_sign1 + x_sign2

titles = ['Semnal sinusoidal', 'Semnal sawtooth', 'Suma semnalelor']
signal = [x_sign1, x_sign2, x_sign3]

fig, axs = plt.subplots(3, figsize=(10, 12))
fig.suptitle('Semnale cu forme de unda diferite si suma lor')

for i in range(0, 3):
    axs[i].plot(time_sign, signal[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_4.pdf', format='pdf')
