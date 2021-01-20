# https://www.codewars.com/kata/569218bc919ccba77000000b/train/python

import datetime

def date_nb_days(a0, a, p):

  money = a0
  num_days = 0
  while(money < a):
    money = money + ((p/36000)*money)
    num_days += 1

  s = '01/01/2016'
  res = datetime.datetime.strptime(s, '%m/%d/%Y') + datetime.timedelta(days=num_days)

  return "{}-{}-{}".format(res.year, str(res.month).zfill(2), str(res.day).zfill(2))

if __name__ == "__main__":
  print(date_nb_days(4254, 4761, 8))



#  d = datetime.datetime.strptime(s, '%m/%d/%Y') + datetime.timedelta(days=1)