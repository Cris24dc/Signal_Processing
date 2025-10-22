import numpy as np
import matplotlib.pyplot as plt

# 7. a)
time_sign = np.linspace(0, 5, 1000)
x_sign1 = np.sin(6*np.pi*time_sign)
 
time_sign_decim = time_sign[0::4]
x_sign1_decim = x_sign1[0::4]

titles = ['Semnal original', 'Semnal decimat de la primul element']
time = [time_sign, time_sign_decim]
signal = [x_sign1, x_sign1_decim]

fig, axs = plt.subplots(2, figsize=(10, 12))
fig.suptitle('Semnal decimat 1/4')

for i in range(0, 2):
    axs[i].plot(time[i], signal[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_7_a.pdf', format='pdf')

# Obs:
# Semnalul isi pastreaza forma (chiar daca are locuri unde apar linii),
# dar deoarece ultimele 3 valori din vector nu exista, plot-ul omite informatie la final

# 7. b)
time_sign_decim = time_sign[1::4]
x_sign1_decim = x_sign1[1::4]

titles = ['Semnal original', 'Semnal decimat de la al doilea element']
time = [time_sign, time_sign_decim]
signal = [x_sign1, x_sign1_decim]

fig, axs = plt.subplots(2, figsize=(10, 12))
fig.suptitle('Semnal decimat 1/4')

for i in range(0, 2):
    axs[i].plot(time[i], signal[i])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_7_b.pdf', format='pdf')

# Obs:
# la fel ca la cel de sus, dar acum se pierde mai putin informatie la final,
# insa se pierde putina informatie si la inceput