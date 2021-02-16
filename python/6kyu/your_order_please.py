# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

import re

def order(sentence):
  if sentence == "":
    return ""

  dict_res = {}
  len_total = 0

  for word in sentence.split(" "):
    extract_number = re.findall(r'\d+',word)
    dict_res[extract_number[0]] = word

  res_string = ""

  for i in range(1,len(dict_res)+1):
    res_string += dict_res[str(i)] + " "

  return res_string[:-1]

order("is2 Thi1s T4est 3a")

  

