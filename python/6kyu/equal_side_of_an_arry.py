# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):
    idx = 0
    while (idx < len(arr)):
        left_sum = sum(arr[:idx])
        right_sum = sum(arr[idx+1:])
        if (left_sum == right_sum):
            return idx
        idx += 1
    return -1

print(find_even_index([-10,10]))