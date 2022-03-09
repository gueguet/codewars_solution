# https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python

import string

def find_missing_letter(chars):
    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    
    if (chars[0].islower()):
        diff = letters_lower.index(chars[0]) 
        for ind, letter in enumerate(chars):
            if not (letter == letters_lower[ind+diff]):
                return letters_lower[ind+diff]
    else:
        diff = letters_upper.index(chars[0]) 
        for ind, letter in enumerate(chars):
            if not (letter == letters_upper[ind+diff]):
                return letters_upper[ind+diff]
    

print(find_missing_letter(['O','Q','R','S']))


"""
* clever

def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))
"""
