import numpy as np
from scipy.io import wavfile
import sounddevice as sd

# 5.
time_sign = np.linspace(0, 3, 800)
x_sign1 = np.sin(1600*np.pi*time_sign)
x_sign2 = np.sin(200*np.pi*time_sign)
x_sign3 = np.concatenate((x_sign1, x_sign2))

rate = int(10e5)
wavfile.write('./img/Ex_5.wav', rate, x_sign3)

fs ,x_sign = wavfile.read('./img/Ex_5.wav')
sd.play(x_sign,fs)
sd.wait()

# Obs:
# daca frecventa creste, semnalul are un sunet mai inalt