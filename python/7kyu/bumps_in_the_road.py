# https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python

def bumps(road):
    count_bumps = road.count("n")
    if (count_bumps > 15):
        return 'Car Dead'
    else:
        return 'Woohoo!'
