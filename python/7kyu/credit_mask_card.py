# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    res = ""
    if (len(cc) > 4):
        res = "#" * (len(cc) - 4) + cc[-4:]
        return res
    else:
        return cc

cc = 'SF$SDfgsd2eA'
r = maskify(cc)


"""
Clever solution 

enough :
return "#"*(len(cc)-4) + cc[-4:]

with fill 
return '{message:#>{fill}}'.format(message=cc[-4:], fill=len(cc))
"""