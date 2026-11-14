
import numpy as np

# Adjacency matrix representing four connected computers
# Computer order: A, B, C, D

A = np.array([
    [0., 1., 1., 0.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [0., 1., 1., 0.]
])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Identify the dominant eigenvalue
index = np.argmax(np.real(eigenvalues))

dominant_value = np.real(eigenvalues[index])

# Extract the corresponding eigenvector
dominant_vector = np.abs(
    np.real(eigenvectors[:, index])
)

# Normalize the eigenvector
centrality = dominant_vector / dominant_vector.sum()

# Names of the computers
nodes = ["A", "B", "C", "D"]

# Display the dominant eigenvalue
print("Dominant eigenvalue:", dominant_value)

# Display importance scores
print("\nComputer network importance:")

for node, score in zip(nodes, centrality):
    print(f"Computer {node}: {score:.4f}")

# Verify the eigenvalue equation Av = lambda*v
v = np.real(eigenvectors[:, index])

verification = np.linalg.norm(
    A @ v - dominant_value * v
)

print("\nVerification error:", verification)

# Identify the most influential computer
most_important = nodes[np.argmax(centrality)]

print("Most influential computer:", most_important)
