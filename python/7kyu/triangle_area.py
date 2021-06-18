# https://www.codewars.com/kata/59bd84b8a0640e7c49002398/train/python

def t_area(t_str):
  splited = t_str.splitlines()
  return ((len(splited) - 2) ** 2 / 2)


t_area('\n.\n. .\n. . .\n. . . .\n. . . . .\n')
