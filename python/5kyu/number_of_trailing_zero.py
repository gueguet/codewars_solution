# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/python

# We would first count the number of multiples of 5 between 1 and n (which is X ), then the number of multiples of 25 ( ~s ), then 125, and so on

def zeros(n):
    count = 0
    i = 5
    if n < 0:
        return False
    while n//i > 0:
        count = count + n//i
        i = i * 5
    return count

zeros(30)
