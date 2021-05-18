# https://www.codewars.com/kata/609eee71109f860006c377d1/train/python

def last_survivor(letters, coords): 

  string_list = list(letters)
  print(string_list)

  for num in coords:
    string_list.pop(num)

  return "".join(string_list)

last_survivor('abc', [1, 1])

"""
* clever

def last_survivor(letters, coords): 
    l=[x for x in letters]
    [l.pop(x) for x in coords]
    return l[0]    
"""