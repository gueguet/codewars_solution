# https://www.codewars.com/kata/5b728f801db5cec7320000c7/train/python

import string

def solve(st, k):
    removed_letter = 0
    letter_count = 0

    while (removed_letter < k):
        letter = string.ascii_lowercase[letter_count]

        if (letter in st):
            st = st.replace(letter, '', 1)
            if (st == ''):
                return ''
            removed_letter += 1
        else:
            letter_count += 1

    return st

if __name__ == "__main__":
    solve('abracadabra', 6)


"""
nice solution :

def solve(st,k): 
    for l in sorted(st)[:k]:
        st=st.replace(l,'',1)
    return st
"""

