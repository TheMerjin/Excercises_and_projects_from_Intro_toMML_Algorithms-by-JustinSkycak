from Roulette_wheel import random_draw
import random
import matplotlib
matplotlib.use("Qt5agg")
from matplotlib import pyplot as plt
def test(n, distribution):
    draws = []
    for i in range(n):
        draws.append(random_draw(distribution))
    plt.hist(draws, bins = [0,1,2,3,4,5])
    plt.show()
test(1000, [0.5, 0.3, 0.0, 0.0, 0.4])
    #[0,1,2,3,1] 
