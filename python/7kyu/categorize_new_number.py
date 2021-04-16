# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

def open_or_senior(data):
    res = []
    for (x,y) in data:
        if (x>=55 and y>7):
            res.append("Senior")
        else:
            res.append("Open")
    return res

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))