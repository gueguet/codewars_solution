# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python

def row_sum_odd_numbers(n):
  current_num = 1
  line = 1
  while (line < n):
    for i in range(line):
      current_num += 2
    line += 1

  res = 0

  for i in range(n):
    res += current_num
    current_num += 2

  return(res)    

row_sum_odd_numbers(3)