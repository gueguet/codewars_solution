# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n):
    persistence = 1

    if (len(str(n)) == 1):
        return 0

    else:
        counter = 0
        while(len(str(n)) > 1):
            counter += 1
            persistence = 1
            for digit in str(n):
                persistence = persistence * int(digit)
            n = persistence
        return counter

    return 0

persistence(39)

