class HashTable():
    def __init__(self, buckets):
        self.array = [ [] for i in range(len(buckets))]
        self.buckets = buckets
    def hash(self, string):
        if not isinstance(string, str):
            raise Exception(" Wrong input")
        else:
            sum = 0
            letter_to_number = {chr(i): i - 97 for i in range(97, 123)}
            for i in string:
                sum += letter_to_number[i]
            bucket = sum % self.buckets
            return bucket
    def insert(self, arr, key, values):
        bucket = hash(key)
        arr[bucket].append((key, values))
    def find(self ,arr, key):
        bucket = hash(key)
        for i in arr[bucket]:
            if i[0] == key:
                return i[1]

    