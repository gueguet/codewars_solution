# https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/python

from collections import deque

def who_is_next(names, r):
    # your code
    queue = deque(names)

    i = 1
    while(i<r):
        name = queue.popleft()
        queue.append(name)
        queue.append(name)
        i += 1
    return queue[0]

print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951))


"""
! * Got time out first !!
abcde
aabbccddee
aaaabbbbccccddddeeee

note the triangle pattern:
By dividing by 2, you shift the pattern upwards.
The goal is to divide until you get the last row

minus 4 is used here instead of minus 5 people because you want the ceil of the quotient
using minus 5 and find the ceil of the division works too

# original solution by Spencer-Zhang, magnert, Yazan24

nNames = len(names)
while r > nNames:
    r = (r - nNames) // 2 + ((r - nNames) % 2) # equivalent of ceil((r-5)/2)
return names[r-1]
"""