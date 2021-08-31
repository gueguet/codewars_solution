# https://www.codewars.com/kata/588e2a1ad1140d31cb00008c

def generate_pairs(m, n):
  res = []
  for i in range(m,n+1):
    for j in range(i,n+1):
      res.append((i,j))
  return res


generate_pairs(2,4)

"""
* clever

return [(x, y) for x in range(m, n + 1) for y in range(m, n + 1) if x <= y]
"""
