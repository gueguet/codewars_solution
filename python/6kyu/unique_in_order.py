# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
    if (iterable == ''):
        return []
    previous = iterable[0]
    res = [previous]
    for element in iterable[1:]:
        if (element == previous):
            pass
        else:
            res.append(element)
        previous = element
    return res
