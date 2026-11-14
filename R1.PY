
from scipy.optimize import minimize

# x = acres used for maize
# y = acres used for beans

# Profit per acre
maize_profit = 20000
beans_profit = 15000

# Objective function: minimize negative profit
def negative_profit(z):
    x, y = z
    return -(maize_profit*x + beans_profit*y)

# Land constraint: maximum 10 acres
def land_constraint(z):
    x, y = z
    return 10 - x - y

# Water constraint: maximum 30 units
def water_constraint(z):
    x, y = z
    return 30 - 4*x - 2*y

constraints = [
    {
        "type": "ineq",
        "fun": land_constraint
    },
    {
        "type": "ineq",
        "fun": water_constraint
    }
]

# Acres cannot be negative
bounds = [
    (0, None),
    (0, None)
]

# Find the best combination
solution = minimize(
    negative_profit,
    x0=[5, 5],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

# Get the optimized values
x, y = solution.x

# Calculate maximum profit
maximum_profit = maize_profit*x + beans_profit*y

# Calculate resource usage
total_land = x + y
total_water = 4*x + 2*y

print("Optimization success:", solution.success)
print(f"Maize acres: {x:.2f}")
print(f"Beans acres: {y:.2f}")
print(f"Total land used: {total_land:.2f} acres")
print(f"Total water used: {total_water:.2f} units")
print(f"Maximum expected profit: KSh {maximum_profit:.2f}")
