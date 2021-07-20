# https://www.codewars.com/kata/50654ddff44f800200000007/train/python

def solution(a, b):
  if (len(a) < len(b)):
    return a + b + a
  else:
    return b + a + b 
