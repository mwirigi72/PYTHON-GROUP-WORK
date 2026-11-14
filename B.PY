
import numpy as np
import timeit

# Step 1: Generate one million network latency readings
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

# Step 2: Process data using a normal Python loop
def loop_version():
    squared = []

    for value in latency_ms:
        seconds = value / 1000.0
        squared.append(seconds ** 2)

    return squared

# Step 3: Process data using NumPy vectorization
def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2

# Step 4: Measure execution time
loop_time = timeit.timeit(loop_version, number=1)

vector_time = timeit.timeit(
    vectorized_version, number=3
) / 3

# Step 5: Calculate results
result = vectorized_version()

# Step 6: Display results
print("NETWORK LATENCY ANALYSIS")
print("------------------------")

print("First five squared latency values:")
print(result[:5])

print(f"Loop time: {loop_time:.4f} seconds")
print(f"Vectorized time: {vector_time:.4f} seconds")

print(
    f"Approximate speed-up: "
    f"{loop_time / vector_time:.1f}x"
)
