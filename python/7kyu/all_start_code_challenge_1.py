# https://www.codewars.com/kata/5863f97fb3a675d9a700003f

def sum_ppg(playerOne, playerTwo):
  res = playerOne['ppg'] + playerTwo['ppg']
  return res


iverson = { 'team': '76ers', 'ppg': 11.2 }
jordan =  { 'team': 'bulls', 'ppg': 20.2 }


print(sum_ppg(iverson, jordan))
