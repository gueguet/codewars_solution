# https://www.codewars.com/kata/589433358420bf25950000b6/train/python

def chess_knight(cell):

  horse_letter = cell[0]
  horse_num = int(cell[1])

  if (horse_num <= 1):
    if (horse_letter == "A"):
      return 2
    if (horse_letter == "B"):
      return 3
    if (horse_letter == "G"):
      return 2
    if (horse_letter == "H"):
      return 3
