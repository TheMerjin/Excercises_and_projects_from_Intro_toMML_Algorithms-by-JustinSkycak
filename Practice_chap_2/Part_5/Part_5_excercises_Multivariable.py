def multi_var_gradient_descent( function, derivative,iterations = 10000, alpha = 0.01, num_args = 2):
    first_guesses_if_three_vars = [[0,0,0],[1,1,1], [2,2,2]]
    first_guesses_if_two_vars = [[0,0],[1,1], [2,2]]
    potential_mins  = []
    first_guesses = first_guesses_if_three_vars if num_args == 3 else first_guesses_if_two_vars
    for i in first_guesses:
        variables = i
        for _ in range(4700000):
            variables = [a - (alpha* b) for a,b in zip(variables, derivative(variables))]
        potential_mins.append(variables)
    current_min = float('inf')
    for num in potential_mins:
        current_try = function(num)
        if current_try < current_min:
            current_min = current_try
    return current_min

    
def func1(vars):
    x,y,z = vars
    return (x-1)**2 + 3*(y-2)**2 + 4*(z+1)**2
def derivative(vars):
    x,y,z = vars
    d_x = 2*(x-1)
    d_y = 6*(y-2)
    d_z = 8*(z+1)
    return [d_x, d_y, d_z]
print(multi_var_gradient_descent(func1, derivative=derivative, num_args=3))