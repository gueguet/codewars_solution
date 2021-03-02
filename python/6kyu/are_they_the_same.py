# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2):

  if (array1==None or array2==None):
    return False

  if (len(array1) != len(array2)):
    return False

  array1 = list(map(abs,array1))
  array2 = list(map(abs,array2))

  print(array1)
  print(array2)

  array1.sort()
  array2.sort()

  for i in range(len(array1)):
    if (array1[i]*array1[i] == array2[i]):
      pass
    else:
      return False

  return True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1,a2))

"""
* Clever solution :
return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2)
"""