
import numpy as np

# Step 1: Expected voltage readings
expected_voltage = np.array([
    1.0, 2.0, 3.0, 4.0, 5.0
])

# Step 2: Actual voltage readings from sensors
measured_voltage = np.array([
    1.0000001, 1.9999998, 3.0000002,
    4.0000001, 4.9999999
])

# Step 3: Calculate absolute errors
absolute_error = np.abs(
    expected_voltage - measured_voltage
)

# Step 4: Calculate relative errors
relative_error = (
    absolute_error / np.abs(expected_voltage)
)

# Step 5: Compare readings using tolerance
results = np.isclose(
    expected_voltage,
    measured_voltage,
    atol=0.000001,
    rtol=0
)

# Step 6: Display the results
print("SENSOR CALIBRATION REPORT")
print("-------------------------")

print("Expected voltage:")
print(expected_voltage)

print("\nMeasured voltage:")
print(measured_voltage)

print("\nAbsolute errors:")
print(absolute_error)

print("\nRelative errors:")
print(relative_error)

print("\nCalibration results:")

for i in range(len(results)):
    if results[i]:
        print(f"Sensor {i+1}: PASS")
    else:
        print(f"Sensor {i+1}: FAIL")
