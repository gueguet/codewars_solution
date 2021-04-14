# https://www.codewars.com/kata/5613d06cee1e7da6d5000055/train/python


def is_prime(n):
    if (n == 0 or n == 1):
        return False

    if (n == 2):
        return True

    if (n % 2 == 0):
        return False

    for i in range(3, int(n**0.5+1)):
        if (n % i == 0):
            return False

    return True


def step(g,m,n):
    if m >= n:
        return []
    else:
        for i in range(m,n+1-g):
            print(i)
            if is_prime(i) and is_prime(i+g):
                return[i,i+g]



# print(step(6,100,110))
print(step(10,300,400))

