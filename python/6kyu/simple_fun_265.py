# https://www.codewars.com/kata/59128363e5bc24091a00006f/train/python

from string import ascii_lowercase

def the_janitor(word):

  res = []
  word = list(word)

  for i in range(len(list(ascii_lowercase))):
    
    counter = 0
    for j in range(len(word)):

      if word[j] == ascii_lowercase[i]:
        if counter == 0:
          counter = 1
          pos_first_seen = j
        else:
          counter = j+ 1 - pos_first_seen

    res.append(counter)

  return res

the_janitor("abacaba")


"""
* clever --> use rdindex() !!

def the_janitor(word):
    return [word.rindex(c) - word.index(c) + 1 if c in word else 0 for c in alphabet]
"""
