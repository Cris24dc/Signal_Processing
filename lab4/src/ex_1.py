import matplotlib.pyplot as plt
import numpy as np
import time

# 1.
def DFT(x):
    N = len(x)
    fourier_matrix = np.ones((N, N), dtype=complex)
    for row in range(N):
        for col in range(N):
            fourier_matrix[row][col] = np.exp(-2j*np.pi*row*col/N)

    return np.dot(fourier_matrix, x)


def FFT(x):
    N = len(x)

    if N == 1:
        return x
    else:
        x_even = FFT(x[::2])
        x_odd = FFT(x[1::2])
        complex_exp = np.exp(-2j*np.pi*np.arange(N)/N)

    X = np.ones(N, dtype=complex)

    for k in range(N//2):
        X[k] = x_even[k] + complex_exp[k] * x_odd[k]
        X[k + N // 2] = x_even[k] - complex_exp[k] * x_odd[k]

    return(X)


N_sizes = [128, 256, 512, 1024, 2048, 4096, 8192]
dft_time = []
fft_time = []
np_fft_time = []


for N_size in N_sizes:
    t = np.linspace(0, 2, N_size)
    signal = 1/2*np.cos(8*np.pi*t + np.pi/2) + np.sin(6*np.pi*t) + np.sin(20*np.pi*t)

    start=time.time()
    DFT(signal)
    dft_time.append(time.time() - start)

    start=time.time()
    FFT(signal)
    fft_time.append(time.time() - start)

    start=time.time()
    np.fft.fft(signal)
    np_fft_time.append(time.time() - start)


plt.figure()
plt.title('DFT vs FFT vs np.fft')
plt.plot(N_sizes, dft_time, color='cyan', label="DFT")
plt.plot(N_sizes, fft_time, color='limegreen', label="FFT")
plt.plot(N_sizes, np_fft_time, color='purple', label="np.fft")
plt.xlabel('N vector size')
plt.ylabel('Execution Time')
plt.legend()
plt.yscale('log')
plt.grid()

plt.tight_layout()
plt.savefig('./img/Ex_1.pdf', format='pdf')
