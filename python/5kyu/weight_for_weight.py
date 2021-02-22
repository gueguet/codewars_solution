# https://www.codewars.com/kata/55c6126177c9441a570000cc/train/python

# return sum of digits of a number
from typing import final
from pprint import pprint
from collections import Counter

def sum_digits(num):
  res = 0
  for char in num:
    res += int(char)
  return res

def order_weight(strng):
  if strng == "":
    return ""

  # can use : sorrted(strng.split())
  weight_list = strng.split(" ")
  weight_list.sort()
  new_weight_list = list(map(sum_digits, weight_list))

  res_dict = {k: [] for k in new_weight_list}

  for (index, val) in enumerate(new_weight_list):
    res_dict[val].append(weight_list[index])

  final_res = ""
  for key in sorted(res_dict.keys()):
    for item in res_dict[key]:
      final_res = final_res + item + " "

  return(final_res[:-1])

order_weight("2000 10003 1234000 44444444 9999 11 11 22 123")


"""
Best practice - keep first method okay :

--> Use the sorted method with the method defined... way easier !!
Or you can even use lambda functions

def order_weight(strng):
    # your code
    initial_list = sorted(strng.split())
    result = " ".join(sorted(initial_list, key=sum_string))
    
    return result

In one function :
def order_weight(_str):
  return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
"""