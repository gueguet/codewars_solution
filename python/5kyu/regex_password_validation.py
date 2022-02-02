# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python

import re
                 
regex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{6,}$"

# print(bool(re.search(regex, 'fjd3IR9')))
print(bool(re.search(regex, '7i!qogiPKkkS8Q')))


"""
* clever 

from re import compile, VERBOSE

regex = compile("""
^              # begin word
(?=.*?[a-z])   # at least one lowercase letter
(?=.*?[A-Z])   # at least one uppercase letter
(?=.*?[0-9])   # at least one number
[A-Za-z\d]     # only alphanumeric
{6,}           # at least 6 characters long
$              # end word
""", VERBOSE)    
"""
