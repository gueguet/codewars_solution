def mxdiflg(a1, a2):

  if (a1 == [] or a2 == []):
    return -1

  max_len = 0
  for w1 in a1:
    for w2 in a2:
      diff = abs(len(w2) - len(w1))
      if (diff > max_len):
        max_len = diff

  return max_len




s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]


print(mxdiflg(s1,s2))