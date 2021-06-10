# https://www.codewars.com/kata/573992c724fc289553000e95/train/python

# ! not finished...

def smallest(n):

  print(n)
  n = str(n)
  res = ""

  if (n.count("0") == 0):
    min_val = min(n)
    min_ind = n.index(min_val)

    if (n.index(max(n)) == 0):
      res += n[1:] + n[0]
      return [int(res), 0, len(n)-1]

    counter = 0
    while (min_ind == 0):
      counter += 1
      res += n[counter-1]
      n = n[counter:]
      min_val = min(n)
      min_ind = n.index(min_val)

    res += min_val + n[:min_ind] + n[min_ind+1:]
    return[int(res), min_ind+counter, counter]


  elif (n.count("0") == 1):
    min_ind = n.index("0")
    res = n[:min_ind] + n[min_ind+1:]

    if min_ind == 1:
      return[int(res), 0, min_ind]
    else:
      return[int(res), min_ind, 0]


  else:
    print("mazette")
    min_ind = n.rindex("0")
    res = n[:min_ind] + n[min_ind+1:]
    return [int(res), min_ind, 0]


smallest(187863002809)
smallest(40164208904583763)


# idea --> find min max with max distance between ?


# [119989884756, 4, 1] should equal [119989884756, 4, 0]
