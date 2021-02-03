# https://www.codewars.com/kata/599c20626bd8795ce900001d/train/python

def summy(string_of_ints):
    
    res = 0
    list_of_int = string_of_ints.split(" ")

    for item in list_of_int:
        res += int(item)

    return res


summy("1 2 3")
