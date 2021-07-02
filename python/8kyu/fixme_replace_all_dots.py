# https://www.codewars.com/kata/596c6eb85b0f515834000049/train/python

import re
def replace_dots(str):
    return re.sub(r"\.", "-", str)
