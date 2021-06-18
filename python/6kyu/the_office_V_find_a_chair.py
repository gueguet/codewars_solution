# https://www.codewars.com/kata/57f6051c3ff02f3b7300008b

def meeting(rooms, number):

  tot_chairs = 0
  taken_chairs = []

  if (number == 0):
    return "Game On"

  for room in rooms:
    available_chair = room[1] - room[0].count('X')
    taken_chairs.append(0)
    for _ in range(available_chair):
      taken_chairs[-1] += 1
      tot_chairs += 1
      if (tot_chairs == number):
        return taken_chairs
      else:
        pass

  return "Not enough!"

  

meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4)
