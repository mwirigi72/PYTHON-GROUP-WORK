
import numpy as np
import matplotlib.pyplot as plt

# Create random number generator
rng = np.random.default_rng(42)

# Water supply information
available_supply = 10000.0
mean_demand = 8000.0
std_demand = 1500.0

# Number of simulations
N = 100_000

# Generate random daily water demand
water_demand = rng.normal(mean_demand, std_demand, N)

# Identify days when demand exceeds supply
shortage = water_demand > available_supply

# Calculate probability of water shortage
shortage_probability = shortage.mean()

# Display results
print(f"Estimated water shortage probability: {shortage_probability:.4%}")
print(f"Number of shortage cases: {shortage.sum()} out of {N}")

# Calculate running shortage probability
running_probability = np.cumsum(shortage) / np.arange(1, N + 1)

# Select points for the graph
indices = np.unique(
    np.logspace(1, np.log10(N), 200).astype(int)
) - 1

# Plot convergence graph
plt.semilogx(
    indices + 1,
    running_probability[indices]
)

plt.xlabel("Number of simulations")
plt.ylabel("Estimated water shortage probability")
plt.title("Monte Carlo estimate of water shortage risk")
plt.grid(True)
plt.show()
