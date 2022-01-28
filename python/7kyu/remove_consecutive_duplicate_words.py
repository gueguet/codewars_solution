# https://www.codewars.com/kata/5b39e91ee7a2c103300018b3/train/python

def remove_consecutive_duplicates(s):
  words = s.split(" ")
  res = []
  last_seen = "" 
  for word in words:
    if word != last_seen:
      res.append(word)
      last_seen = word
  return " ".join(res)

remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta')


"""
# * clever

from itertools import groupby

def remove_consecutive_duplicates(s):
  return ' '.join(k for k,_ in groupby(s.split()))
"""

