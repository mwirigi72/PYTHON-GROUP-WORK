
import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Step 1: Define the electrical system coefficient matrix
A = np.array([
    [4.0, -1.0,  0.0],
    [-1.0, 4.0, -1.0],
    [0.0, -1.0,  3.0]
])

# Step 2: Store different voltage measurement sets
voltage_readings = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]

# Step 3: Perform LU decomposition once
lu, piv = lu_factor(A)

# Step 4: Process each voltage measurement
for i, voltage in enumerate(voltage_readings, start=1):

    # Calculate unknown current values
    current = lu_solve((lu, piv), voltage)

    # Verify the calculated values
    verification = A @ current

    # Calculate numerical error
    residual = voltage - verification

    # Display results
    print(f"ELECTRICAL MEASUREMENT {i}")
    print("-------------------------")

    print("Calculated current values:")
    print(np.round(current, 4))

    print("Verification:")
    print(np.round(verification, 4))

    print("Residual error:")
    print(np.round(residual, 8))

    print()
