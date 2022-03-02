# https://www.codewars.com/kata/5748838ce2fab90b86001b1a/train/python

from math import pi

def square_area(A):
    total_perim = 4 * A
    rayon =  total_perim / (2 * pi)
    square = rayon ** 2
    return round(square, 2) 
