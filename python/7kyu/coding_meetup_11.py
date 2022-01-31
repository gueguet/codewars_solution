# https://www.codewars.com/kata/582ba36cc1901399a70005fc/train/python

from statistics import mean

def get_average(lst):
  ages = []
  for row in lst:
    ages.append(row["age"])
  return round(mean(ages))



"""
* clever 

return round(sum(x["age"] for x in lst) / len(lst))
"""
