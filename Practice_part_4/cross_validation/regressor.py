from Matrix import Matrix

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Regressor:
    def __init__(self, data):
        self.data = data

    def linear_fit(self):
        data = self.data
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

        # y = Xp

        p.show()

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
        return p

    def polynomial_fit(self, degree=2):
        data = self.data
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

        # y = Xp

        p.show()

        # Data points
        x_data = [i[0] for i in data]
        y_data = [i[1] for i in data]

        # Line parameters
        a = p.matrix[0][0]
        b = p.matrix[1][0]
        c = p.matrix[2][0]
        variables = [a, b, c]

        # Generate values for x to plot the line
        x_line = np.linspace(-10, 10 + 5, 5000)  # Generate x values for the line
        coeffs = [p.matrix[i][0] for i in range(len(p.matrix))]
        y_line = sum(
            c * x_line ** (degree - i) for i, c in enumerate(coeffs)
        )  # Calculate corresponding y values for the line

        # Plot the data points
        plt.scatter(x_data, y_data, color="red", label="Data points")

        # Plot the line
        plt.plot(
            x_line,
            y_line,
            color="blue",
            label=f"Line: y = {a}x^3 + {b}x^2 + {c}x + ",
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
        return p

    def mutiple_var_fit(self):
        data = self.data
        num_vars = len(data[0])
        y = []
        for i in data:
            y.append([i[-1]])
        y_matrix = Matrix(y)
        X = []
        for i in data:
            new_row = [i[n] for n in range(num_vars - 1)] + [1]
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
        c = p.matrix[2][0]
        variables = [a, b, c]
        # Generate values for x to plot the line
        x_vals = np.linspace(-10, 10, 1000)
        y_vals = np.linspace(-10, 10, 1000)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = a * X + b * Y + c
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

    def exp_fit(self):
        data = self.data
        y = []

        for i in data:
            y.append([np.log(i[1])])
        y_matrix = Matrix(y)
        X = []
        for i in data:
            new_row = [1, i[0]]
            X.append(new_row)
        X_matrix = Matrix(X)

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

        # Line parameters
        a = p.matrix[0][0]
        b = p.matrix[1][0]

        # Generate values for x to plot the line
        x_line = np.linspace(-10, 10 + 5, 5000)  # Generate x values for the line
        y_line = (
            np.e**a * x_line**np.e**b
        )  # Calculate corresponding y values for the line

        # Plot the data points
        plt.scatter(x_data, y_data, color="red", label="Data points")

        # Plot the line
        plt.plot(
            x_line,
            y_line,
            color="blue",
            label=f"Line: y = {a}*  {b}^x",
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

    def power_fit(self):
        data = self.data
        y = []

        for i in data:
            y.append([np.log(i[1])])
        y_matrix = Matrix(y)
        X = []
        for i in data:
            new_row = [1, np.log(i[0])]
            X.append(new_row)
        X_matrix = Matrix(X)

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

        # Line parameters
        a = p.matrix[0][0]
        b = p.matrix[1][0]

        # Generate values for x to plot the line
        x_line = np.linspace(-10, 10 + 5, 5000)  # Generate x values for the line
        y_line = np.e**a * x_line**b  # Calculate corresponding y values for the line

        # Plot the data points
        plt.scatter(x_data, y_data, color="red", label="Data points")

        # Plot the line
        plt.plot(
            x_line,
            y_line,
            color="blue",
            label=f"Line: y = {a}*  x^{b}",
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

    def logistic_fit(self, lower_bound: int, upper_bound: int):
        data = self.data
        y = []
        constant = lower_bound
        coefficient = upper_bound // 1

        for i in data:
            y.append(-np.log([(coefficient / (i[1] - constant)) - 1]))
        y_matrix = Matrix(y)
        X = []
        for i in data:
            new_row = [i[0], 1]
            X.append(new_row)
        X_matrix = Matrix(X)

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

        # Line parameters
        a = p.matrix[0][0]
        b = p.matrix[1][0]

        # Generate values for x to plot the line
        x_line = np.linspace(-10, 10 + 5, 5000)  # Generate x values for the line
        y_line = (
            coefficient / (1 + np.e ** (-1 * (a * x_line + b))) + constant
        )  # Calculate corresponding y values for the line

        # Plot the data points
        plt.scatter(x_data, y_data, color="red", label="Data points")

        # Plot the line
        plt.plot(
            x_line,
            y_line,
            color="blue",
            label=f"Line: y = {a}*  x^{b}",
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

    def run_method_by_name(self, method_name: str, *args, **kwargs):
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            if callable(method):
                return method(*args, **kwargs)
            else:
                raise TypeError(f"{method_name} is not callable.")

    def sample(self, method):
        methods = [
            ("linear_fit", {}),
            ("polynomial_fit", {"degree": 3}),
            ("exp_fit", {}),
            ("power_fit", {}),
            ("logistic_fit", {"lower_bound": 1, "upper_bound": 100}),
        ]


# Generate values for x to plot the line

if __name__ == "__main__":
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
    errors = []
    for point in data:
        data.remove(point)
        regressor = Regressor(data)
        p = regressor.polynomial_fit(degree=8)

        # Line parameters
        coeffs = [p.matrix[i][0] for i in range(len(p.matrix))]
        degree = len(p.matrix)
        x = point[0]
        y_true = point[1]

        y_pred = sum(coeffs[i] * (x**i) for i in range(len(coeffs)))
        errors.extend([(y_pred - y_true) ** 2])
        data.append(point)
    print("errors:")
    print(sum(errors))
