from scipy import datasets, ndimage
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

pixel_noise = 200
noise = np.random.randint(-pixel_noise, high=pixel_noise+1, size=X.shape)
X_noisy = X + noise
X_denoised = ndimage.gaussian_filter(X_noisy, sigma=2)

snr_noisy = snr(X, X_noisy)
snr_denoised = snr(X, X_denoised)


plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(X, cmap='gray')
plt.title('Original')

plt.subplot(1, 3, 2)
plt.imshow(X_noisy, cmap='gray')
plt.title(f'Noisy\n(SNR = {snr_noisy:.2f}dB)')

plt.subplot(1, 3, 3)
plt.imshow(X_denoised, cmap='gray')
plt.title(f'Denoised\n(SNR = {snr_denoised:.2f}dB)')

plt.savefig('./img/Ex_3.pdf', format='pdf')