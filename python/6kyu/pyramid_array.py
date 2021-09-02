# https://www.codewars.com/kata/515f51d438015969f7000013/train/python

def pyramid(n):
  res = []
  for _ in range(1,n+1):
    res.append([1 for x in range(_)])
  return res

pyramid(3)


"""
* clever

return [[1]*x for x in range(1, n+1)]
"""
