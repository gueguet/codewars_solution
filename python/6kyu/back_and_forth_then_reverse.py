# https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python

# ! too slow

# def arrange(s):
#   res = []
#   s_cop = s.copy()[::-1]

#   while(len(s_cop) > 1):
#     res.append(s_cop.pop())
#     s_cop = s_cop[::-1]
#     res.append(s_cop.pop())

#   if (len(s_cop) == 1):
#     res.append(s_cop.pop())

#   return res


def arrange(s):
  res = []
  n = len(s)

  if (n%2 == 0):
    for i in range((n//2)):
      if (i%2 == 0):
        res.append(s[i])
        res.append(s[-i-1])
      else:
        res.append(s[-i-1])
        res.append(s[i])
    return res

  else:
    for i in range((n//2)+1):
      if (i%2 == 0):
        res.append(s[i])
        res.append(s[-i-1])
      else:
        res.append(s[-i-1])
        res.append(s[i])
    return res[:-1]


print(arrange([1,2]))
# arrange([4, 3, 2])
# arrange([9, 7, -2, 8, 5, -3, 6, 5, 1])


"""
* clever --> create a deque is faster than doing copy, and pop() is also faster apparently

from collections import deque

def arrange(s):
    q=deque(s)
    return [q.pop() if 0<i%4<3 else q.popleft() for i in range(len(s))]

"""
