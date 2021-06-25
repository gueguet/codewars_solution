# https://www.codewars.com/kata/5d68d05e7a60ba002b0053f6
import math 

def bonus(arr, s):

  res = []

  multiplier = 1
  for i in range(1,len(arr)):
    multiplier += arr[0]/arr[i]

  res.append(round(s/multiplier))

  for i in range(1,len(arr)):
    res.append(round((arr[0]/arr[i])*res[0]))

  return res

bonus([18, 15, 12], 851)


"""
* clever

s=s/(sum(1/n for n in arr))
return [round(s/n) for n in arr]

"""
