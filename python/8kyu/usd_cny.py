# https://www.codewars.com/kata/5977618080ef220766000022/train/python

def usdcny(usd):
    res_chine = usd * 6.75
    return "{} Chinese Yuan".format(f"{res_chine:.2f}")


"""
* clever

def usdcny(usd):
    return f"{(usd * 6.75):.2f} Chinese Yuan"
"""
