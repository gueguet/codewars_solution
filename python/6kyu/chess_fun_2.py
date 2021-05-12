# https://www.codewars.com/kata/589425c2561a35dd1a0000a2/train/python

def bishop_and_pawn(bishop, pawn):

  letter_dict = dict(zip(["a","b","c","d","e","f","g","h"],[x for x in range(1,9)]))

  print(letter_dict)

  bishop_letter = bishop[0]
  bishop_num = int(bishop[1])

  pawn_letter = pawn[0]
  pawn_num = int(pawn[1])

  diff_letter = abs(letter_dict[bishop_letter] - letter_dict[pawn_letter])
  diff_num = (abs(bishop_num - pawn_num))

  if (diff_letter == diff_num):
    return True

  else:
    return False


bishop_and_pawn("a1","c3")


"""
* clever --> think about ord !!
def bishop_and_pawn(bishop, pawn):
    return abs(ord(bishop[0]) - ord(pawn[0])) == abs(int(bishop[1]) - int(pawn[1]))
"""