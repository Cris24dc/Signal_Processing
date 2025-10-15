import numpy as np
import matplotlib.pyplot as plt

# 1. a)
t = np.arange(0, 0.03 + 0.0005, 0.0005)

# 1. b)
x = np.cos(520*np.pi*t + np.pi/3)
y = np.cos(280*np.pi*t - np.pi/3)
z = np.cos(120*np.pi*t + np.pi/3)

fig, axs = plt.subplots(3, figsize=(8, 6))
fig.suptitle('Semnal Continuu', fontsize=14)

axs[0].plot(t, x)
axs[0].set_title('x(t)')
axs[0].grid()

axs[1].plot(t, y)
axs[1].set_title('y(t)')
axs[1].grid()

axs[2].plot(t, z)
axs[2].set_title('z(t)')
axs[2].grid()

fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('./Continuu.pdf', format='pdf')

# 1. c)
T = 1 / 200 
t_e = np.arange(0, 0.03 + T, T)
x_e = np.cos(520*np.pi*t_e + np.pi/3)
y_e = np.cos(280*np.pi*t_e - np.pi/3)
z_e = np.cos(120*np.pi*t_e + np.pi/3)

fig, axs = plt.subplots(3, figsize=(8, 6))
fig.suptitle('Semnal Esantion', fontsize=14)

axs[0].stem(t_e, x_e)
axs[0].set_title('x[t]')
axs[0].grid()

axs[1].stem(t_e, y_e)
axs[1].set_title('y[t]')
axs[1].grid()

axs[2].stem(t_e, z_e)
axs[2].set_title('z[t]')
axs[2].grid()

fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('./Esantion.pdf', format='pdf')

# 2. a)
time_sign1 = np.arange(0, 0.05, 1/1600)
x_sign1 = np.sin(800*np.pi*time_sign1)

fig, ax = plt.subplots(1, figsize=(8, 6))
fig.suptitle('Semnal 400Hz si 1600 esantioane', fontsize=14)

ax.plot(time_sign1, x_sign1)
ax.set_title('x[sign1]')
ax.grid()

fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('./Sign1.pdf', format='pdf')

# 2. b)
time_sign2 = np.linspace(0, 3, 200)
x_sign2 = np.sin(1600*np.pi*time_sign2)

fig, ax = plt.subplots(1, figsize=(8, 6))
fig.suptitle('Semnal 800Hz pe 3 secunde', fontsize=14)

ax.plot(time_sign2, x_sign2)
ax.set_title('x[sign2]')
ax.grid()

fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('./Sign2.pdf', format='pdf')