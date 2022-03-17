# https://www.codewars.com/kata/5efae11e2d12df00331f91a6/train/python

import hashlib

def crack(hash):
  for i in range(100000):
      password = f"{i:05d}"
      if hashlib.md5(password.encode()).hexdigest() == hash:
        return password


"""
* clever

import hashlib
def crack(hash):
    for i in range(100000):
        if hashlib.md5(str(i).zfill(5).encode()).hexdigest() == hash:
            return str(i).zfill(5)

"""
