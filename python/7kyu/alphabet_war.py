def alphabet_war(fight):
  left_dict = dict(zip(['w','p','b','s'],[4,3,2,1]))
  right_dict = dict(zip(['m','q','d','z'],[4,3,2,1]))

  left_score = 0
  right_score = 0

  for char in fight:
    if (char in left_dict):
      left_score += left_dict[char]
    elif (char in right_dict):
      right_score += right_dict[char]
    else:
      pass

  if (left_score > right_score):
    return 'Left side wins!'
  elif (left_score == right_score):
    return "Let's fight again!"
  else:
    return 'Right side wins!'