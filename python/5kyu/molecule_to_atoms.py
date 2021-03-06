# https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python

from collections import Counter
from collections import deque
from termcolor import cprint
from pprint import pprint

def parse_molecule (formula):

    closing_char = ")]}"
    opening_char = "([{"

    multiplier = 1
    atom = ""
    last_char = "" 

    # * could be a dequeue
    saved_multiplier = deque()

    res = Counter()

    for char in reversed(formula):

        print(char)

        if (char.isnumeric()):
            if (last_char.isnumeric()):
                multiplier = int(multiplier/saved_multiplier.pop())
                last_multiplier = int(char + str(last_char))
                saved_multiplier.append(last_multiplier)
                multiplier = multiplier * last_multiplier
            else:
                last_multiplier = int(char)
                saved_multiplier.append(last_multiplier)
                multiplier = multiplier * int(char)

        elif (char in closing_char): # * be careful --> read the string in reverse
            pass

        elif (char in opening_char): # * be careful --> read the string in reverse
            if (len(saved_multiplier) != 0):
                multiplier = int(multiplier/saved_multiplier.pop())
            
        else:
            atom = char + atom
            if (char.isupper()):
                res[atom] += multiplier
                atom = ""
                
                # ! how to know if need to reduce the multiplier... ?
                if (last_char.isnumeric()):
                    multiplier = int(multiplier/saved_multiplier.pop())

        last_char = char

    return res


# print(parse_molecule("Mg(OH)2"))
# parse_molecule("{[Co(NH3)4(OH)2]3Co}(SO4)3")
# print(parse_molecule("K4[ON(SO3)2]2")) # * should be : {'K': 4, 'O': 14, 'N': 2, 'S': 4}
# print(parse_molecule("C6H12O6")) # * should be : {'K': 4, 'O': 14, 'N': 2, 'S': 4}
# print(parse_molecule("(C5H5)Fe(CO)2CH3")) 

print(parse_molecule("As2{Be4C5[BCo3(CO2)3]2}4Cu5")) # * should be : {'As': 2, 'Be': 16, 'C': 44, 'B': 8, 'Co': 24, 'O': 48, 'Cu': 5}