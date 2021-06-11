# https://www.codewars.com/kata/60908bc1d5811f0025474291/train/python


def find_squares(num):
  
  perfect_square_list = [x*x for x in range(10000)]

  for i in range(len(perfect_square_list)):
    if (perfect_square_list[i+1] - perfect_square_list[i] == num):
      return "{}-{}".format(perfect_square_list[i+1],perfect_square_list[i])

  return ""

find_squares(16)

"""
* clever

def find_squares(n):
    m = (n-1)//2
    return f'{(m+1)**2}-{m**2}'
"""
