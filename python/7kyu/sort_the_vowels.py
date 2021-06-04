# https://www.codewars.com/kata/59e49b2afc3c494d5d00002a/train/python

def sort_vowels(s):


  # ! can replace with --> if isintance(s,str), do the two tests in once
  if type(s) == int:
    return ""
  if not s:
    return ""

  vowels = "aeiouAEIOU"
  res = ""

  # don't need this...
  if s[0] in vowels:
    res += "|{}\n".format(s[0].upper())
  else:
    res += "{}|\n".format(s[0].upper())

  for char in s[1:]:
    if char == " ": # no need to do that 
      res += " |\n" 
      continue

    if char in vowels:
      res += "|{}\n".format(char)
    else:
      res += "{}|\n".format(char)

  return res[:-1]


sort_vowels('Rnd Te5T')

"""
* clever

def sort_vowels(s):
    return "" if not isinstance(s, str) else "\n".join("|" + x if x in "aeiouAEIOU" else x + "|" for x in s)

"""
