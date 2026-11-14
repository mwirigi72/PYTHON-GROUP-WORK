
import numpy as np

# x = Number of Test A
# y = Number of Test B

# Step 1: Create the coefficient matrix
# Chemical X: Test A uses 2, Test B uses 3
# Chemical Y: Test A uses 4, Test B uses 1

A = np.array([
    [2.0, 3.0],
    [4.0, 1.0]
])

# Step 2: Store the total chemical usage
b = np.array([18.0, 16.0])

# Step 3: Solve the simultaneous equations
solution = np.linalg.solve(A, b)

# Step 4: Calculate the residual
residual = b - A @ solution

# Step 5: Display the results
print("HOSPITAL LABORATORY REPORT")
print("--------------------------")

print(f"Number of Test A: {solution[0]:.0f}")
print(f"Number of Test B: {solution[1]:.0f}")

# Step 6: Verify the solution
print("\nVerification:")
print(A @ solution)

print("\nResidual:")
print(residual)

print("\nResidual norm:")
print(np.linalg.norm(residual))
