# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python


"""
* Timeout problem...
def scramble(s1, s2):
    for char in s2:
        if s2.count(char) > s1.count(char):
            return False
    return True
"""

from collections import Counter

def scramble(s1,s2):
    cnt = Counter(s1)
    cnt.subtract(Counter(s2))
    return (all(e >= 0 for e in cnt.values()))

scramble('scriptjavx', 'javascript')

"""
* clever

def scramble(s1,s2):
for c in set(s2):
    if s1.count(c) < s2.count(c):
        return False
return True

* very interesting
def scramble(s1,s2):
    print(Counter(s2))
    print(Counter(s1))
    print(Counter(s2)- Counter(s1))
    return len(Counter(s2)- Counter(s1)) == 0
"""