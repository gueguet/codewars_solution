# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python

def duplicate_count(text):
    text = text.lower()
    res = 0
    seen = ""
    for char in text:
        if (text.count(char) > 1 and char not in seen):
            seen += char
            res += 1
    return res

duplicate_count("abcdeaB")


"""
* clever solution --> use set !

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
"""