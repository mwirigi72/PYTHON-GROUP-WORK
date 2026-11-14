import numpy as np
from scipy.integrate import simpson

# Time measurements in minutes
time_minutes = np.array(
    [0, 10, 20, 30, 40, 50, 60],
    dtype=float
)

# Water flow rate in litres per minute
flow_rate = np.array(
    [12, 14, 16, 18, 17, 15, 13],
    dtype=float
)

# Calculate total water volume using trapezoidal rule
volume_trapezoid = np.trapezoid(
    flow_rate,
    time_minutes
)

# Calculate total water volume using Simpson's rule
volume_simpson = simpson(
    flow_rate,
    x=time_minutes
)

# Calculate the difference
difference = abs(
    volume_simpson - volume_trapezoid
)

# Display the results
print(
    f"Water volume using trapezoidal rule: "
    f"{volume_trapezoid:.2f} litres"
)

print(
    f"Water volume using Simpson's rule: "
    f"{volume_simpson:.2f} litres"
)

print(
    f"Difference between estimates: "
    f"{difference:.2f} litres"
)