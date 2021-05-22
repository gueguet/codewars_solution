# https://www.codewars.com/kata/59a96d71dbe3b06c0200009c/train/python

def generate_shape(integer):

    res = ''

    for i in range(integer):
        res += '+'*integer
        res += '\n'

    return res[:-1]


generate_shape(3)
