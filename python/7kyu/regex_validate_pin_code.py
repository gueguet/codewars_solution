# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python

import re

def validate_pin(pin):
    if ('\n' in pin):
        return False
    if re.match(r"^\d{4}$",pin):
        return True
    elif re.match(r"^\d{6}$",pin):
        return True
    else:
        return False


print(validate_pin("1234"))
print(validate_pin("12345"))
print(validate_pin("123456"))
print(validate_pin("12345aaa6"))


"""
* Clever :
return len(pin) in (4, 6) and pin.isdigit()
return bool(re.fullmatch("\d{4}|\d{6}", pin))
"""
