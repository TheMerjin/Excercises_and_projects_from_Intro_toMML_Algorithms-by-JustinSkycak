from Practice_chap_3.Matrix import Matrix


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


def test_matrix_operations():
    tests = [
        {
            "function": "add",
            "input": (Matrix([[2, 3, 4], [6, 8, 7]]), Matrix([[1, 1, 1], [1, 1, 1]])),
            "output": Matrix([[3, 4, 5], [7, 9, 8]]),
        },
        {
            "function": "is_pivot",
            "input": (Matrix([[2, 3, 4], [6, 8, 7]]), 1),
            "output": 0,
        },
        {
            "function": "minus",
            "input": (Matrix([[2, 3, 4], [6, 8, 7]]), Matrix([[1, 1, 1], [1, 1, 1]])),
            "output": Matrix([[1, 2, 3], [5, 7, 6]]),
        },
        {
            "function": "scalar_multiply",
            "input": (Matrix([[2, 3, 4], [6, 8, 7]]), 2),
            "output": Matrix([[4, 6, 8], [12, 16, 14]]),
        },
        {
            "function": "matrix_multiply",
            "input": (Matrix([[2, 3], [6, 8]]), Matrix([[1, 2], [3, 4]])),
            "output": Matrix([[11, 16], [30, 44]]),
        },
        {
            "function": "transpose",
            "input": (Matrix([[2, 3], [6, 8], [4, 5]]),),
            "output": Matrix([[2, 6, 4], [3, 8, 5]]),
        },
        {
            "function": "swap_rows",
            "input": (Matrix([[1, 2], [3, 4], [5, 6]]), 2, 0),
            "output": Matrix([[5, 6], [3, 4], [1, 2]]),
        },
        {
            "function": "swap_rows",
            "input": (Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 10]]), 2, 0),
            "output": Matrix([[5, 6, 10], [3, 4, 5], [1, 2, 3]]),
        },
        {
            "function": "swap_rows",
            "input": (Matrix([[1], [3], [5]]), 0, 2),
            "output": Matrix([[5], [3], [1]]),
        },
        {},
    ]

    num_successes = 0
    num_failures = 0

    for test in tests:
        function_name = test["function"]
        inputs = test["input"]

        expected_output = test["output"]

        try:
            matrix_instance = inputs[0]
            method = getattr(matrix_instance, function_name)
            result = method(*inputs[1:]) if len(inputs) > 1 else method()
        except Exception as e:

            print(f"Error calling {function_name} with inputs {inputs}: {e}")
            num_failures += 1
            continue

        if matrix_equal(result, expected_output):
            num_successes += 1
        else:
            num_failures += 1
            input_strs = [
                inp.show() if isinstance(inp, Matrix) else str(inp) for inp in inputs
            ]
            print(f"{function_name} failed on input {tuple(input_strs)}")
            if isinstance(expected_output, int):
                print(f"Expected output: {expected_output}")
                print(f"Actual output: {result}")
            else:
                print(f"Expected output: {expected_output.matrix}")
                print(f"Actual output: {result.matrix}")

    print(f"\nTesting complete: {num_successes} successes and {num_failures} failures.")


test_matrix_operations()