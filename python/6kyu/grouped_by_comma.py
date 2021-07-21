# https://www.codewars.com/kata/5274e122fc75c0943d000148/train/python

def group_by_commas(n):
  n = str(n)
  tot_len = len(n)

  res = ""
  
  if (tot_len % 3 != 0):
    for i in range(tot_len % 3):
      res += n[i]
    if (tot_len > tot_len % 3):
      res += ","

  count = 0
  for j in range(tot_len % 3, tot_len):
    if (count == 3):
      res += "," + n[j]
      count = 1
    else:
      res += n[j]
      count += 1

  return res


group_by_commas(100)
group_by_commas(10000)
# group_by_commas(35235235)


"""
clever

def group_by_commas(n):
    return '{:,}'.format(n)
"""
