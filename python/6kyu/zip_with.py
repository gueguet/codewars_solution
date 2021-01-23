# https://www.codewars.com/kata/5825792ada030e9601000782/train/python

def zip_with(fn,a1,a2):
  min_lenght = min(len(a1),len(a2))
  res = []
  for i in range (min_lenght):
    res.append(fn(a1[i],a2[i]))
  return res


if __name__ == "__main__":
  # zip_with(lambda a,b: a+b,[0,1,2,3,4,5],[6,5,4,3,2,1])
  zip_with(lambda a,b: a+b,[0,1,2,3,4  ],[6,5,4,3,2,1])


"""
quicker : use zip and map!
zip will simlply stop if the length of an array is 
smaller than the other! No error 

def zip_with(fn,a1,a2):
  return [fn(i,j) for i,j in zip(a1,a2)]

def zip_with(fn, a1, a2):
  return list(map(fn, a1, a2))
"""