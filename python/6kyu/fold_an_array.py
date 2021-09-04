# https://www.codewars.com/kata/57ea70aa5500adfe8a000110/train/python

def lets_fold(array):
  res = []
  n = len(array)

  for i in range(n//2):
    res.append(array[i] + array[-i-1])
  if (n % 2 != 0):
    res.append(array[n//2])

  return res


def fold_array(array, runs):
  res = array
  for _ in range(runs):
    res = lets_fold(res)
  return res


"""
* clever

def fold_array(array, runs):
    worker = array[:]
    for r in range(runs):
        for i in range(len(worker)/2):
            worker[i] += worker.pop()
    return worker
"""
