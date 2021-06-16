# https://www.codewars.com/kata/5cb7baa989b1c50014a53333/train/python

import numpy as np

def is_sator_square(tablet):
    n = len(tablet)
    table = np.array(tablet)
    for i in range(n-1):
        if (list(table[i]) != list(table[-i-1,::-1])):
            return False
        if (list(table[i]) != list(table[:,i])):
            return False
        if (list(table[i]) != list(table[::-1,-i-1])):
            return False
        
    return True

tablet = [['P', 'E', 'R'],
          ['E', 'V', 'E'],
          ['R', 'E', 'P']]

is_sator_square(tablet)


"""
* clever

def is_sator_square(tablet):
    A = {''.join(lst) for lst in tablet}
    B = {''.join(lst)[::-1] for lst in tablet}
    C = {''.join(lst) for lst in zip(*tablet)}
    D = {''.join(lst)[::-1] for lst in zip(*tablet)}
    return A == B == C == D

"""