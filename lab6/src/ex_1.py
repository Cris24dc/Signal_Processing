import matplotlib.pyplot as plt
import numpy as np

# 1.
B = 1

time = np.linspace(-3, 3, 800)
sinc = np.power(np.sinc(B * time), 2)

Fs_list = [1.0, 1.5, 2.0, 4.0]
Ts_list = [1/Fs for Fs in Fs_list]

sampled_time = [np.arange(int(np.ceil(-3 / Ts)), int(np.floor(3 / Ts)) + 1) * Ts for Ts in Ts_list]
sampled_sinc = [np.power(np.sinc(B * t), 2) for t in sampled_time]
N = len(sampled_time)
x_hat = []

for i in range(4):
    Ts = Ts_list[i]
    n_samples = sampled_time[i]
    x_n = sampled_sinc[i]
    x_recon = np.zeros_like(time)
    for n in range(len(n_samples)):
        x_recon += x_n[n] * np.sinc((time - n_samples[n]) / Ts)

    x_hat.append(x_recon)

lables = [('t[s]', 'Amplitude')]
titles = [f'Fs = {fs} Hz' for fs in Fs_list]
colors = ['black', 'limegreen', 'orange']

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.ravel()
fig.suptitle('Functia sinc2(t), reconstructia sa si puncte de esantionare')

for i in range(0, 4):
    axs[i].plot(time, sinc, colors[0])
    axs[i].plot(time, x_hat[i], colors[1], linewidth=3, dashes=(1.5, 2))
    axs[i].stem(sampled_time[i], sampled_sinc[i], colors[2])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('t[s]')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_1.pdf', format='pdf')

# Pentru o valoare mai mare a B-ului
# frecventa de esantionare de 2.0 Hz nu mai este
# suficienta pentru a reprezenta corect semnalul
