# https://www.codewars.com/kata/56e7d40129035aed6c000632/train/python

def easyline(n):
    a = [[1]]
    for size in range(2,n+2):
        tmp = [1]*size
        for i in range(1,size-1):
            tmp[i] = a[-1][i-1] + a[-1][i]
        a.append(tmp)
    return sum(x*x for x in a[-1])