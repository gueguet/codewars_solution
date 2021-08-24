# https://www.codewars.com/kata/58da7ae9b340a2440500009c/train/python

from math import sqrt

def point_in_circle(x, y):
  norm = sqrt(x**2 + y**2)
  if (norm < 1):
    return True
  else:
    return False
