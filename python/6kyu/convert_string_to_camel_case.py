# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python

import re 

def to_camel_case(text):
  
  splitted = []
  splitted = re.split(r"[\_\-]", text)

  res = ""

  if (splitted != []):
    res += splitted[0]

  for word in splitted[1::]:
    res += word.capitalize()

  return res


to_camel_case("the_Cat-was_Hungry")
