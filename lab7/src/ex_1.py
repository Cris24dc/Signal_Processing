import numpy as np
import matplotlib.pyplot as plt

# 1.
N = 100
X = np.arange(N)
Y = np.arange(N)

X_1, Y_1 = np.meshgrid(X, Y)

image1 = np.sin(2*np.pi*X_1 + 3*np.pi*Y_1)
freqs1 = np.fft.fft2(image1)
image2 = np.sin(4*np.pi*X_1) + np.cos(6*np.pi*Y_1)
freqs2 = np.fft.fft2(image2)
# ---
freqs3 = np.zeros((N, N))
freqs3[0][5] = freqs3[0][N-5] = 1.0
image3 = np.fft.ifft2(freqs3)
freqs4 = np.zeros((N, N))
freqs4[5][0] = 1.0
image4 = np.fft.ifft2(freqs4)
freqs5 = np.zeros((N, N))
freqs5[5][5] = freqs5[N-5][N-5] = 1.0
image5 = np.fft.ifft2(freqs5)

time_domain = [image1, image2, image3, image4, image5]
freqs_domain = [freqs1, freqs2, freqs3, freqs4, freqs5]
titles = ["Image in time domain", "Image in frequency domain"]

fig, axs = plt.subplots(5, 2, figsize=(10, 18), constrained_layout=True)
axs = axs.ravel()

for i, j in zip(range(0, 10, 2), range(0, 5)):
    im1 = axs[i].imshow(np.real(time_domain[j]))
    axs[i].set_title(titles[0])
    axs[i].set_ylabel('Amplitude')
    axs[i].set_xlabel('Time')
    fig.colorbar(im1, ax=axs[i], fraction=0.046, pad=0.04)

    im2 = axs[i+1].imshow(np.log1p(np.abs(freqs_domain[j])))
    axs[i+1].set_title(titles[1])
    axs[i+1].set_ylabel('Magnitude')
    axs[i+1].set_xlabel('Frequency')
    fig.colorbar(im2, ax=axs[i+1], fraction=0.046, pad=0.04)

plt.savefig('./img/Ex_1.pdf', format='pdf')

# Obs imagine 2: Deoarece perioada lui sin si cos este 2pi, iar 4pi si 6pi sunt multiplii ai lui 2pi,
# ambele semnale, cel orizontal si cel vertical ar trebui sa fie 0 (o imagine monocroma).
# In schimb doar cos ajunge sa fie 0. Deoarece in multiplii de 2pi, cos are valoarea 1,
# fiind in varf, acesta are panta 0 (o linie orizontala), iar sin avand valoarea 0, acesta are
# panta 1 (o linie oblica). Deoarece np.pi nu este o valoare continua, ci este o aproximare,
# aproximarea lui sin, ajunge sa cumuleze eroarea lui pi. Deci pe imagine, observam cum eroarea
# lui pi este cumulata pentru semnalul orizontal.

# Obs imagine 1: Deoarece in sin, avem un semnal (X + 1.5*Y) * 2pi, asta inseamna ca
# in imagine doar observam cumulul erorii generat de sinus si valoarea aproximata a lui pi.

# Obs imagine 3, 4, 5: Daca activam 2 componente simetrice in frecventa,
# doar pe prima linie sau doar pe prima coloana, in timp o sa avem doar un semnal orizontal,
# respectiv doar un semnal vertical. Daca activam 2 componente simetrice si pe linie si pe coloana,
# o sa obtinem o imagine cu 2 semnale, unul vertical si unul orizontal.