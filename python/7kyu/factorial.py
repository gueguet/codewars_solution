# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

def factorial(n):
  if (n<0 or n>12):
    raise ValueError
  if (n==0):
    return 1
  else:
    return factorial(n-1)*n
