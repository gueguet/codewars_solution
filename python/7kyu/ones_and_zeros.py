# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/train/python

def binary_array_to_number(arr):
    res = 0
    power = 0
    for digit in arr[::-1]:
        res += digit * (2**power)
        power += 1
    return res


binary_array_to_number([0,0,0,1])
binary_array_to_number([0,0,1,0])
binary_array_to_number([1,1,1,1])


"""
* clever :
return sum(digit * 2**i for i, digit in enumerate(reversed(arr)))
return int("".join(map(str, arr)), 2)
"""