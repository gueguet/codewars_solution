# https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python

def goodVsEvil(good, evil):
  
  list_good_power = good.split()
  list_evil_power = evil.split()

  good_race_value = [1,2,3,3,4,10]
  evil_race_value = [1,2,2,2,3,5,10]

  good_power_res = 0
  evil_power_res = 0

  for i in range(len(list_good_power)):
    good_power_res += int(list_good_power[i])*good_race_value[i]

  for i in range(len(list_evil_power)):
    evil_power_res += int(list_evil_power[i])*evil_race_value[i]

  if (good_power_res > evil_power_res):
    return "Battle Result: Good triumphs over Evil"

  elif (good_power_res < evil_power_res):
    return "Battle Result: Evil eradicates all trace of Good"

  else:
    return "Battle Result: No victor on this battle field"

goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')


"""
* clever

good = sum([int(x)*y for x, y in zip(good.split(), points_good)])
evil = sum([int(x)*y for x, y in zip(evil.split(), points_evil)])
"""
