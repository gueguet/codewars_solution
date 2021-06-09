# https://www.codewars.com/kata/5b6ee22ac5cc71833f0010d7/train/python

def kaprekar_split(n):
  squared_num = str(n**2)

  if (n==1):
    return 0

  for i in range(1,len(squared_num)):
    if (int(squared_num[:i]) + int(squared_num[i:]) == n):
      return i

  return -1

kaprekar_split(2223)
