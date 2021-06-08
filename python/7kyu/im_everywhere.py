# https://www.codewars.com/kata/6097a9f20d32c2000d0bdb98/train/python

vowels = "aeiouAEIOU"


def has_more_vowels(word):
    count_vowels = 0
    count_con = 0
    for letter in word:
        if letter in vowels:
            count_vowels += 1
        else:
            count_con += 1
    return count_vowels >= count_con


def i(word):
    if (not word or word[0].islower() or word[0].lower()=="i" or has_more_vowels(word)):
        return "Invalid word"
    return "i" + word


"""
* clever

def less_vowels(word):
    vowels = sum(c in "aeiou" for c in word.lower())
    return len(word) - vowels > vowels
"""