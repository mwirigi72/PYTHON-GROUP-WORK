
import numpy as np

# Step 1: Define the square object coordinates
square = np.array([
    [0, 0],
    [2, 0],
    [2, 2],
    [0, 2]
])

# Step 2: Define the rotation angle
angle = np.deg2rad(45)

# Step 3: Create the rotation matrix
rotation = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

# Step 4: Create the scaling matrix
scale = np.array([
    [2, 0],
    [0, 2]
])

# Step 5: Combine the transformations
transformation = rotation @ scale

# Step 6: Calculate new coordinates
new_coordinates = square @ transformation.T

# Step 7: Display original and transformed coordinates
print("COMPUTER GRAPHICS TRANSFORMATION")
print("--------------------------------")

print("\nOriginal square coordinates:")
print(square)

print("\nNew square coordinates:")
print(np.round(new_coordinates, 3))

# Step 8: Calculate determinant
determinant = np.linalg.det(transformation)

print("\nTransformation determinant:")
print(round(determinant, 3))

# Step 9: Check whether the matrix is invertible
if not np.isclose(determinant, 0):
    print("The transformation matrix is invertible.")
else:
    print("The transformation matrix is not invertible.")
