# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python

import re

def remove_url_anchor(url):
  match = re.match(r".+?(?=#)", url)
  if (match):
    return match[0]
  else:
    return url

remove_url_anchor("www.codewars.com/katas/?page=1#about")


"""
* Clever

return url.split('#')[0]
"""

