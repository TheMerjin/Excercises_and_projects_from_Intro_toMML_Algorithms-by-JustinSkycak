from multi_var_euler_estimator import EulerEstimator
import matplotlib
from matplotlib import pyplot as plt
def exp_builtin(x, terms=20):
    result = 1.0
    fact = 1
    power = 1
    
    for n in range(1, terms):
        fact *= n  # factorial
        power *= x  # x^n
        result += power / fact  # add the next term
        
    return result

###############################
### constants

###############################
### main variables: V, n, m, h
def dV_dt(t,x):
    return 1/1 * (current_S(t,x) - ( current_K(t,x) + current_L(t,x) + current_Na(t,x)))
def dn_dt(t,x):
    n = x['n']
    return alpha_n(t,x) * (1-n)- beta_n(t,x) * n

def dm_dt(t,x):
    m = x["m"]
    return alpha_m(t,x) *(1-m) - beta_m(t,x) * m
def dh_dt(t,x):
    h = x["h"]
    return alpha_h(t,x) *(1-h) - beta_h(t,x) * h

###############################
### intermediate variables: alphas, betas, stimulus (s),
#currents (I’s), ...
def alpha_n(t,x):
    V = x["v"]
    return (0.01*(10-V))/(exp_builtin(0.1*(10 - V)) - 1)
def alpha_m(t,x):
    V = x["v"]
    return (0.1*(25-V))/(exp_builtin(0.1*(25 - V)) - 1)
def alpha_h(t,x):
    V = x["v"]
    return 0.07* exp_builtin(-V/20)
    
def beta_n(t,x):
    V = x["v"]
    return 0.125* exp_builtin(-V/80) 
def beta_m(t,x):
    V= x["v"]
    return 4 * exp_builtin(-V/18)
def beta_h(t,x):
    V= x["v"]
    return 1/ exp_builtin(0.1*(30 - V))
def current_S(t,x):
    intervals =  [[10,11] , [20,21], [30,40], [50,51],  [53,54], [56,57] , [59,60] , [62,63] , [65,66]]
    for interval in intervals:
        if t > interval[0] and t < interval[1]:
            return 150
    return 0


def current_Na(t,x):
    return G_Na(t, x)*(x["v"] - 115)
def current_K(t,x):
    return G_K(t, x) * ( x["v"] + 12)
def current_L(t,x):
    return G_L(t, x) * ( x["v"] - 10.6)
def G_Na(t,x):
    return 120* x["m"]**3 * x["h"]
def G_K(t,x):
    return 36* (x["n"]**4)
def G_L(t,x):
    return 0.3


V_0 = 0
x = {"v" : V_0}
n_0 = alpha_n(0,x)/(alpha_n(0,x) + beta_n(0,x))
m_0 = alpha_m(0, x)/(alpha_m(0,x) + beta_m(0,x))
h_0 = alpha_h(0,x)/(alpha_h(0,x) + beta_h(0,x))
C = 1.0
V_Na = 115
V_K = -12
V_L = 10.6
################################
### input into EulerEstimator
derivatives = {
'v': dV_dt,
'n': dn_dt,
"m" : dm_dt,
"h" : dh_dt
}
initial_state = { "v" : V_0, "n" : n_0, "m" : m_0, "h" : h_0}
initial_point = (0, initial_state)
step_size = 0.01
num_steps = int(80/0.01)
euler = EulerEstimator(derivatives)
d2 = euler.estimate_points(initial_point, step_size,
 num_steps)
times = [point[0] for point in d2]
voltage_values = [point[1]["v"] for point in d2]
n_values = [point[1]["n"] for point in d2]
m_values = [point[1]["m"] for point in d2]
h_values = [point[1]["h"] for point in d2]

# Plot the results
plt.figure(figsize=(10, 6))

# Plot all variables
plt.plot(times, voltage_values, label="Voltage (V)", color='blue')


# Labels and title
plt.xlabel("Time (steps or ms)")
plt.ylabel("Variable Values")
plt.title("Hodgkin-Huxley Model of Action Potentials in Neurons")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
plt.clf()
plt.plot(times, n_values, label="n", color='green')
plt.plot(times, m_values, label="m", color='red')
plt.plot(times, h_values, label="h", color='purple')
plt.show()