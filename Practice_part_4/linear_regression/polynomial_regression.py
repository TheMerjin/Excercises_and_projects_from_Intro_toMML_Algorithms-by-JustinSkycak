from Matrix import Matrix


def psuedo_inverse_polynomial(data, degree=2):

    y = []
    for i in data:
        y.append([i[1]])
    y_matrix = Matrix(y)
    X = []
    for i in data:
        new_row = [i[0] ** n for n in range(degree, -1, -1)]
        X.append(new_row)
    X_matrix = Matrix(X)

    X_transpose = X_matrix.transpose()
    X_transpose_X = X_transpose.matrix_multiply(X_matrix)
    X_transpose_X_inverse = X_transpose_X.RREF_inverse()
    X_transpose_X_inverse_XT = X_transpose_X_inverse.matrix_multiply(X_transpose)
    p = X_transpose_X_inverse_XT.matrix_multiply(y_matrix)
    return p


data = [(-3, -4), (-2, 3), (3, -1), (1, 0), (4, 5)]
# y = Xp
p = psuedo_inverse_polynomial(data, degree=3)

p.show()
import matplotlib.pyplot as plt
import numpy as np

# Data points
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

# Line parameters
a = p.matrix[0][0]
b = p.matrix[1][0]
c = p.matrix[2][0]
d = p.matrix[3][0]

# Generate values for x to plot the line
x_line = np.linspace(-10, 10 + 5, 5000)  # Generate x values for the line
y_line = (
    a * x_line**3 + b * x_line**2 + c * x_line * 1 + d
)  # Calculate corresponding y values for the line

# Plot the data points
plt.scatter(x_data, y_data, color="red", label="Data points")

# Plot the line
plt.plot(x_line, y_line, color="blue", label=f"Line: y = {a}x^3 + {b}x^2 + {c}x + {d}")

# Labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Fit: y = mx + b")

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
