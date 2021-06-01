# https://www.codewars.com/kata/58a6568827f9546931000027/train/python

def number_of_carries(a, b):
  
  count_carry = 0
  current_carry = 0

  a = str(a)
  b = str(b)

  len_a = len(a)
  len_b = len(b)

  while (len_a != 0 or len_b != 0):

    x = 0;
    y = 0;

    if (len_a > 0):
        x = int(a[len_a - 1]) + int('0');
        len_a -= 1;
      
    if (len_b > 0):
        y = int(b[len_b - 1]) + int('0');
        len_b -= 1;

    current_sum = x + y + current_carry;

    if (current_sum >= 10):
      count_carry += 1
      current_carry = 1

    else:
      current_carry = 0

  return count_carry



number_of_carries(543,3456)
