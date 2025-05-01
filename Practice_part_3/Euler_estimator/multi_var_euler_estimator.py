class EulerEstimator():
    def __init__(self, derivatives : dict):
        self.derivatives = derivatives
    def eval_derivative(self, coord):
        t, state = coord
        output = {k : v(t,state) for k,v in self.derivatives.items()}
        return output
    def estimate_points(self, initial_point, step_size, num_steps):
        t, state = initial_point
        points = []
        current_t = t
        current_state = state
        next_state = None
        points.append((current_t, current_state))
        for i in range(num_steps):
            next_t = current_t + step_size
            next_state = { k : v + self.derivatives[k](current_t, current_state) * step_size for k,v in current_state.items()}
            state_cache = (next_t, next_state)
            points.append(state_cache)
            next_t = current_t + step_size
            current_t = next_t
            current_state = next_state
        return points
        

initial_state = {'a':-0.45, 'b':-0.05, 'c': 0}
initial_point = (-0.4, initial_state) # points take
 
def da_dt(t, state):
    return state['a'] + 1
def db_dt(t, state):
    return state['a'] + state['b']
def dc_dt(t, state):
    return 2 * state['b'] + 3 * t
derivatives = {
 'a': da_dt,
 'b': db_dt,
 'c': dc_dt
 }
euler = EulerEstimator(derivatives)
d1 = euler.eval_derivative(initial_point)
step_size = 2
num_steps = 3
d2 = euler.estimate_points(initial_point, step_size,
 num_steps)
for x in d2:
    print(x, "\n")