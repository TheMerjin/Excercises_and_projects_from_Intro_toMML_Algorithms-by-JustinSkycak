from Matrix import Matrix

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Non_Linear_regressor:
    def __init__(self, data):
        self.data = data

    def non_linear_fit(self, func1: "function", func2: "function"):
        functions = [func1, func2]
        data = self.data
        y = []
        for i in data:
            y.append([i[-1]])
        y_matrix = Matrix(y)
        X = []
        for i in data:
            new_row = [f(i[0]) for f in functions]
            X.append(new_row)
        X_matrix = Matrix(X)
        X_matrix.show()
        X_transpose = X_matrix.transpose()
        X_transpose_X = X_transpose.matrix_multiply(X_matrix)
        X_transpose_X_inverse = X_transpose_X.RREF_inverse()
        X_transpose_X_inverse_XT = X_transpose_X_inverse.matrix_multiply(X_transpose)
        p = X_transpose_X_inverse_XT.matrix_multiply(y_matrix)

        # y = Xp

        p.show()

        # Data points
        x_data = [i[0] for i in data]
        y_data = [i[1] for i in data]
        z_data = [i[-1] for i in data]

        # Line parameters
        a = p.matrix[0][0]
        b = p.matrix[1][0]
        variables = [a, b]

        # Generate values for x to plot the line
        x_line = np.linspace(-3, 6, 5000)  # Generate x values for the line
        y_line = a * func1(x_line) + b * func2(
            x_line
        )  # Calculate corresponding y values for the line

        # Plot the data points
        plt.scatter(x_data, y_data, color="red", label="Data points")

        # Plot the line
        plt.plot(
            x_line,
            y_line,
            color="blue",
            label=f"Line: y = {a} sin(x) + {b} 2^x ",
        )

        # Labels and title
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Linear Fit: y = mx + b")

        # Show the legend
        plt.legend()

        # Show the plot
        plt.grid(True)
        plt.show()

    def multi_var_non_linear_fit(self, func1: "function", func2: "function"):
        functions = [func1, func2]
        data = self.data
        num_vars = len(data[0])
        y = []
        for i in data:
            y.append([i[-1]])
        y_matrix = Matrix(y)
        X = []
        for i in data:
            new_row = [f(i[0], i[1]) for f in functions]
            X.append(new_row)
        X_matrix = Matrix(X)
        X_matrix.show()
        X_transpose = X_matrix.transpose()
        X_transpose_X = X_transpose.matrix_multiply(X_matrix)
        X_transpose_X_inverse = X_transpose_X.RREF_inverse()
        X_transpose_X_inverse_XT = X_transpose_X_inverse.matrix_multiply(X_transpose)
        p = X_transpose_X_inverse_XT.matrix_multiply(y_matrix)

        # y = Xp

        p.show()

        # Data points
        x_data = [i[0] for i in data]
        y_data = [i[1] for i in data]
        z_data = [i[-1] for i in data]

        # Line parameters
        a = p.matrix[0][0]
        b = p.matrix[1][0]
        variables = [a, b]
        # Generate values for x to plot the line
        x_vals = np.linspace(-10, 10, 1000)
        y_vals = np.linspace(-10, 10, 1000)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = a * func1(X, Y) + b * func2(X, Y)
        # Sample data

        # Create 3D figure
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")

        # Plot the points
        ax.scatter(x_data, y_data, z_data)
        ax.plot_surface(X, Y, Z, alpha=0.5, color="blue")
        # Labels
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        plt.show()
        return variables


# Generate values for x to plot the line
def func1(x, y):
    return x * y**2


def func2(x, y):
    return 2 ** (x + y)


if __name__ == "__main__":
    data = [(-2, 3, -3), (1, 0, -4), (3, -1, 2), (4, 5, 3)]
    regressor = Non_Linear_regressor(data)
    regressor.multi_var_non_linear_fit(func1, func2)
