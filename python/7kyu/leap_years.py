# https://www.codewars.com/kata/526c7363236867513f0005ca/train/python

def isLeapYear(year):
  if (year % 400 == 0):
    return True
  
  if (year % 100 == 0):
    return False

  if (year % 4 == 0):
    return True

  return False
