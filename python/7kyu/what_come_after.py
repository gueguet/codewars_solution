# https://www.codewars.com/kata/590f5b4a7bbb3e246000007d/train/python

def comes_after(st, l): 
  res = ""
  for i in range(len(st)-1):
    if st[i].lower() == l.lower():
      if st[i+1].isalpha():
        res += st[i+1]
  return res


"""
* clever

def comes_after(st, letter):
    letter = letter.lower()
    return ''.join(b for a, b in zip(st.lower(), st[1:]) if a == letter and b.isalpha())  
"""
