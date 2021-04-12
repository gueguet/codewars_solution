# https://www.codewars.com/kata/5a045fee46d843effa000070/train/python

import math


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5 + 1), 2):
        if (n % i == 0):
            return False
    return True

def decomp(n):
    n = math.factorial(n)
    print(n)

    prime_list = [x for x in range(n) if is_prime(x)]
    print(prime_list)

    res = ""
    for num in prime_list:
        
        print(num)
        print(n)

        if (n > num):
            res += "{}^{} * ".format(num, n//num)
        else:
            res += "{}".format(num)

        n = n%num

    print(res) 
    return res 



decomp(12)