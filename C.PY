
import numpy as np

# Step 1: Floating-point comparison
calculated = 0.1 + 0.2
expected = 0.3

print("FLOATING-POINT COMPARISON")
print("------------------------")

print("0.1 + 0.2 =", calculated)
print("Exact comparison:", calculated == expected)
print("Tolerance-based comparison:",
      np.isclose(calculated, expected))

# Step 2: Calculate absolute and relative errors
true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nERROR CALCULATION")
print("-----------------")

print(f"True value: {true_value:.8f}")
print(f"Approximate value: {approx_value:.8f}")
print(f"Absolute error: {absolute_error:.8f}")
print(f"Relative error: {relative_error:.8%}")

# Step 3: Compare unstable and stable formulas
print("\nNUMERICAL STABILITY TEST")
print("------------------------")

for x in [1e-4, 1e-8, 1e-12]:

    # Direct mathematical formula
    direct = (np.sqrt(1 + x) - 1) / x

    # Stable mathematical formula
    stable = 1 / (np.sqrt(1 + x) + 1)

    print(
        f"x={x:.0e}: "
        f"direct={direct:.12f}, "
        f"stable={stable:.12f}"
    )
