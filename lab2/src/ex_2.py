import numpy as np
import matplotlib.pyplot as plt

# 2. a)
t = np.linspace(0, 2, 200)
sign1 = np.sin(2*np.pi*t + 2)
sign2 = np.sin(3*np.pi*t + 3)
sign3 = np.sin(4*np.pi*t + 4)
sign4 = np.sin(5*np.pi*t + 5)

plt.figure()
plt.title('4 sinusoide')
plt.plot(t, sign1, color='cyan')
plt.plot(t, sign2, color='orange')
plt.plot(t, sign3, color='limegreen')
plt.plot(t, sign4, color='purple')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.savefig('./img/Ex_2_a.pdf', format='pdf')

# 2. b)
SNR = [0.1, 1, 10, 100]
z = np.random.normal(size = 200)
gamma = []
for i in range(0, 4):
    gamma.append(np.sqrt(np.power((np.linalg.norm(sign1)), 2) / (np.power((np.linalg.norm(z)), 2) * SNR[i])))

fig, axs = plt.subplots(4, figsize=(10, 12))
fig.suptitle('Semnale cu zgomot')

titles = ['SNR = 0.1', 'SNR = 1', 'SNR = 10', 'SNR = 100']

for i in range(0, 4):
    axs[i].plot(t, sign1 + gamma[i] * z)
    axs[i].set_title(titles[i])
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Amplitude')
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_2_b.pdf', format='pdf')