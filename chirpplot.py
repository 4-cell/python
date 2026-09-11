import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

# Parameters
fs = 44100       # Sampling rate (Hz)
duration = 0.050 # 50 ms
f = 300          # Cosine frequency (Hz)

# Time array: 0 to 50 ms
t = np.arange(0, duration, 1 / fs)

# 1. 300 Hz cosine
cos_300 = np.cos(2 * np.pi * f * t)

# 2. Chirp from 300 Hz to 1500 Hz
chirp_300_1500hz = chirp(
    t,
    f0=300,
    f1=1500,
    t1=duration,
    method='linear'
)

# Print information
print("Number of samples:", len(t))
print("cos_300 shape:", cos_300.shape)
print("chirp_300_1500hz shape:", chirp_300_1500hz.shape)

# 3. Plot both signals
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t * 1000, cos_300)
plt.title("300 Hz Cosine")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t * 1000, chirp_300_1500hz)
plt.title("Linear Chirp: 300 Hz → 1500 Hz")
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()
