# https://www.codewars.com/kata/5517fcb0236c8826940003c9/train/python

from math import gcd
from fractions import Fraction

def sum_fracts(lst):

  if not lst:
    return None
  
  num_list = [el[0] for el in lst]
  denom_list = [el[1] for el in lst]

  # find lcm
  ans = denom_list[0] 
  for i in range(1, len(denom_list)):
    ans = (((denom_list[i] * ans)) // (gcd(denom_list[i], ans)))
  lcm = ans

  # find num sum
  sum_num = 0
  for i in range(0,len(num_list)):
    sum_num += num_list[i] * (lcm // denom_list[i])

  if (sum_num % lcm == 0):
    return sum_num//lcm

  # reduce fraction
  res = Fraction(sum_num, lcm)
  str_res = str(res).split('/')

  return ([int(str_res[0]),int(str_res[1])])


sum_fracts([[69, 130], [87, 1310], [3, 4]])


"""
* clever... better to know hos Fraction work in python :)

from fractions import Fraction

def sum_fracts(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]
"""
