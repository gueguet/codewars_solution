# https://www.codewars.com/kata/52e1476c8147a7547a000811/train/python

import re
                 
regex = "^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{6,}$"

# print(bool(re.search(regex, 'fjd3IR9')))
print(bool(re.search(regex, '7i!qogiPKkkS8Q')))
