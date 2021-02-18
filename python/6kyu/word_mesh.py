# https://www.codewars.com/kata/5c1ae703ba76f438530000a2/train/python

from termcolor import cprint

def word_mesh(word_array):
  res = ""
  for i in range(len(word_array)-1):

    match = False
    for j in range(len(word_array[i]),0,-1):
      if(word_array[i][-j:] == word_array[i+1][:j]):
        res += word_array[i+1][:j]
        match = True
        break

    if(match == False):
      return "failed to mesh"

  return res

word_mesh(['california', 'niagara', 'arachnophobia', 'biannual', 'alumni', 'nibbles', 'blessing'])
# 'niaaraabiaalnibles' should equal 'niaarabiaalnibles'



"""
# Using regex
import re
def word_mesh(arr):
    common = re.findall(r'(.+) (?=\1)',' '.join(arr))
    return ''.join(common) if len(common) + 1 == len(arr) else 'failed to mesh'
"""