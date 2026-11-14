import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Number of operating machines
machines = np.array(
    [2, 4, 6, 8, 10, 12, 14],
    dtype=float
)

# Electricity consumption per hour in kWh
electricity = np.array(
    [18, 27, 39, 54, 72, 93, 117],
    dtype=float
)

# Define a quadratic model
def model(x, a, b, c):
    return a * x**2 + b * x + c

# Fit the model to the recorded measurements
parameters, covariance = curve_fit(
    model,
    machines,
    electricity
)

a, b, c = parameters

# Calculate predicted electricity consumption
predicted = model(machines, a, b, c)

# Calculate Root Mean Square Error
rmse = np.sqrt(
    np.mean((electricity - predicted)**2)
)

# Predict electricity consumption for 16 machines
prediction = model(16, a, b, c)

print(
    f"Fitted model: y = {a:.4f}x^2 "
    f"+ {b:.2f}x + {c:.2f}"
)

print(f"RMSE: {rmse:.2f} kWh")

print(
    f"Predicted consumption for 16 machines: "
    f"{prediction:.2f} kWh"
)

# Generate points for the fitted curve
x_plot = np.linspace(2, 16, 300)

# Plot actual measurements
plt.scatter(
    machines,
    electricity,
    label="Actual measurements"
)

# Plot fitted curve
plt.plot(
    x_plot,
    model(x_plot, a, b, c),
    label="Fitted curve"
)

plt.xlabel("Number of operating machines")
plt.ylabel("Electricity consumption (kWh)")
plt.title("Factory electricity consumption")

plt.legend()
plt.grid(True)
plt.show()