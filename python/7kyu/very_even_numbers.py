# https://www.codewars.com/kata/58c9322bedb4235468000019/train/python

def is_very_even_number(n):
    if (len(str(n)) == 1):
        return n % 2 == 0
    else:
        return is_very_even_number(sum([int(x) for x in str(n)]))



