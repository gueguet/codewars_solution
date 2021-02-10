# https://www.codewars.com/kata/57a03b8872292dd851000069/train/python

def nth_smallest(arr, n):

  arr = sorted(list(set(arr)))

  if (n > len(arr)):
    return None

  return arr[n-1]


if __name__ == "__main__":
  nth_smallest([45, -10, 4, 5, 4],4)