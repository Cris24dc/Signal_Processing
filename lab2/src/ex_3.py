import numpy as np
from scipy.io import wavfile
import sounddevice as sd

# 3.
rate = int(10e5)

time_sign1 = np.linspace(0, 3, 1600)
x_sign1 = np.sin(800*np.pi*time_sign1)

time_sign2 = np.linspace(0, 3, 800)
x_sign2 = np.sin(1600*np.pi*time_sign2)

time_sign3 = np.linspace(0, 5, 240)
x_sign3 = (240*time_sign3) % 1

time_sign4 = np.linspace(0, 5, 300)
x_sign4 = 1/4*np.sign(np.sin(600*np.pi*time_sign4))

wavfile.write('./img/Ex_3_a.wav', rate, x_sign1)
# wavfile.write('./img/Ex_3_b.wav', rate, x_sign2)
# wavfile.write('./img/Ex_3_c.wav', rate, x_sign3)
# wavfile.write('./img/Ex_3_d.wav', rate, x_sign4)

fs ,x_sign1 = wavfile.read('./img/Ex_3_a.wav')
sd.play(x_sign1,fs)
sd.wait()
