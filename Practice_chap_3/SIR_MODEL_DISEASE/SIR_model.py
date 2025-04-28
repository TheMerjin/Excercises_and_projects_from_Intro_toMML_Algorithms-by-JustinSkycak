# This excercise is for SIR modeling for disease spread
from multi_var_euler_estimator import EulerEstimator
import matplotlib
from matplotlib import pyplot as plt

"""The SIR model assumes three populations : susceptible, infected, recovered"""
""" the more meeting beetween people occurs the rate of decrease of susceptible people increases as suscptible become infected"""
NUM_PEOPLE = 1001

num_infected = 1
num_susceptible = 1000

num_meetings = num_infected * num_susceptible * 0.01
days = 100
for i in range(days):
    num_meetings = num_infected * num_susceptible * 0.01
    d_S = -0.03 * 0.01 * num_susceptible * num_infected
    d_I = -d_S - 0.02 * num_infected
    d_R = 0.02 * num_infected


def d_S(t, state):
    return state["susceptible"] * state["infected"] * 0.01 * -0.03


def d_I(t, state):
    return (
        -(state["susceptible"] * state["infected"] * 0.01 * -0.03)
        - 0.02 * state["infected"]
    )


def d_R(t, state):
    return 0.02 * state["infected"]


derivates = {"susceptible": d_S, "infected": d_I, "recovered": d_R}

initial_state = {"susceptible": 1000, "infected": 1, "recovered": 0}
initial_point = (0, initial_state)

euler = EulerEstimator(derivatives=derivates)
step_size = 0.3
num_steps = 1000
d2 = euler.estimate_points(initial_point, step_size, num_steps)

steps = [i * step_size for i in range(num_steps)]

times = [point[0] for point in d2]
susceptible_values = [point[1]["susceptible"] for point in d2]
infected_values = [point[1]["infected"] for point in d2]
recovered_values = [point[1]["recovered"] for point in d2]

# Plotting using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(times, susceptible_values, label="Susceptible", color="blue")
plt.plot(times, infected_values, label="Infected", color="red")
plt.plot(times, recovered_values, label="Recovered", color="green")

plt.xlabel("Time (steps or days)")
plt.ylabel("Number of People")
plt.title("SIR Model Dynamics")
plt.legend()
plt.grid(True)
plt.show()
