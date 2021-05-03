# https://www.codewars.com/kata/606b43f4adea6e00425dff42/train/python

def grid_map(inp, op):
    res = []
    for element_list in inp:
        res.append(list(map(op,element_list)))

    return res

num_grid = [[1,2,3,4], [5,6,7,8,9], [0,2,4]]
char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]

grid_map(num_grid, lambda x: x + 1)
