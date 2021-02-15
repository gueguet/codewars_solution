# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

import string

def stock_list(listOfArt, listOfCat):
  if (listOfArt == [] or listOfCat == []):
    return ""

  res_dict = dict(zip(string.ascii_uppercase,[0]*26))

  for art in listOfArt:
    splitted_art = art.split(" ")
    letter, value = splitted_art[0], splitted_art[1]
    res_dict[letter[0]] += int(value)

  res = ""
  for wanted_letter in listOfCat:
    res += "({} : {}) - ".format(wanted_letter,res_dict[wanted_letter])

  print(res[:-3])
  return res[:-3]

if __name__ == "__main__":
  b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
  c = ["A", "B"]
  stock_list(b, c)


"""quick solution : 
from collections import Counter

def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1
    cnt = Counter()
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)
"""