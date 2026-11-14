
import numpy as np
import matplotlib.pyplot as plt

# Five temperature monitoring points
A = np.array([
    [ 2., -1.,  0.,  0.,  0.],
    [-1.,  2., -1.,  0.,  0.],
    [ 0., -1.,  2., -1.,  0.],
    [ 0.,  0., -1.,  2., -1.],
    [ 0.,  0.,  0., -1.,  2.]
])

# Simplified greenhouse boundary conditions
b = np.array([100., 0., 0., 0., 20.])


# Jacobi method
def jacobi(A, b, tolerance=1e-8, max_iterations=500):

    D = np.diag(A)
    R = A - np.diagflat(D)

    temperatures = np.zeros_like(b)

    for iteration in range(max_iterations):

        new_temperatures = (b - R @ temperatures) / D

        error = np.linalg.norm(
            new_temperatures - temperatures,
            ord=np.inf
        )

        temperatures = new_temperatures

        if error < tolerance:
            return temperatures, iteration + 1

    return temperatures, max_iterations


# Gauss-Seidel method
def gauss_seidel(A, b, tolerance=1e-8, max_iterations=500):

    temperatures = np.zeros_like(b)

    for iteration in range(max_iterations):

        old_temperatures = temperatures.copy()

        for i in range(len(b)):

            temperatures[i] = (
                b[i]
                - A[i, :i] @ temperatures[:i]
                - A[i, i+1:] @ old_temperatures[i+1:]
            ) / A[i, i]

        error = np.linalg.norm(
            temperatures - old_temperatures,
            ord=np.inf
        )

        if error < tolerance:
            return temperatures, iteration + 1

    return temperatures, max_iterations


# Calculate temperatures
jacobi_result, jacobi_iterations = jacobi(A, b)

gs_result, gs_iterations = gauss_seidel(A, b)

# Display results
print("GREENHOUSE TEMPERATURE MONITORING")
print("----------------------------------")

for i in range(5):
    print(f"Monitoring point {i + 1}: {gs_result[i]:.2f} C")

print("\nJacobi result:", jacobi_result)
print("Gauss-Seidel result:", gs_result)

print("\nJacobi iterations:", jacobi_iterations)
print("Gauss-Seidel iterations:", gs_iterations)

# Compare with direct solution
direct_result = np.linalg.solve(A, b)

print("\nDirect solution:", direct_result)

# Display temperature graph
points = [1, 2, 3, 4, 5]

plt.plot(points, gs_result, marker="o", label="Gauss-Seidel")
plt.plot(points, jacobi_result, marker="s", label="Jacobi")

plt.xlabel("Temperature monitoring point")
plt.ylabel("Estimated temperature (C)")
plt.title("Greenhouse Temperature Distribution")

plt.legend()
plt.grid(True)
plt.show()
