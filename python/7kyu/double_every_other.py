# https://www.codewars.com/kata/5809c661f15835266900010a/train/python

def double_every_other(lst):
    res = []
    for ind,x in enumerate(lst):
        if (ind%2 != 0):
            res.append(2*x)
        else:
            res.append(x)
    return res

    # return list(map(lambda x:x**2 if (x%2==0) else x, lst))


"""
# * clever

return [x * 2 if i % 2 else x for i, x in enumerate(l)]
"""
