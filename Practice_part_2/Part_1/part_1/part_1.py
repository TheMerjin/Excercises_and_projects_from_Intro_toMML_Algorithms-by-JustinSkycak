""" Excercises for part 1. Brute force encoding"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
def encode_string(string, a, b):
    
    stoi = {v: i+1 for i,v in  enumerate(alphabet)} #dict string to index
    stoi[" "] = 0 # add space character

    encoded_array= [ a*stoi[i] + b for i in string.lower()] #the index is found and encoded
    return encoded_array
    
print(encode_string("a", 1, 2))

def decode_numbers(numbers, a , b ):
    decoded_numbers = [(i-b)/a for i in numbers]
    for n in decoded_numbers:
        if n > len(alphabet):
            return False
        if n < 0:
            return False
        if not n.is_integer():
            return False
    itos = {i+1: v for i,v in  enumerate(alphabet)} #dict string to index
    itos[0] = " "
     # add space character
    return "".join([itos[i] for i in decoded_numbers])

def decode_message(message):
    for i in range(1, 101):
        for n in range(1, 101):
            decoded_message = decode_numbers(message, i , n )
            if decoded_message:
                print(decoded_message, f"value of a: {i} value of b: {n}")
    return decoded_message
