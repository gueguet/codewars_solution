# https://www.codewars.com/kata/515decfd9dcfc23bb6000006

def is_valid_IP(strng):
  splited_list = strng.split(".")

  if (len(splited_list) != 4):
    return False

  for num in splited_list:
    if (num[0] == "0") and len(num) != 1:
      return False
    if (len(num) > 3):
      return False
    for digit in num:
      if not digit.isdigit():
        return False

  for num in splited_list:
    if (int(num) > 255):
      return False

  return True

is_valid_IP('12.255.56.1')


"""
* clever

def is_valid_IP(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4
"""
