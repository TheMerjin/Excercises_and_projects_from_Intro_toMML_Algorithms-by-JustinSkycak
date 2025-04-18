"part 4 excercises gradient descent"
import math as m
def gradient_descent(function, derivative,alpha = 0.001):
    first_guesses = [0,1,1/2]
    potential_mins  = []
    for i in first_guesses:
        current_x_guess = i 
        for _ in range(470000):
            current_x_guess = current_x_guess - alpha * derivative(current_x_guess)
        potential_mins.append(current_x_guess)
    current_min = float('inf')
    print(potential_mins)
    for num in potential_mins:
        current_try = function(num)
        if current_try < current_min:
            current_min = current_try
    return current_min
def func1(x):
    return (m.sin(x)/(1+x**2))
def func1_derivative(x):
    numerator = (1 + x**2) * m.cos(x) - 2 * x * m.sin(x)
    denominator = (1 + x**2) ** 2
    return numerator / denominator

print(gradient_descent(function=func1, derivative=func1_derivative))

        


