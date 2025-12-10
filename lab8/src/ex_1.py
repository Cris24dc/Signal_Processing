import numpy as np
import matplotlib.pyplot as plt

# 1. a)
N = 1000
time = np.arange(N)

trend_y = 0.00001*time**2 + 0.0003*time + 1
seasonal_y = 5 * (1/2*np.cos(2/50*np.pi*time + 1) + 1/5*np.cos(2/80*np.pi*time + 3))
residuals_y = np.random.normal(0, 1, N)
time_series_y = trend_y + seasonal_y + residuals_y

Ox = [time] * 4
Oy = [trend_y, seasonal_y, residuals_y, time_series_y]
lables = [('Time', 'Amplitude')]
titles = ['Trend', 'Seasonal', 'Residuals', 'Time Series']
colors = ['darkolivegreen', 'darkcyan', 'rebeccapurple']

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.ravel()
fig.suptitle('Time series')

for i in range(0, 4):
    axs[i].plot(Ox[i], Oy[i], colors[0])
    axs[i].set_title(titles[i])
    axs[i].set_xlabel(lables[0][0])
    axs[i].set_ylabel(lables[0][1])
    axs[i].grid()

plt.tight_layout()
plt.savefig('./img/Ex_1_a.pdf', format='pdf')

# 1. b)
autocorrelation = np.correlate(time_series_y, time_series_y, mode='full')
autocorrelation = autocorrelation / np.max(autocorrelation)
window = np.arange(-N + 1, N)

fig, axs = plt.subplots(1, 1, figsize=(12, 8))
fig.suptitle('Autocorrelation')

axs.plot(window, autocorrelation, colors[0])
axs.set_xlabel(lables[0][0])
axs.set_ylabel(lables[0][1])
axs.grid()

plt.tight_layout()
plt.savefig('./img/Ex_1_b.pdf', format='pdf')

# 1. c)
p = 20
train_N = int(N * 0.80)

y_target = time_series_y[p:train_N]

X_train = []
for i in range(p, train_N):
    X_train.append(time_series_y[i-p:i][::-1])
X_train = np.array(X_train)

coeff, _, _, _ = np.linalg.lstsq(X_train, y_target, rcond=None)

X_test = []
for i in range(train_N, N):
    X_test.append(time_series_y[i-p:i][::-1])
X_test = np.array(X_test)

y_pred_test = X_test @ coeff

Ox = [time, time[train_N:]]
Oy = [time_series_y, y_pred_test]
lables = [('Time', 'Amplitude')]
legend = ['Semnal Original', 'Predicție AR']
titles = ['Original signal', 'Prediction AR']

fig, axs = plt.subplots(1, 1, figsize=(12, 8))
fig.suptitle('AR prediction (p = 50)')

axs.plot(Ox[0], Oy[0], colors[1], label=legend[0])
axs.plot(Ox[1], Oy[1], colors[2], label=legend[1], linestyle='--')
axs.set_xlabel(lables[0][0])
axs.set_ylabel(lables[0][1])
axs.grid()
axs.legend()

plt.tight_layout()
plt.savefig('./img/Ex_1_c.pdf', format='pdf')

# 1. d)
p_values = range(1, 20) 
m_values = range(50, 400, 10)

best_rmse = np.inf
best_p = -1
best_m = -1

for i, p in enumerate(p_values):
    for j, m in enumerate(m_values):
        end = train_N
        start = train_N - m
        
        y_train = time_series_y[start:train_N]
        y_target = y_train[p:]
        
        X_train = []
        for k in range(p, len(y_train)):
            X_train.append(y_train[k-p:k][::-1])
        X_train = np.array(X_train)
        
        coeffs, _, _, _ = np.linalg.lstsq(X_train, y_target, rcond=None)

        X_valid = []
        for k in range(train_N, N):
            X_valid.append(time_series_y[k-p:k][::-1])
        X_valid = np.array(X_valid)
            
        y_pred = X_valid @ coeffs
        
        rmse = np.sqrt(np.mean((time_series_y[train_N:] - y_pred) ** 2))
        
        if rmse < best_rmse:
            best_rmse = rmse
            best_p = p
            best_m = m

print(f"p = {best_p}")
print(f"m = {best_m}")