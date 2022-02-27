# https://www.codewars.com/kata/559f44187fa851efad000087/train/python

def seven_ate9(str_):
    res = str_[0]
    for i in range(1, len(str_) - 1):
        if str_[i-1] == "7" and str_[i+1] == "7" and str_[i] == "9":
            pass
        else:
            res += str_[i]
    res += str_[-1]
    return res
        
"""
* clever

def seven_ate9(str_):
   while str_.find('797') != -1:
       str_ = str_.replace('797','77')
   return str_
"""
