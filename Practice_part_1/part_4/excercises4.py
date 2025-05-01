"excercises 4 of Inrto to machine learning algorithms"

import random
import matplotlib
matplotlib.use("Qt5agg")
from matplotlib import pyplot as plt
plt.style.use('_mpl-gallery')

def sim_probability(num_heads, num_flips):
    all_flips = {}
    num_trials = 1000
    for i in range(num_trials):
        flips = []
        for n in range(num_flips):
            if random.random() >= 0.5:
                flips.append(1)
            else:
                flips.append(0) 
        all_flips[f"{i}"] = flips
    count = 0
    num_heads_in_each_flip = []
    for k,v in all_flips.items():
        count = 0
        for n in v:
            if n == 1:
                count += 1
        num_heads_in_each_flip.append(count)
    
    num__times_heads_equals_num_heads = 0
    for _ in num_heads_in_each_flip:
        if _ == num_heads:
            num__times_heads_equals_num_heads += 1
    

    return num__times_heads_equals_num_heads/ num_trials, sum(num_heads_in_each_flip)/ len(num_heads_in_each_flip)




NUM_FLIPS = 50
probs = []
for _ in range(0,NUM_FLIPS+1):
    x = sim_probability(_, NUM_FLIPS)[0]
    probs.append(x)
x_range = list(range(0, NUM_FLIPS+1))



def plot_probs(x, x_range):
    plt.figure(figsize=(6,6))
    
    plt.tight_layout()
    plt.plot(x_range, x)
    plt.show()
    print(sum(probs))
    
if __name__ == "__main__":
    plot_probs(probs, x_range)