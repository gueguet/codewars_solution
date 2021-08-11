# https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python

def remove_duplicate_words(s):
  seen = []

  for word in s.split(" "):
    if word not in seen:
      seen.append(word)

  print(seen)

  return " ".join(seen)


"""
* clever

def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split()))
"""
