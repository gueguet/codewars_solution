# https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python

def largest_pair_sum(numbers):
  res = 0
  max_num = max(numbers)
  res += max_num
  numbers.remove(max_num)
  max_num = max(numbers)
  res += max_num
  return res

largest_pair_sum([10,14,2,23,19])


"""
* clever

def largest_pair_sum(numbers): 
    return sum(sorted(numbers)[-2:])
"""