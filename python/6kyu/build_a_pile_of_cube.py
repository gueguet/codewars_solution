# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

def find_nb(m):
  tot = 0
  for n in range(1, m):
    tot += n**3
    if (tot == m):
      return(n)
    if (tot > m):
      return -1

find_nb(24723578342962)
