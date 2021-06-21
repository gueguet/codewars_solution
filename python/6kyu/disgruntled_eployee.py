# https://www.codewars.com/kata/541103f0a0e736c8e40011d5/train/python

def off(n):

  switch = [1 for i in range (n)]

  for i in range(1,n+1):
    for j in range(i-1,n,i):
      if (switch[j] == 1):
        switch[j] = 0
      else:
        switch[j] = 1

  res = []
  for i in range(len(switch)):
    if (switch[i] == 0):
      res.append(i+1)

  return res


off(4)


"""
* clever... mhh why not, less funny

def off(n):
    return [i * i for i in range(1, int(n ** 0.5) + 1)]
"""
