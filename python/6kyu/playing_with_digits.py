# https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python

def dig_pow(n, p):
  target = str(n)
  total = sum([int(target[i]) ** (p + i) for i in range(len(target))])
  return total / n if (total % n) == 0 else -1