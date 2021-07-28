# https://www.codewars.com/kata/56f3a1e899b386da78000732

def partlist(arr):
  res = []
  for i in range(1,len(arr)):
    res.append((" ".join(arr[0:i])," ".join(arr[i:])))
  return(res)


partlist(["I", "wish", "I", "hadn't", "come"])
