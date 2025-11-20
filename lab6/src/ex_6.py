import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np

data = np.genfromtxt('./data/train.csv', delimiter=',')
signal = np.array([elem[2] for elem in data[1:]])
N = len(signal)
time = np.linspace(0, N/24, N)

fig, axs = plt.subplots(1, 1, figsize=(10, 8))
fig.suptitle('Data')

axs.plot(time, signal, 'olivedrab')
axs.set_xlabel('Time (days)')
axs.set_ylabel('Amplitude')
axs.grid()

plt.tight_layout()
plt.savefig('./img/Data.pdf', format='pdf')

# 1. a)
days3 = 24 * 3
rand_start = np.random.randint(0, N - days3 + 1)
signal = signal[rand_start:rand_start+days3]
N = len(signal)
time = np.linspace(rand_start, rand_start+days3, N)

fig, axs = plt.subplots(1, 1, figsize=(10, 8))
fig.suptitle('Data over 3 days')

axs.plot(time, signal, 'olivedrab')
axs.set_xlabel('Time (days)')
axs.set_ylabel('Amplitude')
axs.grid()

plt.tight_layout()
plt.savefig('./img/Ex_6_a.pdf', format='pdf')

# 1. b)
colors = ['darkgray', 'darkorange', 'lightseagreen', 'mediumpurple', 'olivedrab']

w = [5, 9, 13, 17]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs = axs.ravel()
fig.suptitle('Filtered Data')

for i in range(0, 4):
    filtered_signal = np.convolve(signal, np.ones(w[i]), mode='valid') / w[i]
    time_filter = time[:len(filtered_signal)]

    axs[i].plot(time, signal, colors[0])
    axs[i].plot(time_filter, filtered_signal, colors[i + 1])
    axs[i].set_title(f'w = {w[i]}')
    axs[i].set_xlabel('Time (days)')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_6_b.pdf', format='pdf')

# 1. c)

# Aceastra frecventa de taiere, pastreaza trend-urile zilnice
# scotand varietatile rapide ce se pot intampla la o perioada
# de sub 6 ore
cutoff_freq = 4

nyquist = 24 / 2
# Normalizam frecventa
Wn = cutoff_freq / nyquist 

# 1. d)
b_butt, a_butt = sig.butter(5, Wn, btype='low')
b_cheb, a_cheb = sig.cheby1(5, 5, Wn, btype='low')

# 1. e)
signal_butt = sig.filtfilt(b_butt, a_butt, signal)
signal_cheb = sig.filtfilt(b_cheb, a_cheb, signal)

titles = ['Butterworth', 'Chebyshev']
filtered_signals = [signal_butt ,signal_cheb]

fig, axs = plt.subplots(2, 1, figsize=(10, 8))
axs = axs.ravel()
fig.suptitle('Filtrele Butterworth si Chebyshev aplicate pe semnal')

for i in range(0, 2):
    axs[i].plot(time, signal, colors[0])
    axs[i].plot(time, filtered_signals[i], colors[i + 1])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_6_e.pdf', format='pdf')

# Aleg filtrul Butterworth, deoarece Chebyshev
# taie mai abrupt frecventele inalte

# 1. f)
orders = [1, 12]
rps = [0.1, 10]

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.ravel()
fig.suptitle('Efectele Ordinului si a parametrului RP')

for i, order in enumerate(orders):
    b_butt, a_butt = sig.butter(order, Wn, btype='low')
    filtered = sig.filtfilt(b_butt, a_butt, signal)
    
    axs[i].plot(time, signal, colors[0])
    axs[i].plot(time, filtered, colors[i+1])
    axs[i].set_title(f'Butterworth: Ordin {order}')
    axs[i].legend()
    axs[i].grid()

for i, rp in enumerate(rps):
    idx = i + 2
    b, a = sig.cheby1(5, rp, Wn, btype='low')
    filtered = sig.filtfilt(b, a, signal)
    
    axs[idx].plot(time, signal, colors[0])
    axs[idx].plot(time, filtered, colors[i+1])
    axs[idx].set_title(f'Chebyshev (Ordin 5): RP {rp}dB')
    axs[idx].legend()
    axs[idx].grid()

plt.tight_layout()
plt.savefig('./img/Ex_6_f.pdf', format='pdf')

# Butterworth Ordin 1: Pierde detalii din semnalul original
# Butterworth Ordin 12: Match-uieste mai bine detaliile semnalului original
# Chebyshev RP 0.1dB: Se comporta aproape ca un Butterworth
# Chebyshev RP 10dB: Este prea smooth si pierde schimbarile bruste de amplitudine
