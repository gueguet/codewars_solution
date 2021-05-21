# https://www.codewars.com/kata/573d498eb90ccf20a000002a/train/python

def decode(string):
    #your code here
    num_map = {
        "1":"9",
        "9":"1",
        "2":"8",
        "8":"2",
        "3":"7",
        "7":"3",
        "4":"6",
        "6":"4",
        "5":"0",
        "0":"5",
    }

    res = ""

    for char in string:
        res += num_map[char]

    return res


decode("4103432323")





