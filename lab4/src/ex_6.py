import matplotlib.pyplot as plt
import numpy as np
import librosa

signal, freq = librosa.load('./img/Ex_5.mp3')
spectrogram_matrix = []
N = len(signal)
group = int(N * 0.01)
overlap = int(group * 0.5)
step = group - overlap


for i in range(0, N - group, step):
    current_group = signal[i:i + group]
    result = np.fft.fft(current_group)
    spectrogram_matrix.append(np.abs(result))

spectrogram_matrix = np.array(spectrogram_matrix).T
spectogram_dB = librosa.amplitude_to_db(spectrogram_matrix)


fig, axs = plt.subplots(1, 1, figsize=(10, 8))
librosa.display.specshow(spectogram_dB, y_axis='log', cmap='viridis')
plt.colorbar(format='%d dB')
plt.title('Audio Spectrogram')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('./img/Ex_6.pdf', format='pdf')
