# https://www.codewars.com/kata/55e6f5e58f7817808e00002e

from typing import Mapping


def seven(m):
  steps = 0

  while(len(str(m)) > 2):
    m = int(str(m)[0:-1]) - (int(str(m)[-1]) * 2)
    steps += 1

  return (m,steps)
  
  # your code 


if __name__ == "__main__":
  seven(1603)

