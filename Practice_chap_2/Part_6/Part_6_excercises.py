def selection_sort(array):
    copy_of_arr = array[:]
    sorted_array = []
    for i in range(len(copy_of_arr)):
        least_element = calc_min(copy_of_arr)
        copy_of_arr.remove(least_element)
        sorted_array.append(least_element)
    return sorted_array

def calc_min(arr):
    least_element = float("inf")
    for i in arr:
        if i < least_element:
            least_element = i
    return least_element
def bubble_sort(arr):
    copy_of_arr = arr[:]
    x = True
    while x:
        did_swap = False
       for i in range(len(copy_of_arr)):
            for j in range(0, len(copy_of_arr)-i-1): 
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        return arr

def insertion_sort(arr):
    copy_of_arr = arr[:]
    x = True
    while x:
        did_swap = False
        for i in range(len(copy_of_arr)):
            for j in range(0, len(copy_of_arr)-i-1):
                if arr[j] > arr[j+1]:
                    for i in range(j+1):
                        if arr[i] < arr[j+1]:
                            temp = arr[j+1]
                            arr.remove(arr[j+1])
                            arr.insert(i+1, temp)
                            break
        return arr
def calc_max(arr):
    largest_element = -float("inf")
    for i in arr:
        if i > largest_element:
            largest_element = i
    return largest_element
def counting_sort(arr):
    min_number = calc_min(arr)
    arr = [ i - min_number for i in arr]
    sorted_array = []
    counts = [0 for i in range(calc_max(arr)+1)]
    for i in (arr):
        counts[i] += 1
    for  i  in range(len(counts)):
        for _ in range(counts[i]):
            sorted_array.append(i+min_number)
    return sorted_array

