def five_start_times_three_minus_four(n):
    terms = [5]
    while len(terms) < n:
        prev_term = terms[-1]
        next_term = 3* prev_term -4
        terms.append(next_term)
    return terms

def recursive_five_start_times_three_minus_four(n):
    if n == 1:
        return 5
    else:
        prev_term = recursive_five_start_times_three_minus_four(n-1)
        return 3* prev_term - 4
    
    
print(recursive_five_start_times_three_minus_four(4))
