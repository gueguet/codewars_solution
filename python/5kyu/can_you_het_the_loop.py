# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

def loop_size(node):
    
    seen = []
    
    tail = 0
    loop_size = 0
    
    current_node = node
    
    for i in range(100000): # ! not clean at all...
        seen.append(current_node.__repr__())
        current_node = current_node.next
        
        if (current_node.__repr__() in seen): 
            break
            
    return len(seen) - seen.index(current_node.__repr__())
         

"""
* same method but no timeout...

def loop_size(n):
    l = []
    while not n in l:
        l.append(n)
        n = n.next
    return len(l) - l.index(n)
"""