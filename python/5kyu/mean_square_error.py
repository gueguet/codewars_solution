# https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python


def solution(array_a, array_b):
    square_diff = [abs(x-y)**2 for x, y in zip(array_a, array_b)]
    return sum(square_diff)/len(square_diff)


a1 = [1, 2, 3]
a2 = [4, 5, 6]

(solution(a1, a2), 9)

"""
* clever

def solution(a, b):
    return sum((x - y)**2 for x, y in zip(a, b)) / len(a)

from sklearn.metrics import mean_squared_error as solution
"""
