# https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python

# sqrt (s * (s - a) * (s - b) * (s - c)), where s = (a + b + c) / 2.

from math import sqrt

def heron(a,b,c):
    s = ( a+b+c ) / 2
    res = sqrt((s * (s - a) * (s - b) * (s - c)))
    return round(res,2)



heron(3, 4, 5)