# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        return n % n**0.5 == 0

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
