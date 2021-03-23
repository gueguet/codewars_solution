# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python


def make_readable(seconds):
    seconds = seconds
    minutes = seconds // 60
    hours = minutes // 60

    return("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))

make_readable(86399)

"""
* clever
return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
"""