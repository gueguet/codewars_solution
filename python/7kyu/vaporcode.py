# https://www.codewars.com/kata/5966eeb31b229e44eb00007a/train/python

def vaporcode(s):
  res = ""
  for letter in s:
    if letter.isalpha():
      res += letter.upper()
      res += "  " 
    elif letter == " ":
      pass
    else:
      res += letter + "  "
  return res[:-2]


vaporcode("Lets go to the movies")


"""
* clever

def vaporcode(s):
    return "  ".join(s.replace(" ", ""))
"""
