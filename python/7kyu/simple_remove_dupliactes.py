# https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/python



def solve(arr):

  counter = {}

  for el in arr:
    if el not in counter:
      counter[el] = arr.count(el)

  print(counter)

  return list(set(arr))

solve([3, 4, 4, 3, 6, 3])