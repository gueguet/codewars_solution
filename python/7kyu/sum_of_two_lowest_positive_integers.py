# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

def sum_two_smallest_numbers(numbers):
    res = 0
    numbers = sorted(numbers)
    res = numbers[0] + numbers[1]
    return res

sum_two_smallest_numbers([5, 20, 12, 18, 22])


""" 
clever :
return sum(sorted(numbers)[:2])
"""