# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

import unittest

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j] == target):
                return [i, j]    


class Test(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([1234,5678,9012], 14690), [1,2])

if __name__ == "__main__":
    unittest.main()



"""
# * Clever
# * function uses a dictionary (d) to store previously encountered numbers and their indices
# * time complexity of O(n)

def two_sum(nums, target):
    d = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in d:
            return [d[diff], i]
        d[num] = i
"""