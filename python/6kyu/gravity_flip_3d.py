# https://www.codewars.com/kata/5f849ab530b05d00145b9495/train/python

import numpy as np


def flip(d, a):
  res = []

  if (d == "R"):
    for line in a:
      res.append(sorted(line))

  if (d == "L"):
    for line in a:
      res.append(sorted(line, reverse=True))

  if (d == "D"):
    a = np.array(a)
    a = np.transpose(a)
    for line in a:
      res.append(sorted(line))
    res = np.transpose(res).tolist()

  if (d == "U"):
    a = np.array(a)
    a = np.transpose(a)
    for line in a:
      res.append(sorted(line, reverse=True))
    res = np.transpose(res).tolist()

  return res


box = [[1, 3, 2],
        [4, 5, 1],
        [6, 5, 3],
        [7, 2, 9]]


print(flip('U', box))


"""
* clever (super clever...)

import numpy as np

dir = {
    'L': lambda a: np.sort(a)[:, ::-1],
    'R': lambda a: np.sort(a),
    'U': lambda a: np.sort(a, axis=0)[::-1, :],
    'D': lambda a: np.sort(a, axis=0)
}

def flip(d, a):
    return dir[d](np.array(a)).tolist()

"""
