# https://www.codewars.com/kata/54db15b003e88a6a480000b9/train/python

from math import gcd

def from_nb_2_str(n, modsys):
  
  multiply_res = 1
  for num in modsys:
    multiply_res *= num

  print(multiply_res)
  print(n)
  if (multiply_res <= n):
    return "Not applicable"

  for i in range(len(modsys)):
    for j in range(i+1,len(modsys)):
      if gcd(modsys[i],modsys[j]) != 1:
        return "Not applicable"

  res = []

  for mod in modsys:
    res.append(n%mod)
  
  return "-" + str(res[0]) + "--" + "--".join(str(val) for val in res[1:-1]) + "--" + str(res[0-1]) + "-"

  

print(from_nb_2_str(779, [8,7,5,3]))
# print(from_nb_2_str(15, [8,6,5,3]))


"""
* clever

! super cool
from itertools import combinations
from fractions import gcd
from functools import reduce

def fromNb2Str(n, modsys): 
    if any(gcd(x, y) > 1 for x, y in combinations(modsys, 2)) or n > reduce(lambda x, y: x*y, modsys):
        return "Not applicable"
    return "-" + "--".join(str(n % m) for m in modsys) + "-"
"""
