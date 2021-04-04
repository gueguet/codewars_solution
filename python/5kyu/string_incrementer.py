# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

def increment_string(strng):
    num = None
    idx = 0
    for char in strng:
        if not (char.isalpha()):
            num = strng[idx:]
            break
        idx += 1
    strng = strng[:idx]

    if num is None:
        return strng + str(1)
    else:
        int_num = int(num)

    if (len(str(int_num+1))) == len(num):
        return (strng + str(int_num+1))

    else:
        if (num.count('0') == len(num)):
            return (strng + '0' * (num.count('0')-1) + str((int_num+1)))
        else:
            return (strng + '0' * num.count('0') + str(int_num+1))

        return (strng + str(int_num+1))

# print(increment_string("foo"))
# print(increment_string("foobar00"))
# print(increment_string("foobar001"))
# print(increment_string("test099"))
# print(increment_string("test99"))

print(increment_string("foobar00999"))

