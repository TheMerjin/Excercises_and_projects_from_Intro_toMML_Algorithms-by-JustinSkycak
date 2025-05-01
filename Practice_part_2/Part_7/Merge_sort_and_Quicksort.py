" Here is part 13 and we are using merge and quicksort"
import random
def merge(arr1, arr2):
    i =0
    j = 0
    merged_sorted_list = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]: 
            merged_sorted_list.append(arr1[i])
            i += 1 
        else:
            merged_sorted_list.append(arr2[j])
            j+= 1
    merged_sorted_list.extend(arr1[i:])
    merged_sorted_list.extend(arr2[j:])
    return merged_sorted_list


def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        half_point = len(arr)//2
        half1 = merge_sort(arr[:half_point])
        half2 = merge_sort(arr[half_point: len(arr)])
        return merge(half1, half2)

def quick_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        pivot = random.choice(arr)
        less_than = [i for i in arr if i < pivot]
        equal = [i for i in arr if i == pivot]
        greater_than = [i for i in arr if i > pivot]
        return quick_sort(less_than) + [pivot] + quick_sort(greater_than)
        

