# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/python

def wave(people):
    res = []
    for i in range(len(people)):
        if people[i].isalpha():
            res.append(people[:i] + people[i].upper() + people[i+1::])
    return res
            

"""
* clever

def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]

"""
