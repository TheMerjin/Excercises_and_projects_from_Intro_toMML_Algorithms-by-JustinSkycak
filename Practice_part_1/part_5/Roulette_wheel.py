"The excercise in part 5 roulette wheel index selection"
import random

def random_draw(distribution):
    past_distribution = []
    cum_distribution = []
    for i in range(len(distribution)):
        if i== 0:
            past_distribution.append(distribution[i])
            cum_distribution.append(distribution[i])
        else:
            cum_distribution.append(distribution[i]+sum(past_distribution))
            past_distribution.append(distribution[i])
    random_num = random.random()
    for _ in range(len(cum_distribution)):
            if random_num <= cum_distribution[_]:
                return _
            
    return cum_distribution

                    
print(random_draw([0.5, 0.3, 0.2]))
                        


# [0.4, 0.2, 0.2, 0.2] = [0.4, 0.4+0.2, ...] 