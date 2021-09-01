# https://www.codewars.com/kata/5700c9acc1555755be00027e/train/python

def contain_all_rots(strng, arr):
  for i in range(len(strng)):
    rot = strng[i:] + strng[:i]
    if (rot in arr):
      pass
    else:
      return False
  return True

"""
* clever

return all(s[i:]+s[:i] in l for i in range(len(s)))
"""
