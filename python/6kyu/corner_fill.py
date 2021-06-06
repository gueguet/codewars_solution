# https://www.codewars.com/kata/60b7d7c82358010006c0cda5/train/python


def corner_fill(square):
  res = []
  count = 1 

  while (len(square) != 0):

    if (count % 2 == 1):
      for i in range(len(square[0])):
        res.append(square[0][i])
      square.pop(0)
      for j in range(len(square)):
        res.append(square[j][-1])
      for line in square:
        line.pop(-1)

    else:
      for j in range(len(square)):
        res.append(square[-j-1][-1])
      for line in square:
        line.pop(-1)
      for i in range(len(square[0])):
        res.append(square[0][-i-1])
      square.pop(0)

    count += 1

  return res



# A =  [[1,2,3],
#       [4,5,6],
#       [7,8,9]]


A =  [[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16]]


corner_fill(A)




"""
* clever --> use a new matrix that you fill and do not change the original one !!

def corner_fill(square):
    n = len(square)
    res = []
    
    for i in range(0, n):
        if i % 2 == 0: # even
            res.extend(square[i][0:n-i])
            for j in range(i+1, n):
                res.append(square[j][n-i-1])
        else: # odd
            for j in reversed(range(i+1, n)):
                res.append(square[j][n-i-1])
            res.extend(reversed(square[i][0:n-i]))
                
    return res

"""
