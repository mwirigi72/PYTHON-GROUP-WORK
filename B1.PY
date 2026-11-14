
import numpy as np

# Step 1: Store network latency measurements
latency_ms = np.array([
    20, 35, 50, 75, 100,
    120, 150, 180, 200, 250
])

# Step 2: Convert milliseconds into seconds
latency_seconds = latency_ms / 1000

# Step 3: Calculate squared latency values
squared_latency = latency_seconds ** 2

# Step 4: Calculate average network latency
average_latency = np.mean(latency_ms)

# Step 5: Identify high latency measurements
high_latency = latency_ms[latency_ms > 100]

# Step 6: Display the results
print("NETWORK PERFORMANCE REPORT")
print("---------------------------")

print("Latency in milliseconds:")
print(latency_ms)

print("\nLatency in seconds:")
print(latency_seconds)

print("\nSquared latency values:")
print(squared_latency)

print(f"\nAverage latency: {average_latency:.2f} ms")

print("\nHigh latency measurements:")
print(high_latency)
