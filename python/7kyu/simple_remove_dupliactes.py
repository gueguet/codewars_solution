# https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/python

from collections import Counter

def solve(arr):
  counter = Counter(arr)
  print(counter)


solve([3, 4, 4, 3, 6, 3])

