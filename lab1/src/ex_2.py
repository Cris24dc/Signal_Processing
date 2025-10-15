import numpy as np
import matplotlib.pyplot as plt

# 2. a)
time_sign1 = np.linspace(0, 0.03, 1600)
x_sign1 = np.sin(800*np.pi*time_sign1)

fig, ax = plt.subplots(1)
fig.suptitle('Semnal 400Hz si 1600 esantioane')

ax.plot(time_sign1, x_sign1)
ax.grid()
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('./img/Ex_2_a.pdf', format='pdf')

# 2. b)
time_sign2 = np.linspace(0, 3, 800)
x_sign2 = np.sin(1600*np.pi*time_sign2)

fig, ax = plt.subplots(1)
fig.suptitle('Semnal 800Hz pe 3 secunde')

ax.plot(time_sign2, x_sign2)
ax.grid()
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('./img/Ex_2_b.pdf', format='pdf')

# 2. c)
time_sign3 = np.linspace(0, 5, 240)
x_sign3 = (240*time_sign3) % 1

fig, ax = plt.subplots(1)
fig.suptitle('Semnal sawtooth')

ax.plot(time_sign3, x_sign3)
ax.grid()
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_ylim(-0.5, 2)

plt.tight_layout()
plt.savefig('./img/Ex_2_c.pdf', format='pdf')

# 2. d)
time_sign4 = np.linspace(0, 5, 300)
x_sign4 = 1/4*np.sign(np.sin(600*np.pi*time_sign4))

fig, ax = plt.subplots(1)
fig.suptitle('Semnal square')

ax.plot(time_sign4, x_sign4)
ax.grid()
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('./img/Ex_2_d.pdf', format='pdf')

# 2. e)
time_sign5 = np.random.rand(128, 128)

fig, ax = plt.subplots(1)
fig.suptitle('Semnal 2D random')

ax.imshow(time_sign5, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.tight_layout()
plt.savefig('./img/Ex_2_e.pdf', format='pdf')

# 2. f)
def f(x):
    return x**2 + x

time_sign6 = np.arange(128 * 128)
x_sign6 = f(time_sign6).reshape((128, 128))

fig, ax = plt.subplots(1)
fig.suptitle('Semnal 2D al lui f(x) = x^2 + x')

ax.imshow(x_sign6, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.tight_layout()
plt.savefig('./img/Ex_2_f.pdf', format='pdf')