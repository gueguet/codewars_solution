# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python 

import string

def is_pangram(s):
    s = s.lower()
    string_list = []
    for letter in s:
        if letter in string.ascii_lowercase:
            if letter not in string_list:
                string_list.append(letter)
                
    for lower_letter in string.ascii_lowercase:
        if (lower_letter not in string_list):
            return False
            
    return True

"""
* clever

import string

def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
"""
