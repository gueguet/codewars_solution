# https://www.codewars.com/kata/5d50e3914861a500121e1958/train/python

import string

def add_letters(*letters):
    letter_to_val = dict(zip(string.ascii_lowercase, [x for x in range(1,27)]))
    val_to_letter = dict(zip([x for x in range(1,27)], string.ascii_lowercase))
    
    if letters == []:
        return "z"
    
    sum = 0
    for letter in letters:
        sum += letter_to_val[letter]
            
    if (sum % 26 == 0):
        return "z"
        
    return val_to_letter[sum % 26]
    


add_letters("f", "k", "i", "e", "a", "c", "s", "x")


"""
* clever

num = 'abcdefghijklmnopqrstuvwxyz'
def add_letters(*letters):
    x = 0
    x = sum(num.index(i)+1 for i in letters)
    while x-1 > 25:
        x -= 26
        
    return num[x-1]
"""
