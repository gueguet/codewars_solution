# https://www.codewars.com/kata/5894134c8afa3618c9000146/train/python

def chess_board_cell_color(cell1, cell2):

    cell1_letter = cell1[0]
    cell1_num = cell1[1]

    cell2_letter = cell2[0]
    cell2_num = cell2[1]

    black_when_even = ["B","D","F","H"]
    black_when_odd = ["A","C","E","G"]

    cell1_color = ""
    cell2_color = ""

    if (int(cell1_num) % 2 == 0):
        if (cell1_letter in black_when_even):
            cell1_color = "black"
        else:
            cell1_color = "white"
    else:
        if (cell1_letter in black_when_odd):
            cell1_color = "black"
        else:
            cell1_color = "white"
            

    if (int(cell2_num) % 2 == 0):
        if (cell2_letter in black_when_even):
            cell2_color = "black"
        else:
            cell2_color = "white"
    else:
        if (cell2_letter in black_when_odd):
            cell2_color = "black"
        else:
            cell2_color = "white"


    if (cell1_color == cell2_color):
        return True
    else:
        return False


chess_board_cell_color("A1", "H3")



"""
* clever...

def chess_board_cell_color(a, b):
    return (ord(a[0]) + int(a[1])) % 2 == (ord(b[0]) + int(b[1])) % 2

def chess_board_cell_color(cell1, cell2):
    is_black = lambda c: (c[0] in "BDFH") ^ (c[1] in "1357")
    return is_black(cell1) == is_black(cell2)
"""
