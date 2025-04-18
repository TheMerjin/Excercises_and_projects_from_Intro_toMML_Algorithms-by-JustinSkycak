"this is to practice testing and the hello world excercises"


def check_if_symmetric(string):
    "checks if a string is symmetric"
    len_string = len(string)
    if len_string == 1:
        return True
    for n in range(len_string):
        if string[n] != string[len_string-n-1]:
            return False
    return True
print(check_if_symmetric("abba"))
def convert_to_numbers(string):
    stoi = {
    " ": 0,
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
    "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
    "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
    "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
    "z": 26
}
    out = []
    for i in string:
        out.append(stoi[i])
    return out
print(convert_to_numbers("a cat"))
def convert_to_letters(arr):
    stoi = {
    " ": 0,
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7,
    "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
    "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19,
    "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
    "z": 26
}
    itos = {n:v for v, n  in stoi.items()}
    out = []
    for i in arr:
        out.append(itos[i])
    return "".join(out)
def get_intersections(arr1, arr2):
    result = []
    for i in arr1:
        if i in arr2:
            result.append(i)
    return result

        
print(type((3,4)))