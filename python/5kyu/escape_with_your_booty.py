# https://www.codewars.com/kata/5b0560ef4e44b721850000e8/train/python

def navy_is_close(my_ship, list_navy):
  for navy in list_navy:
    if ((navy[0] - my_ship[0] == 0) and  (abs(navy[1] - my_ship[1]) == 1)):
      return True
    if ((navy[1] - my_ship[1] == 0) and  (abs(navy[0] - my_ship[0]) == 1)):
      return True
    if ((navy[1] - my_ship[1] == 1) and  (abs(navy[0] - my_ship[0]) == 1)):
      return True
      
  return False

def check_course(sea_map):
  list_navy = []
  
  for i in range(len(sea_map)):
    for j in range(len(sea_map[0])):
      if (sea_map[i][j] == "X"):
        my_ship = [i,j]
      if (sea_map[i][j] == "N"):
        if (i == 0):
          list_navy.append([i,j,"down"])
        else:
          list_navy.append([i,j,"up"])

  for i in range(len(sea_map[0])-1):

    if (navy_is_close(my_ship, list_navy) == True):
      return False

    for navy in list_navy:
      if navy[2] == "down":
        navy[0] += 1 
      else:
        navy[0] -= 1
      if navy[0] == 0 and navy[2] == "up":
        navy[2] = "down"
      if navy[0] == (len(sea_map)-1) and navy[2] == "down":
        navy[2] = "up"

    if (navy_is_close(my_ship, list_navy) == True):
      return False

    my_ship[1] += 1

  if (navy_is_close(my_ship, list_navy) == True):
    return False

  return True


sea_map = ['X000P', 
           '00000', 
           '0000D', 
           '00000', 
           '00000', 
           '00000', 
           '0000N']

# sea_map = ['000NN00NNN0', 
#            '00000000000', 
#            '00000000000', 
#            '00000000000', 
#            '00000000000', 
#            '00000000000', 
#            '00000000000', 
#            '00000000000', 
#            '00000000000', 
#            '00000000000', 
#            '000DD00DDD0', 
#            'X000000000P', 
#            '00000NN0000']

print(check_course(sea_map))

