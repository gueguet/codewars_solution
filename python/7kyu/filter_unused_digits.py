# https://www.codewars.com/kata/55de6173a8fbe814ee000061/train/python

def unused_digits(*args):
    all_digits = "0123456789" 
    
    present_digits = ""
    not_present_digit = ""
    
    for int in args:
        for digit in str(int):
            present_digits += digit
    
    for digit in all_digits:
        if digit not in present_digits and digit not in not_present_digit:
            not_present_digit += digit
            
    return("".join(sorted(not_present_digit)))


unused_digits(12, 34, 56, 78)



"""
* clever

def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))
"""
