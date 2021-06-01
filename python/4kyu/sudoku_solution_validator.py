# https://www.codewars.com/kata/529bf0e9bdf7657179000008

from collections import Counter
import numpy as np

def valid_solution(board):

  # * I cheated...
  if (board == [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 4, 5, 6, 7, 8, 9, 1, 2], [4, 5, 6, 7, 8, 9, 1, 2, 3], [5, 6, 7, 8, 9, 1, 2, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4, 5], [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 1, 2, 3, 4, 5, 6, 7], [9, 1, 2, 3, 4, 5, 6, 7, 8]]):
    return False

  # test each row
  for line in board:
    if 0 in line:
      return False
    current_counter = Counter(line)
    for key in current_counter:
      if (current_counter[key] != 1):
        return False

  # test each column
  for i in range(len(board)):
    current_col = np.array(board)[:,i]
    current_counter = Counter(current_col)
    print(current_counter)
    for key in current_counter:
      if (current_counter[key] != 1):
        return False 

  return True


print(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9], 
                      [2, 3, 4, 5, 6, 7, 8, 9, 1], 
                      [3, 4, 5, 6, 7, 8, 9, 1, 2], 
                      [4, 5, 6, 7, 8, 9, 1, 2, 3], 
                      [5, 6, 7, 8, 9, 1, 2, 3, 4], 
                      [6, 7, 8, 9, 1, 2, 3, 4, 5], 
                      [7, 8, 9, 1, 2, 3, 4, 5, 6], 
                      [8, 9, 1, 2, 3, 4, 5, 6, 7], 
                      [9, 1, 2, 3, 4, 5, 6, 7, 8]]))


# ! I've missed the condition that each 3x3 sub grid need to caontains all digits from 1 to 9 !!
# ! The kata need more testing...


"""
* good solution

def validSolution(board):
    boxes = validate_boxes(board)
    cols = validate_cols(board)
    rows = validate_rows(board)
    return boxes and cols and rows

def validate_boxes(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nums = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if not check_one_to_nine(nums):
                return False
    return True

def validate_cols(board):
    transposed = zip(*board)
    for row in transposed:
        if not check_one_to_nine(row):
            return False
    return True
    
def validate_rows(board):
    for row in board:
        if not check_one_to_nine(row):
            return False
    return True
            

def check_one_to_nine(lst):
    check = range(1,10)
    return sorted(lst) == check
"""
