"excercises for part 2 of chapter1"

def binary_to_decimal(string):
    #binary to decimal lol
    "binary to decimal"
    len_string = len(string)
    output = 0
    for i in range(len_string):
        output += int(string[len_string - i - 1]) * 2**i
    return str(output)
def hexadecimal_to_decimal(string):
    "hexa decimal to decimal"
    len_string = len(string)
    output = 0
    string = list(string)
    htoi= {
    "0": 0, "1": 1, "2": 2, "3": 3,
    "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "a": 10, "b": 11,
    "c": 12, "d": 13, "e": 14, "f": 15
}
    string = [htoi[n.lower()] for n in string]
    for i in range(len_string):
        output += int(string[len_string - i - 1]) * 16**i
    return str(output)

def decimal_to_binary(string):
    "decimal to binary"
    string = int(string)
    out = []
    while string > 0:
        last_num = None
        last_idx = None
        for i in range(string):
            if 2**i > string:
                break
            else:
                last_num = 2**i
                last_idx = i
        string -= last_num
        out.append(last_idx)
    output = [ ]
    for i in range(out[0]+1):
        if i in out:
            output.insert(0, 1)
        else:
            output.insert(0, 0)
    return "".join([str(s) for s in output])
def decimal_to_hexadecimal(string):
    "decimal to binary"
    string = int(string)
    coeficcients = []
    out = []
    last_idx = None
    while string > 0:
        last_num = None
        for i in range(string):
            if 16**i > string:
                break
            else:
                last_num = 16**i
                last_idx = i
        out.append(last_idx)
        val = None
        idx = None
        for i in range(16):
            num = last_num*i
            if string - num <  0:
                break
            else:
                idx = i
                val = num
        string -= val
        coeficcients.append(idx)
        htoi= {
    "0": 0, "1": 1, "2": 2, "3": 3,
    "4": 4, "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "a": 10, "b": 11,
    "c": 12, "d": 13, "e": 14, "f": 15
}
    itoh = {k : v for v,k in htoi.items()}
    output = ""
    for i in range(out[0]+1):
        if i in out:
            x = out.index(i)
            x = coeficcients[x]
            num = itoh[x].upper()
            output = num + output
        else:
            output  = "0" + output
    return output

def binary_to_hexadecimal(string):
    "binary to hexadecimal"

    return decimal_to_hexadecimal(binary_to_decimal(string))
