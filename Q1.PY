import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Initial chemical concentration
C0 = 100.0       # Concentration in mg/L

# Decay constant
k = 0.15         # Per hour

# Define the differential equation
def treatment_model(t, C):
    return [-k * C[0]]

# Generate time values from 0 to 8 hours
t_eval = np.linspace(0, 8, 100)

# Solve the differential equation
solution = solve_ivp(
    treatment_model,
    (0, 8),
    [C0],
    t_eval=t_eval,
    rtol=1e-9,
    atol=1e-11
)

# Calculate the exact mathematical solution
exact = C0 * np.exp(-k * solution.t)

# Display the results
print("Solver success:", solution.success)

print(
    f"Chemical concentration after 8 hours: "
    f"{solution.y[0, -1]:.2f} mg/L"
)

print(
    f"Exact concentration after 8 hours: "
    f"{exact[-1]:.2f} mg/L"
)

print(
    f"Maximum numerical error: "
    f"{np.max(np.abs(solution.y[0] - exact)):.3e} mg/L"
)

# Plot the numerical and exact solutions
plt.plot(
    solution.t,
    solution.y[0],
    label="SciPy numerical solution"
)

plt.plot(
    solution.t,
    exact,
    linestyle="--",
    label="Exact solution"
)

plt.xlabel("Time (hours)")
plt.ylabel("Chemical concentration (mg/L)")
plt.title("Chemical concentration during wastewater treatment")

plt.legend()
plt.grid(True)
plt.show()