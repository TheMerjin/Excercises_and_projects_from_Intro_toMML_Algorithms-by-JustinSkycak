class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists
        self.num_rows = len(list_of_lists)
        self.num_cols = len(list_of_lists[0])
        self.dims = (self.num_rows, self.num_cols)
        self.cols = [list(col) for col in zip(*self.matrix)]
        self.rows = [i for i in self.matrix]

    def show(self):
        for i in self.matrix:
            print(i)
        return self.matrix

    def transpose(self):
        transposed_matrix = [
            [0 for _ in range(self.num_rows)] for _ in range(self.num_cols)
        ]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                transposed_matrix[j][i] = self.matrix[i][j]
        return Matrix(transposed_matrix)

    def add(self, other):
        if not self.check_same_dims(other):
            print(
                "incorrect_dimensions:",
                f" self.dims : {self.dims}",
                f"other.dims {other.dims}",
            )
            raise Exception(
                "incorrect_dimensions:",
                f" self.dims : {self.dims}",
                f"other.dims {other.dims}",
            )
        else:
            result = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    result[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return Matrix(result)

    def check_same_dims(self, other):
        if self.num_rows == other.num_rows and self.num_cols == other.num_cols:
            return True
        return False

    def scalar_multiply(self, num):
        result = [[0 for _ in range(self.num_cols)] for _ in range(self.num_rows)]
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                result[i][j] = self.matrix[i][j] * num
        return Matrix(result)

    def minus(self, other):
        if not self.check_same_dims(other):
            print(
                "incorrect_dimensions:",
                f" self.dims : {self.dims}",
                f"other.dims {other.dims}",
            )
            raise Exception(
                "incorrect_dimensions:",
                f" self.dims : {self.dims}",
                f"other.dims {other.dims}",
            )
        neg_other = other.scalar_multiply(-1)
        return self.add(neg_other)

    def matrix_multiply(self, other):
        if self.num_cols != other.num_rows or self.num_rows != other.num_cols:
            raise Exception(
                "The dims dont math for multiplication",
                "self.dims",
                self.dims,
                "other.dims",
                other.dims,
            )
        else:
            result = [[0 for n in range(other.num_cols)] for i in range(self.num_rows)]
            for i in range(len(result)):
                for j in range(len(result[0])):
                    result[i][j] = self.dot_product(
                        self.matrix[i], [row[j] for row in other.matrix]
                    )
        return Matrix(result)

    def dot_product(self, arr1, arr2):
        if len(arr1) != len(arr2):
            raise Exception(f"len arr1{len(arr1)} != len(arr2): {len(arr2)}")
        dot_product = 0
        for i in range(len(arr1)):
            dot_product += arr1[i] * arr2[i]
        return dot_product

    def recursive_determinant(self):
        if self.num_rows != self.num_cols:
            raise Exception(
                "determinants may not be preformed on a non-square matrix",
                f"the dims {self.dims}",
            )
        if self.num_rows == 1:
            return self.matrix[0][0]
        if self.num_rows == 2:
            return (
                self.matrix[0][0] * self.matrix[1][1]
                - self.matrix[0][1] * self.matrix[1][0]
            )
        det = 0
        for col in range(self.num_cols):
            minor = self.get_minor(0, col)
            cofactor = (
                ((-1) ** col) * self.matrix[0][col] * minor.recursive_determinant()
            )
            det += cofactor
        return det

    def get_minor(self, row, col):
        minor = [
            [self.matrix[i][j] for j in range(self.num_cols) if j != col]
            for i in range(self.num_rows)
            if i != row
        ]
        return Matrix(minor)

    def to_reduced_row_echelon_form(self):
        row_index = 0
        matrix = [row[:] for row in self.matrix]
        for col in range(self.num_cols):
            # Find the pivot row: first row with a non-zero in this column
            pivot_row = None
            for r in range(row_index, self.num_rows):
                if matrix[r][col] != 0:
                    pivot_row = r
                    break

            if pivot_row is None:
                continue  # No pivot in this column

            if pivot_row != row_index:
                # Swap pivot row with current row
                matrix[row_index], matrix[pivot_row] = (
                    matrix[pivot_row],
                    matrix[row_index],
                )

            # Normalize the pivot row
            pivot = matrix[row_index][col]
            matrix[row_index] = [val / pivot for val in matrix[row_index]]

            # Eliminate entries **below and above** pivot
            for r in range(self.num_rows):
                if r != row_index and matrix[r][col] != 0:
                    factor = matrix[r][col]
                    matrix[r] = [
                        a - factor * b for a, b in zip(matrix[r], matrix[row_index])
                    ]

            row_index += 1  # Move to the next row

        return Matrix(matrix)


if __name__ == "__main__":

    A = Matrix([[2, 3, 4], [6, 8, 7]])
    print("A:")
    print(A.cols)
    print("swap rows")
    print("/n")
    A.show()
    At = A.transpose()
    print("At:")
    At.show()

    print("test: row-echolon/n")
    L = Matrix([[0, -3, 9], [1 / 2, 3, 0], [10, 5, 1]])

