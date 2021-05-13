# https://www.codewars.com/kata/5f70c883e10f9e0001c89673/train/python

def flip(d, a):

    if (d == "R"):
      a.sort()
      return a

    if (d == "L"):
      a.sort(reversed)
      return a


print(flip('R', [3, 2, 1, 2]))


"""
* clever
return sorted(a, reverse=d=='L')
"""