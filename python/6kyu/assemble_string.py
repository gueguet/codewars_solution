# https://www.codewars.com/kata/6210fb7aabf047000f3a3ad6/train/python

def assemble(arr):
    if len(arr) == 0:
        return ''
    
    res = ['#' for i in range(len(arr[0]))]
    
    for ind in range(len(res)):
        if (res[ind] == '#'):
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if arr[i][j] != "*":
                        res[j] = arr[i][j] 
                
    return "".join(res) 

print(assemble(['H*llo, W*rld!', 'Hel*o, *or*d!', '*ello* World*']))


"""
* clever

def assemble(arr):
    return ''.join(c.discard('*') or c and c.pop() or '#' for c in map(set, zip(*arr)))
    
--------------------------------------------------------------------------------------
    
def assemble(input):
    result = list(input[0]) if input else []
    
    for i in input:
        for j, k in enumerate(i):
            result[j] = k if result[j] == '*' else result[j]
    
    return ''.join(result).replace('*', '#')
"""
