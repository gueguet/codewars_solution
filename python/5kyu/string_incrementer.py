# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

import re

def increment_string(strng):
    
    match_number = re.findall("\d+",strng)
    res = strng
    
    if match_number:
        number = int(match_number[-1])
        res = res[:-len(str(number))]
        new_number = number + 1
        
        if (len(str(new_number)) > len(str(number)) and match_number[-1][0] == "0"):
            res = res[:-1]
            res += str(new_number)
        else:    
            res += str(new_number)
    
    else:
        res += "1"
    
    return res    


"""
# * Clever

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
"""

increment_string("B18331uwya10700001619484159")