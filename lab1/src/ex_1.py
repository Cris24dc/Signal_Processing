import numpy as np
import matplotlib.pyplot as plt

# 1. a)
t = np.linspace(0, 0.03, int(0.3/0.0005))

# 1. b)
x = np.cos(520*np.pi*t + np.pi/3)
y = np.cos(280*np.pi*t - np.pi/3)
z = np.cos(120*np.pi*t + np.pi/3)

fig, axs = plt.subplots(3)
fig.suptitle('Semnalele x(t), y(t), z(t)')
for ax in axs.flat:
    ax.grid()
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

axs[0].plot(t, x)
axs[0].set_title('x(t)')
axs[0].set_ylim(-1.5, 1.5)

axs[1].plot(t, y)
axs[1].set_title('y(t)')
axs[1].set_ylim(-1.5, 1.5)

axs[2].plot(t, z)
axs[2].set_title('z(t)')
axs[2].set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('./img/Ex_1_b.pdf', format='pdf')

# 1. c)
fs = int(0.03/(1/200))
t_e = np.linspace(0, 0.03, fs)
x_e = np.cos(520*np.pi*t_e + np.pi/3)
y_e = np.cos(280*np.pi*t_e - np.pi/3)
z_e = np.cos(120*np.pi*t_e + np.pi/3)

fig, axs = plt.subplots(3)
fig.suptitle('Semnalele x[n], y[n], z[n]')
for ax in axs.flat:
    ax.grid()
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

axs[0].stem(t_e, x_e)
axs[0].set_title('x[n]')
axs[0].set_ylim(-1.5, 1.5)

axs[1].stem(t_e, y_e)
axs[1].set_title('y[n]')
axs[1].set_ylim(-1.5, 1.5)

axs[2].stem(t_e, z_e)
axs[2].set_title('z[n]')
axs[2].set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('./img/Ex_1_c.pdf', format='pdf')
