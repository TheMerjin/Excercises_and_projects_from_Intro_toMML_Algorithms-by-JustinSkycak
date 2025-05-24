from Matrix import Matrix
import matplotlib.pyplot as plt
import numpy as np


def psuedo_inverse_polynomial(data, degree=2):
    y = [[i[1]] for i in data]
    y_matrix = Matrix(y)

    X = [[x**n for n in range(degree, -1, -1)] for x, _ in data]
    X_matrix = Matrix(X)

    X_transpose = X_matrix.transpose()
    X_transpose_X = X_transpose.matrix_multiply(X_matrix)
    X_transpose_X_inverse = X_transpose_X.RREF_inverse()
    X_transpose_X_inverse_XT = X_transpose_X_inverse.matrix_multiply(X_transpose)
    p = X_transpose_X_inverse_XT.matrix_multiply(y_matrix)

    return p


def plot_polynomial_fit(data, p):
    x_data = [i[0] for i in data]
    y_data = [i[1] for i in data]

    degree = len(p.matrix) - 1

    # Generate x values for plotting
    x_line = np.linspace(min(x_data) - 1, max(x_data) + 1, 1000)

    # Generate y values using the fitted polynomial
    coeffs = [p.matrix[i][0] for i in range(degree + 1)]
    y_line = sum(coeff * x_line ** (degree - i) for i, coeff in enumerate(coeffs))

    # Plotting
    plt.scatter(x_data, y_data, color="red", label="Data points")
    plt.plot(x_line, y_line, color="blue", label=f"Degree {degree} Fit")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    plt.title(f"Polynomial Fit (degree {degree})")
    plt.legend()
    plt.grid(True)
    plt.show()


# === EXAMPLE USAGE ===
data = [
    (0, 0),
    (1, 10),
    (2, 20),
    (3, 50),
    (4, 35),
    (5, 100),
    (6, 110),
    (7, 190),
    (8, 150),
    (9, 260),
    (10, 270),
]

degree = 8
p = psuedo_inverse_polynomial(data, degree=degree)
p.show()

plot_polynomial_fit(data, p)
