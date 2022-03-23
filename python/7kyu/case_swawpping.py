# https://www.codewars.com/kata/5590961e6620c0825000008f/train/python

def swap(string_):
    res = ""
    for char in string_:
        if char.islower():
            res += char.upper()
        else:
            res += char.lower()
            
    return res


"""
* clever

def swap(string_):
    return string_.swapcase()
""" 
