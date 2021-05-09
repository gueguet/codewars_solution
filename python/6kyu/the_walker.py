# https://www.codewars.com/kata/5b40b666dfb4291ad9000049/train/python

from math import cos, sin, acos, sqrt, radians, degrees, ceil, floor

def solve(a, b, c, alpha, beta, gamma):
    
    x_oc = a*cos(radians(alpha)) - b*sin(radians(beta)) - c*cos(radians(gamma)) 
    y_oc = a*sin(radians(alpha)) + b*cos(radians(beta)) - c*sin(radians(gamma)) 

    oc = sqrt(x_oc**2 + y_oc**2)
    toc = degrees(acos(x_oc/oc))

    print(oc)
    print(toc)

    min_toc = floor((toc - floor(toc)) * 60)
    sec_toc = floor((toc - floor(toc) - (min_toc/60)) * 3600)

    return ([round(oc), floor(toc), min_toc, sec_toc])


print(solve(12, 20, 18, 45, 30, 60))