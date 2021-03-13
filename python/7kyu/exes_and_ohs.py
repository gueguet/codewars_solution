# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

def xo(s):
    s = s.lower()
    num_x = s.count("x")
    num_o = s.count("o")

    if (num_o != num_x):
        return False

    return True

