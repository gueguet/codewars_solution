# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

import math 

def find_next_square(sq):

    if not isinstance(int(math.sqrt(sq)),int):
        return -1

    # next_square = sq

    # while True:
    #     print(math.sqrt(next_square))
    #     if (isinstance(math.sqrt(next_square), int)):
    #         return next_square
    #     else:
    #         next_square += 1


find_next_square(121)
f
