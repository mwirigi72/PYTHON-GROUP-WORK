
import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt

# Bridge design equations:
# Circle: x^2 + y^2 = 25
# Parabola: y = 0.5*x^2 - 2

def bridge_equations(z):

    x, y = z

    return [
        x**2 + y**2 - 25,
        y - (0.5*x**2 - 2)
    ]


# Initial guesses for the two intersections
initial_guesses = [
    [2.0, 3.0],
    [-2.0, 3.0]
]

intersections = []

# Solve the nonlinear equations
for guess in initial_guesses:

    solution = root(bridge_equations, guess)

    if solution.success:
        x, y = solution.x

        intersections.append([x, y])

        print("Initial guess:", guess)

        print(
            f"Intersection coordinates: "
            f"({x:.4f}, {y:.4f})"
        )

        print(
            "Residuals:",
            bridge_equations(solution.x)
        )

        print("Converged:", solution.success)
        print()


# Plot the circle and parabola
x_values = np.linspace(-5, 5, 400)

circle_upper = np.sqrt(25 - x_values**2)
parabola = 0.5*x_values**2 - 2

plt.plot(
    x_values,
    circle_upper,
    label="Upper circular boundary"
)

plt.plot(
    x_values,
    -circle_upper,
    label="Lower circular boundary"
)

plt.plot(
    x_values,
    parabola,
    label="Bridge support curve"
)

# Mark the calculated intersection points
for point in intersections:
    plt.scatter(
        point[0],
        point[1],
        label="Intersection"
    )

plt.xlabel("Horizontal distance (m)")
plt.ylabel("Vertical distance (m)")

plt.title("Bridge Structure Intersection Analysis")

plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
