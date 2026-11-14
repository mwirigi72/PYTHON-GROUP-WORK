import numpy as np
import matplotlib.pyplot as plt

# Time measurements in minutes
time = np.array(
    [0, 1, 2, 3, 4, 5, 6],
    dtype=float
)

# Remaining water volume in litres
volume = np.array(
    [1000, 970, 935, 895, 850, 800, 745],
    dtype=float
)

# Create an array to store water flow rates
flow_rate = np.zeros_like(volume)

# Forward difference at the beginning
flow_rate[0] = -(
    volume[1] - volume[0]
) / (
    time[1] - time[0]
)

# Central difference for interior measurements
for i in range(1, len(time) - 1):
    flow_rate[i] = -(
        volume[i + 1] - volume[i - 1]
    ) / (
        time[i + 1] - time[i - 1]
    )

# Backward difference at the end
flow_rate[-1] = -(
    volume[-1] - volume[-2]
) / (
    time[-1] - time[-2]
)

# Display estimated water flow rates
for t, v, rate in zip(time, volume, flow_rate):
    print(
        f"Time={t:.0f} min, "
        f"Remaining water={v:.0f} L, "
        f"Flow rate={rate:.2f} L/min"
    )

# Plot water flow rate
plt.plot(time, flow_rate, marker="o")

plt.xlabel("Time (minutes)")
plt.ylabel("Water flow rate (litres/minute)")
plt.title("Estimated Water Flow Rate from Tank")

plt.grid(True)
plt.show()