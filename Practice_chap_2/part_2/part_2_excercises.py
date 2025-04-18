""" Doc string excercises part 2"""

digits = [ 1,2,3,4,5,6,7,8,9]
dtoi = {v: i for v,i in enumerate(digits)}

square  = [ [None, None, None ],
           [None, None, None],
           [None, None, None]]

def is_magic(square):
    # Rows, columns, diagonals
    return (
        sum(square[0]) == 15 and
        sum(square[1]) == 15 and
        sum(square[2]) == 15 and
        sum([row [0] for row in square]) == 15 and
        sum([row [1] for row in square ]) == 15 and
        sum([row[2] for row in square]) == 15 and
        sum([square[i][i] for i in range(len(square))]) == 15 and
        sum([square[i][2-i] for i in range(len(square))]) == 15
    )
current_digits = [1,2,3,4,5,6,7,8,9]
x = True
while x:
    for x1 in current_digits:
        for x2 in current_digits:
            if x2 != x1:
                for x3 in current_digits:
                    if x3 not in [x1, x2]:
                        for x4 in current_digits:
                            if x4 not in [x1, x2, x3]:
                                for x5 in current_digits:
                                    if x5 not in [x1, x2, x3, x4]:
                                        for x6 in current_digits:
                                            if x6 not in [x1, x2, x3, x4, x5]:
                                                for x7 in current_digits:
                                                    if x7 not in [x1, x2, x3, x4, x5, x6]:
                                                        for x8 in current_digits:
                                                            if x8 not in [x1, x2, x3, x4, x5, x6, x7]:
                                                                for x9 in current_digits:
                                                                    if x9 not in [x1, x2, x3, x4, x5, x6, x7, x8]:
                                                                        square = [
                                                                            [x1, x2, x3],
                                                                            [x4, x5, x6],
                                                                            [x7, x8, x9]
                                                                        ]
                                                                        if is_magic(square):
                                                                            for row in square:
                                                                                print(row)
                                                                            print()
