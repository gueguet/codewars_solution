# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

import string 

def rot13(message):
    alphabet = string.ascii_lowercase + string.ascii_lowercase
    res = []
    for char in message:
        if (char.isalpha()):
            initial_idx = alphabet.index(char.lower())
            if (char.isupper()):
                res.append(alphabet[initial_idx + 13].upper())
            else:
                res.append(alphabet[initial_idx + 13])
        else:
            res.append(char)
    return "".join(res)

rot13("Test")
