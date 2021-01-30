# https://www.codewars.com/kata/5b7bd90ef643c4df7400015d/train/python

# the trick is not to generate all the possible combination...
# use ord() to check if it's possible to have a palindrome, we focus on that!

# ord() return the unicode of a string of length 1 (a character)
# ord(a) --> 97, ord(b) --> 98
# it compulsory to change each letter so difference need to be 2 -2 or 0

def solve(st):
  return all(True if ord(x) - ord(y) in [-2, 0, 2] else False for x, y in zip(st, st[::-1]))