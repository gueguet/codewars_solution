# https://www.codewars.com/kata/5e67ce1b32b02d0028148094/train/python

# I've give up...

from itertools import product

def truth_table (boolean_function):
    name = 'f' if (b:=boolean_function.__name__) == '<lambda>' else b
    args = boolean_function.__code__.co_varnames
    
    title = f"{' '.join(args)}\t\t{name}({','.join(args)})\n\n"
    format_line = lambda i, f: f"{' '.join(map(str, i))}\t\t{int(f(*i))}\n"
    body = ''.join(format_line(l, boolean_function) \
                            for l in product([0,1], repeat=len(args)))
    return title + body
