# https://www.codewars.com/kata/61e173ccbc916700267ef2ae/train/python

def triple_crown(receivers):
  max_receive = {0:""}
  max_touchdowns = {0:""}
  max_receiptions = {0:""}
  for player in receivers:
    if receivers[player["Receiving yards"]] > max_receive:
      max_receive[receivers[player["Receiving yards"]]] = player
    
triple_crown({'Cooper Kupp': {'Receiving yards': 1800, 'Receiving touchdowns': 18, 'Receptions': 117},
                                         'Justin Jefferson': {'Receiving yards': 1700, 'Receiving touchdowns': 17, 'Receptions': 116},
                                        'Davante Adams':{'Receiving yards': 1750, 'Receiving touchdowns': 16, 'Receptions': 113}})
