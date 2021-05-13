# https://www.codewars.com/kata/57057a035eef1f7e790009ef/train/python

import re

def one_punch(item): 
  return " ".join(re.sub("e|a|E|A",'',word) for word in sorted(item.split(" "))) if isinstance(item, str) and item else "Broken!"

  # word_list = sorted(item.split(" "))
  # res_list = []

  # for word in word_list:
  #   res_list.append(re.sub("ea"))

print(one_punch('Beard Knife Grenade Motorbike Hat'))