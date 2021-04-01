# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_bits(n):
    bin_value = format(n,'b')
    return bin_value.count("1")

count_bits(1234)

"""
better :
return bin(n).count("1")
"""