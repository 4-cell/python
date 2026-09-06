import matplotlib.pyplot as plt
import numpy as np

# 1. Generate 1 second of a 300 Hz cosine wave sampled at 44.1 kHz
sample_rate = 44_100
duration = .01
frequency = 300
x = np.arange(sample_rate * duration) / sample_rate
y = np.cos(2 * np.pi * frequency * x)

# 2. Create the plot
plt.figure(figsize=(8, 4))
plt.plot(
	x,
	y,
	label="300 Hz Cosine Wave",
	color="royalblue",
	marker=".",
	linestyle="None",
	markersize=1,
)

# 3. Add styling elements
plt.title("300 Hz Cosine Wave", fontsize=14, fontweight="bold")
plt.xlabel("Time (seconds)", fontsize=11)
plt.ylabel("Y Axis (Amplitude)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# 4. Save the graph to an image file
plt.savefig("cosine_wave_300Hz.png", dpi=300, bbox_inches="tight")

