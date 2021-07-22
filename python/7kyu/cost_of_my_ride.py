# https://www.codewars.com/kata/586430a5b3a675296a000395/train/python

size_charge = {
  "economy": 0,
  "medium": 10,
  "full-size": 15
}

def insurance(age, size, num_of_days):
  cost = 0

  if (num_of_days < 0):
    return 0

  if size in size_charge:
    cost += (size_charge[size] * num_of_days)
  else:
    cost += (15 * num_of_days)

  if (age < 25):
    cost += (10*num_of_days)

  cost += num_of_days * 50

  return cost
