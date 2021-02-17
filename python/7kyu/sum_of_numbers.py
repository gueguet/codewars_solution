def get_sum(a,b):
  if (b>a):
    return sum([x for x in range(a,b+1)])
  else:
    return sum([x for x in range(b,a+1)])

print(get_sum(-1,2))