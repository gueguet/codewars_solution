# https://www.codewars.com/kata/56efc695740d30f963000557/train/python

def to_alternating_case(string):
    res = ""

    for letter in string:
        if letter.isalpha():
            if (letter.isupper()):
                res += letter.lower()
            else:
                res += letter.upper()
        else:
            res += letter

    return res

