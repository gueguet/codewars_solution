# https://www.codewars.com/kata/5650ab06d11d675371000003/train/python

def split_in_parts(s, part_length): 
  res = ""
  count = 1
  for letter in s:
    if count % part_length == 0:
      res += letter + " "
    else:
      res += letter
    count += 1

  if res[-1] == " ":
    return res[:-1]
  else:
    return res


split_in_parts("supercalifragilisticexpialidocious", 3)


"""
* clever

from textwrap import wrap

def split_in_parts(s, part_length): 
    return " ".join(wrap(s,part_length))
"""
