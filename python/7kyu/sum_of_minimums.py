# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python

def sum_of_minimums(numbers):
    sum = 0
    for line in numbers:
        sum += min(line)
    return sum


"""
* clever

--> use map(function, array)
return sum(map(min, numbers))
"""
