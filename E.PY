
import numpy as np

# x = number of Type A servers
# y = number of Type B servers

# Type A uses 4 CPU units and 8 GB memory
# Type B uses 2 CPU units and 12 GB memory
# Total usage: 20 CPU units and 72 GB memory

# Step 1: Create the coefficient matrix
A = np.array([
    [4.0, 2.0],
    [8.0, 12.0]
])

# Step 2: Create the results matrix
b = np.array([20.0, 72.0])

# Step 3: Solve the linear equations
solution = np.linalg.solve(A, b)

# Step 4: Calculate the residual
residual = b - A @ solution

# Step 5: Display the results
print("SERVER RESOURCE ANALYSIS")
print("------------------------")

print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")

# Step 6: Verify the solution
print("\nVerification A @ solution:")
print(A @ solution)

print("\nResidual:")
print(residual)

print("\nResidual norm:")
print(np.linalg.norm(residual))
