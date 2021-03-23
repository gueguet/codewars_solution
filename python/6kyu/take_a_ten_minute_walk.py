# https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

def is_valid_walk(walk):
    if (len(walk) != 10):
        return False
    
    horiz = 0
    verti = 0
    horiz_dir = {
        "w":-1,
        "e":1,
    }
    verti_dir = {
        "s":-1,
        "n":1
    }

    for dir in walk:
        if dir in horiz_dir:
            horiz += horiz_dir[dir]
        else:
            verti += verti_dir[dir]

    print(horiz)        
    print(verti)

    if (horiz == 0 and verti == 0):
        return True 

    return False       



"""
* clever :
just count the letter...
return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
"""
