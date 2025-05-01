"""
This file contains automated tests for functions such as check_if_symmetric and get_intersections.
"""

from hello_world import check_if_symmetric, get_intersections


tests = [
 {
 'function': check_if_symmetric,
 'input': 'racecar',
 'output': True
 },
 {
 'function': check_if_symmetric,
 'input': 'batman',
 'output': False
 },
 {
 'function': get_intersections,
 'input': ([1, 2, 3], [3, 4, 5]),
 'output': [3]
 }
 ]
NUM_SUCCESES = 0
NUM_FAILURES = 0
for test in tests:
    function = test['function']
    test_input = test['input']
    if isinstance(test_input, tuple):
        desired_output = test['output']
        actual_output = function(test_input[0], test_input[1])
    else:
        desired_output = test['output']
        actual_output = function(test_input)
    if actual_output == desired_output:
        NUM_SUCCESES += 1
    else:
        NUM_FAILURES += 1
        FUNCTION_NAME = function.__name__
        print('')
        print(f'{FUNCTION_NAME} failed on input {test_input}')
    print(f'\tActual output: {actual_output}')
    print(f'\tDesired output: {desired_output}')
    print(f'Testing complete: {NUM_SUCCESES} successes and {NUM_FAILURES} failures.')
