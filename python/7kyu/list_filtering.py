# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/pytho

def filter_list(l):
    res = []
    for element in l:
        if (isinstance(element, int)):
            res.append(element)
    return res
    # return sorted(l, key = lambda x : isinstance(x,int) == True)

"""
One line
return [i for i in l if not isinstance(i, str)]
"""
