import matplotlib.pyplot as plt
import numpy as np

# 4.
n = 20
time = np.arange(n)

x = 1/2*np.cos(8*np.pi*time + np.pi/2) + np.sin(6*np.pi*time) + np.sin(20*np.pi*time)

d = np.random.randint(1, n)
print(f'd: {d}')
y = np.roll(x, d)

X = np.fft.fft(x)
Y = np.fft.fft(y)

recover1 = np.fft.ifft(np.conj(X) * Y).real

recover_d1 = np.argmax(recover1)
print(f'd1: {recover_d1}')

recover2 = np.fft.ifft(Y/X).real
recover_d2 = np.argmax(recover2)
print(f'd2: {recover_d2}')


# diferenta intre cele 2 este ca
# prima masoara asemanarea semnalelor, iar
# cea de-a doua masoara deplasarea necesara
# pentru a ajunge de la x la y. De asta
# in al doilea grafic putem observa un spike
# la valoarea lui d.

Ox = [time] * 2
Oy = [recover1, recover2]

labels = ('Time', 'Amplitude')
titles = ['IFFT(*FFT(x) * FFT(y))', 'IFFT(FFT(y) / FFT(x))']

fig, axs = plt.subplots(2, 1, figsize=(10, 10))
axs = axs.ravel()
fig.suptitle('Recuperare deplasare d')

for i in range(0, 2):
    axs[i].plot(Ox[i], Oy[i], 'olivedrab')
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(labels[0])
    axs[i].set_ylabel(labels[1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_4.pdf', format='pdf')
