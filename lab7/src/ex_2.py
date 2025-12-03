from scipy import datasets
import numpy as np
import matplotlib.pyplot as plt

# 2.
def snr(original, compressed):
    noise = original - compressed
    p_signal = np.linalg.norm(original)
    p_noise = np.linalg.norm(noise)

    if p_noise == 0:
        return np.inf
    
    return 20*np.log10(p_signal/p_noise)


X = datasets.face(gray=True)
Y = np.fft.fft2(X)
freq_db = 20*np.log10(abs(Y))

treshold = 0
max_snr = 20
current_snr = np.inf

while current_snr > max_snr:
    mask = freq_db > treshold

    Y_comp = Y * mask
    X_comp = np.real(np.fft.ifft2(Y_comp))

    current_snr = snr(X, X_comp)
    treshold += 5


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(X, cmap='gray')
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(X_comp, cmap='gray')
plt.title(f"Compressed \n(SNR = {max_snr}dB)")

plt.savefig('./img/Ex_2.pdf', format='pdf')