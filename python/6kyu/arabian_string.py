# https://www.codewars.com/kata/525821ce8e7b0d240b002615/train/python

def camelize(str_):

  for char in str_:
    if not char.isalnum():
      str_ = str_.replace(char, " ")

  word_list = str_.split(" ")
  
  res = ""

  for word in word_list:
    if (len(word) > 0):
      res += word[0].upper() + word[1:].lower()

  return res

camelize("example name")
  
"""
* clever 
return "".join([w.capitalize() for w in re.split("\W|_", s)])
"""