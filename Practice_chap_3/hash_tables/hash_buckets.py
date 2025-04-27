array = [ [], [], [], [], []]
def hash(string):
    if not isinstance(string, str):
        raise Exception(" Wrong input")
    else:
        sum = 0
        letter_to_number = {chr(i): i - 97 for i in range(97, 123)}
        for i in string:
            sum += letter_to_number[i]
        bucket = sum % 5 
        return bucket
def insert(arr, key, values):
    bucket = hash(key)
    arr[bucket].append((key, values))
def find(arr, key):
    bucket = hash(key)
    for i in arr[bucket]:
        if i[0] == key:
            return i[1]

insert(array, 'a', [0,1])
insert(array, 'b', 'abcd')
insert(array, 'c', 3.14)
print(array)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value