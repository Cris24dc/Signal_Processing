import matplotlib.pyplot as plt
import numpy as np

data = np.genfromtxt('./data/train.csv', delimiter=',')
signal = np.array([elem[2] for elem in data[1:]])
N = len(signal)
time = np.linspace(0, 1, N)

plt.title('Data')
plt.plot(time, signal, 'olivedrab')
plt.grid()
plt.tight_layout()
plt.savefig('./img/Data.pdf', format='pdf')

# 1. a)

# "Numarul de masini care trec printr-o intersectie a fost masurat din ora in ora"
# Deci frecventa de esantionare este:
# fs = 1/T = 1/3600 Hz = 0.00027 Hz

# 1. b)

# Fisierul contine 18288 esantioane 
# => 18287 ore =>
# => 761 zile si 23 ore

# 1. c)

# fs = 1/3600 Hz, deci frecventa maxima
# prezenta in semnal conform frecventei Nyquist
# f_max < fs / 2 este 
# f_max = 0.000138 Hz

# 1. d)

X = np.fft.fft(signal)
fs = 1 / 3600
freq_Ox = np.arange(N) * fs / N
freq_Ox_half = freq_Ox[:(N // 2)]
X_abs = np.abs(X) / N
X_abs_half = X_abs[:(N // 2)]

Ox = [time, freq_Ox_half]
Oy = [signal, X_abs_half]

titles = ['Data', 'Absolute Value']
lables = [('Time', 'Amplitude'), ('Frequency', 'Magnitude')]
colors = ['olivedrab', 'mediumslateblue']

fig, axs = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('Modulul transformatei Fourier')

for i in range(0, 2):
    if i == 0:
        axs[i].plot(Ox[i], Oy[i], colors[i])
    else:
        axs[i].plot(Ox[i], Oy[i], colors[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(lables[i][0])
    axs[i].set_ylabel(lables[i][1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_1_d.pdf', format='pdf')

# 1. e)

signal_X0 = signal - np.mean(signal)
N_X0 = len(signal_X0)
time_X0 = np.linspace(0, 1, N_X0)

X_X0 = np.fft.fft(signal_X0)

freq_Ox_X0 = np.arange(N_X0) * fs / N_X0
freq_Ox_X0_half = freq_Ox_X0[:(N_X0 // 2)]
X_abs_X0 = np.abs(X_X0) / N_X0
X_abs_X0_half = X_abs_X0[:(N_X0 // 2)]

Ox = [time_X0, freq_Ox_X0_half]
Oy = [signal_X0, X_abs_X0_half]

fig, axs = plt.subplots(2, 1, figsize=(10, 8))
fig.suptitle('Modulul transformatei Fourier fara componenta continua')

for i in range(0, 2):
    if i == 0:
        axs[i].plot(Ox[i], Oy[i], colors[i])
    else:
        axs[i].plot(Ox[i], Oy[i], colors[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(lables[i][0])
    axs[i].set_ylabel(lables[i][1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_1_e.pdf', format='pdf')

# 1. f)

X_abs_sorted = np.argsort(X_abs_half[1:])
first4 = X_abs_sorted[-4:] + 1
first4 = first4[::-1]

for i, index in enumerate(first4):
    freq_value = freq_Ox_half[index]
    freq_amount = X_abs_half[index]
    
    periodicity_s = 1.0 / freq_value
    periodicity_h = periodicity_s / 3600.0
    periodicity_d = periodicity_h / 24.0

    print(f"{i+1}:")
    print(f"Freq: {freq_value:.8f} Hz")
    print(f"Magnitude: {freq_amount:.2f}")
    print(f"Periodicity: {periodicity_d:.2f} days")

# Result:
# 1:
# Freq: 0.00000002 Hz
# Magnitude: 66.85
# Periodicity: 762.00 days
# 2:
# Freq: 0.00000003 Hz
# Magnitude: 35.22
# Periodicity: 381.00 days
# 3:
# Freq: 0.00001157 Hz
# Magnitude: 27.10
# Periodicity: 1.00 days
# 4:
# Freq: 0.00000005 Hz
# Magnitude: 25.22
# Periodicity: 254.00 days

# 1. g)

start_index = 4920
samples = 30 * 24
end_index = start_index + samples

signal_month = signal[start_index:end_index]
time_month = np.linspace(0, 30, samples)

fig, axs = plt.subplots(1, 1, figsize=(10, 6))
fig.suptitle('Data over a month')

axs.plot(time_month, signal_month, colors[0])
axs.set_xlabel("Time")
axs.set_ylabel("Amplitude")
axs.grid()

plt.tight_layout()
plt.savefig('./img/Ex_1_g.pdf', format='pdf')

# 1. h)

# Putem cauta periodicitatea unei saptamani si
# sa vedem cate perioade avem, iar apoi din ultima
# data inregistrata, scadem numarul de saptamani 
# si aflam data de start.
# Neajunsul acestei solutii este ca daca nu avem
# nici macar data de final, nu putem afla data de inceput.

# 1. i)

# deoarece, bazat pe comportamentul uman, 
# cele mai dese cicluri se intampla la
# o perioada de minim 24 de ore si maxim o saptamana.

T_min = 24 * 3600
T_max = 24 * 7 * 3600
f_min = 1/ T_min
f_max = 1/ T_max

filter = np.where(np.abs(freq_Ox) >= f_min, 1, 0)
filter = np.where(np.abs(freq_Ox) <= f_max, 1, 0)
filtered_X = X * filter
filtered_signal = np.real(np.fft.ifft(filtered_X))

fig, axs = plt.subplots(1, 1, figsize=(10, 6))
fig.suptitle('Filtered Signal')

axs.plot(time, filtered_signal, colors[0])
axs.set_xlabel("Time")
axs.set_ylabel("Amplitude")
axs.grid()

plt.tight_layout()
plt.savefig('./img/Ex_1_i.pdf', format='pdf')