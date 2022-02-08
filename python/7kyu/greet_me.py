# https://www.codewars.com/kata/535474308bb336c9980006f2/train/python

def greet(name): 
    return "Hello {}{}!".format(name[0].upper(), name[1:].lower())


"""
* clever

def greet(name): 
    return f'Hello {name.title()}!'

def greet(name): 
    return f"Hello {name.capitalize()}!"
"""
