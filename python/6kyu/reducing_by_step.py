# https://www.codewars.com/kata/56efab15740d301ab40002ee/train/python


import math

def gcdi(x,y):
    return math.gcd(x,y)

# lcd exit only in python 3.9+
def lcmu(a, b):
    return abs(a*b) // math.gcd(a, b)

def som(a, b):
    return (a+b)

def maxi(a, b):
    return max(a,b)

def mini(a, b):
    return min(a,b)
    
    
    
    
def oper_array(fct, arr, init): 
    res = [fct(init,arr[0])]
    for i in range(0,len(arr)-1):
        res.append(fct(res[i],arr[i+1]))
    return res


a = [ 18, 69, -90, -78, 65, 40 ]
r = [ 18, 87, -3, -81, -16, 24 ]
op = oper_array(som, a, 0)
