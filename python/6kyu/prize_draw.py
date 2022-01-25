# https://www.codewars.com/kata/5616868c81a0f281e500005c/train/python

import string

alpha_dict = dict(zip(string.ascii_lowercase, [x for x in range(1,27)]))

def get_value_name(name):
    sum = len(name)
    for letter in name:
        sum += alpha_dict[letter]
    return sum
    
def rank(st, we, n):
    
    if not st:
        return "No participants"
    
    st = st.split(",")
    
    if n > len(st):
        return "Not enough participants"
    
    res_dict = {}
    for ind, name in enumerate(st):
        name = name.lower()
        
        if (we[ind] * get_value_name(name)) not in res_dict:
            res_dict[we[ind] * get_value_name(name)] = [name]
            
        else:
            res_dict[we[ind] * get_value_name(name)].append(name)
            res_dict[we[ind] * get_value_name(name)].sort()

    sorted_res = dict(sorted(res_dict.items(), reverse=True))
    
    i = 1
    for key in sorted_res:
        for el in sorted_res[key]:
            if (i == n):
                return el.capitalize()
            i += 1 
            


# rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)
# rank("Lagon,Lily", [1, 5], 2)
# rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2)
# rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4)
rank("William,Willaim,Olivia,Olivai,Lily,Lyli", [1, 1, 1, 1, 1, 1], 4)


"""
* clever

def rank(st, we, n):
    if not st:
        return "No participants"
    
    if n>len(we):
        return "Not enough participants"

    name_score = lambda name,w: w*(len(name)+sum([ord(c.lower())-96for c in name]))
    
    scores= [name_score(s,we[i]) for i,s in enumerate(st.split(','))]
    
    scores = list(zip(st.split(','),scores))    
    
    scores.sort(key=lambda x: (-x[1],x[0]))
    
    return scores[n-1][0]


-------------------------------------------------------


def win_num(name, weight):
    return (len(name) + sum(ord(c)-96 for c in name.lower())) * weight

def rank(st, we, n):
    if not st:      return "No participants"
    elif n>len(we): return "Not enough participants"
    else:           return sorted((-win_num(s,w),s) for s,w in zip(st.split(","), we))[n-1][1]
"""

