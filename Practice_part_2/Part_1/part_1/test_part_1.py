#tests for part 1 
""" Tests for part 1 """

from Practice_chap_2.Part_1.part_1.part_1 import decode_message, decode_numbers, encode_string
tests = [{"function": encode_string, "input": ("a cat", 1,1), "output": [2,1,4,2,21]},
        {"function": decode_message, "input": [2,1,4,2,21], "output" : "a cat"},
        {"function": decode_numbers, "input" : ([2,1,4,2,21], 1,1), "output" : "a cat"}]

NUM_SUCCESES = 0
NUM_FAILURES = 0
for test in tests:
    function = test['function']
    test_input = test['input']
    if isinstance(test_input, tuple):
        desired_output = test['output']
        
        actual_output = function(test_input[0], test_input[1], test_input[2])
        print(test_input[0], test_input[1], test_input[2], "is tuple")
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