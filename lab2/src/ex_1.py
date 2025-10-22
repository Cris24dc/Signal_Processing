import numpy as np
import matplotlib.pyplot as plt

# 1.
t = np.linspace(0, 3, 200)
sin_sign1 = 1/2*np.sin(2.2*np.pi*t + np.pi/2)
cos_sign2 = 1/2*np.cos(2.2*np.pi*t)

fig, axs = plt.subplots(2)
fig.suptitle('Semnale de tip Sin si Cos')
for ax in axs.flat:
    ax.grid()
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')

axs[0].plot(t, sin_sign1)
axs[0].set_title('Sin')
axs[0].set_ylim(-1.5, 1.5)

axs[1].plot(t, cos_sign2)
axs[1].set_title('Cos')
axs[1].set_ylim(-1.5, 1.5)

plt.tight_layout()
plt.savefig('./img/Ex_1.pdf', format='pdf')