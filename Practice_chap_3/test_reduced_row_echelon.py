from Practice_chap_3.Matrix import Matrix
test_cases = [{"matrix" : [[1,2,-1], [2,4,-2], [1,1,1]], "expected_rref" : [[1,0,3], [0,1,-2], [0,0,0]]},
              {"matrix" : [[1,3,1], [1,1,-1], [3,11,5]], "expected_rref" : [[1,0,-2], [0,1,1], [0,0,0]]},
              {"matrix" : [[2,4,-2], [4,9,-3], [-2,-3,7]], "expected_rref" : [[1,0,0], [0,1,0], [0,0,1]]},
              {"matrix" : [[1,2,-1, 1, 3], [2,4,1, 3, 9], [-1,-2,5,0,-2], [3,6,0,6,12]], "expected_rref" : [[1,2,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]}
]
def run_tests():
    NUM_SUCCESES = 0
    NUM_FAILURES = 0
    for test in test_cases:
        matrix = Matrix(test["matrix"])
        expected = Matrix(test["expected_rref"])
        print("next test: \n"
              )
        matrix.RREF()
        if matrix == expected:
            NUM_SUCCESES +=1
            print("works!")
            for row in expected.matrix:
                print(row)
        else:
            NUM_FAILURES += 1
            print(f"excpected")
            for row in expected.matrix:
                print(row)
    print(f"num failures : {NUM_FAILURES} and num succeses: {NUM_SUCCESES}")
run_tests()
    
            
