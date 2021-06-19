# https://www.codewars.com/kata/564d398e2ecf66cec00000a9/train/python

def type_of_triangle(a, b, c): 
  if not isinstance(a,int) or not isinstance(b,int) or not isinstance(c,int):
    return "Not a valid triangle"

  if ((a + b <= c) or (a + c <= b) or (b + c <= a)):
    return "Not a valid triangle"

  if (a == b == c):
    return "Equilateral"

  if (a == b or b == c or a == c):
    return "Isosceles"

  return "Scalene"
