# https://www.codewars.com/kata/594adadee075005308000122/train/python

def even_and_odd(n): 
  ne = "0"
  no = "0"
  for digit in str(n):
    print(digit)
    if (int(digit) % 2 == 0):
      ne += digit
    else:
      no += digit
  return (int(ne),int(no))


even_and_odd(4628)


"""
* clever

def even_and_odd(n): 
    ne = "".join(x for x in str(n) if x in "02468")
    no = "".join(y for y in str(n) if int(y) % 2)
    return tuple(0 if not a else int(a) for a in (ne, no))
"""
