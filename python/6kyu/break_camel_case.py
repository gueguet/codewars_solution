# https://www.codewars.com/kata/5208f99aee097e6552000148/train/python

def solution(s):
  res = ""

  for char in s:
    if (char.isupper()):
      res += " {}".format(char)

    else:
      res += char

  return res