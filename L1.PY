import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# Hourly water-level measurements in centimetres
hours = np.array(
    [8, 9, 10, 11, 12, 13, 14],
    dtype=float
)

water_level = np.array(
    [35, 42, 50, 55, 57, 56, 52],
    dtype=float
)

# Create interpolation functions
linear = interp1d(hours, water_level, kind="linear")
cubic = CubicSpline(hours, water_level)

# Generate estimates every 10 minutes
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)

linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)

# Estimate water level at 11:30 AM
target_time = 11.5

print(
    f"Linear water level at 11:30: "
    f"{float(linear(target_time)):.2f} cm"
)

print(
    f"Cubic water level at 11:30: "
    f"{float(cubic(target_time)):.2f} cm"
)

# Display original measurements
plt.scatter(
    hours,
    water_level,
    label="Hourly water measurements"
)

# Display estimated measurements
plt.plot(
    ten_minute_times,
    linear_estimates,
    label="Linear interpolation"
)

plt.plot(
    ten_minute_times,
    cubic_estimates,
    label="Cubic spline interpolation"
)

plt.xlabel("Time of day")
plt.ylabel("Water level (cm)")
plt.title("Water Tank Level Estimation")

plt.legend()
plt.grid(True)
plt.show()