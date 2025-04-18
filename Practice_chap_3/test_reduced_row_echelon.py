from Matrix import Matrix
def matrix_equal(matrix1, matrix2):
    """Helper function to compare two matrices or integers."""
    if isinstance(matrix1, int) and isinstance(matrix2, int):
        return matrix1 == matrix2
    if matrix1.num_rows != matrix2.num_rows or matrix1.num_cols != matrix2.num_cols:
        return False
    for i in range(matrix1.num_rows):
        for j in range(matrix1.num_cols):
            if matrix1.matrix[i][j] != matrix2.matrix[i][j]:
                return False
    return True
def print_matrix(matrix):
    for row in matrix.matrix:
        print("  ", row)

test_cases = [
    {
        "matrix": Matrix([
            [0, 2, 1],
            [1, -2, -1],
            [2, -4, 0]
        ]),
        "expected_rref": Matrix([
            [1.0, -2.0, -1.0],
            [0.0, 1.0, 0.5],
            [0.0, 0.0, 0.0]
        ])
    },
    {
        "matrix": Matrix([
            [1, 2, 3],
            [2, 4, 6],
            [0, 0, 0]
        ]),
        "expected_rref": Matrix([
            [1.0, 2.0, 3.0],
            [0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0]
        ])
    },
    {
        "matrix": Matrix([
            [1, 2, -1, 3],
            [2, 4, -2, 6],
            [1, 1, 1, 4]
        ]),
        "expected_rref": Matrix([
            [1.0, 0.0, 0.0, 1.0],
            [0.0, 1.0, 0.0, 1.0],
            [0.0, 0.0, 1.0, 2.0]
        ])
    },
    {
        "matrix": Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 10]
        ]),
        "expected_rref": Matrix([
            [1.0, 0.0, -1.0],
            [0.0, 1.0, 2.0],
            [0.0, 0.0, 0.0]
        ])
    },
    {
        "matrix": Matrix([
            [2, 3, 1],
            [4, 7, 3],
            [-2, -3, 1]
        ]),
        "expected_rref": Matrix([
            [1.0, 0.0, 2.0],
            [0.0, 1.0, -1.0],
            [0.0, 0.0, 0.0]
        ])
    }
]
def test_reduce_row_echelon():
    num_successes = 0
    num_failures = 0

    for test in test_cases:
        function_name = "to_reduced_row_echelon_form"
        inputs = test["matrix"]
        
        expected_output = test["expected_rref"]

        try:
            matrix_instance = inputs
            method = getattr(matrix_instance, function_name)
            result = method() 
        except Exception as e:

            print(f"Error calling {function_name} with inputs {inputs}: {e}")
            num_failures += 1
            continue

        if matrix_equal(result, expected_output):
            num_successes += 1
        else:
            num_failures += 1
            print(f"\n{function_name} failed on input:")
            print_matrix(inputs)

            print("Expected output:")
            print_matrix(expected_output)

            print("Actual output:")
            print_matrix(result)

            print(f"\nTesting complete: {num_successes} successes and {num_failures} failures.")



test_reduce_row_echelon()
