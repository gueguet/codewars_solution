# https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

def cakes(recipe, available):
    possible_int = []
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        else:
            possible_int.append(available[ingredient] // recipe[ingredient])
    return(min(possible_int))


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))


"""
* one line solution :
return min(available.get(k, 0)/recipe[k] for k in recipe) 
* .get(k, 0) --> will return 0 if the key does not exist !
"""