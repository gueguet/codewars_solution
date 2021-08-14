# https://www.codewars.com/kata/552c028c030765286c00007d/train/python

def iq_test(numbers):
  numbers = numbers.split(" ")
  numbers = list(map(int, numbers))
  num_odd = 0
  num_even = 0

  for num in numbers:
    if (num % 2 == 0):
      num_even += 1
    else:
      num_odd += 1

  index = 1
  if (num_odd > num_even):
    for num in numbers:
      if (num % 2 == 0):
        return index
      else:
        index += 1
  else:
    for num in numbers:
      if (num % 2 != 0):
        return index
      else:
        index += 1

iq_test("2 4 7 8 10")


"""
* clever

def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
"""
