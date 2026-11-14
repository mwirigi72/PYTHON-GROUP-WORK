
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

# Sensor calibration model
# Find the temperature where sensor output equals 50

def sensor_function(T):
    return T + 0.02 * T**2 - 50


# Bisection method
bisection_result = root_scalar(
    sensor_function,
    bracket=[20, 40],
    method="bisect",
    xtol=1e-10
)


# Fixed-point method
# T = 50 / (1 + 0.02*T)

def fixed_point(T):
    return 50 / (1 + 0.02 * T)


temperature = 25.0
tolerance = 1e-10
history = [temperature]

for iteration in range(100):

    new_temperature = fixed_point(temperature)

    history.append(new_temperature)

    if abs(new_temperature - temperature) < tolerance:
        temperature = new_temperature
        break

    temperature = new_temperature


# Display results
print("INDUSTRIAL SENSOR CALIBRATION")
print("--------------------------------")

print(
    f"Bisection temperature: "
    f"{bisection_result.root:.6f} C"
)

print(
    f"Fixed-point temperature: "
    f"{temperature:.6f} C"
)

print("Fixed-point iterations:", len(history) - 1)

print(
    "Sensor output:",
    f"{temperature + 0.02 * temperature**2:.6f}"
)


# Plot the calibration function
temperatures = np.linspace(20, 40, 300)

plt.plot(
    temperatures,
    sensor_function(temperatures),
    label="Sensor calibration function"
)

plt.axhline(0, linewidth=0.8)
plt.axvline(
    bisection_result.root,
    linestyle="--",
    label="Calculated temperature"
)

plt.xlabel("Actual temperature (C)")
plt.ylabel("Sensor output minus 50")
plt.title("Industrial Temperature Sensor Calibration")

plt.legend()
plt.grid(True)
plt.show()
