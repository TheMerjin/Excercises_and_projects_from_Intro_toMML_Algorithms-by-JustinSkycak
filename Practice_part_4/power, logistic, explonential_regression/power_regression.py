from Matrix import Matrix
import matplotlib.pyplot as plt
import numpy as np


class Power_Regressor:
    def __init__(self, data):
        self.data = data

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


if __name__ == "__main__":
    data = [(1, 2), (2, 3), (3, 5)]
    regressor = Power_Regressor(data)
    regressor.logistic_fit(0.5, 10.5)
