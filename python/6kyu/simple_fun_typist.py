from string import ascii_letters 

def typist(s):
  count = 0
  caps_lock = False
  for letter in s:
    if letter in ascii_letters:
      count += 1
      if letter.isupper() and caps_lock == False:
        caps_lock = True
        count += 1
      if letter.islower() and caps_lock == True:
        count += 1
        caps_lock = False
  return count


"""
* clever

def typist(s):
    it = map(str.isupper, s)
    return len(s) + next(it) + sum(x.isupper() != y for x, y in zip(s, it))
"""
