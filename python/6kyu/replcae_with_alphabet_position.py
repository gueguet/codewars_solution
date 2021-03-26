# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

from string import ascii_lowercase

position_list = [str(i) for i in range (1,27)]

def alphabet_position(text):
    text = text.lower()
    alpha_dict = dict(zip(ascii_lowercase, position_list))
    res = ""
    for char in text:
        if (char in alpha_dict):
            res += alpha_dict[char] + " "
    return res[:-1]


alphabet_position("The sunset sets at twelve o' clock.")


"""
* clever :
return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
"""