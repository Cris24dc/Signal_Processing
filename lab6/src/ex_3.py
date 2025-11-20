import numpy as np

# 3.
N = 3
p_coef = np.random.randint(-100, 100, N + 1)
q_coef = np.random.randint(-100, 100, N + 1)
l = len(p_coef) + len(q_coef) - 1

p_fft = np.fft.fft(p_coef, l)
q_fft = np.fft.fft(q_coef, l)

p = np.poly1d(p_coef)
q = np.poly1d(q_coef)

result_prod = p * q
result_fft = np.poly1d(np.fft.ifft(p_fft * q_fft).real)

print("Inmultirea polinoamelor directa: \n", result_prod)
print("Inmultire folosind fft: \n", result_fft)