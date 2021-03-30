# https://www.codewars.com/kata/55b42574ff091733d900002f

def friend(x):
    res = []
    for friend in x:
        if len(friend) == 4:
            res.append(friend)
    return res


"""
*! clever
return [f for f in x if len(f) == 4]
"""
