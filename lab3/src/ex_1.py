import matplotlib.pyplot as plt
import numpy as np

# 1.
N = 8
fourier_matrix = np.ones((N, N), dtype=complex)
for row in range(1, N):
    for col in range(1, N):
        fourier_matrix[row][col] = np.exp(-2j*np.pi*row*col/N)

# print(fourier_matrix)

fig, axs = plt.subplots(8, figsize=(10, 12))
fig.suptitle('Matricea Fourier')
for row, elem in enumerate(fourier_matrix):
    real_elem  = np.array([a.real for a in elem])
    imag_elem = np.array([b.imag for b in elem])

    axs[row].plot(real_elem, 'mediumvioletred')
    axs[row].plot(imag_elem, 'mediumslateblue')
    axs[row].set_title(f'x[{row}]')
    axs[row].set_xlabel('Time')
    axs[row].set_ylabel('Amplitude')
    axs[row].grid()

plt.tight_layout()
plt.savefig('./img/Ex_1.pdf', format='pdf')

inverse = 1/N * np.conjugate(np.transpose(fourier_matrix))
identity = np.dot(inverse, fourier_matrix)
print(f'Matricea Fourier este unitara: {np.allclose(identity, np.eye(N))}')
