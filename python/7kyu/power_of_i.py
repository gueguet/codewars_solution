# https://www.codewars.com/kata/5a97387e5ee396e70a00016d/train/python

def pofi(n):
  mod = n%4

  if (mod == 0):
    return '1'

  if (mod == 1):
    return 'i'

  if (mod == 2):
    return '-1'

  if (mod == 3):
    return '-i'


pofi(0)
pofi(1)
pofi(2)
pofi(3)
pofi(4)
pofi(5)


"""
* clever
def pofi(n):
    return ['1','i','-1','-i'][n%4]
"""
