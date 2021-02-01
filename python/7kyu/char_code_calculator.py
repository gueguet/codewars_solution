# https://www.codewars.com/kata/57f75cc397d62fc93d000059/train/python

def calc(x):

    total1 = ""

    for char in x:
        total1 += str(ord(char))

    total2 = total1.replace("7","1")

    print(total2)
    print(total1)

    n = 0

    for i in range(len(total1)):
        n += int(total1[i]) - int(total2[i])

    return n


calc('aaaaaddddr')




