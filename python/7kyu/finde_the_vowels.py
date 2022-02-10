# https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python

def vowel_indices(word):
    
    res = []
    
    vowels = "aeiouyAEIOUY"
    counter = 1
    
    for letter in word:
        if letter in vowels:
            res.append(counter)
        counter += 1
    
    return res
 
 
vowel_indices("osef")


"""
*  clever

def vowel_indices(word):
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']
"""
