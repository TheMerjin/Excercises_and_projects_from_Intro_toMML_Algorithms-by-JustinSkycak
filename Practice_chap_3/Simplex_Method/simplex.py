from Matrix import Matrix

variables = ["x1", "x2", "x3", "x4", "x5", "x6"]
array = [
    [1, 2, 1, 0, 0, 0, 0],  # Objective function (maximize)
    [2, 1, 1, 1, 0, 0, 14],  # Constraint 1
    [4, 2, 3, 0, 1, 0, 28],  # Constraint 2
    [2, 5, 5, 0, 0, 1, 30],  # Constraint 3
]


def simplex(
    array,
):
    maximizing_row = 0

    constraint_rows = [i for i in range(1, len(array))]
    matrix_array = Matrix(array)
    max_val = -float("inf")
    found = False
    while not found:
        if all(x <= 0 for x in matrix_array.matrix[maximizing_row][:-1]):
            found = True
            break
        largest_grad = -float("inf")
        largest_col = None
        for i, grad in enumerate(matrix_array.matrix[maximizing_row]):
            if grad > largest_grad:
                largest_grad = grad
                largest_col = i
        least_ratio = float("inf")
        least_val = None
        constant_col = matrix_array.get_cols()[-1]
        least_row = None
        for i, val in enumerate(matrix_array.cols[largest_col][1:], start=1):
            ratio = constant_col[i] / val
            if ratio < least_ratio:
                least_ratio = ratio
                least_val = val
                least_row = i
        matrix_array.normalize_row(largest_col, least_row)
        cols = matrix_array.get_cols()
        for i, row in enumerate(cols[largest_col]):
            if (row) != 0 and i != least_row:
                matrix_array.subtract_rows(least_row, i, row)
        max_val = -1 * matrix_array.matrix[maximizing_row][-1]

    return max_val


print(simplex(array))
