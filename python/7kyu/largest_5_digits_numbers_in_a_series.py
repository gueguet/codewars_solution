# https://www.codewars.com/kata/51675d17e0c1bed195000001/train/python

def solution(digits):

  max_seq = int(digits[0:5])

  for i in range(0,len(digits)-4):
    if int(digits[i:i+5]) > max_seq:
      max_seq = int(digits[i:i+5])

  return max_seq


solution("731674765")
