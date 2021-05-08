# https://www.codewars.com/kata/5f3afc40b24f090028233490/train/python

def swap(s,n):
    n_bin = "{0:b}".format(n) # or bin(n)[2:]
    n_bin_list = list(n_bin)

    res = ""
    counter = 0

    for letter in s:

        if counter == len(n_bin_list):
            counter = 0

        if (letter.isalnum()):

            if (n_bin_list[counter] == "1"):

                if (letter.isupper()):
                    res += letter.lower()
                else:
                    res += letter.upper()

            else:
                res += letter

            counter += 1

        else:
            res += letter

    return res


swap("Hello world!", 11)


""" 
* clever
from itertools import cycle
def swap(s,n):
    binary = cycle(bin(n)[2:])
    return ''.join(char.swapcase() if char.isalpha() and next(binary) == '1' else char for char in s)
"""