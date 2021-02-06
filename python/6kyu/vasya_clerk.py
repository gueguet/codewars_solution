# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/train/python

def tickets(people):

  vasya_change = {"25":0, "50":0, "100":0}

  for people_money in people:

    if (people_money == 25):
      vasya_change["25"] += 1

    elif (people_money == 50):
      if (vasya_change["25"] >= 1):
        vasya_change["25"] -= 1
        vasya_change["50"] += 1
      else:
        return "NO" 
    
    elif (people_money == 100):
      if (vasya_change["50"] >= 1 and vasya_change["25"] >= 1):
        vasya_change["50"] -= 1
        vasya_change["25"] -= 1
      elif (vasya_change["25"] >= 3):
        vasya_change["25"] -= 3
        vasya_change["100"] += 1
      else:
        return "NO"

    else:
      return "Error..."

  return "YES"



tickets([25, 25, 50])