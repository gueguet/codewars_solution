# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
  if (s == ''):
    return False
  res = "#"
  splitted = s.split(" ")
  for word in splitted:
    if (word != ''):
      word = word.lower()
      res += word[0].upper() + word[1:]
  if (len(res) < 140):
    return res
  else:
    return False
  


generate_hashtag('Codewars      ')


"""
* clever --> .title() method

def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False
"""
