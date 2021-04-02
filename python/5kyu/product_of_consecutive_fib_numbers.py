# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python

# def fib(n):
#     if (n==0):
#         return 0
#     if (n==1):
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)


def productFib(prod):

    # create list of fib numbers
    fib_list = [0,1]
    for _ in range(1000):
        new_item = fib_list[-1] + fib_list[-2]
        fib_list.append(new_item)

    # loop
    idx = 0
    while (fib_list[idx] * fib_list[idx+1] <= prod):
        if (fib_list[idx] * fib_list[idx+1] == prod):
            return [fib_list[idx], fib_list[idx+1], True]
        idx += 1
    return [fib_list[idx],fib_list[idx+1], False]


productFib(4895)


"""
* No need need to calculate all members before the loop...
* Clever :
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]
"""