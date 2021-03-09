# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    list_reorder = sorted(list(str(num)), reverse=True)
    return int(''.join(list_reorder))

descending_order(42145)
