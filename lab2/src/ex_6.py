import numpy as np
import matplotlib.pyplot as plt

# 6. a)
time_sign = np.linspace(0, 1, 200)
x_sign1 = np.sin(100*2*np.pi*time_sign)
x_sign2 = np.sin(50*2*np.pi*time_sign)
x_sign3 = np.sin(0*2*np.pi*time_sign)

titles = ['Semnal f = fs/2', 'Semnal f = fs/4', 'Semnal f = 0 Hz']
signal = [x_sign1, x_sign2, x_sign3]

fig, axs = plt.subplots(3, figsize=(10, 12))
fig.suptitle('Semnale de tip sinus cu frecvente fundamentale')

for i in range(0, 3):
    axs[i].plot(time_sign, signal[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_6.pdf', format='pdf')

# Obs:
# fs/2, fs/4 -> frecventa semnalului fiind mare, semnalul devine ascutit si des,
#               iar frecventa de esantionare de 4 ori mai mare, este mai aproape de adevar
#               decat frecventa de esantionare de 2 ori mai mare
# fs = 0 Hz  -> valoarea semnalului nu se modifica deloc in timp