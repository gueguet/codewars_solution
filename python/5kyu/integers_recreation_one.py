# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

import math

def list_squared(m, n):

    res = []

    for i in range(m, n+1):
        sum_all_divisors_squared = sum([x*x for x in range(1,i+1) if i%x == 0])
        if (math.sqrt(sum_all_divisors_squared).is_integer()):
            res.append([i, sum_all_divisors_squared])

    return res




# ! GOT A TIMEOUT !!! Need to use memoization :

def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]
    return helper

@memoize
def sum_of_squares(n):
    squares = [x**2 for x in range(1, n+1) if n % x == 0]
    return sum(squares)

def list_squared(m, n):
    result = []
    for i in range(m, n):
        sums = sum_of_squares(i)
        if sums > 0 and sums**0.5 % 1 == 0:
            result.append([i, sums])
    return result





# * other solution 

def get_divisors_sum(n):
    """Get the divisors: iterate up to sqrt(n), check if the integer divides n with r == 0
        Return the sum of the divisors squared."""
    divs=[1]
    for i in range(2,int(n**0.5)+1): # * this is how you can reduce the time !!!
        if n%i == 0:
            divs.extend([i, int(n/i)])
    divs.extend([n])

    print(divs)
    
    # Get sum, return the sum 
    sm = sum([d**2 for d in list(set(divs))])
    return sm
    
    
def list_squared(m, n):
    """Search for squares amongst the sum of squares of divisors of numbers from m to n """
    out = []
    for j in range(m,n+1):
        s = get_divisors_sum(j) # sum of divisors squared.
        if  (s ** 0.5).is_integer(): # check if a square.
            out.append([j, s])
    return out


list_squared(246,246)