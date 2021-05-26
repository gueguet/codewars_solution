# https://www.codewars.com/kata/60a82776de1604000e29eb50/train/python

# def f(a, b):
  # len(a) if len(a) > b else 0


f=lambda a,b:(len(a),0)[len(a)>b]