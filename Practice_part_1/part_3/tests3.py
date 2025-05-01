from excercises3 import five_start_times_three_minus_four, recursive_five_start_times_three_minus_four


tests = [
 {
 'function': five_start_times_three_minus_four,
 'input': 1,
 'output': [5]
 },
 {
 'function': recursive_five_start_times_three_minus_four,
 'input': 3 ,
 'output': five_start_times_three_minus_four(3)[-1],
 },
 {
 'function': five_start_times_three_minus_four,
 'input': 3,
 'output': [5,11, 29]
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
