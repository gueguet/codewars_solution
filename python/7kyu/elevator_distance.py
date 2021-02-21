def elevator_distance(array):
  total_distance = 0
  current_floor = array[0]
  for floor in array[1::]:
    total_distance += abs(floor - current_floor)
    current_floor = floor

  return total_distance

elevator_distance([7,1,7,1])

"""
clever :
return sum(abs(a - b) for a, b in zip(array, array[1:]))
since array[1:] isd shorter --> generator will stop at the end of this array[1:]
"""