# https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python

def what_century(year):
    if (year[2:4] == "00"):
        base = str(int(year[0:2]))
    else:
        base = str(int(year[0:2]) + 1)
    
    if (base == "11"):
        return "11th"
    
    if (base == "12"):
        return "12th"
    
    if (base == "13"):
        return "13th"
    
    if (base[-1] == "1"):
        base += "st"
        return base
        
    if (base[-1] == "2"):
        base += "nd"
        return base
        
    if (base[-1] == "3"):
        base += "rd"
        return base
    
    else:
        base += "th"
        
    return base

    
""" 

* clever

def what_century(year):
    n = (int(year) - 1) // 100 + 1
    return str(n) + ("th" if n < 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))
"""
