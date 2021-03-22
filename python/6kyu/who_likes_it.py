# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    if (len(names) == 0):
        return "no one likes this"
    elif (len(names) == 1):
        return "{} likes this".format(names[0])
    elif (len(names) == 2):
        return "{} and {} like this".format(names[0], names[1])
    elif (len(names) == 3):
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], len(names) - 2)

"""
* interesting answer

def likes(names):
formats = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
n = len(names)
return formats[min(n,4)].format(*names, others=n-2)
        
"""