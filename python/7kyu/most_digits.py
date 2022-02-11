def find_longest(arr):
    max = "0"
    for number in arr:
        if len(str(number)) > len(max):
            max = str(number)
    return int(max)

"""
* clever

def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))
"""
