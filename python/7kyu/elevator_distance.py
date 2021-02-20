def elevator_distance(array):
  total_distance = 0
  current_floor = array[0]
  for floor in array[1::]:
    total_distance += abs(floor - current_floor)
    current_floor = floor

  return total_distance

elevator_distance([7,1,7,1])

