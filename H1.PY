
import numpy as np

# Four computers in a company network
A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find dominant eigenvalue
index = np.argmax(eigenvalues.real)

dominant_value = eigenvalues.real[index]

# Get dominant eigenvector
dominant_vector = np.abs(
    eigenvectors[:, index].real
)

# Calculate importance scores
centrality = dominant_vector / dominant_vector.sum()

computers = ["Computer A", "Computer B",
             "Computer C", "Computer D"]

print("COMPANY COMPUTER NETWORK ANALYSIS")

for computer, score in zip(computers, centrality):
    print(f"{computer}: {score:.4f}")

# Identify the most influential computer
highest_score = np.max(centrality)

print("\nMost influential computers:")

for computer, score in zip(computers, centrality):
    if np.isclose(score, highest_score):
        print(computer)

# Verify the calculation
v = eigenvectors[:, index].real

error = np.linalg.norm(
    A @ v - dominant_value * v
)

print("\nVerification error:", error)
