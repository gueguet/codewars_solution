# https://www.codewars.com/kata/60a2d7f50eee95000d34f414/train/python

import numpy as np

def last_survivors(arr, nums):

  numpy_arr = []
  for line in arr:
    numpy_arr.append(list(line))
  numpy_arr = np.array(numpy_arr)


  for i in range(len(nums)):

    current_col =  numpy_arr[:,i][::-1]
    
    for j in range(len(current_col)):
      if (nums[i] != 0 and current_col[j] != " "):
        current_col[j] = " "
        nums[i] -= 1

  res = ""
  for line in numpy_arr:
    for char in line:
      if (char != " "):
        res += char

  return res


# test_array = ['to   ','  tal','it   ','  ari','an   ','  ism']
# nums = [7,6,4,2,1]

test_array = ['abc','   ',' a ']
nums = [0,4,1]

# test_array = ['help us we are dying']
# nums = [2,0,2,1,2,0,2,1,2,0,2,1,2,0,2,1,2,0,2,1]

# test_array = ['zj','zj']
# nums = [9,0]

last_survivors(test_array, nums)


"""
* clever

def last_survivors(arr, nums):
    return ''.join(map(shrink, zip(*arr) ,nums))

def shrink(col,n):
    return ''.join(col).replace(' ','')[:-n or len(col)]
"""
