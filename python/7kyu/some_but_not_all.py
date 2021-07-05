# https://www.codewars.com/kata/60dda5a66c4cf90026256b75/train/python

def some_but_not_all(seq, pred): 
  
  validation_couter = 0

  for el in seq:
    if pred(el):
      validation_couter += 1

  if validation_couter == 0:
    return False
  
  if validation_couter == len(seq):
    return False

  return True


"""
* Clever

def some_but_not_all(seq, pred): 
  return any(map(pred, seq)) and not all(map(pred, seq))
"""
