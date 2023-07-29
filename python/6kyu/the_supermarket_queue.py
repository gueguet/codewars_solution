# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/solutions/python

def is_empty(d):
    for key in d:
        if d[key] > 0:
            return False
    return True

def queue_time(customers, n):
    tot = 0
    d = {}
    for i in range(n):
        d[i] = 0
    
    d_is_empty = True # * a bit of cheating...

    while (len(customers) != 0) or (not d_is_empty):
        for key in d:
            if d[key] == 0 and len(customers) != 0:
                d[key] = customers.pop(0)
        for key in d:
            d[key] -= 1
        tot += 1
        d_is_empty = is_empty(d)

    return tot

print(queue_time([10,2,3,3], 2))

"""
* Smart --> we keep the quicker till at the beginning of the list, it's the one that can say if a new customer is accepted or not...

def queue_time2(customers, n):
    qn = [0] * n
    for c in customers:
        qn = sorted(qn)
        qn[0] += c
    return max(qn)

import heapq
def queue_time3(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)
"""