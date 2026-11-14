
import numpy as np
from scipy.optimize import root_scalar

# Diode parameters
Is = 1e-12       # Saturation current in amperes
nVt = 0.05       # Thermal voltage factor in volts
target_current = 0.001  # Required current in amperes


# Diode equation
def diode_function(V):
    return Is * (np.exp(V / nVt) - 1) - target_current


# Derivative of diode equation
def diode_derivative(V):
    return (Is / nVt) * np.exp(V / nVt)


# Newton-Raphson method
newton = root_scalar(
    diode_function,
    fprime=diode_derivative,
    x0=1.0,
    method="newton",
    xtol=1e-12
)


# Secant method
secant = root_scalar(
    diode_function,
    x0=0.9,
    x1=1.1,
    method="secant",
    xtol=1e-12
)


# Calculate voltage values
newton_voltage = newton.root
secant_voltage = secant.root

# Verify the current
calculated_current = Is * (
    np.exp(newton_voltage / nVt) - 1
)


# Display results
print("DIODE VOLTAGE ANALYSIS")
print("----------------------")

print(
    f"Newton-Raphson voltage: "
    f"{newton_voltage:.6f} V"
)

print(
    f"Secant method voltage:  "
    f"{secant_voltage:.6f} V"
)

print(
    f"Calculated current: "
    f"{calculated_current:.6f} A"
)

print(
    f"Required current: "
    f"{target_current:.6f} A"
)

print(
    f"Newton iterations: "
    f"{newton.iterations}"
)

print(
    f"Secant iterations: "
    f"{secant.iterations}"
)
