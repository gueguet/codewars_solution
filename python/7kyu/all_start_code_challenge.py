# https://www.codewars.com/kata/5865a75da5f19147370000c7/train/python

def add_arrays(array1, array2): 
  
  if len(array1) != len(array2):
    raise "Input arguments are not of equal length"

  res = []
  for i in range(len(array1)):
    res.append(array1[i] + array2[i])
  return res


"""
* clever --> use zip !!!

def add_arrays(arr1, arr2): 
    if len(arr1) != len(arr2):
        raise "Input arguments are not of equal length"
    return [x + y for x, y in zip(arr1, arr2)]
"""
