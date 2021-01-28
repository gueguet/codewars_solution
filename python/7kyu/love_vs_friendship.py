# https://www.codewars.com/kata/59706036f6e5d1e22d000016/train/python

import string

def words_to_marks(s):
  list_letter = string.ascii_lowercase[0:27]
  list_number = [i for i in range(1,27)]

  value_dict = dict(zip(list_letter,list_number))

  res = 0
  for char in s:
    res += value_dict[char]

  return res


