def averages(arr):

  if (arr == None):
    return []

  if (arr == [] or arr==[0] or arr==[1]):
    return []

  res = []

  for i in range(len(arr)-1):
    avg = (arr[i] + arr[i+1]) / 2
    res.append(avg)

  return res
