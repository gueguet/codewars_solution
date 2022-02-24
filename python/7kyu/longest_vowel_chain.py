# https://www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python

def solve(s):
    vowels = "aeiou"
    max_res = ""
    chain = ""
    
    for letter in s:
        if letter in vowels:
            chain += letter
        else:
            if len(chain) > len(max_res):
                max_res = chain
            chain = ""
    
    return len(max_res)


"""
* clever

def solve(s):
    return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))
    
    
from re import findall
def solve(s):
    return max(map(len, findall("[aeiou]+", s)))
"""
