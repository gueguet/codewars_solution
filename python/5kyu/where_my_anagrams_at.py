# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

from collections import Counter

def anagrams(word, words):
    model_counter = Counter(word)

    res_anag = []
    for possible_ana in words:
        possible_counter = Counter(possible_ana)

        print(model_counter - possible_counter)

        if (model_counter == possible_counter):
            res_anag.append(possible_ana)

    return res_anag

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

"""
* clever...
return [item for item in words if sorted(item)==sorted(word)]
"""