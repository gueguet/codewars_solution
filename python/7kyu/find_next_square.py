# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

import math 

def find_next_square(sq):

    if not math.sqrt(sq).is_integer():
        return -1

    next_square = sq+1

    while True:
        if math.sqrt(next_square).is_integer():
            return next_square
        else:
            next_square += 1


find_next_square(121)

