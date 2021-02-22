# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

from os import close
def valid_parentheses(string):

  open_par = 0
  close_par = 0
  
  for char in string:

    if (char == "("):
      open_par += 1
    elif (char == ")"):
      close_par += 1

    if (close_par > open_par):
      return False

  if (open_par == close_par):
    return True

  return False
  

# print(valid_parentheses("  ("))
# print(valid_parentheses("hi())("))

