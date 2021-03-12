# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    #your code here
    seen = []
    for char in string.lower():
        if char not in seen:
            seen.append(char)
        else:
            return False

    return True