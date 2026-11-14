
import numpy as np

# Step 1: Create four corners of a square
# Each row represents a coordinate [x, y]
points = np.array([
    [0.0, 0.0],
    [1.0, 0.0],
    [1.0, 1.0],
    [0.0, 1.0]
])

# Step 2: Convert 45 degrees into radians
angle = np.deg2rad(45)

# Step 3: Create a rotation matrix
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

# Step 4: Create a scaling matrix
scale = np.array([
    [2.0, 0.0],
    [0.0, 1.5]
])

# Step 5: Combine rotation and scaling matrices
transformation = rotation @ scale

# Step 6: Transform the original coordinates
transformed_points = points @ transformation.T

# Step 7: Display the results
print("Original points:")
print(points)

print("\nTransformation matrix:")
print(transformation)

print("\nTransformed points:")
print(transformed_points)

# Step 8: Calculate the determinant
print("\nDeterminant:")
print(np.linalg.det(transformation))
