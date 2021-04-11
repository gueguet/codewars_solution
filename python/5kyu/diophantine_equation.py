# https://www.codewars.com/kata/554f76dca89983cc400000bb/train/python

import math

def sol_equa(n):
    """
    x - 2y = first_num
    x + 2y = second_num
    """

    result = []

    for i in range(1, int(math.sqrt(n)) + 1):

        if n % i != 0:
            continue # if not divisible by the int --> end the current iteration

        j = n / i # math like old time... i * j = n and we fix the i 
        y = (j - i) / 4
        x = i + 2 * y

        if (x.is_integer() and y.is_integer()):
            result.append([int(x), int(y)])

    result.sort(reverse=True)
    return result