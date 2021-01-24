# https://www.codewars.com/kata/534d0a229345375d520006a0/train/python

def power_of_two(n):
  if (n==0):
    return False
    
  while(n != 1):
    if (n%2 == 0):
      n = n//2 # be careful we want an int 
    else:
      return False
    
  return True



"""
https://stackoverflow.com/questions/8556206/what-does-mean-in-python

def power_of_two(x):
if x == 0:
    return False
elif x & x-1 != 0:
    return False
else:
    return True
"""