class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists
        self.num_rows = len(list_of_lists)
        self.num_cols = len(list_of_lists[0])
        self.dims = (self.num_rows, self.num_cols)
        self.cols = [list(col) for col in zip(*self.matrix)]
        self.rows = [i for i in self.matrix]
        self.shape = (self.num_cols, self.num_rows)

    def __eq__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            return False
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if (
                    abs(self.matrix[i][j] - other.matrix[i][j]) > 1e-9
                ):  # Small tolerance
                    return False
        return True

    def show(self):
        for i in self.matrix:
            print(i)
        return self.matrix

    def to_array(self):
        return self.matrix

    def get_cols(self):
        return [list(col) for col in zip(*self.matrix)]

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

    def is_pivot(self, start_row, col):
        cols = [list(col) for col in zip(*self.matrix)]
        for row in range(start_row, len(cols[col])):
            if self.matrix[row][col] != 0:
                return row
        return None

    def normalize_row(self, pivot_index, row):
        self.matrix[row] = [p / self.matrix[row][pivot_index] for p in self.matrix[row]]
        return self

    def swap_rows(self, index1, index2):
        self.matrix[index1], self.matrix[index2] = (
            self.matrix[index2],
            self.matrix[index1],
        )
        return self

    def subtract_rows(self, pivot_row, other_row, factor: int):
        f = factor
        self.matrix[other_row] = [
            o - p * f for p, o in zip(self.matrix[pivot_row], self.matrix[other_row])
        ]
        return self

    def RREF(self):
        row_index = 0
        for col in range(self.num_cols):
            pivot_row = self.is_pivot(row_index, col)
            if pivot_row is None:
                continue
            if pivot_row != row_index:
                self.swap_rows(pivot_row, row_index)
            self.normalize_row(col, row_index)
            cols = self.get_cols()
            for i, row in enumerate(cols[col]):
                if (row) != 0 and i != row_index:
                    self.subtract_rows(row_index, i, row)
            row_index += 1

        return self

    def generate_indentity_matrix(self, dim):
        output = []
        for row in range(dim):
            output.append([])
            for col in range(dim):
                if row == col:
                    output[row].append(1)
                else:
                    output[row].append(0)

        return Matrix(output)

    def append(self, matrix: list):
        if len(matrix) != len(self.matrix):
            raise Exception(
                "Not same row length and therefore can't be added",
                f"{matrix.num_rows}, {self.matrix.num_rows}",
            )
        else:
            for i, row in enumerate(self.matrix):
                for r in matrix[i]:
                    self.matrix[i].append(r)
        return self

    def prepend(self, matrix: list):
        if len(matrix) != len(self.matrix):
            raise Exception(
                "Not same row length and therefore can't be added",
                f"{matrix.num_rows}, {self.matrix.num_rows}",
            )
        else:
            for i, row in enumerate(self.matrix):
                self.matrix[i] = matrix[i] + self.matrix[i]
        return self

    def RREF_inverse(self):
        self.shape = (self.num_cols, self.num_rows)
        if self.num_cols != self.num_rows:
            raise ValueError

        Im = self.generate_indentity_matrix(self.num_rows)
        self.append(Im.matrix)
        self.RREF()
        output = Matrix(self.get_cols()[3:]).transpose()
        return output

    def RREF_determinant(self):
        for row in self.matrix:
            # Check if the entire row is zeros
            if all(
                col == 0 for col in row
            ):  # Check if all elements in the row are zero
                return 0  # If any row is all zeros, the matrix is singular

        determinant = 1
        row_index = 0
        for col in range(self.num_cols):
            pivot_row = self.is_pivot(row_index, col)
            if pivot_row is None:
                continue
            if pivot_row != row_index:
                self.swap_rows(pivot_row, row_index)
                determinant *= -1
            pivot = self.matrix[row_index][col]

            determinant = determinant * pivot
            self.normalize_row(col, row_index)

            cols = self.get_cols()
            for i, row in enumerate(cols[col]):
                if (row) != 0 and i != row_index:
                    self.subtract_rows(row_index, i, row)
            row_index += 1

        return determinant


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
    L = Matrix([[0, 2, 3], [0, 1, 0], [4, 5, 6]])
    print("result")
    L.show()
    G = L.generate_indentity_matrix(10)
    print(L.RREF_determinant())
