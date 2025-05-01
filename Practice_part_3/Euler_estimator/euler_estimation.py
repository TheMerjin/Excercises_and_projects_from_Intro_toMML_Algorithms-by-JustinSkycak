import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("Qt5Agg")
class EulerEstimator():
    def __init__(self, derivative):
        self.derivative = derivative
    def eval_derivative(self, coord):
        x,y = coord
        return self.derivative(x)
    def estimate_points(self, initial_point, step_size, num_steps):
        points = []
        points.append(initial_point)
        current_point = initial_point
        current_x = initial_point[0]
        current_y = initial_point[1]
        for i in range(num_steps):
            next_x = current_x + step_size
            next_y = current_y + self.eval_derivative(current_point)*step_size
            next_point = (next_x, next_y)
            points.append(next_point)
            current_x = next_x
            current_y = next_y
            current_point = next_point
        return points
    

            


def derivative(t):
    return t-2
euler = EulerEstimator(derivative= derivative)
initial_point = (0,-2)
d1 = euler.eval_derivative(initial_point) 

step_size = 0.5
num_steps = 10
output = euler.estimate_points(initial_point, step_size,num_steps)
points = zip(*output)
x,y = points
plt.plot(x,y)
plt.show()