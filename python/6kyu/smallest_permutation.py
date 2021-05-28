# https://www.codewars.com/kata/5fefee21b64cc2000dbfa875/train/python

import itertools

def min_permutation(n):
  if (n<0):
    is_neg = True
  else:
    is_neg = False

  n = abs(n)
  all_permutations = list(itertools.permutations(list(str(n))))
  min_found = int(''.join(all_permutations[0]))

  for permut in all_permutations:

    # no leading 0
    if (permut[0] == '0'):
      continue

    current_int = int(''.join(permut))
    if (current_int <= min_found):
      min_found = current_int

  if (is_neg == True):
    return -min_found
  else:
    return min_found



print(min_permutation(-4406891))


"""
* clever

def min_permutation(n):
    f = n < 0
    s = "".join(sorted(str(abs(n))))
    n = s.count("0")
    s = s.replace("0", "")
    return int(s[:1] + "0" * n + s[1:]) * (-1 if f else 1)
"""