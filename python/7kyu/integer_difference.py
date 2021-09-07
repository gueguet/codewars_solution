# https://www.codewars.com/kata/57741d8f10a0a66915000001/train/python

def int_diff(lst, n):
  res = 0
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
      if abs(lst[j] - lst[i]) == n:
        res += 1
  return res

int_diff([1, 2, 3, 4],0)

"""
* clever

import itertools

def int_diff(arr, n):
  return sum(abs(a-b) == n for a, b in itertools.combinations(arr, 2))
"""
