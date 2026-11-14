import numpy as np
import matplotlib.pyplot as plt

# Population growth parameters
initial_population = 100.0
growth_rate = 0.2
carrying_capacity = 1000.0

# Time settings
h = 1.0
end_time = 20.0

# Logistic population growth equation
def population_growth(N):
    return (
        growth_rate * N
        * (1 - N / carrying_capacity)
    )

# Generate time values
time = np.arange(0, end_time + h, h)

# Create an array to store population values
population = np.zeros_like(time)
population[0] = initial_population

# Apply Euler's method
for i in range(len(time) - 1):
    population[i + 1] = (
        population[i]
        + h * population_growth(population[i])
    )

# Display population predictions
print(
    f"Population after 10 years: "
    f"{population[10]:.2f} antelopes"
)

print(
    f"Population after 20 years: "
    f"{population[-1]:.2f} antelopes"
)

# Plot population growth
plt.plot(
    time,
    population,
    marker="o",
    label="Euler population estimate"
)

plt.axhline(
    carrying_capacity,
    linestyle="--",
    label="Carrying capacity"
)

plt.xlabel("Time (years)")
plt.ylabel("Antelope population")
plt.title("Wildlife Population Growth Using Euler's Method")

plt.legend()
plt.grid(True)
plt.show()