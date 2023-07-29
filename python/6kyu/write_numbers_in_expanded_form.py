# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

def expanded_form(num):
    res = []
    for digit in str(num):
        length = len(str(num))
        if (digit != "0"):
            res.append(digit + "0" * (length - 1))
            num = int(num) - int(digit + "0" * (length - 1))
    return " + ".join(res)
        
# * Clever 

# def expanded_form_2(num):
#     num = list(str(num))
#     return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')

print(expanded_form(70304))