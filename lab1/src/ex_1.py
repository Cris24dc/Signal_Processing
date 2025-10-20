import numpy as np
import matplotlib.pyplot as plt

# 1. a)
t = np.linspace(0, 0.03, int(0.03/0.0005))

# 1. b)
x = np.cos(520*np.pi*t + np.pi/3)
y = np.cos(280*np.pi*t - np.pi/3)
z = np.cos(120*np.pi*t + np.pi/3)

title = ['x(t)', 'y(t)', 'z(t)']
funct = [x, y, z]

fig, axs = plt.subplots(3)
fig.suptitle('Semnalele x(t), y(t), z(t)')
for ax in axs.flat:
    ax.grid()
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

for i in range(3):
    axs[i].plot(t, funct[i])
    axs[i].set_title(title[i])
    axs[i].set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('./img/Ex_1_b.pdf', format='pdf')

# 1. c)
fs = 200
Te = 1/fs
t_e = np.linspace(0, 0.03, int(0.03/Te))
x_e = np.cos(520*np.pi*t_e + np.pi/3)
y_e = np.cos(280*np.pi*t_e - np.pi/3)
z_e = np.cos(120*np.pi*t_e + np.pi/3)

title = ['x[n]', 'y[n]', 'z[n]']
funct = [x_e, y_e, z_e]

fig, axs = plt.subplots(3)
fig.suptitle('Semnalele x[n], y[n], z[n]')
for ax in axs.flat:
    ax.grid()
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

for i in range(3):
    axs[i].stem(t_e, funct[i])
    axs[i].set_title(title[i])
    axs[i].set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('./img/Ex_1_c.pdf', format='pdf')
