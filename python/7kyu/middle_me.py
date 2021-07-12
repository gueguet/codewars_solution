# https://www.codewars.com/kata/59cd155d1a68b70f8e000117/train/python

def middle_me(N, X, Y): 
  res = ""
  if (N % 2 == 1):
    return X
  for i in range(N//2):
    res += Y
  res += X
  for i in range(N//2):
    res += Y
  return res
