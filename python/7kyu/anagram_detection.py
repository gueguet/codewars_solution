# https://www.codewars.com/kata/529eef7a9194e0cbc1000255

from typing import Counter


def is_anagram(test, original):
    dict_test = Counter(test.lower())
    dict_original = Counter(original.lower())
    
    if (dict_original == dict_test):
        return True
    else:
        return False


is_anagram("foefet", "toffee")

"""
* clever

def is_anagram(test, original):
    return sorted(original.lower()) == sorted(test.lower()) 
"""
