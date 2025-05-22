from Matrix import Matrix


def psuedo_inverse_linear(data):
    y = []
    for i in data:
        y.append([i[1]])
    y_matrix = Matrix(y)
    X = []
    for i in data:
        X.append([i[0], 1])
    X_matrix = Matrix(X)
    X_transpose = X_matrix.transpose()
    X_transpose_X = X_transpose.matrix_multiply(X_matrix)
    X_transpose_X_inverse = X_transpose_X.RREF_inverse()
    X_transpose_X_inverse_XT = X_transpose_X_inverse.matrix_multiply(X_transpose)
    p = X_transpose_X_inverse_XT.matrix_multiply(y_matrix)
    return p


data = [(-2, 3), (1, 0), (3, -1), (4, 5)]
# y = Xp
p = psuedo_inverse_linear(data)

p.show()
import matplotlib.pyplot as plt
import numpy as np

# Data points
x_data = [i[0] for i in data]
y_data = [i[1] for i in data]

# Line parameters
m = p.matrix[0][0]
b = p.matrix[1][0]

# Generate values for x to plot the line
x_line = np.linspace(-10, 10 + 5, 5000)  # Generate x values for the line
y_line = m * x_line + b  # Calculate corresponding y values for the line

# Plot the data points
plt.scatter(x_data, y_data, color="red", label="Data points")

# Plot the line
plt.plot(x_line, y_line, color="blue", label=f"Line: y = {m}x + {b}")

# Labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Fit: y = mx + b")

# Show the legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
