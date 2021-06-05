# https://www.codewars.com/kata/55031bba8cba40ada90011c4/train/python

import re

def is_cubic(number):
  cube_sum = sum([int(digit)**3 for digit in number])
  if cube_sum == int(number):
    return True
  return False

def is_sum_of_cubes(s):

  res = []
  groups = re.findall(r'\d{1,3}', s)

  for group in groups:
    print(group)
    if is_cubic(group):
      print(group)
      res.append(int(group))

  if res:
    res.append(sum(res))
    return " ".join([str(num) for num in res]) + " Lucky"

  return "Unlucky"


s = "aqdf&0#1xyz!22[153(777.777"

is_sum_of_cubes(s)


