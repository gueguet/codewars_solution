# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

def sort_array(source_array):

  res = []
  odd_array = sorted(list(filter(lambda x:x%2==1, source_array)))

  coutner = 0
  for el in source_array:
    if (el % 2 == 1):
      res.append(odd_array[coutner])
      coutner += 1
    else:
      res.append(el)

  return res


sort_array([5, 3, 2, 8, 1, 4])


"""
* clever

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

"""
