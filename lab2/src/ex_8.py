import numpy as np
import matplotlib.pyplot as plt

# 8. a)
alpha = np.linspace(-np.pi/2, np.pi/2, 200)
sin_alpha = np.sin(alpha)
taylor = alpha
pade = (alpha - (7 * alpha**3) / 60) / (1 + (alpha**2) / 20)
eroare_taylor = np.abs(sin_alpha - taylor)
eroare_pade = np.abs(sin_alpha - pade)

titles = ['sin(x)', 'Semnal aproximat Taylor', 'Semnal aproximat Pade', 'Eroare Taylor', 'Eroare Pade']
time = [alpha, alpha, alpha, alpha, alpha]
signal = [sin_alpha, taylor, pade, eroare_taylor, eroare_pade]

fig, axs = plt.subplots(5, figsize=(10, 12))
fig.suptitle('Aproximare Taylor si Pade pentru sin(x)')

for i in range(0, 5):
    axs[i].plot(time[i], signal[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_8_a.pdf', format='pdf')

# 8. b)
fig, axs = plt.subplots(3, figsize=(10, 12))
fig.suptitle('Aproximare Taylor si Pade pentru sin(x) pe Oy logaritmic')

for i in range(0, 3):
    axs[i].plot(time[i], signal[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.yscale('log')
plt.savefig('./img/Ex_8_b.pdf', format='pdf')