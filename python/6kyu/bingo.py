# https://www.codewars.com/kata/5af304892c5061951e0000ce/train/python

import numpy as np

def count_commun_digit(line1, line2):
  res = 0
  for digit in line1:
    if (digit) in line2:
      res += 1
  if ("FREE SPACE") in line2:
    res += 1
  return res

def bingo(card, numbers):

  numbers = [x[1:] for x in numbers]
  card = np.array(card[1:])

  for i in range(len(card)):
    if (count_commun_digit(numbers,list(card[i])) == 5):
      return True

  for i in range(len(card)):
    if (count_commun_digit(numbers,list(card[:,i])) == 5):
      return True

  diag1 = [] 
  for i in range(len(card)):
    diag1.append(card[i][i])

  diag2 = [] 
  for i in range(len(card)):
    diag2.append(card[i][-(i+1)])

  if (count_commun_digit(numbers,diag1) == 5):
    return True

  if (count_commun_digit(numbers,diag2) == 5):
    return True

  return False




card = [['B', 'I', 'N', 'G', 'O'],
 [1, 16, 31, 46, 61], 
 [3, 18, 33, 48, 63], 
 [5, 20, 'FREE SPACE', 50, 65], 
 [7, 22, 37, 52, 67], 
 [9, 24, 39, 54, 69]]

a = ['B1', 'I18', 'G52', 'O69']



print(bingo(card, a))

