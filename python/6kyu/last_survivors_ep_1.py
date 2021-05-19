# https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651/train/python

from string import ascii_lowercase

def has_duplicate(string):
    for letter in string:
        if (string.count(letter) > 1):
            return True
    return False


def last_survivors(string):

    list_alpha = list(ascii_lowercase)
    res_list = []

    while(has_duplicate(string)):

        for letter in string:

          if (string.count(letter) > 1):

            if (letter == "z"):
              string = string.replace(letter,'', 1)
              string = string.replace("z", "a", 1)
              break

            else:
              string = string.replace(letter,'',1)
              string = string.replace(letter, list_alpha[list_alpha.index(letter)+1],1)
              break

    return string


"""
# * clever

import re

def last_survivors(string):
    change_letter = lambda s: chr((ord(s)-96)%26+97)
    reg = r"([a-z])(.*?)\1"
    print(re.findall(reg, string))
    while re.search(reg, string) is not None:
        string = re.sub(reg, lambda m: change_letter(m[1])+m[2], string, count=1)
    return string
"""


last_survivors("auualilr")
