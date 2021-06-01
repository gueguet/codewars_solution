# https://www.codewars.com/kata/583d10c03f02f41462000137/train/python

def max_sum(a, ranges):

  max_sum = -1000000 # * not clean
  for (i,j) in ranges:
    current_sum = sum(a[i:j+1])
    if current_sum > max_sum:
      max_sum = current_sum

  print(max_sum)
  return max_sum


"""
* clever

def max_sum(arr, ranges):
    return max( sum(arr[start:stop+1]) for start, stop in ranges )
"""
